# Threat-to-Detection Priority Matrix
# ================================================================
# Description: Maps documented threat actor techniques to the existing 
#   OT detection library, identifying covered techniques and gaps.
#   Used to prioritise new detection rule development based on the 
#   intersection of "technique used by adversaries targeting your 
#   sector" and "technique not covered by current detections."
#
# Usage: Review quarterly alongside the ATTCK_ICS_Coverage_Assessment.
#   Update when new threat intelligence changes the actor profiles or 
#   when new detection rules close identified gaps.
#
# Last Updated: [Date]
# ================================================================

## How to Use This Matrix

1. Identify which threat actors are relevant to your sector (reference Chapter 3)
2. Review the techniques listed for those actors
3. Check the "Detection Coverage" column for each technique
4. Techniques marked "GAP" for actors relevant to your sector are your highest-priority development targets
5. Techniques marked "PARTIAL" warrant review to determine if existing coverage is sufficient

---

## Volt Typhoon (VOLTZITE)

**Attribution:** People's Republic of China state-sponsored
**Target Sectors:** Energy, Water, Communications, Transportation
**Operational Profile:** Patient pre-positioning, living-off-the-land, extended dwell times (months to years). In 2025 escalated to Stage 2 ICS Kill Chain capability with direct OT device interaction.

| ATT&CK for ICS Technique | Technique ID | Observed Tradecraft | Detection Rule | Coverage Status | Priority |
|---|---|---|---|---|---|
| Valid Accounts | T0859 | Compromised VPN and gateway credentials for initial access and lateral movement | UC-ICS-004 (credential brute force), UC-ICS-009 (cross-domain lateral movement) | PARTIAL — covers brute force and remote access pivot, does not cover credential reuse from extracted credentials | HIGH |
| Remote Services | T0886 | RDP, SSH through legitimate remote access infrastructure to engineering workstations | UC-ICS-003 (IT/OT boundary traversal), UC-ICS-009 | COVERED | — |
| External Remote Services | T0822 | VPN, cellular gateway web interfaces (TCP/9191, TCP/9443) for initial OT access | UC-ICS-009 (remote access correlation) | PARTIAL — covers VPN gateway authentication, does not cover cellular gateway web interface access | HIGH |
| Network Connection Enumeration | T0840 | Native Windows tools (arp, netstat, ping, ipconfig) on compromised engineering workstations | UC-ICS-008 (Modbus function code scan) | PARTIAL — UC-ICS-008 covers Modbus-specific reconnaissance, does not cover host-based discovery tool execution | HIGH |
| Remote System Discovery | T0846 | Systematic enumeration of OT network from compromised workstations | UC-ICS-008 | PARTIAL — same gap as T0840 | HIGH |
| Automated Collection | T0802 | Extraction of PLC configuration files and alarm data from engineering workstations | — | GAP — no detection for configuration file access on engineering workstations | CRITICAL |
| Standard Application Layer Protocol | T0869 | Uses legitimate protocols (SSH, HTTP, TLS) for C2, blending with normal traffic | — | GAP — living-off-the-land C2 via standard protocols is extremely difficult to detect without behavioural analytics | MEDIUM |
| Manipulation of Control | T0831 | Investigating operational thresholds to determine what would trigger process shutdowns | UC-ICS-002 (write command outside maintenance) | PARTIAL — covers write commands but not read-based reconnaissance of alarm thresholds | HIGH |

**Volt Typhoon Priority Gaps:**
1. CRITICAL: T0802 — Configuration file and alarm data extraction from engineering workstations
2. HIGH: T0859 — Credential reuse detection (not brute force, but use of previously extracted credentials)
3. HIGH: T0840/T0846 — Host-based discovery tool execution on engineering workstations (requires EDR/Sysmon telemetry)
4. HIGH: T0822 — Cellular gateway and edge device authentication monitoring

---

## Seashell Blizzard (ELECTRUM)

**Attribution:** Russian GRU (Unit 74455, Sandworm)
**Target Sectors:** Energy (primary), Government, Transportation, critical infrastructure broadly
**Operational Profile:** ICS-specific malware development (Industroyer, Industroyer2, PathWiper), destructive intent, escalation from Ukraine into European supply chain. KAMACITE serves as access development team.

| ATT&CK for ICS Technique | Technique ID | Observed Tradecraft | Detection Rule | Coverage Status | Priority |
|---|---|---|---|---|---|
| Unauthorised Command Message | T0855 | Industroyer2: crafted IEC 61850 and IEC 60870-5-104 commands to open circuit breakers | UC-ICS-002 (write command outside maintenance), UC-ICS-006 (DNP3 operations) | PARTIAL — covers Modbus/DNP3 write commands, does not cover IEC 61850/60870-5-104 protocols | HIGH |
| Modify Controller Tasking | T0821 | Upload modified control logic to PLCs via native engineering protocols | UC-ICS-007 (CIP programme operations) | PARTIAL — covers CIP environments, does not cover Siemens S7Comm or IEC protocol environments without additional Suricata rules | HIGH |
| Device Restart/Shutdown | T0816 | DNP3 and Modbus diagnostic commands to restart or disable controllers | UC-ICS-005 (Modbus diagnostics), UC-ICS-006 (DNP3 operations) | COVERED | — |
| Data Destruction | T0809 | PathWiper: MBR corruption and NTFS structure destruction across all mounted volumes | — | GAP — requires EDR-based detection of MBR access and systematic volume enumeration | CRITICAL |
| Remote System Discovery | T0846 | KAMACITE: systematic reconnaissance of internet-exposed Smart HMIs, VFDs, power meters, gateways | UC-ICS-008 (Modbus function code scan) | PARTIAL — covers internal Modbus scanning, does not cover external reconnaissance of internet-exposed devices | MEDIUM |
| Supply Chain Compromise | T0862 | Compromise of vendor and integrator access for initial OT access | — | GAP — requires vendor access behavioural baselining beyond current UC-ICS-009 capability | HIGH |
| Block Reporting Message | T0804 | DNP3 disable unsolicited messages to blind SCADA master | UC-ICS-006 (DNP3 disable unsolicited) | COVERED | — |
| Denial of Service | T0814 | Protocol-level DoS against controllers during destructive operations | UC-ICS-005 (Modbus diagnostics) | PARTIAL — covers Modbus FC8 DoS, does not cover protocol-flooding or application-layer DoS | MEDIUM |

**Seashell Blizzard Priority Gaps:**
1. CRITICAL: T0809 — Wiper malware detection (PathWiper MBR corruption, systematic volume destruction)
2. HIGH: T0855/T0821 — IEC 61850 and IEC 60870-5-104 protocol coverage (requires additional Suricata/Zeek parsers for utility environments)
3. HIGH: T0862 — Vendor/supply chain access behavioural anomaly detection

---

## Storm-0784 (BAUXITE)

**Attribution:** Iran-linked (CyberAv3ngers)
**Target Sectors:** Water (primary), Energy
**Operational Profile:** Exploitation of internet-accessible OT devices, default credentials, direct HMI manipulation. Less sophisticated but shorter attack path (begins at Stage 2).

| ATT&CK for ICS Technique | Technique ID | Observed Tradecraft | Detection Rule | Coverage Status | Priority |
|---|---|---|---|---|---|
| Default Credentials | T0812 | Authentication to HMIs and PLCs using factory-default passwords | UC-ICS-004 (credential brute force) | PARTIAL — detects brute force pattern but not single successful login with default credentials | HIGH |
| Exploitation of Remote Services | T0866 | Direct exploitation of internet-facing HMI web interfaces and management consoles | — | GAP — requires detection of authentication from external/unexpected IP ranges to OT web interfaces | CRITICAL |
| Valid Accounts | T0859 | Use of compromised or default credentials for ongoing access | UC-ICS-004, UC-ICS-009 | PARTIAL — covers brute force and remote access pivot patterns | MEDIUM |
| Modify Parameter | T0836 | Setpoint manipulation through HMI interfaces (e.g., changing chemical dosing parameters) | UC-ICS-002 (write command outside maintenance) | PARTIAL — covers protocol-level write commands, does not cover HMI application-layer setpoint changes | HIGH |
| Manipulation of View | T0832 | Altering HMI displays to show false process values to operators | — | GAP — requires HMI application-level monitoring or process value cross-validation | HIGH |
| Loss of Control | T0827 | Disabling operator control through HMI manipulation or credential lockout | — | GAP — requires correlation of authentication failures with process anomalies | MEDIUM |

**Storm-0784 Priority Gaps:**
1. CRITICAL: T0866 — External-to-OT authentication detection (internet-facing device monitoring)
2. HIGH: T0812 — Default credential usage detection (single successful logon, not brute force pattern)
3. HIGH: T0836 — HMI application-layer setpoint change detection
4. HIGH: T0832 — HMI display manipulation detection

---

## CHERNOVITE

**Attribution:** State-sponsored (specific nation-state attribution varies by source)
**Target Sectors:** Energy, Manufacturing (targets Schneider Electric and Omron controllers)
**Operational Profile:** PIPEDREAM/INCONTROLLER modular toolkit using native ICS protocols. Designed for broad applicability across multiple controller vendors.

| ATT&CK for ICS Technique | Technique ID | Observed Tradecraft | Detection Rule | Coverage Status | Priority |
|---|---|---|---|---|---|
| Modify Controller Tasking | T0821 | PIPEDREAM modules upload modified logic to Schneider Modicon and Omron NX/NJ controllers via Modbus and FINS | UC-ICS-002 (write commands), UC-ICS-007 (CIP operations) | PARTIAL — covers Modbus write and CIP, does not cover Omron FINS protocol operations | HIGH |
| Programme Upload | T0845 | Extraction of running PLC logic for analysis before modification | UC-ICS-007 (CIP programme upload) | PARTIAL — covers CIP environments only | HIGH |
| Remote Services | T0886 | Uses OPC UA for interaction with automation devices | UC-ICS-001 (unauthorised ICS protocol communication) | COVERED — UC-ICS-001 includes OPC UA in the monitored protocol list | — |
| Change Operating Mode | T0858 | Switches controllers between Run and Programme mode to enable logic modification | UC-ICS-007 (CIP change operating mode) | PARTIAL — covers CIP/Rockwell environments, does not cover Schneider or Omron mode change commands | HIGH |
| Manipulation of Control | T0831 | Direct register writes to alter process setpoints and outputs | UC-ICS-002 (write command outside maintenance) | COVERED | — |
| Module Firmware | T0839 | Firmware modification for persistence (demonstrated capability) | — | GAP — addressed by Hunt-ICS-001 in Chapter 9 but no automated detection rule | MEDIUM |

**CHERNOVITE Priority Gaps:**
1. HIGH: T0821/T0845/T0858 — Schneider-specific and Omron FINS protocol coverage (requires additional Suricata rules and Zeek parsers)
2. MEDIUM: T0839 — Automated firmware change detection (currently hunt-only coverage via Chapter 9)

---

## Gap Prioritisation Summary

### CRITICAL Gaps (address immediately)
| Gap | Threat Actor(s) | Recommended Action |
|---|---|---|
| Configuration file extraction from engineering workstations (T0802) | Volt Typhoon | Develop EDR-based detection for access to PLC project files and configuration exports |
| Wiper malware detection (T0809) | Seashell Blizzard | Develop EDR-based detection for MBR access patterns and systematic volume enumeration |
| External-to-OT authentication (T0866) | Storm-0784 | Develop detection for authentication to OT devices from external/unexpected IP ranges |

### HIGH Gaps (address within next quarter)
| Gap | Threat Actor(s) | Recommended Action |
|---|---|---|
| Host-based discovery tool execution on OT systems (T0840, T0846) | Volt Typhoon | Develop EDR/Sysmon detection for network discovery tools on engineering workstations |
| Credential reuse after extraction (T0859) | Volt Typhoon | Develop CTI-driven correlation: credential extraction tool execution → OT system authentication (see Chapter 10 CTI-ICS-001) |
| IEC 61850/60870-5-104 protocol monitoring (T0855, T0821) | Seashell Blizzard | Deploy additional Suricata rules and Zeek parsers for utility-specific protocols |
| Vendor access behavioural anomaly (T0862) | Seashell Blizzard | Develop behavioural baseline for vendor access patterns and detect deviations |
| Default credential single-login detection (T0812) | Storm-0784 | Develop detection for successful authentication using known-default credential patterns |
| HMI application-layer setpoint changes (T0836) | Storm-0784 | Develop detection leveraging HMI application logs or process historian cross-validation |
| Omron FINS and Schneider-specific protocol coverage (T0821, T0845) | CHERNOVITE | Deploy FINS protocol Suricata rules; extend Zeek parsers for Schneider protocols |

### MEDIUM Gaps (address within next two quarters)
| Gap | Threat Actor(s) | Recommended Action |
|---|---|---|
| Living-off-the-land C2 via standard protocols (T0869) | Volt Typhoon | Long-term: behavioural analytics (Chapter 16 ML capability). Short-term: hunting (Chapter 9) |
| Protocol-flooding DoS (T0814) | Seashell Blizzard | Develop Zeek-based volumetric anomaly detection |
| Automated firmware change detection (T0839) | CHERNOVITE | Promote Hunt-ICS-001 from Chapter 9 to scheduled detection rule |
| HMI display manipulation (T0832) | Storm-0784 | Requires HMI application-level monitoring; long-term capability |
