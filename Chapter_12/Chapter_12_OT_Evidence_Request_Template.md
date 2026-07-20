# OT Evidence Request Template
# ================================================================
# Description: Communication template for requesting specific forensic
#   evidence from OT Engineering during an incident investigation.
#   Designed to be clear, specific, and respectful of OT Engineering's
#   time and operational constraints.
#
# Usage: Pre-populate Sections 1-2 during peacetime with standard
#   contact information and general guidance. During an incident,
#   complete Sections 3-5 with incident-specific details and send
#   to the Engineering Liaison.
#
# Chapter Reference: Chapter 12 — Digital Forensics and Lessons Learned
# ================================================================

---

## EVIDENCE REQUEST

**Subject:** FORENSIC EVIDENCE REQUEST — Incident [Reference Number]

**Priority:** [URGENT — Active Incident / HIGH — Investigation in Progress / ROUTINE — Post-Incident Collection]

**Date/Time of Request:** [DD/MM/YYYY HH:MM UTC]

---

### SECTION 1 — REQUEST HEADER

| Field | Value |
|-------|-------|
| **Incident Reference** | |
| **Incident Severity** | [1-Critical / 2-High / 3-Medium / 4-Low] |
| **Requesting SOC Analyst** | |
| **SOC Contact (Phone)** | |
| **SOC Contact (Email)** | |
| **OT Engineering Recipient** | [Name / Engineering Liaison] |
| **Evidence Delivery Deadline** | [Date/Time — be realistic] |

---

### SECTION 2 — INCIDENT CONTEXT

*Provide a brief, plain-language description of the suspected compromise. OT Engineering needs enough context to understand WHY the evidence is needed, but this should be concise — not a full forensic report.*

**What happened:**
[2-3 sentences describing the detected activity in plain language. Example: "We detected an unauthorised connection from the historian server to multiple PLCs at 14:32 UTC today. This was not associated with any scheduled maintenance. We need to determine whether any PLC configurations were modified."]

**What systems are potentially affected:**

| Hostname / Asset ID | IP Address | Purdue Level | Device Type | Role in Incident |
|---------------------|------------|:------------:|-------------|-----------------|
| | | | | [Source / Target / Both / Unknown] |

**Current incident status:** [Detection / Triage / Containment / Eradication / Recovery / Post-Incident]

**Is there an active safety concern?** [Yes — detail / No / Under assessment]

---

### SECTION 3 — EVIDENCE ITEMS REQUESTED

*List each evidence item specifically. Include the device identifier, the timeframe needed, and WHY it is needed. Be as specific as possible to minimise the burden on OT Engineering.*

#### Item 1: SCADA Historian Data

| Field | Value |
|-------|-------|
| **Requested** | ☐ Yes ☐ Not needed for this incident |
| **Historian System** | [Hostname / System name] |
| **Timeframe** | [Start datetime] to [End datetime] |
| **Process Variables of Interest** | [List specific tags/variables — e.g., "All variables associated with PLC at 10.10.2.15" or "Temperature, pressure, and flow for Process Unit 3"] |
| **Export Format** | [CSV preferred / System-native format acceptable] |
| **Why Needed** | [e.g., "To determine whether the adversary's Modbus write commands caused any change in process variables"] |

#### Item 2: HMI Alarm Logs

| Field | Value |
|-------|-------|
| **Requested** | ☐ Yes ☐ Not needed for this incident |
| **HMI System(s)** | [Hostname(s)] |
| **Timeframe** | [Start datetime] to [End datetime] |
| **Specific Alarms of Interest** | [All alarms / Specific process area / Specific alarm types] |
| **Export Format** | [CSV / Screenshot / System-native] |
| **Why Needed** | [e.g., "To determine whether operators observed any anomalous alarms coinciding with the detected network activity"] |

#### Item 3: PLC Configuration Download

| Field | Value |
|-------|-------|
| **Requested** | ☐ Yes ☐ Not needed for this incident |
| **PLC / Controller(s)** | [Device identifier(s), IP address(es)] |
| **Comparison Baseline** | [Golden image location — e.g., "Compare against golden image stored at \\server\golden-images\PLC-001\"] |
| **Why Needed** | [e.g., "Network forensics show a configuration download to this PLC at 15:47 UTC. We need to verify whether the current configuration matches the approved baseline."] |

**⚠️ IMPORTANT:** Please document the following when collecting PLC configurations:
- Date/time of download
- Engineering tool and version used
- Name of the engineer performing the download
- Whether any differences from the golden image were identified

#### Item 4: Operator Statements

| Field | Value |
|-------|-------|
| **Requested** | ☐ Yes ☐ Not needed for this incident |
| **Operator(s) on Shift During Incident** | [Names or shift identifier if known] |
| **Questions to Address** | |

Operator statement questions:
1. Did you observe any unusual alarms, readings, or HMI behaviour during [timeframe]?
2. Did any displays go blank, freeze, or show unexpected values?
3. Did you take any manual actions (manual overrides, process shutdowns, mode changes) during [timeframe]?
4. Did anyone (including vendors or other engineers) access the control room or connect to systems during [timeframe]?
5. Is there anything else unusual you noticed, even if it seemed unrelated at the time?

| **Why Needed** | [e.g., "Operator observations provide context that log data cannot — whether the adversary's actions had visible impact on the control room"] |

#### Item 5: Manual Endpoint Evidence Collection

| Field | Value |
|-------|-------|
| **Requested** | ☐ Yes ☐ Not needed for this incident |
| **System(s) Without EDR / Central Logging** | [Hostname(s), IP(s)] |
| **Evidence to Collect** | |

For each system without EDR, please collect:
- [ ] Windows Event Logs: Security, System, Application (export as .evtx)
- [ ] Running processes: `tasklist /v > processes.txt`
- [ ] Network connections: `netstat -ano > netstat.txt`
- [ ] Scheduled tasks: `schtasks /query /v /fo csv > tasks.csv`
- [ ] Services: `sc query type= all state= all > services.txt`
- [ ] Autostart entries: `reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run > run_keys.txt`
- [ ] Screenshots of any anomalous displays or error messages
- [ ] Timestamp the collection: run `echo %date% %time% > collection_timestamp.txt` before starting

| **Why Needed** | [e.g., "This SCADA server does not have EDR deployed. Manual collection provides the endpoint evidence needed to determine whether it was compromised."] |

#### Item 6: Other Evidence

| Field | Value |
|-------|-------|
| **Requested** | ☐ Yes ☐ Not needed for this incident |
| **Description** | |
| **Why Needed** | |

---

### SECTION 4 — EVIDENCE HANDLING INSTRUCTIONS

**Delivery method:** [Secure file share link / Encrypted email / Physical media — specify]

**Delivery location:** [URL / email address / physical drop-off point]

**File naming convention:** Please name files as:
`[IncidentRef]_[DeviceHostname]_[EvidenceType]_[YYYYMMDD].[ext]`

Example: `INC-2026-042_PLC-001_ConfigDownload_20260215.l5x`

**Documentation:** For each evidence item collected, please record:
1. Who collected it (name)
2. When it was collected (date/time)
3. Which device it was collected from (hostname/IP)
4. Which tool was used to collect it
5. Where the original is stored

**Preservation:** Please do not reboot, power cycle, or reset any potentially affected device until the SOC confirms that evidence collection is complete, unless required for safety reasons.

---

### SECTION 5 — QUESTIONS AND COORDINATION

If you have any questions about this evidence request, please contact:

| Role | Name | Phone | Email |
|------|------|-------|-------|
| **Primary SOC Contact** | | | |
| **Backup SOC Contact** | | | |
| **Incident Manager** | | | |

**Next scheduled update:** [Date/Time — the SOC will provide a status update at this time]

**Acknowledgement requested:** Please confirm receipt of this request and provide an estimated timeline for evidence delivery.

---

### ACKNOWLEDGEMENT (OT Engineering)

| Field | Value |
|-------|-------|
| **Received By** | |
| **Date/Time Received** | |
| **Estimated Delivery Time** | |
| **Items That Cannot Be Collected (and why)** | |
| **Questions / Concerns** | |
