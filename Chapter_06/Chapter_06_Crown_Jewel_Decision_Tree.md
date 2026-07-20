# Crown Jewel Rapid Assessment Decision Tree

## Purpose

This decision tree provides a quick, structured method for initial crown jewel classification during engineering interviews and site walkthroughs. It is designed for speed, not precision — formal scoring using the *Crown Jewel Identification Worksheet* (Chapter 5) should follow for all assets classified as Tier 1–3 during this rapid assessment.

Use this tree when you encounter a new asset and need to quickly determine its approximate criticality tier before a full scoring exercise.

---

## Decision Tree

```
START: Identify the asset
│
├─── Q1: Could compromise of this asset directly endanger human safety?
│    │   (e.g., SIS, ESD, fire/gas detection, pressure relief controls)
│    │
│    ├── YES ──────────────────────────── ► TIER 1 (Critical)
│    │                                      Immediate crown jewel.
│    │                                      Highest detection priority.
│    │                                      Any alert = Critical severity.
│    │
│    └── NO / UNCERTAIN
│         │
│         ├─── Q2: Does this asset directly execute control logic
│         │    for a physical process?
│         │    (e.g., PLC, DCS controller, RTU controlling actuators/valves)
│         │    
│         │    ├── YES
│         │    │    │
│         │    │    ├─── Q2a: Would loss of this controller cause
│         │    │    │    production shutdown or equipment damage?
│         │    │    │
│         │    │    ├── YES ────────────── ► TIER 2 (High)
│         │    │    │                        Process control crown jewel.
│         │    │    │                        Dedicated detection use cases.
│         │    │    │                        Alert = High severity.
│         │    │    │
│         │    │    └── NO ─────────────── ► TIER 3 (Medium)
│         │    │                             Non-critical process control.
│         │    │                             Standard monitoring.
│         │    │
│         │    └── NO
│         │         │
│         │         ├─── Q3: Does this asset provide operator visibility
│         │         │    into a critical process?
│         │         │    (e.g., HMI, SCADA server, historian for Tier 1/2 process)
│         │         │
│         │         │    ├── YES ─────────── ► TIER 3 (Medium)
│         │         │    │                     Loss of view risk.
│         │         │    │                     Monitor for availability
│         │         │    │                     and integrity.
│         │         │    │
│         │         │    └── NO
│         │         │         │
│         │         │         ├─── Q4: Does this asset hold or provide
│         │         │         │    access to control logic, configuration
│         │         │         │    backups, or OT network documentation?
│         │         │         │    (e.g., engineering workstation, code repo,
│         │         │         │    configuration management server)
│         │         │         │
│         │         │         │    ├── YES ── ► TIER 4 (Standard)
│         │         │         │    │            Engineering asset.
│         │         │         │    │            Monitor access and
│         │         │         │    │            data exfiltration.
│         │         │         │    │
│         │         │         │    └── NO
│         │         │         │         │
│         │         │         │         ├─── Q5: Does this asset control
│         │         │         │         │    network access between IT
│         │         │         │         │    and OT, or manage identity?
│         │         │         │         │    (e.g., IDMZ firewall, jump server,
│         │         │         │         │    VPN gateway, domain controller)
│         │         │         │         │
│         │         │         │         │    ├── YES ► TIER 5 (Supporting)
│         │         │         │         │    │          Boundary/identity asset.
│         │         │         │         │    │          Monitor for boundary
│         │         │         │         │    │          violations and abuse.
│         │         │         │         │    │
│         │         │         │         │    └── NO ─► UNCLASSIFIED
│         │         │         │         │              Record in inventory.
│         │         │         │         │              Assign during formal
│         │         │         │         │              scoring exercise.
```

---

## Quick Reference Table

| Tier | Label | Typical Assets | Alert Severity | Detection Priority |
|------|-------|----------------|----------------|--------------------|
| Tier 1 | Critical | SIS, ESD, fire/gas systems | Critical | Immediate — dedicated use cases required |
| Tier 2 | High | Production PLCs, DCS controllers, critical RTUs | High | High — dedicated use cases for key ATT&CK techniques |
| Tier 3 | Medium | HMIs, SCADA servers, historians, non-critical PLCs | Medium | Medium — standard monitoring with enrichment |
| Tier 4 | Standard | Engineering workstations, config servers, code repos | Medium/Low | Standard — access monitoring, exfiltration detection |
| Tier 5 | Supporting | IDMZ firewalls, jump servers, VPN gateways, DCs | Medium/Low | Standard — boundary and identity monitoring |
| Unclassified | — | Newly discovered or unassessed assets | Informational | Pending — assess during next review cycle |

---

## Escalation Rules by Tier

| Tier | SOC Action on Alert | Engineering Escalation | Management Notification |
|------|--------------------|-----------------------|------------------------|
| Tier 1 | Immediate investigation. Senior analyst or lead. | Immediate — regardless of indicator confidence | Within 1 hour of confirmed alert |
| Tier 2 | Priority investigation within SLA. | Immediate for confirmed activity; within 4 hours for suspected | Within 4 hours of confirmed alert |
| Tier 3 | Standard triage within SLA. | As needed based on triage outcome | Daily reporting |
| Tier 4 | Standard triage. | If investigation confirms OT-relevant activity | Weekly reporting |
| Tier 5 | Standard triage. | If boundary violation or credential abuse confirmed | Weekly reporting |

---

## Important Notes

- **When in doubt, tier up.** It is better to over-classify and reduce after formal scoring than to under-classify and miss a critical asset. A Tier 2 asset mistakenly classified as Tier 4 receives inadequate detection coverage.

- **Safety always wins.** Any asset where there is *any* credible connection to a safety function should be classified as Tier 1 until formal analysis proves otherwise. This includes assets that do not directly control safety functions but whose compromise could indirectly affect safety (e.g., an HMI that displays safety system status to operators).

- **Context matters.** The same device type may be different tiers in different installations. A PLC controlling office HVAC is Tier 4 or 5. A PLC controlling reactor cooling is Tier 1 or 2. Always assess based on the process being controlled, not the device type.

- **This tree is for initial classification only.** All Tier 1–3 classifications should be validated through formal scoring using the *Crown Jewel Identification Worksheet* from Chapter 5, with joint sign-off from security and OT engineering.
