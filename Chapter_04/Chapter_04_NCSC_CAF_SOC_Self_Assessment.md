# NCSC CAF v4.0 SOC Self-Assessment Template

**Purpose:** Assess your SOC's current capability against the NCSC Cyber Assessment Framework v4.0 Objectives C and D, with supporting evidence tracking for Objective A elements relevant to SOC operations.

**Scope:** This template focuses on the CAF principles and contributing outcomes most directly relevant to Security Operations Centre functions: detection, monitoring, threat hunting, incident response, and lessons learned. It also covers the threat understanding and asset management contributing outcomes that inform SOC operations.

**Assessment Scale:**
- **Achieved** — The contributing outcome is fully met; evidence demonstrates both existence and effectiveness of the capability.
- **Partially Achieved** — Some elements are in place, but gaps remain in capability, coverage, or evidence of effectiveness.
- **Not Achieved** — The contributing outcome is not met or insufficient evidence exists.

**Instructions:** Complete each row with your current assessment, the evidence supporting that assessment, identified gaps, and planned improvement actions with owners and target dates.

---

## Objective A — Managing Security Risk (SOC-Relevant Elements)

### Principle A2: Risk Management

| Contributing Outcome | Assessment | Evidence | Gaps Identified | Improvement Actions | Owner | Target Date |
|---------------------|------------|----------|----------------|--------------------| ------|-------------|
| **A2.b — Understanding Threat** | | | | | | |
| *Organisation proactively analyses its threat landscape* | | | | | | |
| *Threat analysis methodology is documented* | | | | | | |
| *Attack scenarios are modelled (e.g., attack trees)* | | | | | | |
| *Threat understanding informs risk management decisions* | | | | | | |

### Principle A3: Asset Management

| Contributing Outcome | Assessment | Evidence | Gaps Identified | Improvement Actions | Owner | Target Date |
|---------------------|------------|----------|----------------|--------------------| ------|-------------|
| **A3.a — Asset Management** | | | | | | |
| *OT assets are inventoried and classified* | | | | | | |
| *Crown jewels are identified and prioritised* | | | | | | |
| *Asset inventory is maintained and current* | | | | | | |

---

## Objective C — Detecting Cyber Security Events

### Principle C1: Security Monitoring

| Contributing Outcome | Assessment | Evidence | Gaps Identified | Improvement Actions | Owner | Target Date |
|---------------------|------------|----------|----------------|--------------------| ------|-------------|
| **C1.a — Monitoring Coverage** | | | | | | |
| *IT network monitoring in place* | | | | | | |
| *OT network monitoring in place (IDMZ, L3, L2)* | | | | | | |
| *IT/OT boundary monitoring in place* | | | | | | |
| *Endpoint monitoring (workstations, HMIs, servers)* | | | | | | |
| *Crown jewel assets have priority monitoring* | | | | | | |
| **C1.b — Securing Logs** | | | | | | |
| *Logs collected from OT-relevant sources* | | | | | | |
| *Log integrity protected* | | | | | | |
| *Retention meets regulatory requirements* | | | | | | |
| **C1.c — Generating Alerts** | | | | | | |
| *SIEM analytics rules active for OT use cases* | | | | | | |
| *Detection rules mapped to ATT&CK for ICS* | | | | | | |
| *Alert prioritisation accounts for OT context (Purdue level, crown jewel status)* | | | | | | |
| *False positive rate managed and documented* | | | | | | |
| **C1.d — Identifying Security Incidents** | | | | | | |
| *Triage process incorporates OT operational context* | | | | | | |
| *Escalation paths to OT engineering defined* | | | | | | |
| *Maintenance window context available during triage* | | | | | | |
| **C1.e — Monitoring Tools and Skills** | | | | | | |
| *SOC analysts trained on OT environment and protocols* | | | | | | |
| *Monitoring tools appropriate for OT (passive, protocol-aware)* | | | | | | |
| *Skills development programme for OT SOC capability* | | | | | | |
| **C1.f — Understanding Users' and System's Behaviour & Threat Intelligence** *(New in v4.0)* | | | | | | |
| *Behavioural baselines established for OT networks* | | | | | | |
| *Anomaly detection based on behavioural deviation* | | | | | | |
| *Threat intelligence integrated into monitoring* | | | | | | |
| *Intelligence sources cover ICS-specific threats* | | | | | | |

### Principle C2: Threat Hunting

| Contributing Outcome | Assessment | Evidence | Gaps Identified | Improvement Actions | Owner | Target Date |
|---------------------|------------|----------|----------------|--------------------| ------|-------------|
| **C2.a — Proactive Security Event Discovery** | | | | | | |
| *Proactive search for anomalies conducted routinely* | | | | | | |
| *Hunt activities documented with findings* | | | | | | |
| **C2.b — Threat Hunting** *(New/Enhanced in v4.0)* | | | | | | |
| *Threat hunting follows structured methodology* | | | | | | |
| *Hunts are risk- and intelligence-led* | | | | | | |
| *Hunts target specific hostile TTPs (not just IOCs)* | | | | | | |
| *Hunt findings drive detection improvement* | | | | | | |
| *Hunting capability covers OT telemetry sources* | | | | | | |

---

## Objective D — Minimising the Impact of Cyber Security Incidents

### Principle D1: Response and Recovery Planning

| Contributing Outcome | Assessment | Evidence | Gaps Identified | Improvement Actions | Owner | Target Date |
|---------------------|------------|----------|----------------|--------------------| ------|-------------|
| **D1.a — Response Plan** | | | | | | |
| *ICS-specific IR playbooks exist* | | | | | | |
| *Playbooks account for OT safety constraints* | | | | | | |
| *Decision authority structure defined (SOC, OT Eng, Ops)* | | | | | | |
| *Cross-functional CSIRT established* | | | | | | |
| **D1.b — Response and Recovery Capability** | | | | | | |
| *IR plan tested via tabletop exercises* | | | | | | |
| *OT engineering participates in IR exercises* | | | | | | |
| *Containment procedures respect IT/OT boundary* | | | | | | |
| *Recovery procedures include OT system restoration* | | | | | | |
| **D1.c — Testing and Exercising** | | | | | | |
| *Tabletop exercises conducted at least quarterly* | | | | | | |
| *Scenarios include OT-specific attack scenarios* | | | | | | |
| *Exercise findings tracked to completion* | | | | | | |
| **D1.d — Incident Reporting** | | | | | | |
| *Incident classification criteria defined against regulatory thresholds* | | | | | | |
| *Reporting timelines achievable (24hr early warning for NIS 2)* | | | | | | |
| *Reporting procedures documented and tested* | | | | | | |

### Principle D2: Lessons Learned

| Contributing Outcome | Assessment | Evidence | Gaps Identified | Improvement Actions | Owner | Target Date |
|---------------------|------------|----------|----------------|--------------------| ------|-------------|
| **D2.a — Incident Root Cause Analysis** | | | | | | |
| *Post-incident reviews conducted* | | | | | | |
| *Root cause analysis documented* | | | | | | |
| *Findings shared across IT and OT teams* | | | | | | |
| **D2.b — Using Lessons Learned** | | | | | | |
| *Lessons drive detection improvements* | | | | | | |
| *Lessons inform architecture changes* | | | | | | |
| *Lessons shared with sector peers (ISAC)* | | | | | | |
| *Improvement actions tracked to completion* | | | | | | |

---

## Assessment Summary

| Objective / Principle | Achieved | Partially Achieved | Not Achieved | Total COs |
|----------------------|----------|-------------------|--------------|-----------|
| A2 — Risk Management | | | | |
| A3 — Asset Management | | | | |
| C1 — Security Monitoring | | | | |
| C2 — Threat Hunting | | | | |
| D1 — Response and Recovery | | | | |
| D2 — Lessons Learned | | | | |
| **TOTAL** | | | | |

---

## Priority Gaps (Top 5)

| # | Gap Description | Contributing Outcome(s) | Impact | Remediation Plan | Owner | Target Date |
|---|----------------|------------------------|--------|-----------------|-------|-------------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |

---

**Assessment Date:** _______________
**Assessed By:** _______________
**Next Review Date:** _______________

---

*This template accompanies Chapter 4: The Regulatory Roadmap. For the complete CAF v4.0 framework, refer to the NCSC publication at https://www.ncsc.gov.uk/collection/cyber-assessment-framework*
