# Intelligence Requirements Template
# ================================================================
# Description: Structured template for documenting intelligence
#   requirements with priority, sources, and satisfaction status.
#   Pre-populated with requirements derived from the four sources
#   described in Chapter 10: threat landscape, detection gaps,
#   vulnerability landscape, and geopolitical context.
#
# Usage: Review and customise requirements quarterly. Assign
#   ownership to specific analysts. Track satisfaction status to
#   identify collection gaps.
# ================================================================

## PROGRAMME METADATA

- **Organisation**: [Name]
- **Sector**: [e.g., Energy, Water, Manufacturing]
- **Last Review Date**: [Date]
- **Next Scheduled Review**: [Date]
- **CTI Programme Owner**: [Name / Role]

---

## INTELLIGENCE REQUIREMENTS

### Priority Definitions
- **Critical**: Must be answered to maintain operational security posture; reviewed weekly
- **Important**: Significantly informs security decisions; reviewed monthly
- **Routine**: Provides context and situational awareness; reviewed quarterly

---

### IR-01: Threat Landscape — Active Threat Actors

| Field | Value |
|-------|-------|
| **Requirement ID** | IR-01 |
| **Question** | Which threat actors are currently targeting our sector and geography, and what TTPs do they employ? |
| **Priority** | Critical |
| **Source(s)** | Chapter 3 case studies, Dragos Year in Review, CISA ICS-CERT advisories, sector ISAC intelligence |
| **Collection Source(s)** | CISA ICS-CERT, Dragos WorldView/OT-CERT, sector ISAC feed, Microsoft Threat Intelligence |
| **Responsible Analyst** | [Name] |
| **Review Frequency** | Weekly |
| **Satisfaction Status** | ☐ Satisfied ☐ Partially Satisfied ☐ Unsatisfied |
| **Notes** | |

---

### IR-02: Threat Landscape — Emerging Capabilities

| Field | Value |
|-------|-------|
| **Requirement ID** | IR-02 |
| **Question** | What new ICS-targeting malware, tools, or frameworks have been publicly disclosed or observed in the wild? |
| **Priority** | Critical |
| **Source(s)** | Vendor threat research (Dragos, Mandiant, ESET, Microsoft), CISA advisories, academic publications |
| **Collection Source(s)** | Dragos intelligence reports, CISA alerts, vendor security blogs, MITRE ATT&CK for ICS updates |
| **Responsible Analyst** | [Name] |
| **Review Frequency** | Weekly |
| **Satisfaction Status** | ☐ Satisfied ☐ Partially Satisfied ☐ Unsatisfied |
| **Notes** | |

---

### IR-03: Detection Coverage Gaps

| Field | Value |
|-------|-------|
| **Requirement ID** | IR-03 |
| **Question** | Which ATT&CK for ICS techniques used by threat actors targeting our sector are not covered by our current detection rules or hunting capabilities? |
| **Priority** | Critical |
| **Source(s)** | ATTCK_ICS_Coverage_Assessment query output (Chapter 7), OT Kill Chain Mapping Worksheets (Chapter 3) |
| **Collection Source(s)** | Internal — Sentinel coverage assessment, detection rule inventory |
| **Responsible Analyst** | [Name] |
| **Review Frequency** | Monthly |
| **Satisfaction Status** | ☐ Satisfied ☐ Partially Satisfied ☐ Unsatisfied |
| **Notes** | |

---

### IR-04: Vulnerability Landscape — Active Exploitation

| Field | Value |
|-------|-------|
| **Requirement ID** | IR-04 |
| **Question** | Which ICS/OT vulnerabilities affecting products in our asset register are being actively exploited in the wild? |
| **Priority** | Critical |
| **Source(s)** | CISA KEV catalogue, ICS-CERT advisories, vendor security advisories |
| **Collection Source(s)** | CISA KEV RSS, ICS-CERT email list, vendor notification portals |
| **Responsible Analyst** | [Name] |
| **Review Frequency** | Weekly |
| **Satisfaction Status** | ☐ Satisfied ☐ Partially Satisfied ☐ Unsatisfied |
| **Notes** | Cross-reference against OT_AssetRegister watchlist |

---

### IR-05: Vulnerability Landscape — Product-Specific Advisories

| Field | Value |
|-------|-------|
| **Requirement ID** | IR-05 |
| **Question** | What new vulnerabilities have been disclosed in the specific products and firmware versions in our OT asset register? |
| **Priority** | Important |
| **Source(s)** | Vendor security advisories, CISA ICS-CERT advisories, NVD |
| **Collection Source(s)** | [List vendor portals for products in your environment] |
| **Responsible Analyst** | [Name] |
| **Review Frequency** | Weekly |
| **Satisfaction Status** | ☐ Satisfied ☐ Partially Satisfied ☐ Unsatisfied |
| **Notes** | |

---

### IR-06: Geopolitical Context

| Field | Value |
|-------|-------|
| **Requirement ID** | IR-06 |
| **Question** | Are there geopolitical developments (conflicts, sanctions, elections, diplomatic tensions) that may increase the threat of state-sponsored cyber operations against our sector or geography? |
| **Priority** | Important |
| **Source(s)** | Government advisories, geopolitical analysis, NCSC/CISA threat briefings |
| **Collection Source(s)** | NCSC alerts, CISA shields-up advisories, ISAC threat briefings |
| **Responsible Analyst** | [Name] |
| **Review Frequency** | Monthly |
| **Satisfaction Status** | ☐ Satisfied ☐ Partially Satisfied ☐ Unsatisfied |
| **Notes** | |

---

### IR-07: Supply Chain Threats

| Field | Value |
|-------|-------|
| **Requirement ID** | IR-07 |
| **Question** | Are there known supply chain compromises or vendor breaches affecting products or services used in our OT environment? |
| **Priority** | Important |
| **Source(s)** | Vendor notifications, CISA advisories, ISAC intelligence |
| **Collection Source(s)** | Vendor communication channels, sector ISAC, CISA alerts |
| **Responsible Analyst** | [Name] |
| **Review Frequency** | Monthly |
| **Satisfaction Status** | ☐ Satisfied ☐ Partially Satisfied ☐ Unsatisfied |
| **Notes** | |

---

### IR-08: Internal Intelligence — SOC Operations

| Field | Value |
|-------|-------|
| **Requirement ID** | IR-08 |
| **Question** | What patterns, indicators, and lessons are emerging from our own SOC investigations, hunting operations, and false positive analysis? |
| **Priority** | Important |
| **Source(s)** | SOC investigation logs, hunt reports, false positive documentation |
| **Collection Source(s)** | Internal — Sentinel incidents, hunt report database |
| **Responsible Analyst** | [Name] |
| **Review Frequency** | Monthly |
| **Satisfaction Status** | ☐ Satisfied ☐ Partially Satisfied ☐ Unsatisfied |
| **Notes** | |

---

## CUSTOM REQUIREMENTS

### IR-09: [Custom Requirement Title]

| Field | Value |
|-------|-------|
| **Requirement ID** | IR-09 |
| **Question** | [Your specific intelligence question] |
| **Priority** | ☐ Critical ☐ Important ☐ Routine |
| **Source(s)** | |
| **Collection Source(s)** | |
| **Responsible Analyst** | |
| **Review Frequency** | |
| **Satisfaction Status** | ☐ Satisfied ☐ Partially Satisfied ☐ Unsatisfied |
| **Notes** | |

---

## REVIEW LOG

| Date | Reviewer | Changes Made | Requirements Added/Removed |
|------|----------|-------------|---------------------------|
| | | | |
| | | | |
