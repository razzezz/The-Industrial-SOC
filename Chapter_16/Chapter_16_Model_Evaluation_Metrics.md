# Model Evaluation Metrics for Safety-Critical OT Environments
# ================================================================
# Description: Structured template for tracking ML model performance
#   in OT security contexts. Includes standard ML metrics and
#   OT-specific metrics designed to capture the unique consequences
#   of model errors in safety-critical environments.
#
# Usage: Complete quarterly for each deployed model. Review with both
#   SOC and OT engineering stakeholders.
#
# Reference: Chapter 8 — Leveraging AI and Machine Learning
# ================================================================

## MODEL IDENTIFICATION
- **Model Name**: [e.g., Asset Behaviour Profiling v1.0.0]
- **Model Type**: [Isolation Forest | ARIMA | Prophet | LSTM | Other]
- **Use Case**: [Asset Behaviour | Process Anomaly | Protocol Anomaly]
- **Deployment Date**: [Date first deployed to production]
- **Current Version**: [Version string]
- **Last Retrained**: [Date]
- **Next Scheduled Retraining**: [Date]
- **Review Period**: [Start date — End date]
- **Reviewed By**: [SOC analyst + OT engineer names]

---

## SECTION 1: STANDARD ML PERFORMANCE METRICS

These metrics assess the model's technical accuracy. They should be calculated against a labelled validation dataset that includes both confirmed true positives (genuine anomalies) and confirmed true negatives (normal operations).

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| **True Positives (TP)** | | — | — |
| **False Positives (FP)** | | — | — |
| **True Negatives (TN)** | | — | — |
| **False Negatives (FN)** | | — | — |
| **Precision** (TP / (TP+FP)) | | ≥ 0.70 | ☐ Met ☐ Not Met |
| **Recall** (TP / (TP+FN)) | | ≥ 0.80 | ☐ Met ☐ Not Met |
| **F1 Score** (harmonic mean) | | ≥ 0.75 | ☐ Met ☐ Not Met |
| **False Positive Rate** (FP / (FP+TN)) | | ≤ 0.10 | ☐ Met ☐ Not Met |
| **Alert Volume** (total alerts/day) | | ≤ 10 | ☐ Met ☐ Not Met |

### Notes on Targets
- **Recall is prioritised over precision** in OT security. Missing a genuine threat (false negative) has higher consequences than investigating a false alarm (false positive).
- **Alert volume target** is per-model. Total ML alert volume across all models should not exceed analyst capacity (assessed in ML Readiness Checklist).
- Targets should be calibrated to the environment. The values above are starting recommendations.

---

## SECTION 2: OT-SPECIFIC PERFORMANCE METRICS

These metrics capture the unique dimensions of model performance in safety-critical OT environments.

### 2.1 False Positive Operational Impact Score (FP-OIS)

Each false positive is scored by the operational impact it would have caused if the analyst had taken containment action without proper verification. This metric ensures that false positives affecting crown jewel assets at low Purdue levels receive more attention than those affecting supporting systems.

| FP-OIS Category | Count | Example |
|-----------------|-------|---------|
| **Critical (Score 8–10)** | | FP on Tier 1 asset at L0-L1; containment would halt safety-critical process |
| **High (Score 5–7)** | | FP on Tier 2 asset at L2; containment would disrupt production |
| **Medium (Score 3–4)** | | FP on Tier 3 asset at L3; containment would affect engineering access |
| **Low (Score 1–2)** | | FP on Tier 4–5 asset at L3-L4; minimal operational impact |

**Aggregate FP-OIS**: [Sum of all FP impact scores] / [Number of false positives]

**Target**: Aggregate FP-OIS ≤ 3.0 (indicating false positives cluster on lower-impact assets)

**Status**: ☐ Met ☐ Not Met

### 2.2 Model Drift Rate

Measures how the model's performance changes over time, indicating whether retraining is needed.

| Period | Alert Volume | FP Rate | Precision | Drift Indicator |
|--------|-------------|---------|-----------|-----------------|
| Month 1 of review | | | | — |
| Month 2 of review | | | | ↑ ↓ → |
| Month 3 of review | | | | ↑ ↓ → |

**Drift Assessment**: ☐ Stable (< 10% change) ☐ Moderate (10–25% change) ☐ Significant (> 25% change)

**Action Required**: ☐ None ☐ Investigate drift cause ☐ Retrain model ☐ Retrain with operational change documentation

### 2.3 Retraining Currency

| Metric | Value | Target |
|--------|-------|--------|
| Days since last retraining | | ≤ 90 |
| Operational changes since last retraining | | Document below |
| Training data coverage (days) | | ≥ 30 |
| Golden baseline last validated | | ≤ 180 days ago |

**Operational Changes Since Last Retraining:**
- [ ] New assets commissioned
- [ ] Processes modified
- [ ] Network reconfiguration
- [ ] Seasonal transition (summer ↔ winter)
- [ ] Batch recipe changes
- [ ] Vendor/firmware updates
- [ ] None

### 2.4 Analyst Utility Assessment

This qualitative assessment captures whether the model's output is actually useful to analysts — a metric that technical performance numbers alone cannot provide.

| Question | Rating (1–5) | Comments |
|----------|-------------|----------|
| Do alerts include sufficient context for triage? | | |
| Can analysts understand why the model alerted? | | |
| Does the model surface genuine threats that rules miss? | | |
| Is the alert volume manageable alongside rule-based alerts? | | |
| Does OT engineering find the model's output credible? | | |
| **Average Utility Score** | **/5** | |

**Target**: Average Utility Score ≥ 3.5

**Status**: ☐ Met ☐ Not Met

---

## SECTION 3: CORRELATION WITH RULE-BASED DETECTIONS

| Metric | Value | Notes |
|--------|-------|-------|
| ML anomalies that correlated with rule-based detections | | Higher = ML confirming known threats |
| ML anomalies with NO corresponding rule match | | These are the "detection gap" finds |
| ML anomalies confirmed as true positives (after investigation) | | Combined true positive rate |
| Rule-based detections where ML provided additional context | | ML enrichment value |

---

## SECTION 4: DECISION AND ACTIONS

### Overall Model Assessment

| Assessment | ☐ |
|-----------|---|
| **Performing Well** — Continue current deployment | ☐ |
| **Needs Tuning** — Adjust thresholds or features | ☐ |
| **Needs Retraining** — Retrain on current data | ☐ |
| **Under Review** — Significant concerns, investigate | ☐ |
| **Recommend Retirement** — Model not providing value | ☐ |

### Action Items

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| | | | |
| | | | |
| | | | |

### Sign-Off

| Role | Name | Date |
|------|------|------|
| SOC Analyst / ML Engineer | | |
| OT Engineering Representative | | |
| SOC Manager | | |
