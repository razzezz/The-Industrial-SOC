# OT Cyber Defence Maturity Self-Assessment Scorecard
# ================================================================
# Description: Structured self-assessment tool for evaluating OT
#   cyber defence maturity across seven capability domains.
#   Each domain is assessed against five maturity levels with
#   clear criteria. Designed for cross-functional completion.
#
# Usage: Complete this assessment with input from IT Security,
#   OT Engineering, and Operations. Reassess at least annually
#   (every six months during active improvement phases).
#   Compare scores over time to track improvement trends.
# ================================================================

## Assessment Information

| Field | Value |
|-------|-------|
| **Organisation** | [Name] |
| **Assessment Date** | [Date] |
| **Assessed By** | [Names and roles of all assessors] |
| **Previous Assessment Date** | [Date or "First Assessment"] |
| **Target Maturity Level** | [Overall target] |

---

## Scoring Guide

For each capability domain, select the maturity level (1–5) that most accurately describes the **current operational state** — not the planned state, not the state on a good day, but the typical, sustained capability.

If the organisation meets some but not all criteria for a level, score at the lower level. Partial capability at a higher level should be noted in the comments but does not qualify for that level's score.

---

## Domain 1: Asset Visibility

| Level | Criteria |
|-------|----------|
| **1 — Chaotic** | No OT-specific asset inventory accessible to the security team. OT assets are known only to engineering, if at all. No classification of assets by criticality. |
| **2 — Managed** | Basic inventory of crown jewel assets exists (may be spreadsheet-based). OT_AssetRegister watchlist created in SIEM with crown jewel entries. Crown jewels identified through structured exercise with engineering input. |
| **3 — Defined** | Comprehensive asset inventory covering all Purdue levels, with crown jewel tiers (Tier 1, Tier 2, Tier 3) assigned. Inventory is maintained and reviewed at least quarterly. Asset data is accessible to the SOC and integrated into detection logic and triage procedures. |
| **4 — Proactive** | Asset inventory is continuously updated through automated discovery (passive network monitoring, DHCP/DNS correlation). Asset context (firmware versions, communication baselines, maintenance schedules) is integrated into the SIEM. Changes to the asset landscape trigger review of detection coverage. |
| **5 — Optimised** | Real-time asset visibility across all Purdue levels. Automated detection of new or changed assets with immediate assessment and classification. Asset data feeds attack path analysis and predictive threat modelling. Full lifecycle tracking from deployment to decommissioning. |

**Current Level:** [ ]  
**Previous Level:** [ ]  
**Target Level:** [ ]  
**Comments/Evidence:**  

---

## Domain 2: Detection and Monitoring

| Level | Criteria |
|-------|----------|
| **1 — Chaotic** | No OT-specific detection rules or monitoring. OT incidents discovered through operational impact. No SIEM integration of OT telemetry. |
| **2 — Managed** | Basic monitoring deployed at IDMZ (Purdue Level 3.5). Initial detection rules for IT/OT boundary traffic deployed in SIEM. Zeek/Suricata or equivalent passive monitoring on SPAN/TAP at boundary. |
| **3 — Defined** | OT-specific SIEM use cases deployed, tuned, and documented. Detection coverage extends into OT network (Purdue Levels 2–3). EDR deployed on engineering workstations/HMIs. ATT&CK for ICS coverage assessment conducted with gaps documented. OT False Positive Rate tracked and managed. |
| **4 — Proactive** | Detection engineering driven by intelligence and ATT&CK for ICS coverage gaps. IT/OT log correlation functioning for cross-boundary incident reconstruction. Detection covers ICS-specific tactics (Inhibit Response Function, Impair Process Control, Impact). Detection rules reviewed and refined based on exercise and incident findings. |
| **5 — Optimised** | ML-assisted anomaly detection deployed with human-in-the-loop. Continuous detection refinement based on intelligence, exercises, and incidents. Industry-leading ATT&CK for ICS coverage. Detection contributes to sector-wide intelligence sharing. |

**Current Level:** [ ]  
**Previous Level:** [ ]  
**Target Level:** [ ]  
**Comments/Evidence:**  

---

## Domain 3: Threat Hunting

| Level | Criteria |
|-------|----------|
| **1 — Chaotic** | No threat hunting capability. Investigation is purely reactive (alert-driven). |
| **2 — Managed** | Ad-hoc investigation of OT anomalies, but no structured hunting programme. Some proactive analysis driven by individual analyst curiosity. |
| **3 — Defined** | Initial hunting operations conducted, but not yet regular or structured. Hunting methodology defined (hypothesis-driven). Data sources identified and accessible for hunting. |
| **4 — Proactive** | Structured threat hunting programme with regular operations (monthly or more). Hypotheses informed by CTI and ATT&CK for ICS. Documented findings feed detection engineering and architectural improvements. Hunt results tracked as a metric. |
| **5 — Optimised** | Advanced hunting leveraging ML-assisted analytics and graph-based analysis. Hunt findings contribute to sector-wide intelligence. Hunting programme identifies novel threats not covered by existing detection. Continuous hunting operations integrated into daily SOC workflow. |

**Current Level:** [ ]  
**Previous Level:** [ ]  
**Target Level:** [ ]  
**Comments/Evidence:**  

---

## Domain 4: Threat Intelligence

| Level | Criteria |
|-------|----------|
| **1 — Chaotic** | No CTI function. Threat awareness limited to general news and vendor marketing. No intelligence requirements defined. |
| **2 — Managed** | Passive consumption of threat intelligence from government alerts (CISA, NCSC) and vendor reports. No structured processing or operationalisation. Awareness of key threat actors relevant to sector. |
| **3 — Defined** | Intelligence requirements defined for the organisation's sector and operational environment. Structured processing of threat intelligence using the intelligence cycle. CTI products (threat profiles, IOC feeds) produced and disseminated to detection engineers and hunters. |
| **4 — Proactive** | Operational CTI function producing intelligence requirements, threat profiles, and detection recommendations. Intelligence drives detection engineering priorities, hunting hypotheses, and exercise scenarios. Intelligence feedback loop from incidents and AARs is operational. |
| **5 — Optimised** | Strategic CTI capability informing board-level risk decisions. Predictive threat modelling based on adversary capability and intent analysis. Active contribution to sector-wide intelligence sharing (ISACs, government partnerships). Graph-based threat intelligence and attack path analysis operational. |

**Current Level:** [ ]  
**Previous Level:** [ ]  
**Target Level:** [ ]  
**Comments/Evidence:**  

---

## Domain 5: Incident Response

| Level | Criteria |
|-------|----------|
| **1 — Chaotic** | No documented IR playbooks for OT scenarios. No CSIRT roster. Response is ad-hoc and uncoordinated. No decision authority structure defined. |
| **2 — Managed** | 3–5 documented IR playbooks for critical OT scenarios. CSIRT roster established with IT Security, OT Engineering, and Operations. First tabletop exercise completed. Basic escalation process from SOC to engineering. |
| **3 — Defined** | IR playbooks cover all common OT scenarios. Regular tabletop exercises (quarterly). At least one functional exercise completed. CSIRT tested through exercise or real incident. After-Action Reviews conducted for all OT incidents. Communication templates established. |
| **4 — Proactive** | Playbooks refined based on incident and exercise experience. Decision authority structure tested and effective. SOAR automation deployed for enrichment and notification (not containment below L3.5). Purple team exercises test response capabilities annually. Intelligence-informed response procedures. |
| **5 — Optimised** | Response capability validated through regular red/purple team exercises. Rapid CSIRT assembly (<30 min for Sev 1). Response procedures adapted to adversary-specific TTPs. Incident experience contributes to sector-wide response improvement. Forensic capability including OT evidence collection. |

**Current Level:** [ ]  
**Previous Level:** [ ]  
**Target Level:** [ ]  
**Comments/Evidence:**  

---

## Domain 6: Cross-Functional Collaboration

| Level | Criteria |
|-------|----------|
| **1 — Chaotic** | No formal relationship between SOC and OT Engineering. Mutual distrust or indifference. No shared processes or communication channels. |
| **2 — Managed** | Initial engagement between SOC and OT Engineering. CSIRT roster establishes named contacts. Basic escalation process exists. Engineering aware of monitoring deployment. |
| **3 — Defined** | Engineering liaison function operational. Maintenance window data shared with SOC (OT_MaintenanceWindows watchlist populated). Regular touchpoints between SOC and engineering. Shadow engineering sessions initiated. RACI matrix defined for hybrid SOC model if applicable. |
| **4 — Proactive** | Collaboration is routine and unremarkable. MTTEE consistently within target. Engineering participates in exercise design and AAR. Satisfaction surveys indicate healthy relationships. Joint training sessions conducted regularly. |
| **5 — Optimised** | Fully integrated OT security function with hybrid IT/OT expertise. Engineering and security operate as a single team for incident response. Joint career development paths. Cross-functional collaboration cited as a programme strength in audits and assessments. |

**Current Level:** [ ]  
**Previous Level:** [ ]  
**Target Level:** [ ]  
**Comments/Evidence:**  

---

## Domain 7: Metrics and Measurement

| Level | Criteria |
|-------|----------|
| **1 — Chaotic** | No OT-specific security metrics tracked. Programme effectiveness is unmeasured. |
| **2 — Managed** | Basic metrics tracked: number of OT alerts, escalations to engineering. No trend analysis. No regular reporting. |
| **3 — Defined** | Technical and operational metrics tracked: MTTD, MTTT, OT FP Rate, Crown Jewel Monitoring Coverage. Quarterly reporting to leadership. Trend analysis over time. |
| **4 — Proactive** | Full metrics framework including technical, operational, collaboration, and business metrics. Metrics drive improvement priorities. Quarterly Improvement Review established with executive participation. |
| **5 — Optimised** | Board-level reporting with business metrics demonstrating measurable risk reduction. Metrics benchmarked against sector peers. Predictive analytics on programme performance. Insurance and compliance improvements directly attributable to measured capability improvements. |

**Current Level:** [ ]  
**Previous Level:** [ ]  
**Target Level:** [ ]  
**Comments/Evidence:**  

---

## Summary Scorecard

| Domain | Previous | Current | Target | Gap |
|--------|----------|---------|--------|-----|
| Asset Visibility | | | | |
| Detection and Monitoring | | | | |
| Threat Hunting | | | | |
| Threat Intelligence | | | | |
| Incident Response | | | | |
| Cross-Functional Collaboration | | | | |
| Metrics and Measurement | | | | |
| **Overall (Average)** | | | | |

## Priority Improvement Areas (Top 3)

1. **Domain:** [ ] — **Current:** [ ] — **Target:** [ ] — **Key Action:** [ ]
2. **Domain:** [ ] — **Current:** [ ] — **Target:** [ ] — **Key Action:** [ ]
3. **Domain:** [ ] — **Current:** [ ] — **Target:** [ ] — **Key Action:** [ ]

## Assessment Sign-Off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| IT Security Lead | | | |
| OT Engineering Lead | | | |
| Operations Lead | | | |
| Executive Sponsor | | | |
