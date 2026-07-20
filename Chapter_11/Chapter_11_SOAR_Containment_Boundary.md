# SOAR Containment Boundary Reference
# ================================================================
# Description: Documents the Purdue-level-based automation boundaries
#   for SOAR playbooks in OT environments. Defines where automated
#   containment is permitted, conditional, or prohibited.
#
# Usage: Include in SOC SOPs. Reference when developing or reviewing
#   SOAR playbooks. Every SOAR playbook with a containment action
#   must include a Purdue level check as defined here.
#
# Reference: Chapter 11 — Purpose-Built Incident Response
# ================================================================

---

## The SOAR Containment Boundary

The fundamental rule: **automate enrichment everywhere, automate containment only above the boundary.**

---

### Purdue Levels 4–5: Enterprise IT
**Automation Level: FULL**

| Permitted Actions | Implementation |
|------------------|----------------|
| Endpoint isolation via EDR | Standard SOAR playbook |
| User account disable | Standard SOAR playbook |
| IP/domain block at perimeter | Standard SOAR playbook |
| Malware quarantine | Standard SOAR playbook |
| Evidence collection trigger | Standard SOAR playbook |
| Ticket creation | Standard SOAR playbook |

**Condition:** Standard IT SOAR playbooks apply without restriction.

---

### Purdue Level 3.5: Industrial DMZ (IDMZ)
**Automation Level: AUTOMATED WITH NOTIFICATION**

| Permitted Actions | Implementation | Notification Required |
|------------------|----------------|----------------------|
| Isolate compromised jump host | SOAR playbook + notification | OT SME + Engineering Liaison |
| Isolate compromised relay server | SOAR playbook + notification | OT SME + Engineering Liaison |
| Disable VPN/remote access session | SOAR playbook + notification | OT SME + Engineering Liaison |
| Block suspicious data replication | SOAR playbook + notification | OT SME + Engineering Liaison |

**Condition:** Containment executes automatically BUT simultaneous notification is sent to OT SME and Engineering Liaison. This is because IDMZ systems are IT infrastructure, but their isolation affects access to the OT environment.

**Implementation Note:** SOAR playbooks for IDMZ containment must include a parallel notification step that fires at the same time as the containment action, not after. Use Azure Logic Apps parallel branches or equivalent.

---

### Purdue Level 3: Site Operations
**Automation Level: ENRICHMENT AND NOTIFICATION ONLY**

| Permitted Automations | Prohibited Automations |
|----------------------|----------------------|
| Incident enrichment with OT_AssetRegister | Endpoint isolation |
| Maintenance window correlation | Network isolation |
| Notification to OT SME | Account disable |
| Notification to Engineering Liaison | Process kill |
| Ticket creation | Firewall rule change |
| Evidence collection from SIEM/logs | Any containment action |

**Condition:** ALL containment actions require human decision. The SOAR playbook may develop containment options and present them to the analyst, but it must NOT execute any action that affects the system's network connectivity, running processes, or access controls.

**Required for containment:** SOC analyst approval + OT Engineer approval. Documented in incident record.

---

### Purdue Levels 0–2: Control Systems
**Automation Level: ENRICHMENT AND NOTIFICATION ONLY — ABSOLUTE BOUNDARY**

| Permitted Automations | Prohibited Automations |
|----------------------|----------------------|
| Incident enrichment with OT_AssetRegister | ANY containment action |
| Maintenance window correlation | ANY response action |
| Notification to OT SME | Endpoint interaction |
| Notification to Engineering Liaison | Network changes |
| Notification to Safety Engineer (Tier 1 assets) | Account changes |
| Severity escalation based on crown jewel tier | PLC/RTU commands |

**Condition:** Engineering-led response with SOC advisory. Safety assessment required before ANY action. The SOC role at these levels is intelligence, enrichment, and monitoring — not containment.

**Required for ANY action:** Safety Engineer assessment + OT Engineer approval + Operations Supervisor awareness. Documented with full rationale.

---

## SOAR Playbook Design Checklist

When creating or reviewing any SOAR playbook that includes a containment action:

- [ ] Does the playbook include a Purdue level check for the target asset?
- [ ] Does the playbook query the `OT_AssetRegister` watchlist to determine Purdue level?
- [ ] If the target is at L3 or below, does the playbook HALT automated containment?
- [ ] If the target is at L3.5, does the playbook include parallel notification?
- [ ] Is the engineering approval gate implemented for L3 and below?
- [ ] Is there a manual override/approval step for all OT-related containment?
- [ ] Are all automated actions logged with timestamps and decision context?
- [ ] Has the playbook been reviewed by the OT SME?
- [ ] Has the playbook been tested in a tabletop exercise?

---

## Pseudo-Code: Purdue Level Check in SOAR Playbook

```
// Logic Apps / SOAR Containment Playbook
// Step 1: Get target asset IP from incident entities
// Step 2: Query OT_AssetRegister watchlist

let AssetContext = _GetWatchlist('OT_AssetRegister')
    | where IPAddress == TargetIP
    | project PurdueLevel, CrownJewelTier, DeviceType;

// Step 3: Apply containment boundary

IF AssetContext.PurdueLevel IN ("L4", "L5") THEN
    → Execute automated containment
    → Log action

ELSE IF AssetContext.PurdueLevel == "L3.5" THEN
    → Execute automated containment
    → SIMULTANEOUSLY notify OT SME and Engineering Liaison
    → Log action and notification

ELSE IF AssetContext.PurdueLevel == "L3" THEN
    → HALT automated containment
    → Enrich incident with OT context
    → Notify OT SME and Engineering Liaison
    → Present containment options to analyst
    → WAIT for human approval before any action
    → Log decision and approver

ELSE IF AssetContext.PurdueLevel IN ("L0", "L1", "L2") THEN
    → HALT ALL automated response
    → Enrich incident with OT context
    → Set severity based on CrownJewelTier
    → Notify OT SME + Engineering Liaison + Safety Engineer
    → Add incident task: "Safety assessment required"
    → Add incident task: "Engineering-led response — SOC advisory only"
    → Log enrichment

ELSE (Asset not in OT_AssetRegister)
    → Flag as unregistered OT asset
    → Treat as L3 (conservative) until classified
    → Notify OT SME for asset classification
```
