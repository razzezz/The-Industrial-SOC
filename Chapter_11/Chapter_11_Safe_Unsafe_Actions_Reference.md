# Safe / Unsafe Response Actions: OT Quick Reference
# ================================================================
# Description: Quick-reference card for SOC analysts showing which
#   incident response actions are safe, conditional, or prohibited
#   in OT environments. Designed for printing and SOC wall display.
#
# Usage: Print, laminate, and post in SOC. Brief all analysts on
#   OT-specific cautions during onboarding and quarterly refreshers.
#
# RULE: When in doubt, DO NOT act on OT systems. Consult OT SME.
#
# Reference: Chapter 11 — Purpose-Built Incident Response
# ================================================================

---

## Response Action Matrix

### ✅ SAFE in OT — Standard procedures apply (Purdue L3.5+)

| Action | Scope | Notes |
|--------|-------|-------|
| Isolate IT endpoint via EDR | Enterprise workstations (L4–5) | Standard IT procedure |
| Disable compromised user account | Enterprise AD accounts | Verify no OT service dependencies first |
| Block IP/domain at perimeter firewall | Internet-facing infrastructure | Standard IT procedure |
| Collect forensic image (IT systems) | Workstations, servers at L4–5 | Standard IT procedure |
| Deploy EDR agent | Enterprise systems (L4–5) | Standard IT procedure |
| Active network scan | IT network (L4–5) | Standard IT procedure |
| Isolate IDMZ system | Jump hosts, relay servers (L3.5) | Safe but NOTIFY OT SME — affects remote access |

---

### ⚠️ CONDITIONAL in OT — Requires assessment and approval

| Action | Scope | Conditions | Required Approval |
|--------|-------|-----------|-------------------|
| EDR isolation of engineering workstation | L3 workstations | Verify no active PLC programming session | OT Engineer |
| Kill process via EDR | L3 workstations | Verify process is not critical to operations | OT Engineer |
| Force password reset (OT-accessible accounts) | Accounts used at L3 | Coordinate with shift to avoid lockout | OT SME + Shift Supervisor |
| Deploy EDR agent on OT workstation | L3 only, never below | Test in maintenance window, passive mode first | OT Engineer + Change Management |
| Enable EDR blocking mode on OT workstation | L3 workstations only | Only after extended tuning period in detect mode | OT SME + SOC Manager |
| Memory dump of OT workstation | L3 workstations | Test impact on system first | OT Engineer |
| EDR network isolation of L3 system | Site operations systems | Is this system operationally critical right now? | Joint: OT Engineer + SOC + Operations |
| Network VLAN isolation | OT subnets at L3 | Assess all downstream dependencies | Joint: OT Engineer + SOC + Operations |
| System shutdown | OT systems at L3 | Cascading failure assessment required | Joint: All CSIRT authorities |

---

### ❌ NEVER in OT — Absolute prohibition (Purdue L0–2)

| Action | Scope | Why Prohibited |
|--------|-------|---------------|
| Automated SOAR containment | Any asset at L0–L3 | Cannot assess operational impact automatically |
| Active network scanning | L0–L2 networks | Crashes legacy PLCs, RTUs, and field devices |
| Deploy EDR agent on controllers | PLCs, RTUs, SIS at L0–L1 | Not supported; destabilises real-time systems |
| Kill process on HMI | Active operator displays at L2 | May cause loss of view — operators blind to process |
| Automated network isolation | Control system networks at L0–L2 | Loss of control — operators lose ability to command process |
| Send commands to PLC/RTU | Controllers at L0–L1 | Only OT engineering, only with safety sign-off |
| Disable OT service accounts | Shared/service accounts at L0–L2 | May sever control system communications |
| Modify firewall rules in OT network | Firewalls between L0–L3 | May disrupt control system traffic paths |
| Reboot or power-cycle controller | PLCs, RTUs, SIS at L0–L1 | Only OT engineering, after process safety assessment |

---

## Decision Aid

```
Is the target system at Purdue Level 3.5 or above?
├── YES → Standard IT response procedures apply.
│         SOAR automation permitted.
│         Notify OT SME if system is in IDMZ.
│
└── NO → Is the target system at Purdue Level 3?
    ├── YES → CONDITIONAL. Consult OT SME before any action.
    │         Verify no operational dependencies.
    │         Document approval before executing.
    │
    └── NO → Target is at Purdue Level 0, 1, or 2.
             ❌ NO containment without engineering.
             Enrich, notify, monitor ONLY.
             Engineering-led response with SOC advisory.
             Safety assessment before ANY action.
```

---

## Key Principles

1. **Safety first.** Every action must be assessed for physical consequence.
2. **Never act alone below L3.** OT Engineering must be involved in every decision.
3. **Enrich, don't contain.** At L0–L2, the SOC's role is intelligence and monitoring, not containment.
4. **Document everything.** Every decision, every decision-maker, every rationale.
5. **When in doubt, monitor.** Enhanced monitoring with deferred containment is always available.
