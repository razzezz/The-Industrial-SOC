# OT Engineering Security Training Plan

## Purpose

This training plan develops the cybersecurity awareness and collaboration competencies that OT Engineers and Operations staff require to participate effectively in the cross-functional OT security programme. It is designed for professionals who are experts in industrial control systems and process operations but have limited exposure to cybersecurity operations.

The goal is not to make OT engineers into cybersecurity specialists. It is to build enough shared understanding that they can participate meaningfully in triage decisions, provide operational context efficiently during investigations, and recognise when something in their environment warrants a call to the SOC.

---

## Training Tracks

### Track 1: Security Awareness for OT (All OT Engineers — Complete Within 60 Days)

| Module | Learning Objectives | Delivery Method | Duration | Assessment |
|--------|-------------------|-----------------|----------|------------|
| **1.1 — The OT Threat Landscape** | Understand that ICS environments are actively targeted. Know the key threat actors (Volt Typhoon, Seashell Blizzard) and their objectives. Understand the difference between opportunistic and targeted attacks. | Briefing from SOC Lead or CTI analyst | 2 hours | Discussion: articulate why OT is a target and name 2 relevant threat actors |
| **1.2 — How Attacks Reach OT** | Understand the ICS Cyber Kill Chain (Stage 1 IT compromise → Stage 2 OT access). Recognise the common entry vectors: phishing, compromised vendor access, IT/OT boundary traversal. | Classroom session with real-world case studies (Chapter 3) | 2 hours | Walk through a simplified attack scenario and identify the transition from IT to OT |
| **1.3 — What the SOC Sees** | Visit the SOC. Observe how OT network traffic appears in Sentinel. See an OT alert being triaged. Understand what information the SOC has — and what it lacks without engineering context. | Guided SOC visit and observation session | 2 hours | Debrief: describe what information the SOC needs from engineering during an investigation |
| **1.4 — Social Engineering & Physical Security** | Recognise phishing attempts targeting OT environments. Understand risks of USB drives from vendors. Know the policy for vendor remote access. Report suspicious contacts or communications. | Interactive workshop with examples | 1.5 hours | Pass a simulated phishing recognition exercise (≥ 80%) |
| **1.5 — Secure Engineering Practices** | Understand why USB scanning before connection matters. Know the approved methods for transferring files to the OT network. Recognise the risks of unauthorised software on engineering workstations. Follow the change management process for security-relevant changes. | Self-study guide + discussion with OT SME | 1.5 hours | Describe the approved process for 3 common engineering activities (file transfer, firmware update, remote vendor access) |

**Total Track 1:** ~9 hours over 60 days

---

### Track 2: Collaboration Competency (OT Engineers Participating in CSIRT — Complete Within 120 Days)

| Module | Learning Objectives | Delivery Method | Duration | Assessment |
|--------|-------------------|-----------------|----------|------------|
| **2.1 — Incident Response Basics** | Understand the incident response lifecycle. Know the CSIRT structure and the OT engineer's role within it. Understand the containment decision process (safety veto, joint decision authority). | Classroom session (Chapter 11 overview) | 2 hours | Describe the OT engineer's responsibilities during a Severity 2 incident |
| **2.2 — Providing Operational Context** | Learn how to provide structured operational context when the SOC calls: asset function, process dependency, fail-safe position, maintenance status, operational impact of proposed containment. | Role-play exercise with SOC analyst | 2 hours | Successfully provide operational context for 3 simulated SOC escalation calls |
| **2.3 — Understanding Detection Rules** | Review 3–5 OT detection rules in plain language. Understand what triggers them. Recognise when a rule might produce a false positive due to legitimate engineering activity. Provide feedback for rule tuning. | Walkthrough with Detection Engineer | 2 hours | Review a new detection rule and identify at least one potential false positive scenario based on operational knowledge |
| **2.4 — Tabletop Exercise Participation** | Participate in a monthly tabletop exercise. Practice the CSIRT decision process. Provide the engineering perspective on containment scenarios. | Monthly tabletop exercise (first attended as observer, second as participant) | 2 hours (× 2) | Active participation in at least one exercise with constructive contribution to containment decisions |
| **2.5 — Evidence Preservation** | Understand what digital evidence exists in OT systems (PLC programme files, historian data, HMI screenshots, configuration backups). Know the chain of custody requirements. Know what NOT to do when an incident is suspected (do not reboot, do not re-download programmes, do not clear logs). | Classroom session (Chapter 12 overview) | 1.5 hours | List the evidence sources available from 3 common OT asset types and describe the preservation procedure for each |

**Total Track 2:** ~11.5 hours over 120 days (builds on Track 1)

---

### Track 3: Security Awareness for Operations Staff (All Operations — Complete Within 90 Days)

| Module | Learning Objectives | Delivery Method | Duration | Assessment |
|--------|-------------------|-----------------|----------|------------|
| **3.1 — Why Security Matters for Operations** | Understand that cyber attacks can cause production disruption, safety incidents, and environmental damage. Know the real-world examples (Ukraine power grid, Triton/TRISIS, Colonial Pipeline). | Briefing with video/case study materials | 1 hour | Discussion participation |
| **3.2 — Recognising Suspicious Activity** | Know what to look for: unexpected HMI behaviour, unfamiliar login screens, unexpected USB devices, strangers in the control room, unexpected alarms or process changes. Know who to call (SOC hotline, engineering lead). | Interactive workshop | 1 hour | Identify suspicious indicators from 5 provided scenarios |
| **3.3 — Incident Communication** | Understand the Internal Alert template. Know what information Operations must provide during an incident: production status, safety system status, what has changed recently. | Walkthrough of communication templates (Chapter 11) | 1 hour | Complete a simulated Internal Alert response form |
| **3.4 — Security During Maintenance** | Understand why security monitoring changes during maintenance windows. Know the requirement to notify the SOC (via engineering liaison) before maintenance. Understand vendor access procedures. | Discussion with Engineering Liaison | 1 hour | Describe the process for notifying the SOC of upcoming maintenance |

**Total Track 3:** ~4 hours over 90 days

---

## Ongoing Development

| Activity | Audience | Frequency | Purpose |
|----------|----------|-----------|---------|
| **Threat Intelligence Briefing** | OT Engineers, CSIRT members | Quarterly | Update on sector-specific threats, new attack techniques, relevant advisories |
| **Tabletop Exercise Participation** | OT Engineers in CSIRT | Monthly | Maintain readiness and relationship with SOC |
| **Security Awareness Refresher** | All Operations staff | Annually | Reinforce key messages, update with new threats and examples |
| **"Lessons Learned" Briefing** | OT Engineers, Operations | After any significant incident | Share what happened, what was learned, and what changes were made |
| **New Starter Induction** | New OT Engineering / Operations hires | Within first 30 days | Complete Track 1 (engineers) or Track 3 (operations) as part of onboarding |

---

## Key Principles for Delivering This Training

1. **Respect their expertise.** OT engineers are specialists in their domain. The training should be presented as mutual capability-building, not as security professionals educating engineers about "proper" security hygiene.

2. **Use their language.** Wherever possible, frame security concepts in operational terms. "An adversary gaining access to this PLC could change the setpoint on this process loop" is more meaningful than "T0855: Unauthorised Command Message."

3. **Use real examples.** Abstract threat descriptions are less effective than concrete examples from their sector. The Dragos Year in Review and CISA advisories provide sector-specific incident data.

4. **Make it practical.** Every module should include something the participant can use or do immediately. Avoid purely theoretical sessions.

5. **Never blame.** Security awareness training that implies engineers have been negligent or operations staff are the "weakest link" will destroy the trust the collaboration programme depends on.

---

*Training records are maintained by the CSIRT Lead and reported at the quarterly programme review. Training completion is tracked as a collaboration metric (Joint Training Completion %).*
