# OT Incident Escalation Template
# ================================================================
# Description: Structured format for SOC-to-Engineering escalation
#   communications. Provides engineering teams with the concise,
#   actionable information they need to assess operational impact.
#
# Usage: Complete this template when escalating any OT-related
#   incident to the engineering liaison or OT SME. Paste into
#   Teams message, email, or incident comments. Keep it concise
#   — engineering needs facts, not narrative.
#
# Reference: Chapter 11 — Purpose-Built Incident Response
# ================================================================

---

## Escalation Communication

```
=====================================================
OT SECURITY ESCALATION — [SEV-X] — [INCIDENT ID]
=====================================================

TIME:       [Date/Time of escalation]
ANALYST:    [Your name and contact number]
INCIDENT:   [Sentinel Incident ID / Link]

--- WHAT WAS DETECTED ---
Alert:      [Alert title]
Source:     [SIEM / EDR / NDR / Suricata / Zeek / Manual]
Technique:  [ATT&CK for ICS technique ID and name]
Timestamp:  [When the activity occurred]

--- WHICH ASSET IS AFFECTED ---
Hostname:   [Asset hostname]
IP Address: [IP address]
Purdue Level: [L0 / L1 / L2 / L3 / L3.5]
Crown Jewel: [Tier 1 / Tier 2 / Tier 3 / Tier 4 / Tier 5]
Device Type: [PLC / HMI / Engineering WS / SCADA / Historian / etc.]
Process:    [Physical process this asset supports]
Owner:      [Engineering contact from OT_AssetRegister]

--- CURRENT STATUS ---
Production: [Running normally / Degraded / Disrupted / Unknown]
Safety:     [Normal / Under assessment / Alarm active / SIS bypassed]
Operators:  [Reporting normal / Reporting anomalies — specify]

--- SOC ASSESSMENT ---
Confidence: [High / Medium / Low]
Assessment: [Brief assessment — e.g., "Suspected unauthorised remote 
             access via compromised vendor credentials. No evidence 
             of process manipulation yet."]
Stage:      [ICS Kill Chain stage if applicable]

--- WHAT WE NEED FROM ENGINEERING ---
☐ Operational impact assessment for proposed containment
☐ Maintenance window validation (is this expected activity?)
☐ Process safety assessment
☐ PLC logic validation against golden image
☐ Confirm whether observed [specific activity] is expected
☐ Other: [specify]

--- RECOMMENDED NEXT ACTION ---
[SOC's recommendation — e.g., "Recommend EDR isolation of 
engineering workstation after confirming no active PLC sessions.
Requesting engineering assessment of operational impact."]

--- URGENCY ---
[Immediate response required / Response within 30 min / 
Advisory — response within 2 hours]

=====================================================
NEXT UPDATE: [Time] or sooner if status changes.
SOC CONTACT: [Analyst name] — [Phone] — [Teams handle]
=====================================================
```

---

## Usage Notes

**When to use this template:**
- Any incident involving assets at Purdue Levels 0–3
- Any incident involving Tier 1 or Tier 2 crown jewel assets
- Any incident where the SOC cannot independently determine operational context
- Any incident where containment actions may affect the physical process

**When NOT to use this template:**
- Standard IT incidents with no OT connection
- Incidents fully resolved at Purdue Levels 4–5
- Informational alerts that have been triaged and closed

**Distribution:**
- Primary: OT SME or Engineering Liaison (as per CSIRT roster)
- CC: SOC Manager, relevant process/safety engineer
- For SEV-1/SEV-2: Additionally notify Operations Manager and CISO

**Response expectations:**
- SEV-1: Engineering response within 15 minutes
- SEV-2: Engineering response within 30 minutes  
- SEV-3: Engineering response within 2 hours
- SEV-4: Engineering response within next business day
