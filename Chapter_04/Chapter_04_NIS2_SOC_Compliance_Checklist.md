# NIS 2 SOC Compliance Checklist

**Purpose:** Identify and track NIS 2 Directive requirements that directly impact Security Operations Centre capabilities in ICS/OT environments, with practical guidance on demonstrating compliance through operational evidence.

**Scope:** This checklist covers the NIS 2 requirements (Articles 21 and 23 primarily) that require active SOC involvement. It does not cover governance, policy, or organisational measures that fall outside SOC operational responsibility.

**Note:** NIS 2 is transposed into national law by each EU member state. Specific requirements may vary by jurisdiction. This checklist is based on the directive text and should be cross-referenced with your national transposition law.

---

## Part 1: Risk Management Measures (Article 21)

### Detection and Monitoring Capabilities

| # | Requirement (Art. 21 Reference) | SOC Implication | Current Status | Evidence Available | Gap / Action Required | Owner | Target |
|---|-------------------------------|-----------------|----------------|-------------------|---------------------|-------|--------|
| 1.1 | Security of network and information systems acquisition, development, and maintenance, including vulnerability handling and disclosure (Art. 21(2)(e)) | SOC must monitor for vulnerabilities in OT systems. Vulnerability assessment results must be documented and tracked. | ☐ Met ☐ Partial ☐ Gap | | | | |
| 1.2 | Policies and procedures to assess the effectiveness of cybersecurity risk-management measures (Art. 21(2)(f)) | SOC must demonstrate detection effectiveness through testing, metrics (MTTD, MTTR), and coverage assessments. | ☐ Met ☐ Partial ☐ Gap | | | | |
| 1.3 | Basic cyber hygiene practices and cybersecurity training (Art. 21(2)(g)) | SOC analysts must receive OT-specific training. Training records must be maintained. | ☐ Met ☐ Partial ☐ Gap | | | | |
| 1.4 | Supply chain security, including security-related aspects concerning the relationships between each entity and its direct suppliers or service providers (Art. 21(2)(d)) | SOC must monitor third-party access to OT environments. Vendor session monitoring and anomaly detection required. | ☐ Met ☐ Partial ☐ Gap | | | | |

### Incident Handling Capabilities

| # | Requirement (Art. 21 Reference) | SOC Implication | Current Status | Evidence Available | Gap / Action Required | Owner | Target |
|---|-------------------------------|-----------------|----------------|-------------------|---------------------|-------|--------|
| 2.1 | Incident handling (Art. 21(2)(b)) | SOC must have documented incident response procedures covering OT environments. Procedures must account for OT safety constraints. | ☐ Met ☐ Partial ☐ Gap | | | | |
| 2.2 | Business continuity management, including backup management, disaster recovery, and crisis management (Art. 21(2)(c)) | SOC IR playbooks must integrate with business continuity plans. Recovery procedures for OT systems must be documented and tested. | ☐ Met ☐ Partial ☐ Gap | | | | |

---

## Part 2: Incident Reporting (Article 23)

### Reporting Readiness

| # | Requirement | SOC Capability Required | Current Status | Evidence | Gap / Action | Owner | Target |
|---|------------|------------------------|----------------|----------|-------------|-------|--------|
| 3.1 | **Early Warning — within 24 hours** of becoming aware of a significant incident | Detection capability sufficient to identify significant incidents in near-real-time. Triage process to classify incidents against NIS 2 "significant incident" threshold. | ☐ Met ☐ Partial ☐ Gap | | | | |
| 3.2 | **Incident Notification — within 72 hours** providing initial assessment, severity, impact, and IOCs | Investigation capability to produce initial assessment within 72 hours. IOC extraction and documentation process. | ☐ Met ☐ Partial ☐ Gap | | | | |
| 3.3 | **Final Report — within 1 month** (or intermediate progress report if incident ongoing) | Post-incident reporting capability including root cause analysis, impact assessment, remediation measures, and cross-border impact assessment. | ☐ Met ☐ Partial ☐ Gap | | | | |
| 3.4 | Reporting to CSIRT or competent authority | Escalation path from SOC to reporting authority documented and tested. Contact details for relevant CSIRT and competent authority maintained. | ☐ Met ☐ Partial ☐ Gap | | | | |

### Significant Incident Classification

NIS 2 defines a significant incident as one that:
- Has caused or is capable of causing **severe operational disruption** of the service or **financial loss** for the entity concerned, OR
- Has affected or is capable of affecting other natural or legal persons by causing **considerable material or non-material damage**

| # | Classification Capability | SOC Readiness | Notes |
|---|--------------------------|---------------|-------|
| 4.1 | Can your SOC classify an OT security event against the "severe operational disruption" threshold within 24 hours? | ☐ Yes ☐ No ☐ Partial | |
| 4.2 | Does your triage process include OT operational impact assessment (in coordination with OT engineering)? | ☐ Yes ☐ No ☐ Partial | |
| 4.3 | Is the "significant incident" threshold defined in your SOC procedures with OT-specific examples? | ☐ Yes ☐ No ☐ Partial | |
| 4.4 | Have you tested your ability to meet the 24-hour early warning deadline in a tabletop exercise? | ☐ Yes ☐ No | |

---

## Part 3: Detection Capability Requirements

The following detection capabilities are necessary to meet NIS 2 obligations. Cross-reference with your detection engineering programme and ATT&CK for ICS coverage assessment.

| # | Detection Capability | Required for NIS 2? | Current State | ATT&CK for ICS Techniques Covered | Book Reference |
|---|---------------------|---------------------|---------------|-----------------------------------|----------------|
| 5.1 | Unauthorised access to OT networks | Yes (Art. 21(2)(a)) | ☐ Active ☐ Planned ☐ Gap | T0886, T0859 | Ch 8, UC-ICS-003 |
| 5.2 | Lateral movement from IT to OT | Yes (Art. 21(2)(a)) | ☐ Active ☐ Planned ☐ Gap | T0867, T0886 | Ch 8, UC-ICS-009 |
| 5.3 | Unauthorised ICS protocol commands | Yes (Art. 21(2)(a)) | ☐ Active ☐ Planned ☐ Gap | T0855, T0821 | Ch 8, UC-ICS-001, UC-ICS-002 |
| 5.4 | Credential compromise in OT systems | Yes (Art. 21(2)(a)) | ☐ Active ☐ Planned ☐ Gap | T0859 | Ch 8, UC-ICS-004 |
| 5.5 | Malware/ransomware at IT/OT boundary | Yes (Art. 21(2)(b)) | ☐ Active ☐ Planned ☐ Gap | T0865, T0866 | Ch 7, Ch 8 |
| 5.6 | Third-party/vendor access anomalies | Yes (Art. 21(2)(d)) | ☐ Active ☐ Planned ☐ Gap | T0859, T0886 | Ch 5, UC-ICS-009 |
| 5.7 | Data exfiltration from OT networks | Yes (Art. 21(2)(a)) | ☐ Active ☐ Planned ☐ Gap | T0882, T0811 | Ch 8 |

---

## Part 4: Evidence Checklist for NIS 2 Audit

| # | Evidence Item | Description | Available? | Location |
|---|-------------|-------------|------------|----------|
| E1 | Detection rule inventory | List of all active SIEM and IDS detection rules with ATT&CK for ICS mapping | ☐ Yes ☐ No | |
| E2 | Incident response playbooks | Documented IR procedures covering OT-specific scenarios | ☐ Yes ☐ No | |
| E3 | IR testing records | Documentation of tabletop exercises and their outcomes | ☐ Yes ☐ No | |
| E4 | Incident log | Record of security incidents, classification, response actions, and timelines | ☐ Yes ☐ No | |
| E5 | Detection metrics | MTTD, MTTR, alert volume, false positive rate, detection coverage score | ☐ Yes ☐ No | |
| E6 | Threat intelligence programme | Evidence of threat landscape analysis and intelligence-driven detection | ☐ Yes ☐ No | |
| E7 | Training records | SOC analyst OT security training documentation | ☐ Yes ☐ No | |
| E8 | Vendor monitoring records | Evidence of third-party access monitoring and anomaly detection | ☐ Yes ☐ No | |
| E9 | Vulnerability management records | OT vulnerability assessment results and remediation tracking | ☐ Yes ☐ No | |
| E10 | After-action reports | Post-incident reviews with root cause analysis and improvement actions | ☐ Yes ☐ No | |

---

## Summary

| Area | Items Met | Items Partial | Items Gap | Total |
|------|----------|--------------|-----------|-------|
| Risk Management (Part 1) | | | | 4 |
| Incident Reporting (Part 2) | | | | 4 |
| Incident Classification (Part 2) | | | | 4 |
| Detection Capabilities (Part 3) | | | | 7 |
| Evidence (Part 4) | | | | 10 |
| **TOTAL** | | | | **29** |

**Assessment Date:** _______________
**Assessed By:** _______________
**Next Review Date:** _______________

---

*This checklist accompanies Chapter 4: The Regulatory Roadmap. For the full NIS 2 Directive text, refer to Directive (EU) 2022/2555 at https://eur-lex.europa.eu/eli/dir/2022/2555*
