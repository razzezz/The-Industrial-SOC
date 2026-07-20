# Framework Mapping Matrix: SOC-Relevant Requirements

**Purpose:** Cross-reference overlapping requirements across NCSC CAF v4.0, NIS 2, NIST SP 800-82r3, and ISA/IEC 62443 for SOC-relevant capabilities. Use this matrix to identify where a single improvement initiative satisfies multiple frameworks simultaneously, enabling integrated roadmap planning.

**How to Use:** For each capability area, the matrix shows the corresponding requirement from each framework. Shaded rows indicate capabilities where all four frameworks have overlapping requirements — these are the highest-priority improvement areas because closing a gap delivers compliance value across all frameworks simultaneously.

---

## Detection and Monitoring Capabilities

| SOC Capability | NCSC CAF v4.0 | NIS 2 | NIST SP 800-82r3 | ISA/IEC 62443 | Book Chapter |
|---------------|---------------|-------|-------------------|---------------|-------------|
| **Network monitoring at IT/OT boundary** | C1.a (Monitoring Coverage) | Art. 21(2)(a) — Security of networks | SI-4 (System Monitoring), AU-6 (Audit Record Review) | SR 6.1 (Audit Log Accessibility), SR 6.2 (Continuous Monitoring) | Ch 7 |
| **OT protocol-aware monitoring** | C1.a, C1.f (Behaviour & TI) | Art. 21(2)(a) | SI-4, SI-5 (Security Alerts) | SR 3.2 (Malicious Code Protection), SR 6.1 | Ch 7, Ch 8 |
| **Endpoint monitoring (workstations, HMIs)** | C1.a | Art. 21(2)(a) | SI-3 (Malicious Code Protection), SI-4 | SR 3.2 | Ch 7 |
| **Log collection and retention** | C1.b (Securing Logs) | Art. 21(2)(a) | AU-2 (Audit Events), AU-3 (Content of Audit Records), AU-11 (Audit Record Retention) | SR 6.1 | Ch 7 |
| **Log integrity protection** | C1.b | Art. 21(2)(a) | AU-9 (Protection of Audit Information) | SR 6.1 | Ch 7 |
| **SIEM correlation (IT + OT)** | C1.c (Generating Alerts), C1.d (Identifying Incidents) | Art. 21(2)(a) | SI-4, AU-6 | SR 6.2 | Ch 7, Ch 8 |
| **Behavioural baseline and anomaly detection** | C1.f (Understanding Behaviour) | Art. 21(2)(f) — Assessing effectiveness | SI-4 | SR 6.2 | Ch 7, Ch 8 |

---

## Threat Intelligence and Hunting

| SOC Capability | NCSC CAF v4.0 | NIS 2 | NIST SP 800-82r3 | ISA/IEC 62443 | Book Chapter |
|---------------|---------------|-------|-------------------|---------------|-------------|
| **Threat landscape analysis** | A2.b (Understanding Threat) | Art. 21(2)(e) — Vulnerability handling | RA-3 (Risk Assessment), PM-16 (Threat Awareness) | SR 2.8 (Auditable Events) | Ch 10 |
| **ATT&CK for ICS mapping** | C1.c, C2.b | Art. 21(2)(f) | SI-4, RA-5 | SR 6.1 | Ch 8, Ch 10 |
| **Structured threat hunting** | C2.b (Threat Hunting) | Art. 21(2)(f) | RA-5 (Vulnerability Monitoring), SI-4 | SR 6.1, SR 6.2 | Ch 9 |
| **Intelligence-driven detection** | C1.f, C2.b | Art. 21(2)(e) | PM-16, SI-5 | SR 2.8, SR 6.1 | Ch 8, Ch 10 |

---

## Incident Response

| SOC Capability | NCSC CAF v4.0 | NIS 2 | NIST SP 800-82r3 | ISA/IEC 62443 | Book Chapter |
|---------------|---------------|-------|-------------------|---------------|-------------|
| **ICS-specific IR playbooks** | D1.a (Response Plan) | Art. 21(2)(b) — Incident handling | IR-1 (IR Policy), IR-4 (Incident Handling), IR-8 (IR Plan) | SR 6.1 | Ch 11 |
| **Cross-functional CSIRT** | D1.b (Response Capability) | Art. 21(2)(b) | IR-2 (IR Training), IR-3 (IR Testing) | SR 6.2 | Ch 11, Ch 15 |
| **Incident classification (against regulatory threshold)** | D1.d (Incident Reporting) | Art. 23 — Reporting obligations | IR-6 (Incident Reporting) | SR 6.2 | Ch 11 |
| **24-hour early warning capability** | D1.d | Art. 23(4)(a) | IR-6 | SR 6.2 | Ch 11 |
| **72-hour incident notification** | D1.d | Art. 23(4)(b) | IR-6 | SR 6.2 | Ch 11, Ch 12 |
| **Tabletop exercises** | D1.c (Testing) | Art. 21(2)(f) | IR-3 (IR Testing), CP-4 (Contingency Plan Testing) | SR 6.2 | Ch 11, Ch 16 |

---

## Incident Recovery and Lessons Learned

| SOC Capability | NCSC CAF v4.0 | NIS 2 | NIST SP 800-82r3 | ISA/IEC 62443 | Book Chapter |
|---------------|---------------|-------|-------------------|---------------|-------------|
| **Post-incident review / After-action review** | D2.a (Root Cause Analysis) | Art. 23(4)(d) — Final report | IR-4, IR-8 | SR 6.2 | Ch 12 |
| **Lessons learned feeding detection improvement** | D2.b (Using Lessons Learned) | Art. 21(2)(f) | IR-4, SI-4 | SR 2.11 (Improvement) | Ch 12, Ch 16 |
| **Intelligence sharing (ISAC)** | D2.b | Art. 29 — Voluntary information sharing | PM-15 (External Contact) | SR 2.8 | Ch 10, Ch 12 |

---

## Asset Management and Architecture

| SOC Capability | NCSC CAF v4.0 | NIS 2 | NIST SP 800-82r3 | ISA/IEC 62443 | Book Chapter |
|---------------|---------------|-------|-------------------|---------------|-------------|
| **OT asset inventory** | A3.a (Asset Management) | Art. 21(2)(a) | CM-8 (System Component Inventory) | SR 7.8 (Control System Component Inventory) | Ch 6 |
| **Crown jewel analysis** | A3.a | Art. 21(2)(a) | RA-2 (Security Categorisation) | Zone/Conduit assessment (62443-3-2) | Ch 6 |
| **Network segmentation (zones and conduits)** | B5.a (Resilient Design) | Art. 21(2)(a) | SC-7 (Boundary Protection) | SR 5.1 (Network Segmentation), SR 7.6 | Ch 5 |
| **IDMZ architecture** | B5.a | Art. 21(2)(a) | SC-7 | SR 5.1, SR 5.2 (Zone Boundary Protection) | Ch 5 |

---

## Access Control and Identity

| SOC Capability | NCSC CAF v4.0 | NIS 2 | NIST SP 800-82r3 | ISA/IEC 62443 | Book Chapter |
|---------------|---------------|-------|-------------------|---------------|-------------|
| **Authentication monitoring** | B2.a (Identity Verification), C1.a | Art. 21(2)(a) | AC-7 (Unsuccessful Login Attempts), AU-2 | SR 1.1 (Human User Identification), SR 1.2 (Software Process ID) | Ch 7, Ch 8 |
| **Credential abuse detection** | C1.a, C1.f | Art. 21(2)(a) | AC-7, SI-4 | SR 1.1 | Ch 8, UC-ICS-004 |
| **Vendor/third-party access monitoring** | B2.a, C1.a | Art. 21(2)(d) — Supply chain security | AC-17 (Remote Access), AU-2 | SR 1.13 (Remote Access) | Ch 5 |

---

## Continuous Improvement

| SOC Capability | NCSC CAF v4.0 | NIS 2 | NIST SP 800-82r3 | ISA/IEC 62443 | Book Chapter |
|---------------|---------------|-------|-------------------|---------------|-------------|
| **Detection coverage assessment** | C1.a, C2.b | Art. 21(2)(f) | CA-2 (Control Assessments), CA-7 (Continuous Monitoring) | SR 2.11 | Ch 8, Ch 16 |
| **Security metrics (MTTD, MTTR, coverage)** | All Objectives | Art. 21(2)(f) | CA-7, PM-6 (Measures of Performance) | SR 2.11 | Ch 16 |
| **Purple team / detection validation** | C1.a, D1.c | Art. 21(2)(f) | CA-8 (Penetration Testing), IR-3 | SR 6.2 | Ch 16 |
| **Maturity progression** | All Objectives | Art. 21(2)(f) | CA-2, PM-6 | SR 2.11 | Ch 16 |

---

## Using This Matrix

### Identifying High-Priority Gaps

A gap that maps to requirements in all four frameworks is a higher priority than one that maps to a single framework. When building your integrated roadmap:

1. Sort gaps by the number of frameworks they impact (more = higher priority)
2. Within equal-priority gaps, sequence by dependency (e.g., log collection before SIEM correlation)
3. Within equal-dependency gaps, prioritise by regulatory enforcement deadline

### Evidencing a Single Initiative Against Multiple Frameworks

When you implement a capability (e.g., network monitoring at the IDMZ), document it once and reference it in multiple compliance contexts. Example:

**Initiative:** Deploy Zeek with ICS protocol parsers at the IDMZ boundary, forwarding to Microsoft Sentinel.

**Evidence Produced:**
- Detection use case documentation (satisfies CAF C1.a, C1.c, NIS 2 Art. 21(2)(a), NIST SI-4, 62443 SR 6.1)
- Alert records and investigation logs (satisfies CAF C1.d, NIS 2 Art. 21(2)(b), NIST AU-6)
- ATT&CK for ICS coverage assessment (satisfies CAF C2.b, NIS 2 Art. 21(2)(f), NIST RA-5)

This single initiative and its documentation address requirements across all four frameworks.

---

*This matrix accompanies Chapter 4: The Regulatory Roadmap. Use alongside the Regulatory Applicability Checklist to build your integrated compliance roadmap.*
