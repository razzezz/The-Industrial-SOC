# Joint KPIs and Metrics Definitions — OT SOC Operations

## Purpose

This document provides complete definitions, calculation methodologies, data sources, targets, and reporting cadences for all metrics used to measure the effectiveness of the OT security operations programme and cross-functional collaboration. These metrics are reported at the quarterly programme review and tracked in the Microsoft Sentinel workbook dashboard.

---

## Operational Metrics

### MTTD — Mean Time to Detect

| Attribute | Definition |
|-----------|------------|
| **Description** | Average time between adversary activity occurring and the SOC identifying it. |
| **Calculation** | Sum of (Detection Timestamp − Activity Timestamp) for all true positive incidents / Count of true positive incidents |
| **Data Source** | Microsoft Sentinel incident records (CreatedTime vs. estimated activity start from investigation) |
| **Segmentation** | Track separately for: IT-side activity (ICS Kill Chain Stage 1), OT-side activity (ICS Kill Chain Stage 2) |
| **Target** | IT: < 4 hours. OT: < 8 hours. Reduce quarterly. |
| **Reporting Cadence** | Monthly, reported at quarterly review |
| **Owner** | IT Security Lead |
| **Interpretation** | A low IT MTTD with high OT MTTD indicates a visibility gap at lower Purdue Levels. Prioritise sensor deployment. |

### MTTT — Mean Time to Triage

| Attribute | Definition |
|-----------|------------|
| **Description** | Average time between an alert firing and the analyst completing initial triage assessment. |
| **Calculation** | Sum of (Triage Completion Timestamp − Alert Timestamp) / Count of triaged alerts |
| **Data Source** | Sentinel incident workflow timestamps |
| **Segmentation** | Track by: Crown Jewel Tier (Tier 1, Tier 2, Tier 3–5), Purdue Level, Shift (day/night/weekend) |
| **Target** | Tier 1 crown jewel alerts: < 15 minutes. Tier 2: < 30 minutes. All others: per standard SLA. |
| **Reporting Cadence** | Monthly, reported at quarterly review |
| **Owner** | SOC Lead |
| **Interpretation** | Persistent breach of Tier 1 target indicates insufficient staffing, inadequate OT training, or missing operational context (maintenance window data not available). |

### MTTEE — Mean Time to Engage Engineering

| Attribute | Definition |
|-----------|------------|
| **Description** | Average time between an OT incident requiring engineering input and the engineering team being actively engaged. |
| **Calculation** | Sum of (Engineering Engagement Timestamp − Escalation Initiated Timestamp) / Count of engineering escalations |
| **Data Source** | Sentinel incident records (escalation comments/timestamps) or ITSM records |
| **Segmentation** | Track by: Business hours vs. off-hours, Site location, Incident severity |
| **Target** | Business hours: < 30 minutes. Off-hours: < 60 minutes. |
| **Reporting Cadence** | Monthly, reported at quarterly review |
| **Owner** | Engineering Liaison |
| **Interpretation** | Persistent high MTTEE indicates broken communication channel, insufficient engineering on-call coverage, or cultural resistance. Address at weekly sync. |

### OT False Positive Rate

| Attribute | Definition |
|-----------|------------|
| **Description** | Percentage of OT alerts that are determined upon investigation to be legitimate activity. |
| **Calculation** | (OT alerts closed as False Positive or Benign Positive / Total OT alerts investigated) × 100 |
| **Data Source** | Sentinel incident closure classifications |
| **Segmentation** | Track by: Detection rule, Asset category, Purdue Level |
| **Target** | < 30% (initial target). Reduce by 5% per quarter through tuning. |
| **Reporting Cadence** | Monthly, reported at quarterly review |
| **Owner** | Detection Engineer + Engineering Liaison (jointly) |
| **Interpretation** | High FP rate for specific rules indicates need for operational context tuning (maintenance windows, communication baselines). High FP rate for specific asset categories may indicate misconfiguration or incomplete asset register. |

### Alert Volume by Purdue Level

| Attribute | Definition |
|-----------|------------|
| **Description** | Distribution of alerts across Purdue Levels over time. |
| **Calculation** | Count of alerts grouped by target asset's Purdue Level per reporting period |
| **Data Source** | Sentinel alerts enriched with OT_AssetRegister watchlist data |
| **Segmentation** | By Purdue Level (0–5), by alert severity, by detection rule category |
| **Target** | No absolute target — track trends. Alert at unexpected volume changes (>50% increase at any level). |
| **Reporting Cadence** | Monthly, reported at quarterly review |
| **Owner** | SOC Lead |
| **Interpretation** | Absence of alerts at Levels 0–2 may indicate visibility gap, not security. Unexpected spike at any level warrants investigation. |

---

## Coverage Metrics

### Crown Jewel Monitoring Coverage

| Attribute | Definition |
|-----------|------------|
| **Description** | Percentage of crown jewel assets with active detection coverage. |
| **Calculation** | (Crown jewel assets with ≥ 1 active detection rule covering them / Total crown jewel assets) × 100 |
| **Data Source** | OT_CrownJewels watchlist cross-referenced with detection rule asset scope |
| **Segmentation** | By Tier (1, 2), by site, by asset type |
| **Target** | Tier 1: 100%. Tier 2: 90%. |
| **Reporting Cadence** | Quarterly |
| **Owner** | Detection Engineer |
| **Interpretation** | Any Tier 1 asset without coverage is an unacceptable gap requiring immediate remediation. |

### ATT&CK for ICS Detection Coverage

| Attribute | Definition |
|-----------|------------|
| **Description** | Percentage of ATT&CK for ICS techniques covered by active detection rules. |
| **Calculation** | (ATT&CK for ICS techniques with ≥ 1 active detection rule / Total ATT&CK for ICS techniques applicable to the environment) × 100 |
| **Data Source** | ATT&CK Coverage Assessment query (Chapter 7) |
| **Segmentation** | By ATT&CK Tactic, by data source type (SIEM, NIDS, EDR) |
| **Target** | Initial: > 30% of applicable techniques. Year 1 target: > 50%. Year 2 target: > 70%. |
| **Reporting Cadence** | Quarterly |
| **Owner** | Detection Engineer |
| **Interpretation** | Coverage should expand steadily. Prioritise techniques used by threat actors relevant to the organisation's sector (Chapter 10 intelligence requirements). |

### Purdue Level Visibility

| Attribute | Definition |
|-----------|------------|
| **Description** | Percentage of each Purdue Level from which the SOC receives telemetry. |
| **Calculation** | (Purdue Level segments with active telemetry collection / Total Purdue Level segments in environment) × 100 |
| **Data Source** | Data connector health checks, sensor deployment records |
| **Segmentation** | By Purdue Level, by site |
| **Target** | Levels 3.5–5: 100%. Level 3: > 90%. Levels 0–2: visibility roadmap defined, target set per environment. |
| **Reporting Cadence** | Quarterly |
| **Owner** | SOC Lead + OT SME |
| **Interpretation** | Strong visibility at L3.5–5 with none at L0–2 is common but leaves the most critical assets unmonitored. Track improvement over time. |

---

## Collaboration Metrics

### CSIRT Assembly Time

| Attribute | Definition |
|-----------|------------|
| **Description** | Time from incident declaration to full CSIRT engagement. |
| **Calculation** | CSIRT fully assembled timestamp − Incident declaration timestamp |
| **Data Source** | Incident records, exercise records |
| **Segmentation** | By severity level, by time of day (business hours vs. off-hours), exercise vs. real incident |
| **Target** | Severity 1: < 30 minutes. Severity 2: < 60 minutes. |
| **Reporting Cadence** | Per incident/exercise, aggregated quarterly |
| **Owner** | CSIRT Lead |
| **Interpretation** | Consistently missed targets indicate problems with the contact tree, on-call arrangements, or team commitment. |

### Joint Training Completion

| Attribute | Definition |
|-----------|------------|
| **Description** | Percentage of required personnel who have completed cross-functional training. |
| **Calculation** | (Personnel with required training complete / Total personnel requiring training) × 100 |
| **Data Source** | Training records (CSIRT Lead) |
| **Segmentation** | SOC Analysts: IT Security OT Training Plan Track 1+2 completion. OT Engineers: OT Engineering Security Training Plan Track 1+2 completion. Operations: Track 3 completion. |
| **Target** | > 80% within 6 months of programme launch. > 95% within 12 months. |
| **Reporting Cadence** | Quarterly |
| **Owner** | CSIRT Lead |
| **Interpretation** | Low completion indicates resourcing pressure, leadership support gaps, or training delivery issues. |

### Tabletop Exercise Cadence

| Attribute | Definition |
|-----------|------------|
| **Description** | Number of cross-functional tabletop exercises conducted. |
| **Calculation** | Count of exercises per quarter |
| **Data Source** | Exercise records |
| **Segmentation** | Operational-level exercises (monthly), Executive-level exercises (semi-annual) |
| **Target** | ≥ 3 per quarter (monthly cadence). ≥ 2 per year with executive participation. |
| **Reporting Cadence** | Quarterly |
| **Owner** | CSIRT Lead |
| **Interpretation** | Missed exercises indicate competing priorities are eroding the collaboration programme. Escalate to executive sponsor. |

### Engineering Collaboration Score

| Attribute | Definition |
|-----------|------------|
| **Description** | Qualitative assessment of collaboration quality between the SOC and engineering teams. |
| **Calculation** | Average score from quarterly survey (5-point Likert scale) across collaboration dimensions |
| **Data Source** | Quarterly survey distributed to SOC analysts, OT engineers, and operations staff |
| **Survey Dimensions** | Communication quality (1–5), Trust level (1–5), Response timeliness (1–5), Context quality provided (1–5), Overall collaboration satisfaction (1–5) |
| **Target** | Average ≥ 3.5 within 6 months. Average ≥ 4.0 within 12 months. |
| **Reporting Cadence** | Quarterly |
| **Owner** | Engineering Liaison |
| **Interpretation** | Declining scores indicate relationship erosion — often caused by repeated false positive escalations, unilateral security actions, or unmet commitments. Address root cause at next weekly sync. |

---

## Business Metrics

### Downtime Prevented

| Attribute | Definition |
|-----------|------------|
| **Description** | Estimated production downtime avoided through proactive security actions. |
| **Calculation** | Estimated based on incident type and sector benchmarks for unmitigated impact. Documented per incident as part of the AAR. |
| **Data Source** | Incident records, AAR reports |
| **Target** | Track trend — demonstrate increasing value over time. |
| **Reporting Cadence** | Quarterly |
| **Owner** | CSIRT Lead |

### Downtime Caused by Security

| Attribute | Definition |
|-----------|------------|
| **Description** | Production downtime resulting from security actions or tool deployments. |
| **Calculation** | Sum of documented production downtime attributed to security operations |
| **Data Source** | Incident records, change management records, engineering feedback |
| **Target** | Zero. Any non-zero value requires root cause analysis and process improvement. |
| **Reporting Cadence** | Quarterly |
| **Owner** | CSIRT Lead + Engineering Liaison |

### Audit and Compliance Findings

| Attribute | Definition |
|-----------|------------|
| **Description** | Trend in regulatory or audit findings related to OT cybersecurity. |
| **Calculation** | Count of findings per audit, severity-weighted |
| **Data Source** | Audit reports, regulatory correspondence |
| **Target** | Declining trend. Zero critical findings. |
| **Reporting Cadence** | Per audit, aggregated annually |
| **Owner** | CSIRT Lead |

---

## Dashboard Implementation

These metrics are implemented as a Microsoft Sentinel Workbook with the following tabs:

1. **Operational Overview** — MTTD, MTTT, MTTEE, OT FP Rate, Alert Volume by Purdue Level
2. **Detection Coverage** — Crown Jewel Monitoring, ATT&CK Coverage heatmap, Purdue Level Visibility
3. **Collaboration** — CSIRT Assembly Time, Training Completion, Exercise Cadence, Collaboration Score
4. **Executive Summary** — Business metrics, trend lines, maturity progression

---

*Metric definitions are reviewed annually as part of the CSIRT Charter review. Any metric that consistently fails to provide actionable insight should be retired and replaced.*
