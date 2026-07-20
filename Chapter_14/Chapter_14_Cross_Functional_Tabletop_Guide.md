# Cross-Functional Tabletop Exercise Guide
# ================================================================
# Description: Guide for conducting joint IT/OT tabletop exercises
#   using the scenarios from the Chapter 11 Tabletop Scenario
#   Library. Covers planning, facilitation, evaluation, and
#   after-action documentation.
#
# Usage: Use this guide to plan and execute quarterly cross-
#   functional tabletop exercises. Minimum cadence: one per quarter,
#   with at least two per year involving executive leadership.
# ================================================================

---

## Purpose

Cross-functional tabletop exercises test the coordination between IT Security, OT Engineering, and Operations during simulated cyber incidents. They reveal gaps in communication, decision-making, and playbook coverage that can only be discovered through practice — before a real incident forces discovery under pressure.

---

## Exercise Planning (4–6 Weeks Before)

### Step 1: Select the Scenario

Choose a scenario from the Chapter 11 Tabletop Scenario Library or develop a custom scenario based on current threat intelligence. Rotate scenarios across categories:

| Exercise # | Recommended Scenario Category | Chapter 11 Reference |
|-----------|------------------------------|---------------------|
| Q1 | Ransomware at IT/OT Boundary | Scenario 1 |
| Q2 | ICS Protocol Attack | Scenario 2 or 3 |
| Q3 | Insider Threat / Physical-Cyber | Scenario 4 |
| Q4 | Supply Chain / Advanced Persistent Threat | Scenario 5 or 6 |

### Step 2: Define Exercise Scope

| Element | Detail |
|---------|--------|
| **Exercise Date/Time** | [Schedule during business hours; allow 2–3 hours] |
| **Scenario** | [Selected scenario name and reference] |
| **Scope** | ☐ Discussion-based only ☐ Discussion + simulated notifications ☐ Full walkthrough with tooling |
| **Classification** | ☐ Operational (SOC + Engineering) ☐ Strategic (includes leadership) |
| **Facility/Site** | [Which operational site is the scenario based on?] |

### Step 3: Confirm Participants

| Role | Name | Organisation | Required / Optional |
|------|------|-------------|-------------------|
| **Facilitator** | | | Required |
| **Scribe / Note-taker** | | | Required |
| SOC Analyst / Shift Lead | | IT Security | Required |
| Detection Engineer | | IT Security | Required |
| OT Security SME | | IT Security / Engineering | Required |
| Engineering Lead | | OT Engineering | Required |
| Control Room Operator | | Operations | Required |
| Plant / Site Manager | | Operations | Optional (Required for strategic exercises) |
| CISO | | Executive | Optional (Required for strategic exercises) |
| COO / VP Operations | | Executive | Optional (Required for strategic exercises) |
| Communications / PR | | Corporate | Optional |
| Legal / Compliance | | Corporate | Optional |

### Step 4: Prepare Exercise Materials

- [ ] Scenario briefing document (2 pages maximum — use Chapter 11 scenario guides)
- [ ] Inject schedule (timed reveals of new information during the exercise)
- [ ] Reference materials: relevant IR playbook, CSIRT charter, communication templates, escalation paths
- [ ] Evaluation criteria checklist (below)
- [ ] Facility diagrams and network architecture for the scenario site

---

## Exercise Execution

### Opening (10 minutes)

1. Welcome participants; state exercise objectives
2. Establish ground rules:
   - There are no wrong answers — the purpose is to identify gaps, not to test individuals
   - Participants should respond as they would in a real incident
   - "Time compression" — the facilitator will compress timelines for discussion
   - Chatham House Rule if external participants are present
3. Distribute scenario briefing

### Inject Delivery (90–120 minutes)

Deliver scenario injects at planned intervals. After each inject, facilitate discussion using these prompt questions:

**For SOC participants:**
- What is your initial triage assessment?
- What additional data do you need? Where would you find it?
- Does this trigger an escalation? To whom?
- What detection rule would/should have caught this?

**For OT Engineering participants:**
- What is the operational impact of this scenario?
- Is the affected system a crown jewel? What process does it support?
- What is the fail-safe position for this system?
- Can the process continue safely with this system compromised/isolated?

**For Operations / Leadership participants:**
- At what point do you notify the regulator?
- At what point do you issue a public statement?
- What is the business continuity plan if the process must shut down?
- What decision authority does the SOC have vs. engineering vs. operations?

### Debrief (30–45 minutes)

Conduct an immediate hot debrief while observations are fresh:

1. **What went well?** — Identify processes that worked as designed
2. **What gaps did we discover?** — Communication, decision authority, technical capability, playbook coverage
3. **What would we do differently?** — Specific improvements
4. **Key surprise?** — What did participants learn that they did not know before?

---

## Evaluation Criteria

Score each dimension during the exercise:

| Dimension | Rating (1–5) | Observations |
|-----------|-------------|-------------|
| **Detection**: Was the initial alert identified and triaged appropriately? | | |
| **Escalation**: Was the correct escalation path followed? Was engineering engaged at the right time? | | |
| **Communication**: Were notifications timely, clear, and directed to the right audience? | | |
| **Decision Authority**: Was it clear who had authority to make containment decisions? Was engineering's safety veto respected? | | |
| **Playbook Coverage**: Did the existing IR playbook cover the scenario adequately? | | |
| **Cross-Functional Coordination**: Did IT Security and OT Engineering work effectively together? | | |
| **Operational Awareness**: Did participants understand the physical/operational impact of the scenario? | | |
| **Recovery Planning**: Was a recovery approach discussed that accounted for both cyber and operational requirements? | | |

**Rating Scale**: 1 = Not addressed / major gap, 2 = Partially addressed / significant issues, 3 = Adequate with improvements needed, 4 = Well handled with minor gaps, 5 = Excellent / no gaps identified

---

## After-Action Report

Complete within one week of the exercise:

| Section | Content |
|---------|---------|
| **Exercise Summary** | Scenario used, date, participants, duration |
| **Objectives** | What the exercise was designed to test |
| **Findings — Strengths** | What worked well (minimum 3 items) |
| **Findings — Gaps** | Gaps identified with severity (Critical / High / Medium / Low) |
| **Recommended Actions** | Specific remediation actions with owners and target dates |
| **Playbook Updates Required** | Specific playbook changes identified |
| **Detection Rule Gaps** | Detection rules that need development or tuning |
| **Training Gaps** | Knowledge or skill gaps identified in participants |
| **Next Exercise** | Recommended scenario and date for next exercise |

---

## Remediation Tracking

| # | Finding | Severity | Action Required | Owner | Target Date | Status |
|---|---------|----------|----------------|-------|-------------|--------|
| 1 | | ☐ Critical ☐ High ☐ Medium ☐ Low | | | | ☐ Open ☐ In Progress ☐ Complete |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |

---

## Exercise Calendar

| Quarter | Date | Scenario | Classification | Participants | Status |
|---------|------|----------|---------------|-------------|--------|
| Q1 | | | ☐ Operational ☐ Strategic | | ☐ Planned ☐ Complete |
| Q2 | | | ☐ Operational ☐ Strategic | | ☐ Planned ☐ Complete |
| Q3 | | | ☐ Operational ☐ Strategic | | ☐ Planned ☐ Complete |
| Q4 | | | ☐ Operational ☐ Strategic | | ☐ Planned ☐ Complete |
