# Integration Health Check

## Quarterly Assessment of Deployed Security Tool Effectiveness

**Assessment Period:** Q__ 20__
**Assessor(s):** _______________
**Date Completed:** _______________

---

## Instructions

This health check should be completed quarterly for every security tool deployed in the OT security programme. Each tool is assessed across five dimensions. A tool that scores poorly should be investigated — either the integration needs improvement, or the tool's continued deployment should be questioned.

**Scoring Guide:**
- **5 — Excellent:** Fully contributing, no issues
- **4 — Good:** Minor issues, not affecting operations
- **3 — Adequate:** Functional but improvement needed
- **2 — Poor:** Significant issues affecting value
- **1 — Critical:** Not contributing meaningfully

---

## Tool Assessment

*Copy this section for each deployed tool.*

### Tool: _______________

| Field | Value |
|---|---|
| **Vendor** | |
| **Version** | |
| **Capability provided** | |
| **Tier** | ☐ 1 (Essential) ☐ 2 (Enhanced) ☐ 3 (Advanced) |
| **Deployment locations** | |
| **Responsible owner** | |

---

#### Dimension 1: Data Flowing

*Is the tool's telemetry being ingested into the SIEM continuously and reliably?*

| Check | Status | Notes |
|---|---|---|
| Data connector / ingestion pipeline active | ☐ Yes ☐ No ☐ Intermittent | |
| Last data point received | Timestamp: _____ | |
| Any ingestion gaps in the assessment period? | ☐ None ☐ Minor (< 1hr total) ☐ Significant (> 1hr) | Duration: _____ |
| ASIM parsers in place and functioning? | ☐ Yes ☐ Partial ☐ No | |
| Data volume consistent with expectations? | ☐ Yes ☐ Higher ☐ Lower | |
| Log format changes requiring parser updates? | ☐ None ☐ Minor ☐ Breaking | |

**Score: ___ / 5**

**Action Required:** _______________

---

#### Dimension 2: Context Enriched

*Are alerts from this tool enriched with OT operational context?*

| Check | Status | Notes |
|---|---|---|
| Alerts enriched with OT_AssetRegister data? | ☐ Yes ☐ Partial ☐ No | |
| Asset classification included (device type, Purdue level)? | ☐ Yes ☐ No | |
| Crown jewel tier displayed? | ☐ Yes ☐ No | |
| Engineering owner identified in alerts? | ☐ Yes ☐ No | |
| Maintenance window context available? | ☐ Yes ☐ No | |
| Context enrichment automated (not manual lookup)? | ☐ Yes ☐ Partial ☐ No | |

**Score: ___ / 5**

**Action Required:** _______________

---

#### Dimension 3: Rules Active

*How many active detection rules use this tool's data, and what do they cover?*

| Metric | Value |
|---|---|
| Active detection rules using this tool's data | Count: _____ |
| ATT&CK for ICS techniques covered by these rules | List: |
| ATT&CK for ICS tactics covered | _____ / 12 |
| Hunting queries using this tool's data | Count: _____ |
| New rules created this quarter | Count: _____ |
| Rules retired or disabled this quarter | Count: _____ |
| Date of most recent rule creation/update | _____ |

**Score: ___ / 5**

**Action Required:** _______________

---

#### Dimension 4: Investigations Supported

*Is this tool's data being used effectively during investigations?*

| Metric | Value |
|---|---|
| Investigations that used this tool's data this quarter | Count: _____ |
| True positive detections attributed to this tool | Count: _____ |
| False positive rate for this tool's alerts | _____ % |
| Analyst feedback on data quality | ☐ Excellent ☐ Good ☐ Adequate ☐ Poor |
| Analyst feedback on data availability during investigation | ☐ Always available ☐ Usually ☐ Sometimes ☐ Rarely |
| Any investigation impeded by tool data issues? | ☐ No ☐ Yes — describe: |

**Score: ___ / 5**

**Action Required:** _______________

---

#### Dimension 5: Maintenance Current

*Is the tool being maintained effectively?*

| Check | Status | Notes |
|---|---|---|
| Software version current (within vendor support)? | ☐ Yes ☐ No — version gap: _____ | |
| Signature/rule updates applied? | ☐ Current ☐ Behind by: _____ | |
| Health monitoring configured with alerting? | ☐ Yes ☐ Partial ☐ No | |
| Sensor failures detected and resolved this quarter? | Count: _____ Avg resolution: _____ | |
| Licence status | ☐ Current ☐ Expiring within 90 days ☐ Expired | Renewal date: _____ |
| Vendor support engagement this quarter | ☐ None needed ☐ Engaged — resolved ☐ Engaged — unresolved | |
| Capacity / performance issues? | ☐ None ☐ Minor ☐ Significant | |

**Score: ___ / 5**

**Action Required:** _______________

---

### Tool Summary

| Dimension | Score |
|---|---|
| Data Flowing | /5 |
| Context Enriched | /5 |
| Rules Active | /5 |
| Investigations Supported | /5 |
| Maintenance Current | /5 |
| **Average Score** | **/5** |

**Overall Assessment:**
- ☐ **Healthy (≥ 4.0)** — Tool is fully contributing to the security programme
- ☐ **Needs Attention (3.0–3.9)** — Specific improvements required (document below)
- ☐ **At Risk (2.0–2.9)** — Significant integration or effectiveness issues
- ☐ **Review for Removal (< 2.0)** — Tool is not contributing meaningfully

**Improvement Actions:**

| Action | Owner | Deadline |
|---|---|---|
| | | |
| | | |
| | | |

---

## Quarterly Summary Dashboard

*Complete this summary across all deployed tools.*

| Tool | Capability | Tier | Data Flowing | Context | Rules | Investigations | Maintenance | Average | Status |
|---|---|---|---|---|---|---|---|---|---|
| | | | /5 | /5 | /5 | /5 | /5 | /5 | |
| | | | /5 | /5 | /5 | /5 | /5 | /5 | |
| | | | /5 | /5 | /5 | /5 | /5 | /5 | |
| | | | /5 | /5 | /5 | /5 | /5 | /5 | |
| | | | /5 | /5 | /5 | /5 | /5 | /5 | |
| | | | /5 | /5 | /5 | /5 | /5 | /5 | |

**Programme-Wide Observations:**

_______________

**Tooling Changes Recommended:**

_______________

---

## Quarter-over-Quarter Trend

| Tool | Q__ Score | Q__ Score | Q__ Score | Q__ Score | Trend |
|---|---|---|---|---|---|
| | | | | | ↑ ↓ → |
| | | | | | ↑ ↓ → |
| | | | | | ↑ ↓ → |
| | | | | | ↑ ↓ → |

---

## Sign-Off

| Role | Name | Date |
|---|---|---|
| SOC Manager | | |
| OT Security SME | | |
| Security Director / CISO | | |
