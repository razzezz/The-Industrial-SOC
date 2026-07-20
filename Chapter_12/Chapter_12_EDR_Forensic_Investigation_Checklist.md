# EDR Forensic Investigation Checklist
# ================================================================
# Description: Step-by-step checklist for conducting endpoint forensics
#   via EDR on Windows-based OT systems. Covers the six-step workflow:
#   initial triage, process analysis, network connection analysis,
#   file system forensics, memory forensics, and lateral movement tracking.
#
# Usage: Print and use as a procedural guide during active investigations.
#   Check each item as completed. Record evidence references in the
#   "Notes / Evidence Ref" column. Feed findings into the Forensic Report
#   Template (Chapter_12_Forensic_Report_Template.md).
#
# Chapter Reference: Chapter 12 — Digital Forensics and Lessons Learned
# ================================================================

## INVESTIGATION HEADER

| Field | Value |
|-------|-------|
| **Incident Reference** | |
| **Lead Analyst** | |
| **Date/Time Started** | |
| **EDR Platform** | |
| **Endpoints in Scope** | |
| **Associated Sentinel Incident(s)** | |

---

## STEP 1 — INITIAL TRIAGE

**Objective:** Identify all affected endpoints, establish the earliest indicator of compromise, and determine the initial access vector.

- [ ] **1.1** Review the triggering Sentinel alert(s) and EDR alert(s). Record alert names, timestamps, and affected hostnames.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **1.2** Search EDR for the primary IOC (hash, IP, domain, command line) across the full endpoint fleet. Record all matching endpoints.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **1.3** For each affected endpoint, check against the OT_AssetRegister watchlist. Record Purdue Level, Crown Jewel Tier, and Device Type.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **1.4** Pull the full EDR timeline for each affected endpoint, starting 24 hours before the first known indicator.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **1.5** Identify the earliest evidence of compromise across all endpoints. Record the timestamp — this becomes T+0 in the unified timeline.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **1.6** Determine the initial access vector: phishing payload, remote access exploit, removable media, supply chain, or unknown.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **1.7** Check OT_MaintenanceWindows watchlist — was there a scheduled maintenance window coinciding with the initial activity? Rule out legitimate activity.
  - Notes / Evidence Ref: _______________________________________________

**Triage Summary:**
- Total endpoints affected: ______
- Earliest compromise timestamp: ______
- Initial access vector: ______
- OT systems involved (Y/N): ______ If yes, notify Engineering Liaison immediately.

---

## STEP 2 — PROCESS ANALYSIS

**Objective:** Reconstruct the execution chain on each affected endpoint. Map adversary activity to ATT&CK for ICS techniques.

- [ ] **2.1** For the initial payload process, record: process name, PID, parent process, command-line arguments, file path, file hash (SHA-256), digital signature status.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **2.2** Map the complete process tree from the initial payload downward. Record all child processes, their command lines, and timestamps.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **2.3** Identify any Living-off-the-Land Binaries (LOLBins) in the process tree:
  - [ ] PowerShell (powershell.exe, pwsh.exe)
  - [ ] Command Prompt (cmd.exe)
  - [ ] Certutil (certutil.exe)
  - [ ] BITSAdmin (bitsadmin.exe)
  - [ ] MSHTA (mshta.exe)
  - [ ] Regsvr32 (regsvr32.exe)
  - [ ] Rundll32 (rundll32.exe)
  - [ ] WMIC (wmic.exe)
  - [ ] Other: ______________________________
  - Notes / Evidence Ref: _______________________________________________

- [ ] **2.4** Check for encoded/obfuscated command-line arguments (Base64-encoded PowerShell, hex-encoded strings, etc.). Decode and record.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **2.5** Map each observed technique to ATT&CK for ICS. Record technique IDs.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **2.6** Check process execution against known threat actor tooling profiles (Chapter 10 adversary profiles).
  - Notes / Evidence Ref: _______________________________________________

---

## STEP 3 — NETWORK CONNECTION ANALYSIS

**Objective:** Identify C2 channels, lateral movement connections, and any communications with OT devices.

- [ ] **3.1** For each suspicious process identified in Step 2, pull all associated network connections from EDR. Record: destination IP, port, protocol, bytes transferred, timestamps.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **3.2** Identify potential C2 communications:
  - [ ] Periodic beaconing (consistent time intervals between connections)
  - [ ] Connections to external IPs with no legitimate business purpose
  - [ ] Encrypted communications on non-standard ports
  - [ ] DNS requests to unusual domains (potential DNS tunnelling)
  - [ ] HTTP/HTTPS to dynamic DNS domains
  - Notes / Evidence Ref: _______________________________________________

- [ ] **3.3** Record C2 profile: IP(s), domain(s), port(s), protocol, beaconing interval, encryption method, data volume.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **3.4** Check all destination IPs against OT_AssetRegister. Flag any connections to OT systems (Purdue Levels 0–3).
  - Notes / Evidence Ref: _______________________________________________

- [ ] **3.5** Check all external IPs/domains against threat intelligence (VirusTotal, commercial TI feeds, ISAC intelligence).
  - Notes / Evidence Ref: _______________________________________________

- [ ] **3.6** Cross-reference network connections with Zeek connection logs for corroboration (Workstream 3).
  - Notes / Evidence Ref: _______________________________________________

---

## STEP 4 — FILE SYSTEM FORENSICS

**Objective:** Identify adversary tools, staged payloads, and exfiltrated data. Detect anti-forensic techniques.

- [ ] **4.1** List all files created by suspicious processes. Record: file name, path, SHA-256 hash, creation timestamp, size.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **4.2** Submit all file hashes to VirusTotal and/or other reputation services. Record detection results.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **4.3** Identify dropped tools (e.g., Mimikatz, PsExec, LaZagne, Cobalt Strike, Impacket tools, custom tools).
  - Notes / Evidence Ref: _______________________________________________

- [ ] **4.4** Check for timestomping: compare file creation/modification timestamps in the MFT against the process execution timeline from Step 2. Flag discrepancies.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **4.5** Look for staging directories (commonly: C:\ProgramData, C:\Users\Public, C:\Windows\Temp, user Temp directories, Recycle Bin).
  - Notes / Evidence Ref: _______________________________________________

- [ ] **4.6** Check for evidence of data staging for exfiltration: compressed archives (.zip, .rar, .7z), renamed file extensions, files in unusual locations.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **4.7** Record all file-based IOCs in the IOC Extraction Checklist.
  - Notes / Evidence Ref: _______________________________________________

---

## STEP 5 — MEMORY FORENSICS

**Objective:** Detect fileless techniques, code injection, and credential harvesting.

- [ ] **5.1** Check for LSASS memory access. Look for:
  - [ ] Processes accessing lsass.exe memory (Sysmon Event ID 10 or EDR equivalent)
  - [ ] Suspicious processes opening handles to LSASS with PROCESS_VM_READ access
  - [ ] Procdump, comsvcs.dll MiniDump, or Task Manager memory dump of LSASS
  - Notes / Evidence Ref: _______________________________________________

- [ ] **5.2** Check for code injection techniques:
  - [ ] Process hollowing (legitimate process spawned in suspended state, then modified)
  - [ ] Reflective DLL injection (DLLs loaded without corresponding file-on-disk)
  - [ ] APC injection, thread injection, or other memory injection methods
  - Notes / Evidence Ref: _______________________________________________

- [ ] **5.3** Check for unsigned or anomalous DLLs loaded by system processes. Cross-reference against known-good baselines.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **5.4** If EDR supports memory snapshot analysis, capture and examine memory artifacts from key affected endpoints.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **5.5** If credential dumping is confirmed, list all potentially compromised accounts. Cross-reference with accounts that have access to OT systems.
  - Notes / Evidence Ref: _______________________________________________

**⚠️ OT IMPACT NOTE:** If compromised credentials include service accounts used by SCADA polling, historian connections, or control system communications, notify OT Engineering immediately. Credential reset must be coordinated per the decision authority structure (Chapter 11).

---

## STEP 6 — LATERAL MOVEMENT TRACKING

**Objective:** Build the complete adversary movement path across the environment. Identify the direction of movement toward OT.

- [ ] **6.1** Compile all remote execution indicators across affected endpoints:
  - [ ] PsExec / PsExec-like tools (new service installations, PSEXESVC.exe)
  - [ ] WMI remote execution (wmiprvse.exe spawning unexpected processes)
  - [ ] DCOM remote execution
  - [ ] WinRM / PowerShell Remoting (wsmprovhost.exe)
  - [ ] RDP (mstsc.exe, or inbound Type 10 logons)
  - [ ] SSH (if applicable to OT-adjacent Linux systems)
  - Notes / Evidence Ref: _______________________________________________

- [ ] **6.2** Build the lateral movement graph: source host → credentials used → method → destination host → timestamp. Record each hop.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **6.3** Determine the direction of movement. Is the adversary moving:
  - [ ] Laterally within IT (expanding scope)
  - [ ] From IT toward OT (boundary traversal)
  - [ ] Within OT (already past the boundary)
  - Notes / Evidence Ref: _______________________________________________

- [ ] **6.4** Identify the furthest point of adversary access. Which was the highest-criticality system reached? Record Purdue Level and Crown Jewel Tier.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **6.5** Correlate lateral movement with Sentinel authentication logs (Windows Event 4624 Types 3, 7, 10) for independent confirmation.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **6.6** Correlate lateral movement with Zeek connection logs for network-level confirmation of each hop.
  - Notes / Evidence Ref: _______________________________________________

- [ ] **6.7** Determine whether any lateral movement crossed the IT/OT boundary (Purdue Level 4/5 → Level 3.5 or below). If yes, this is a critical finding.
  - Notes / Evidence Ref: _______________________________________________

---

## INVESTIGATION CLOSURE

- [ ] All six steps completed for all in-scope endpoints
- [ ] All IOCs extracted and recorded in IOC Extraction Checklist
- [ ] All ATT&CK for ICS technique mappings documented
- [ ] Unified timeline drafted combining all endpoint findings
- [ ] Findings handed off to Workstream 4 (Correlation) for integration with network and OT data
- [ ] Evidence preserved per retention policy

| Field | Value |
|-------|-------|
| **Date/Time Completed** | |
| **Total Endpoints Investigated** | |
| **Total IOCs Extracted** | |
| **ATT&CK Techniques Observed** | |
| **Furthest Point of Compromise** | |
| **IT/OT Boundary Crossed (Y/N)** | |
