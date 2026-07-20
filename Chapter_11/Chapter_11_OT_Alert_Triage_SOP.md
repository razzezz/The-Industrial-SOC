# OT Alert Triage Standard Operating Procedure
# ================================================================
# Description: Step-by-step procedure for triaging alerts involving
#   OT assets. Codifies the four-dimension triage framework into
#   an analyst-actionable process. Extends standard IT triage with
#   consequence assessment, operational context, and engineering
#   escalation paths.
#
# Usage: Mandatory procedure for all SOC analysts when triaging
#   alerts tagged with "OT-Environment" by Sentinel automation.
#   Print and display at SOC analyst workstations.
#
# Prerequisites: OT_AssetRegister watchlist populated (Chapter 6),
#   OT_CrownJewels watchlist populated (Chapter 6),
#   OT_MaintenanceWindows watchlist maintained (Chapter 7),
#   Sentinel automation rules enriching OT incidents (UC-IR-001)
#
# Related: Chapter_11_OT_Incident_Severity_Matrix.md
#          Chapter_11_OT_Escalation_Template.md
#          Chapter_11_Safe_Unsafe_Actions_Reference.md
# ================================================================

## SCOPE

This SOP applies to all alerts and incidents in Microsoft Sentinel that
involve OT assets, identified by the presence of the "OT-Environment"
tag applied by the Sentinel automation rule (UC-IR-001). If no OT tag
is present AND the analyst has no reason to believe OT assets are
involved, standard IT triage procedures apply.

---

## STEP 1 — INITIAL ASSESSMENT

**Objective**: Determine whether this alert involves OT assets and
establish the initial assessment context.

1.1. Read the alert title, assigned severity, and mapped MITRE ATT&CK
     technique.

1.2. Check for the "OT-Environment" tag.
     - **If OT-Environment tag is PRESENT** → Proceed to Step 2.
     - **If OT-Environment tag is ABSENT** → Check whether any entity
       IPs or hostnames appear in the OT_AssetRegister watchlist
       manually. If they do, flag the automation gap and proceed to
       Step 2. If they do not, proceed with standard IT triage.

1.3. Note the alert source:
     - Sentinel KQL analytics rule → Note rule ID
     - EDR (Defender for Endpoint) → Note alert type and severity
     - Network IDS (Suricata/Zeek) → Note signature or notice type
     - Defender for IoT → Note alert category
     - Manual report → Note reporter and initial description

---

## STEP 2 — OT CONTEXT RETRIEVAL

**Objective**: Gather all available OT context for the affected
asset(s) before making triage decisions.

2.1. Review the enrichment data appended by the automation rule:

| Field | Source | Value |
|-------|--------|-------|
| Purdue Level | OT_AssetRegister | L__ |
| Crown Jewel Tier | OT_CrownJewels | Tier __ |
| Device Type | OT_AssetRegister | [PLC/HMI/EWS/SCADA/Historian/etc.] |
| Responsible Engineer | OT_AssetRegister | [Name] |
| Device Function | OT_AssetRegister | [Brief description] |

2.2. Check the incident tasks for maintenance window correlation:
     - **If maintenance window IS active** for the affected assets →
       Note the MaintenanceID, EngineerName, and ExpectedProtocols.
       Compare the observed activity against expected maintenance
       activity.
     - **If no maintenance window is active** → Note this explicitly.
       Activity involving ICS write commands or unusual access patterns
       outside maintenance windows requires elevated scrutiny.

2.3. If the OT_AssetRegister does not contain the affected asset:
     - This is a previously unknown device on the OT network.
     - Escalate to OT SME immediately regardless of other triage
       dimensions.
     - Create a task to add the device to the asset register.

---

## STEP 3 — CONSEQUENCE ASSESSMENT

**Objective**: Assess the potential physical consequence if this
activity is malicious and succeeds. This step distinguishes OT triage
from standard IT triage.

3.1. Based on the device type and Purdue Level, assess potential
     consequences:

| Purdue Level | Device Types | Potential Consequences |
|-------------|-------------|----------------------|
| L0 (Process) | Sensors, actuators | Loss of Safety, physical damage |
| L1 (Control) | PLCs, RTUs, DCS controllers | Loss of Control, Loss of Safety |
| L2 (Supervisory) | HMIs, SCADA servers, historians | Loss of View, Loss of Control |
| L3 (Operations) | Engineering workstations, file servers | Staging for deeper compromise |
| L3.5 (IDMZ) | Jump hosts, data diodes, relay servers | Boundary breach, pivot point |
| L4–5 (Enterprise) | Corporate IT systems | Standard IT impact |

3.2. Classify the potential consequence:

- **Loss of Safety**: Activity could compromise Safety Instrumented
  Systems or bypass safety interlocks. → **ALWAYS Severity 1.**
- **Loss of Control**: Activity could prevent operators from sending
  commands to the process. → **Severity 1 or 2** depending on
  redundancy.
- **Loss of View**: Activity could prevent operators from monitoring
  process status. → **Severity 2 or 3** depending on backup
  visibility.
- **No direct OT consequence**: Activity affects OT-adjacent IT
  systems without direct process impact. → **Severity 3 or 4.**

3.3. Consider cascading effects:
     - Could compromise of this system lead to compromise of
       higher-criticality systems? (Lateral movement potential)
     - Is this system on a known attack path to crown jewel assets?
       (Reference Chapter 10 attack path analysis)

---

## STEP 4 — TRIAGE DECISION

**Objective**: Apply the triage decision framework to determine
priority, response timeline, and escalation path.

4.1. Apply the following decision logic:

### Tier 1 Safety Systems
**IF** Crown Jewel Tier = 1 (Safety Systems):
- **Action**: ALWAYS escalate to OT SME immediately
- **Action**: ALWAYS notify Engineering Liaison
- **Response target**: 15 minutes
- **Severity**: 1 (Critical)

### Tier 2 Process Control — High Confidence
**IF** Crown Jewel Tier = 2 AND Indicator Confidence = High:
- **Action**: Escalate to Tier 2 analyst + OT SME
- **Action**: Notify Engineering Liaison
- **Response target**: 30 minutes
- **Severity**: 2 (High)

### Tier 2 Process Control — Lower Confidence, No Maintenance
**IF** Crown Jewel Tier = 2 AND Indicator Confidence = Low/Medium
AND No active maintenance window:
- **Action**: Investigate at Tier 2
- **Action**: Consult OT SME if indicators develop
- **Response target**: 1 hour
- **Severity**: 3 (Medium)

### Tier 3–5 — High Confidence
**IF** Crown Jewel Tier = 3/4/5 AND Indicator Confidence = High:
- **Action**: Standard Tier 2 investigation
- **Action**: Consult OT SME for operational context
- **Response target**: 1 hour
- **Severity**: 3 (Medium)

### Tier 3–5 — Lower Confidence, Maintenance Active
**IF** Crown Jewel Tier = 3/4/5 AND Indicator Confidence = Low/Medium
AND Maintenance window is active:
- **Action**: Correlate with maintenance activity
- **Action**: Close if consistent with documented maintenance
- **Response target**: 4 hours
- **Severity**: 4 (Low) — if correlated with maintenance

### Default
- **Action**: Standard IT triage procedures
- **Action**: Enrich with OT context from watchlists
- **Response target**: Per standard SLA

4.2. Document the triage decision in the Sentinel incident:
     - Assigned severity and rationale
     - Response target
     - Escalation path activated (if any)
     - Maintenance window correlation result

---

## STEP 5 — INVESTIGATION

**Objective**: Investigate the alert using OT-appropriate techniques
and data sources.

5.1. **Network Session Analysis** — Query ASIM-normalised
     `_Im_NetworkSession` for the affected asset:
     - Communication partners (who is this device talking to?)
     - Protocol usage (expected vs. unexpected protocols)
     - Volume and timing patterns
     - Comparison against known communication baseline

5.2. **ICS Protocol Analysis** — Review Zeek ICS protocol logs:
     - Modbus function codes (read vs. write vs. diagnostic)
     - DNP3 objects and functions
     - S7Comm/OPC-UA operations
     - Compare against expected operations for the device type
       and current maintenance status

5.3. **EDR Telemetry** (for systems with EDR deployed):
     - Process creation timeline
     - Network connections initiated by processes
     - File modifications
     - Registry changes
     - User logon events

5.4. **Authentication Analysis** — Query `_Im_Authentication`:
     - Logon events to the affected system
     - Source systems/IPs for authentication
     - Account usage patterns (normal hours vs. off-hours)
     - Failed logon attempts preceding successful logons

5.5. **Cross-boundary Correlation** — Check for related activity
     across the IT/OT boundary:
     - Did the same user/IP authenticate to IT systems?
     - Is there related EDR activity on engineering workstations?
     - Are there matching indicators in the IDMZ logs?

---

## STEP 6 — ESCALATION OR CLOSURE

**Objective**: Determine whether the investigation warrants escalation
to the CSIRT or can be closed.

### Escalation Criteria

Escalate to OT SME and Engineering Liaison if ANY of the following:

- [ ] Investigation confirms or cannot rule out malicious activity
      involving OT assets at Purdue Levels 0–2
- [ ] Unauthorised ICS write commands detected
- [ ] New/unknown device detected on OT network
- [ ] Credential compromise affecting accounts with OT access
- [ ] Activity pattern matches known threat actor TTP
- [ ] Multiple correlated alerts across IT/OT boundary
- [ ] Any indicator of compromise to Safety Instrumented Systems

### Closure Criteria

Close the incident (with documentation) if ALL of the following:

- [ ] Activity is confirmed as legitimate and expected
- [ ] Activity correlates with documented maintenance window
- [ ] No indicators of compromise found after thorough investigation
- [ ] OT SME concurs with closure (for Tier 1–2 assets)

### Documentation Requirements

Regardless of outcome, document in the Sentinel incident:

- Triage rationale (which decision path was followed)
- Investigation steps taken and findings
- Escalation decision and rationale
- If closed: confirmation that activity is legitimate, with evidence
- If escalated: summary provided to OT SME/Engineering Liaison
  using the OT Incident Escalation Template

*(See: Chapter_11_OT_Escalation_Template.md)*
