# Collection Management Framework Worksheet
# ================================================================
# Description: Mapping worksheet connecting intelligence
#   requirements to collection sources with coverage gap tracking.
#   Includes pre-populated ICS-relevant intelligence sources.
#
# Usage: Maintain alongside the Intelligence Requirements Template.
#   Review monthly to ensure all requirements have adequate
#   collection sources assigned and monitored.
# ================================================================

## COLLECTION SOURCE INVENTORY

### External Sources — Government and Regulatory

| Source | URL / Access | Type | Cost | Relevant Requirements | Monitoring Owner | Frequency |
|--------|-------------|------|------|----------------------|-----------------|-----------|
| CISA ICS-CERT Advisories | https://www.cisa.gov/topics/industrial-control-systems | Advisory | Free | IR-01, IR-02, IR-04, IR-05 | | Daily |
| CISA Known Exploited Vulnerabilities (KEV) | https://www.cisa.gov/known-exploited-vulnerabilities-catalog | Catalogue | Free | IR-04 | | Daily |
| CISA Shields Up Alerts | https://www.cisa.gov/shields-up | Alert | Free | IR-06 | | As published |
| NCSC Advisories (UK) | https://www.ncsc.gov.uk/section/keep-up-to-date/threat-reports | Advisory | Free | IR-01, IR-06 | | Weekly |
| NCSC CiSP | https://www.ncsc.gov.uk/section/keep-up-to-date/cisp | Sharing platform | Free (registration) | IR-01, IR-02, IR-06 | | Daily |
| ENISA Threat Landscape | https://www.enisa.europa.eu/topics/cyber-threats/threats-and-trends | Report | Free | IR-01, IR-06 | | Annual + ad hoc |
| NVD / CVE Database | https://nvd.nist.gov/ | Vulnerability DB | Free | IR-05 | | Daily |
| MITRE ATT&CK for ICS | https://attack.mitre.org/matrices/ics/ | Framework | Free | IR-01, IR-03 | | Quarterly |

### External Sources — Sector ISACs

| Source | URL / Access | Type | Cost | Relevant Requirements | Monitoring Owner | Frequency |
|--------|-------------|------|------|----------------------|-----------------|-----------|
| E-ISAC (Electricity) | https://www.eisac.com | ISAC | Membership | IR-01, IR-02, IR-07 | | Daily |
| WaterISAC | https://www.waterisac.org | ISAC | Membership | IR-01, IR-02, IR-07 | | Daily |
| ONG-ISAC (Oil & Natural Gas) | https://www.ongisac.org | ISAC | Membership | IR-01, IR-02, IR-07 | | Daily |
| MFG-ISAC (Manufacturing) | Contact via NCI | ISAC | Membership | IR-01, IR-02, IR-07 | | Daily |
| [Your Sector ISAC] | | ISAC | | | | |

### External Sources — Vendor Threat Intelligence

| Source | URL / Access | Type | Cost | Relevant Requirements | Monitoring Owner | Frequency |
|--------|-------------|------|------|----------------------|-----------------|-----------|
| Dragos WorldView / OT-CERT | https://www.dragos.com/threat-intelligence/ | Subscription | Paid / Free tier | IR-01, IR-02, IR-04 | | Weekly |
| Microsoft Threat Intelligence | https://www.microsoft.com/security/blog/topic/threat-intelligence/ | Blog / Defender TI | Included with M365 E5 | IR-01, IR-02 | | Weekly |
| Mandiant Threat Intelligence | https://www.mandiant.com/advantage/threat-intelligence | Subscription | Paid | IR-01, IR-02 | | Weekly |
| ESET Research | https://www.welivesecurity.com/en/eset-research/ | Blog | Free | IR-01, IR-02 | | Weekly |

### External Sources — Vendor Security Advisories

| Vendor | Advisory Portal URL | Products in Environment | Monitoring Owner | Frequency |
|--------|-------------------|----------------------|-----------------|-----------|
| [e.g., Siemens] | https://cert-portal.siemens.com/ | [List specific products] | | Monthly (Patch Tuesday) |
| [e.g., Schneider Electric] | https://www.se.com/ww/en/work/support/cybersecurity/security-notifications.jsp | [List specific products] | | Monthly |
| [e.g., Rockwell Automation] | https://www.rockwellautomation.com/en-us/trust-center/security-advisories.html | [List specific products] | | Monthly |
| [e.g., ABB] | https://search.abb.com/library/Download.aspx?DocumentID=9AKK108467A0271 | [List specific products] | | Monthly |
| [Add your OT vendors] | | | | |

### Internal Sources

| Source | Access Method | Type | Relevant Requirements | Monitoring Owner | Frequency |
|--------|-------------|------|----------------------|-----------------|-----------|
| SOC Investigation Logs | Sentinel Incidents | Internal | IR-03, IR-08 | | Continuous |
| Hunt Reports | [Repository location] | Internal | IR-03, IR-08 | | Per hunt |
| False Positive Analysis | Sentinel Workbook | Internal | IR-08 | | Weekly |
| OT Engineering Feedback | Weekly IT/OT sync | Internal | IR-08 | | Weekly |
| Incident After-Action Reviews | [Repository location] | Internal | IR-08 | | Per incident |

---

## COLLECTION COVERAGE MATRIX

Map each intelligence requirement to its collection sources and assess coverage:

| Requirement ID | Requirement Summary | Primary Source | Secondary Source(s) | Coverage Assessment | Gap Identified |
|---------------|--------------------|----|----|----|-----|
| IR-01 | Active threat actors | CISA ICS-CERT | Dragos, ISAC, Microsoft TI | ☐ Full ☐ Partial ☐ Gap | |
| IR-02 | Emerging capabilities | Dragos/Mandiant | CISA, ESET, academic | ☐ Full ☐ Partial ☐ Gap | |
| IR-03 | Detection coverage gaps | Internal (Sentinel) | MITRE ATT&CK mapping | ☐ Full ☐ Partial ☐ Gap | |
| IR-04 | Active exploitation | CISA KEV | Vendor advisories, Exploit-DB | ☐ Full ☐ Partial ☐ Gap | |
| IR-05 | Product-specific vulns | Vendor portals | CISA ICS-CERT, NVD | ☐ Full ☐ Partial ☐ Gap | |
| IR-06 | Geopolitical context | NCSC/CISA alerts | ISAC briefings | ☐ Full ☐ Partial ☐ Gap | |
| IR-07 | Supply chain threats | Vendor notifications | CISA, ISAC | ☐ Full ☐ Partial ☐ Gap | |
| IR-08 | Internal intelligence | SOC logs, hunt reports | Engineering feedback | ☐ Full ☐ Partial ☐ Gap | |

---

## COLLECTION GAP ANALYSIS

| Gap Description | Affected Requirements | Proposed Source | Action Required | Owner | Target Date |
|----------------|----------------------|-----------------|----------------|-------|-------------|
| | | | | | |
| | | | | | |

---

## REVIEW LOG

| Date | Reviewer | Changes Made |
|------|----------|-------------|
| | | |
