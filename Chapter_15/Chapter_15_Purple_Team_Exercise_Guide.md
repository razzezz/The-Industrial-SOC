# OT Purple Team Exercise Planning Guide
# ================================================================
# Description: Comprehensive guide for planning and executing
#   purple team exercises in OT environments. Covers scoping,
#   safety constraints, scenario design, execution protocol,
#   debrief, and findings documentation.
#
# Usage: Use this guide to plan each purple team exercise.
#   Complete the Exercise Planning Worksheet before execution.
#   Use the Exercise Report Template to document findings and
#   feed into the continuous improvement cycle.
# ================================================================

## Part 1: Purple Team Principles for OT

### Why Purple Team Over Red Team in OT

Purple team exercises are collaborative: the offensive team executes a specific TTP and the defensive team attempts to detect it in real time. If detection fails, the teams work together to understand why. This model is strongly preferred in OT environments for three reasons:

1. **Safety.** Unannounced adversarial activity near process control systems carries risk that does not exist in enterprise IT. Purple team eliminates this risk through transparency and coordination.

2. **Improvement velocity.** Every TTP is discussed, analysed, and addressed during the exercise. Purple team produces more improvement per exercise hour than red team.

3. **Collaboration.** Purple team exercises build relationships between offensive testers, SOC analysts, and OT engineering observers — the cross-functional collaboration that is essential for OT defence.

### The Safety Boundary: Non-Negotiable

No adversary simulation activity may directly interact with process control devices at Purdue Levels 0–2 without explicit engineering approval. Even with approval, the risk tolerance is far lower than in IT. The safety boundary is absolute, not a guideline.

---

## Part 2: Exercise Scoping

### Zone Classification

Before every exercise, classify the environment into three zones:

| Zone | Purdue Levels | Activity Permitted | Approval Required |
|------|---------------|-------------------|-------------------|
| **Safe Zone** | Levels 4–5 (Enterprise IT), Level 3.5 (IDMZ) | Active adversary simulation: credential attacks, lateral movement, tool deployment, C2 establishment, data staging | SOC Lead + Exercise Director |
| **Restricted Zone** | Level 3 (Site Operations: SCADA servers, historian, engineering workstations) | Discovery and collection only: scanning, protocol enumeration, data access. NO execution or manipulation. | SOC Lead + OT Engineering Lead + Plant Manager. Engineering present during execution. |
| **Prohibited Zone** | Levels 0–2 (PLCs, RTUs, SIS, I/O modules) | NO direct interaction. Test detection through simulated telemetry (replayed PCAPs) or paper-based tabletop only. | N/A — activity is not permitted regardless of approval. |

### Scoping Checklist

Before proceeding to exercise design, confirm all of the following:

- [ ] Zone classification completed and documented
- [ ] Restricted Zone activities explicitly listed and approved by OT Engineering
- [ ] Prohibited Zone boundary communicated to all exercise participants
- [ ] Safety assessment completed by OT Engineering for any Restricted Zone activities
- [ ] Rollback procedures documented for all Restricted Zone activities
- [ ] Emergency stop procedure defined (exercise can be halted at any time by any participant)
- [ ] Maintenance window confirmed (exercise activities in Restricted Zone during maintenance only)
- [ ] Operations team notified of exercise timing and potential observable effects
- [ ] Backup engineering access confirmed (in case primary access is affected)

---

## Part 3: Exercise Planning Worksheet

Complete this worksheet for each purple team exercise.

### Exercise Information

| Field | Value |
|-------|-------|
| **Exercise Name** | [e.g., "Volt Typhoon Boundary Traversal"] |
| **Exercise Date(s)** | [Date(s)] |
| **Exercise Director** | [Name] |
| **Red Team Lead** | [Name] |
| **Blue Team Lead** | [Name] |
| **OT Engineering Observer** | [Name — REQUIRED] |
| **Executive Sponsor** | [Name] |
| **Scope** | [Brief description] |

### Objective

| # | Objective | Measure of Success |
|---|-----------|-------------------|
| 1 | | |
| 2 | | |
| 3 | | |

### Threat Scenario

| Field | Value |
|-------|-------|
| **Simulated Threat Actor** | [Microsoft naming — e.g., Volt Typhoon (VOLTZITE)] |
| **Reference Advisory/Report** | [e.g., CISA AA24-038A] |
| **ATT&CK for ICS Techniques** | [List of technique IDs] |
| **ICS Kill Chain Stages Covered** | [Stage 1 / Boundary Traversal / Stage 2] |

### Exercise Phases

#### Phase 1: [Name]

| Field | Value |
|-------|-------|
| **Zone** | [Safe / Restricted] |
| **TTPs Executed** | [ATT&CK technique IDs and descriptions] |
| **Expected Blue Team Detection** | [What should the SOC see?] |
| **Detection Rules Being Tested** | [UC-ICS-XXX references] |
| **Tooling Used (Red)** | [Tools and techniques] |
| **Tooling Used (Blue)** | [SIEM, EDR, NDR — what should detect this?] |
| **Safety Considerations** | [Any OT impact risk, mitigations] |
| **Success Criteria** | [What constitutes detection success?] |

#### Phase 2: [Name]

| Field | Value |
|-------|-------|
| **Zone** | [Safe / Restricted] |
| **TTPs Executed** | |
| **Expected Blue Team Detection** | |
| **Detection Rules Being Tested** | |
| **Tooling Used (Red)** | |
| **Tooling Used (Blue)** | |
| **Safety Considerations** | |
| **Success Criteria** | |

#### Phase 3: [Name]

| Field | Value |
|-------|-------|
| **Zone** | [Safe / Restricted] |
| **TTPs Executed** | |
| **Expected Blue Team Detection** | |
| **Detection Rules Being Tested** | |
| **Tooling Used (Red)** | |
| **Tooling Used (Blue)** | |
| **Safety Considerations** | |
| **Success Criteria** | |

#### Phase 4: [Name — Simulated OT Activity]

| Field | Value |
|-------|-------|
| **Zone** | Prohibited — simulated telemetry only |
| **TTPs Simulated** | |
| **Telemetry Method** | [PCAP replay / synthetic log injection / paper-based] |
| **Expected Blue Team Detection** | |
| **Detection Rules Being Tested** | |
| **Safety Considerations** | No live interaction with control devices |
| **Success Criteria** | |

### Assumptions and Exercise Constraints

| # | Assumption / Constraint |
|---|-------------------------|
| 1 | [e.g., "Red team starts with valid VPN credentials — initial access is assumed"] |
| 2 | [e.g., "No actual malware deployed — simulation uses benign tools that mimic TTPs"] |
| 3 | |

### Communications Plan

| Event | Channel | Recipients |
|-------|---------|------------|
| Exercise start | | |
| Phase transitions | | |
| Emergency stop | | |
| Exercise end | | |
| Debrief scheduling | | |

---

## Part 4: Execution Protocol

### Before Execution

1. All participants briefed on scope, zones, safety constraints, and emergency stop procedure
2. OT Engineering confirms current operational state and approves exercise timing
3. Blue Team confirms monitoring tools are operational and logging
4. Red Team confirms tools are staged and exercise infrastructure is ready
5. Exercise Director confirms go/no-go with all stakeholders

### During Execution

1. Exercise Director maintains oversight of all phases
2. Red Team executes TTPs according to the phase plan
3. Blue Team monitors in real time using standard SOC tools and procedures
4. After each phase, **PAUSE** for debrief:
   - Red Team reveals what they did
   - Blue Team reports what they detected (and did not detect)
   - OT Engineering observer comments on operational impact implications
   - Detection gaps documented in real time
5. Emergency stop procedure: **Any participant can halt the exercise at any time** by communicating "EXERCISE STOP" on the designated channel. All Red Team activity ceases immediately.

### After Execution

1. Red Team provides complete log of all actions taken, with timestamps
2. Blue Team provides complete log of all detections, with timestamps
3. Exercise Director schedules debrief within 48 hours
4. All exercise artifacts (logs, screenshots, PCAP captures) preserved

---

## Part 5: Exercise Report Template

### Exercise Summary

| Field | Value |
|-------|-------|
| **Exercise Name** | |
| **Date(s)** | |
| **Duration** | |
| **Scope** | |
| **Simulated Threat Actor** | |
| **Phases Completed** | |

### Results by Phase

#### Phase [#]: [Name]

| TTP | ATT&CK ID | Detected? | Detection Method | Time to Detect | Notes |
|-----|-----------|-----------|-----------------|----------------|-------|
| | | Yes / No / Partial | | | |
| | | Yes / No / Partial | | | |

**Detection Gaps Identified:**

**Root Cause of Missed Detections:**

#### Phase [#]: [Name]

| TTP | ATT&CK ID | Detected? | Detection Method | Time to Detect | Notes |
|-----|-----------|-----------|-----------------|----------------|-------|
| | | Yes / No / Partial | | | |
| | | Yes / No / Partial | | | |

**Detection Gaps Identified:**

**Root Cause of Missed Detections:**

### Overall Results

| Metric | Value |
|--------|-------|
| **Total TTPs Tested** | |
| **TTPs Detected** | |
| **TTPs Partially Detected** | |
| **TTPs Missed** | |
| **Detection Rate** | [%] |
| **Average Time to Detect** | |
| **Fastest Detection** | |
| **Slowest Detection** | |

### OT Engineering Assessment

| Question | Assessment |
|----------|------------|
| Were any exercise activities observed in the operational environment? | |
| Were any process impacts noted during the exercise? | |
| What would the operational impact have been if this were a real attack? | |
| Were the safety constraints adequate? | |
| Recommendations for future exercise scoping? | |

### Findings and Recommendations

| # | Finding | Category | Priority | Recommendation | Owner | Due Date |
|---|---------|----------|----------|----------------|-------|----------|
| 1 | | Detection / Response / Process / Tooling | High / Med / Low | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |

### Integration with Continuous Improvement Cycle

| Finding | Feeds Into | Specific Action |
|---------|-----------|-----------------|
| [Detection gap] | Detection Engineering (Phase 1: Preparation) | [New rule to be developed] |
| [Response delay] | IR Playbook Update (Phase 1: Preparation) | [Playbook step to be added/updated] |
| [Collaboration gap] | Cross-Functional Process (Chapter 14) | [Process improvement] |
| [Tooling gap] | Tooling Review (Chapter 13) | [Tooling investment or configuration] |

---

## Part 6: Pre-Built Exercise Scenarios

### Scenario A: Volt Typhoon Boundary Traversal

**Threat Actor:** Volt Typhoon (VOLTZITE)  
**Reference:** CISA Advisory AA24-038A  
**Focus:** Living-off-the-land techniques, IT/OT boundary traversal  

| Phase | Zone | TTPs | Detection Tests |
|-------|------|------|-----------------|
| 1 — Initial Access | Safe | T1133 (External Remote Services) — compromised VPN credential | Anomalous VPN auth (geographic, temporal) |
| 2 — Discovery and Persistence | Safe | T1018 (Remote System Discovery), T1083 (File Discovery), T1053.005 (Scheduled Tasks) | EDR process telemetry, Sysmon events |
| 3 — Boundary Traversal | Safe/Restricted | Lateral movement to IDMZ, access to historian/jump servers | UC-ICS-003, UC-ICS-009, authentication anomalies |
| 4 — OT Discovery (Simulated) | Prohibited (simulated) | Modbus/DNP3 scanning via PCAP replay | UC-ICS-005, UC-ICS-006, UC-ICS-008 |

### Scenario B: Seashell Blizzard Destructive Attack

**Threat Actor:** Seashell Blizzard (ELECTRUM)  
**Reference:** MITRE ATT&CK Group G0034  
**Focus:** Destructive capability deployment, wiper malware  

| Phase | Zone | TTPs | Detection Tests |
|-------|------|------|-----------------|
| 1 — Spearphishing and Initial Compromise | Safe | T1566.001 (Spearphishing Attachment) — simulated | Email security, EDR detection |
| 2 — Credential Harvesting and Lateral Movement | Safe | T1003 (Credential Dumping), T1021 (Remote Services) | EDR, ITDR, authentication anomalies |
| 3 — Staging in IDMZ | Safe/Restricted | Tool deployment on jump server, data staging | UC-ICS-003, file integrity monitoring, EDR |
| 4 — OT Impact (Simulated) | Prohibited (simulated) | Wiper deployment simulation via synthetic logs | Alert correlation, incident response activation |

### Scenario C: Insider Threat — Credential Abuse

**Threat Actor:** Insider (no external actor)  
**Focus:** Misuse of legitimate credentials, after-hours access  

| Phase | Zone | TTPs | Detection Tests |
|-------|------|------|-----------------|
| 1 — After-Hours VPN Access | Safe | T1078 (Valid Accounts) — access outside business hours | Temporal anomaly detection |
| 2 — Engineering Workstation Access | Restricted | Access to engineering workstation, project file access | UC-ICS-004, authentication to OT assets |
| 3 — Maintenance Window Abuse | Restricted | Activity during non-scheduled maintenance window | OT_MaintenanceWindows watchlist correlation |
| 4 — PLC Logic Download (Simulated) | Prohibited (simulated) | Simulated logic download via synthetic log | UC-ICS-002, process change detection |
