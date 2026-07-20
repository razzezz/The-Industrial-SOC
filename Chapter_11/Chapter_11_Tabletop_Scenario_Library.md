# OT Incident Response Tabletop Scenario Library
# ================================================================
# Description: Six facilitated tabletop exercise scenarios for
#   cross-functional OT incident response exercises. Each scenario
#   includes setup, injects, decision points, facilitator notes,
#   and scoring criteria.
#
# Usage: Select one scenario per exercise. Invite representatives
#   from all five CSIRT functions. Allow 2–3 hours per exercise.
#   Conduct quarterly at minimum. Rotate scenarios.
#
# Participants: IT Security, OT Engineering, Plant Operations,
#   Legal/Compliance, Executive Leadership
#
# Reference: Chapter 11 — Purpose-Built Incident Response
# ================================================================

---

## Exercise Framework

### Before the Exercise
- Distribute scenario setup (not injects) 48 hours in advance
- Confirm attendance from all CSIRT functions
- Prepare the room: whiteboard, printed Safe/Unsafe Actions matrix,
  CSIRT roster, SOAR containment boundary reference
- Assign facilitator (should not participate in decisions)
- Assign scribe to capture decisions and discussion

### During the Exercise
- Facilitator reads each inject and pauses for discussion
- Each decision point should generate 10–15 minutes of discussion
- Facilitator prompts if discussion stalls: "Who leads this decision?",
  "What's the safety impact?", "What do we tell the regulator?"
- Scribe captures: decisions made, who made them, rationale, time taken

### After the Exercise
- Debrief immediately (30 minutes)
- Identify: What worked? What was unclear? What needs updating?
- Document findings and assign actions
- Update playbooks, roster, or procedures based on findings

---

## Scenario 1: Ransomware at the IT/OT Boundary

**Difficulty:** Introductory — recommended as first exercise
**Duration:** 2 hours
**Primary Focus:** IT/OT coordination, containment decision-making

### Setup
It is 14:30 on a Tuesday. All production lines are running normally. No maintenance windows are active. The facility operates 24/7 with shift changes at 06:00, 14:00, and 22:00.

### Inject 1 (14:30)
EDR (running in detect mode) on Engineering Workstation EW-03 at Purdue Level 3 generates a high-severity alert. Analysis shows a ransomware dropper has been staged but not executed. EW-03 is used daily for PLC programming and has active S7Comm connections to three PLCs at Purdue Level 1.

**Discussion Questions:**
- Who is the first call? What information do you provide?
- Do you isolate EW-03 via EDR immediately? What do you check first?
- What is the status of PLC programming sessions on EW-03?

### Inject 2 (14:45)
While you are assessing EW-03, the ransomware payload executes. EW-03's local files and one mapped network share (containing PLC project files) are encrypted. The PLCs continue running with their current logic — they are not affected, but EW-03 can no longer communicate with them. EDR has captured the full process tree.

**Discussion Questions:**
- What is the operational impact of losing EW-03?
- How long can production continue without engineering workstation access?
- Do you now isolate EW-03 (post-encryption)?
- What is the status of PLC project file backups?

### Inject 3 (15:15)
A second engineering workstation (EW-05) shows the same indicators. The dropper has been staged but not yet executed. Preliminary investigation suggests both workstations were compromised via a phishing email received three days ago. The mapped network share suggests lateral movement.

**Discussion Questions:**
- Do you isolate EW-05 immediately (the dropper hasn't executed yet)?
- Do you isolate the entire engineering VLAN at the network level?
- What is the blast radius assessment? What other systems may be affected?

### Inject 4 (16:00)
Operations confirms production can continue for 48 hours without engineering workstation access. However, if a PLC fault occurs during this period, there is no way to reprogram or troubleshoot the PLCs without engineering workstations. The safety engineer confirms safety systems are independent and unaffected.

**Discussion Questions:**
- Given the 48-hour window, what is your containment and eradication plan?
- Do you proactively rebuild workstations or investigate first?
- What enhanced monitoring do you deploy for the 48-hour period?

### Inject 5 (17:00)
The CISO receives a ransom demand for £500,000. The threat actor claims to have exfiltrated "engineering documentation" before encrypting.

**Discussion Questions:**
- How do you verify the exfiltration claim?
- Under what circumstances, if any, does the organisation consider payment?
- Does this meet the NIS 2 significant incident threshold? What is your reporting timeline?
- What do you communicate to staff, customers, and media?

### Facilitator Scoring Criteria
- [ ] OT SME was contacted before any containment action on EW-03
- [ ] Safety assessment was conducted before containment decisions
- [ ] PLC programming session status was verified before isolation
- [ ] SOAR containment boundary was respected (no automated action below L3.5)
- [ ] Containment decisions were documented with all decision-makers named
- [ ] NIS 2 reporting timeline was correctly identified
- [ ] Backup and recovery options for PLC project files were assessed

---

## Scenario 2: Unauthorised PLC Logic Change

**Difficulty:** Intermediate
**Duration:** 2.5 hours
**Primary Focus:** Process safety, forensic decision-making, regulatory reporting

### Setup
It is 03:15 on a Sunday morning. Minimum staffing. One operator in the control room, one SOC analyst on shift. The facility is a water treatment plant operating continuously.

### Inject 1 (03:15)
Sentinel analytic rule UC-ICS-002 fires: Modbus write command from engineering workstation 10.1.3.50 to PLC 10.1.2.10 outside any maintenance window. The PLC controls a chemical dosing pump for chlorination. The write command changed the dosing setpoint.

**Discussion Questions:**
- What is your immediate action as the on-shift SOC analyst?
- Who do you call at 03:15 on a Sunday? In what order?
- Do you revert the setpoint change immediately or investigate first?

### Inject 2 (03:30)
The on-call process engineer confirms the new setpoint is 3x the normal value. At this level, the chlorine dosing would exceed safe drinking water limits within approximately 4 hours, but the process has built-in safety limits that would trigger an alarm before reaching dangerous levels. The engineer recommends reverting the setpoint and switching to manual dosing control as a precaution.

**Discussion Questions:**
- Who authorises the setpoint revert?
- Do you follow the process engineer's recommendation? Why or why not?
- What evidence do you collect before reverting (knowing that reverting may overwrite forensic evidence)?

### Inject 3 (04:00)
EDR investigation on the engineering workstation shows a remote desktop session from the IDMZ jump host, authenticated with valid credentials belonging to a senior control engineer who is on annual leave. The jump host's EDR shows a credential dumping tool was executed 12 hours earlier (Saturday afternoon).

**Discussion Questions:**
- How far back do you expand the investigation timeline?
- What other systems may the adversary have accessed?
- Do you disable the compromised credentials now?
- How do you contact the engineer on leave?

### Inject 4 (06:00)
The morning investigation reveals the adversary has been in the IT network for three weeks. They accessed network documentation, PLC programming files, and water quality monitoring data. There is no evidence they accessed any other PLC, but you cannot be certain.

**Discussion Questions:**
- Do you validate all PLC logic across the facility against golden images?
- How long will this validation take, and can production continue during it?
- Is this a NIS 2 significant incident? Justify your assessment.
- What intelligence do you share with WaterISAC?

### Facilitator Scoring Criteria
- [ ] SOC analyst correctly escalated despite off-hours
- [ ] Process engineer was consulted before any PLC change
- [ ] Setpoint revert was authorised by engineering, not SOC alone
- [ ] Evidence was considered before making changes to PLC
- [ ] Compromised credentials were addressed promptly
- [ ] Investigation scope expanded to cover 3-week dwell time
- [ ] Regulatory reporting requirements were correctly assessed

---

## Scenario 3: Credential Dumping on Active HMI

**Difficulty:** Intermediate
**Duration:** 2 hours
**Primary Focus:** Balancing security response with operational continuity

[Scenario as described in Chapter 11 main text. Facilitator adds these scoring criteria:]

### Facilitator Scoring Criteria
- [ ] Team did NOT immediately kill the process without assessing HMI impact
- [ ] Batch completion timeline was factored into containment decision
- [ ] Backup HMI activation was planned before primary HMI taken offline
- [ ] Credential remediation was planned but timed to avoid operator lockout
- [ ] Enhanced monitoring was deployed during the wait period
- [ ] Clear trigger criteria were defined for "immediate intervention regardless of batch"

---

## Scenario 4: Safety System Alert

**Difficulty:** Advanced
**Duration:** 2.5 hours
**Primary Focus:** Safety-first response, executive decision-making

[Scenario as described in Chapter 11 main text. Facilitator adds these scoring criteria:]

### Facilitator Scoring Criteria
- [ ] Tier 1 triage rules were applied: immediate escalation, 15-minute target
- [ ] Safety engineer was engaged immediately
- [ ] The team did NOT dismiss the alert despite lack of known malicious indicators
- [ ] Controlled safe state was recommended as precaution
- [ ] Executive decision for production halt was supported with structured briefing
- [ ] Root cause (misconfigured tool) was identified and prevention plan developed

---

## Scenario 5: Volt Typhoon-Style Pre-Positioning

**Difficulty:** Advanced
**Duration:** 3 hours
**Primary Focus:** Living-off-the-land detection, strategic response, intelligence sharing

[Scenario as described in Chapter 11 main text. Facilitator adds these scoring criteria:]

### Facilitator Scoring Criteria
- [ ] Team recognised living-off-the-land challenge (no malware to detect)
- [ ] Temporal analysis (02:00–05:00 pattern) was used as a discriminator
- [ ] Credential revocation was debated (alerting adversary vs. containing access)
- [ ] 3-month dwell time drove comprehensive scope assessment
- [ ] Strategic intelligence assessment was produced (pre-positioning vs. imminent threat)
- [ ] CTI programme was engaged to update threat model

---

## Scenario 6: Supply Chain Compromise via Vendor Remote Access

**Difficulty:** Intermediate–Advanced
**Duration:** 2.5 hours
**Primary Focus:** Third-party risk, vendor management, intelligence value assessment

[Scenario as described in Chapter 11 main text. Facilitator adds these scoring criteria:]

### Facilitator Scoring Criteria
- [ ] Vendor access was suspended promptly
- [ ] Impact of losing vendor emergency support was assessed
- [ ] Intelligence value of exfiltrated data was assessed (DCS configs, process flows)
- [ ] Vendor was contacted and held accountable
- [ ] Supply chain security improvements were identified
- [ ] Information sharing with ISAC was considered

---

## Scenario Rotation Schedule

| Quarter | Scenario | Focus Area |
|---------|----------|-----------|
| Q1 | Scenario 1: Ransomware at IT/OT Boundary | Introductory — build foundations |
| Q2 | Scenario 2: Unauthorised PLC Logic Change | Process safety, regulatory reporting |
| Q3 | Scenario 3 or 6: HMI Compromise or Supply Chain | Operational continuity vs. security |
| Q4 | Scenario 4 or 5: Safety System or APT Pre-positioning | Advanced scenarios, executive engagement |

Repeat annually, increasing complexity with additional injects based on lessons learned from previous exercises.
