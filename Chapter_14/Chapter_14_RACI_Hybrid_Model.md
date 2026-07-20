# RACI Matrix — Hybrid SOC Model for OT Security Operations

## Purpose

This matrix defines the Responsibility Assignment for all operational functions in the hybrid SOC model, where an MSSP provides 24/7 monitoring and an in-house OT security team provides deep operational context, detection engineering, and incident coordination.

**R** = Responsible (performs the work)
**A** = Accountable (owns the outcome, one per function)
**C** = Consulted (provides input before the action)
**I** = Informed (notified after the action)

---

## Alert Triage and Investigation

| Function | MSSP SOC | In-House OT Security | OT Engineering | Operations | Executive |
|----------|---------|---------------------|---------------|------------|-----------|
| **24/7 alert monitoring** | R, A | I | — | — | — |
| **Initial triage (all alerts)** | R, A | I | — | — | — |
| **OT alert context enrichment** | R | A, C | C | — | — |
| **Tier 1 crown jewel alert escalation** | R | A | C | I | — |
| **Engineering escalation** | I | R, A | R | I | — |
| **Maintenance window verification** | R | A | C | — | — |
| **Deep investigation (IT-side)** | R | A, C | — | — | — |
| **Deep investigation (OT-side)** | C | R, A | C | — | — |
| **Investigation closure** | R | A | I | — | — |

---

## Detection Engineering

| Function | MSSP SOC | In-House OT Security | OT Engineering | Operations | Executive |
|----------|---------|---------------------|---------------|------------|-----------|
| **Detection rule design (IT)** | R | A, C | — | — | — |
| **Detection rule design (OT)** | C | R, A | C | — | — |
| **Detection rule testing** | C | R, A | C | — | — |
| **Detection rule deployment** | R | A | I | — | — |
| **False positive tuning** | R | A, C | C | — | — |
| **ATT&CK coverage assessment** | C | R, A | — | — | — |
| **Detection rule lifecycle management** | C | R, A | — | — | — |

---

## Threat Hunting

| Function | MSSP SOC | In-House OT Security | OT Engineering | Operations | Executive |
|----------|---------|---------------------|---------------|------------|-----------|
| **Hunting hypothesis development** | C | R, A | C | — | — |
| **Hunting execution (IT telemetry)** | R | A, C | — | — | — |
| **Hunting execution (OT telemetry)** | C | R, A | C | — | — |
| **Hunting findings documentation** | C | R, A | I | — | — |
| **Detection rule creation from findings** | C | R, A | C | — | — |

---

## Threat Intelligence

| Function | MSSP SOC | In-House OT Security | OT Engineering | Operations | Executive |
|----------|---------|---------------------|---------------|------------|-----------|
| **Threat intelligence collection** | R | A, C | — | — | — |
| **Intelligence analysis (IT threats)** | R | A, C | — | — | — |
| **Intelligence analysis (OT/ICS threats)** | C | R, A | C | — | — |
| **Intelligence operationalisation** | C | R, A | C | — | — |
| **Sector intelligence briefings** | C | R, A | I | I | I |
| **ISAC participation** | I | R, A | C | — | — |

---

## Incident Response

| Function | MSSP SOC | In-House OT Security | OT Engineering | Operations | Executive |
|----------|---------|---------------------|---------------|------------|-----------|
| **Incident declaration** | R | A | I | I | I |
| **CSIRT activation** | I | R, A | R | R | I |
| **Cybersecurity assessment** | R | A | C | — | — |
| **Operational impact assessment** | — | C | R, A | C | — |
| **Containment at L4–L5** | R | A | — | — | — |
| **Containment at L3.5 (IDMZ)** | R | A | C | I | — |
| **Containment at L0–L3** | I | C | R, A | C | I |
| **Evidence collection (IT)** | R | A | — | — | — |
| **Evidence collection (OT)** | I | C | R, A | — | — |
| **Regulatory notification** | I | C | I | I | R, A |
| **Recovery coordination** | C | R, A | R | R | I |
| **After-Action Review** | R | A | R | R | I |
| **Post-incident intelligence feedback** | C | R, A | C | — | — |

---

## Operational Context and Liaison

| Function | MSSP SOC | In-House OT Security | OT Engineering | Operations | Executive |
|----------|---------|---------------------|---------------|------------|-----------|
| **OT_MaintenanceWindows watchlist maintenance** | I | A | R | C | — |
| **OT_AssetRegister watchlist maintenance** | I | R, A | C | — | — |
| **OT_CrownJewels watchlist maintenance** | I | R, A | C | C | — |
| **Weekly IT/OT sync** | I | R, A | R | R | — |
| **Monthly tabletop exercise** | C | R, A | R | R | — |
| **Quarterly programme review** | C | R, A | R | R | R |
| **Engineering liaison (ongoing)** | I | R, A | R | C | — |

---

## Tooling and Infrastructure

| Function | MSSP SOC | In-House OT Security | OT Engineering | Operations | Executive |
|----------|---------|---------------------|---------------|------------|-----------|
| **SIEM platform management** | R | A | — | — | — |
| **OT sensor deployment** | C | R, A | C | I | — |
| **OT sensor health monitoring** | R | A | I | — | — |
| **Tool evaluation and selection** | C | R, A | C | C | I |
| **Tool pilot programme** | C | R, A | R | C | — |
| **Integration health checks** | R | A | I | — | — |

---

## Training and Development

| Function | MSSP SOC | In-House OT Security | OT Engineering | Operations | Executive |
|----------|---------|---------------------|---------------|------------|-----------|
| **SOC analyst OT training delivery** | I | R, A | C | C | — |
| **OT engineering security training delivery** | I | R, A | C | — | — |
| **Operations security awareness delivery** | I | R, A | C | C | — |
| **Training completion tracking** | C | R, A | — | — | I |
| **Competency assessment** | C | R, A | C | — | — |

---

## Customisation Guidance

This RACI is a starting template. Customise it based on your specific organisational context:

1. **Review with all parties.** Distribute the RACI to MSSP, in-house team, engineering, and operations leads. Confirm that each party agrees with their assignments.

2. **Resolve ambiguity.** Every function must have exactly one "A" (Accountable). If two parties both claim accountability, resolve it before deploying the RACI.

3. **Align with contracts.** For the hybrid model, ensure the MSSP contract explicitly covers the functions where the MSSP is Responsible. Gaps between the RACI and the contract will create operational blind spots.

4. **Review quarterly.** As the programme matures, responsibilities may shift. Functions initially performed by the MSSP may be brought in-house, or vice versa.

5. **Include in onboarding.** Every new team member (MSSP analyst, in-house hire, or engineering participant) should receive the RACI as part of their induction.

---

*This RACI is reviewed annually as part of the CSIRT Charter review and updated whenever the delivery model or organisational structure changes.*
