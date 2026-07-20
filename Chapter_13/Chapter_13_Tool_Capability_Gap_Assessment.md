# Tool Capability Gap Assessment

## OT Security Capability Mapping and Gap Identification

**Assessment Date:** _______________
**Assessor(s):** _______________
**Organisation/Site:** _______________

---

## Instructions

1. For each capability in the three-tier framework, record the current tool(s) providing it.
2. Assess SIEM integration status and detection rule coverage.
3. Map ATT&CK for ICS techniques that the capability enables detection of.
4. Identify gaps — capabilities with no current tool or inadequate coverage.
5. Prioritise gaps using threat intelligence (Step 2 in Chapter 13 Practical Steps).

---

## Tier 1: Essential Capabilities

*These must be in place before investing in Tier 2 or Tier 3.*

### 1.1 EDR/ITDR (OT-Aware Endpoint Detection)

| Dimension | Current State |
|---|---|
| **Tool(s) deployed** | |
| **Purdue levels covered** | ☐ Level 4 ☐ Level 3.5 ☐ Level 3 ☐ Other: _____ |
| **Asset types covered** | ☐ Eng. Workstations ☐ HMIs ☐ SCADA Servers ☐ Historians ☐ Jump Hosts |
| **Deployment mode** | ☐ Passive/Detect ☐ Protect/Block ☐ Mixed |
| **SIEM integration** | ☐ Native connector ☐ Custom integration ☐ Not integrated |
| **Active detection rules using this data** | Count: _____ |
| **ATT&CK for ICS techniques detected** | |
| **Last rule created/updated** | Date: _____ |
| **Gap assessment** | ☐ Adequate ☐ Partial Gap ☐ Critical Gap ☐ Not Deployed |
| **Gap description** | |

### 1.2 SIEM with OT Use Cases

| Dimension | Current State |
|---|---|
| **Tool(s) deployed** | |
| **IT and OT in same instance?** | ☐ Yes ☐ No (separate) ☐ Cross-workspace |
| **ASIM normalisation active?** | ☐ Yes ☐ Partial ☐ No |
| **OT watchlists configured?** | ☐ OT_AssetRegister ☐ OT_CrownJewels ☐ OT_MaintenanceWindows |
| **OT-specific detection rules active** | Count: _____ |
| **Hunting queries for OT** | Count: _____ |
| **Automation rules for OT enrichment** | Count: _____ |
| **ATT&CK for ICS tactic coverage** | _____ / 12 tactics |
| **Gap assessment** | ☐ Adequate ☐ Partial Gap ☐ Critical Gap ☐ Not Deployed |
| **Gap description** | |

### 1.3 Passive Asset Discovery and Network Monitoring

| Dimension | Current State |
|---|---|
| **Tool(s) deployed** | |
| **Type** | ☐ Open-source (Zeek/Suricata) ☐ Commercial OT NDR ☐ Defender for IoT ☐ Hybrid |
| **Monitoring points** | ☐ IDMZ boundary ☐ Between L2-L3 ☐ Within L2 ☐ Within L1 |
| **Sites covered** | _____ / _____ total sites |
| **Crown jewel assets with network visibility** | _____ % of Tier 1 | _____ % of Tier 2 |
| **SIEM integration** | ☐ Native connector ☐ Custom (Filebeat/AMA) ☐ Not integrated |
| **ASIM parsers in place** | ☐ NetworkSession ☐ DnsEvent ☐ ICS Protocol (custom) |
| **Active detection rules using this data** | Count: _____ |
| **Gap assessment** | ☐ Adequate ☐ Partial Gap ☐ Critical Gap ☐ Not Deployed |
| **Gap description** | |

---

## Tier 2: Enhanced Detection Capabilities

### 2.1 Passive Vulnerability Management

| Dimension | Current State |
|---|---|
| **Tool(s) deployed** | |
| **Method** | ☐ Traffic-based fingerprinting ☐ Banner grabbing ☐ Vendor CVE DB ☐ None |
| **Assets with vulnerability assessment** | _____ / _____ total OT assets |
| **CVE data integrated into SIEM?** | ☐ Yes ☐ No |
| **CVE data linked to OT_AssetRegister?** | ☐ Yes ☐ No |
| **Gap assessment** | ☐ Adequate ☐ Partial Gap ☐ Critical Gap ☐ Not Deployed |
| **Gap description** | |

### 2.2 Protocol-Aware Deep Packet Inspection

| Dimension | Current State |
|---|---|
| **Tool(s) deployed** | |
| **Protocols with function-code level parsing** | |
| **Protocols with register/address level parsing** | |
| **Protocols with value-level extraction** | |
| **SIEM integration for parsed protocol data** | ☐ Yes ☐ Partial ☐ No |
| **Detection rules using deep protocol data** | Count: _____ |
| **Gap assessment** | ☐ Adequate ☐ Partial Gap ☐ Critical Gap ☐ Not Deployed |
| **Gap description** | |

---

## Tier 3: Advanced Capabilities

### 3.1 Threat Intelligence Platform

| Dimension | Current State |
|---|---|
| **Tool(s) deployed** | |
| **Type** | ☐ Dedicated TIP ☐ Sentinel built-in TI ☐ Commercial feed ☐ None |
| **STIX/TAXII exchange capability?** | ☐ Yes ☐ No |
| **IOC matching against ingested logs?** | ☐ Yes ☐ No |
| **Integration with detection rules?** | ☐ Yes ☐ No |
| **Gap assessment** | ☐ Adequate ☐ Partial Gap ☐ Critical Gap ☐ Not Deployed |
| **Gap description** | |

### 3.2 SOAR (Automation and Orchestration)

| Dimension | Current State |
|---|---|
| **Tool(s) deployed** | |
| **Type** | ☐ Sentinel native ☐ Dedicated SOAR platform ☐ None |
| **Automated enrichment active?** | ☐ Yes ☐ No |
| **Automated notification active?** | ☐ Yes ☐ No |
| **Automated containment active?** | ☐ Yes (with approval gates) ☐ Yes (without) ☐ No |
| **Human approval gates for L0-L3 actions?** | ☐ Yes ☐ No ☐ N/A |
| **Gap assessment** | ☐ Adequate ☐ Partial Gap ☐ Critical Gap ☐ Not Deployed |
| **Gap description** | |

### 3.3 Machine Learning

| Dimension | Current State |
|---|---|
| **Tool(s) deployed** | |
| **Type** | ☐ Built-in SIEM/NDR ML ☐ Custom models ☐ None |
| **Use cases active** | ☐ Asset behaviour profiling ☐ Process anomaly ☐ Protocol anomaly ☐ Other |
| **ML Readiness Assessment completed? (Ch.8)** | ☐ Yes ☐ No |
| **Gap assessment** | ☐ Adequate ☐ Partial Gap ☐ Critical Gap ☐ Not Deployed |
| **Gap description** | |

---

## Gap Prioritisation Matrix

*For each identified gap, assess priority using threat intelligence alignment.*

| Gap ID | Capability Gap | Tier | ATT&CK for ICS Techniques Affected | Primary Threat Actors Using These Techniques | Threat Intel Priority (H/M/L) | Deployment Priority |
|---|---|---|---|---|---|---|
| GAP-01 | | | | | | |
| GAP-02 | | | | | | |
| GAP-03 | | | | | | |
| GAP-04 | | | | | | |
| GAP-05 | | | | | | |
| GAP-06 | | | | | | |
| GAP-07 | | | | | | |
| GAP-08 | | | | | | |

**Prioritisation guidance:**
- Tier 1 gaps always take priority over Tier 2 and Tier 3 gaps.
- Within the same tier, gaps aligned with the highest-probability adversary techniques (from Chapter 10 intelligence requirements) take priority.
- Gaps affecting crown jewel visibility take priority over gaps affecting general visibility.

---

## Recommended Actions

| Priority | Gap ID | Recommended Action | Estimated Timeline | Estimated Cost | Owner |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

---

## Assessment Sign-Off

| Role | Name | Date | Signature |
|---|---|---|---|
| SOC Manager | | | |
| OT Security SME | | | |
| OT Engineering Liaison | | | |
| CISO / Security Director | | | |
