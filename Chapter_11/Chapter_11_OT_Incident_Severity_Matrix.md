# OT Incident Severity Matrix
# ================================================================
# Description: Four-level severity classification for OT security
#   incidents. Incorporates physical consequence, safety system
#   status, and regulatory reporting thresholds alongside standard
#   cybersecurity severity indicators.
#
# Usage: Print and display in SOC. Reference during incident triage.
#   Severity drives escalation path, response timeline, and
#   regulatory reporting decisions.
#
# Reference: Chapter 11 — Purpose-Built Incident Response
# ================================================================

---

## SEV-1: CRITICAL — Safety or Environmental Impact Imminent or Active

**Criteria (any one triggers SEV-1):**
- Confirmed or suspected compromise of Tier 1 (safety system) assets
- Confirmed manipulation of PLC/DCS logic at Purdue Levels 0–1
- Active disruption of operator visibility to safety-critical processes
- OT Engineering assesses continued operation poses safety risk
- Any incident where physical harm or environmental release is possible

**Response Requirements:**

| Action | Timeline |
|--------|----------|
| CSIRT activation | Immediate |
| OT SME + Safety Engineer engaged | Immediate |
| Engineering Liaison + Operations Manager | Within 15 minutes |
| CISO + Plant Director notified | Within 30 minutes |
| Consider controlled shutdown if safe state cannot be assured | Immediate assessment |
| Regulatory early warning (NIS 2 Article 23) | Within 24 hours if threshold met |
| Communication updates to CSIRT | Every 15 minutes during active response |

**Decision Authority:** Joint — OT Engineering (safety lead) + IT Security (threat lead) + Executive (business lead). Safety VETO applies.

---

## SEV-2: HIGH — Operational Impact Confirmed or Likely

**Criteria (any one triggers SEV-2):**
- Confirmed adversary presence on OT systems at Purdue Levels 0–3
- Confirmed credential compromise for accounts with OT access
- Confirmed lateral movement from IT into OT network
- Confirmed exfiltration of control logic, network diagrams, or operational procedures
- EDR alert indicating adversary tooling on engineering workstations with active OT connections

**Response Requirements:**

| Action | Timeline |
|--------|----------|
| CSIRT activation | Within 1 hour |
| OT Engineering + Operations engaged | Immediately |
| Enhanced monitoring deployed | Within 1 hour |
| Containment options developed and presented | Within 2 hours |
| Assess against NIS 2 reporting threshold | Within 4 hours |
| Communication updates to CSIRT | Every 30 minutes during active response |

**Decision Authority:** Joint — IT Security leads investigation; OT Engineering provides impact assessment; containment requires engineering approval for Purdue Levels 0–3.

---

## SEV-3: MEDIUM — OT Boundary Probed or IT-Side Compromise with OT Implications

**Criteria (any one triggers SEV-3):**
- Confirmed compromise of IDMZ systems (jump hosts, historian relays, patch servers)
- Compromise of enterprise accounts belonging to engineers with OT access
- Scanning or reconnaissance targeting OT network ranges from compromised IT systems
- EDR detection on engineering workstations that have not yet accessed OT systems
- Unauthorised access attempts at the IT/OT boundary

**Response Requirements:**

| Action | Timeline |
|--------|----------|
| Standard SOC investigation with OT context enrichment | Immediate |
| OT SME consulted for impact assessment | Within 30 minutes |
| Engineering Liaison notified | Within 1 hour |
| Enhanced monitoring of IT/OT boundary | Within 1 hour |
| IT-side containment (SOAR permitted at L3.5+) | Per standard SOC procedures |
| Communication updates | Every 1 hour, then daily |

**Decision Authority:** IT Security leads. SOAR automation permitted at Purdue Levels 3.5+. OT SME consulted for context.

---

## SEV-4: LOW — Anomalous OT Activity, Likely Benign

**Criteria:**
- ML anomaly detection flagging new but potentially legitimate communication patterns
- Unusual timing of known legitimate operations
- Minor policy violations (e.g., direct internet access from OT-adjacent workstation)
- Alerts during active maintenance windows correlating with documented activity
- Alerts from detection rules in tuning phase with known false-positive patterns

**Response Requirements:**

| Action | Timeline |
|--------|----------|
| Standard investigation with OT context | Within 4 hours |
| Enrich with maintenance window and operational context | At triage |
| Consult OT SME if unable to confirm benign | As needed |
| Close with documentation if confirmed benign | Per investigation |
| Include in daily SOC report | End of shift |

**Decision Authority:** SOC analyst. Escalate if benign origin cannot be confirmed.

---

## Regulatory Reporting Quick Reference

| Regulation | Trigger | Timeline | Authority |
|-----------|---------|----------|-----------|
| **NIS 2 (EU)** | Significant incident causing severe operational disruption or capable of affecting others | Early warning: 24 hours; Notification: 72 hours; Final report: 1 month | National Competent Authority / CSIRT |
| **NCSC CAF (UK)** | Incident affecting essential service delivery | Report to lead regulator and NCSC per sector-specific timeline | NCSC + Sector Regulator |
| **NERC CIP (US — Energy)** | Cyber Security Incident affecting BES Cyber Systems | 1 hour for certain incidents (CIP-008-6) | E-ISAC |
| **TSA SD (US — Pipeline)** | Cybersecurity incident on pipeline systems | 12 hours to CISA | CISA |

**Note:** Legal/Compliance leads regulatory reporting assessment. The SOC provides the technical incident details; Legal determines whether the regulatory threshold is met.
