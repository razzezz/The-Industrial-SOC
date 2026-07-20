# EDR Deployment Decision Tree for OT Environments

## Purpose

This decision tree provides a structured framework for determining where and how to deploy Endpoint Detection and Response (EDR) agents in OT environments. It balances the security value of endpoint telemetry against the operational risk of deploying software on systems that support critical physical processes.

---

## Decision Tree

```
START: Is the target system an OT-registered asset?
│
├── NO → Follow standard IT EDR deployment procedures.
│
└── YES → Q1: What Purdue Level is the asset?
    │
    ├── Level 0–1 (Field Devices, Basic Control)
    │   │ PLCs, RTUs, DCS Controllers, SIS, Field Instruments
    │   │
    │   └── DO NOT DEPLOY EDR.
    │       These devices run proprietary or real-time operating
    │       systems that cannot support endpoint agents.
    │       The risk of agent-induced faults is unacceptable.
    │       Compensate: Network monitoring (Zeek + Suricata)
    │       on the network segment serving these devices.
    │       
    │       Exception: Vendor-approved lightweight telemetry
    │       agents (e.g., Nozomi Arc) may be considered ONLY with:
    │       - Explicit written vendor approval
    │       - Laboratory testing on identical hardware/firmware
    │       - OT engineering sign-off
    │       - Staged rollout with rollback plan
    │
    ├── Level 2 (Supervisory Control)
    │   │ HMIs, SCADA Servers, Engineering Workstations
    │   │
    │   ├── Q2: What is the device type?
    │   │
    │   │   ├── Engineering Workstation
    │   │   │   │ HIGH PRIORITY — Deploy EDR
    │   │   │   │
    │   │   │   ├── Q3: Has the EDR been tested in a lab/non-prod
    │   │   │   │   environment with the engineering software?
    │   │   │   │   ├── YES → Deploy in DETECT-ONLY mode.
    │   │   │   │   │         Monitor for 4 weeks minimum.
    │   │   │   │   │         Proceed to Tuning Checklist.
    │   │   │   │   │
    │   │   │   │   └── NO → Test first.
    │   │   │   │           Install EDR on a test workstation
    │   │   │   │           running the same engineering software.
    │   │   │   │           Validate: no performance degradation,
    │   │   │   │           no application conflicts, no increased
    │   │   │   │           CPU/memory during engineering operations.
    │   │   │   │           Only proceed when validated.
    │   │   │   │
    │   │   │   └── Q4: After 4+ weeks in detect-only mode, is
    │   │   │       the false positive rate acceptable?
    │   │   │       ├── YES → Consider enabling BLOCKING mode.
    │   │   │       │         Requires:
    │   │   │       │         - Engineering team approval
    │   │   │       │         - Change management ticket
    │   │   │       │         - Rollback plan documented
    │   │   │       │         - First enable during maintenance window
    │   │   │       │
    │   │   │       └── NO → Continue tuning.
    │   │   │               Add exclusions for legitimate
    │   │   │               engineering processes.
    │   │   │               Reassess after another 4 weeks.
    │   │   │
    │   │   ├── HMI Station
    │   │   │   │ CAUTION — Deploy with vendor validation
    │   │   │   │
    │   │   │   ├── Q3: Has the HMI vendor confirmed EDR
    │   │   │   │   compatibility with their application?
    │   │   │   │   ├── YES → Q4: Has EDR been tested on a
    │   │   │   │   │   non-production HMI with realistic load?
    │   │   │   │   │   ├── YES → Deploy in DETECT-ONLY mode.
    │   │   │   │   │   │         Monitor HMI responsiveness
    │   │   │   │   │   │         closely for 8 weeks minimum.
    │   │   │   │   │   │         HMIs are more latency-sensitive
    │   │   │   │   │   │         than engineering workstations.
    │   │   │   │   │   │
    │   │   │   │   │   └── NO → Test first on non-production HMI.
    │   │   │   │   │
    │   │   │   │   └── NO → Do NOT deploy until vendor confirms.
    │   │   │   │           Request vendor compatibility statement.
    │   │   │   │           Compensate: Deploy Sysmon instead
    │   │   │   │           (lower resource impact, no blocking).
    │   │   │   │           Supplement with network monitoring.
    │   │   │   │
    │   │   │   └── BLOCKING MODE on HMIs:
    │   │   │       Generally NOT recommended unless:
    │   │   │       - Extended detect-only period (12+ weeks)
    │   │   │       - Zero false positives on HMI processes
    │   │   │       - Redundant HMI available
    │   │   │       - Engineering team explicit approval
    │   │   │       Risk: EDR blocking a legitimate HMI process
    │   │   │       causes operator loss of view — a safety event.
    │   │   │
    │   │   └── SCADA Server
    │   │       │ MEDIUM PRIORITY — Deploy with caution
    │   │       │
    │   │       ├── Q3: Is there a redundant SCADA server?
    │   │       │   ├── YES → Deploy EDR on secondary server first.
    │   │       │   │         Validate for 4 weeks, then deploy
    │   │       │   │         on primary. DETECT-ONLY mode.
    │   │       │   │
    │   │       │   └── NO → Deploy during maintenance window.
    │   │       │           DETECT-ONLY mode only.
    │   │       │           Have rollback plan ready.
    │   │       │           Engineering team on standby.
    │   │       │
    │   │       └── BLOCKING MODE on SCADA servers:
    │   │           Only with redundancy and extensive tuning.
    │   │           Same criteria as HMI blocking decision.
    │   │
    │   └── ALWAYS for Level 2:
    │       - Schedule deployment during maintenance windows
    │       - Have OT engineering on standby during deployment
    │       - Monitor system performance for 24 hours post-deploy
    │       - Configure EDR exclusions BEFORE deployment (see checklist)
    │
    ├── Level 3 (Site Operations)
    │   │ Historians, MES, Batch Management, Reporting
    │   │
    │   └── DEPLOY with standard change management.
    │       These systems run standard operating systems with
    │       sufficient resources for EDR agents.
    │       Deploy in DETECT-ONLY mode initially.
    │       Enable blocking after tuning period (4 weeks).
    │       Lower operational risk than Level 2.
    │
    ├── Level 3.5 (IDMZ)
    │   │ Jump Servers, Remote Access, Patch Management
    │   │
    │   └── MANDATORY — Deploy EDR in BLOCKING mode.
    │       These are the gateway systems between IT and OT.
    │       Every remote access session and vendor connection
    │       passes through these systems. Full EDR with active
    │       blocking is appropriate and recommended.
    │       No vendor compatibility concerns (standard servers).
    │
    └── Level 4–5 (Enterprise)
        │
        └── Follow standard IT EDR deployment.
            No OT-specific considerations.
```

---

## Deployment Phase Summary

| Phase | Scope | Mode | Duration | Gate to Next Phase |
|-------|-------|------|----------|-------------------|
| **Phase 1: Pilot** | 2–3 non-critical engineering workstations | Detect-only | 4 weeks | No performance impact, no application conflicts |
| **Phase 2: Engineering WS** | All engineering workstations | Detect-only | 8 weeks | Acceptable false positive rate, engineering approval |
| **Phase 3: HMI/SCADA** | HMI stations, SCADA servers, historians | Detect-only | 8+ weeks | Vendor validation, no HMI latency impact |
| **Phase 4: Enable Blocking** | Engineering workstations first, then expand | Active blocking | Ongoing | Extended tuning complete, documented approval |

---

## Key Principles

1. **Never deploy on real-time controllers.** PLCs, RTUs, DCS controllers, and SIS devices cannot support EDR agents.

2. **Detect-only first, always.** Every EDR deployment in OT starts in detect-only mode. Blocking is earned through validated tuning.

3. **Vendor validation for Level 2.** HMI and SCADA server deployments require confirmation from the control system vendor that the EDR agent is compatible with their application.

4. **Engineering approval is mandatory.** No EDR deployment at Level 2–3 proceeds without OT engineering team awareness and approval.

5. **Performance monitoring.** Monitor CPU, memory, disk I/O, and application responsiveness for at least 24 hours after every deployment. Establish pre-deployment baselines.

6. **Exclusions before deployment.** Configure OT application exclusions in the EDR policy BEFORE deploying the agent, not after performance issues arise.

7. **IDMZ systems are mandatory.** Jump servers, remote access gateways, and IDMZ infrastructure should have full EDR with blocking mode. These are standard servers with no vendor compatibility concerns.
