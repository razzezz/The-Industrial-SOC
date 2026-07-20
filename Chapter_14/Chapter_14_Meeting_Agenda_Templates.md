# Meeting Agenda Templates — IT/OT Cross-Functional Collaboration

---

## 1. Weekly IT/OT Sync

**Frequency:** Weekly
**Duration:** 30 minutes
**Attendees:** SOC Lead or OT SME, Engineering Lead, Operations Representative, Engineering Liaison
**Format:** Standing meeting, virtual or in-person
**Chair:** Engineering Liaison (rotates quarterly)

### Agenda

| Time | Item | Owner | Notes |
|------|------|-------|-------|
| 0:00–0:05 | **Operational Status Check** | Operations Rep | Current production status, any active outages or constraints, upcoming shutdowns |
| 0:05–0:10 | **Maintenance Window Review** | Engineering Lead | Upcoming maintenance windows (next 7 days), changes to OT_MaintenanceWindows watchlist, new engineering activities that may generate alerts |
| 0:10–0:15 | **Security Alerts & Investigations** | SOC Lead / OT SME | Notable OT alerts from past week, investigation outcomes, false positive trends, any new detection rules deployed |
| 0:15–0:20 | **Threat Intelligence Update** | SOC Lead / OT SME | New advisories relevant to sector, threat actor activity updates, new vulnerabilities affecting OT assets in the environment |
| 0:20–0:25 | **Operational Changes** | Engineering Lead | Upcoming firmware upgrades, new device deployments, network changes, vendor remote access sessions, anything that may alter telemetry patterns |
| 0:25–0:30 | **Actions & Closing** | Chair | Review actions from previous week, assign new actions, confirm next meeting |

### Standing Follow-Up Items
- [ ] OT_MaintenanceWindows watchlist updated with next week's windows
- [ ] Any new assets added to OT_AssetRegister
- [ ] False positive tuning requests logged

---

## 2. Monthly Tabletop Exercise

**Frequency:** Monthly
**Duration:** 60 minutes
**Attendees:** All core CSIRT members
**Format:** Facilitated exercise, in-person preferred
**Facilitator:** CSIRT Lead (or rotating facilitator)

### Agenda

| Time | Item | Owner | Notes |
|------|------|-------|-------|
| 0:00–0:05 | **Welcome & Scenario Introduction** | Facilitator | Brief the scenario context, ground rules, objectives for the exercise |
| 0:05–0:10 | **Scenario Background** | Facilitator | Present the initial scenario conditions. Reference the Chapter 11 Tabletop Scenario Library for pre-built scenarios |
| 0:10–0:25 | **Phase 1: Detection & Initial Response** | All | Inject 1: Initial alert fires. Discussion: Who sees it? What is the triage decision? When is engineering engaged? |
| 0:25–0:40 | **Phase 2: Investigation & Containment** | All | Inject 2: Investigation reveals scope. Discussion: What containment options exist? Safety assessment? Production impact? Who decides? |
| 0:40–0:50 | **Phase 3: Recovery & Communication** | All | Inject 3: Containment executed. Discussion: Recovery sequence? Regulatory notification? Internal communication? |
| 0:50–0:55 | **Debrief** | Facilitator | What went well? What gaps were identified? What surprised participants? |
| 0:55–1:00 | **Actions** | Facilitator | Playbook updates required, process changes, training gaps identified, next scenario selection |

### Scenario Rotation (12-Month Cycle)
| Month | Scenario | Primary Focus |
|-------|----------|--------------|
| 1 | Ransomware at IT/OT Boundary | Cross-domain containment decisions |
| 2 | Anomalous PLC Programming | Engineering assessment under pressure |
| 3 | Compromised Vendor Remote Access | Supply chain and third-party risk |
| 4 | Credential Harvesting Targeting OT | Lateral movement IT→OT |
| 5 | Safety System Anomaly | Safety-critical decision making |
| 6 | Insider Threat — Unauthorised Configuration | Trust and verification |
| 7 | Ransomware at IT/OT Boundary (repeat) | Assess improvement from Month 1 |
| 8 | IDMZ Compromise | Architecture and segmentation |
| 9 | Coordinated Multi-Site Attack | Communication and coordination at scale |
| 10 | Firmware Supply Chain Compromise | Detection limitations and recovery |
| 11 | Living-off-the-Land in OT (Volt Typhoon-style) | Behavioural detection and hunting |
| 12 | Full-Scope Exercise (selected scenario) | Executive participation, regulatory notification |

---

## 3. Quarterly Programme Review

**Frequency:** Quarterly
**Duration:** 120 minutes
**Attendees:** Core CSIRT members, Executive Sponsor, MSSP Account Lead (if hybrid model)
**Format:** Structured review, presentation + discussion
**Chair:** CSIRT Lead

### Agenda

| Time | Item | Owner | Notes |
|------|------|-------|-------|
| 0:00–0:10 | **Executive Summary** | CSIRT Lead | High-level programme status, key achievements, critical issues requiring executive attention |
| 0:10–0:30 | **Metrics Review** | CSIRT Lead / SOC Lead | Present all metrics from Joint KPIs dashboard. Highlight trends, improvements, and areas of concern. Compare against targets |
| 0:30–0:45 | **Incident Review** | IT Security Lead | Summary of significant incidents in the quarter. Lessons learned implemented. Outstanding AAR actions. Regulatory interactions |
| 0:45–1:00 | **Detection & Coverage** | Detection Engineer / OT SME | ATT&CK for ICS coverage progress. New detection rules deployed. Crown jewel monitoring status. Hunting operations conducted and findings |
| 1:00–1:15 | **Collaboration Assessment** | Engineering Liaison | Engineering Collaboration Score results. Feedback from engineering and operations teams. Collaboration successes and challenges |
| 1:15–1:30 | **Training & Competency** | CSIRT Lead | Training completion rates. Skills gaps identified. Upcoming training opportunities. New hires/role changes |
| 1:30–1:45 | **Strategic Priorities** | CSIRT Lead + Executive Sponsor | Maturity progression (Chapter 16 assessment). Budget requirements. Tooling changes (from Chapter 13 reviews). Organisational changes |
| 1:45–1:55 | **Systemic Issues & Blockers** | All | Issues that cannot be resolved at the working level. Resource constraints. Organisational obstacles. Policy gaps |
| 1:55–2:00 | **Actions & Next Quarter Priorities** | CSIRT Lead | Confirm action owners and deadlines. Set top 3 priorities for next quarter. Confirm next review date |

### Quarterly Review Pack (Prepared in Advance)
The CSIRT Lead prepares and distributes the following 48 hours before the review:
- Metrics dashboard export (from Chapter_14_Joint_KPIs_Metrics.md)
- Incident summary report
- ATT&CK for ICS coverage assessment output
- Training completion status
- Engineering Collaboration Score survey results
- Proposed priorities for next quarter

---

## 4. Annual Charter Review

**Frequency:** Annually (or following a major incident)
**Duration:** 60 minutes
**Attendees:** Core CSIRT members, Executive Sponsor
**Chair:** Executive Sponsor

### Agenda

| Time | Item | Owner | Notes |
|------|------|-------|-------|
| 0:00–0:10 | **Year in Review** | CSIRT Lead | Programme achievements, maturity progression, key metrics trends over 12 months |
| 0:10–0:20 | **Charter Review** | CSIRT Lead | Walk through each charter section. Identify elements that need updating: role changes, authority adjustments, process refinements |
| 0:20–0:35 | **Lessons from Incidents & Exercises** | IT Security Lead | Systemic findings from the year's incidents and tabletop exercises that should inform charter changes |
| 0:35–0:45 | **Organisational Changes** | Executive Sponsor | Any organisational restructuring, budget changes, or strategic shifts that affect the CSIRT |
| 0:45–0:55 | **Updated Charter Approval** | All | Review and agree updated charter. Confirm all signatories |
| 0:55–1:00 | **Close** | Executive Sponsor | Reaffirm commitment. Set expectations for the coming year |

---

*Store all meeting minutes and action logs in [designated repository]. Archive quarterly review packs for trend analysis and audit evidence.*
