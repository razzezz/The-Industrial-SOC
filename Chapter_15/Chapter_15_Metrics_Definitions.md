# OT Cyber Defence Metrics Definitions List
# ================================================================
# Description: Detailed definitions for all metrics referenced in
#   Chapter 15. Each metric includes definition, collection method,
#   target value, reporting frequency, and maturity level at which
#   tracking should begin.
#
# Usage: Select metrics appropriate to your current maturity level.
#   At Level 2, begin with the "Start At" Level 2 metrics.
#   Add metrics progressively as maturity increases.
#   Present at Quarterly Improvement Reviews.
# ================================================================

---

## Technical Metrics

### TM-01: Crown Jewel Monitoring Coverage

| Field | Value |
|-------|-------|
| **Definition** | Percentage of Tier 1 and Tier 2 crown jewels for which the SOC has at least one active, tuned, documented detection rule that would fire on adversary activity targeting that asset. |
| **Formula** | (Crown Jewels with Active Detection / Total Crown Jewels) × 100, calculated separately for Tier 1 and Tier 2 |
| **Collection Method** | Cross-reference OT_CrownJewels watchlist with detection rule library. Each crown jewel asset must have at least one rule that references it directly or covers the network segment and protocol it uses. |
| **Target** | Tier 1: 100%. Tier 2: ≥90%. |
| **Reporting Frequency** | Quarterly |
| **Start At Maturity Level** | Level 3 |
| **Trend Interpretation** | Declining coverage indicates new assets added without detection, or rules retired without replacement. Investigate immediately. |

### TM-02: ATT&CK for ICS Detection Coverage

| Field | Value |
|-------|-------|
| **Definition** | Percentage of MITRE ATT&CK for ICS techniques covered by at least one active, documented detection rule. Tracked by tactic. |
| **Formula** | (Techniques with Active Detection / Total ATT&CK for ICS Techniques) × 100, per tactic |
| **Collection Method** | ATT&CK for ICS coverage assessment query (Chapter 7). Map each active analytics rule to ATT&CK technique IDs. |
| **Target** | Overall: ≥60% at Level 3, ≥80% at Level 4. ICS-specific tactics (TA0106, TA0107, TA0105): ≥50% at Level 3, ≥75% at Level 4. |
| **Reporting Frequency** | Quarterly |
| **Start At Maturity Level** | Level 3 |
| **Trend Interpretation** | Gaps in ICS-specific tactics (Inhibit Response Function, Impair Process Control, Impact) are the highest priority. These represent the most operationally consequential adversary objectives. |

### TM-03: Mean Time to Detect (MTTD)

| Field | Value |
|-------|-------|
| **Definition** | Average time between adversary activity occurring and the SOC identifying it through an alert or investigation finding. Tracked separately for IT-side activity (ICS Kill Chain Stage 1) and OT-side activity (Stage 2). |
| **Formula** | Average of (Alert Timestamp − Activity Timestamp) across all true positive incidents in the reporting period |
| **Collection Method** | Incident records. Activity timestamp from forensic timeline; alert timestamp from SIEM. For exercises, use the red team action timestamp and blue team detection timestamp. |
| **Target** | IT-side: <1 hour. OT-side: <4 hours. A significant disparity indicates an OT visibility gap. |
| **Reporting Frequency** | Quarterly (based on incidents and exercises in period) |
| **Start At Maturity Level** | Level 3 |
| **Trend Interpretation** | Improving MTTD indicates better detection coverage and analyst proficiency. Widening IT/OT MTTD gap indicates OT visibility investment needed. |

### TM-04: OT False Positive Rate

| Field | Value |
|-------|-------|
| **Definition** | Percentage of OT-tagged alerts determined upon investigation to be legitimate, expected operational activity rather than genuine security events. |
| **Formula** | (OT Alerts Closed as False Positive / Total OT Alerts Investigated) × 100 |
| **Collection Method** | SIEM incident data. Filter for alerts tagged with OT asset context (from OT_AssetRegister watchlist enrichment). Classification upon closure. |
| **Target** | <30% at Level 2, <15% at Level 3, <10% at Level 4 |
| **Reporting Frequency** | Monthly |
| **Start At Maturity Level** | Level 2 |
| **Trend Interpretation** | Declining FP rate indicates improving operational context (better maintenance window data, better baselines). Rising FP rate may indicate environmental change not reflected in detection logic, or new detection rules requiring tuning. |

---

## Operational Metrics

### OM-01: Mean Time to Triage (MTTT)

| Field | Value |
|-------|-------|
| **Definition** | Average time between an OT alert firing and the analyst completing the initial triage assessment (scope determination, severity assignment, escalation decision). |
| **Formula** | Average of (Triage Complete Timestamp − Alert Timestamp) across all OT alerts in the reporting period |
| **Collection Method** | SIEM/SOAR workflow data. Triage completion defined as the analyst recording the initial assessment and routing the alert. |
| **Target** | Tier 1 crown jewel alerts: <15 minutes. All OT alerts: <30 minutes. |
| **Reporting Frequency** | Monthly |
| **Start At Maturity Level** | Level 3 |
| **Trend Interpretation** | Increasing MTTT may indicate alert fatigue, inadequate analyst training on OT context, or insufficient enrichment automation. |

### OM-02: Mean Time to Engage Engineering (MTTEE)

| Field | Value |
|-------|-------|
| **Definition** | Average time between an OT incident requiring engineering input and the engineering team being actively engaged in the investigation or response. |
| **Formula** | Average of (Engineering Engagement Timestamp − Engineering Escalation Timestamp) |
| **Collection Method** | Incident records. Escalation timestamp from SIEM/SOAR; engagement timestamp from incident log or communication records. |
| **Target** | Business hours: <30 minutes. Outside business hours: <60 minutes. |
| **Reporting Frequency** | Quarterly |
| **Start At Maturity Level** | Level 3 |
| **Trend Interpretation** | Consistently exceeding target indicates engineering liaison function needs strengthening. Review escalation paths, contact information currency, and engineering team buy-in. |

### OM-03: Incidents Detected Before Operational Impact

| Field | Value |
|-------|-------|
| **Definition** | Count of security incidents detected and contained before they affected the operational process (production, safety, or environmental). |
| **Formula** | Count of incidents where containment was completed before any operational impact occurred |
| **Collection Method** | Incident records. Operational impact assessment from OT Engineering and Operations during incident closure or AAR. |
| **Target** | Increasing trend. Absolute number depends on threat exposure. |
| **Reporting Frequency** | Quarterly |
| **Start At Maturity Level** | Level 3 |
| **Trend Interpretation** | This is the primary value metric for the security programme. Communicate this to executive leadership — it represents harm prevented. |

### OM-04: Downtime Prevented vs Downtime Caused

| Field | Value |
|-------|-------|
| **Definition** | Ratio comparing estimated operational downtime prevented by security actions against operational downtime caused by security actions. |
| **Formula** | Estimated Downtime Prevented (hours) / Downtime Caused by Security (hours) |
| **Collection Method** | Downtime Prevented: estimated by OT Engineering for each incident detected before impact. Downtime Caused: tracked for false-positive-driven shutdowns, security tool impacts, and security-driven maintenance overruns. |
| **Target** | Ratio >5:1. If ratio <1:1, the programme has a fundamental problem. |
| **Reporting Frequency** | Quarterly |
| **Start At Maturity Level** | Level 3 |
| **Trend Interpretation** | Declining ratio indicates security actions are causing more disruption. Investigate whether FP rate is rising, tool deployment is impacting OT systems, or security-driven maintenance is excessive. |

### OM-05: Hunts Conducted and Findings

| Field | Value |
|-------|-------|
| **Definition** | Number of structured threat hunting operations conducted in the reporting period, with categorised outcomes. |
| **Formula** | Count of completed hunts. For each: hypothesis, methodology, outcome (True Positive / Detection Improvement / No Finding / Gap Documented). |
| **Collection Method** | Hunt operation logs using the hunt documentation template from Chapter 9. |
| **Target** | ≥1 per month at Level 4. ≥2 per month at Level 5. |
| **Reporting Frequency** | Quarterly |
| **Start At Maturity Level** | Level 4 |
| **Trend Interpretation** | Hunts consistently finding "nothing" may indicate good security posture or poor hypothesis quality. Cross-reference with intelligence to assess whether hypotheses are well-targeted. |

### OM-06: Exercises Completed

| Field | Value |
|-------|-------|
| **Definition** | Number and type of security exercises completed in the reporting period. |
| **Formula** | Count by type: Tabletop, Functional, Purple Team, Red Team. Each exercise must have documented findings and tracked action items to count. |
| **Collection Method** | Exercise records and reports. |
| **Target** | Tabletop: ≥4 per year (quarterly). Purple Team: ≥1 per year. Functional: ≥1 per year. |
| **Reporting Frequency** | Quarterly |
| **Start At Maturity Level** | Level 2 (tabletop only); Level 4 (purple team) |
| **Trend Interpretation** | Exercises that produce no findings may indicate mature capability or insufficiently challenging scenarios. Review scenario design. |

---

## Collaboration Metrics

### CM-01: CSIRT Assembly Time

| Field | Value |
|-------|-------|
| **Definition** | Time from incident declaration (Severity 1 or 2) to full CSIRT engagement, including representatives from all required functions (IT Security, OT Engineering, Operations, and any additional roles per the CSIRT Charter). |
| **Formula** | Time of last required participant engagement − Time of incident declaration |
| **Collection Method** | Measured during both real incidents and exercises. Communication logs, incident management platform timestamps. |
| **Target** | Severity 1: <30 minutes. Severity 2: <60 minutes. |
| **Reporting Frequency** | Per incident/exercise; trended quarterly |
| **Start At Maturity Level** | Level 3 |
| **Trend Interpretation** | Consistently exceeding target indicates contact roster is stale, notification processes are ineffective, or CSIRT members do not treat assembly as a priority. |

### CM-02: Joint Training Sessions

| Field | Value |
|-------|-------|
| **Definition** | Number of cross-functional training events completed involving both IT Security and OT Engineering (or Operations) participants. |
| **Formula** | Count of sessions. Qualifying events: shadow engineering sessions, combined tabletop exercises, cross-training workshops, joint incident simulations, plant floor visits by SOC analysts. |
| **Collection Method** | Training records. Must include attendance from both IT Security and OT Engineering/Operations. |
| **Target** | ≥6 per year (approximately bimonthly). |
| **Reporting Frequency** | Quarterly |
| **Start At Maturity Level** | Level 3 |
| **Trend Interpretation** | Consistency matters more than volume. Regular engagement builds trust; sporadic engagement does not. |

### CM-03: Engineering Collaboration Score

| Field | Value |
|-------|-------|
| **Definition** | Qualitative assessment of the quality of collaboration between the SOC and engineering/operations teams. Gathered through anonymous quarterly surveys of both SOC and engineering team members. |
| **Formula** | Average score on a 1–5 Likert scale across survey questions, tracked separately for SOC respondents and engineering respondents. |
| **Collection Method** | Anonymous quarterly survey (5–10 questions covering communication quality, trust, responsiveness, mutual respect, perceived value). |
| **Target** | ≥3.5 average. No individual question below 3.0. |
| **Reporting Frequency** | Quarterly |
| **Start At Maturity Level** | Level 3 |
| **Trend Interpretation** | Declining scores are an early warning of cultural friction. Investigate before it manifests as operational problems. A divergence between SOC and engineering scores indicates one side feels the collaboration is less effective. |

---

## Business Metrics

### BM-01: Cyber Risk Score Reduction

| Field | Value |
|-------|-------|
| **Definition** | Reduction in assessed cyber risk to OT operations, expressed through the organisation's risk framework. |
| **Formula** | (Previous Period Risk Score − Current Period Risk Score) / Previous Period Risk Score × 100 |
| **Collection Method** | Risk assessment output from the organisation's risk management process. OT-specific risk items tracked separately. |
| **Target** | Measurable reduction year-over-year, linked to specific capability improvements. |
| **Reporting Frequency** | Annually (or aligned with risk assessment cycle) |
| **Start At Maturity Level** | Level 4 |
| **Trend Interpretation** | Risk score should decrease as maturity increases. If risk score increases despite capability improvements, the threat landscape may be evolving faster than the programme — review CTI input. |

### BM-02: Audit Findings Reduction

| Field | Value |
|-------|-------|
| **Definition** | Reduction in security-related audit findings over time, including regulatory assessments (NCSC CAF, NIS 2), internal audits, and insurance assessments. |
| **Formula** | Count of findings by severity, compared period-over-period. Track open, closed, and new findings. |
| **Collection Method** | Audit reports and finding registers. |
| **Target** | Decreasing trend in total findings. No repeat findings (previously identified and remediated issues should not recur). |
| **Reporting Frequency** | Per audit; trended annually |
| **Start At Maturity Level** | Level 3 |
| **Trend Interpretation** | Repeat findings indicate the improvement cycle is not closing the loop. Investigate whether AAR recommendations are being implemented. |

### BM-03: Compliance Score

| Field | Value |
|-------|-------|
| **Definition** | Organisation's score against relevant regulatory frameworks, expressed as profile status for each applicable control. |
| **Formula** | Framework-specific (e.g., NCSC CAF: count of Indicators of Good Practice at each profile level; NIS 2: compliance percentage against Article 21 requirements). |
| **Collection Method** | Regulatory assessment results. |
| **Target** | Improving trend. Specific targets aligned with regulatory expectations and organisational risk appetite. |
| **Reporting Frequency** | Per assessment; trended annually |
| **Start At Maturity Level** | Level 3 |
| **Trend Interpretation** | Compliance improvement should track maturity improvement. Chapter 4 maps book chapters to framework requirements — use this to identify which capability improvements drive which compliance improvements. |

### BM-04: Insurance Premium Impact

| Field | Value |
|-------|-------|
| **Definition** | Changes in cyber insurance premiums attributable to improved OT security posture. |
| **Formula** | (Current Premium − Previous Premium) / Previous Premium × 100. Adjust for market-wide premium changes to isolate the organisation-specific impact. |
| **Collection Method** | Insurance renewal data. Discussions with broker and underwriter to identify which security improvements influenced the premium. |
| **Target** | Stable or declining premiums despite market trends. Documented recognition of security improvements by underwriter. |
| **Reporting Frequency** | Annually (at insurance renewal) |
| **Start At Maturity Level** | Level 4 |
| **Trend Interpretation** | Premium reductions directly attributable to security improvements are powerful evidence for continued investment. Document the causal chain. |

---

## Metrics Implementation Priority by Maturity Level

| Maturity Level | Metrics to Track |
|----------------|-----------------|
| **Level 2** | TM-04 (OT FP Rate), OM-06 (Exercises — tabletop only) |
| **Level 3** | Add: TM-01 (Crown Jewel Coverage), TM-02 (ATT&CK Coverage), TM-03 (MTTD), OM-01 (MTTT), OM-02 (MTTEE), OM-03 (Incidents Before Impact), OM-04 (Downtime Ratio), CM-01 (CSIRT Assembly), CM-02 (Joint Training), CM-03 (Collaboration Score), BM-02 (Audit Findings), BM-03 (Compliance) |
| **Level 4** | Add: OM-05 (Hunts), OM-06 (Purple team), BM-01 (Risk Score), BM-04 (Insurance) |
| **Level 5** | All metrics. Benchmark against sector peers. |
