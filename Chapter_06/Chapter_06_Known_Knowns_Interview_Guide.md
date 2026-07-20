# "Known Knowns" Interview Guide for OT Teams

## Purpose

This guide provides a structured approach for SOC practitioners to conduct collaborative discovery sessions with OT engineering and plant operations teams. The goal is to extract the operational knowledge that exists within the engineering team — critical systems, process dependencies, legacy assets, and access patterns — and translate it into an actionable asset inventory for security operations.

## Before the Interview

### Preparation Checklist

- [ ] Identify the right participants: Senior OT engineer, shift supervisor or operations manager, control system integrator (if available)
- [ ] Frame the session as a **learning exercise, not an audit**. You are there to understand, not to assess or criticise.
- [ ] Bring any existing documentation you have found: network diagrams, asset spreadsheets, previous audit reports
- [ ] Prepare a blank copy of the *OT Asset Register Template* to populate during the session
- [ ] Book a meeting room near the control room or plant floor if possible — proximity to the systems helps the conversation
- [ ] Allocate 2 hours for the first session. Plan for follow-up sessions as needed
- [ ] Bring coffee

### Setting the Tone

Open the session with something like:

> "We're trying to build a better picture of the OT environment so we can make our security monitoring more relevant and less noisy. We're not here to find problems — we're here to understand your world so we can protect it better. You know these systems better than anyone, and we need that knowledge."

This framing matters. OT engineers have often experienced "security" as an external force that imposes restrictions without understanding operational constraints. Position yourself as a partner, not an authority.

---

## Interview Topics and Questions

### Topic 1: Critical Processes and Systems

**Objective:** Identify the crown jewels from an operational perspective.

| # | Question | What You're Learning | Record In |
|---|----------|---------------------|-----------|
| 1.1 | "What systems, if they went offline right now, would cause the biggest operational problem?" | Crown jewel identification from an operational perspective | CrownJewelTier, ProcessFunction |
| 1.2 | "What would happen if [system X] stopped working? How long before there's a real problem?" | Consequence severity and time-to-impact | SafetyScore, FinancialScore |
| 1.3 | "Are there any systems where failure could result in a safety incident?" | Safety-critical asset identification | SafetyCritical = true, SafetyScore |
| 1.4 | "Which systems are involved in environmental compliance monitoring or reporting?" | Regulatory and environmental impact assets | EnvironmentalScore, RegulatoryScore |
| 1.5 | "If you had to restart a process after a complete shutdown, what's the sequence? What has to come up first?" | Process dependencies and recovery priorities | Notes, ProcessArea |
| 1.6 | "Are there any single points of failure — systems with no redundancy?" | High-impact, single-target assets | Notes, CrownJewelTier |

### Topic 2: System Architecture and Inventory

**Objective:** Map the physical systems to network assets.

| # | Question | What You're Learning | Record In |
|---|----------|---------------------|-----------|
| 2.1 | "Can you walk me through how [process X] works, from sensor to operator display?" | Process-to-asset mapping across Purdue levels | DeviceType, PurdueLevel, ProcessFunction |
| 2.2 | "For each of those systems, do you know the manufacturer and model?" | Device identity | Manufacturer, Model |
| 2.3 | "Which PLCs/controllers run the logic for this process? How many are there?" | Level 1 asset identification | IPAddress, DeviceType = PLC |
| 2.4 | "Which HMIs do operators use to monitor and control this process?" | Level 2 asset identification | DeviceType = HMI |
| 2.5 | "Is there a historian that records process data? Where does it sit on the network?" | Level 3 asset identification | DeviceType = Historian |
| 2.6 | "Do you have network diagrams or architecture drawings we could review together?" | Existing documentation to validate and supplement | All fields |
| 2.7 | "Are there any P&IDs (piping and instrumentation diagrams) we could look at?" | Process-to-controller mapping | ProcessArea, ProcessFunction |

### Topic 3: Legacy and End-of-Life Systems

**Objective:** Identify the assets with the greatest vulnerability exposure and operational fragility.

| # | Question | What You're Learning | Record In |
|---|----------|---------------------|-----------|
| 3.1 | "Which systems have been here the longest? Which ones are the hardest to replace?" | Legacy asset identification | FirmwareVersion, VendorSupport |
| 3.2 | "Are there any systems still running Windows XP, Server 2003, or Server 2008?" | Legacy OS identification | OSVersion |
| 3.3 | "Are there systems where the vendor no longer provides support or patches?" | End-of-life identification | VendorSupport = EndOfLife |
| 3.4 | "Has anyone ever tried to update the firmware on [system X]? What happened?" | Patch history and constraints | Notes |
| 3.5 | "Are there spare parts available for the critical legacy systems?" | Operational resilience context | Notes |

### Topic 4: Access and Connectivity

**Objective:** Understand who and what connects to OT systems.

| # | Question | What You're Learning | Record In |
|---|----------|---------------------|-----------|
| 4.1 | "Who else accesses these systems — vendors, contractors, remote engineers?" | External access surface | Notes |
| 4.2 | "How do vendors connect when they need to do maintenance?" | Remote access architecture | DeviceType = RemoteAccessGW/VPN |
| 4.3 | "Do operators share login accounts on the HMIs, or does everyone have their own?" | Authentication posture | AuthType = Shared/AD/Local |
| 4.4 | "Are there any default passwords on PLCs or controllers that haven't been changed?" | Default credential risk | AuthType = Default |
| 4.5 | "Are any OT systems connected directly to the internet for any reason?" | Direct internet exposure | Notes (critical finding) |
| 4.6 | "Is there a process for requesting changes to PLC logic or HMI configurations?" | Change management maturity | Notes |

### Topic 5: Protocols and Communication

**Objective:** Understand the communication landscape for detection baseline development.

| # | Question | What You're Learning | Record In |
|---|----------|---------------------|-----------|
| 5.1 | "What industrial protocols are in use? Modbus, DNP3, EtherNet/IP, Profinet, OPC?" | Protocol landscape | Protocols |
| 5.2 | "For the critical PLCs, which devices talk to them and how often?" | Communication profile | CommPartners |
| 5.3 | "Are there scheduled tasks or batch processes that cause spikes in network traffic at specific times?" | Normal operational patterns (avoids false positives) | Notes |
| 5.4 | "Are there any wireless connections in the OT environment?" | Wireless access surface | Notes |
| 5.5 | "Is there any serial communication (RS-232/485) still in use?" | Non-IP communication gaps | Notes |

### Topic 6: Maintenance and Change

**Objective:** Understand operational rhythms for maintenance window correlation.

| # | Question | What You're Learning | Record In |
|---|----------|---------------------|-----------|
| 6.1 | "How often is maintenance performed on the control systems? Is there a regular schedule?" | Maintenance cadence | OT_MaintenanceWindows data |
| 6.2 | "What does a typical maintenance window look like? Who is involved, and what systems are touched?" | Maintenance activity patterns | OT_MaintenanceWindows data |
| 6.3 | "How are maintenance activities planned and approved? Is there a change management system?" | Change management process | ChangeRequestRef patterns |
| 6.4 | "Are there annual or seasonal shutdowns when significant work is done?" | Major maintenance windows | Notes |

---

## After the Interview

### Immediate Actions (within 48 hours)

1. **Transcribe notes** into the OT Asset Register Template (CSV format)
2. **Send a summary** back to the interviewees for review and correction — this builds trust and improves accuracy
3. **Identify gaps** — what couldn't they answer? What needs a follow-up session or documentation review?
4. **Flag crown jewels** — based on the interview, which systems are clearly Tier 1 or Tier 2?
5. **Schedule the follow-up** — plan the next session to fill gaps and validate with documentation

### Building the Relationship

The interview is not a one-time event. The goal is to establish an ongoing relationship where OT engineering and the SOC share information routinely. Practical ways to sustain this:

- Share back what you learn: "We discovered these 15 devices on the OT network through our monitoring — do you recognise them all?"
- Invite engineering to participate in detection rule development: "We're building a rule to detect unusual PLC writes — can you tell us what 'normal' looks like?"
- Acknowledge their expertise publicly: reference their input in reports and presentations
- Deliver value first: fix a problem they care about before asking for more of their time

---

## Tips for Difficult Conversations

**"That's classified / I can't share that."** Respect the boundary. Ask if there's a sanitised version available, or if you can discuss the general architecture without specific details. Some progress is better than none.

**"We don't have time for this."** Acknowledge the constraint. Offer to work in short sessions (30 minutes) or to shadow them during routine work rather than scheduling dedicated meetings.

**"Security people always break things."** This is earned distrust from past experience. Acknowledge it directly: "That's a fair concern. Our goal is to monitor and detect, not to change or block anything in the OT environment without your agreement. We will not take any action on OT systems without discussing it with you first."

**"We already have security covered."** Ask them to describe their current security controls. This reveals what they consider "security" (often physical access controls, backup procedures, or vendor support contracts) and identifies the gaps where SOC monitoring adds value.
