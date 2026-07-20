# Conflict Resolution Escalation Path — IT/OT Security Operations

## Purpose

This document defines the escalation path for resolving disagreements between IT Security, OT Engineering, and Operations during security operations. Disagreements are expected and healthy — they reflect the different priorities that each function brings to the table. The goal is not to eliminate disagreement but to resolve it efficiently, safely, and with documented rationale.

---

## Escalation Levels

### Level 0: Working-Level Resolution (Target: Immediate)

**Participants:** The individuals directly involved in the disagreement (e.g., SOC analyst and OT engineer).

**Process:**
1. Each party states their position and rationale clearly.
2. Both parties reference the relevant policy, playbook, or charter provision.
3. If the disagreement involves a factual question (e.g., "Is this asset in a maintenance window?"), the relevant data source (OT_MaintenanceWindows watchlist, asset register) is consulted.
4. If agreement is reached, document the decision and proceed.

**Escalation trigger:** Agreement not reached within 15 minutes for time-sensitive decisions (active incident), or within one business day for non-time-sensitive decisions.

---

### Level 1: Functional Lead Resolution (Target: 30 Minutes for Incidents)

**Participants:** Functional leads — IT Security Lead, OT Engineering Lead, and/or Operations Representative.

**Process:**
1. The original parties brief their respective functional leads on the disagreement.
2. Functional leads discuss the issue directly, with each articulating their function's concerns and constraints.
3. The CSIRT Charter's Decision Authority Structure is applied:
   - **If the disagreement concerns process safety:** OT Engineering Lead's position prevails (safety veto).
   - **If the disagreement concerns security assessment:** IT Security Lead's position prevails.
   - **If the disagreement concerns production impact:** Operations Representative's position prevails within their domain.
   - **If the disagreement spans multiple domains:** Proceed to Level 2.

**Escalation trigger:** Functional leads cannot agree, or the disagreement spans multiple authority domains.

---

### Level 2: CSIRT Lead Resolution (Target: 60 Minutes for Incidents)

**Participants:** CSIRT Lead plus the disagreeing functional leads.

**Process:**
1. Each functional lead presents their position to the CSIRT Lead.
2. The CSIRT Lead asks clarifying questions and assesses the risk profile of each option.
3. The CSIRT Lead makes a decision based on the balance of safety risk, security risk, and operational impact.
4. **Exception:** If OT Engineering raises a safety concern at any point, the CSIRT Lead cannot override the safety veto. The decision either accommodates the safety concern or is escalated to Level 3.
5. The decision and its rationale are documented in the incident record.

**Escalation trigger:** CSIRT Lead determines the decision has implications beyond operational authority (significant financial impact, regulatory implications, or safety concern that cannot be resolved within the CSIRT).

---

### Level 3: Executive Resolution (Target: 2 Hours)

**Participants:** Executive Sponsor (CISO, COO, or designated executive), CSIRT Lead, relevant functional leads.

**Process:**
1. CSIRT Lead briefs the Executive Sponsor on the situation, the options, and the points of disagreement.
2. Executive Sponsor makes the final decision, accepting explicit responsibility for the risk of the chosen option.
3. **Exception:** Even the Executive Sponsor cannot override a safety veto from OT Engineering if there is a credible risk of harm to people or the environment. In such cases, the only acceptable resolution is to find an alternative approach that addresses both the safety concern and the security/operational need.
4. The decision and its rationale are documented and signed by the Executive Sponsor.

---

## Decision Framework for Common Disagreements

### "Should we isolate this asset?"

| IT Security Says | OT Engineering Says | Resolution Path |
|------------------|-------------------|-----------------|
| "Isolate immediately — active compromise confirmed" | "Isolation will trip the process — unacceptable safety risk" | OT Engineering veto prevails. IT Security implements enhanced monitoring (Chapter 11: Enhanced Monitoring with Deferred Isolation). Plan isolation for next safe maintenance window. |
| "Isolate immediately — active compromise confirmed" | "We can tolerate isolation if we switch to backup system first" | Proceed with isolation after OT Engineering confirms backup is active and stable. |
| "Isolate as precaution — suspicious but not confirmed" | "No isolation without confirmed threat — production disruption not justified" | Implement enhanced monitoring. Escalate to Level 1 if indicators strengthen. |

### "Should we deploy this security tool in the OT network?"

| IT Security Says | OT Engineering Says | Resolution Path |
|------------------|-------------------|-----------------|
| "We need this sensor deployed now — critical visibility gap" | "Not until it's been tested in our lab environment" | OT Engineering's position prevails. Follow the pilot programme process from Chapter 13. |
| "Passive sensor only, SPAN port, zero process interaction" | "We need to understand exactly what traffic it will see" | Reasonable concern — provide OT Engineering with full documentation and conduct a joint review before deployment. |

### "Should we scan the OT network?"

| IT Security Says | OT Engineering Says | Resolution Path |
|------------------|-------------------|-----------------|
| "Active vulnerability scan needed for compliance" | "Active scanning risks device instability" | Active scanning of PLCs and RTUs is prohibited without vendor-specific approval. Use passive discovery methods (Chapter 6). If active scanning is required for compliance, scope it to engineering workstations and servers only, with OT Engineering present. |

### "Should we patch this OT system?"

| IT Security Says | OT Engineering Says | Resolution Path |
|------------------|-------------------|-----------------|
| "Critical vulnerability, actively exploited, must patch" | "Patching requires downtime and vendor validation" | Schedule for next maintenance window. Implement compensating controls (network segmentation, enhanced monitoring) in the interim. Only emergency patching (outside maintenance windows) with executive approval and OT Engineering on standby. |

---

## Post-Resolution Requirements

Every disagreement resolved at Level 1 or above must be:

1. **Documented** in the incident record or relevant meeting minutes, including both positions and the rationale for the resolution.
2. **Reviewed** at the next weekly IT/OT sync to ensure both parties are satisfied with the outcome and to identify any process improvements.
3. **Reported** at the quarterly programme review if the disagreement represents a systemic issue (recurring pattern, structural gap, or unresolved tension).
4. **Fed back** into playbook or policy updates if the resolution revealed a gap in documented procedures.

---

## Anti-Patterns to Avoid

**Unilateral action.** IT Security taking containment action on OT assets without engineering consultation. This is the single most damaging action for the collaboration programme and may be the single most dangerous action for the physical process.

**Passive aggression.** OT Engineering blocking every security initiative without engaging constructively on alternatives. The safety veto exists for genuine safety concerns, not as a blanket refusal mechanism.

**Escalation avoidance.** Individuals accepting a decision they believe is wrong rather than escalating. The escalation path exists to be used — avoiding it to preserve harmony can lead to poor outcomes.

**Authority confusion.** Anyone claiming decision authority outside their domain (IT Security overriding safety concerns, OT Engineering blocking IT-only containment actions, Operations vetoing decisions that do not affect production).

---

*This escalation path is reviewed annually as part of the CSIRT Charter review. All CSIRT members must be familiar with the escalation levels and their responsibilities at each level.*
