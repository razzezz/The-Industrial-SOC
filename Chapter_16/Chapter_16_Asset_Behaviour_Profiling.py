#!/usr/bin/env python3
"""
Chapter 08 — Asset Behaviour Profiling for OT Networks
================================================================
Description:
    Builds a communication graph of OT assets from ASIM-normalised
    network session data exported from Microsoft Sentinel, trains an
    Isolation Forest model to learn normal device behaviour, and
    identifies devices exhibiting anomalous communication patterns.

Usage:
    # Phase 1 — Build baseline and train model
    python Chapter_08_Asset_Behaviour_Profiling.py --mode train \
        --data baseline_network_sessions.csv \
        --asset-register ot_asset_register.csv \
        --output-model model_asset_behaviour.pkl

    # Phase 2 — Score new data against trained model
    python Chapter_08_Asset_Behaviour_Profiling.py --mode score \
        --data recent_network_sessions.csv \
        --asset-register ot_asset_register.csv \
        --model model_asset_behaviour.pkl \
        --output anomalies.csv

Data Requirements:
    Network session data: Export from Sentinel using the KQL query below.
    Asset register: Export of OT_AssetRegister watchlist as CSV.

    KQL Export Query (run in Sentinel > Logs):
    -----------------------------------------------
    _Im_NetworkSession(starttime=ago(30d))
    | join kind=inner (
        _GetWatchlist('OT_AssetRegister')
        | project DstIpAddr = IPAddress, DstHostname = Hostname,
            DstPurdueLevel = PurdueLevel, DstDeviceType = DeviceType,
            DstCrownJewelTier = CrownJewelTier
    ) on DstIpAddr
    | project TimeGenerated, SrcIpAddr, DstIpAddr, DstHostname,
        DstPurdueLevel, DstDeviceType, DstCrownJewelTier,
        NetworkProtocol, DstPortNumber, DstAppName,
        NetworkBytes, NetworkDirection

ATT&CK for ICS: T0886 (Remote Services), T0822 (Unauthorized Command
    Message), T0846 (Remote System Discovery)

Reference: Chapter 8 — Leveraging AI and Machine Learning
Dependencies: pandas, networkx, scikit-learn, numpy
    pip install pandas networkx scikit-learn numpy --break-system-packages
================================================================
"""

import argparse
import json
import logging
import os
import pickle
from datetime import datetime

import numpy as np
import pandas as pd
import networkx as nx
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# ----------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------
ANOMALY_CONTAMINATION = 0.05  # Expected proportion of anomalies (5%)
RANDOM_STATE = 42
MIN_SESSIONS_FOR_BASELINE = 10  # Minimum sessions to include a device

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


# ----------------------------------------------------------------
# Data Loading
# ----------------------------------------------------------------
def load_network_sessions(filepath: str) -> pd.DataFrame:
    """Load ASIM-normalised network session data exported from Sentinel."""
    logger.info(f"Loading network session data from {filepath}")
    df = pd.read_csv(filepath, parse_dates=["TimeGenerated"])
    required_cols = [
        "TimeGenerated", "SrcIpAddr", "DstIpAddr",
        "NetworkProtocol", "DstPortNumber",
    ]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    logger.info(f"Loaded {len(df):,} network sessions")
    return df


def load_asset_register(filepath: str) -> pd.DataFrame:
    """Load OT Asset Register watchlist export."""
    logger.info(f"Loading asset register from {filepath}")
    df = pd.read_csv(filepath)
    logger.info(f"Loaded {len(df):,} asset records")
    return df


# ----------------------------------------------------------------
# Communication Graph Construction
# ----------------------------------------------------------------
def build_communication_graph(sessions: pd.DataFrame) -> nx.DiGraph:
    """
    Build a directed communication graph from network session data.

    Nodes represent devices (IP addresses).
    Edges represent communication paths, annotated with:
        - session_count: total sessions observed
        - protocols: set of protocols used
        - ports: set of destination ports
        - avg_bytes: average bytes per session
        - first_seen / last_seen: temporal bounds
        - hour_distribution: sessions per hour of day (24-element list)
    """
    logger.info("Building communication graph...")
    G = nx.DiGraph()

    # Aggregate edge features
    edge_data = sessions.groupby(["SrcIpAddr", "DstIpAddr"]).agg(
        session_count=("TimeGenerated", "count"),
        protocols=("NetworkProtocol", lambda x: list(x.dropna().unique())),
        ports=("DstPortNumber", lambda x: list(x.dropna().unique())),
        avg_bytes=("NetworkBytes", "mean"),
        first_seen=("TimeGenerated", "min"),
        last_seen=("TimeGenerated", "max"),
    ).reset_index()

    # Compute hour-of-day distribution per edge
    sessions["Hour"] = sessions["TimeGenerated"].dt.hour
    hour_dist = (
        sessions.groupby(["SrcIpAddr", "DstIpAddr", "Hour"])
        .size()
        .reset_index(name="count")
    )

    for _, row in edge_data.iterrows():
        src, dst = row["SrcIpAddr"], row["DstIpAddr"]
        G.add_node(src)
        G.add_node(dst)

        # Build hour distribution (24 bins)
        mask = (hour_dist["SrcIpAddr"] == src) & (hour_dist["DstIpAddr"] == dst)
        h_dist = [0] * 24
        for _, h_row in hour_dist[mask].iterrows():
            h_dist[int(h_row["Hour"])] = int(h_row["count"])

        G.add_edge(
            src, dst,
            session_count=int(row["session_count"]),
            protocols=row["protocols"],
            ports=row["ports"],
            avg_bytes=float(row["avg_bytes"]) if pd.notna(row["avg_bytes"]) else 0.0,
            first_seen=str(row["first_seen"]),
            last_seen=str(row["last_seen"]),
            hour_distribution=h_dist,
        )

    logger.info(
        f"Communication graph: {G.number_of_nodes()} nodes, "
        f"{G.number_of_edges()} edges"
    )
    return G


# ----------------------------------------------------------------
# Feature Extraction
# ----------------------------------------------------------------
def extract_device_features(G: nx.DiGraph) -> pd.DataFrame:
    """
    Extract a feature vector for each device in the communication graph.

    Features capture the communication profile of each device:
        - out_degree: number of outbound communication partners
        - in_degree: number of inbound communication partners
        - total_sessions_out: total outbound sessions
        - total_sessions_in: total inbound sessions
        - unique_protocols_out: number of distinct outbound protocols
        - unique_ports_out: number of distinct outbound destination ports
        - avg_bytes_out: average outbound bytes per session
        - communication_regularity: std dev of hour distribution (lower = more regular)
        - business_hours_ratio: proportion of sessions during 06:00-18:00
        - peer_diversity: ratio of unique peers to total sessions
    """
    logger.info("Extracting device features...")
    features = []

    for node in G.nodes():
        # Outbound edges
        out_edges = G.out_edges(node, data=True)
        out_data = [d for _, _, d in out_edges]
        # Inbound edges
        in_edges = G.in_edges(node, data=True)
        in_data = [d for _, _, d in in_edges]

        total_out = sum(d["session_count"] for d in out_data) if out_data else 0
        total_in = sum(d["session_count"] for d in in_data) if in_data else 0

        if (total_out + total_in) < MIN_SESSIONS_FOR_BASELINE:
            continue

        # Protocol and port diversity (outbound)
        all_protocols_out = set()
        all_ports_out = set()
        for d in out_data:
            all_protocols_out.update(d.get("protocols", []))
            all_ports_out.update(d.get("ports", []))

        # Hour distribution (combined in/out)
        combined_hours = [0] * 24
        for d in out_data + in_data:
            for i, count in enumerate(d.get("hour_distribution", [0] * 24)):
                combined_hours[i] += count

        total_sessions = sum(combined_hours)
        business_hours = sum(combined_hours[6:18])
        business_hours_ratio = (
            business_hours / total_sessions if total_sessions > 0 else 0.0
        )
        hour_std = float(np.std(combined_hours)) if total_sessions > 0 else 0.0

        # Average bytes (outbound)
        avg_bytes_out = (
            np.mean([d["avg_bytes"] for d in out_data]) if out_data else 0.0
        )

        # Peer diversity
        total_peers = G.out_degree(node) + G.in_degree(node)
        peer_diversity = (
            total_peers / (total_out + total_in) if (total_out + total_in) > 0 else 0.0
        )

        features.append({
            "device_ip": node,
            "out_degree": G.out_degree(node),
            "in_degree": G.in_degree(node),
            "total_sessions_out": total_out,
            "total_sessions_in": total_in,
            "unique_protocols_out": len(all_protocols_out),
            "unique_ports_out": len(all_ports_out),
            "avg_bytes_out": avg_bytes_out,
            "communication_regularity": hour_std,
            "business_hours_ratio": business_hours_ratio,
            "peer_diversity": peer_diversity,
        })

    df = pd.DataFrame(features)
    logger.info(f"Extracted features for {len(df)} devices")
    return df


# ----------------------------------------------------------------
# Model Training
# ----------------------------------------------------------------
FEATURE_COLUMNS = [
    "out_degree", "in_degree", "total_sessions_out", "total_sessions_in",
    "unique_protocols_out", "unique_ports_out", "avg_bytes_out",
    "communication_regularity", "business_hours_ratio", "peer_diversity",
]


def train_model(features: pd.DataFrame) -> tuple:
    """
    Train an Isolation Forest model on device features.

    Returns:
        (model, scaler) — trained IsolationForest and fitted StandardScaler
    """
    logger.info("Training Isolation Forest model...")
    X = features[FEATURE_COLUMNS].fillna(0).values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = IsolationForest(
        contamination=ANOMALY_CONTAMINATION,
        random_state=RANDOM_STATE,
        n_estimators=200,
        max_samples="auto",
    )
    model.fit(X_scaled)

    # Score training data for baseline
    scores = model.decision_function(X_scaled)
    predictions = model.predict(X_scaled)
    n_anomalies = (predictions == -1).sum()

    logger.info(
        f"Model trained. Baseline anomalies: {n_anomalies}/{len(features)} "
        f"({n_anomalies / len(features) * 100:.1f}%)"
    )
    logger.info(
        f"Score range: [{scores.min():.4f}, {scores.max():.4f}], "
        f"threshold ≈ {np.percentile(scores, ANOMALY_CONTAMINATION * 100):.4f}"
    )

    return model, scaler


def save_model(model, scaler, features, filepath: str):
    """Save trained model, scaler, and baseline features."""
    artifact = {
        "model": model,
        "scaler": scaler,
        "baseline_features": features,
        "feature_columns": FEATURE_COLUMNS,
        "trained_at": datetime.utcnow().isoformat() + "Z",
        "model_version": "1.0.0",
        "contamination": ANOMALY_CONTAMINATION,
        "device_count": len(features),
    }
    with open(filepath, "wb") as f:
        pickle.dump(artifact, f)
    logger.info(f"Model saved to {filepath}")


def load_model(filepath: str) -> tuple:
    """Load trained model, scaler, and metadata."""
    with open(filepath, "rb") as f:
        artifact = pickle.load(f)
    logger.info(
        f"Model loaded (version {artifact['model_version']}, "
        f"trained {artifact['trained_at']}, "
        f"{artifact['device_count']} baseline devices)"
    )
    return artifact["model"], artifact["scaler"], artifact


# ----------------------------------------------------------------
# Anomaly Scoring
# ----------------------------------------------------------------
def score_devices(
    features: pd.DataFrame,
    model: IsolationForest,
    scaler: StandardScaler,
    asset_register: pd.DataFrame,
) -> pd.DataFrame:
    """
    Score device features against the trained model.

    Returns a DataFrame of anomalies enriched with asset register context.
    """
    logger.info("Scoring devices against model...")
    X = features[FEATURE_COLUMNS].fillna(0).values
    X_scaled = scaler.transform(X)

    scores = model.decision_function(X_scaled)
    predictions = model.predict(X_scaled)

    results = features.copy()
    results["anomaly_score"] = -scores  # Invert so higher = more anomalous
    results["is_anomaly"] = predictions == -1

    # Normalise anomaly scores to 0.0–1.0
    min_score = results["anomaly_score"].min()
    max_score = results["anomaly_score"].max()
    if max_score > min_score:
        results["anomaly_score_normalised"] = (
            (results["anomaly_score"] - min_score) / (max_score - min_score)
        )
    else:
        results["anomaly_score_normalised"] = 0.0

    # Enrich with asset register context
    if "IPAddress" in asset_register.columns:
        enrichment = asset_register.rename(columns={"IPAddress": "device_ip"})
        enrich_cols = ["device_ip"]
        for col in ["Hostname", "PurdueLevel", "DeviceType", "CrownJewelTier",
                     "EngineeringOwner", "ProcessFunction"]:
            if col in enrichment.columns:
                enrich_cols.append(col)
        results = results.merge(
            enrichment[enrich_cols], on="device_ip", how="left"
        )

    anomalies = results[results["is_anomaly"]].sort_values(
        "anomaly_score_normalised", ascending=False
    )
    logger.info(f"Identified {len(anomalies)} anomalous devices")
    return anomalies


def format_for_sentinel(anomalies: pd.DataFrame) -> list[dict]:
    """
    Format anomaly results for ingestion into the Sentinel
    OT_ML_Anomalies_CL custom table via the Log Analytics API.
    """
    records = []
    for _, row in anomalies.iterrows():
        record = {
            "TimeGenerated": datetime.utcnow().isoformat() + "Z",
            "AnomalyType": "AssetBehaviour",
            "AssetIdentifier": row["device_ip"],
            "AnomalyScore": round(float(row["anomaly_score_normalised"]), 4),
            "AnomalyDescription": _build_description(row),
            "BaselineReference": "30-day communication profile",
            "ObservedBehaviour": json.dumps({
                "out_degree": int(row.get("out_degree", 0)),
                "in_degree": int(row.get("in_degree", 0)),
                "unique_protocols": int(row.get("unique_protocols_out", 0)),
                "business_hours_ratio": round(
                    float(row.get("business_hours_ratio", 0)), 2
                ),
            }),
            "ModelVersion": "asset_behaviour_v1.0.0",
            "Features": json.dumps(
                {col: float(row[col]) for col in FEATURE_COLUMNS if col in row}
            ),
        }
        # Add enrichment fields if available
        for field in ["Hostname", "PurdueLevel", "DeviceType",
                      "CrownJewelTier", "EngineeringOwner"]:
            if field in row and pd.notna(row[field]):
                record[field] = str(row[field])
        records.append(record)
    return records


def _build_description(row: pd.Series) -> str:
    """Build a human-readable anomaly description."""
    parts = [f"Device {row['device_ip']}"]
    if "Hostname" in row and pd.notna(row["Hostname"]):
        parts[0] += f" ({row['Hostname']})"
    parts.append("exhibits anomalous communication behaviour.")

    details = []
    if row.get("out_degree", 0) > 10:
        details.append(f"high outbound peer count ({int(row['out_degree'])})")
    if row.get("business_hours_ratio", 1) < 0.3:
        details.append("significant off-hours activity")
    if row.get("unique_protocols_out", 0) > 5:
        details.append(f"high protocol diversity ({int(row['unique_protocols_out'])})")
    if row.get("peer_diversity", 0) > 0.5:
        details.append("unusual peer diversity ratio")

    if details:
        parts.append("Notable: " + "; ".join(details) + ".")
    if "CrownJewelTier" in row and pd.notna(row["CrownJewelTier"]):
        parts.append(f"Crown Jewel Tier: {row['CrownJewelTier']}.")

    return " ".join(parts)


# ----------------------------------------------------------------
# Main
# ----------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="OT Asset Behaviour Profiling — Chapter 8",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--mode", choices=["train", "score"], required=True,
        help="'train' to build baseline model, 'score' to detect anomalies",
    )
    parser.add_argument(
        "--data", required=True,
        help="Path to ASIM network session CSV export",
    )
    parser.add_argument(
        "--asset-register", required=True,
        help="Path to OT_AssetRegister watchlist CSV export",
    )
    parser.add_argument(
        "--model", default="model_asset_behaviour.pkl",
        help="Path to model file (output for train, input for score)",
    )
    parser.add_argument(
        "--output-model", default=None,
        help="Override model output path (train mode only)",
    )
    parser.add_argument(
        "--output", default="anomalies_asset_behaviour.csv",
        help="Path for anomaly output CSV (score mode)",
    )
    parser.add_argument(
        "--sentinel-output", default=None,
        help="Path for Sentinel-formatted JSON output (score mode)",
    )

    args = parser.parse_args()

    sessions = load_network_sessions(args.data)
    asset_register = load_asset_register(args.asset_register)

    G = build_communication_graph(sessions)
    features = extract_device_features(G)

    if args.mode == "train":
        model, scaler = train_model(features)
        model_path = args.output_model or args.model
        save_model(model, scaler, features, model_path)
        logger.info("Training complete.")

    elif args.mode == "score":
        model, scaler, metadata = load_model(args.model)
        anomalies = score_devices(features, model, scaler, asset_register)

        if len(anomalies) > 0:
            anomalies.to_csv(args.output, index=False)
            logger.info(f"Anomalies written to {args.output}")

            if args.sentinel_output:
                sentinel_records = format_for_sentinel(anomalies)
                with open(args.sentinel_output, "w") as f:
                    json.dump(sentinel_records, f, indent=2)
                logger.info(
                    f"Sentinel-formatted output written to {args.sentinel_output}"
                )
        else:
            logger.info("No anomalies detected.")

    logger.info("Done.")


if __name__ == "__main__":
    main()
