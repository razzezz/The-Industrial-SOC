# Attack Path Documentation Template

**Book Reference:** Chapter 5 — Defensible Architecture and Segmentation  
**Purpose:** Document attack paths from initial access to crown jewel process impact, with detection coverage assessment at each stage.  
**Usage:** Complete one template per crown jewel process. Use for segmentation prioritisation and detection gap analysis.

---

## Crown Jewel Process

| Field | Value |
|-------|-------|
| **Process Name** | |
| **Crown Jewel Tier** | Tier 1 / Tier 2 / Tier 3 |
| **Location / Site** | |
| **Process Owner (OT)** | |
| **Impact if Compromised** | |

---

## Attack Path Stages

### Stage 1 — Enterprise Compromise (Level 4–5)

**Objective:** Establish foothold in enterprise network and identify path to OT environment.

| Element | Detail |
|---------|--------|
| **Likely Initial Access Vectors** | ☐ Phishing ☐ Credential theft ☐ Exploited internet-facing service ☐ Supply chain compromise ☐ Insider threat ☐ Other: ______ |
| **Enterprise Systems on Path** | List enterprise systems that provide onward access toward OT (e.g., AD, VPN servers, email): |
| **Relevant ATT&CK Techniques** | e.g., T1566 (Phishing), T1078 (Valid Accounts), T1133 (External Remote Services) |

**Detection Coverage at Stage 1:**

| Detection Capability | Status | Rule / Use Case Reference | Notes |
|---------------------|:---:|---|---|
| Email / phishing detection | ☐ Active ☐ Gap | | |
| EDR on enterprise endpoints | ☐ Active ☐ Gap | | |
| Identity-based detections (ITDR) | ☐ Active ☐ Gap | | |
| Network anomaly detection (C2) | ☐ Active ☐ Gap | | |
| VPN / remote access monitoring | ☐ Active ☐ Gap | | |

---

### Stage 2 — IDMZ Traversal (Level 3.5)

**Objective:** Transition from enterprise network into OT boundary services.

| Element | Detail |
|---------|--------|
| **IDMZ Components on Path** | List specific IDMZ systems the adversary would target (jump servers, historian replicas, patch relays, remote access gateways): |
| **Boundary Firewalls** | IT-facing FW: __________ OT-facing FW: __________ |
| **Known Legitimate Cross-Boundary Traffic** | Protocols and services permitted through IDMZ: |
| **Relevant ATT&CK for ICS Techniques** | e.g., T0886 (Remote Services), T0822 (External Remote Services), T0859 (Valid Accounts) |

**Detection Coverage at Stage 2:**

| Detection Capability | Status | Rule / Use Case Reference | Notes |
|---------------------|:---:|---|---|
| Firewall log analysis (both boundaries) | ☐ Active ☐ Gap | | |
| IT/OT boundary traversal detection | ☐ Active ☐ Gap | UC-ICS-003 | |
| Jump server authentication monitoring | ☐ Active ☐ Gap | UC-ICS-011 | |
| Remote access correlation | ☐ Active ☐ Gap | UC-ICS-009 | |
| Network IDS at IDMZ (Zeek/Suricata) | ☐ Active ☐ Gap | UC-ICS-012 | |
| Vendor session anomaly detection | ☐ Active ☐ Gap | UC-ICS-010 | |

---

### Stage 3 — Operational Network Access (Level 3)

**Objective:** Access site operations systems and pivot toward supervisory control.

| Element | Detail |
|---------|--------|
| **Level 3 Systems on Path** | List historians, MES, batch systems the adversary would target: |
| **Network Segments** | VLANs / subnets traversed: |
| **Relevant ATT&CK for ICS Techniques** | e.g., T0846 (Remote System Discovery), T0859 (Valid Accounts) |

**Detection Coverage at Stage 3:**

| Detection Capability | Status | Rule / Use Case Reference | Notes |
|---------------------|:---:|---|---|
| EDR on Level 3 systems | ☐ Active ☐ Gap | | |
| Windows authentication monitoring | ☐ Active ☐ Gap | | |
| Network monitoring (L3/L3.5 boundary) | ☐ Active ☐ Gap | | |
| Historian access anomaly detection | ☐ Active ☐ Gap | | |

---

### Stage 4 — Supervisory Control Access (Level 2)

**Objective:** Access HMIs, SCADA servers, or engineering workstations to observe and interact with the process.

| Element | Detail |
|---------|--------|
| **Level 2 Systems on Path** | List HMIs, SCADA servers, engineering workstations: |
| **Connectivity to Level 1** | Protocols used to communicate with controllers (Modbus, DNP3, S7Comm, EtherNet/IP, OPC-UA): |
| **Relevant ATT&CK for ICS Techniques** | e.g., T0843 (Program Download), T0821 (Modify Controller Tasking) |

**Detection Coverage at Stage 4:**

| Detection Capability | Status | Rule / Use Case Reference | Notes |
|---------------------|:---:|---|---|
| EDR on Level 2 systems (detect-only) | ☐ Active ☐ Gap | | |
| Engineering workstation logon monitoring | ☐ Active ☐ Gap | | |
| Network monitoring (L2/L3 boundary) | ☐ Active ☐ Gap | | |
| ICS protocol monitoring (Zeek/ICSNPP) | ☐ Active ☐ Gap | | |
| Write command outside maintenance window | ☐ Active ☐ Gap | UC-ICS-002 | |

---

### Stage 5 — Controller Manipulation (Level 1–0)

**Objective:** Modify PLC logic, send unauthorised commands, or disable safety systems.

| Element | Detail |
|---------|--------|
| **Target Controllers** | List specific PLCs, RTUs, DCS controllers for this crown jewel: |
| **Safety System** | SIS present? ☐ Yes ☐ No — If yes, type: __________ |
| **Physical Consequence** | What happens if the controller is manipulated? |
| **Relevant ATT&CK for ICS Techniques** | e.g., T0839 (Module Firmware), T0831 (Manipulation of Control), T0836 (Modify Parameter) |

**Detection Coverage at Stage 5:**

| Detection Capability | Status | Rule / Use Case Reference | Notes |
|---------------------|:---:|---|---|
| Unauthorised ICS protocol communication | ☐ Active ☐ Gap | UC-ICS-001 | |
| Modbus diagnostic function abuse | ☐ Active ☐ Gap | UC-ICS-005 | |
| DNP3 unauthorised operations | ☐ Active ☐ Gap | UC-ICS-006 | |
| Modbus function code scanning | ☐ Active ☐ Gap | UC-ICS-008 | |
| Safety zone access monitoring | ☐ Active ☐ Gap | | |

---

## Gap Summary

| Stage | Total Detection Capabilities | Active | Gaps | Coverage % |
|:---:|:---:|:---:|:---:|:---:|
| 1 — Enterprise | | | | |
| 2 — IDMZ | | | | |
| 3 — Operations | | | | |
| 4 — Supervisory | | | | |
| 5 — Controller | | | | |
| **Overall** | | | | |

---

## Priority Remediation Actions

| Priority | Gap Description | Remediation Action | Effort | Target Date | Owner |
|:---:|---|---|---|---|---|
| P1 | | | Low / Med / High | | |
| P2 | | | | | |
| P3 | | | | | |

---

## Review

| Completed By | Date | Reviewed By | Date |
|-------------|------|------------|------|
| | | | |

**Next Review Date:** _______________
