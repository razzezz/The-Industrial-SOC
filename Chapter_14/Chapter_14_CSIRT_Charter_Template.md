# CSIRT Charter Template — OT Cross-Functional Collaboration

**Document Classification:** [TLP:AMBER / Internal / Confidential]
**Version:** 1.0
**Last Reviewed:** [Date]
**Next Review:** [Date + 12 months]
**Executive Sponsor:** [Name, Title]

---

## 1. Mission Statement

The [Organisation Name] OT Computer Security Incident Response Team (CSIRT) exists to detect, assess, respond to, and recover from cybersecurity incidents affecting operational technology environments while preserving process safety, operational availability, and regulatory compliance.

The CSIRT operates as a cross-functional body that brings together IT Security, OT Engineering, and Operations to ensure that all response decisions account for both cybersecurity risk and physical process consequences.

---

## 2. Organisational Model

**Select one:**

- [ ] **Federated Model** — Representatives from each function participate while remaining organisationally embedded in their home teams. IT Security leads the cybersecurity response; OT Engineering retains veto authority over process safety.

- [ ] **Integrated Model** — A dedicated OT Security team with hybrid skillsets serves as the permanent bridge between IT Security and OT Engineering, with defined authority over OT security operations.

**Rationale for model selection:**
[Document why the chosen model is appropriate for the organisation's size, maturity, budget, and operational complexity.]

---

## 3. CSIRT Composition

### 3.1 Core Members

| Role | Function | Named Individual | Alternate | Contact Method |
|------|----------|-----------------|-----------|----------------|
| **CSIRT Lead** | Tie-breaking, escalation, coordination | [Name] | [Name] | [Phone, Email, Chat] |
| **IT Security Lead** | Threat analysis, forensics, containment strategy | [Name] | [Name] | [Phone, Email, Chat] |
| **OT Security SME** | Operational context, triage support, protocol expertise | [Name] | [Name] | [Phone, Email, Chat] |
| **OT Engineering Lead** | Process safety, operational impact assessment | [Name] | [Name] | [Phone, Email, Chat] |
| **Operations Representative** | Production status, shift context, execution feasibility | [Name] | [Name] | [Phone, Email, Chat] |
| **Engineering Liaison** | SOC-Engineering interface, maintenance context | [Name] | [Name] | [Phone, Email, Chat] |

### 3.2 Extended Members (Activated as Required)

| Role | Function | Named Individual | Activation Criteria |
|------|----------|-----------------|---------------------|
| **Legal/Compliance** | Regulatory reporting, evidence handling | [Name] | Any Severity 1–2 incident; any incident with regulatory notification requirement |
| **Executive Leadership** | Business continuity decisions, external communications | [Name] | Any Severity 1 incident; any incident with potential production impact exceeding [X hours] |
| **Site Safety Officer** | Safety system assessment, safety case implications | [Name] | Any incident involving Safety Instrumented Systems or potential safety impact |
| **Communications/PR** | External messaging, media liaison | [Name] | Any incident with potential public visibility or media interest |
| **MSSP/MDR Provider** | Monitoring, initial triage, agreed response actions | [Name/Team] | Continuous — the MSSP provides the monitoring backbone and escalates to the CSIRT |
| **Vendor Support** | Control system vendor expertise | [Vendor Contact] | Any incident requiring control system vendor knowledge for assessment or recovery |

---

## 4. Decision Authority Structure

### 4.1 Authority Matrix

| Decision Domain | Primary Authority | Consultation Required | Veto Power |
|----------------|-------------------|----------------------|------------|
| **Process Safety** | OT Engineering Lead | Operations, Site Safety Officer | OT Engineering — absolute veto |
| **Cybersecurity Assessment** | IT Security Lead | OT Security SME | None — advisory to other domains |
| **Containment at Purdue L4–L5** | IT Security Lead | None required | None |
| **Containment at Purdue L3.5 (IDMZ)** | IT Security Lead | OT Engineering Lead (notification) | OT Engineering — if safety concern exists |
| **Containment at Purdue L0–L3** | CSIRT Lead (consensus) | All core CSIRT members | OT Engineering — safety veto; Operations — production impact veto |
| **Production Impact** | Operations Representative | OT Engineering Lead | Operations — final say on production decisions |
| **Business Continuity** | Executive Leadership | CSIRT Lead, Operations | Executive — final say on business decisions |
| **Regulatory Notification** | Legal/Compliance | CSIRT Lead, IT Security Lead | None — regulatory obligations are mandatory |
| **External Communication** | Executive Leadership | Communications/PR, Legal | Executive — final say on external messaging |

### 4.2 Conflict Resolution

When CSIRT members disagree on a course of action:

1. The disagreement is articulated clearly, with each position's rationale documented.
2. The CSIRT Lead facilitates a structured discussion, ensuring all perspectives are heard.
3. If consensus cannot be reached within the required response timeframe:
   - **Safety decisions:** OT Engineering's position prevails.
   - **All other decisions:** CSIRT Lead makes the final call and documents the rationale.
4. Post-incident, the disagreement and resolution are reviewed in the After-Action Review.
5. Persistent or systemic disagreements are escalated to the executive sponsor at the quarterly review.

*(See: Chapter_14_Conflict_Resolution_Escalation.md for the detailed escalation path.)*

---

## 5. Activation Criteria

### 5.1 CSIRT Activation Levels

| Level | Trigger | Response |
|-------|---------|----------|
| **Level 1 — Monitoring** | Elevated threat intelligence relevant to sector; ongoing investigation with OT indicators | Engineering Liaison notifies OT Engineering. SOC increases monitoring posture. Weekly sync includes threat update. |
| **Level 2 — Partial Activation** | Confirmed security incident involving OT assets at Purdue L3+ or IT assets with potential OT pivot | CSIRT Lead, IT Security Lead, OT Security SME, and Engineering Liaison assemble. OT Engineering Lead on standby. |
| **Level 3 — Full Activation** | Confirmed incident involving assets at Purdue L0–L2, any incident with potential safety impact, or any Severity 1 incident | All core CSIRT members assemble. Extended members activated as required by criteria in Section 3.2. |

### 5.2 Assembly Protocol

- **Level 2:** CSIRT Lead sends assembly notification via [primary channel]. Target assembly: 30 minutes during business hours, 60 minutes off-hours.
- **Level 3:** CSIRT Lead initiates phone tree via [emergency channel]. Target assembly: 15 minutes during business hours, 30 minutes off-hours.
- **Assembly location:** [Physical war room / Virtual bridge details]
- **Backup communication:** If primary communication channels are compromised, use [backup method — typically personal mobile phones with a pre-distributed contact list].

---

## 6. Day-to-Day Collaboration Provisions

### 6.1 Scheduled Touchpoints

| Touchpoint | Frequency | Duration | Attendees | Purpose |
|------------|-----------|----------|-----------|---------|
| **IT/OT Weekly Sync** | Weekly | 30 min | SOC Lead/OT SME, Engineering Lead, Operations Rep | Maintenance schedules, recent alerts, operational changes, intelligence updates |
| **Monthly Tabletop Exercise** | Monthly | 60 min | All core CSIRT members | Scenario-based exercise, playbook validation, gap identification |
| **Quarterly Programme Review** | Quarterly | 120 min | Core CSIRT + Executive Sponsor | Metrics review, maturity assessment, strategic priorities, systemic issues |
| **Annual Charter Review** | Annually | 60 min | Core CSIRT + Executive Sponsor | Charter update, role changes, process improvements, lessons learned |

### 6.2 Communication Channels

| Channel | Platform | Purpose | Response Expectation |
|---------|----------|---------|---------------------|
| **Real-time operational** | [Teams/Slack channel name] | Active investigations, engineering queries, maintenance notifications | During business hours: 15 minutes. Off-hours: best effort. |
| **Non-urgent coordination** | [Email distribution list] | Meeting coordination, document sharing, non-time-sensitive queries | 24 hours |
| **Emergency escalation** | Phone tree / SMS group | CSIRT activation, safety-critical communications | Immediate |
| **Documentation** | [SharePoint/Confluence/Wiki] | Playbooks, procedures, charter, training materials | N/A — reference resource |

### 6.3 Information Sharing

The following information is shared on an ongoing basis between the SOC and Engineering:

| Information | Direction | Mechanism | Cadence |
|------------|-----------|-----------|---------|
| Maintenance window schedules | Engineering → SOC | OT_MaintenanceWindows watchlist | Updated as scheduled; reviewed weekly |
| Asset register updates | Engineering → SOC | OT_AssetRegister watchlist | Updated as changes occur; reviewed monthly |
| Threat intelligence relevant to sector | SOC → Engineering | Weekly sync briefing + shared channel | Weekly minimum; immediate for critical advisories |
| Detection rule changes | SOC → Engineering | Change management + weekly sync | As deployed; reviewed weekly |
| Alert and investigation summaries | SOC → Engineering | Weekly sync + incident reports | Weekly summary; real-time for significant findings |
| Operational changes affecting telemetry | Engineering → SOC | Shared channel + weekly sync | As planned; minimum 48 hours advance notice |

---

## 7. Training and Competency Requirements

All CSIRT members must complete the following training within 90 days of charter activation or role assignment:

| Role | Required Training | Recommended Training |
|------|-------------------|---------------------|
| IT Security / SOC Analysts | Plant floor orientation; OT protocol awareness; ICS Cyber Kill Chain | SANS ICS410; SANS ICS515 |
| OT Engineering | SOC operations overview; Basic IR concepts; Threat landscape briefing | SANS SEC401 or equivalent |
| Operations | Security awareness (OT-specific); Incident communication procedures | Tabletop exercise participation |
| CSIRT Lead | All of the above, at overview level | SANS MGT517 or equivalent |

*(See: Chapter_14_IT_Security_OT_Training_Plan.md and Chapter_14_OT_Engineering_Security_Training_Plan.md for detailed curricula.)*

---

## 8. Metrics and Reporting

The CSIRT reports the following metrics to the executive sponsor at the quarterly programme review:

| Metric Category | Key Metrics | Target |
|----------------|-------------|--------|
| **Operational** | MTTD (IT/OT split), MTTT (Tier 1 crown jewels), MTTEE, OT False Positive Rate | Per Chapter_14_Joint_KPIs_Metrics.md |
| **Coverage** | Crown Jewel Monitoring %, ATT&CK for ICS Coverage %, Purdue Level Visibility | 100% Tier 1, 90% Tier 2; expanding quarterly |
| **Collaboration** | CSIRT Assembly Time, Joint Training %, Tabletop Exercise Cadence, Engineering Collaboration Score | Per metrics definitions |
| **Business** | Downtime prevented, Downtime caused by security, Audit findings trend | Improving quarterly |

---

## 9. Charter Approval

| Function | Name | Signature | Date |
|----------|------|-----------|------|
| Executive Sponsor | | | |
| IT Security Leadership | | | |
| OT Engineering Leadership | | | |
| Operations Leadership | | | |
| CSIRT Lead | | | |

---

*This charter is reviewed annually or following any major incident that reveals gaps in the collaboration framework. All amendments require executive sponsor approval.*
