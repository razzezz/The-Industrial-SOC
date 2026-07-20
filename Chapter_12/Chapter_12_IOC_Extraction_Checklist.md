# IOC Extraction Checklist
# ================================================================
# Description: Systematic checklist for extracting indicators of
#   compromise from forensic evidence across all data sources.
#   Each IOC is assessed for confidence, assigned a shelf life,
#   and tagged for dissemination.
#
# Usage: Complete during the forensic investigation. Transfer final
#   IOCs to the ISAC Sharing Template for external dissemination
#   and to SIEM watchlists/TI feeds for internal operationalisation.
#
# Chapter Reference: Chapter 12 — Digital Forensics and Lessons Learned
# ================================================================

---

## EXTRACTION HEADER

| Field | Value |
|-------|-------|
| **Incident Reference** | |
| **Extraction Analyst** | |
| **Extraction Date** | |
| **Total IOCs Extracted** | [Update on completion] |
| **Classification** | TLP: [RED / AMBER+STRICT / AMBER / GREEN / CLEAR] |

---

## NETWORK INDICATORS

### IP Addresses

| # | IP Address | Direction | Port(s) | Protocol | Context | Confidence | Shelf Life | Source | Disseminate |
|---|-----------|:---------:|---------|----------|---------|:----------:|:----------:|--------|:-----------:|
| N-IP-001 | | Inbound / Outbound / Both | | | [C2 / Scanning / Exfil / Lateral Movement] | High / Med / Low | [days/weeks] | [EDR / Zeek / PCAP / Firewall] | ☐ SIEM ☐ ISAC |
| N-IP-002 | | | | | | | | | |
| N-IP-003 | | | | | | | | | |

**Extraction notes:**
- Check each IP against VirusTotal, AbuseIPDB, and commercial TI feeds before assigning confidence.
- Assign "High" confidence if the IP was directly involved in C2 or exploitation with no legitimate use.
- Assign "Medium" if the IP appeared in suspicious traffic but may be shared infrastructure (CDN, cloud hosting).
- Assign "Low" if the IP is circumstantial (appeared in logs during the incident window but role is unclear).
- Shelf life: C2 infrastructure IPs typically rotate within days to weeks. Assign accordingly.

### Domains

| # | Domain | Type | Context | Confidence | Shelf Life | Source | Disseminate |
|---|--------|------|---------|:----------:|:----------:|--------|:-----------:|
| N-DOM-001 | | FQDN / Subdomain | [C2 / Phishing / Staging / DGA] | | | | ☐ SIEM ☐ ISAC |
| N-DOM-002 | | | | | | | |

### URLs

| # | URL | Context | Confidence | Shelf Life | Source | Disseminate |
|---|-----|---------|:----------:|:----------:|--------|:-----------:|
| N-URL-001 | | [Payload download / C2 endpoint / Phishing landing] | | | | ☐ SIEM ☐ ISAC |

### Email Indicators

| # | Indicator | Type | Context | Confidence | Source | Disseminate |
|---|-----------|------|---------|:----------:|--------|:-----------:|
| N-EM-001 | | Sender address / Subject / Attachment name | [Phishing delivery] | | | ☐ SIEM ☐ ISAC |

---

## HOST INDICATORS

### File Hashes

| # | SHA-256 | MD5 (if available) | File Name | File Path | File Size | VT Detections | Classification | Confidence | Source | Disseminate |
|---|---------|-------|-----------|-----------|-----------|:-------------:|---------------|:----------:|--------|:-----------:|
| H-HASH-001 | | | | | | /[total] | [Ransomware / RAT / Backdoor / Tool / Dropper / Unknown] | | [EDR / Disk] | ☐ SIEM ☐ ISAC |
| H-HASH-002 | | | | | | | | | | |
| H-HASH-003 | | | | | | | | | | |

**Extraction notes:**
- Always extract SHA-256 as the primary hash. MD5 for legacy system compatibility.
- Submit all hashes to VirusTotal. Record the detection ratio and any vendor classifications.
- Assign "High" confidence to hashes confirmed as malicious by multiple AV engines or by forensic analysis.
- Assign "Medium" to hashes with limited detections or that may be dual-use tools (e.g., PsExec, Mimikatz).
- File hashes have a long shelf life — the same binary may be reused across campaigns for months or years.

### File Names and Paths

| # | File Name | File Path | Context | Confidence | Source | Disseminate |
|---|-----------|-----------|---------|:----------:|--------|:-----------:|
| H-FILE-001 | | | [Payload / Tool / Staging / Exfil archive] | | | ☐ SIEM ☐ ISAC |

**Note:** File names are low-fidelity indicators — adversaries can easily change them. Use for enrichment context, not as primary detection.

### Registry Keys

| # | Registry Key Path | Value Name | Value Data | Context | Confidence | Source | Disseminate |
|---|------------------|------------|------------|---------|:----------:|--------|:-----------:|
| H-REG-001 | | | | [Persistence / Configuration / Evasion] | | [EDR / Sysmon / Forensic image] | ☐ SIEM ☐ ISAC |

### Scheduled Tasks

| # | Task Name | Task Path | Action / Command | Trigger | Context | Confidence | Source | Disseminate |
|---|-----------|-----------|-----------------|---------|---------|:----------:|--------|:-----------:|
| H-TASK-001 | | | | | [Persistence / Execution] | | | ☐ SIEM ☐ ISAC |

### Services

| # | Service Name | Display Name | Image Path | Start Type | Context | Confidence | Source | Disseminate |
|---|-------------|-------------|------------|:----------:|---------|:----------:|--------|:-----------:|
| H-SVC-001 | | | | | [Persistence / Backdoor] | | | ☐ SIEM ☐ ISAC |

### Named Pipes / Mutexes

| # | Indicator | Type | Context | Confidence | Source | Disseminate |
|---|-----------|------|---------|:----------:|--------|:-----------:|
| H-OBJ-001 | | Named Pipe / Mutex | [C2 channel / Tool signature] | | | ☐ SIEM ☐ ISAC |

---

## BEHAVIOURAL INDICATORS

*Behavioural indicators describe adversary actions rather than static artifacts. These are higher-fidelity and longer-lived than file/network IOCs.*

| # | Behaviour Description | ATT&CK for ICS Technique | Detection Possible (Y/N) | Detection Rule Exists (Y/N) | Rule Reference | Disseminate |
|---|----------------------|:------------------------:|:------------------------:|:---------------------------:|---------------|:-----------:|
| B-001 | | | | | | ☐ ISAC |
| B-002 | | | | | | |
| B-003 | | | | | | |

**Examples of behavioural indicators:**
- "Adversary used Modbus function code 43 from a historian server to enumerate PLCs"
- "PowerShell executed with Base64-encoded command line from a scheduled task named 'SystemUpdate'"
- "RDP session from IT subnet to IDMZ historian outside maintenance window"

---

## COMMAND-LINE STRINGS

| # | Command Line | Process | Context | Confidence | Source | Disseminate |
|---|-------------|---------|---------|:----------:|--------|:-----------:|
| CMD-001 | | | [Execution / Recon / Exfil / Persistence] | | [EDR / Sysmon] | ☐ SIEM ☐ ISAC |

---

## DISSEMINATION TRACKER

### Internal Dissemination

| IOC Set | Destination | Format | Date Submitted | Submitted By | Confirmed Active |
|---------|------------|--------|---------------|-------------|:----------------:|
| [All network IOCs] | Sentinel TI Watchlist | CSV / STIX | | | ☐ |
| [All file hashes] | EDR Block/Detect List | Hash list | | | ☐ |
| [Behavioural IOCs] | Detection Engineering | AAR recommendations | | | ☐ |
| [Behavioural IOCs] | Hunting Team | Hunting hypotheses | | | ☐ |

### External Dissemination

| IOC Set | Recipient | TLP | Format | Date Shared | Shared By |
|---------|-----------|:---:|--------|-------------|-----------|
| | [Sector ISAC] | | STIX / Template / Email | | |
| | [CISA AIS] | | STIX/TAXII | | |
| | [Peer organisation] | | | | |

---

## IOC REVIEW AND EXPIRY

*All IOCs have a finite useful life. Schedule review to remove expired IOCs from active detection.*

| Review Date | Analyst | IOCs Reviewed | IOCs Expired / Removed | IOCs Extended | Notes |
|-------------|---------|:-------------:|:----------------------:|:-------------:|-------|
| [30 days post-incident] | | | | | |
| [90 days post-incident] | | | | | |
| [180 days post-incident] | | | | | |
