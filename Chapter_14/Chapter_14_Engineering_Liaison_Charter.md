# Engineering Liaison Role Charter
# ================================================================
# Description: Role definition for the critical interface position
#   between the SOC and OT Engineering teams. Defines
#   responsibilities, required competencies, reporting structure,
#   and operational touchpoints.
#
# Usage: Use to define, recruit for, or develop the Engineering
#   Liaison function. This role is the single most impactful
#   hire or development investment for OT SOC capability.
# ================================================================

---

## Role Overview

| Field | Detail |
|-------|--------|
| **Role Title** | OT Security Engineering Liaison |
| **Alternative Titles** | OT Security SME, IT/OT Bridge Engineer, OT Cyber Analyst |
| **Reports To** | [SOC Manager / CISO — with dotted line to Engineering Lead] |
| **Location** | [Should have regular physical presence at operational site(s)] |
| **Classification** | ☐ Full-time dedicated ☐ Part-time / additional responsibility ☐ MSSP-provided |

---

## Purpose

The Engineering Liaison serves as the primary interface between IT Security Operations and OT Engineering/Operations teams. This role translates between the security and engineering domains, ensures that security operations respect operational constraints, and provides the OT subject matter expertise that enables the SOC to effectively triage, investigate, and respond to threats in the industrial control system environment.

---

## Core Responsibilities

### 1. Operational Bridge (Day-to-Day)

- Serve as the first point of contact for SOC analysts when OT context is needed during alert triage
- Translate OT alert context into operationally meaningful assessments (what does this alert mean for the physical process?)
- Maintain and update the OT_AssetRegister and OT_CrownJewels watchlists in coordination with OT Engineering
- Coordinate maintenance window scheduling and communicate active windows to the SOC via the OT_MaintenanceWindows watchlist
- Attend SOC shift handovers (or review handover notes) to maintain awareness of ongoing OT investigations

### 2. Detection Engineering Support

- Provide OT domain expertise during detection rule development and tuning
- Review and validate false positive analyses for OT-related alerts
- Ensure detection rules account for legitimate operational activity (shift patterns, batch cycles, maintenance windows)
- Prioritise detection engineering backlog based on crown jewel risk and threat intelligence

### 3. Incident Response Coordination

- Serve as the engineering coordinator during OT security incidents
- Activate the engineering response chain when OT assets are involved
- Provide real-time operational impact assessment to the incident commander
- Advise on safe/unsafe containment actions for specific OT systems
- Ensure engineering's safety veto authority is respected during response

### 4. Cross-Functional Communication

- **Lead the weekly IT/OT sync** meeting using the Meeting Agenda Template
- Facilitate the monthly cross-functional tabletop exercises
- Prepare and present the OT component of the quarterly programme review
- Translate between security terminology and engineering/operations language

### 5. Intelligence and Hunting Support

- Provide OT context for threat intelligence operationalisation (Chapter 10)
- Support threat hunting operations with domain expertise on normal vs. anomalous OT behaviour
- Review vulnerability intelligence assessments for OT-specific context
- Contribute operational knowledge to threat modelling exercises

### 6. Training and Knowledge Development

- Deliver plant floor orientation sessions for SOC analysts
- Facilitate maintenance window observation opportunities for SOC staff
- Coordinate SOC analyst participation in OT-specific training (ICS410, ICS515)
- Deliver security awareness content to OT engineering and operations teams

---

## Required Competencies

### Essential

| Competency | Description |
|-----------|-------------|
| **ICS Fundamentals** | Understanding of SCADA, DCS, PLC, RTU, HMI functions; Purdue Model; common ICS protocols (Modbus, DNP3, EtherNet/IP, OPC UA) |
| **SOC Operations** | Understanding of SOC workflows, alert triage, incident response lifecycle, SIEM operations |
| **Communication** | Ability to translate between security and engineering domains; build trust with both teams |
| **Operational Awareness** | Understanding of the physical processes being controlled; safety implications of security actions |
| **Incident Response** | Experience with or training in incident response procedures; understanding of containment decisions in OT |

### Desirable

| Competency | Description |
|-----------|-------------|
| **Detection Engineering** | KQL query development; ASIM normalisation; Sentinel analytics rule creation |
| **Threat Intelligence** | ATT&CK for ICS mapping; threat actor profiling; intelligence operationalisation |
| **Network Security** | Understanding of Zeek, Suricata; network traffic analysis; ICS protocol analysis |
| **Certifications** | SANS GICSP, ICS410, ICS515; GRID; vendor-specific OT certifications |

### Development Path

For individuals transitioning into this role:

| Background | Development Priority |
|-----------|---------------------|
| **From SOC/IT Security** | ICS fundamentals, plant floor orientation, protocol awareness, engineering relationship building |
| **From OT Engineering** | SOC operations, SIEM/KQL, incident response procedures, threat landscape orientation |

---

## Operational Touchpoints

| Activity | Frequency | Duration | Participants |
|----------|-----------|----------|-------------|
| SOC shift handover review | Daily | 15 min | Liaison + outgoing SOC shift lead |
| Weekly IT/OT sync | Weekly | 30 min | Liaison + SOC lead + engineering lead |
| OT alert review | Weekly | 30 min | Liaison + detection engineering |
| Monthly tabletop exercise | Monthly | 2–3 hours | Full cross-functional team |
| Quarterly programme review | Quarterly | 2 hours | Leadership + all functional teams |
| Maintenance window coordination | As needed | Varies | Liaison + engineering + SOC |
| Incident response coordination | As needed | Duration of incident | CSIRT members |

---

## Key Performance Indicators

| KPI | Target | Measurement |
|-----|--------|-------------|
| Mean Time to Engage Engineering (MTTEE) | < 30 min business hours | Incident records |
| OT False Positive Rate | < 20% overall | Sentinel incident classifications |
| Weekly IT/OT sync attendance | 100% | Meeting records |
| Watchlist currency | Updated within 48 hours of changes | Watchlist audit |
| Tabletop exercise facilitation | ≥ 1 per quarter | Exercise records |
| SOC analyst OT training | 80% completion within 12 months | Training records |

---

## Authority and Escalation

| Situation | Liaison Authority |
|-----------|------------------|
| OT alert triage — provide context | Full authority to provide guidance to SOC analysts |
| Watchlist updates | Authority to update after engineering approval |
| Incident escalation to engineering | Authority to activate engineering response chain |
| Containment actions on OT systems | **No unilateral authority** — must coordinate with engineering; engineering retains safety veto |
| Detection rule tuning | Authority to request tuning; detection engineering implements |
| Process or equipment shutdown | **No authority** — operations management decision only |

---

## Charter Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| SOC Manager / CISO | | | |
| OT Engineering Lead | | | |
| Operations Manager | | | |
| Programme Sponsor | | | |
