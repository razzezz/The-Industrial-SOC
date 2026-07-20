# Asset Visibility Maturity Self-Assessment

## Purpose

This checklist enables SOC teams to evaluate their current OT asset visibility maturity level and identify the specific actions needed to progress to the next level. Complete this assessment quarterly and track progress over time.

---

## How to Use

For each criterion, mark it as **Met**, **Partial**, or **Not Met**. Your maturity level is the highest level where **all** criteria are Met. Criteria marked Partial indicate the areas to focus on for progression.

---

## Level 1 — Reactive

*Baseline: Some knowledge of OT assets exists, but it is not structured, current, or integrated with security operations.*

| # | Criterion | Status | Evidence / Notes |
|---|-----------|--------|-----------------|
| 1.1 | A document or spreadsheet exists that lists at least some OT assets | ☐ Met ☐ Partial ☐ Not Met | |
| 1.2 | At least one person on the security team can name the most critical OT process | ☐ Met ☐ Partial ☐ Not Met | |
| 1.3 | The SOC is aware that OT assets exist on the network | ☐ Met ☐ Partial ☐ Not Met | |
| 1.4 | There is some form of network diagram (even hand-drawn) for the OT environment | ☐ Met ☐ Partial ☐ Not Met | |

**If all Level 1 criteria are Met:** You are at Level 1. Proceed to Level 2 assessment.

**To reach Level 1:** Conduct the first "Known Knowns" interview with OT engineering (Chapter 6, Practical Step 1).

---

## Level 2 — Managed

*The OT asset register is built from multiple sources, crown jewels are identified, and the register is integrated with the SIEM.*

| # | Criterion | Status | Evidence / Notes |
|---|-----------|--------|-----------------|
| 2.1 | An OT asset register exists with structured fields (not just a name list) | ☐ Met ☐ Partial ☐ Not Met | |
| 2.2 | The register includes data from IT tools (AD, DHCP, network logs) | ☐ Met ☐ Partial ☐ Not Met | |
| 2.3 | The register includes data from OT engineering interviews | ☐ Met ☐ Partial ☐ Not Met | |
| 2.4 | Crown jewel analysis has been conducted with OT engineering input | ☐ Met ☐ Partial ☐ Not Met | |
| 2.5 | Crown jewel tiers are assigned to assets in the register | ☐ Met ☐ Partial ☐ Not Met | |
| 2.6 | The register is imported into Sentinel as the OT_AssetRegister watchlist | ☐ Met ☐ Partial ☐ Not Met | |
| 2.7 | At least one detection rule references the OT_AssetRegister watchlist for enrichment | ☐ Met ☐ Partial ☐ Not Met | |
| 2.8 | The register is reviewed and updated at least quarterly | ☐ Met ☐ Partial ☐ Not Met | |
| 2.9 | The OT_MaintenanceWindows watchlist is populated and maintained | ☐ Met ☐ Partial ☐ Not Met | |
| 2.10 | At least one attack path to a crown jewel has been documented | ☐ Met ☐ Partial ☐ Not Met | |

**If all Level 2 criteria are Met:** You are at Level 2. This is the target state after implementing Chapter 6.

**To reach Level 2:** Complete Practical Steps 1–6 from Chapter 6.

---

## Level 3 — Defined

*Passive network monitoring supplements the register. Most assets are validated through observation. New devices are detected automatically.*

| # | Criterion | Status | Evidence / Notes |
|---|-----------|--------|-----------------|
| 3.1 | Passive network monitoring (Zeek/Suricata) is deployed at the IDMZ boundary | ☐ Met ☐ Partial ☐ Not Met | |
| 3.2 | Passive monitoring is deployed at least one additional OT network boundary | ☐ Met ☐ Partial ☐ Not Met | |
| 3.3 | ≥80% of registered assets have been validated by passive network observation | ☐ Met ☐ Partial ☐ Not Met | |
| 3.4 | UC-ICS-013 (New OT Device Detection) is deployed and producing alerts | ☐ Met ☐ Partial ☐ Not Met | |
| 3.5 | New device alerts are reviewed and resolved within 48 hours | ☐ Met ☐ Partial ☐ Not Met | |
| 3.6 | Communication baselines are being developed for Tier 1 and Tier 2 assets | ☐ Met ☐ Partial ☐ Not Met | |
| 3.7 | The register includes protocol and communication partner data from passive observation | ☐ Met ☐ Partial ☐ Not Met | |
| 3.8 | ASIM parsers for OT data sources are deployed and normalising data | ☐ Met ☐ Partial ☐ Not Met | |

**If all Level 3 criteria are Met:** You are at Level 3. Chapter 7 develops capabilities to this level.

**To reach Level 3:** Deploy passive monitoring per Chapter 7 sensor placement guidance.

---

## Level 4 — Proactive

*Continuous monitoring covers all crown jewels. Baselines are validated. Vulnerability intelligence is integrated.*

| # | Criterion | Status | Evidence / Notes |
|---|-----------|--------|-----------------|
| 4.1 | 100% of Tier 1 and Tier 2 crown jewel assets have passive monitoring coverage | ☐ Met ☐ Partial ☐ Not Met | |
| 4.2 | Validated communication baselines exist for all Tier 1 and Tier 2 assets | ☐ Met ☐ Partial ☐ Not Met | |
| 4.3 | Deviations from baselines generate alerts that are triaged by the SOC | ☐ Met ☐ Partial ☐ Not Met | |
| 4.4 | Known CVEs are mapped to assets in the register based on firmware/OS version | ☐ Met ☐ Partial ☐ Not Met | |
| 4.5 | CISA KEV entries affecting registered assets trigger immediate assessment | ☐ Met ☐ Partial ☐ Not Met | |
| 4.6 | Detection coverage gaps on Tier 1/Tier 2 assets are tracked as a metric | ☐ Met ☐ Partial ☐ Not Met | |
| 4.7 | The register is updated in near-real-time through passive discovery correlation | ☐ Met ☐ Partial ☐ Not Met | |
| 4.8 | ATT&CK for ICS technique coverage is mapped per crown jewel asset | ☐ Met ☐ Partial ☐ Not Met | |

**If all Level 4 criteria are Met:** You are at Level 4. Chapters 8–9 develop capabilities to this level.

---

## Level 5 — Optimised

*Full visibility, automated tracking, ML-driven baselines, and continuous improvement.*

| # | Criterion | Status | Evidence / Notes |
|---|-----------|--------|-----------------|
| 5.1 | Passive monitoring covers all OT network segments (not just boundaries) | ☐ Met ☐ Partial ☐ Not Met | |
| 5.2 | Automated asset tracking detects additions, removals, and changes | ☐ Met ☐ Partial ☐ Not Met | |
| 5.3 | ML-based network baselines identify behavioural deviations | ☐ Met ☐ Partial ☐ Not Met | |
| 5.4 | Vulnerability correlation is automated (CVE to firmware version matching) | ☐ Met ☐ Partial ☐ Not Met | |
| 5.5 | Asset risk scoring integrates threat intelligence, vulnerability data, and crown jewel tier | ☐ Met ☐ Partial ☐ Not Met | |
| 5.6 | Asset inventory metrics drive procurement and architecture decisions | ☐ Met ☐ Partial ☐ Not Met | |
| 5.7 | Regular tabletop exercises validate that crown jewel classifications are current | ☐ Met ☐ Partial ☐ Not Met | |

**If all Level 5 criteria are Met:** You are at Level 5. Chapters 8–10 develop the advanced capabilities at this level.

---

## Assessment Summary

| Field | Value |
|-------|-------|
| Assessment Date | |
| Assessor(s) | |
| Current Maturity Level | |
| Target Maturity Level (12 months) | |
| Top 3 Gaps to Address | 1. |
| | 2. |
| | 3. |
| Next Review Date | |
