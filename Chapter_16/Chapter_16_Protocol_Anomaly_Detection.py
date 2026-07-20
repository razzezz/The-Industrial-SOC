#!/usr/bin/env python3
"""
Chapter 08 — Protocol Anomaly Detection for ICS Networks
================================================================
Description:
    Learns normal ICS protocol command sequences from Zeek protocol
    logs (Modbus, DNP3, S7Comm) and flags unusual command patterns
    using an LSTM neural network for sequence prediction.

    Complements Suricata signature rules (UC-ICS-005 through UC-ICS-007)
    by detecting novel or variant attack patterns that exact signatures
    would miss.

Usage:
    # Train model on baseline protocol data
    python Chapter_08_Protocol_Anomaly_Detection.py --mode train \
        --data zeek_ics_protocol_logs.csv \
        --asset-register ot_asset_register.csv \
        --output-model model_protocol_anomaly.keras

    # Score new data
    python Chapter_08_Protocol_Anomaly_Detection.py --mode score \
        --data recent_protocol_logs.csv \
        --asset-register ot_asset_register.csv \
        --model model_protocol_anomaly.keras \
        --output anomalies.csv

Data Format (zeek_ics_protocol_logs.csv):
    Export from Sentinel using the KQL query below.

    KQL Export Query:
    -----------------------------------------------
    _Im_NetworkSession(starttime=ago(90d))
    | where DstAppName in ("Modbus", "DNP3", "S7Comm", "EtherNet/IP")
    | join kind=inner (
        _GetWatchlist('OT_AssetRegister')
        | project DstIpAddr = IPAddress
    ) on DstIpAddr
    | project TimeGenerated, SrcIpAddr, DstIpAddr,
        DstAppName, DstPortNumber, NetworkProtocol,
        EventType, EventSubType, EventResult,
        AdditionalFields
    | sort by DstIpAddr asc, TimeGenerated asc

ATT&CK for ICS: T0814 (Denial of Service), T0840 (Network Sniffing),
    T0821 (Modify Controller Tasking), T0843 (Program Download)

Reference: Chapter 8 — Leveraging AI and Machine Learning
Dependencies: pandas, numpy, tensorflow, scikit-learn
    pip install pandas numpy tensorflow scikit-learn --break-system-packages

Note: This is the most technically complex use case in Chapter 8.
    It belongs in Phase 3 of the ML Maturity Roadmap and requires
    minimum 90 days of clean protocol data for effective training.
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
from sklearn.preprocessing import LabelEncoder

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


# ----------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------
SEQUENCE_LENGTH = 10          # Commands in each input sequence
EMBEDDING_DIM = 32            # Token embedding dimension
LSTM_UNITS = 64               # LSTM hidden units
EPOCHS = 20                   # Training epochs
BATCH_SIZE = 128              # Training batch size
ANOMALY_PERCENTILE = 5        # Bottom N% probability = anomaly
VALIDATION_SPLIT = 0.15       # Validation data proportion
MIN_SEQUENCES = 500           # Minimum sequences for training


# ----------------------------------------------------------------
# Data Loading and Tokenisation
# ----------------------------------------------------------------
def load_protocol_data(filepath: str) -> pd.DataFrame:
    """Load ICS protocol log data exported from Sentinel."""
    logger.info(f"Loading protocol data from {filepath}")
    df = pd.read_csv(filepath, parse_dates=["TimeGenerated"])
    required_cols = ["TimeGenerated", "SrcIpAddr", "DstIpAddr", "DstAppName"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    df = df.sort_values(["DstIpAddr", "TimeGenerated"])
    logger.info(f"Loaded {len(df):,} protocol events")
    return df


def tokenise_commands(data: pd.DataFrame) -> tuple:
    """
    Create tokens from protocol command features.

    Each unique combination of (Protocol, EventType, EventSubType,
    SrcIP→DstIP direction) becomes a token. This captures the
    "grammar" of ICS protocol usage.

    Returns:
        (token_sequences_by_asset, encoder, token_info)
    """
    logger.info("Tokenising protocol commands...")

    # Build composite token from available fields
    data = data.copy()
    data["EventType"] = data.get("EventType", pd.Series(["unknown"] * len(data)))
    data["EventSubType"] = data.get(
        "EventSubType", pd.Series(["unknown"] * len(data))
    )

    data["CommandToken"] = (
        data["DstAppName"].fillna("unknown").astype(str) + "|" +
        data["EventType"].fillna("unknown").astype(str) + "|" +
        data["EventSubType"].fillna("unknown").astype(str)
    )

    # Encode tokens as integers
    encoder = LabelEncoder()
    data["TokenID"] = encoder.fit_transform(data["CommandToken"])

    # Build token info for explainability
    token_info = {}
    for token_str, token_id in zip(
        encoder.classes_, encoder.transform(encoder.classes_)
    ):
        token_info[int(token_id)] = token_str

    # Group into sequences per destination asset (the controller)
    sequences_by_asset = {}
    for dst_ip, group in data.groupby("DstIpAddr"):
        tokens = group["TokenID"].values
        if len(tokens) >= SEQUENCE_LENGTH + 1:
            sequences_by_asset[dst_ip] = tokens

    logger.info(
        f"Created {len(encoder.classes_)} unique tokens across "
        f"{len(sequences_by_asset)} assets"
    )
    return sequences_by_asset, encoder, token_info


def create_training_sequences(
    sequences_by_asset: dict,
) -> tuple:
    """
    Create input/output pairs for LSTM training.

    For each sequence of tokens [t1, t2, ..., tn], create pairs:
        Input:  [t1, t2, ..., t_{n-1}]
        Output: t_n (the next expected token)

    Returns:
        (X, y) — input sequences and target tokens
    """
    X_sequences = []
    y_targets = []

    for asset_ip, tokens in sequences_by_asset.items():
        for i in range(len(tokens) - SEQUENCE_LENGTH):
            X_sequences.append(tokens[i:i + SEQUENCE_LENGTH])
            y_targets.append(tokens[i + SEQUENCE_LENGTH])

    X = np.array(X_sequences)
    y = np.array(y_targets)
    logger.info(f"Created {len(X):,} training sequences")
    return X, y


# ----------------------------------------------------------------
# LSTM Model
# ----------------------------------------------------------------
def build_model(vocab_size: int) -> "tensorflow.keras.Model":
    """Build the LSTM sequence prediction model."""
    import tensorflow as tf
    from tensorflow.keras import layers, models

    model = models.Sequential([
        layers.Embedding(
            input_dim=vocab_size + 1,
            output_dim=EMBEDDING_DIM,
            input_length=SEQUENCE_LENGTH,
        ),
        layers.LSTM(LSTM_UNITS, return_sequences=False),
        layers.Dropout(0.2),
        layers.Dense(vocab_size, activation="softmax"),
    ])

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    logger.info(f"Model built: vocab_size={vocab_size}, params={model.count_params()}")
    return model


def train_model(
    X: np.ndarray,
    y: np.ndarray,
    vocab_size: int,
) -> tuple:
    """
    Train the LSTM model and determine the anomaly threshold.

    Returns:
        (model, threshold) — trained model and probability threshold
    """
    import tensorflow as tf

    if len(X) < MIN_SEQUENCES:
        raise ValueError(
            f"Insufficient training sequences ({len(X)} < {MIN_SEQUENCES}). "
            f"Need more protocol data — minimum 90 days recommended."
        )

    model = build_model(vocab_size)

    logger.info(f"Training LSTM ({EPOCHS} epochs, {len(X):,} sequences)...")
    history = model.fit(
        X, y,
        epochs=EPOCHS,
        batch_size=BATCH_SIZE,
        validation_split=VALIDATION_SPLIT,
        verbose=1,
    )

    # Determine anomaly threshold from training data probabilities
    logger.info("Calculating anomaly threshold from training data...")
    predictions = model.predict(X, batch_size=BATCH_SIZE, verbose=0)
    actual_probs = np.array([
        predictions[i, y[i]] for i in range(len(y))
    ])
    threshold = np.percentile(actual_probs, ANOMALY_PERCENTILE)

    logger.info(
        f"Training complete. Final accuracy: "
        f"{history.history['accuracy'][-1]:.4f}. "
        f"Anomaly threshold (p{ANOMALY_PERCENTILE}): {threshold:.6f}"
    )
    return model, threshold


def save_training_artifacts(
    model,
    encoder: LabelEncoder,
    token_info: dict,
    threshold: float,
    model_path: str,
):
    """Save model and supporting artifacts."""
    model.save(model_path)
    metadata = {
        "encoder": encoder,
        "token_info": token_info,
        "threshold": threshold,
        "sequence_length": SEQUENCE_LENGTH,
        "trained_at": datetime.utcnow().isoformat() + "Z",
        "model_version": "protocol_anomaly_v1.0.0",
        "vocab_size": len(encoder.classes_),
    }
    meta_path = model_path.replace(".keras", "_metadata.pkl")
    with open(meta_path, "wb") as f:
        pickle.dump(metadata, f)
    logger.info(f"Model saved to {model_path}, metadata to {meta_path}")


def load_training_artifacts(model_path: str) -> tuple:
    """Load model and supporting artifacts."""
    import tensorflow as tf
    model = tf.keras.models.load_model(model_path)
    meta_path = model_path.replace(".keras", "_metadata.pkl")
    with open(meta_path, "rb") as f:
        metadata = pickle.load(f)
    logger.info(
        f"Model loaded (version {metadata['model_version']}, "
        f"trained {metadata['trained_at']}, "
        f"vocab {metadata['vocab_size']} tokens)"
    )
    return model, metadata


# ----------------------------------------------------------------
# Anomaly Scoring
# ----------------------------------------------------------------
def score_sequences(
    data: pd.DataFrame,
    model,
    metadata: dict,
    asset_register: pd.DataFrame,
) -> pd.DataFrame:
    """
    Score new protocol data against the trained model.

    For each sequence, the model predicts the probability of the
    next observed command. Low-probability commands (below threshold)
    are flagged as anomalous.
    """
    encoder = metadata["encoder"]
    threshold = metadata["threshold"]
    token_info = metadata["token_info"]

    # Tokenise new data using the fitted encoder
    data = data.copy()
    data["EventType"] = data.get("EventType", pd.Series(["unknown"] * len(data)))
    data["EventSubType"] = data.get(
        "EventSubType", pd.Series(["unknown"] * len(data))
    )
    data["CommandToken"] = (
        data["DstAppName"].fillna("unknown").astype(str) + "|" +
        data["EventType"].fillna("unknown").astype(str) + "|" +
        data["EventSubType"].fillna("unknown").astype(str)
    )

    # Handle unseen tokens (assign to a special "unknown" bucket)
    known_tokens = set(encoder.classes_)
    data["CommandToken_Clean"] = data["CommandToken"].apply(
        lambda x: x if x in known_tokens else "UNSEEN_TOKEN"
    )

    # Flag completely unseen tokens as automatic anomalies
    unseen_mask = data["CommandToken_Clean"] == "UNSEEN_TOKEN"
    if unseen_mask.sum() > 0:
        logger.warning(
            f"{unseen_mask.sum()} events with unseen protocol commands — "
            f"flagged as automatic anomalies"
        )

    anomalies = []

    for dst_ip, group in data.groupby("DstIpAddr"):
        group = group.sort_values("TimeGenerated")
        known_group = group[~unseen_mask.loc[group.index]]

        if len(known_group) < SEQUENCE_LENGTH + 1:
            continue

        # Encode tokens
        tokens = encoder.transform(known_group["CommandToken_Clean"].values)

        # Create sequences and score
        for i in range(len(tokens) - SEQUENCE_LENGTH):
            seq = tokens[i:i + SEQUENCE_LENGTH].reshape(1, -1)
            actual_next = tokens[i + SEQUENCE_LENGTH]
            row_idx = known_group.index[i + SEQUENCE_LENGTH]

            pred_probs = model.predict(seq, verbose=0)[0]
            actual_prob = pred_probs[actual_next]

            if actual_prob < threshold:
                # This command was unexpected given the preceding sequence
                context_tokens = [
                    token_info.get(int(t), "?") for t in tokens[i:i + SEQUENCE_LENGTH]
                ]
                anomalies.append({
                    "Timestamp": group.loc[row_idx, "TimeGenerated"],
                    "AssetIP": dst_ip,
                    "SrcIP": group.loc[row_idx, "SrcIpAddr"],
                    "Protocol": group.loc[row_idx, "DstAppName"],
                    "ObservedCommand": token_info.get(int(actual_next), "unknown"),
                    "CommandProbability": float(actual_prob),
                    "Threshold": float(threshold),
                    "PrecedingSequence": " → ".join(context_tokens[-5:]),
                    "AnomalySeverity": float(
                        np.clip(1.0 - (actual_prob / threshold), 0.0, 1.0)
                    ),
                    "DetectionMethod": "LSTM_SequenceAnalysis",
                })

        # Add unseen token anomalies for this asset
        unseen_group = group[unseen_mask.loc[group.index]]
        for idx, row in unseen_group.iterrows():
            anomalies.append({
                "Timestamp": row["TimeGenerated"],
                "AssetIP": dst_ip,
                "SrcIP": row["SrcIpAddr"],
                "Protocol": row["DstAppName"],
                "ObservedCommand": row["CommandToken"],
                "CommandProbability": 0.0,
                "Threshold": float(threshold),
                "PrecedingSequence": "N/A (unseen token)",
                "AnomalySeverity": 1.0,
                "DetectionMethod": "UnseenToken",
            })

    anomalies_df = pd.DataFrame(anomalies)

    if not anomalies_df.empty:
        # Enrich with asset register
        anomalies_df = _enrich_anomalies(anomalies_df, asset_register)

    logger.info(f"Detected {len(anomalies_df)} protocol anomalies")
    return anomalies_df


def _enrich_anomalies(
    anomalies: pd.DataFrame,
    asset_register: pd.DataFrame,
) -> pd.DataFrame:
    """Enrich anomalies with OT Asset Register context."""
    if "IPAddress" in asset_register.columns:
        enrichment = asset_register.rename(columns={"IPAddress": "AssetIP"})
        enrich_cols = ["AssetIP"]
        for col in ["Hostname", "PurdueLevel", "DeviceType",
                     "CrownJewelTier", "EngineeringOwner"]:
            if col in enrichment.columns:
                enrich_cols.append(col)
        anomalies = anomalies.merge(
            enrichment[enrich_cols].drop_duplicates(),
            on="AssetIP", how="left",
        )
    return anomalies


def format_for_sentinel(anomalies: pd.DataFrame) -> list[dict]:
    """Format for Sentinel OT_ML_Anomalies_CL table."""
    records = []
    for _, row in anomalies.iterrows():
        record = {
            "TimeGenerated": str(row.get("Timestamp", datetime.utcnow().isoformat())),
            "AnomalyType": "ProtocolAnomaly",
            "AssetIdentifier": row["AssetIP"],
            "AnomalyScore": round(float(row["AnomalySeverity"]), 4),
            "AnomalyDescription": (
                f"Unexpected {row['Protocol']} command to {row['AssetIP']}"
                f" ({row.get('Hostname', 'unknown')})"
                f" from {row['SrcIP']}."
                f" Command: {row['ObservedCommand']}"
                f" (probability: {row['CommandProbability']:.4f},"
                f" threshold: {row['Threshold']:.4f})."
                f" Preceding: {row['PrecedingSequence']}."
            ),
            "BaselineReference": "90-day protocol command sequence model",
            "ObservedBehaviour": json.dumps({
                "protocol": row["Protocol"],
                "command": row["ObservedCommand"],
                "probability": round(float(row["CommandProbability"]), 6),
                "source_ip": row["SrcIP"],
                "detection_method": row["DetectionMethod"],
            }),
            "ModelVersion": "protocol_anomaly_lstm_v1.0.0",
        }
        for field in ["Hostname", "PurdueLevel", "DeviceType",
                      "CrownJewelTier", "EngineeringOwner"]:
            if field in row and pd.notna(row[field]):
                record[field] = str(row[field])
        records.append(record)
    return records


# ----------------------------------------------------------------
# Main
# ----------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="OT Protocol Anomaly Detection — Chapter 8",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--mode", choices=["train", "score"], required=True,
    )
    parser.add_argument("--data", required=True, help="Protocol log CSV")
    parser.add_argument("--asset-register", required=True, help="Asset register CSV")
    parser.add_argument(
        "--model", default="model_protocol_anomaly.keras",
        help="Model path (output for train, input for score)",
    )
    parser.add_argument(
        "--output-model", default=None, help="Override model output path",
    )
    parser.add_argument(
        "--output", default="anomalies_protocol.csv", help="Anomaly output CSV",
    )
    parser.add_argument(
        "--sentinel-output", default=None, help="Sentinel JSON output",
    )

    args = parser.parse_args()

    data = load_protocol_data(args.data)
    asset_register = pd.read_csv(args.asset_register)

    if args.mode == "train":
        sequences_by_asset, encoder, token_info = tokenise_commands(data)
        X, y = create_training_sequences(sequences_by_asset)
        vocab_size = len(encoder.classes_)
        model, threshold = train_model(X, y, vocab_size)
        model_path = args.output_model or args.model
        save_training_artifacts(model, encoder, token_info, threshold, model_path)
        logger.info("Training complete.")

    elif args.mode == "score":
        model, metadata = load_training_artifacts(args.model)
        anomalies = score_sequences(data, model, metadata, asset_register)

        if len(anomalies) > 0:
            anomalies.to_csv(args.output, index=False)
            logger.info(f"Anomalies written to {args.output}")
            if args.sentinel_output:
                records = format_for_sentinel(anomalies)
                with open(args.sentinel_output, "w") as f:
                    json.dump(records, f, indent=2)
                logger.info(f"Sentinel output written to {args.sentinel_output}")
        else:
            logger.info("No protocol anomalies detected.")

    logger.info("Done.")


if __name__ == "__main__":
    main()
