# Attack Path to Crown Jewels Mapping Worksheet

## Purpose

This worksheet provides a structured format for documenting the complete attack path from initial access to a crown jewel asset. For each traversal between Purdue levels, it captures the current monitoring status and identifies gaps. Completed worksheets directly inform the telemetry deployment priorities in Chapter 7.

---

## Instructions

1. Select one crown jewel process (start with the highest-tier crown jewel).
2. Identify the crown jewel asset(s) at the lowest Purdue level involved in that process.
3. Work **upward** through the Purdue Model, documenting each network traversal.
4. At each stage, assess the current monitoring capability.
5. Gaps identified become the priority deployment list.

Complete one worksheet per crown jewel process.

---

## Crown Jewel Process Summary

| Field | Value |
|-------|-------|
| **Process Name** | |
| **Crown Jewel Tier** | ☐ Tier 1 ☐ Tier 2 ☐ Tier 3 |
| **Crown Jewel Asset(s)** | *(List asset IDs from OT_AssetRegister)* |
| **Lowest Purdue Level** | ☐ L0 ☐ L1 ☐ L2 |
| **Site / Facility** | |
| **Engineering Owner** | |
| **Assessment Date** | |
| **Assessed By** | |

---

## Stage 1: Crown Jewel Zone (Level 0–1)

*The physical process layer. PLCs, RTUs, DCS controllers, SIS, and field devices.*

| Item | Details |
|------|---------|
| **Assets at this level** | *(List IPs, hostnames, device types)* |
| **Protocols in use** | ☐ Modbus ☐ DNP3 ☐ S7Comm ☐ EtherNet/IP ☐ Profinet ☐ OPC-UA ☐ BACnet ☐ Other: ___ |
| **Communication partners** | *(Which L2 devices communicate with these assets?)* |
| **Network segmentation** | ☐ Dedicated VLAN ☐ Shared with L2 ☐ Flat network ☐ Unknown |

### Monitoring Assessment — Level 0–1

| Monitoring Capability | Status | Details |
|----------------------|--------|---------|
| Passive network sensor (Zeek/Suricata) on this segment | ☐ Yes ☐ No ☐ Partial | |
| ICS protocol parsing (Modbus/DNP3/S7Comm function codes visible) | ☐ Yes ☐ No ☐ Partial | |
| Communication baseline established for crown jewel assets | ☐ Yes ☐ No ☐ In Progress | |
| EDR/endpoint agent on any L0–L1 device | ☐ N/A (not possible) | |
| UC-ICS-001 (Unauthorised ICS Protocol Communication) deployed | ☐ Yes ☐ No | |
| UC-ICS-005/006 (Protocol-specific Suricata rules) deployed | ☐ Yes ☐ No | |

**Gaps identified:** _____________________________________________

---

## Stage 2: Supervisory Control Zone (Level 2)

*HMIs, SCADA servers, engineering workstations that interact with the crown jewel.*

| Item | Details |
|------|---------|
| **Assets at this level** | *(List IPs, hostnames, device types)* |
| **Operating systems** | ☐ Windows 11/10 ☐ Windows 7 ☐ Windows XP ☐ Linux ☐ Other: ___ |
| **How L2 connects to L1** | ☐ Direct L2 switch ☐ Firewall-separated ☐ Routed ☐ Unknown |
| **Authentication method** | ☐ AD domain ☐ Local accounts ☐ Shared accounts ☐ None |

### Monitoring Assessment — Level 2

| Monitoring Capability | Status | Details |
|----------------------|--------|---------|
| Windows Event Log forwarding to SIEM | ☐ Yes ☐ No ☐ Partial | |
| Sysmon deployed | ☐ Yes ☐ No | |
| EDR deployed (detect mode) | ☐ Yes ☐ No | |
| EDR deployed (block mode) | ☐ Yes ☐ No | |
| Authentication logs forwarded to SIEM | ☐ Yes ☐ No ☐ Partial | |
| UC-ICS-002 (Write Command Outside Maintenance) deployed | ☐ Yes ☐ No | |
| UC-ICS-004 (Credential Brute Force OT) deployed | ☐ Yes ☐ No | |

**Gaps identified:** _____________________________________________

---

## Stage 3: Traversal from Level 2 to Level 3

*The boundary between supervisory control and site operations.*

| Item | Details |
|------|---------|
| **Boundary type** | ☐ Firewall ☐ Router ACL ☐ VLAN only ☐ No boundary ☐ Unknown |
| **Firewall logs forwarded to SIEM** | ☐ Yes ☐ No ☐ N/A |
| **Traffic permitted** | *(What protocols/ports are allowed through?)* |
| **Known bypasses** | *(Any direct connections that skip the boundary?)* |

### Monitoring Assessment — L2/L3 Boundary

| Monitoring Capability | Status | Details |
|----------------------|--------|---------|
| Firewall/ACL logs in SIEM | ☐ Yes ☐ No ☐ N/A | |
| Network sensor (Zeek/Suricata) at boundary | ☐ Yes ☐ No | |
| NetFlow/IPFIX from boundary device | ☐ Yes ☐ No | |

**Gaps identified:** _____________________________________________

---

## Stage 4: Site Operations Zone (Level 3)

*Historians, MES, batch management, operational reporting.*

| Item | Details |
|------|---------|
| **Assets at this level** | *(List IPs, hostnames, device types)* |
| **Historian present** | ☐ Yes — hostname: ___ ☐ No |
| **Data replication to IDMZ** | ☐ Yes ☐ No ☐ Unknown |
| **Connection to L2** | ☐ Direct ☐ Via firewall ☐ Unknown |

### Monitoring Assessment — Level 3

| Monitoring Capability | Status | Details |
|----------------------|--------|---------|
| Windows Event Log forwarding to SIEM | ☐ Yes ☐ No ☐ Partial | |
| EDR deployed | ☐ Yes ☐ No | |
| Historian access logging | ☐ Yes ☐ No | |
| Authentication logs in SIEM | ☐ Yes ☐ No | |

**Gaps identified:** _____________________________________________

---

## Stage 5: Traversal from Level 3 to IDMZ (Level 3.5)

*The critical boundary between OT and IT. The primary detection choke point.*

| Item | Details |
|------|---------|
| **IDMZ exists** | ☐ Yes ☐ No (critical gap) ☐ Partial |
| **Boundary firewall(s)** | *(OT-facing firewall model/hostname, IT-facing firewall model/hostname)* |
| **Services in IDMZ** | ☐ Historian relay ☐ Patch relay ☐ Jump server ☐ AV relay ☐ Other: ___ |
| **Remote access gateway** | ☐ Yes — type: ___ ☐ No |

### Monitoring Assessment — IDMZ

| Monitoring Capability | Status | Details |
|----------------------|--------|---------|
| OT-facing firewall logs in SIEM | ☐ Yes ☐ No | |
| IT-facing firewall logs in SIEM | ☐ Yes ☐ No | |
| Network sensor (Zeek/Suricata) at IDMZ | ☐ Yes ☐ No | |
| Jump server authentication logs in SIEM | ☐ Yes ☐ No ☐ N/A | |
| Jump server session recording | ☐ Yes ☐ No ☐ N/A | |
| UC-ICS-003 (IT/OT Boundary Traversal) deployed | ☐ Yes ☐ No | |
| UC-ICS-009 (Cross-Domain Lateral Movement) deployed | ☐ Yes ☐ No | |

**Gaps identified:** _____________________________________________

---

## Stage 6: Enterprise IT (Level 4–5) to IDMZ

*The traversal from enterprise network to the IDMZ boundary.*

| Item | Details |
|------|---------|
| **Enterprise firewall to IDMZ** | ☐ Yes ☐ No ☐ Unknown |
| **VPN termination point** | *(For remote vendor/engineer access)* |
| **Permitted connections** | *(What enterprise systems connect to the IDMZ?)* |

### Monitoring Assessment — IT/IDMZ Boundary

| Monitoring Capability | Status | Details |
|----------------------|--------|---------|
| Enterprise firewall logs in SIEM | ☐ Yes ☐ No | |
| VPN authentication logs in SIEM | ☐ Yes ☐ No | |
| IT EDR coverage on enterprise systems connecting to IDMZ | ☐ Yes ☐ No | |
| AD authentication monitoring for accounts with IDMZ access | ☐ Yes ☐ No | |

**Gaps identified:** _____________________________________________

---

## Stage 7: External Access (Internet) to Enterprise

*Initial access vectors — where the attack typically begins.*

| Item | Details |
|------|---------|
| **External-facing services** | *(VPN, web apps, email, cloud services)* |
| **MFA enforced on external access** | ☐ Yes ☐ No ☐ Partial |
| **Email security** | ☐ Yes ☐ No |

### Monitoring Assessment — External Boundary

| Monitoring Capability | Status | Details |
|----------------------|--------|---------|
| Perimeter firewall/WAF logs in SIEM | ☐ Yes ☐ No | |
| Email gateway logs in SIEM | ☐ Yes ☐ No | |
| DNS query logging | ☐ Yes ☐ No | |
| Endpoint EDR on user workstations | ☐ Yes ☐ No ☐ Partial | |

**Gaps identified:** _____________________________________________

---

## Gap Summary and Prioritisation

*List all gaps identified above. Prioritise based on proximity to the crown jewel (gaps closer to the crown jewel asset are higher priority).*

| Priority | Gap Description | Purdue Level | Remediation Action | Owner | Target Date |
|----------|----------------|-------------|-------------------|-------|------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |

---

## Summary Assessment

| Metric | Value |
|--------|-------|
| **Total Purdue level traversals in attack path** | |
| **Traversals with full monitoring** | |
| **Traversals with partial monitoring** | |
| **Traversals with no monitoring** | |
| **Monitoring coverage (%)** | |
| **Highest-priority gap** | |
| **Estimated effort to close top 3 gaps** | |
