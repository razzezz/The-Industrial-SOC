# OT Cyber Defence Improvement Roadmap Template
# ================================================================
# Description: Planning template for one-year and three-year
#   improvement horizons. Organises actions by maturity transition
#   with milestones, resource requirements, and status tracking.
#
# Usage: Complete based on the Maturity Self-Assessment results.
#   Review and update quarterly at the Quarterly Improvement Review.
#   Focus on one maturity transition at a time — do not attempt
#   to skip levels.
# ================================================================

## Roadmap Information

| Field | Value |
|-------|-------|
| **Organisation** | [Name] |
| **Created Date** | [Date] |
| **Created By** | [Name and role] |
| **Current Overall Maturity** | [Level from self-assessment] |
| **1-Year Target Maturity** | [Target level] |
| **3-Year Target Maturity** | [Target level] |
| **Executive Sponsor** | [Name and title] |
| **Last Reviewed** | [Date] |

---

## One-Year Roadmap

### Current Maturity Transition: Level [ ] → Level [ ]

#### Quarter 1 (Months 1–3)

| # | Action | Domain | Owner | Dependencies | Resources Required | Status | Due Date |
|---|--------|--------|-------|-------------|-------------------|--------|----------|
| 1.1 | | | | | | Not Started | |
| 1.2 | | | | | | Not Started | |
| 1.3 | | | | | | Not Started | |
| 1.4 | | | | | | Not Started | |
| 1.5 | | | | | | Not Started | |

**Q1 Milestone:** [ ]  
**Q1 Success Criteria:** [ ]

#### Quarter 2 (Months 4–6)

| # | Action | Domain | Owner | Dependencies | Resources Required | Status | Due Date |
|---|--------|--------|-------|-------------|-------------------|--------|----------|
| 2.1 | | | | | | Not Started | |
| 2.2 | | | | | | Not Started | |
| 2.3 | | | | | | Not Started | |
| 2.4 | | | | | | Not Started | |
| 2.5 | | | | | | Not Started | |

**Q2 Milestone:** [ ]  
**Q2 Success Criteria:** [ ]

#### Quarter 3 (Months 7–9)

| # | Action | Domain | Owner | Dependencies | Resources Required | Status | Due Date |
|---|--------|--------|-------|-------------|-------------------|--------|----------|
| 3.1 | | | | | | Not Started | |
| 3.2 | | | | | | Not Started | |
| 3.3 | | | | | | Not Started | |
| 3.4 | | | | | | Not Started | |
| 3.5 | | | | | | Not Started | |

**Q3 Milestone:** [ ]  
**Q3 Success Criteria:** [ ]

#### Quarter 4 (Months 10–12)

| # | Action | Domain | Owner | Dependencies | Resources Required | Status | Due Date |
|---|--------|--------|-------|-------------|-------------------|--------|----------|
| 4.1 | | | | | | Not Started | |
| 4.2 | | | | | | Not Started | |
| 4.3 | | | | | | Not Started | |
| 4.4 | | | | | | Not Started | |
| 4.5 | | | | | | Not Started | |

**Q4 Milestone:** [ ]  
**Q4 Success Criteria:** [ ]

**1-Year Review:** [ ]

---

## Three-Year Roadmap (High Level)

### Year 1: Level [ ] → Level [ ]

| Priority | Focus Areas | Key Milestones | Investment Required |
|----------|-------------|----------------|---------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

### Year 2: Level [ ] → Level [ ]

| Priority | Focus Areas | Key Milestones | Investment Required |
|----------|-------------|----------------|---------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

### Year 3: Level [ ] → Level [ ]

| Priority | Focus Areas | Key Milestones | Investment Required |
|----------|-------------|----------------|---------------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

---

## Pre-Built Action Libraries by Maturity Transition

The following action libraries provide a starting point for each maturity transition. Select and adapt actions based on your organisation's specific gaps as identified by the Maturity Self-Assessment.

### Level 1 → Level 2 Actions (6–12 Months)

| # | Action | Domain | Reference |
|---|--------|--------|-----------|
| A | Conduct crown jewel identification exercise with OT Engineering | Asset Visibility | Chapter 6 |
| B | Build initial OT asset inventory and populate OT_AssetRegister watchlist | Asset Visibility | Chapter 6 |
| C | Deploy passive monitoring at IDMZ (Zeek + Suricata on SPAN/TAP) | Detection | Chapter 7 |
| D | Deploy initial detection rules: UC-ICS-001, UC-ICS-003, UC-ICS-004 | Detection | Chapter 7 |
| E | Document 3–5 critical OT IR playbooks | Incident Response | Chapter 11 |
| F | Establish CSIRT roster with IT Security, OT Engineering, Operations | Incident Response | Chapter 11 |
| G | Conduct first tabletop exercise | Incident Response | Chapter 15 |
| H | Hold first cross-functional SOC/OT Engineering meeting | Collaboration | Chapter 14 |
| I | Begin tracking basic OT alert metrics | Metrics | Chapter 15 |

### Level 2 → Level 3 Actions (12–18 Months)

| # | Action | Domain | Reference |
|---|--------|--------|-----------|
| A | Expand monitoring into OT network (Purdue Levels 2–3) | Detection | Chapter 7 |
| B | Deploy EDR on engineering workstations and HMIs (audit mode first) | Detection | Chapter 13 |
| C | Expand detection rule library based on ATT&CK for ICS prioritisation | Detection | Chapter 7 |
| D | Conduct ATT&CK for ICS coverage assessment | Detection | Chapter 7 |
| E | Populate OT_MaintenanceWindows watchlist | Detection | Chapter 7 |
| F | Establish quarterly tabletop exercises | Incident Response | Chapter 15 |
| G | Conduct first functional exercise | Incident Response | Chapter 11 |
| H | Implement After-Action Review process for all OT incidents | Incident Response | Chapter 12 |
| I | Operationalise engineering liaison function | Collaboration | Chapter 14 |
| J | Initiate shadow engineering programme | Collaboration | Chapter 14 |
| K | Begin tracking MTTD, MTTT, OT FP Rate, Crown Jewel Monitoring Coverage | Metrics | Chapter 15 |
| L | Conduct first Quarterly Improvement Review | Metrics | Chapter 15 |

### Level 3 → Level 4 Actions (18–24 Months)

| # | Action | Domain | Reference |
|---|--------|--------|-----------|
| A | Establish structured threat hunting programme (monthly hunts) | Threat Hunting | Chapter 9 |
| B | Stand up CTI function with defined intelligence requirements | Threat Intelligence | Chapter 10 |
| C | Shift to intelligence-driven detection engineering | Detection | Chapter 7, 10 |
| D | Implement IT/OT log correlation for cross-boundary reconstruction | Detection | Chapter 7 |
| E | Extend detection to ICS-specific ATT&CK tactics (TA0106, TA0107, TA0105) | Detection | Chapter 7 |
| F | Conduct first purple team exercise | Exercises | Chapter 15 |
| G | Operationalise intelligence feedback loop from incidents and AARs | Threat Intelligence | Chapter 12 |
| H | Achieve consistent MTTEE within target | Collaboration | Chapter 14 |
| I | Implement full metrics framework (technical, operational, collaboration, business) | Metrics | Chapter 15 |
| J | Establish regular executive reporting | Metrics | Chapter 15 |

### Level 4 → Level 5 Actions (24+ Months)

| # | Action | Domain | Reference |
|---|--------|--------|-----------|
| A | Evaluate and pilot ML-assisted triage with human-in-the-loop | Detection | Chapter 8 |
| B | Explore attack path analysis using graph-based approaches | Threat Intelligence | Chapter 10 |
| C | Establish regular red team exercises (with OT safety constraints) | Exercises | Chapter 15 |
| D | Achieve industry-leading ATT&CK for ICS detection coverage | Detection | Chapter 7 |
| E | Contribute to sector-wide intelligence sharing (ISACs) | Threat Intelligence | Chapter 10 |
| F | Implement predictive threat modelling | Threat Intelligence | Chapter 10 |
| G | Achieve board-level risk reduction reporting | Metrics | Chapter 15 |
| H | Benchmark metrics against sector peers | Metrics | Chapter 15 |

---

## Risk and Dependencies Register

| # | Risk / Dependency | Impact | Likelihood | Mitigation | Owner |
|---|-------------------|--------|------------|------------|-------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

---

## Budget Summary

| Year | Capital (Tooling) | Operational (Staff/Services) | Training | Total |
|------|-------------------|------------------------------|----------|-------|
| Year 1 | | | | |
| Year 2 | | | | |
| Year 3 | | | | |
| **Total** | | | | |

---

## Review Log

| Date | Reviewer | Changes Made | Next Review |
|------|----------|-------------|-------------|
| | | | |
| | | | |
| | | | |
