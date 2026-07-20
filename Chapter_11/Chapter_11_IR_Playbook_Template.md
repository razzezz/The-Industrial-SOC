# OT Incident Response Playbook Template
# ================================================================
# Description: Customisable eight-phase playbook structure for OT 
#   incident response. Includes built-in safety assessment and 
#   cross-functional coordination checkpoints at each phase.
#
# Usage: Complete one playbook per scenario type. Pre-populate 
#   environment-specific details (asset names, contacts, network 
#   topology) before an incident occurs. Store in a location 
#   accessible during an incident — not in a system that may be 
#   unavailable during a network incident.
#
# Related: Chapter_11_Tabletop_Scenario_Library.md
#          Chapter_11_Safe_Unsafe_Actions_Reference.md
#          Chapter_11_OT_Incident_Severity_Matrix.md
# ================================================================

## PLAYBOOK IDENTIFICATION

- **Playbook ID**: PB-OT-[sequential number]
- **Scenario Type**: [e.g., Ransomware at IT/OT Boundary, Unauthorised PLC Logic Change, Credential Harvesting on HMI, Supply Chain Compromise, Insider Threat, Internet-Exposed OT]
- **Author**: [Name]
- **Date Created**: [Date]
- **Last Reviewed**: [Date]
- **Version**: [e.g., 1.0]
- **Status**: [Draft | Reviewed | Approved | In Use | Retired]
- **Approved By**: [CSIRT Lead / CISO / OT Engineering Lead]

---

## APPLICABILITY

- **Target Environment**: [e.g., Plant A SCADA network, Water treatment DCS, Substation automation]
- **Purdue Levels Involved**: [e.g., L2–L4]
- **Key Assets**: [List specific assets this playbook covers — hostnames, IPs, device types]
- **Relevant ATT&CK for ICS Techniques**: [e.g., T0855, T0836, T0859]
- **Known Threat Actors Using These Techniques**: [Microsoft naming — e.g., Volt Typhoon (VOLTZITE)]
- **Regulatory Considerations**: [e.g., NIS 2 Art. 23 reporting, NCSC CAF D1, sector-specific]

---

## PHASE 1: DETECTION

### Alert Source
- [ ] SIEM analytics rule (Sentinel KQL) — Rule ID: _______________
- [ ] EDR alert (Defender for Endpoint) — Alert type: _______________
- [ ] Network IDS (Suricata/Zeek) — Signature/notice: _______________
- [ ] Defender for IoT — Alert type: _______________
- [ ] Manual report from engineering
- [ ] External notification (ISAC, vendor, law enforcement)

### Initial Indicators
| Field | Value |
|-------|-------|
| Alert timestamp (UTC) | |
| Source IP(s) | |
| Destination IP(s) | |
| Protocol(s) | |
| ICS command(s) observed | |
| Process name(s) | |
| File hash(es) | |
| User account(s) | |
| EDR alert severity | |

### Automated Enrichment (from Sentinel Automation)
| Field | Value |
|-------|-------|
| OT-Environment tag applied | Yes / No |
| Purdue Level | |
| Crown Jewel Tier | |
| Device Type | |
| Responsible Engineer | |
| Active Maintenance Window | Yes / No — MW ID: _______ |

---

## PHASE 2: TRIAGE

### System Identification
| Question | Answer |
|----------|--------|
| Which OT systems are involved? | |
| What are their Purdue Levels? | |
| What are their Crown Jewel Tiers? | |
| Is EDR deployed on affected systems? | Yes / No / Partial |
| EDR mode on affected systems? | Detect-only / Active prevention |

### Impact Assessment
| Question | Answer |
|----------|--------|
| Is production currently affected? | None / Monitoring / Degraded / Disrupted |
| Is safety currently at risk? | None / Under assessment / Confirmed risk |
| Are operators aware of the issue? | Yes / No |
| Can operators maintain process control? | Yes / Degraded / No |

### Triage Decision (per OT Alert Triage Framework)
| Dimension | Assessment |
|-----------|------------|
| Indicator Confidence | Low / Medium / High |
| Asset Criticality | Tier 1 / Tier 2 / Tier 3 / Tier 4–5 |
| Potential Consequence | Loss of View / Loss of Control / Loss of Safety / None |
| Operational Context | Maintenance active / No maintenance / Unknown |

**Assigned Priority**: _______________
**Response Target**: _______________
**Assigned Analyst**: _______________

---

## PHASE 3: SAFETY ASSESSMENT

> **This phase is led by OT Engineering. SOC provides security context; OT Engineering assesses operational safety.**

### Safety Checklist
| Question | Assessment | Assessed By |
|----------|------------|-------------|
| Is the process currently in a safe and stable state? | Yes / No / Unknown | |
| What are the fail-safe positions for affected PLCs/controllers? | [Document per asset] | |
| If we lose network to affected PLCs, what state do they default to? | Hold last / Fail safe / Fail dangerous / Unknown | |
| Can operators maintain control via alternative means (backup HMI, local panels, manual)? | Yes / Degraded / No | |
| Are Safety Instrumented Systems operational and independent of affected network? | Yes / No / Unknown | |
| Is the process in a critical phase where disruption would cause equipment damage? | Yes / No | |
| Are redundant systems available and tested? | Yes / No / Partial | |

### Safety Assessment Outcome
- **Assessment**: Safe to proceed with containment / Defer containment — process risk too high / Controlled shutdown recommended
- **Assessed by**: [OT Engineer name]
- **Operations concurrence**: [Operations lead name]
- **Timestamp (UTC)**: _______________

---

## PHASE 4: CONTAINMENT

### Containment Options Assessment
| Option | Available? | Operational Impact | Risk if Executed | Risk if NOT Executed | Selected? |
|--------|-----------|-------------------|-----------------|---------------------|-----------|
| EDR network isolation | | | | | |
| VLAN/subnet isolation | | | | | |
| Firewall rule (block specific traffic) | | | | | |
| Switch port shutdown | | | | | |
| EDR process kill (specific process only) | | | | | |
| Physical disconnection | | | | | |
| Enhanced monitoring + deferred isolation | | | | | |
| Read-only mode (block writes, allow reads) | | | | | |

### Selected Containment Approach
- **Approach**: _______________
- **Rationale**: _______________
- **Assessed risk of this approach**: _______________
- **Assessed risk of alternatives not selected**: _______________

### Containment Authorisation

> **REQUIRED: All three roles must authorise containment actions affecting Purdue Levels 0–3**

| Role | Name | Authorised? | Method | Timestamp (UTC) |
|------|------|-------------|--------|-----------------|
| IT Security | | Yes / No | Verbal / Written | |
| OT Engineering | | Yes / No | Verbal / Written | |
| Plant Operations | | Yes / No | Verbal / Written | |
| Executive (if required) | | Yes / No | Verbal / Written | |

### Containment Execution
- **Executed by**: _______________
- **Execution time (UTC)**: _______________
- **Verification**: Containment confirmed effective? Yes / No
- **Post-containment observations**: _______________

---

## PHASE 5: ERADICATION

### Eradication Actions
| Action | Target System | Executed By | Timestamp | Result |
|--------|---------------|-------------|-----------|--------|
| EDR: Kill process | | | | |
| EDR: Quarantine file | | | | |
| EDR: Remove registry entry | | | | |
| Reimage from known-good media | | | | |
| Restore from validated backup | | | | |
| PLC: Load golden image (OT Eng only) | | | | |
| Credential: Reset compromised account | | | | |
| Credential: Rotate service account | | | | |

### Credential Reset Coordination
- **Accounts requiring reset**: _______________
- **Service account dependencies identified**: _______________
- **Reset sequence (to avoid disrupting control loops)**: _______________
- **Operations confirmed timing**: [Name] at [time UTC]

### Eradication Validation
| Check | Result | Verified By |
|-------|--------|-------------|
| No persistence mechanisms remain | Pass / Fail | |
| No unauthorised scheduled tasks, services, or autorun entries | Pass / Fail | |
| PLC logic matches golden image | Pass / Fail / N/A | |
| No adversary tools remain on disk | Pass / Fail | |
| EDR full scan clean | Pass / Fail / N/A | |

---

## PHASE 6: RECOVERY

### Recovery Sequence
| Step | System / Action | Dependencies | Executed By | Timestamp | Verified |
|------|----------------|-------------|-------------|-----------|----------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

### Operational Validation
| Check | Result | Verified By |
|-------|--------|-------------|
| Process readings are accurate and current | Pass / Fail | |
| Operator commands are executing correctly | Pass / Fail | |
| Communication links established (SCADA → PLC) | Pass / Fail | |
| Process is stable within normal parameters | Pass / Fail | |
| Operators confirm normal operation | Pass / Fail | |
| Safety systems confirm normal status | Pass / Fail | |

- **Recovery declared by**: _______________
- **Recovery time (UTC)**: _______________

---

## PHASE 7: FORENSICS

### Evidence Collection Checklist
| Evidence Type | Collected? | Location / Reference | Collected By | Chain of Custody Doc |
|---------------|-----------|---------------------|--------------|---------------------|
| EDR timeline data | | | | |
| EDR process trees | | | | |
| PCAP from IDMZ sensors | | | | |
| Zeek connection logs | | | | |
| Zeek ICS protocol logs | | | | |
| Suricata alert logs | | | | |
| Windows Security Event Logs | | | | |
| Sysmon logs | | | | |
| Application logs (SCADA/HMI) | | | | |
| PLC configuration download (OT Eng) | | | | |
| Historian data export | | | | |
| Safety system event logs | | | | |
| Photographs of physical conditions | | | | |
| Firewall / switch logs | | | | |

### IOCs Extracted
| IOC Type | Value | Confidence | Shelf Life | Shared Externally? |
|----------|-------|------------|------------|-------------------|
| File Hash | | | | |
| IP Address | | | | |
| Domain | | | | |
| Registry Key | | | | |
| Scheduled Task | | | | |
| User-Agent | | | | |

---

## PHASE 8: LESSONS LEARNED

### Immediate Feedback (within 48 hours)
| Question | Assessment |
|----------|------------|
| Did existing detection rules identify this activity? | Yes / Partially / No |
| Was the detection timely? | Yes / Delayed by _____ |
| Did the playbook support effective response? | Yes / Partially / No |
| Were there gaps or ambiguities in the playbook? | |
| Was the CSIRT activation effective? | |
| Were communication templates adequate? | |
| Were fail-safe positions accurately documented? | |
| Was the safety assessment process smooth? | |

### Follow-Up Actions
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| New/updated detection rule(s) | | | |
| Playbook refinement | | | |
| Architecture change request | | | |
| Intelligence requirement update | | | |
| Training need identified | | | |
| ISAC report submitted | | | |
| Fail-safe documentation update | | | |

### After-Action Review
- **AAR scheduled for**: [Date — within 2 weeks of incident closure]
- **AAR lead**: _______________
- **Full AAR documented in**: [Reference to Chapter 12 AAR Template]
