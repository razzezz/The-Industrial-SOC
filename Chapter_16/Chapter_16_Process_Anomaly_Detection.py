#!/usr/bin/env python3
"""
Chapter 08 — Process Anomaly Detection for OT Environments
================================================================
Description:
    Monitors process historian data (temperature, pressure, flow rate,
    level, pH, etc.) for statistical anomalies using ARIMA for
    short-term deviation detection and Facebook Prophet for long-term
    trend analysis with seasonal decomposition.

    Detects both sudden deviations (potential cyberattack or equipment
    failure) and gradual drifts (potential slow manipulation or
    degradation) that fall below alarm thresholds.

Usage:
    # Analyse a single process variable
    python Chapter_08_Process_Anomaly_Detection.py \
        --data historian_export.csv \
        --asset-register ot_asset_register.csv \
        --variable Temperature \
        --asset-ip 10.1.2.10 \
        --output anomalies.csv

    # Batch mode — analyse all variables for all assets in a directory
    python Chapter_08_Process_Anomaly_Detection.py \
        --batch-dir ./historian_exports/ \
        --asset-register ot_asset_register.csv \
        --output anomalies_all.csv

Data Format (historian_export.csv):
    Timestamp,AssetIP,Variable,Value
    2026-01-01T00:00:00Z,10.1.2.10,Temperature,74.2
    2026-01-01T00:01:00Z,10.1.2.10,Temperature,74.3
    ...

ATT&CK for ICS: T0836 (Modify Parameter), T0831 (Manipulation of Control),
    T0855 (Unauthorized Command Message)

Reference: Chapter 8 — Leveraging AI and Machine Learning
Dependencies: pandas, numpy, statsmodels, prophet
    pip install pandas numpy statsmodels prophet --break-system-packages
================================================================
"""

import argparse
import json
import logging
import os
import warnings
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd

# Suppress convergence warnings from statsmodels during batch processing
warnings.filterwarnings("ignore", category=UserWarning)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


# ----------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------
# ARIMA configuration
ARIMA_ORDER = (5, 1, 0)  # (p, d, q) — sensible default for process data
ARIMA_ANOMALY_THRESHOLD_SIGMA = 3.0  # Std deviations for anomaly flag

# Prophet configuration
PROPHET_INTERVAL_WIDTH = 0.95  # 95% prediction interval
PROPHET_CHANGEPOINT_SCALE = 0.05  # Sensitivity to trend changes

# General
MIN_DATA_POINTS = 100  # Minimum data points for model training
RESAMPLE_INTERVAL = "5min"  # Resample interval for irregular data


# ----------------------------------------------------------------
# Data Loading
# ----------------------------------------------------------------
def load_historian_data(filepath: str) -> pd.DataFrame:
    """Load process historian data from CSV."""
    logger.info(f"Loading historian data from {filepath}")
    df = pd.read_csv(filepath, parse_dates=["Timestamp"])
    required_cols = ["Timestamp", "AssetIP", "Variable", "Value"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    df["Value"] = pd.to_numeric(df["Value"], errors="coerce")
    df = df.dropna(subset=["Value"])
    logger.info(f"Loaded {len(df):,} data points")
    return df


def load_asset_register(filepath: str) -> pd.DataFrame:
    """Load OT Asset Register watchlist export."""
    logger.info(f"Loading asset register from {filepath}")
    return pd.read_csv(filepath)


# ----------------------------------------------------------------
# ARIMA-Based Short-Term Anomaly Detection
# ----------------------------------------------------------------
def detect_arima_anomalies(
    series: pd.Series,
    asset_ip: str,
    variable: str,
    threshold_sigma: float = ARIMA_ANOMALY_THRESHOLD_SIGMA,
) -> pd.DataFrame:
    """
    Use ARIMA to model expected values and flag residuals that exceed
    the threshold. Detects sudden deviations from expected patterns.

    Args:
        series: Time-indexed pandas Series of process values
        asset_ip: IP address of the asset for output context
        variable: Name of the process variable
        threshold_sigma: Number of std deviations for anomaly threshold

    Returns:
        DataFrame of detected anomalies with context
    """
    from statsmodels.tsa.arima.model import ARIMA

    if len(series) < MIN_DATA_POINTS:
        logger.warning(
            f"Insufficient data for ARIMA ({len(series)} < {MIN_DATA_POINTS}). "
            f"Skipping {asset_ip}/{variable}."
        )
        return pd.DataFrame()

    logger.info(
        f"Running ARIMA anomaly detection: {asset_ip}/{variable} "
        f"({len(series)} points)"
    )

    try:
        # Fit ARIMA model
        model = ARIMA(series, order=ARIMA_ORDER)
        fitted = model.fit()

        # Calculate residuals
        residuals = fitted.resid
        residual_mean = residuals.mean()
        residual_std = residuals.std()

        if residual_std == 0:
            logger.warning(f"Zero residual variance for {asset_ip}/{variable}")
            return pd.DataFrame()

        # Identify anomalies: residuals beyond threshold
        z_scores = (residuals - residual_mean) / residual_std
        anomaly_mask = abs(z_scores) > threshold_sigma

        if anomaly_mask.sum() == 0:
            logger.info(f"No ARIMA anomalies detected for {asset_ip}/{variable}")
            return pd.DataFrame()

        anomalies = pd.DataFrame({
            "Timestamp": series.index[anomaly_mask],
            "AssetIP": asset_ip,
            "Variable": variable,
            "ObservedValue": series[anomaly_mask].values,
            "ExpectedValue": fitted.fittedvalues[anomaly_mask].values,
            "Residual": residuals[anomaly_mask].values,
            "ZScore": z_scores[anomaly_mask].values,
            "DetectionMethod": "ARIMA",
            "AnomalyType": np.where(
                z_scores[anomaly_mask] > 0, "HighDeviation", "LowDeviation"
            ),
        })

        # Calculate anomaly severity (0.0–1.0 based on z-score magnitude)
        max_z = abs(z_scores).max()
        anomalies["AnomalySeverity"] = np.clip(
            abs(anomalies["ZScore"]) / max(max_z, threshold_sigma * 2), 0.0, 1.0
        )

        logger.info(
            f"ARIMA detected {len(anomalies)} anomalies for {asset_ip}/{variable}"
        )
        return anomalies

    except Exception as e:
        logger.error(f"ARIMA failed for {asset_ip}/{variable}: {e}")
        return pd.DataFrame()


# ----------------------------------------------------------------
# Prophet-Based Trend and Seasonal Analysis
# ----------------------------------------------------------------
def detect_prophet_anomalies(
    series: pd.Series,
    asset_ip: str,
    variable: str,
) -> pd.DataFrame:
    """
    Use Facebook Prophet to model seasonal patterns and detect
    values outside the prediction interval. Detects gradual drifts
    and seasonal anomalies.

    Args:
        series: Time-indexed pandas Series of process values
        asset_ip: IP address of the asset for output context
        variable: Name of the process variable

    Returns:
        DataFrame of detected anomalies with context
    """
    from prophet import Prophet

    if len(series) < MIN_DATA_POINTS * 2:
        logger.warning(
            f"Insufficient data for Prophet ({len(series)} < {MIN_DATA_POINTS * 2}). "
            f"Skipping {asset_ip}/{variable}."
        )
        return pd.DataFrame()

    logger.info(
        f"Running Prophet anomaly detection: {asset_ip}/{variable} "
        f"({len(series)} points)"
    )

    try:
        # Prepare data for Prophet (requires 'ds' and 'y' columns)
        prophet_df = pd.DataFrame({
            "ds": series.index,
            "y": series.values,
        })

        # Configure and fit Prophet
        model = Prophet(
            interval_width=PROPHET_INTERVAL_WIDTH,
            changepoint_prior_scale=PROPHET_CHANGEPOINT_SCALE,
            daily_seasonality=True,
            weekly_seasonality=True,
        )
        # Suppress Prophet's verbose output
        model.fit(prophet_df, **{"suppress_stdout_stderr": True}
                  if hasattr(model, "fit") else {})

        # Generate predictions
        forecast = model.predict(prophet_df)

        # Identify anomalies: observed values outside prediction interval
        anomaly_mask = (
            (prophet_df["y"].values < forecast["yhat_lower"].values) |
            (prophet_df["y"].values > forecast["yhat_upper"].values)
        )

        if anomaly_mask.sum() == 0:
            logger.info(f"No Prophet anomalies detected for {asset_ip}/{variable}")
            return pd.DataFrame()

        anomalies = pd.DataFrame({
            "Timestamp": prophet_df["ds"][anomaly_mask].values,
            "AssetIP": asset_ip,
            "Variable": variable,
            "ObservedValue": prophet_df["y"][anomaly_mask].values,
            "ExpectedValue": forecast["yhat"][anomaly_mask].values,
            "ExpectedLower": forecast["yhat_lower"][anomaly_mask].values,
            "ExpectedUpper": forecast["yhat_upper"][anomaly_mask].values,
            "DetectionMethod": "Prophet",
            "AnomalyType": np.where(
                prophet_df["y"][anomaly_mask].values
                > forecast["yhat_upper"][anomaly_mask].values,
                "AboveSeasonalBound", "BelowSeasonalBound"
            ),
        })

        # Severity based on distance from prediction interval
        interval_width = (
            forecast["yhat_upper"][anomaly_mask].values
            - forecast["yhat_lower"][anomaly_mask].values
        )
        deviation = np.where(
            anomalies["AnomalyType"] == "AboveSeasonalBound",
            anomalies["ObservedValue"] - anomalies["ExpectedUpper"],
            anomalies["ExpectedLower"] - anomalies["ObservedValue"],
        )
        anomalies["AnomalySeverity"] = np.clip(
            deviation / np.where(interval_width > 0, interval_width, 1.0),
            0.0, 1.0,
        )

        logger.info(
            f"Prophet detected {len(anomalies)} anomalies for {asset_ip}/{variable}"
        )
        return anomalies

    except Exception as e:
        logger.error(f"Prophet failed for {asset_ip}/{variable}: {e}")
        return pd.DataFrame()


# ----------------------------------------------------------------
# Enrichment and Output
# ----------------------------------------------------------------
def enrich_with_asset_context(
    anomalies: pd.DataFrame,
    asset_register: pd.DataFrame,
) -> pd.DataFrame:
    """Enrich anomaly results with OT Asset Register context."""
    if anomalies.empty or asset_register.empty:
        return anomalies

    if "IPAddress" in asset_register.columns:
        enrichment = asset_register.rename(columns={"IPAddress": "AssetIP"})
        enrich_cols = ["AssetIP"]
        for col in ["Hostname", "PurdueLevel", "DeviceType", "CrownJewelTier",
                     "EngineeringOwner", "ProcessFunction"]:
            if col in enrichment.columns:
                enrich_cols.append(col)
        anomalies = anomalies.merge(
            enrichment[enrich_cols].drop_duplicates(),
            on="AssetIP", how="left",
        )

    # Adjust severity based on crown jewel tier
    if "CrownJewelTier" in anomalies.columns:
        tier_multiplier = {
            "Tier 1": 1.0, "Tier 2": 0.85, "Tier 3": 0.7,
            "Tier 4": 0.5, "Tier 5": 0.3,
        }
        anomalies["AdjustedSeverity"] = anomalies.apply(
            lambda r: min(1.0, r["AnomalySeverity"] * tier_multiplier.get(
                str(r.get("CrownJewelTier", "")), 0.5
            ) * 1.5),  # Tier 1 assets get a 1.5x severity boost
            axis=1,
        )
    else:
        anomalies["AdjustedSeverity"] = anomalies["AnomalySeverity"]

    return anomalies


def format_for_sentinel(anomalies: pd.DataFrame) -> list[dict]:
    """Format anomaly results for Sentinel OT_ML_Anomalies_CL table."""
    records = []
    for _, row in anomalies.iterrows():
        record = {
            "TimeGenerated": str(row.get("Timestamp", datetime.utcnow().isoformat())),
            "AnomalyType": "ProcessAnomaly",
            "AssetIdentifier": row["AssetIP"],
            "AnomalyScore": round(float(row.get("AdjustedSeverity",
                                                  row["AnomalySeverity"])), 4),
            "AnomalyDescription": (
                f"Process variable '{row['Variable']}' on {row['AssetIP']} "
                f"({row.get('Hostname', 'unknown')}): "
                f"observed {row['ObservedValue']:.2f}, "
                f"expected ~{row['ExpectedValue']:.2f}. "
                f"Detection: {row['DetectionMethod']} — {row['AnomalyType']}."
            ),
            "BaselineReference": f"{row['DetectionMethod']} model baseline",
            "ObservedBehaviour": json.dumps({
                "variable": row["Variable"],
                "observed": round(float(row["ObservedValue"]), 4),
                "expected": round(float(row["ExpectedValue"]), 4),
            }),
            "ModelVersion": f"process_anomaly_{row['DetectionMethod'].lower()}_v1.0.0",
        }
        for field in ["Hostname", "PurdueLevel", "DeviceType",
                      "CrownJewelTier", "EngineeringOwner"]:
            if field in row and pd.notna(row[field]):
                record[field] = str(row[field])
        records.append(record)
    return records


# ----------------------------------------------------------------
# Analysis Pipeline
# ----------------------------------------------------------------
def analyse_variable(
    data: pd.DataFrame,
    asset_ip: str,
    variable: str,
) -> pd.DataFrame:
    """
    Run both ARIMA and Prophet analysis on a single variable.

    Returns combined anomalies from both methods.
    """
    # Filter to specific asset and variable
    mask = (data["AssetIP"] == asset_ip) & (data["Variable"] == variable)
    subset = data[mask].copy()

    if subset.empty:
        logger.warning(f"No data for {asset_ip}/{variable}")
        return pd.DataFrame()

    # Create time-indexed series, resample to regular intervals
    subset = subset.set_index("Timestamp").sort_index()
    series = subset["Value"].resample(RESAMPLE_INTERVAL).mean().dropna()

    if len(series) < MIN_DATA_POINTS:
        logger.warning(
            f"Insufficient data after resampling for {asset_ip}/{variable} "
            f"({len(series)} points)"
        )
        return pd.DataFrame()

    # Run both detection methods
    arima_anomalies = detect_arima_anomalies(series, asset_ip, variable)
    prophet_anomalies = detect_prophet_anomalies(series, asset_ip, variable)

    # Combine results
    all_anomalies = pd.concat(
        [arima_anomalies, prophet_anomalies], ignore_index=True
    )
    return all_anomalies


# ----------------------------------------------------------------
# Main
# ----------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="OT Process Anomaly Detection — Chapter 8",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--data", help="Path to historian data CSV",
    )
    parser.add_argument(
        "--batch-dir", help="Directory of historian CSV exports for batch mode",
    )
    parser.add_argument(
        "--asset-register", required=True,
        help="Path to OT_AssetRegister watchlist CSV export",
    )
    parser.add_argument(
        "--variable", help="Process variable to analyse (single mode)",
    )
    parser.add_argument(
        "--asset-ip", help="Asset IP to analyse (single mode)",
    )
    parser.add_argument(
        "--output", default="anomalies_process.csv",
        help="Path for anomaly output CSV",
    )
    parser.add_argument(
        "--sentinel-output", default=None,
        help="Path for Sentinel-formatted JSON output",
    )

    args = parser.parse_args()
    asset_register = load_asset_register(args.asset_register)
    all_anomalies = []

    if args.data and args.asset_ip and args.variable:
        # Single variable mode
        data = load_historian_data(args.data)
        anomalies = analyse_variable(data, args.asset_ip, args.variable)
        if not anomalies.empty:
            all_anomalies.append(anomalies)

    elif args.batch_dir:
        # Batch mode — process all CSV files in directory
        batch_path = Path(args.batch_dir)
        for csv_file in sorted(batch_path.glob("*.csv")):
            data = load_historian_data(str(csv_file))
            for (asset_ip, variable), _ in data.groupby(["AssetIP", "Variable"]):
                anomalies = analyse_variable(data, asset_ip, variable)
                if not anomalies.empty:
                    all_anomalies.append(anomalies)

    elif args.data:
        # Auto mode — analyse all assets and variables in data file
        data = load_historian_data(args.data)
        for (asset_ip, variable), _ in data.groupby(["AssetIP", "Variable"]):
            anomalies = analyse_variable(data, asset_ip, variable)
            if not anomalies.empty:
                all_anomalies.append(anomalies)

    else:
        parser.error("Provide --data (with --asset-ip and --variable) or --batch-dir")

    if all_anomalies:
        combined = pd.concat(all_anomalies, ignore_index=True)
        combined = enrich_with_asset_context(combined, asset_register)
        combined.to_csv(args.output, index=False)
        logger.info(f"Total anomalies: {len(combined)}, written to {args.output}")

        if args.sentinel_output:
            sentinel_records = format_for_sentinel(combined)
            with open(args.sentinel_output, "w") as f:
                json.dump(sentinel_records, f, indent=2)
            logger.info(f"Sentinel output written to {args.sentinel_output}")
    else:
        logger.info("No anomalies detected across all analysed variables.")

    logger.info("Done.")


if __name__ == "__main__":
    main()
