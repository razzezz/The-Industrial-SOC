# Hunting Hypothesis Template
# ================================================================
# Description: Structured template for documenting OT/ICS threat
#   hunting hypotheses. Ensures every hunt is structured, repeatable,
#   and auditable. Aligns with MITRE ATT&CK for ICS and the ICS
#   Kill Chain framework.
#
# Usage: Complete one template per hunting hypothesis before
#   executing the hunt. Store alongside hunt results in the
#   hunting operations log.
#
# Reference: Chapter 9 — The OT Threat Hunting Mindset
# ================================================================

## HYPOTHESIS IDENTIFICATION
- **Hunt ID**: Hunt-ICS-[sequential number]
- **Hypothesis Title**: [Descriptive title]
- **Hunter**: [Analyst name]
- **Date Created**: [Date]
- **Priority**: [Critical | High | Medium | Low]
- **Status**: [Draft | Approved | In Progress | Complete | Deferred]

## THE HYPOTHESIS

### Adversary Action (What)
_State the specific adversary activity you are searching for. Be precise — tie it to observable actions, not vague suspicions._

- **Hypothesis Statement**: [e.g., "An adversary has uploaded modified firmware to PLCs controlling the water treatment dosing process to establish persistence that survives a power cycle."]
- **ATT&CK for ICS Techniques**: [e.g., T0839 — Module Firmware, T0836 — Modify Program]
- **ICS Kill Chain Stage**: [Stage 1 — IT Intrusion | Boundary Traversal | Stage 2 — ICS Attack]
- **Tactic(s) Addressed**: [e.g., Persistence (TA0110), Impair Process Control (TA0106)]

### Rationale (Why)
_Explain why you believe this activity might be occurring. Link to threat intelligence, detection gaps, or operational observations._

- **Intelligence Source**: [e.g., CISA Advisory AA24-038a — Volt Typhoon, Dragos 2025 YIR, ISAC alert, internal incident]
- **Detection Gap**: [e.g., "ATT&CK coverage assessment shows no detection rules for Persistence (TA0110) — firmware modification is the highest-risk persistence technique for our environment."]
- **Environmental Factors**: [e.g., "Our PLCs have not had firmware validated against golden images in 18 months. Recent vendor advisory disclosed a firmware vulnerability in our PLC model."]
- **Threat Actor Relevance**: [e.g., "Mint Sandstorm-affiliated elements (XENOTIME) have demonstrated firmware-level attacks against SIS controllers in the petrochemical sector — our sector."]

### Data Sources (Where)
_Identify the specific data sources required to test this hypothesis. Be precise — table names, log sources, watchlists._

| Data Source | Table / Location | Required Fields | Available? |
|---|---|---|---|
| [e.g., Zeek Modbus logs] | [Zeek_modbus_CL] | [func_code_d, id_orig_h, id_resp_h, register_d] | [Yes/No/Partial] |
| [e.g., OT Asset Register] | [_GetWatchlist('OT_AssetRegister')] | [IPAddress, DeviceType, PurdueLevel, CrownJewelTier] | [Yes/No] |
| [e.g., Maintenance Windows] | [_GetWatchlist('OT_MaintenanceWindows')] | [AffectedAssets, StartTime, EndTime, Status] | [Yes/No] |
| [e.g., EDR Process Events] | [DeviceProcessEvents] | [FileName, ProcessCommandLine, DeviceName] | [Yes/No] |

- **Data Gaps**: [Document any data sources that would be ideal but are not currently available]
- **Lookback Period**: [e.g., 30 days — firmware changes are rare, longer lookback increases chance of detection]

### Analytical Approach (How)
_Describe the specific methodology for testing the hypothesis._

- **Query Strategy**: [e.g., "Query Zeek Modbus logs for function code 43 operations, exclude operations during active maintenance windows, enrich with asset context, and cross-reference with change management records."]
- **Baseline Comparison**: [e.g., "Compare firmware operation frequency against the 90-day historical baseline. Any firmware operations outside maintenance windows are anomalous."]
- **Enrichment Steps**: [e.g., "Join with OT_AssetRegister for crown jewel tier and Purdue level. Join with OT_MaintenanceWindows for maintenance context."]
- **Correlation**: [e.g., "Correlate firmware operations with EDR telemetry from the source workstation to identify the user and process responsible."]
- **Queries / Scripts**: [Reference the specific query files — e.g., "Hunt-ICS-001 in Chapter_09_Hunting_Queries.kql"]

## EXPECTED OUTCOMES

### If Confirmed (True Positive)
- **Immediate Actions**: [e.g., "Escalate to SOC leadership and OT engineering. Do NOT interact with the affected PLC — request engineering validate firmware integrity."]
- **Evidence Preservation**: [e.g., "Capture network traffic to/from affected PLC. Preserve EDR telemetry from source workstation. Request PLC memory dump through engineering."]
- **Escalation Path**: [e.g., "SOC Manager → OT Engineering Lead → CISO → Legal (if reportable incident)"]

### If Refuted (True Negative)
- **Documentation**: [Record negative finding — this provides assurance and contributes to coverage assessment]
- **Baseline Update**: [Update what "normal" looks like based on hunt observations]
- **Detection Opportunity**: [Can this hunt be converted to a scheduled detection rule?]

### If Inconclusive
- **Additional Data Needed**: [What additional data sources or enrichment would resolve the ambiguity?]
- **Follow-Up Hunt**: [Should a narrower follow-up hunt be scheduled?]
- **Engineering Consultation**: [Should findings be reviewed with OT engineering for operational context?]

## APPROVAL

_Hunting hypotheses targeting OT environments should be reviewed before execution to ensure the analytical approach does not risk interaction with live control systems._

- **Reviewed By**: [SOC Manager / Hunt Lead]
- **Approved**: [Yes / No / Conditional]
- **Conditions**: [Any restrictions on the hunt — e.g., "Do not query live PLCs directly. Use only passively collected log data."]
- **OT Engineering Notified**: [Yes / No — required for any hunt that may generate questions from engineering]
