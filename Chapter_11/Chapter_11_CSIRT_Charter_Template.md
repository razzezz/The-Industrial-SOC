# OT CSIRT Charter Template
# ================================================================
# Description: Template for establishing a cross-functional
#   Computer Security Incident Response Team (CSIRT) for OT
#   environments. Defines composition, decision authorities,
#   activation criteria, and operational procedures.
#
# Usage: Customise for your organisation, obtain executive
#   sponsorship, and distribute to all CSIRT members. Review
#   annually or after any major incident.
#
# Related: Chapter_11_CSIRT_Roster_Template.md
#          Chapter_11_OT_Incident_Severity_Matrix.md
#          Chapter_11_IR_Playbook_Template.md
# ================================================================

## 1. CHARTER PURPOSE

This charter establishes the [Organisation Name] Operational Technology
Computer Security Incident Response Team (OT CSIRT). It defines the
team's mission, composition, authorities, and operational procedures
for responding to cybersecurity incidents that affect or may affect
industrial control systems and operational technology.

**Effective Date**: [Date]
**Charter Owner**: [CISO / VP Engineering / Plant Director]
**Review Frequency**: Annually, or after any Severity 1 incident

---

## 2. MISSION

The OT CSIRT exists to detect, respond to, contain, and recover from
cybersecurity incidents affecting OT environments while maintaining
process safety, operational continuity, and regulatory compliance. The
team operates under the principle that **minimising total harm — both
cyber and physical — takes precedence over speed of containment**.

---

## 3. SCOPE

### In Scope
- All cybersecurity incidents affecting assets at Purdue Levels 0–3.5
- Incidents at Purdue Levels 4–5 that involve assets with OT access
  (engineering workstations, VPN accounts, service accounts)
- Incidents at any level that may affect Safety Instrumented Systems
- Supply chain incidents affecting OT vendors or products
- Physical security incidents with cyber implications for OT

### Out of Scope
- Standard IT security incidents with no OT nexus (handled by IT IR)
- Physical safety incidents with no cyber element (handled by HSE)
- OT operational issues with no security element (handled by OT Ops)

---

## 4. CSIRT COMPOSITION AND ROLES

### 4.1 IT Security Function

**Role**: Threat analysis, forensic investigation, containment
strategy development, SIEM/EDR/NDR operation.

**Responsibilities during incident**:
- Lead cybersecurity assessment (threat identification, scope, TTP analysis)
- Operate SIEM, EDR, and network monitoring tools
- Propose containment options with technical assessment
- Collect and preserve digital evidence (IT-side)
- Extract and disseminate IOCs
- Coordinate external intelligence (ISAC, CISA, law enforcement)

**Authority**:
- Full authority over containment actions at Purdue Levels 4–5
- Authority over containment at Level 3.5 with notification to OT Eng
- Advisory role for containment at Levels 0–3 (no unilateral authority)

**Named Personnel**:
| Sub-Role | Primary | Backup |
|----------|---------|--------|
| IR Lead | | |
| SOC Manager | | |
| OT Security SME | | |
| Forensic Analyst | | |

### 4.2 OT Engineering Function

**Role**: Process safety assessment, operational impact analysis,
control system evidence collection, fail-safe position expertise.

**Responsibilities during incident**:
- Lead safety assessment (Phase 3 of IR playbook)
- Assess operational impact of proposed containment actions
- Provide fail-safe position information for affected systems
- Collect evidence from PLCs, controllers, and OT-specific systems
- Validate PLC logic against golden images
- Lead recovery validation for control systems

**Authority**:
- Veto authority over any action that creates a safety risk at L0–L3
- Lead authority on PLC/controller interaction during incident
- Required signoff for containment actions at Purdue Levels 0–3

**Named Personnel**:
| Sub-Role | Primary | Backup |
|----------|---------|--------|
| OT Engineering Lead | | |
| Process/Controls Engineer | | |
| Safety Engineer | | |

### 4.3 Plant Operations Function

**Role**: Production status, process monitoring, manual control
capability, operational continuity.

**Responsibilities during incident**:
- Provide real-time production and process status
- Confirm safety system operational status
- Assess feasibility of manual control if automated systems isolated
- Manage operator transition to backup systems if required
- Confirm process stability during and after containment actions
- Declare operational recovery

**Authority**:
- Authority to initiate controlled shutdown on safety grounds
- Required signoff for containment actions at Purdue Levels 0–3
- Authority over production continuity decisions

**Named Personnel**:
| Sub-Role | Primary | Backup |
|----------|---------|--------|
| Operations Manager | | |
| Shift Supervisor | | |
| Safety Officer | | |

### 4.4 Legal and Compliance Function

**Role**: Regulatory reporting, evidence handling, legal exposure
assessment, external communication approval.

**Responsibilities during incident**:
- Ensure regulatory reporting timelines are met (NIS 2: 24hr/72hr/30d)
- Advise on evidence preservation for legal proceedings
- Review external communications before release
- Coordinate with sector regulator as required
- Assess legal exposure and advise on disclosure obligations

**Authority**:
- Authority over regulatory notification content and timing
- Required review of all external communications
- Authority to engage external legal counsel

**Named Personnel**:
| Sub-Role | Primary | Backup |
|----------|---------|--------|
| Legal Counsel | | |
| Compliance Officer | | |
| Regulatory Liaison | | |

### 4.5 Executive Leadership

**Role**: Business continuity decisions, resource authorisation,
external stakeholder management.

**Responsibilities during incident**:
- Authorise actions with significant financial/operational impact
- Approve resource allocation (additional staff, vendor engagement)
- Manage external stakeholder communications (board, customers, media)
- Make business continuity decisions when containment and operations conflict

**Authority**:
- Authority over business impact decisions
- Authority to authorise production shutdown for security reasons
- Authority to engage external incident response vendors

**Named Personnel**:
| Sub-Role | Primary | Backup |
|----------|---------|--------|
| CISO | | |
| Plant Director / VP Ops | | |
| Executive On-Call | | |

---

## 5. ACTIVATION CRITERIA

### Full CSIRT Activation (All Functions)
- Any Severity 1 incident (safety impact confirmed or suspected)
- Any incident involving confirmed compromise at Purdue Levels 0–2
- Any incident requiring regulatory notification
- Any incident involving a known APT targeting ICS

### Partial CSIRT Activation (IT Security + OT Engineering)
- Severity 2 incident (operational impact)
- Suspected compromise at Purdue Level 3
- Unauthorised ICS write commands detected
- New unknown device on OT network

### IT Security Response Only (with OT SME consultation)
- Severity 3–4 incidents with OT context
- Alerts at Purdue Levels 3.5–5 involving OT-adjacent systems
- Maintenance window correlation investigations

---

## 6. DECISION-MAKING FRAMEWORK

### The Consensus Rule
**All functions must agree before any action that affects operations at
Purdue Levels 0–3.** This includes containment, eradication, and
recovery actions.

### When Consensus Cannot Be Reached
If the CSIRT cannot reach consensus on a containment action:
1. **Default position**: Defer the action. Do not execute.
2. **Escalate**: The CSIRT Lead escalates to Executive Leadership.
3. **Exception**: If OT Engineering or Operations identifies an
   **imminent safety risk**, they have authority to initiate emergency
   actions (e.g., controlled shutdown) without full consensus.
4. **Document**: All disagreements and the rationale for each position
   must be documented in the incident record.

### Decision Authority Summary
| Decision Type | Lead Authority | Required Concurrence |
|--------------|----------------|---------------------|
| Safety action (emergency shutdown) | OT Eng / Operations | Unilateral if imminent risk |
| Containment at L0–3 | Joint decision | IT Sec + OT Eng + Operations |
| Containment at L3.5 | IT Security | Notify OT Engineering |
| Containment at L4–5 | IT Security | None required |
| Regulatory notification | Legal/Compliance | CISO approval |
| External communication | Executive | Legal review |
| Production shutdown for security | Executive | OT Eng + Operations input |
| Vendor engagement | IT Security | Executive approval (cost) |

---

## 7. COMMUNICATION PROTOCOLS

### Internal Communication Channels
- **Primary**: [e.g., Microsoft Teams — OT CSIRT channel]
- **Backup**: [e.g., Signal group, phone bridge]
- **Out-of-band**: [e.g., Personal mobile phones — for scenarios where
  corporate communications may be compromised]

### Communication Cadence During Active Incident
- **Severity 1**: Status update every 15 minutes
- **Severity 2**: Status update every 30 minutes
- **Severity 3**: Status update every 2 hours
- **Severity 4**: Update at shift handover

### External Communication
All external communications (media, customers, regulators, ISAC) must
be reviewed by Legal and approved by Executive Leadership before release.

---

## 8. TRAINING AND EXERCISE REQUIREMENTS

| Activity | Frequency | Participants |
|----------|-----------|-------------|
| Tabletop exercise | Quarterly | Full CSIRT |
| Charter review | Annually | CSIRT leads |
| Contact roster update | Monthly | CSIRT coordinator |
| Individual role training | Annually | All members |
| Joint IT/OT exercise | Semi-annually | IT Security + OT Engineering |
| Regulatory reporting drill | Annually | Legal + CISO |

---

## 9. CHARTER APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| CISO | | | |
| OT Engineering Director | | | |
| Plant/Operations Director | | | |
| General Counsel | | | |
| Executive Sponsor | | | |
