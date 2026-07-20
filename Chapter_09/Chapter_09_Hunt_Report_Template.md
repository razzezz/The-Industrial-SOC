# Hunt Report Template
# ================================================================
# Description: Comprehensive template for documenting threat hunt
#   execution, findings, and recommendations. Essential for audit
#   evidence, knowledge sharing, and feeding hunt intelligence back
#   into the detection engineering and CTI programmes.
#
# Usage: Complete one report per executed hunt. Store in the hunting
#   operations log alongside the hypothesis template.
#
# Regulatory Note: NCSC CAF v4.0 Contributing Outcome C2.b requires
#   documented evidence of structured threat hunting activity. This
#   template provides that evidence.
#
# Reference: Chapter 9 — The OT Threat Hunting Mindset
# ================================================================

## HUNT IDENTIFICATION

- **Hunt ID**: Hunt-ICS-[sequential number]
- **Hypothesis Title**: [From hypothesis template]
- **Hunter(s)**: [Analyst name(s)]
- **Date Executed**: [Date]
- **Duration**: [Total hours spent on this hunt]
- **Status**: [Complete — Confirmed | Complete — Refuted | Complete — Inconclusive | Ongoing]

## EXECUTIVE SUMMARY

_Two to three sentences summarising the hunt objective, approach, and outcome. Written for SOC leadership and compliance audiences._

[e.g., "This hunt investigated the hypothesis that unauthorised firmware modifications had been performed on PLCs in the water treatment process area. Analysis of 30 days of Zeek Modbus logs identified zero firmware-related operations outside documented maintenance windows. The hypothesis is refuted for the hunting period, and a scheduled detection rule (UC-ICS-010) has been recommended to provide continuous monitoring."]

## HYPOTHESIS RECAP

- **Hypothesis**: [The specific hypothesis statement]
- **ATT&CK for ICS Techniques**: [Technique IDs]
- **ICS Kill Chain Stage**: [Stage]
- **Rationale**: [Brief summary of why this hunt was prioritised]
- **Derived From**: [Detection gap | Threat intelligence | Operational observation | Purple team | Ad hoc]

## EXECUTION DETAILS

### Data Sources Queried

| Data Source | Table / Location | Lookback Period | Records Analysed | Data Quality |
|---|---|---|---|---|
| [e.g., Zeek Modbus logs] | [Zeek_modbus_CL] | [30 days] | [1,247,832] | [Good / Gaps identified] |
| [e.g., OT Asset Register] | [OT_AssetRegister watchlist] | [Current] | [142 assets] | [Good] |
| [e.g., EDR Process Events] | [DeviceProcessEvents] | [14 days] | [89,421] | [Partial — 3 workstations not reporting] |

### Queries Executed

| Query Reference | Description | Results | Notes |
|---|---|---|---|
| [Hunt-ICS-001 — Main] | [Firmware operation detection with maintenance exclusion] | [X results returned] | [See detailed results below] |
| [Hunt-ICS-001 — Corr.] | [EDR correlation for source workstation activity] | [X results returned] | [] |

### Data Gaps Identified
_Document any data sources that were unavailable or incomplete during the hunt._

- [e.g., "Zeek Modbus detailed logging (register-level) was not enabled for 4 of 12 PLCs — these devices are on a network segment without a Zeek sensor. Recommendation: Deploy sensor per Chapter 7 architecture."]

## FINDINGS

### Finding 1: [Title]
- **Severity**: [Critical | High | Medium | Low | Informational]
- **Description**: [Detailed description of the finding]
- **Evidence**: [Specific log entries, query results, or artefacts that support the finding]
- **Affected Assets**: [Device names, IPs, Purdue levels, crown jewel tiers]
- **ATT&CK for ICS Mapping**: [Technique(s) confirmed or suspected]
- **Assessment**: [Confirmed malicious | Suspicious — requires further investigation | Benign — documented as false positive source | Environmental — operational issue, not security]

### Finding 2: [Title]
_Repeat for each finding._

### No Findings (Negative Result)
_If no findings were identified, document this explicitly. Negative results are valuable — they provide assurance and contribute to the coverage assessment._

- **Scope Confirmed**: [What was searched and found clean]
- **Confidence Level**: [High — comprehensive data, thorough analysis | Medium — some data gaps | Low — significant data gaps limit conclusions]
- **Assurance Statement**: [e.g., "No firmware operations were observed outside documented maintenance windows for any of the 87 PLCs with Zeek Modbus logging coverage during the 30-day hunting period. This provides high confidence that unauthorised firmware modification has not occurred on monitored devices during this period."]

## ANALYST ASSESSMENT

_The hunter's professional judgment on the overall outcome._

- **Hypothesis Outcome**: [Confirmed | Refuted | Inconclusive]
- **Confidence**: [High | Medium | Low]
- **Reasoning**: [Why the analyst reached this conclusion]
- **Caveats**: [Limitations that affect the conclusion — e.g., "This assessment is limited to devices with Zeek Modbus logging coverage. 4 PLCs on the unmonitored segment could not be assessed."]

## RECOMMENDATIONS

### Immediate Actions
_Actions required now based on hunt findings._

| # | Action | Owner | Priority | Due Date |
|---|---|---|---|---|
| 1 | [e.g., Deploy Zeek sensor to unmonitored OT segment] | [SOC Engineering] | [High] | [Date] |
| 2 | [e.g., Validate PLC firmware on unmonitored devices] | [OT Engineering] | [Medium] | [Date] |

### Detection Engineering Recommendations
_Can this hunt be converted to a scheduled detection rule or improved?_

- **New Detection Rule**: [e.g., "Convert Hunt-ICS-001 firmware detection to scheduled analytic rule UC-ICS-010 running daily with 30-day lookback."]
- **Existing Rule Tuning**: [e.g., "UC-ICS-002 maintenance window exclusion should be expanded to include the newly documented annual firmware validation windows."]
- **Signature Updates**: [e.g., "Add Suricata signatures for S7Comm programme upload operations to complement existing Modbus coverage."]

### Hunting Programme Recommendations
_Improvements to the hunting process itself._

- **Follow-Up Hunts**: [e.g., "Schedule Hunt-ICS-002 (covert channels) for next month — addresses the adjacent Collection tactic gap."]
- **Data Collection Improvements**: [e.g., "Enable Zeek Modbus detailed logging (register-level) on all monitored segments."]
- **Baseline Updates**: [e.g., "Update communication baseline to include the firmware validation traffic pattern observed during MW-2026-0001."]

### CTI Feedback
_Intelligence generated by this hunt that should feed back into the CTI programme (Chapter 10)._

- **New IOCs**: [Any indicators of compromise identified]
- **TTP Observations**: [Any adversary techniques confirmed or ruled out]
- **Coverage Assessment Update**: [How does this hunt change the ATT&CK for ICS coverage status?]

## METRICS

| Metric | Value |
|---|---|
| Hunt Duration (hours) | [X] |
| Data Sources Queried | [X] |
| Records Analysed | [X] |
| Findings Identified | [X] |
| Findings Confirmed Malicious | [X] |
| Detection Rules Created/Updated | [X] |
| ATT&CK Techniques Investigated | [X] |
| Coverage Gaps Addressed | [X] |

## APPENDICES

### Appendix A: Full Query Results
_Attach or reference the raw query output for reproducibility._

### Appendix B: Supporting Evidence
_Screenshots, packet captures, log extracts, or other artefacts._

### Appendix C: Related Hunts
_References to prior or planned hunts addressing related techniques._

| Hunt ID | Title | Date | Outcome | Relationship |
|---|---|---|---|---|
| [Hunt-ICS-XXX] | [Title] | [Date] | [Outcome] | [e.g., "Addresses adjacent technique in same tactic"] |
