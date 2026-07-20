# EDR Response Decision Trees for OT Environments
# ================================================================
# Description: Decision trees for common EDR response actions in
#   OT environments. Each tree incorporates Purdue level awareness,
#   operational impact assessment, and engineering coordination.
#
# Usage: Reference during incident response when considering EDR
#   actions on OT-connected systems. Follow the tree from top to
#   bottom, taking the path indicated by each answer.
#
# Reference: Chapter 11 — Purpose-Built Incident Response
# ================================================================

---

## Decision Tree 1: EDR Network Isolation

**Trigger:** SOC analyst considers isolating an endpoint via EDR to contain a confirmed or suspected threat.

```
START: EDR isolation requested for [endpoint]
│
├── Q1: What Purdue Level is this endpoint?
│   │
│   ├── Level 4-5 (Enterprise IT)
│   │   └── ✅ PROCEED with standard EDR isolation.
│   │       No OT coordination required.
│   │
│   ├── Level 3.5 (IDMZ)
│   │   └── ⚠️ PROCEED with isolation + NOTIFY OT SME.
│   │       Isolation may affect remote access to OT.
│   │       Notify engineering liaison simultaneously.
│   │
│   ├── Level 3 (Site Operations)
│   │   └── Q2: Is this an engineering workstation?
│   │       │
│   │       ├── YES
│   │       │   └── Q3: Are there active PLC programming or 
│   │       │       monitoring sessions from this workstation?
│   │       │       │
│   │       │       ├── YES → ❌ DO NOT isolate.
│   │       │       │   Defer until sessions can be safely migrated.
│   │       │       │   Consult OT Engineer for migration plan.
│   │       │       │
│   │       │       ├── NO → Q4: Can operators maintain control
│   │       │       │   without this workstation?
│   │       │       │   │
│   │       │       │   ├── YES → ⚠️ PROCEED with OT Engineer approval.
│   │       │       │   │   Document approval and rationale.
│   │       │       │   │
│   │       │       │   └── NO → ❌ DO NOT isolate.
│   │       │       │       Consider network-only isolation (VLAN).
│   │       │       │       Plan for maintenance window.
│   │       │       │
│   │       │       └── UNKNOWN → Consult OT Engineer before deciding.
│   │       │
│   │       └── NO (SCADA server, historian, etc.)
│   │           └── Q5: Is this system critical for current operations?
│   │               │
│   │               ├── YES → ❌ DO NOT isolate.
│   │               │   Enhanced monitoring only.
│   │               │   Develop containment plan for maintenance window.
│   │               │
│   │               └── NO → ⚠️ PROCEED with joint approval.
│   │                   OT Engineer + Operations Supervisor + SOC.
│   │
│   └── Level 0-2 (Control Systems)
│       └── ❌ NEVER isolate via EDR.
│           EDR should not be deployed at L0-2.
│           If somehow present: DO NOT use for containment.
│           Engineering-led response only.
```

---

## Decision Tree 2: Kill Process via EDR

**Trigger:** SOC analyst identifies a suspicious or malicious process and considers terminating it via EDR remote response.

```
START: Process kill requested for [process] on [endpoint]
│
├── Q1: What Purdue Level is this endpoint?
│   │
│   ├── Level 4-5 (Enterprise IT)
│   │   └── ✅ PROCEED with standard process kill.
│   │
│   ├── Level 3.5 (IDMZ)
│   │   └── Q2: Is this process related to IT/OT data relay
│   │       (historian replication, patch management, etc.)?
│   │       │
│   │       ├── YES → ⚠️ Kill, but NOTIFY OT SME.
│   │       │   Data flow to/from OT may be interrupted.
│   │       │
│   │       └── NO → ✅ PROCEED with standard process kill.
│   │
│   ├── Level 3 (Site Operations)
│   │   └── Q3: Is this an engineering workstation or SCADA server?
│   │       │
│   │       ├── Engineering Workstation
│   │       │   └── Q4: Is the target process part of the 
│   │       │       engineering/development software suite?
│   │       │       │
│   │       │       ├── YES → ⚠️ Consult OT Engineer.
│   │       │       │   Killing may lose unsaved PLC project data.
│   │       │       │   May crash dependent monitoring tools.
│   │       │       │
│   │       │       └── NO → ⚠️ PROCEED with OT Engineer notification.
│   │       │           Monitor for impact after kill.
│   │       │
│   │       └── SCADA Server / HMI
│   │           └── Q5: Is this system actively displaying process
│   │               data to operators or running control logic?
│   │               │
│   │               ├── YES → ❌ DO NOT kill process.
│   │               │   Risk of crashing HMI/SCADA application.
│   │               │   Operators lose visibility.
│   │               │   Monitor and plan for safe intervention window.
│   │               │
│   │               └── NO → ⚠️ OT Engineer + Operations approval required.
│   │                   Verify no operator dependency.
│   │
│   └── Level 0-2
│       └── ❌ NEVER kill processes on control system devices.
│           Engineering-led response only.
```

---

## Decision Tree 3: Collect Forensic Evidence via EDR

**Trigger:** SOC analyst needs to collect evidence (memory dump, disk image, process tree) from an endpoint involved in an OT incident.

```
START: Evidence collection requested from [endpoint]
│
├── Q1: What Purdue Level is this endpoint?
│   │
│   ├── Level 4-5 (Enterprise IT)
│   │   └── ✅ PROCEED with standard EDR evidence collection.
│   │       Full capabilities: memory dump, disk image, process tree,
│   │       network connections, file timeline.
│   │
│   ├── Level 3.5 (IDMZ)
│   │   └── ✅ PROCEED with standard EDR evidence collection.
│   │       These are IT systems. Full capabilities available.
│   │
│   ├── Level 3 (Site Operations)
│   │   └── Q2: What type of evidence collection?
│   │       │
│   │       ├── Process tree / timeline export
│   │       │   └── ✅ Low-impact. PROCEED.
│   │       │       Passive read from EDR telemetry store.
│   │       │
│   │       ├── Network connection dump
│   │       │   └── ✅ Low-impact. PROCEED.
│   │       │       Passive read from EDR telemetry store.
│   │       │
│   │       ├── File system analysis / hash collection
│   │       │   └── ⚠️ PROCEED with monitoring.
│   │       │       May cause brief disk I/O spike on older systems.
│   │       │       Monitor system performance during collection.
│   │       │
│   │       ├── Memory dump
│   │       │   └── Q3: Is this system running real-time applications
│   │       │       (HMI display, SCADA polling)?
│   │       │       │
│   │       │       ├── YES → ⚠️ CAUTION.
│   │       │       │   Memory dump may cause temporary system pause.
│   │       │       │   Schedule during operator shift change or
│   │       │       │   when backup system is available.
│   │       │       │   OT Engineer approval required.
│   │       │       │
│   │       │       └── NO → ⚠️ PROCEED with monitoring.
│   │       │           Monitor system performance during collection.
│   │       │
│   │       └── Disk image (full)
│   │           └── ⚠️ Schedule for maintenance window.
│   │               Full disk image is I/O intensive.
│   │               Not safe during production on real-time systems.
│   │               OT Engineer approval required.
│   │
│   └── Level 0-2 (Control Systems)
│       └── EDR should not be present at these levels.
│           Evidence collection from PLCs/RTUs is ENGINEERING-LED.
│           SOC provides guidance on what to collect.
│           OT Engineer performs the collection.
│           Methods: PLC logic export, configuration backup,
│           historian data export, network PCAP from SPAN port.
```

---

## Decision Tree 4: Enable EDR Blocking Mode

**Trigger:** SOC considers switching EDR from detect (passive) mode to protect (blocking) mode on an OT-connected system.

```
START: EDR mode change requested for [endpoint]
│
├── Q1: What Purdue Level is this endpoint?
│   │
│   ├── Level 4-5 (Enterprise IT)
│   │   └── ✅ Standard change management applies.
│   │
│   ├── Level 3.5 (IDMZ)
│   │   └── ⚠️ PROCEED with standard change management.
│   │       Test in staged rollout. Monitor for false positives
│   │       affecting IT/OT data flow.
│   │
│   ├── Level 3 (Site Operations)
│   │   └── Q2: Has EDR been running in detect mode on this system
│   │       for at least 30 days with false positives resolved?
│   │       │
│   │       ├── YES → Q3: Has the false positive tuning been validated
│   │       │   against all operational scenarios (normal ops,
│   │       │   maintenance, shift change, startup/shutdown)?
│   │       │   │
│   │       │   ├── YES → ⚠️ PROCEED during maintenance window.
│   │       │   │   OT Engineer present during mode switch.
│   │       │   │   Monitor system for 4 hours post-change.
│   │       │   │   Rollback plan documented before switching.
│   │       │   │
│   │       │   └── NO → ❌ NOT YET.
│   │       │       Extend detect-mode tuning period.
│   │       │       Document remaining false positive scenarios.
│   │       │
│   │       └── NO → ❌ NOT YET.
│   │           Minimum 30-day detect-mode baseline required.
│   │           Continue monitoring and tuning false positives.
│   │
│   └── Level 0-2
│       └── ❌ EDR should not be deployed at L0-2.
│           Do not deploy. Do not change mode.
```

---

## Quick Reference Summary

| EDR Action | L4-5 | L3.5 | L3 | L0-2 |
|-----------|------|------|-----|------|
| Network Isolation | ✅ Auto | ⚠️ Auto + Notify | ⚠️ Joint Approval | ❌ Never |
| Kill Process | ✅ Auto | ✅/⚠️ Check relay | ⚠️ OT Approval | ❌ Never |
| Evidence Collection | ✅ Full | ✅ Full | ⚠️ Selective | ❌ Engineering-led |
| Enable Blocking | ✅ Standard | ⚠️ Staged | ⚠️ Extended test | ❌ Not deployed |
| Memory Dump | ✅ Standard | ✅ Standard | ⚠️ Schedule | ❌ Not deployed |
