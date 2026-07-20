# Intrusion Analysis Report Template
# ================================================================
# Description: Standardised format for processing threat
#   intelligence reports into structured, actionable data. Used
#   as part of the intelligence operationalisation workflow
#   described in Chapter 10.
#
# Usage: Complete one report for each intelligence report that
#   passes the relevance filter (affects our sector, products,
#   or threat actors). Output drives detection gap analysis,
#   hunting hypotheses, and detection rule development.
# ================================================================

## REPORT METADATA

| Field | Value |
|-------|-------|
| **Analysis Report ID** | IAR-[YYYY]-[NNN] |
| **Date Processed** | [Date] |
| **Analyst** | [Name] |
| **Source Report Title** | [Original report title] |
| **Source Organisation** | [e.g., CISA, Dragos, Microsoft] |
| **Source URL** | [Link to original report] |
| **TLP Designation** | ☐ TLP:CLEAR ☐ TLP:GREEN ☐ TLP:AMBER ☐ TLP:AMBER+STRICT ☐ TLP:RED |
| **Date Published** | [Original report date] |

---

## RELEVANCE ASSESSMENT

| Criterion | Assessment | Notes |
|-----------|-----------|-------|
| Targets our sector? | ☐ Yes ☐ No ☐ Possible | |
| Targets our geography? | ☐ Yes ☐ No ☐ Possible | |
| Affects products in our asset register? | ☐ Yes ☐ No ☐ Unknown | [Specific products:] |
| Involves threat actors relevant to us? | ☐ Yes ☐ No ☐ Unknown | [Actor name:] |
| **Overall Relevance** | ☐ High ☐ Medium ☐ Low ☐ Not Relevant | |

*If "Not Relevant" — log and archive. No further analysis required.*

---

## THREAT ACTOR ASSESSMENT

| Field | Value |
|-------|-------|
| **Threat Actor** | [Microsoft naming — e.g., "Volt Typhoon"] |
| **Dragos Alias** | [e.g., "VOLTZITE"] |
| **Motivation** | ☐ Espionage ☐ Pre-positioning ☐ Disruption ☐ Financial ☐ Ideological ☐ Unknown |
| **Assessed Capability** | ☐ State-sponsored (advanced) ☐ Sophisticated criminal ☐ Opportunistic ☐ Hacktivist |
| **Target Sectors** | |
| **Target Geographies** | |
| **Activity Status** | ☐ Active ☐ Dormant ☐ Historical ☐ Unknown |

---

## TTP EXTRACTION (ATT&CK for ICS)

Extract all TTPs described in the report, mapped to ATT&CK for ICS techniques:

| Kill Chain Stage | ATT&CK Technique | Technique ID | Description from Report | Confidence |
|-----------------|-------------------|-------------|------------------------|------------|
| Initial Access | | | | ☐ High ☐ Medium ☐ Low |
| Execution | | | | ☐ High ☐ Medium ☐ Low |
| Persistence | | | | ☐ High ☐ Medium ☐ Low |
| Credential Access | | | | ☐ High ☐ Medium ☐ Low |
| Lateral Movement | | | | ☐ High ☐ Medium ☐ Low |
| Discovery | | | | ☐ High ☐ Medium ☐ Low |
| Collection | | | | ☐ High ☐ Medium ☐ Low |
| Command and Control | | | | ☐ High ☐ Medium ☐ Low |
| Inhibit Response | | | | ☐ High ☐ Medium ☐ Low |
| Impair Process Control | | | | ☐ High ☐ Medium ☐ Low |
| Impact | | | | ☐ High ☐ Medium ☐ Low |

---

## INDICATORS OF COMPROMISE

| IOC Type | Value | Confidence | Expiry Date | Context |
|----------|-------|-----------|-------------|---------|
| IP Address | | ☐ High ☐ Medium ☐ Low | | |
| Domain | | ☐ High ☐ Medium ☐ Low | | |
| File Hash (SHA256) | | ☐ High ☐ Medium ☐ Low | | |
| File Hash (MD5) | | ☐ High ☐ Medium ☐ Low | | |
| URL | | ☐ High ☐ Medium ☐ Low | | |
| Email Address | | ☐ High ☐ Medium ☐ Low | | |
| User Agent | | ☐ High ☐ Medium ☐ Low | | |
| Other | | ☐ High ☐ Medium ☐ Low | | |

---

## AFFECTED PRODUCTS AND VULNERABILITIES

| Product | Vendor | Firmware/Version | CVE(s) | In Our Asset Register? |
|---------|--------|-----------------|--------|----------------------|
| | | | | ☐ Yes ☐ No ☐ Unknown |
| | | | | ☐ Yes ☐ No ☐ Unknown |

---

## DETECTION COVERAGE ASSESSMENT

For each extracted TTP, assess current detection coverage:

| Technique ID | Technique Name | Current Detection Rule | Coverage | Gap Action |
|-------------|----------------|----------------------|----------|------------|
| | | | ☐ Covered ☐ Partial ☐ Gap | |
| | | | ☐ Covered ☐ Partial ☐ Gap | |
| | | | ☐ Covered ☐ Partial ☐ Gap | |
| | | | ☐ Covered ☐ Partial ☐ Gap | |

---

## RECOMMENDED ACTIONS

| Priority | Action Type | Description | Owner | Target Date | Status |
|----------|-----------|-------------|-------|-------------|--------|
| | ☐ New Detection Rule | | | | ☐ Open ☐ In Progress ☐ Complete |
| | ☐ Hunting Hypothesis | | | | ☐ Open ☐ In Progress ☐ Complete |
| | ☐ IOC Import | | | | ☐ Open ☐ In Progress ☐ Complete |
| | ☐ Architecture Review | | | | ☐ Open ☐ In Progress ☐ Complete |
| | ☐ Vulnerability Assessment | | | | ☐ Open ☐ In Progress ☐ Complete |
| | ☐ ISAC Sharing | | | | ☐ Open ☐ In Progress ☐ Complete |

---

## ANALYST NOTES

[Free-text notes on the report's significance, analyst assessment, and any caveats about the intelligence quality or applicability.]
