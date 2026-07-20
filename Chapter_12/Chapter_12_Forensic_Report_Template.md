# OT Incident Forensic Report Template
# ================================================================
# Description: Structured template for documenting OT incident
#   forensic investigations. Combines endpoint forensics, network
#   forensics, and OT Engineering inputs into a unified report.
#
# Usage: Complete one report per incident. This report feeds directly
#   into the After-Action Review (Chapter_12_AAR_Template.md) as
#   Section 2 (Incident Timeline) and Section 6 (Intelligence Findings).
#
# Chapter Reference: Chapter 12 — Digital Forensics and Lessons Learned
# ================================================================

---

## REPORT HEADER

| Field | Value |
|-------|-------|
| **Report Title** | Forensic Investigation — [Brief Description] |
| **Incident Reference** | |
| **Report Date** | |
| **Report Author(s)** | |
| **Classification** | TLP: [RED / AMBER+STRICT / AMBER / GREEN / CLEAR] |
| **Report Status** | [Draft / Final] |
| **Distribution** | |

---

## 1. EXECUTIVE SUMMARY

*Provide a concise summary (one paragraph) of the incident: what happened, when, what was affected, and the key forensic findings. Written for leadership consumption.*

[Summary text]

**Key Findings:**
- [Finding 1]
- [Finding 2]
- [Finding 3]

**OT Impact:** [None / Monitoring Only / Process Disruption / Safety Impact]

---

## 2. INVESTIGATION SCOPE

### 2.1 Scope Definition

| Parameter | Value |
|-----------|-------|
| **Investigation Window** | [Start datetime] to [End datetime] |
| **Triggering Alert(s)** | [Alert name(s) and Sentinel incident ID(s)] |
| **Endpoints Investigated** | [Count and hostnames] |
| **Network Segments Analysed** | [Purdue levels and VLANs] |
| **OT Systems in Scope** | [List with Purdue Level and Crown Jewel Tier] |

### 2.2 Data Sources Used

| Data Source | Available | Collected | Notes |
|-------------|:---------:|:---------:|-------|
| EDR Telemetry | ☐ | ☐ | |
| Windows Security Events | ☐ | ☐ | |
| Sysmon Logs | ☐ | ☐ | |
| PCAP (IDMZ) | ☐ | ☐ | |
| Zeek Connection Logs | ☐ | ☐ | |
| Zeek ICS Protocol Logs | ☐ | ☐ | |
| Suricata Alerts | ☐ | ☐ | |
| Firewall Logs | ☐ | ☐ | |
| SCADA Historian Data | ☐ | ☐ | Collected by OT Engineering |
| HMI Alarm Logs | ☐ | ☐ | Collected by OT Engineering |
| PLC Configuration Downloads | ☐ | ☐ | Collected by OT Engineering |
| Operator Statements | ☐ | ☐ | Collected by OT Engineering |

### 2.3 Limitations and Gaps

*Document any evidence that was unavailable, incomplete, or collected with known limitations (e.g., chain of custody gaps, systems without EDR, PCAP gaps).*

[Limitations text]

---

## 3. UNIFIED INCIDENT TIMELINE

*The core forensic output. Integrate all data sources into a single chronological narrative. Use the format below for each event.*

| Timestamp (UTC) | T+ Offset | Source Host | Event Type | Data Source | Description | ATT&CK for ICS |
|------------------|-----------|-------------|------------|-------------|-------------|-----------------|
| YYYY-MM-DD HH:MM:SS | T+0h00m | [hostname] | [type] | [EDR/Sysmon/Zeek/etc.] | [Plain-language description] | [Technique ID] |
| | | | | | | |
| | | | | | | |

**Timeline Narrative:**

*Provide a prose narrative of the timeline, explaining the adversary's progression through the environment. Structure as phases:*

**Phase 1 — Initial Access:**
[Description of how the adversary gained initial access. Include the initial access vector, first compromised system, and evidence source.]

**Phase 2 — Establish Foothold:**
[Description of C2 establishment, persistence mechanisms deployed, and tools installed.]

**Phase 3 — Credential Access:**
[Description of credential harvesting. Which credentials were compromised? Which accounts have OT access?]

**Phase 4 — Lateral Movement:**
[Description of movement through the environment. Include the movement graph showing each hop with credentials and method used.]

**Phase 5 — IT/OT Boundary Traversal:**
[If applicable — description of how the adversary crossed from IT into OT. Which boundary point was crossed? Was it detected?]

**Phase 6 — OT Domain Activity:**
[If applicable — description of adversary actions within OT. ICS protocol commands, reconnaissance, manipulation attempts.]

**Phase 7 — Impact:**
[Description of the realised or attempted impact. Ransomware deployment, data exfiltration, process manipulation, or reconnaissance only.]

---

## 4. ENDPOINT FORENSIC FINDINGS

### 4.1 Affected Endpoints Summary

| Hostname | IP Address | Purdue Level | Crown Jewel Tier | EDR Status | Compromise Confirmed | Role in Attack |
|----------|------------|:------------:|:----------------:|:----------:|:--------------------:|----------------|
| | | | | | | |

### 4.2 Malware and Tools Identified

| File Name | File Path | SHA-256 Hash | VirusTotal Detections | Classification | Associated Process |
|-----------|-----------|--------------|:---------------------:|----------------|-------------------|
| | | | | | |

### 4.3 Persistence Mechanisms Identified

| Host | Mechanism Type | Name/Path | Created By | Timestamp | Eradicated (Y/N) |
|------|---------------|-----------|------------|-----------|:-----------------:|
| | Service / Task / Registry / Other | | | | |

### 4.4 Lateral Movement Path

*Document each lateral movement hop as a directed graph:*

```
[Source Host] --(Method: [PsExec/RDP/WMI/etc.], Credentials: [account])--> [Destination Host]
```

**Lateral Movement Graph:**

[Document each hop]

### 4.5 Credential Compromise Assessment

| Account | Account Type | Harvesting Method | OT Systems Accessible | Credential Reset Status |
|---------|-------------|-------------------|----------------------|:----------------------:|
| | User / Service / Admin | | | |

---

## 5. NETWORK FORENSIC FINDINGS

### 5.1 Command-and-Control Profile

| Parameter | Value |
|-----------|-------|
| **C2 IP Address(es)** | |
| **C2 Domain(s)** | |
| **Port(s)** | |
| **Protocol** | |
| **Encryption** | |
| **Beaconing Interval** | |
| **Average Data Volume per Session** | |
| **First Seen** | |
| **Last Seen** | |
| **Total Data Transferred** | |

### 5.2 ICS Protocol Activity

*Document any ICS protocol communications observed during the incident timeframe that are attributable to the adversary (not normal operations).*

| Timestamp | Source IP | Destination IP (Controller) | Protocol | Function Code / Command | Description | Normal (Y/N) |
|-----------|----------|----------------------------|----------|------------------------|-------------|:------------:|
| | | | Modbus/DNP3/EtherNet-IP/etc. | | | |

### 5.3 Data Exfiltration Assessment

| Finding | Value |
|---------|-------|
| **Exfiltration Detected** | Yes / No / Inconclusive |
| **Destination(s)** | |
| **Volume Transferred** | |
| **Data Type(s)** | |
| **Method** | HTTP / DNS / FTP / SMB / Other |
| **Evidence Source** | |

---

## 6. OT ENGINEERING FINDINGS

*This section is completed in collaboration with OT Engineering based on their evidence collection.*

### 6.1 Historian Data Analysis

| Process Variable | Normal Range | Observed Value During Incident | Timestamp | Anomalous (Y/N) |
|-----------------|-------------|-------------------------------|-----------|:----------------:|
| | | | | |

### 6.2 PLC Configuration Assessment

| Controller | Configuration Match to Golden Image | Differences Found | Assessment (OT Engineering) |
|------------|:----------------------------------:|-------------------|---------------------------|
| | Match / Mismatch / Not Assessed | | |

### 6.3 Operational Impact

| Impact Category | Description |
|----------------|-------------|
| **Loss of View** | [Was operator visibility affected? Duration?] |
| **Loss of Control** | [Was operator control affected? Duration?] |
| **Loss of Safety** | [Were safety systems affected? Detail.] |
| **Production Impact** | [Downtime, throughput reduction, product loss?] |
| **Physical Damage** | [Any equipment damage?] |

---

## 7. INDICATORS OF COMPROMISE

*Complete IOC inventory. Transfer all IOCs to the IOC Extraction Checklist for dissemination processing.*

### 7.1 Network Indicators

| Type | Value | Confidence | First Seen | Last Seen | Context |
|------|-------|:----------:|------------|-----------|---------|
| IP Address | | High/Medium/Low | | | |
| Domain | | | | | |
| URL | | | | | |

### 7.2 Host Indicators

| Type | Value | Confidence | Host(s) Found On | Context |
|------|-------|:----------:|-----------------|---------|
| SHA-256 Hash | | | | |
| File Name | | | | |
| File Path | | | | |
| Registry Key | | | | |
| Scheduled Task | | | | |
| Service Name | | | | |
| Mutex | | | | |

### 7.3 Behavioural Indicators

| Behaviour | Description | ATT&CK for ICS | Detection Rule Exists (Y/N) |
|-----------|-------------|:---------------:|:---------------------------:|
| | | | |

---

## 8. ATT&CK FOR ICS TECHNIQUE MAPPING

| Tactic | Technique ID | Technique Name | Observed Evidence | Detected by Existing Rule (Y/N) | Rule Reference |
|--------|:------------:|---------------|-------------------|:-------------------------------:|---------------|
| Initial Access | | | | | |
| Execution | | | | | |
| Persistence | | | | | |
| Privilege Escalation | | | | | |
| Evasion | | | | | |
| Discovery | | | | | |
| Lateral Movement | | | | | |
| Collection | | | | | |
| Command and Control | | | | | |
| Inhibit Response Function | | | | | |
| Impair Process Control | | | | | |
| Impact | | | | | |

---

## 9. ATTRIBUTION ASSESSMENT

| Field | Value |
|-------|-------|
| **Attribution Confidence** | [None / Low / Medium / High] |
| **Assessed Threat Actor** | [Microsoft naming convention] |
| **Alternative Name(s)** | [e.g., Dragos naming on first reference] |
| **Basis for Attribution** | [TTP overlap / IOC match / infrastructure reuse / intelligence correlation] |
| **Campaign Linkage** | [Is this part of a known campaign? Reference.] |

---

## 10. RECOMMENDATIONS

*Specific, actionable recommendations derived from the forensic findings. Each recommendation should reference the supporting evidence.*

| # | Category | Recommendation | Supporting Evidence | Priority | Owner | Due Date |
|---|----------|---------------|--------------------:|:--------:|-------|----------|
| 1 | Detection Engineering | | [Timeline ref] | | | |
| 2 | Architecture | | | | | |
| 3 | Hunting | | | | | |
| 4 | IR Playbook | | | | | |
| 5 | Asset Management | | | | | |

---

## 11. EVIDENCE INVENTORY

| Evidence ID | Description | Source | Collection Date/Time | Collected By | Storage Location | Hash (SHA-256) | Chain of Custody Notes |
|-------------|-------------|--------|---------------------|-------------|-----------------|----------------|----------------------|
| E-001 | | | | | | | |
| E-002 | | | | | | | |

---

## APPENDICES

### Appendix A: Raw Query Results
*Attach or reference the raw KQL query outputs, Zeek log extracts, and PCAP analysis results that support the timeline.*

### Appendix B: Screenshots and Visual Evidence
*Attach EDR console screenshots, Wireshark captures, process trees, and any photographs from OT evidence collection.*

### Appendix C: OT Engineering Evidence Submissions
*Attach or reference all evidence items submitted by OT Engineering with their collection documentation.*
