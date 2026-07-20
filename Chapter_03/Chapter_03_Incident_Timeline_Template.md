# Incident Timeline Visualisation Template
# ================================================================
# Description: Structured template for reconstructing and
#   visualising the timeline of ICS cyber incidents. Use this
#   template when analysing historical incidents, conducting
#   after-action reviews, or briefing leadership on attack
#   progression through the ICS Cyber Kill Chain.
#
# Usage: Complete one template per incident. Map events against
#   the Purdue Model levels and the ICS Cyber Kill Chain stages
#   to identify detection opportunities and defensive gaps.
# ================================================================

## INCIDENT IDENTIFICATION

- **Incident Name**: [e.g., "BlackEnergy / Ukraine Power Grid 2015"]
- **Date(s)**: [Attack execution date and known intrusion period]
- **Attribution**: [Microsoft naming (Dragos alias) — e.g., "Seashell Blizzard (ELECTRUM)"]
- **Target Sector(s)**: [e.g., Power/Energy, Water, Manufacturing]
- **Target Geography**: [Country/region]
- **Impact Summary**: [One-sentence description of physical/operational impact]

---

## ICS CYBER KILL CHAIN MAPPING

### Stage 1: IT Intrusion and OT Access

| Timestamp / Phase | Event Description | Purdue Level | ATT&CK for ICS Technique | Detection Opportunity | Detected? (Y/N) |
|-------------------|-------------------|--------------|---------------------------|----------------------|-----------------|
| [Date/Phase] | [e.g., Spear-phishing email delivered] | Level 5 (Enterprise) | T0865 (Spear-Phishing Attachment) | Email gateway, EDR | |
| [Date/Phase] | [e.g., Credential harvesting via Mimikatz] | Level 4 (IT Network) | T0859 (Valid Accounts) | LSASS access monitoring | |
| [Date/Phase] | [e.g., Lateral movement to IDMZ jump host] | Level 3.5 (IDMZ) | T0886 (Remote Services) | UC-ICS-003 (IT/OT Boundary Traversal) | |
| | | | | | |
| | | | | | |

### Stage 2: ICS Attack Development and Execution

| Timestamp / Phase | Event Description | Purdue Level | ATT&CK for ICS Technique | Detection Opportunity | Detected? (Y/N) |
|-------------------|-------------------|--------------|---------------------------|----------------------|-----------------|
| [Date/Phase] | [e.g., Reconnaissance of SCADA systems] | Level 3 (Site Operations) | T0846 (Remote System Discovery) | UC-ICS-001 (Unauthorised Protocol Comms) | |
| [Date/Phase] | [e.g., PLC logic modification uploaded] | Level 1 (Controller) | T0821 (Modify Controller Tasking) | UC-ICS-002 (Write Outside Maintenance) | |
| [Date/Phase] | [e.g., Physical process disruption] | Level 0 (Physical) | T0831 (Manipulation of Control) | Process anomaly detection | |
| | | | | | |
| | | | | | |

---

## TIMELINE VISUALISATION

```
[Use the following format to create a visual timeline]

Time ──────────────────────────────────────────────────────────►

L5 (Enterprise)   ■ Initial Access
                   │
L4 (IT Network)    ├──■ Credential Theft ──■ Lateral Movement
                   │
L3.5 (IDMZ)       ├──────────■ Boundary Crossing
                   │
L3 (Site Ops)      ├─────────────■ SCADA Reconnaissance
                   │
L2 (Control)       ├────────────────■ HMI/EWS Access
                   │
L1 (Controller)    ├─────────────────────■ PLC Modification
                   │
L0 (Physical)      └──────────────────────────■ Process Impact

STAGE 1 ◄──────────────────────►  STAGE 2 ◄───────────────────►
```

---

## DWELL TIME ANALYSIS

| Phase | Start Date | End Date | Duration | Notes |
|-------|-----------|----------|----------|-------|
| Initial Access to IT Foothold | | | | |
| IT Lateral Movement | | | | |
| IT/OT Boundary Crossing | | | | |
| OT Reconnaissance | | | | |
| Attack Development | | | | |
| Attack Execution | | | | |
| **Total Dwell Time** | | | **[Total]** | |

---

## DETECTION GAP ANALYSIS

### What Was Detected (and When)

| Detection | Time After Initial Access | Method | Purdue Level |
|-----------|--------------------------|--------|--------------|
| | | | |
| | | | |

### What Was Missed (Detection Gaps)

| Adversary Action | Why It Was Missed | Required Telemetry | Applicable Detection Use Case |
|-----------------|-------------------|-------------------|-------------------------------|
| | | | |
| | | | |

---

## LESSONS FOR OUR ENVIRONMENT

### Applicable Threat Actor Assessment
- **Does this threat actor target our sector?** [Y/N — evidence]
- **Does this threat actor target our geography?** [Y/N — evidence]
- **Do we use the same products/protocols targeted?** [Y/N — specifics]
- **Risk assessment**: [High / Medium / Low relevance to our environment]

### Detection Coverage Assessment
For each ATT&CK for ICS technique used in this incident, assess current coverage:

| Technique ID | Technique Name | Current Detection Rule | Coverage Status |
|-------------|----------------|----------------------|-----------------|
| | | | ☐ Covered ☐ Partial ☐ Gap |
| | | | ☐ Covered ☐ Partial ☐ Gap |
| | | | ☐ Covered ☐ Partial ☐ Gap |
| | | | ☐ Covered ☐ Partial ☐ Gap |

### Priority Actions
1. [Highest-priority gap to close based on this incident analysis]
2. [Second priority]
3. [Third priority]

---

## REFERENCES

- **Primary Source(s)**: [CISA advisory, vendor report, academic paper]
- **ATT&CK for ICS Mapping**: [Link to MITRE ATT&CK page if available]
- **Related Intelligence**: [ISAC reports, sector-specific advisories]
