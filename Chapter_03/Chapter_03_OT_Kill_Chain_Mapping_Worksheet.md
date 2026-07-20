# OT Kill Chain Mapping Worksheet
# ================================================================
# Description: Two-page worksheet for mapping a specific threat
#   actor's known TTPs to the ICS Cyber Kill Chain stages, then
#   assessing current detection coverage against each stage.
#   Includes a gap identification section that feeds directly into
#   the detection engineering backlog.
#
# Reference: Assante, M.J. and Lee, R.M. (2015). "The Industrial
#   Control System Cyber Kill Chain." SANS Institute.
#   https://www.sans.org/white-papers/36297/
#
# Usage: Complete one worksheet per threat actor or per incident
#   scenario. Use the gap analysis output to prioritise detection
#   engineering and hunting operations.
# ================================================================

## THREAT ACTOR / SCENARIO IDENTIFICATION

- **Threat Actor**: [Microsoft naming — e.g., "Volt Typhoon"]
- **Dragos Alias**: [e.g., "VOLTZITE"]
- **Other Aliases**: [e.g., "Bronze Silhouette, Vanguard Panda"]
- **Target Sectors**: [e.g., Energy, Water, Communications]
- **Motivation**: [Espionage / Pre-positioning / Disruption / Financial]
- **Assessment Date**: [Date of this analysis]
- **Analyst**: [Name]

---

## STAGE 1: IT INTRUSION AND OT ACCESS

Map the threat actor's known or assessed techniques for each phase of Stage 1.

### 1.1 Initial Access

| ATT&CK Technique | Technique ID | Evidence / Intelligence Source | Detection Rule | Coverage |
|-------------------|-------------|-------------------------------|----------------|----------|
| [e.g., Spear-Phishing Attachment] | T0865 | [e.g., CISA AA24-038A] | [e.g., Email gateway, EDR] | ☐ Full ☐ Partial ☐ None |
| [e.g., Exploitation of Remote Services] | T0866 | | | ☐ Full ☐ Partial ☐ None |
| [e.g., Supply Chain Compromise] | T0862 | | | ☐ Full ☐ Partial ☐ None |
| | | | | ☐ Full ☐ Partial ☐ None |

### 1.2 Execution and Persistence

| ATT&CK Technique | Technique ID | Evidence / Intelligence Source | Detection Rule | Coverage |
|-------------------|-------------|-------------------------------|----------------|----------|
| [e.g., Command-Line Interface] | T0807 | | | ☐ Full ☐ Partial ☐ None |
| [e.g., Scripting] | T0853 | | | ☐ Full ☐ Partial ☐ None |
| | | | | ☐ Full ☐ Partial ☐ None |

### 1.3 Credential Access

| ATT&CK Technique | Technique ID | Evidence / Intelligence Source | Detection Rule | Coverage |
|-------------------|-------------|-------------------------------|----------------|----------|
| [e.g., Valid Accounts] | T0859 | | | ☐ Full ☐ Partial ☐ None |
| [e.g., Brute Force] | T0812 | | [UC-ICS-004] | ☐ Full ☐ Partial ☐ None |
| | | | | ☐ Full ☐ Partial ☐ None |

### 1.4 Lateral Movement and IT/OT Boundary Traversal

| ATT&CK Technique | Technique ID | Evidence / Intelligence Source | Detection Rule | Coverage |
|-------------------|-------------|-------------------------------|----------------|----------|
| [e.g., Remote Services] | T0886 | | [UC-ICS-003] | ☐ Full ☐ Partial ☐ None |
| [e.g., Lateral Tool Transfer] | T0867 | | | ☐ Full ☐ Partial ☐ None |
| | | | | ☐ Full ☐ Partial ☐ None |

### 1.5 Discovery and Collection (Pre-OT)

| ATT&CK Technique | Technique ID | Evidence / Intelligence Source | Detection Rule | Coverage |
|-------------------|-------------|-------------------------------|----------------|----------|
| [e.g., Network Connection Enumeration] | T0840 | | | ☐ Full ☐ Partial ☐ None |
| [e.g., Remote System Discovery] | T0846 | | | ☐ Full ☐ Partial ☐ None |
| | | | | ☐ Full ☐ Partial ☐ None |

---

## STAGE 2: ICS ATTACK DEVELOPMENT AND EXECUTION

### 2.1 OT Discovery and Reconnaissance

| ATT&CK Technique | Technique ID | Evidence / Intelligence Source | Detection Rule | Coverage |
|-------------------|-------------|-------------------------------|----------------|----------|
| [e.g., Remote System Information Discovery] | T0888 | | | ☐ Full ☐ Partial ☐ None |
| [e.g., Network Connection Enumeration] | T0840 | | [UC-ICS-008] | ☐ Full ☐ Partial ☐ None |
| [e.g., Monitor Process State] | T0801 | | | ☐ Full ☐ Partial ☐ None |
| | | | | ☐ Full ☐ Partial ☐ None |

### 2.2 Control System Manipulation

| ATT&CK Technique | Technique ID | Evidence / Intelligence Source | Detection Rule | Coverage |
|-------------------|-------------|-------------------------------|----------------|----------|
| [e.g., Modify Controller Tasking] | T0821 | | [UC-ICS-007] | ☐ Full ☐ Partial ☐ None |
| [e.g., Unauthorised Command Message] | T0855 | | [UC-ICS-002] | ☐ Full ☐ Partial ☐ None |
| [e.g., Manipulation of Control] | T0831 | | | ☐ Full ☐ Partial ☐ None |
| [e.g., Modify Alarm Settings] | T0838 | | | ☐ Full ☐ Partial ☐ None |
| | | | | ☐ Full ☐ Partial ☐ None |

### 2.3 Impact

| ATT&CK Technique | Technique ID | Evidence / Intelligence Source | Detection Rule | Coverage |
|-------------------|-------------|-------------------------------|----------------|----------|
| [e.g., Loss of Availability] | T0826 | | | ☐ Full ☐ Partial ☐ None |
| [e.g., Loss of Control] | T0827 | | | ☐ Full ☐ Partial ☐ None |
| [e.g., Loss of View] | T0829 | | | ☐ Full ☐ Partial ☐ None |
| [e.g., Damage to Property] | T0879 | | | ☐ Full ☐ Partial ☐ None |
| | | | | ☐ Full ☐ Partial ☐ None |

---

## DETECTION COVERAGE SUMMARY

### Coverage by Kill Chain Stage

| Kill Chain Stage | Total Techniques | Full Coverage | Partial Coverage | No Coverage | Coverage % |
|-----------------|-----------------|---------------|------------------|-------------|-----------|
| 1.1 Initial Access | | | | | |
| 1.2 Execution/Persistence | | | | | |
| 1.3 Credential Access | | | | | |
| 1.4 Lateral Movement / Boundary | | | | | |
| 1.5 Discovery/Collection | | | | | |
| 2.1 OT Reconnaissance | | | | | |
| 2.2 Control Manipulation | | | | | |
| 2.3 Impact | | | | | |
| **TOTAL** | | | | | |

---

## GAP ANALYSIS AND PRIORITISATION

### Critical Gaps (No Coverage on High-Impact Techniques)

| Priority | Technique | Kill Chain Stage | Required Telemetry | Recommended Action | Owner | Target Date |
|----------|----------|-----------------|-------------------|-------------------|-------|-------------|
| 1 | | | | ☐ New Detection Rule ☐ Hunting Query ☐ Telemetry Deployment | | |
| 2 | | | | ☐ New Detection Rule ☐ Hunting Query ☐ Telemetry Deployment | | |
| 3 | | | | ☐ New Detection Rule ☐ Hunting Query ☐ Telemetry Deployment | | |
| 4 | | | | ☐ New Detection Rule ☐ Hunting Query ☐ Telemetry Deployment | | |
| 5 | | | | ☐ New Detection Rule ☐ Hunting Query ☐ Telemetry Deployment | | |

### Hunting Hypotheses Generated

| Hypothesis | Source Technique | Data Sources Required | Priority |
|-----------|-----------------|----------------------|----------|
| | | | |
| | | | |
| | | | |

---

## NOTES AND INTELLIGENCE GAPS

- **Information we need**: [What additional intelligence would improve this assessment?]
- **Assumptions made**: [Where did we lack specific intelligence and make assumptions?]
- **Review date**: [When should this worksheet be reviewed for updated intelligence?]
