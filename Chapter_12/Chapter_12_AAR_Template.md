# After-Action Review (AAR) Template
# ================================================================
# Description: Nine-section AAR template for OT security incidents.
#   Designed to extract maximum learning and drive measurable
#   improvements across all security programme functions.
#
# Usage: Complete within two weeks of incident closure. For Severity 1
#   (Critical) incidents, complete a preliminary AAR within 72 hours
#   and a full AAR within two weeks. Involves the full cross-functional
#   CSIRT plus any additional response contributors.
#
# Chapter Reference: Chapter 12 — Digital Forensics and Lessons Learned
# ================================================================

---

## AAR HEADER

| Field | Value |
|-------|-------|
| **Incident Reference** | |
| **AAR Date** | |
| **AAR Facilitator** | |
| **AAR Type** | [Preliminary / Full] |
| **Incident Severity** | [1-Critical / 2-High / 3-Medium / 4-Low] |
| **Classification** | TLP: [RED / AMBER+STRICT / AMBER / GREEN / CLEAR] |
| **Distribution** | |

### AAR Participants

| Name | Role / Function | CSIRT Role |
|------|----------------|-----------|
| | IT Security | |
| | OT Engineering | |
| | Plant Operations | |
| | Legal / Compliance | |
| | Executive Leadership | |
| | SOC Analyst(s) | |
| | Other | |

---

## SECTION 1 — EXECUTIVE SUMMARY

*Concise overview for leadership. One paragraph maximum. Answers: What happened? When? What was affected? How was it resolved? What are the key findings?*

[Executive summary text]

| Key Metric | Value |
|------------|-------|
| **Incident Duration** | [Detection to closure] |
| **OT Systems Affected** | [Count and highest criticality] |
| **Production Impact** | [None / Hours / Days of downtime] |
| **Safety Impact** | [None / Potential / Confirmed] |
| **Regulatory Reporting Triggered** | [Yes — NIS 2 / NCSC CAF / Other / No] |

---

## SECTION 2 — INCIDENT TIMELINE

*Insert the unified timeline from the Forensic Report (Chapter_12_Forensic_Report_Template.md, Section 3). This is the factual backbone of the AAR — all subsequent sections reference it.*

| Timestamp (UTC) | T+ Offset | Event | Source | Impact |
|------------------|-----------|-------|--------|--------|
| | T+0h00m | [First evidence of adversary activity] | | |
| | | [First SOC alert] | | |
| | | [CSIRT activation] | | |
| | | [Safety assessment complete] | | |
| | | [Containment decision] | | |
| | | [Containment executed] | | |
| | | [Eradication complete] | | |
| | | [Recovery / operational validation] | | |
| | | [Incident closed] | | |

**Timeline Narrative:**

[Prose summary of the incident progression — reference the detailed Forensic Report for full timeline]

---

## SECTION 3 — WHAT WENT WELL

*Honest acknowledgement of successes. Identify practices that should be reinforced and continued.*

**Guidance for facilitator:** Ask each CSIRT function to identify at least one thing that worked well from their perspective. Challenge the team to be specific — "communication was good" is not actionable; "the internal alert template reached Operations within 8 minutes of detection" is.

| # | Area | What Worked | Evidence / Reference |
|---|------|-------------|---------------------|
| 1 | Detection | | |
| 2 | Triage | | |
| 3 | CSIRT Coordination | | |
| 4 | Communication | | |
| 5 | Containment | | |
| 6 | OT Engineering Support | | |
| 7 | Recovery | | |
| 8 | Other | | |

---

## SECTION 4 — WHAT WENT WRONG

*Equally honest assessment of failures and shortcomings. This section requires a blame-free environment — identify systemic failures, not individual fault.*

**Guidance for facilitator:** Frame questions as "What would we do differently?" not "Who made a mistake?" Focus on process failures, not personal failures. If participants are reluctant, the facilitator should lead by identifying a shortcoming from their own function first.

| # | Area | What Failed / Was Insufficient | Impact on Response | Systemic Root Cause |
|---|------|-------------------------------|-------------------|-------------------|
| 1 | Detection | | | |
| 2 | Triage | | | |
| 3 | CSIRT Assembly | | | |
| 4 | Communication | | | |
| 5 | Containment Decision | | | |
| 6 | Tooling / Access | | | |
| 7 | OT Context / Knowledge | | | |
| 8 | Recovery | | | |
| 9 | Other | | | |

---

## SECTION 5 — ROOT CAUSE ANALYSIS

*Move beyond the immediate cause to identify underlying factors. Use the "Five Whys" or Ishikawa (fishbone) analysis.*

### Immediate Cause
[What was the direct, proximate cause of the incident?]

### Contributing Factors

| Factor | Description | Category |
|--------|-------------|----------|
| | | [Technical / Process / People / Environment] |
| | | |
| | | |

### Root Cause(s)
[What underlying systemic issue(s) enabled this incident?]

### Five Whys Analysis (if applicable)

1. **Why** did the incident occur? → [Immediate cause]
2. **Why** did [immediate cause] happen? → [Factor]
3. **Why** did [factor] exist? → [Deeper factor]
4. **Why** did [deeper factor] persist? → [Systemic issue]
5. **Why** did [systemic issue] go unaddressed? → [Root cause]

---

## SECTION 6 — INTELLIGENCE FINDINGS

*IOCs, TTPs, and attribution from the forensic investigation. Structure per the Intrusion Analysis Report Template (Chapter 10).*

### ATT&CK for ICS Techniques Observed

| Tactic | Technique ID | Technique Name | Detected by Existing Rule (Y/N) |
|--------|:------------:|---------------|:-------------------------------:|
| | | | |

### Indicators of Compromise

| Type | Value | Confidence | Shelf Life |
|------|-------|:----------:|:----------:|
| | | | |

*Full IOC inventory: see Forensic Report, Section 7.*

### Attribution Assessment

| Field | Value |
|-------|-------|
| **Attribution Confidence** | [None / Low / Medium / High] |
| **Assessed Threat Actor** | |
| **Campaign Linkage** | |
| **Basis** | |

### Intelligence Shared Externally

| Recipient | Date Shared | TLP | Content Summary |
|-----------|-------------|:---:|-----------------|
| | | | |

---

## SECTION 7 — RECOMMENDATIONS

*Specific, actionable recommendations. Each must have an owner and a due date. Categorised by the feedback function they address.*

### Detection Engineering Recommendations

| # | Recommendation | Evidence Reference | Owner | Due Date | Status |
|---|---------------|-------------------|-------|----------|:------:|
| D-1 | | [Timeline ref] | | | ☐ |
| D-2 | | | | | ☐ |

### Threat Hunting Recommendations

| # | Recommendation | Evidence Reference | Owner | Due Date | Status |
|---|---------------|-------------------|-------|----------|:------:|
| H-1 | | | | | ☐ |

### Architecture Recommendations

| # | Recommendation | Evidence Reference | Owner | Due Date | Status |
|---|---------------|-------------------|-------|----------|:------:|
| A-1 | | | | | ☐ |

### Incident Response Recommendations

| # | Recommendation | Evidence Reference | Owner | Due Date | Status |
|---|---------------|-------------------|-------|----------|:------:|
| IR-1 | | | | | ☐ |

### Asset Management Recommendations

| # | Recommendation | Evidence Reference | Owner | Due Date | Status |
|---|---------------|-------------------|-------|----------|:------:|
| AM-1 | | | | | ☐ |

### Training Recommendations

| # | Recommendation | Evidence Reference | Owner | Due Date | Status |
|---|---------------|-------------------|-------|----------|:------:|
| T-1 | | | | | ☐ |

### External Sharing Recommendations

| # | Recommendation | Evidence Reference | Owner | Due Date | Status |
|---|---------------|-------------------|-------|----------|:------:|
| E-1 | | | | | ☐ |

---

## SECTION 8 — METRICS

*Quantitative measurement of response performance.*

| Metric | Value | Benchmark / Target | Assessment |
|--------|-------|-------------------|:----------:|
| **Time to Detect (TTD)** | [hours:minutes] | | [Met / Missed] |
| **Time to Triage (TTT)** | [hours:minutes] | | |
| **Time to Contain (TTC)** | [hours:minutes] | | |
| **Time to Recover (TTR)** | [hours:minutes] | | |
| **Total Incident Duration** | [hours] | | |
| **CSIRT Assembly Time** | [minutes] | 30 min target | |
| **First Regulatory Notification** | [hours after awareness] | 24h (NIS 2) | |
| **Endpoints Investigated** | [count] | | |
| **IOCs Extracted** | [count] | | |
| **Detection Rules Validated** | [count] | | |
| **Detection Gaps Identified** | [count] | | |

### Operational Impact

| Impact Dimension | Measurement |
|-----------------|-------------|
| **Production Downtime** | [hours / None] |
| **Units / Revenue Lost** | |
| **Safety Incidents** | [count / None] |
| **Environmental Releases** | [Yes / No] |
| **Regulatory Reports Filed** | [count and type] |
| **Insurance Claim Required** | [Yes / No] |

---

## SECTION 9 — FOLLOW-UP ACTIONS TRACKING

*Tracking table for all recommendations. Schedule 30/60/90-day reviews at the time of the AAR.*

| Rec # | Recommendation Summary | Owner | Due Date | 30-Day Review | 60-Day Review | 90-Day Review | Final Status |
|-------|----------------------|-------|----------|:-------------:|:-------------:|:-------------:|:------------:|
| D-1 | | | | ☐ | ☐ | ☐ | |
| D-2 | | | | ☐ | ☐ | ☐ | |
| H-1 | | | | ☐ | ☐ | ☐ | |
| A-1 | | | | ☐ | ☐ | ☐ | |
| IR-1 | | | | ☐ | ☐ | ☐ | |
| AM-1 | | | | ☐ | ☐ | ☐ | |
| T-1 | | | | ☐ | ☐ | ☐ | |
| E-1 | | | | ☐ | ☐ | ☐ | |

### Review Schedule

| Review | Date | Facilitator | Status |
|--------|------|-------------|:------:|
| **30-Day Review** | [Date — calendar-block now] | | ☐ Scheduled |
| **60-Day Review** | [Date — calendar-block now] | | ☐ Scheduled |
| **90-Day Review** | [Date — calendar-block now] | | ☐ Scheduled |

---

## SIGN-OFF

| Role | Name | Signature / Approval | Date |
|------|------|---------------------|------|
| SOC Manager | | | |
| OT Engineering Lead | | | |
| Operations Manager | | | |
| CISO | | | |

---

## APPENDICES

### Appendix A: Full Forensic Report
*Reference: Chapter_12_Forensic_Report_Template.md*

### Appendix B: IOC Extraction Checklist
*Reference: Chapter_12_IOC_Extraction_Checklist.md*

### Appendix C: ISAC Sharing Report
*Reference: Chapter_12_ISAC_Sharing_Template.md (if external sharing was conducted)*

### Appendix D: Regulatory Notifications Filed
*Attach copies of all regulatory notifications submitted.*
