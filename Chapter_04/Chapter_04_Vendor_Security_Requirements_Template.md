# OT Vendor Security Requirements Template

**Purpose:** Communicate minimum security requirements to OT vendors, system integrators, and managed service providers. Aligned to the PSTI Act, ISA/IEC 62443-4-2 component requirements, NCSC CAF v4.0 software security expectations, and the forthcoming UK Cyber Security and Resilience Bill.

**Usage:** Include as an appendix to procurement specifications, RFPs, and vendor contracts. Tailor to your specific environment by marking requirements as Mandatory, Preferred, or Not Applicable.

---

## Section 1: Vendor Information

| Field | Response |
|-------|----------|
| **Vendor Name** | |
| **Product / Service Name** | |
| **Product Category** | ☐ PLC/RTU ☐ DCS ☐ SCADA/HMI ☐ Historian ☐ Engineering Workstation ☐ Network Equipment ☐ Safety System (SIS) ☐ NDR/Security Tool ☐ Managed Service ☐ Other: _______ |
| **Intended Purdue Level(s)** | ☐ L0 ☐ L1 ☐ L2 ☐ L3 ☐ L3.5 (IDMZ) ☐ L4 ☐ L5 |
| **Protocols Used** | |
| **Assessment Date** | |
| **Assessed By** | |

---

## Section 2: Authentication and Access Control

*Aligned to ISA/IEC 62443-4-2 CR 1.1–1.14, NCSC CAF B2*

| # | Requirement | Priority | Vendor Response | Evidence Provided | Compliance |
|---|------------|----------|-----------------|-------------------|------------|
| 2.1 | Product supports unique user accounts (no default shared accounts required for operation) | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 2.2 | Default credentials are prohibited or must be changed during initial commissioning (PSTI Act requirement) | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 2.3 | Product supports role-based access control (RBAC) with separation between operator, engineer, and administrator roles | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 2.4 | Product supports integration with centralised authentication (Active Directory, LDAP, RADIUS) | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 2.5 | Product supports multi-factor authentication for administrative and engineering access | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 2.6 | Failed authentication attempts are logged with timestamp, source, and username | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 2.7 | Account lockout or rate limiting is supported for repeated authentication failures | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |

---

## Section 3: Logging and Audit Trail

*Aligned to ISA/IEC 62443-4-2 CR 6.1–6.2, NCSC CAF C1, NIST SP 800-82r3 AU family*

| # | Requirement | Priority | Vendor Response | Evidence Provided | Compliance |
|---|------------|----------|-----------------|-------------------|------------|
| 3.1 | Product generates security-relevant audit logs, including authentication events, configuration changes, and firmware/logic modifications | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 3.2 | Audit logs include: timestamp (UTC), event type, source identity, target asset, and outcome (success/failure) | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 3.3 | Product supports forwarding audit logs to external SIEM via syslog, CEF, or native API | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 3.4 | Audit logs are protected against tampering and unauthorised deletion | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 3.5 | Product supports configurable log retention periods | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 3.6 | Firmware or logic upload/download events are logged | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |

---

## Section 4: Secure Software Development

*Aligned to NCSC CAF v4.0 B4 (Software Security), PSTI Act, ISA/IEC 62443-4-1*

| # | Requirement | Priority | Vendor Response | Evidence Provided | Compliance |
|---|------------|----------|-----------------|-------------------|------------|
| 4.1 | Vendor follows a recognised secure software development framework (e.g., NIST SSDF, Microsoft SDL, ISA/IEC 62443-4-1) | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 4.2 | Vendor can provide evidence of secure development practices (code review, static analysis, penetration testing) | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 4.3 | Vendor provides a Software Bill of Materials (SBOM) for the product | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 4.4 | Third-party components are actively monitored for vulnerabilities throughout the product lifecycle | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 4.5 | Product has achieved ISA/IEC 62443-4-2 certification or can evidence compliance | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |

---

## Section 5: Vulnerability Management

*Aligned to PSTI Act, NCSC CAF B4, ISA/IEC 62443-4-1 SVV-1–3*

| # | Requirement | Priority | Vendor Response | Evidence Provided | Compliance |
|---|------------|----------|-----------------|-------------------|------------|
| 5.1 | Vendor maintains a public vulnerability disclosure policy | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 5.2 | Vendor provides security patches and advisories for disclosed vulnerabilities within defined SLAs | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 5.3 | Security patches can be applied without requiring full system re-certification or extended downtime | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 5.4 | Vendor provides defined support lifecycle with end-of-support dates published in advance | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 5.5 | Vendor participates in coordinated vulnerability disclosure (CVD) and assigns CVE identifiers | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |

---

## Section 6: Network Security

*Aligned to ISA/IEC 62443-4-2 CR 5.1–5.4, NIST SP 800-82r3 SC family*

| # | Requirement | Priority | Vendor Response | Evidence Provided | Compliance |
|---|------------|----------|-----------------|-------------------|------------|
| 6.1 | Product supports encrypted communication channels (TLS 1.2+, SSH) for management and configuration interfaces | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 6.2 | Product supports network segmentation — can operate within defined zones without requiring unrestricted network access | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 6.3 | Product does not require inbound connections from external networks for normal operation | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 6.4 | All network ports, protocols, and services used by the product are documented | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 6.5 | Unnecessary services and ports can be disabled without affecting core functionality | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |

---

## Section 7: Data Integrity and Availability

*Aligned to ISA/IEC 62443-4-2 CR 3.1–3.9, NIST SP 800-82r3 SI family*

| # | Requirement | Priority | Vendor Response | Evidence Provided | Compliance |
|---|------------|----------|-----------------|-------------------|------------|
| 7.1 | Product validates integrity of firmware and software before execution (code signing, integrity checks) | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 7.2 | Product supports backup and restoration of configuration and logic | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 7.3 | Product supports graceful degradation — maintains safe operation state during partial failure | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 7.4 | Product does not introduce unacceptable latency or jitter to real-time control processes | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |

---

## Section 8: Vendor Remote Access and Support

*Aligned to ISA/IEC 62443-2-4, NCSC CAF B2, NIS 2 Art. 21(2)(d)*

| # | Requirement | Priority | Vendor Response | Evidence Provided | Compliance |
|---|------------|----------|-----------------|-------------------|------------|
| 8.1 | Vendor remote access requires unique authenticated accounts (no shared or generic accounts) | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 8.2 | Vendor remote access sessions are logged with full session capture capability | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 8.3 | Vendor remote access is terminated upon completion — no persistent access | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 8.4 | Vendor will notify operator of security incidents affecting their products or services within agreed timescales | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 8.5 | Vendor remote access traverses the organisation's jump host / privileged access management infrastructure | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |

---

## Section 9: Incident and Vulnerability Notification

*Aligned to CS&R Bill, NIS 2, NCSC CAF D1*

| # | Requirement | Priority | Vendor Response | Evidence Provided | Compliance |
|---|------------|----------|-----------------|-------------------|------------|
| 9.1 | Vendor has a documented incident response process | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 9.2 | Vendor will notify operator of security vulnerabilities in their product within __ business days of discovery | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 9.3 | Vendor will cooperate with operator incident response activities, including providing technical assistance and IOCs | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |
| 9.4 | Vendor maintains cyber insurance appropriate to the services provided | ☐ Mandatory ☐ Preferred ☐ N/A | | | ☐ Met ☐ Partial ☐ Gap |

---

## Assessment Summary

| Section | Requirements Met | Partial | Gaps | Total |
|---------|-----------------|---------|------|-------|
| Authentication & Access Control | | | | 7 |
| Logging & Audit Trail | | | | 6 |
| Secure Software Development | | | | 5 |
| Vulnerability Management | | | | 5 |
| Network Security | | | | 5 |
| Data Integrity & Availability | | | | 4 |
| Remote Access & Support | | | | 5 |
| Incident & Vulnerability Notification | | | | 4 |
| **TOTAL** | | | | **41** |

---

## Risk Acceptance

Where a vendor cannot meet a Mandatory requirement, document the risk acceptance below:

| Requirement # | Risk Description | Compensating Control | Risk Accepted By | Date |
|--------------|-----------------|---------------------|-----------------|------|
| | | | | |
| | | | | |
| | | | | |

---

**Assessment Completed By:** _______________
**Date:** _______________
**Vendor Signoff:** _______________
**Next Review Date:** _______________

---

*This template accompanies Chapter 4: The Regulatory Roadmap. It should be used alongside your organisation's standard procurement processes and reviewed by legal and procurement teams before inclusion in contracts.*
