# SOC Analyst OT Quick Reference Card

*Print this card and keep it at your workstation. It provides the essential OT context for alert triage and escalation.*

---

## OT Alert Triage Framework — Four Dimensions

| # | Dimension | Question to Ask | Where to Find the Answer |
|---|-----------|----------------|--------------------------|
| 1 | **Indicator Confidence** | How confident are we that this is genuinely anomalous or malicious? | Detection rule history, corroborating evidence, multi-source correlation |
| 2 | **Asset Criticality** | What is the crown jewel tier of the affected asset? | `OT_CrownJewels` watchlist in Sentinel |
| 3 | **Potential Consequence** | What could happen if this is malicious and succeeds? | See Consequence Categories below; consult OT SME for Tier 1/2 assets |
| 4 | **Operational Context** | Is there a known operational reason for this activity? | `OT_MaintenanceWindows` watchlist; Engineering Liaison; weekly sync notes |

---

## Triage Decision Quick Reference

| Asset Tier | Indicator Confidence | Maintenance Window Active? | Action | Response Target |
|-----------|---------------------|---------------------------|--------|-----------------|
| **Tier 1 (Safety)** | Any | Any | **ALWAYS escalate immediately** to OT SME + Engineering Liaison | **15 minutes** |
| **Tier 2 (Process)** | High | No | Escalate to Tier 2 + OT SME. Notify Engineering Liaison | **30 minutes** |
| **Tier 2 (Process)** | Low/Medium | No | Investigate at Tier 2. Consult OT SME if indicators develop | **1 hour** |
| **Tier 3–5** | High | No | Standard Tier 2 investigation. Consult OT SME for context | **1 hour** |
| **Tier 3–5** | Low/Medium | Yes | Log, correlate with maintenance activity. Close if consistent | **4 hours** |
| **Any** | Any | — | Default: Enrich with OT context from watchlists. Standard IT triage | **Per SLA** |

---

## Consequence Categories

| Category | Meaning | Example |
|----------|---------|---------|
| **Loss of View** | Operators cannot see process status | HMI screen frozen, historian data stops updating |
| **Loss of Control** | Operators cannot send commands to the process | SCADA-to-PLC communication disrupted, command channel blocked |
| **Loss of Safety** | Safety systems compromised or bypassed | SIS firmware modified, safety interlock disabled |
| **No Direct OT Consequence** | Activity affects IT-side systems only | Engineering workstation malware, email compromise |

---

## Purdue Model Quick Reference

| Level | Name | Example Systems | SOC Relevance |
|-------|------|----------------|---------------|
| **Level 5** | Enterprise Network | Corporate IT, email, internet | Standard IT SOC monitoring |
| **Level 4** | Site Business Planning | Site servers, business apps | Standard IT SOC monitoring |
| **Level 3.5** | Industrial DMZ (IDMZ) | Jump servers, data diodes, historians (DMZ-side) | **Critical boundary — monitor all traversals** |
| **Level 3** | Site Operations | Engineering workstations, HMIs, historians | OT alert triage applies; consult OT SME |
| **Level 2** | Area Supervisory Control | SCADA servers, DCS controllers | **OT SME engagement required** |
| **Level 1** | Basic Control | PLCs, RTUs, DCS I/O | **OT SME + Engineering escalation mandatory** |
| **Level 0** | Physical Process | Sensors, actuators, field devices | **Immediately escalate any anomaly** |

---

## Common ICS Protocols and Key Function Codes

### Modbus TCP (Port 502)

| Function Code | Name | Normal Context | Suspicious Context |
|--------------|------|---------------|-------------------|
| 1 | Read Coils | Routine polling by HMI/SCADA | Unusual source, high frequency, odd timing |
| 2 | Read Discrete Inputs | Routine polling | Unusual source |
| 3 | Read Holding Registers | Routine polling | Unusual source, reconnaissance pattern |
| 4 | Read Input Registers | Routine polling | Unusual source |
| **5** | **Write Single Coil** | **Maintenance, authorised changes** | **Any write outside maintenance window** |
| **6** | **Write Single Register** | **Maintenance, authorised changes** | **Any write outside maintenance window** |
| **15** | **Write Multiple Coils** | **Maintenance, authorised changes** | **Any write outside maintenance window — HIGH PRIORITY** |
| **16** | **Write Multiple Registers** | **Maintenance, authorised changes** | **Any write outside maintenance window — HIGH PRIORITY** |
| 8 | Diagnostics | Vendor maintenance tool | Unusual source, scanning pattern |
| 43 | Read Device Identification | Asset discovery tools | Reconnaissance indicator if from unexpected source |

**Key rule:** Read operations (FC 1–4) are generally lower risk. Write operations (FC 5, 6, 15, 16) outside a maintenance window are always significant.

### DNP3 (Port 20000)

| Function | Normal Context | Suspicious Context |
|----------|---------------|-------------------|
| Read | Routine SCADA polling | Unusual source |
| Write | Authorised setpoint changes | Any write from unexpected source |
| Cold/Warm Restart | Planned maintenance | Unplanned restart — potential attack |
| File Transfer | Firmware updates during maintenance | Any file transfer outside maintenance |
| Disable Unsolicited Messages | Planned reconfiguration | Disrupting normal reporting — Loss of View |

### OPC UA (Port 4840)

| Activity | Normal Context | Suspicious Context |
|----------|---------------|-------------------|
| Browse (discovery) | Engineering tools during configuration | New client browsing node structure — reconnaissance |
| Read | Routine data collection | Unusual client or frequency |
| Write | Authorised changes | Any write from new client |
| Method Call | Automation scripts during maintenance | Unexpected method execution |

---

## Engineering Escalation Template

When escalating to OT Engineering, provide:

```
ESCALATION TO ENGINEERING

Incident Ref: [Sentinel Incident ID]
Date/Time: [Now]
Urgency: [Critical / High / Medium]

Affected Asset:
  Hostname: [hostname]
  IP Address: [IP]
  Purdue Level: [L0–L5]
  Crown Jewel Tier: [Tier 1–5]
  Function: [What this asset does in plain language]

Detected Activity:
  [Describe in plain language — NOT just MITRE technique IDs]
  Example: "Unexpected Modbus write commands (FC 16) to PLC
  controlling cooling pump from an IP not in the asset register"

Current Production Status: [Normal / Degraded / Unknown]

Maintenance Window Active: [Yes — window ID / No]

Question for Engineering:
  [ ] "Is this expected engineering activity?"
  [ ] "What would be the operational impact of isolating [asset]?"
  [ ] "Can we switch to backup [system] while we investigate?"
  [ ] Other: [specify]

SOC Contact: [Name, phone, chat handle]
Next Update: [Time]
```

---

## Key Contacts

| Role | Name | Phone | Chat Handle |
|------|------|-------|-------------|
| OT Security SME | [Name] | [Number] | [Handle] |
| Engineering Liaison | [Name] | [Number] | [Handle] |
| OT Engineering Lead | [Name] | [Number] | [Handle] |
| Operations Manager | [Name] | [Number] | [Handle] |
| CSIRT Lead | [Name] | [Number] | [Handle] |

---

## Critical Reminders

1. **Never isolate an OT asset at Purdue Levels 0–3 without engineering agreement.** The containment may be more dangerous than the threat.

2. **Always check the maintenance window schedule** before escalating an OT alert. The OT_MaintenanceWindows watchlist in Sentinel is your first stop.

3. **Tier 1 (Safety System) alerts are ALWAYS escalated.** No exceptions, regardless of confidence level or maintenance status.

4. **Your first call for OT anomalies should be to engineering — not to your CISO.** "I saw something unusual and wanted to check with you" builds trust. "We detected a threat and isolated the device" destroys it.

5. **Write commands outside maintenance windows are always significant.** Modbus FC 5/6/15/16, DNP3 writes, OPC UA writes from unexpected sources — these warrant investigation regardless of other context.

---

*This reference card is version [X.X], last updated [Date]. Report errors or suggestions to the OT SME or Detection Engineer.*
