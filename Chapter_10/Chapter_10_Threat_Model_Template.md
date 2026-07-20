# Threat Modelling Template
# ================================================================
# Description: Template for developing scenario-based threat models
#   populated with adversary TTPs at each stage of the attack path.
#   Includes three reference scenarios from Chapter 10.
#
# Usage: Develop one threat model per high-priority scenario.
#   Use the attack path methodology from Chapter 5 and populate
#   with TTPs from the intelligence function. Output informs
#   detection engineering and hunting priorities.
# ================================================================

## SCENARIO IDENTIFICATION

| Field | Value |
|-------|-------|
| **Scenario ID** | TM-[YYYY]-[NNN] |
| **Scenario Name** | [e.g., "Patient Pre-Positioner"] |
| **Based On** | [Threat actor or campaign — e.g., "Volt Typhoon (VOLTZITE) tradecraft"] |
| **Target Crown Jewel** | [Specific asset from OT_CrownJewels watchlist] |
| **Target Process** | [Physical process the crown jewel controls] |
| **Worst-Case Impact** | [Physical/operational consequence if adversary succeeds] |
| **Date Created** | [Date] |
| **Analyst** | [Name] |

---

## ATTACK PATH — STAGE BY STAGE

### External → Level 4–5 (Enterprise IT)

| Element | Detail |
|---------|--------|
| **Technique(s)** | [ATT&CK for ICS technique IDs and names] |
| **Adversary Action** | [What the adversary does at this stage] |
| **Required Access** | [e.g., "Internet-facing VPN, compromised credentials"] |
| **Detection Rule(s)** | [Existing detection coverage] |
| **Coverage Status** | ☐ Covered ☐ Partial ☐ Gap |
| **Gap Description** | [If gap — what is missing?] |

### Level 4–5 → IDMZ (Level 3.5)

| Element | Detail |
|---------|--------|
| **Technique(s)** | |
| **Adversary Action** | |
| **Required Access** | |
| **Detection Rule(s)** | [e.g., UC-ICS-003, UC-ICS-009] |
| **Coverage Status** | ☐ Covered ☐ Partial ☐ Gap |
| **Gap Description** | |

### IDMZ → Level 3 (Site Operations)

| Element | Detail |
|---------|--------|
| **Technique(s)** | |
| **Adversary Action** | |
| **Required Access** | |
| **Detection Rule(s)** | [e.g., UC-ICS-009, UC-ICS-010] |
| **Coverage Status** | ☐ Covered ☐ Partial ☐ Gap |
| **Gap Description** | |

### Level 3 → Level 2 (Control Network)

| Element | Detail |
|---------|--------|
| **Technique(s)** | |
| **Adversary Action** | |
| **Required Access** | |
| **Detection Rule(s)** | [e.g., UC-ICS-001] |
| **Coverage Status** | ☐ Covered ☐ Partial ☐ Gap |
| **Gap Description** | |

### Level 2 → Level 1/0 (Controller / Physical Process)

| Element | Detail |
|---------|--------|
| **Technique(s)** | |
| **Adversary Action** | |
| **Required Access** | |
| **Detection Rule(s)** | [e.g., UC-ICS-002, UC-ICS-005/006/007] |
| **Coverage Status** | ☐ Covered ☐ Partial ☐ Gap |
| **Gap Description** | |

---

## DETECTION COVERAGE SUMMARY

| Attack Path Stage | Total Techniques | Covered | Partial | Gaps | Priority Gaps |
|-------------------|-----------------|---------|---------|------|---------------|
| External → L4-5 | | | | | |
| L4-5 → IDMZ | | | | | |
| IDMZ → L3 | | | | | |
| L3 → L2 | | | | | |
| L2 → L1/0 | | | | | |
| **TOTAL** | | | | | |

---

## PRIORITY ACTIONS

| Priority | Gap | Recommended Action | Owner | Target Date |
|----------|-----|-------------------|-------|-------------|
| 1 | | ☐ Detection Rule ☐ Hunting Query ☐ Telemetry ☐ Architecture | | |
| 2 | | ☐ Detection Rule ☐ Hunting Query ☐ Telemetry ☐ Architecture | | |
| 3 | | ☐ Detection Rule ☐ Hunting Query ☐ Telemetry ☐ Architecture | | |

---

## REFERENCE SCENARIOS

### Scenario A: The Patient Pre-Positioner (Volt Typhoon / VOLTZITE)
- **Profile**: State-sponsored, long dwell time, living-off-the-land
- **Stage 1**: Compromised VPN → credential harvesting → LOTL lateral movement → IDMZ access → OT documentation exfiltration
- **Stage 2**: Dormant / pre-positioned — no ICS manipulation observed yet
- **Key Tests**: Credential monitoring, behavioural analytics, IDMZ logging, file share access monitoring

### Scenario B: The Protocol Manipulator (Seashell Blizzard / ELECTRUM, CHERNOVITE)
- **Profile**: State-sponsored, ICS protocol expertise, process manipulation
- **Stage 1**: EWS compromise → legitimate engineering tools for PLC access
- **Stage 2**: Logic download → analysis → modified logic upload → process manipulation → SIS targeting
- **Key Tests**: UC-ICS-001, UC-ICS-002, firmware change hunting, SIS monitoring

### Scenario C: The Hacktivist Opportunist (Storm-0784 / BAUXITE, CARR)
- **Profile**: Ideologically motivated, low sophistication, high speed
- **Stage 1**: Internet-exposed HMI discovery → default credential authentication
- **Stage 2**: Immediate setpoint manipulation via HMI interface
- **Key Tests**: Internet-facing asset monitoring, default credential detection, HMI access logging
