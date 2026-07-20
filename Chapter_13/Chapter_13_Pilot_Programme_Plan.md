# OT Security Tool Pilot Programme Plan

## Document Control

| Field | Value |
|---|---|
| **Tool Under Evaluation** | |
| **Vendor** | |
| **Capability Being Assessed** | |
| **Pilot Site** | |
| **Pilot Duration** | Start: __________ End: __________ |
| **Plan Owner** | |
| **OT Engineering Sponsor** | |
| **Version** | |
| **Last Updated** | |

---

## 1. Pilot Objectives

*Define what this pilot must demonstrate before a deployment decision can be made.*

| Objective | Measurement | Target |
|---|---|---|
| **Safety validation** — Zero operational impact on OT processes | Incident reports, OT Engineering feedback | Zero OT incidents attributable to the tool |
| **Protocol support validation** — Tool parses required ICS protocols at the required depth | Protocol coverage test against live traffic | ≥ 90% of environment protocols parsed at function-code level |
| **SIEM integration** — Data flowing into Sentinel with ASIM normalisation | Sentinel data ingestion verification | Continuous ingestion with < 5 min latency |
| **Detection capability** — Minimum number of active detection use cases | Detection rules created and validated | ≥ 3 use cases mapped to ATT&CK for ICS |
| **False positive rate** — Manageable volume of false positives | Weekly FP count and analyst time | < 10 FPs/week requiring analyst investigation |
| **Analyst usability** — SOC analysts can effectively use tool data | Analyst feedback survey | ≥ 3/5 average usability score |
| *(Custom objective)* | | |

---

## 2. Pilot Scope

### 2.1 Site Selection

| Criterion | Assessment |
|---|---|
| **Site name** | |
| **Why this site?** | *(Cooperative engineering team, representative technology, manageable size)* |
| **Number of OT assets at site** | |
| **Primary ICS protocols in use** | |
| **Primary PLC/controller vendors** | |
| **Crown jewel assets at site** | Tier 1: _____ Tier 2: _____ |
| **Existing monitoring at site** | |

### 2.2 Deployment Scope

| Parameter | Pilot Scope |
|---|---|
| **Monitoring point(s)** | ☐ IDMZ boundary ☐ Between L2–L3 ☐ Within L2 ☐ Other: _____ |
| **Network TAP / SPAN configuration** | |
| **Number of sensors** | |
| **Sensor hardware specifications** | |
| **Network segments monitored** | |
| **Excluded segments (and justification)** | |

### 2.3 Explicitly Out of Scope

*Document what this pilot does NOT include to manage expectations.*

| Exclusion | Reason |
|---|---|
| Active scanning of any OT devices | Safety — passive only during pilot |
| Agent deployment on any OT system | Safety — network monitoring only during pilot |
| Multi-site deployment | Pilot validates single-site before expansion |
| Production detection (alerting SOC) | Shadow mode — logs and assesses without generating SOC incidents |
| | |

---

## 3. Safety Validation Protocol

*This protocol must be completed and signed off before the pilot tool is connected to any OT network segment.*

### 3.1 Pre-Deployment Safety Checks

| Check | Status | Notes | Sign-Off |
|---|---|---|---|
| Tool operates in passive mode (read-only, no traffic injection) | ☐ Verified | | |
| Tool failure mode confirmed as fail-open | ☐ Verified | | |
| Tool deployed on SPAN/TAP (not inline) | ☐ Verified | | |
| Sensor hardware isolated from OT control network | ☐ Verified | | |
| Management traffic for tool routed through IT/IDMZ network, not OT network | ☐ Verified | | |
| OT Engineering has reviewed deployment architecture | ☐ Verified | | |
| Change management approval obtained | ☐ Approved — Ref: _____ | | |
| Rollback procedure documented and tested | ☐ Verified | | |

### 3.2 Monitoring During Pilot

| Monitoring Item | Frequency | Responsibility |
|---|---|---|
| Sensor resource utilisation (CPU, memory, disk) | Daily (first week), then weekly | Security Engineering |
| Network performance on monitored segments | Daily (first week), then weekly | Network Engineering |
| OT process stability and performance | Daily (first week), then weekly | OT Engineering |
| Any operator-reported anomalies | Continuous | Operations |

### 3.3 Emergency Rollback Procedure

**Trigger conditions for immediate rollback:**
- Any reported operational impact on OT processes
- Sensor generating traffic on OT network segments
- Network performance degradation on monitored segments
- OT Engineering request for any reason

**Rollback steps:**
1. _______________
2. _______________
3. _______________
4. _______________

**Rollback owner:** _______________
**Rollback estimated time:** _______________

---

## 4. Timeline

| Phase | Duration | Activities | Milestone |
|---|---|---|---|
| **Planning** | 2 weeks | Site assessment, hardware procurement, change management, stakeholder briefing | Change approved |
| **Deployment** | 1 week | Sensor installation, TAP/SPAN configuration, connectivity validation | Sensor online, data flowing |
| **Safety validation** | 2 weeks | Intensive monitoring of OT impact, daily safety checks | Safety sign-off from OT Engineering |
| **Integration** | 2 weeks | SIEM connector, ASIM parsers, watchlist enrichment, data quality validation | Data visible in Sentinel with context |
| **Detection development** | 4–6 weeks | Write ≥ 3 detection use cases, shadow mode deployment, FP assessment | Detection rules active in shadow mode |
| **Evaluation** | 2 weeks | Consolidate metrics, analyst feedback, OT Engineering assessment, final report | Pilot report completed |
| **Decision** | 1 week | Go / No-Go decision based on success criteria | Decision documented |

**Total pilot duration: 13–17 weeks (approximately 3–4 months)**

---

## 5. Stakeholder Responsibilities

| Stakeholder | Role in Pilot | Named Individual |
|---|---|---|
| **Security Engineering** | Sensor deployment, SIEM integration, detection rule development | |
| **SOC Analysts** | Testing detection use cases, providing usability feedback | |
| **OT Engineering** | Safety validation, operational context, protocol baseline validation | |
| **Network Engineering** | TAP/SPAN configuration, network performance monitoring | |
| **Operations** | Reporting any process anomalies during pilot period | |
| **Vendor** | Technical support, configuration assistance, issue resolution | |
| **Pilot Owner** | Overall coordination, reporting, decision recommendation | |

---

## 6. Success Criteria and Go/No-Go Decision

### 6.1 Mandatory Success Criteria (All Must Pass)

| Criterion | Target | Actual | Pass/Fail |
|---|---|---|---|
| Zero operational impact on OT processes | 0 incidents | | |
| Tool operates in passive mode throughout pilot | 100% passive | | |
| Data flowing into Sentinel continuously | < 5 min latency, < 1% data loss | | |
| OT Engineering approves continued deployment | Written approval | | |

### 6.2 Evaluation Success Criteria (Scored)

| Criterion | Target | Actual | Score (1–5) |
|---|---|---|---|
| Protocol parsing coverage | ≥ 90% of environment protocols | | |
| Detection use cases developed | ≥ 3 active rules | | |
| False positive rate | < 10/week | | |
| Analyst usability rating | ≥ 3/5 | | |
| Asset discovery accuracy | ≥ 80% of known assets identified | | |
| Time to first detection use case | < 4 weeks from data availability | | |

### 6.3 Decision Framework

| Outcome | Criteria | Action |
|---|---|---|
| **GO — Proceed to phased rollout** | All mandatory criteria PASS, evaluation score ≥ 3.5 average | Begin Phase 2 planning |
| **CONDITIONAL GO** | All mandatory criteria PASS, evaluation score 2.5–3.4 | Address specific gaps before rollout |
| **EXTEND PILOT** | Mandatory criteria PASS but insufficient evaluation data | Extend pilot by 4–6 weeks |
| **NO-GO** | Any mandatory criterion FAILS, or evaluation score < 2.5 | Do not proceed. Document findings for future reference |

---

## 7. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Tool causes OT operational disruption | Low | Critical | Safety validation protocol, passive-only deployment, emergency rollback |
| SIEM integration requires more effort than planned | Medium | Medium | Allocate contingency engineering time, engage vendor support early |
| Protocol support is inadequate for environment | Medium | High | Validate protocol support during first 2 weeks before investing in detection development |
| Vendor support is unresponsive during pilot | Low | Medium | Establish escalation contacts before pilot start, document SLA expectations |
| OT Engineering withdraws support | Low | Critical | Regular communication, involve engineering in all decisions, respect their veto on safety |

---

## 8. Pilot Completion Report

*To be completed at pilot end.*

### 8.1 Executive Summary

_______________

### 8.2 Results Against Success Criteria

*(Copy table from 6.1 and 6.2 with actual results)*

### 8.3 Key Findings

_______________

### 8.4 Lessons Learned

_______________

### 8.5 Recommendation

☐ GO — Proceed to phased rollout
☐ CONDITIONAL GO — Address: _______________
☐ EXTEND PILOT — Reason: _______________
☐ NO-GO — Reason: _______________

### 8.6 Sign-Off

| Role | Name | Decision | Date |
|---|---|---|---|
| Pilot Owner | | | |
| SOC Manager | | | |
| OT Engineering Sponsor | | | |
| CISO / Security Director | | | |
