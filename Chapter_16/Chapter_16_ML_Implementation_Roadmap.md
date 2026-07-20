# Phased ML Implementation Roadmap for OT Security
# ================================================================
# Description: Project planning template for the five-phase ML
#   maturity roadmap. Includes milestones, decision gates, and
#   rollback criteria for each phase.
#
# Usage: Adapt timelines to your environment. Do not skip phases.
#   Each decision gate must be passed before advancing.
#
# Reference: Chapter 8 — Leveraging AI and Machine Learning
# ================================================================

## PROGRAMME INFORMATION
- **Programme Owner**: [SOC Manager / Security Director]
- **OT Engineering Sponsor**: [Named OT engineering lead]
- **Start Date**: [Planned start]
- **Current Phase**: [1 / 2 / 3 / 4]
- **Last Updated**: [Date]

---

## PHASE 1: DATA HYGIENE AND PREPARATION (Months 1–3)

**Objective**: Establish clean, validated data foundations. No ML deployment.

### Milestones

| # | Milestone | Owner | Target Date | Status |
|---|-----------|-------|-------------|--------|
| 1.1 | Complete ML Readiness Assessment | SOC Lead + OT Eng | Month 1, Week 2 | ☐ |
| 1.2 | Validate ASIM parser accuracy (spot-check 100 events) | Detection Engineer | Month 1, Week 4 | ☐ |
| 1.3 | Confirm NTP synchronisation across OT log sources | OT Engineer | Month 1, Week 4 | ☐ |
| 1.4 | Generate 30-day communication baselines for crown jewels | SOC Analyst | Month 2, Week 2 | ☐ |
| 1.5 | Validate baselines with OT engineering (workshop) | SOC + OT Eng | Month 2, Week 4 | ☐ |
| 1.6 | Document known operational variations (seasonal, batch, shift) | OT Engineer | Month 2, Week 4 | ☐ |
| 1.7 | Establish data quality metrics and monitoring | SOC Analyst | Month 3, Week 2 | ☐ |
| 1.8 | Build labelled reference datasets (known-good states) | SOC + OT Eng | Month 3, Week 4 | ☐ |
| 1.9 | Deliver Data Readiness Assessment report | SOC Lead | Month 3, Week 4 | ☐ |

### Decision Gate: Advance to Phase 2?

| Criterion | Met? |
|-----------|------|
| All critical ML Readiness Assessment items Met | ☐ Yes ☐ No |
| Communication baselines validated by OT engineering | ☐ Yes ☐ No |
| Data quality metrics meet minimum thresholds | ☐ Yes ☐ No |
| Labelled reference datasets created | ☐ Yes ☐ No |
| Analyst capacity confirmed for ML alert investigation | ☐ Yes ☐ No |

**Decision**: ☐ Advance to Phase 2 ☐ Extend Phase 1 (address gaps) ☐ Pause (prerequisites not achievable)

---

## PHASE 2: SUPERVISED LEARNING (Months 4–6)

**Objective**: Deploy supervised models on known patterns with human validation.

### Milestones

| # | Milestone | Owner | Target Date | Status |
|---|-----------|-------|-------------|--------|
| 2.1 | Configure compute environment (Python, libraries, API access) | SOC Engineer | Month 4, Week 1 | ☐ |
| 2.2 | Deploy Asset Behaviour Profiling model (training mode) | Detection Engineer | Month 4, Week 2 | ☐ |
| 2.3 | Validate model output against known baselines | SOC Analyst + OT Eng | Month 4, Week 4 | ☐ |
| 2.4 | Configure Sentinel custom table (OT_ML_Anomalies_CL) | SOC Engineer | Month 5, Week 1 | ☐ |
| 2.5 | Implement ML-to-Sentinel ingestion pipeline | SOC Engineer | Month 5, Week 2 | ☐ |
| 2.6 | Deploy correlation query (ML + rule-based) | Detection Engineer | Month 5, Week 3 | ☐ |
| 2.7 | Run 2-week silent monitoring period | SOC Analyst | Month 5–6 | ☐ |
| 2.8 | Complete first Model Evaluation Metrics assessment | SOC Lead + OT Eng | Month 6, Week 3 | ☐ |
| 2.9 | Deliver Phase 2 performance report | SOC Lead | Month 6, Week 4 | ☐ |

### Decision Gate: Advance to Phase 3?

| Criterion | Met? |
|-----------|------|
| Supervised model meets precision ≥ 0.70 and recall ≥ 0.80 | ☐ Yes ☐ No |
| False positive rate ≤ 0.10 | ☐ Yes ☐ No |
| ML-to-Sentinel pipeline operational and reliable | ☐ Yes ☐ No |
| Analyst Utility Score ≥ 3.5/5.0 | ☐ Yes ☐ No |
| OT engineering endorses model output as credible | ☐ Yes ☐ No |
| Aggregate FP-OIS ≤ 3.0 | ☐ Yes ☐ No |

**Decision**: ☐ Advance to Phase 3 ☐ Extend Phase 2 (tune models) ☐ Maintain Phase 2 (sufficient value)

---

## PHASE 3: UNSUPERVISED ANOMALY DETECTION (Months 7–12)

**Objective**: Deploy unsupervised models for baseline-deviation detection.

### Milestones

| # | Milestone | Owner | Target Date | Status |
|---|-----------|-------|-------------|--------|
| 3.1 | Export and validate process historian data (90+ days) | OT Engineer + SOC | Month 7, Week 2 | ☐ |
| 3.2 | Deploy Process Anomaly Detection (single Tier 1 process) | Detection Engineer | Month 7, Week 4 | ☐ |
| 3.3 | Run 2-week silent monitoring for process anomaly model | SOC Analyst | Month 8 | ☐ |
| 3.4 | Tune process anomaly thresholds with OT engineering | SOC + OT Eng | Month 8, Week 4 | ☐ |
| 3.5 | Expand process anomaly detection to additional crown jewels | Detection Engineer | Month 9 | ☐ |
| 3.6 | Deploy Protocol Anomaly Detection (training phase) | Detection Engineer | Month 9, Week 2 | ☐ |
| 3.7 | Validate LSTM model on held-out test data | Detection Engineer | Month 10, Week 2 | ☐ |
| 3.8 | Run 4-week silent monitoring for protocol anomaly model | SOC Analyst | Month 10–11 | ☐ |
| 3.9 | Complete comprehensive Model Evaluation for all models | SOC Lead + OT Eng | Month 11, Week 4 | ☐ |
| 3.10 | Deliver Phase 3 performance report | SOC Lead | Month 12 | ☐ |

### Decision Gate: Advance to Phase 4?

| Criterion | Met? |
|-----------|------|
| All deployed models meet performance targets | ☐ Yes ☐ No |
| Aggregate FP-OIS ≤ 3.0 across all models | ☐ Yes ☐ No |
| Analyst Utility Score ≥ 3.5/5.0 for each model | ☐ Yes ☐ No |
| OT engineering confirms models enhance (not hinder) operations | ☐ Yes ☐ No |
| Model governance process operational (versioning, retraining) | ☐ Yes ☐ No |
| No model drift exceeding 25% in any metric | ☐ Yes ☐ No |

**Decision**: ☐ Advance to Phase 4 ☐ Extend Phase 3 (tune/retrain) ☐ Maintain Phase 3 (sufficient value)

---

## PHASE 4: ADVISORY MODE (Year 2+)

**Objective**: ML models provide contextual recommendations to analysts with confidence scoring.

### Milestones

| # | Milestone | Owner | Target Date | Status |
|---|-----------|-------|-------------|--------|
| 4.1 | Implement dynamic alert severity adjustment (ML + rules) | Detection Engineer | Month 13, Week 4 | ☐ |
| 4.2 | Build automated investigation context retrieval | SOC Engineer | Month 14, Week 4 | ☐ |
| 4.3 | Implement predictive maintenance correlation | SOC + OT Eng | Month 15, Week 4 | ☐ |
| 4.4 | Establish quarterly model retraining schedule | SOC Lead | Month 13, Week 2 | ☐ |
| 4.5 | Create golden baseline archive (known-good, never overwritten) | SOC Engineer | Month 13, Week 4 | ☐ |
| 4.6 | Implement baseline drift monitoring | Detection Engineer | Month 14, Week 4 | ☐ |
| 4.7 | Deliver annual ML programme review | SOC Lead | Month 24 | ☐ |

### Ongoing Governance

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Model retraining | Quarterly + on operational change | Detection Engineer |
| Model Evaluation Metrics review | Quarterly | SOC Lead + OT Eng |
| Golden baseline validation | Semi-annually | SOC + OT Eng |
| Baseline drift analysis | Monthly | Detection Engineer |
| ML programme review | Annually | Security Director |

---

## PHASE 5: NEVER REACHED — AUTONOMOUS RESPONSE

**This phase is listed to document its explicit prohibition.**

ML in OT security environments must **never**:
- ☒ Autonomously execute containment actions
- ☒ Automatically isolate network segments or devices
- ☒ Trigger process shutdowns based on model output
- ☒ Modify firewall rules without human approval
- ☒ Override safety system configurations

**This is a safety boundary, not a maturity gate. It applies regardless of model accuracy, organisational maturity, or operational confidence.**

---

## ROLLBACK CRITERIA

If any of the following conditions are met, roll back to the previous phase and investigate:

| Condition | Action |
|-----------|--------|
| Aggregate FP-OIS exceeds 5.0 for two consecutive quarters | Retrain or retire affected model |
| Model causes analyst alert fatigue (Utility Score < 2.5) | Tune thresholds or retire model |
| OT engineering withdraws endorsement | Pause model, investigate with engineering |
| Model drift exceeds 25% without explanation | Retrain with current data |
| False positive leads to unwarranted operational disruption | Immediate review and potential retirement |
| Any model output triggers autonomous action (Phase 5 breach) | Immediate shutdown, incident review |

---

## PROGRAMME METRICS DASHBOARD

| Metric | Phase 1 | Phase 2 | Phase 3 | Phase 4 |
|--------|---------|---------|---------|---------|
| Models deployed | 0 | | | |
| Alerts/day (total) | 0 | | | |
| Aggregate FP-OIS | — | | | |
| Precision (avg) | — | | | |
| Recall (avg) | — | | | |
| Analyst Utility Score | — | | | |
| True threats found by ML alone | — | | | |
| ML-correlated rule confirmations | — | | | |
