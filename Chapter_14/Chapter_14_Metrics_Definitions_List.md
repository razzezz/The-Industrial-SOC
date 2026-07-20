# Metrics Definitions List
# ================================================================
# Description: Comprehensive definitions, calculation methodologies,
#   data sources, targets, and reporting cadences for all OT SOC
#   metrics described in Chapter 14. Covers operational, coverage,
#   collaboration, and business metrics.
#
# Usage: Implement as the measurement framework for the OT security
#   programme. Use the Joint KPIs Dashboard Template for reporting.
# ================================================================

---

## Operational Metrics

### OM-01: Mean Time to Detect (MTTD)

| Field | Definition |
|-------|-----------|
| **Description** | Time between adversary activity occurring and the SOC identifying it |
| **Calculation** | Average of (Alert Timestamp − Estimated Activity Start) across all confirmed incidents |
| **Data Source** | Microsoft Sentinel incidents; incident investigation records |
| **Segmentation** | Track separately for IT-side (Stage 1) and OT-side (Stage 2) activity |
| **Target** | IT: < 4 hours; OT: < 1 hour for Tier 1 crown jewels |
| **Reporting Cadence** | Monthly |
| **Owner** | SOC Manager |
| **Notes** | A low IT MTTD with high OT MTTD indicates visibility gap in the control network |

### OM-02: Mean Time to Triage (MTTT)

| Field | Definition |
|-------|-----------|
| **Description** | Time between an alert firing and the analyst completing initial triage assessment |
| **Calculation** | Average of (Triage Complete Timestamp − Alert Created Timestamp) |
| **Data Source** | Sentinel incident status timestamps |
| **Segmentation** | Track by crown jewel tier (Tier 1 vs. all OT) |
| **Target** | Tier 1 assets: < 15 minutes; All OT: < 30 minutes |
| **Reporting Cadence** | Weekly |
| **Owner** | SOC Shift Lead |
| **Notes** | Consistently exceeding target indicates insufficient staffing or training |

### OM-03: Mean Time to Engage Engineering (MTTEE)

| Field | Definition |
|-------|-----------|
| **Description** | Time between an OT incident requiring engineering input and the engineering team being actively engaged |
| **Calculation** | Average of (Engineering Engaged Timestamp − Engineering Requested Timestamp) |
| **Data Source** | Incident records; communication logs |
| **Segmentation** | Business hours vs. off-hours |
| **Target** | Business hours: < 30 minutes; Off-hours: < 60 minutes |
| **Reporting Cadence** | Monthly |
| **Owner** | Engineering Liaison |
| **Notes** | Measures effectiveness of the engineering liaison function and communication channels |

### OM-04: OT False Positive Rate

| Field | Definition |
|-------|-----------|
| **Description** | Percentage of OT alerts that, upon investigation, are determined to be legitimate activity |
| **Calculation** | (OT False Positive Alerts / Total OT Alerts Investigated) × 100 |
| **Data Source** | Sentinel incident closure classifications |
| **Segmentation** | Track by detection rule AND by asset category |
| **Target** | < 20% overall; < 10% for Tier 1 crown jewel alerts |
| **Reporting Cadence** | Monthly |
| **Owner** | Detection Engineering Lead |
| **Notes** | High FP rate erodes analyst trust and engineering cooperation; drives tuning priorities |

### OM-05: Alert Volume by Purdue Level

| Field | Definition |
|-------|-----------|
| **Description** | Distribution of OT security alerts across Purdue Model levels |
| **Calculation** | Count of alerts per Purdue level per reporting period |
| **Data Source** | Sentinel alerts enriched with OT_AssetRegister watchlist |
| **Segmentation** | By Purdue level (0–5) |
| **Target** | N/A — trend-based; investigate unexpected changes |
| **Reporting Cadence** | Monthly |
| **Owner** | SOC Manager |
| **Notes** | Absence of alerts at Levels 0–2 may indicate visibility gap, not absence of threats |

---

## Coverage Metrics

### CM-01: Crown Jewel Monitoring Coverage

| Field | Definition |
|-------|-----------|
| **Description** | Percentage of Tier 1 and Tier 2 crown jewels for which the SOC has active detection coverage |
| **Calculation** | (Crown jewel assets with ≥ 1 active detection rule / Total crown jewel assets) × 100 |
| **Data Source** | OT_CrownJewels watchlist; detection rule inventory |
| **Segmentation** | By tier (Tier 1, Tier 2) |
| **Target** | 100% Tier 1; 90% Tier 2 |
| **Reporting Cadence** | Monthly |
| **Owner** | Detection Engineering Lead |
| **Notes** | Any unmonitored crown jewel is an unacceptable gap |

### CM-02: ATT&CK for ICS Detection Coverage

| Field | Definition |
|-------|-----------|
| **Description** | Percentage of ATT&CK for ICS techniques with at least one active detection rule |
| **Calculation** | Run ATTCK_ICS_Coverage_Assessment query from Chapter 7 |
| **Data Source** | Sentinel analytics rules; MITRE ATT&CK for ICS matrix |
| **Segmentation** | By tactic |
| **Target** | > 60% of techniques relevant to your sector |
| **Reporting Cadence** | Quarterly |
| **Owner** | Detection Engineering Lead |
| **Notes** | Focus on techniques used by threat actors targeting your sector (Chapter 3 reference) |

### CM-03: Purdue Level Visibility

| Field | Definition |
|-------|-----------|
| **Description** | Percentage of each Purdue level from which the SOC receives telemetry |
| **Calculation** | (Assets at level with telemetry / Total assets at level) × 100, per Purdue level |
| **Data Source** | OT_AssetRegister watchlist; Telemetry Source Inventory (Chapter 7) |
| **Segmentation** | By Purdue level (0–5) |
| **Target** | Level 3.5: 100%; Levels 2–3: > 80%; Levels 0–1: > 50% |
| **Reporting Cadence** | Quarterly |
| **Owner** | SOC Manager / Detection Engineering Lead |
| **Notes** | Supports business cases for additional sensor deployment |

---

## Collaboration Metrics

### CL-01: CSIRT Assembly Time

| Field | Definition |
|-------|-----------|
| **Description** | Time from incident declaration to full CSIRT engagement |
| **Calculation** | Time between incident declaration and last CSIRT member confirmed active |
| **Data Source** | Exercise records; incident records |
| **Segmentation** | Exercises vs. real incidents; Severity 1 vs. other |
| **Target** | < 30 minutes for Severity 1 |
| **Reporting Cadence** | Per exercise / per incident |
| **Owner** | CSIRT Lead |
| **Notes** | Test during every tabletop exercise |

### CL-02: Joint Training Completion

| Field | Definition |
|-------|-----------|
| **Description** | Percentage of SOC analysts who have completed OT training AND OT engineers who have completed security training |
| **Calculation** | (Trained personnel / Total personnel in role) × 100 |
| **Data Source** | Training records (Chapter 14 training plans) |
| **Segmentation** | SOC analysts (OT training) vs. OT engineers (security training) |
| **Target** | > 80% of both groups within 12 months of programme launch |
| **Reporting Cadence** | Quarterly |
| **Owner** | Training Coordinator |
| **Notes** | Track as rolling metric to account for staff turnover |

### CL-03: Tabletop Exercise Cadence

| Field | Definition |
|-------|-----------|
| **Description** | Number of cross-functional tabletop exercises conducted per quarter |
| **Calculation** | Count of completed exercises |
| **Data Source** | Exercise calendar and records |
| **Segmentation** | Operational (SOC + Engineering) vs. Strategic (includes leadership) |
| **Target** | ≥ 1 per quarter; ≥ 2 per year with executive participation |
| **Reporting Cadence** | Quarterly |
| **Owner** | Engineering Liaison |
| **Notes** | Use Cross-Functional Tabletop Exercise Guide for planning |

### CL-04: Engineering Collaboration Score

| Field | Definition |
|-------|-----------|
| **Description** | Qualitative assessment of IT Security / OT Engineering collaboration quality |
| **Calculation** | Survey-based: average score on 5-point scale across survey questions |
| **Data Source** | Quarterly surveys of SOC analysts and OT engineers |
| **Segmentation** | SOC perspective vs. Engineering perspective |
| **Target** | ≥ 3.5/5 (both groups) |
| **Reporting Cadence** | Quarterly |
| **Owner** | Engineering Liaison |
| **Notes** | As important as quantitative metrics; captures trust and communication health |

---

## Business Metrics

### BM-01: Downtime Prevented

| Field | Definition |
|-------|-----------|
| **Description** | Production downtime avoided through proactive security actions |
| **Calculation** | Estimated hours of avoided downtime based on threat severity and asset criticality |
| **Data Source** | Incident records; engineering estimates |
| **Target** | Trend-based; demonstrate value over time |
| **Reporting Cadence** | Quarterly |
| **Owner** | SOC Manager + Engineering Lead (joint) |

### BM-02: Downtime Caused by Security

| Field | Definition |
|-------|-----------|
| **Description** | Production downtime resulting from security actions (false positive investigations, tool issues, containment) |
| **Calculation** | Total hours of production impact attributed to security activities |
| **Data Source** | Incident records; engineering feedback |
| **Target** | Zero; any occurrence triggers root cause analysis |
| **Reporting Cadence** | Per occurrence + quarterly summary |
| **Owner** | SOC Manager |
| **Notes** | Track honestly; supports the "Do No Harm" commitment |

### BM-03: Cyber Risk Score Reduction

| Field | Definition |
|-------|-----------|
| **Description** | Reduction in assessed OT cyber risk across the environment |
| **Calculation** | Per maturity model assessment (Chapter 15) |
| **Data Source** | Maturity self-assessment scorecards |
| **Target** | Year-over-year improvement |
| **Reporting Cadence** | Annually |
| **Owner** | Programme Owner |

### BM-04: Audit and Compliance Findings

| Field | Definition |
|-------|-----------|
| **Description** | Trend in regulatory findings related to OT cybersecurity |
| **Calculation** | Count of findings by severity; comparison with previous assessment |
| **Data Source** | Audit reports; CAF assessments; NIS 2 compliance reviews |
| **Target** | Declining trend; zero critical findings |
| **Reporting Cadence** | Per audit cycle |
| **Owner** | Programme Owner |
