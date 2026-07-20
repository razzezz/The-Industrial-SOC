# Zeek ICS Parser Deployment Guide
# ================================================================
# Description: Step-by-step guide for deploying CISA's ICSNPP
#   (Industrial Control Systems Network Protocol Parsers) for Zeek,
#   with integration into Microsoft Sentinel via ASIM normalisation.
#
# Citation: CISA. "ICSNPP: Industrial Control Systems Network
#   Protocol Parsers." GitHub.
#   https://github.com/cisagov/ICSNPP
#
# Prerequisites:
#   - Zeek 5.0+ deployed on a sensor with access to a network TAP
#     or SPAN port mirroring OT traffic
#   - Microsoft Sentinel workspace with Log Analytics
#   - Azure Monitor Agent or log shipper (Filebeat/Fluentd)
#   - Coordination with OT engineering team for TAP placement
# ================================================================

---

## Overview

CISA's ICSNPP project provides open-source Zeek plugins that enable deep parsing of ICS/SCADA protocols beyond Zeek's built-in capabilities. These parsers generate structured log files recording protocol-level details — function codes, register addresses, data values, and control commands — that are essential for ICS security monitoring, detection engineering, and forensic investigation.

This guide covers installation of the ICSNPP parsers, validation of ICS protocol parsing, integration with Microsoft Sentinel, and the custom ASIM parser development required to normalise ICS protocol data for use with the detection rules described throughout this book.

---

## Step 1: Install ICSNPP Parsers on the Zeek Sensor

### Option A: Install via Zeek Package Manager (Recommended)

```bash
# Install the Zeek Package Manager if not already present
pip3 install zkg

# Configure zkg
zkg autoconfig

# Install ICSNPP parser packages
zkg install icsnpp-modbus
zkg install icsnpp-dnp3
zkg install icsnpp-enip
zkg install icsnpp-s7comm
zkg install icsnpp-bacnet
zkg install icsnpp-opcua-binary

# Verify installation
zkg list installed
```

### Option B: Build from Source

```bash
# Clone the ICSNPP repository
git clone https://github.com/cisagov/ICSNPP.git
cd ICSNPP

# Build and install individual parsers
cd icsnpp-modbus
mkdir build && cd build
cmake .. -DCMAKE_INSTALL_PREFIX=$(zeek-config --prefix)
make && sudo make install

# Repeat for each required protocol parser
```

### Verify Parser Loading

```bash
# Check that Zeek loads the parsers without errors
zeek -N | grep -i "icsnpp"

# Expected output (example):
# Zeek::ICSNPP_MODBUS - ICSNPP Modbus Analyzer (dynamic, version X.X.X)
# Zeek::ICSNPP_DNP3   - ICSNPP DNP3 Analyzer (dynamic, version X.X.X)
# Zeek::ICSNPP_ENIP   - ICSNPP ENIP/CIP Analyzer (dynamic, version X.X.X)
```

---

## Step 2: Configure Zeek for ICS Protocol Logging

### Create an ICS-Specific Zeek Configuration

Create a site-specific configuration file that enables the ICSNPP parsers and configures logging appropriate for OT environments.

```bash
# /opt/zeek/share/zeek/site/ics-monitor.zeek

# Load ICSNPP protocol analysers
@load icsnpp/modbus
@load icsnpp/dnp3
@load icsnpp/enip
@load icsnpp/s7comm
@load icsnpp/bacnet
@load icsnpp/opcua-binary

# Enable JSON log output (required for Sentinel ingestion)
@load policy/tuning/json-logs.zeek

# Set log rotation (align with your SIEM ingestion cycle)
redef Log::default_rotation_interval = 1hr;

# Define OT network ranges for context
# Adjust these to match your environment
redef Site::local_nets += {
    10.1.0.0/16,      # OT network range
    172.16.0.0/16,     # IDMZ range
    192.168.100.0/24   # Engineering VLAN
};
```

### Enable the Configuration

```bash
# Add to local.zeek or deploy via zeekctl
echo '@load site/ics-monitor.zeek' >> /opt/zeek/share/zeek/site/local.zeek

# Deploy the configuration
zeekctl deploy

# Verify Zeek is running and processing traffic
zeekctl status
```

---

## Step 3: Validate ICS Protocol Parsing

### Verify Log File Generation

After deploying the parsers, verify that Zeek is generating ICS-specific log files:

```bash
# Check for ICS protocol logs in the Zeek log directory
ls -la /opt/zeek/logs/current/

# Expected ICS-specific log files:
# modbus.log          — Modbus TCP transactions
# modbus_detailed.log — Detailed register read/write values
# dnp3.log            — DNP3 transactions
# cip.log             — EtherNet/IP CIP service transactions
# enip.log            — EtherNet/IP session management
# s7comm.log          — Siemens S7 protocol transactions
# bacnet.log          — BACnet transactions
# opcua-binary.log    — OPC UA Binary transactions
```

### Validate Modbus Parsing (Example)

```bash
# View recent Modbus transactions
cat /opt/zeek/logs/current/modbus.log | zeek-cut ts uid id.orig_h id.orig_p id.resp_h id.resp_p func unit_id

# Expected fields include:
# ts            — Timestamp
# uid           — Connection unique ID
# id.orig_h     — Source IP (e.g., HMI or engineering workstation)
# id.resp_h     — Destination IP (e.g., PLC)
# func          — Modbus function code (1=Read Coils, 3=Read Holding Registers, 6=Write Single Register, etc.)
# unit_id       — Modbus unit/slave identifier
```

### Key Function Codes to Monitor

| Protocol | Function Code | Operation Type | Security Significance |
|----------|--------------|----------------|----------------------|
| **Modbus** | FC 1-4 | Read (Coils/Registers) | Routine — monitor for unexpected sources |
| **Modbus** | FC 5, 6, 15, 16 | Write (Coils/Registers) | High — should only occur during maintenance |
| **Modbus** | FC 8 | Diagnostics | High — can be abused for reconnaissance (UC-ICS-005) |
| **Modbus** | FC 43 | Read Device Identification | Medium — reconnaissance indicator |
| **DNP3** | Write | Write to data objects | High — controlled operation |
| **DNP3** | Direct/Select Operate | Control relay outputs | Critical — changes physical process |
| **DNP3** | Cold/Warm Restart | Device restart | Critical — service disruption |
| **CIP** | Upload/Download | Programme transfer | Critical — logic modification (UC-ICS-007) |
| **S7Comm** | Upload/Download | Programme transfer | Critical — logic modification |
| **S7Comm** | Stop CPU | Halt controller execution | Critical — denial of control |

---

## Step 4: Ship Zeek Logs to Microsoft Sentinel

### Option A: Azure Monitor Agent (Recommended for Azure Environments)

Configure the Azure Monitor Agent to collect Zeek JSON logs and forward them to a Log Analytics workspace.

```bash
# Install Azure Monitor Agent (follow Microsoft documentation for your OS)
# Configure a Data Collection Rule (DCR) targeting the Zeek log directory

# DCR Configuration (JSON fragment):
# {
#   "dataSources": {
#     "logFiles": [
#       {
#         "streams": ["Custom-ZeekModbus_CL"],
#         "filePatterns": ["/opt/zeek/logs/current/modbus*.log"],
#         "format": "json"
#       },
#       {
#         "streams": ["Custom-ZeekDNP3_CL"],
#         "filePatterns": ["/opt/zeek/logs/current/dnp3*.log"],
#         "format": "json"
#       },
#       {
#         "streams": ["Custom-ZeekCIP_CL"],
#         "filePatterns": ["/opt/zeek/logs/current/cip*.log", "/opt/zeek/logs/current/enip*.log"],
#         "format": "json"
#       },
#       {
#         "streams": ["Custom-ZeekConn_CL"],
#         "filePatterns": ["/opt/zeek/logs/current/conn*.log"],
#         "format": "json"
#       }
#     ]
#   }
# }
```

### Option B: Filebeat

```yaml
# /etc/filebeat/filebeat.yml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /opt/zeek/logs/current/modbus*.log
      - /opt/zeek/logs/current/dnp3*.log
      - /opt/zeek/logs/current/cip*.log
      - /opt/zeek/logs/current/enip*.log
      - /opt/zeek/logs/current/s7comm*.log
      - /opt/zeek/logs/current/conn*.log
    json.keys_under_root: true
    json.add_error_key: true
    fields:
      log_source: "zeek_ics"
    fields_under_root: true

output.logstash:
  hosts: ["your-log-analytics-gateway:5044"]
```

---

## Step 5: Build Custom ASIM Parsers for ICS Protocols

The ASIM parsers normalise Zeek ICS protocol logs into the standard NetworkSession schema, enabling all ASIM-based detection rules to automatically include this data.

### Example: ASIM Parser for Zeek Modbus Logs

```kql
// Custom ASIM NetworkSession parser for Zeek Modbus logs
// Register this parser in the ASIM unifying parser hierarchy
// so that _Im_NetworkSession() includes Zeek Modbus data

let ZeekModbusParser = (
    starttime: datetime = datetime(null),
    endtime: datetime = datetime(null),
    srcipaddr_has_any_prefix: dynamic = dynamic([]),
    dstipaddr_has_any_prefix: dynamic = dynamic([]),
    dstportnumber: int = int(null),
    eventresult: string = '*'
) {
    Custom_ZeekModbus_CL
    | where (isnull(starttime) or TimeGenerated >= starttime)
        and (isnull(endtime) or TimeGenerated <= endtime)
    | extend
        EventType = "NetworkSession",
        EventProduct = "Zeek",
        EventVendor = "CISA ICSNPP",
        EventSchema = "NetworkSession",
        EventSchemaVersion = "0.2.6",
        NetworkProtocol = "Modbus",
        NetworkApplicationProtocol = "Modbus",
        DstPortNumber = 502,
        // Map Zeek fields to ASIM schema
        SrcIpAddr = tostring(column_ifexists("id.orig_h", "")),
        SrcPortNumber = toint(column_ifexists("id.orig_p", "")),
        DstIpAddr = tostring(column_ifexists("id.resp_h", "")),
        EventStartTime = todatetime(column_ifexists("ts", "")),
        // ICS-specific additional fields
        AdditionalFields = bag_pack(
            "ModbusFunction", column_ifexists("func", ""),
            "ModbusUnitId", column_ifexists("unit_id", ""),
            "ModbusException", column_ifexists("exception", "")
        )
    // Apply filters
    | where (array_length(srcipaddr_has_any_prefix) == 0
        or has_any_ipv4_prefix(SrcIpAddr, srcipaddr_has_any_prefix))
    | where (array_length(dstipaddr_has_any_prefix) == 0
        or has_any_ipv4_prefix(DstIpAddr, dstipaddr_has_any_prefix))
    | where (isnull(dstportnumber) or DstPortNumber == dstportnumber)
};
ZeekModbusParser(starttime, endtime, srcipaddr_has_any_prefix,
    dstipaddr_has_any_prefix, dstportnumber, eventresult)
```

### Register the Parser

Follow the Microsoft Sentinel ASIM documentation to register the custom parser in the ASIM unifying parser hierarchy:

1. Save the parser as a KQL function in the Log Analytics workspace
2. Add it to the `_Im_NetworkSession` unifying parser
3. Validate by running `_Im_NetworkSession | where NetworkProtocol == "Modbus" | take 10`

> **Citation:** Microsoft. (2025). *Develop ASIM Parsers*. Available at: https://learn.microsoft.com/en-us/azure/sentinel/normalization-develop-parsers

---

## Step 6: Validate End-to-End Data Flow

### Confirm Data Ingestion in Sentinel

```kql
// Verify Zeek ICS logs are being ingested
Custom_ZeekModbus_CL
| where TimeGenerated > ago(1h)
| summarize EventCount = count(),
    UniqueSources = dcount(column_ifexists("id.orig_h", "")),
    UniqueDestinations = dcount(column_ifexists("id.resp_h", "")),
    FunctionCodes = make_set(column_ifexists("func", ""), 20)
| project EventCount, UniqueSources, UniqueDestinations, FunctionCodes
```

### Confirm ASIM Normalisation

```kql
// Verify that ASIM parser includes Zeek Modbus data
_Im_NetworkSession
| where TimeGenerated > ago(1h)
| where NetworkProtocol == "Modbus"
| summarize count() by SrcIpAddr, DstIpAddr
| take 20
```

### Confirm Detection Rule Coverage

```kql
// Verify that UC-ICS-001 (Unauthorised ICS Protocol Communication)
// is consuming the Zeek Modbus data
_Im_NetworkSession
| where TimeGenerated > ago(1h)
| where NetworkApplicationProtocol in ("Modbus", "DNP3", "EtherNet/IP", "S7Comm")
| join kind=leftanti (
    _GetWatchlist('OT_AssetRegister')
    | project SrcIpAddr = IPAddress
) on SrcIpAddr
| take 10
// If results appear, these are potential UC-ICS-001 detections
```

---

## Troubleshooting

| Issue | Likely Cause | Resolution |
|-------|-------------|------------|
| No ICS protocol logs generated | Parser not loaded; no ICS traffic on monitored interface | Verify `zeek -N` shows parsers; confirm TAP placement captures OT traffic |
| Empty modbus.log | Traffic not on standard port 502 | Check for non-standard Modbus ports; update Zeek port configuration |
| Logs generated but not in Sentinel | Log shipper misconfigured; DCR not targeting correct paths | Verify Filebeat/AMA config; check DCR path patterns |
| ASIM parser returns no results | Parser not registered; table name mismatch | Verify custom table name matches parser reference |
| High log volume | Polling traffic generating excessive events | Add Zeek filters to exclude known-good polling patterns from detailed logs |

---

## Maintenance and Updates

- **Parser updates**: Check the CISA ICSNPP GitHub repository monthly for updated parser versions. Test updates in a lab environment before deploying to production sensors.
- **Log rotation**: Ensure Zeek log rotation aligns with your SIEM ingestion and retention policies.
- **Performance monitoring**: Monitor Zeek sensor CPU and memory utilisation. ICS protocol parsing is CPU-intensive; ensure the sensor is adequately resourced.
- **New protocols**: If new ICS protocols are identified in the environment (via asset discovery or vendor documentation), check ICSNPP for available parsers and deploy as needed.

---

## References

1. CISA. *ICSNPP: Industrial Control Systems Network Protocol Parsers*. GitHub. https://github.com/cisagov/ICSNPP
2. Zeek Project. *Zeek Package Manager Documentation*. https://docs.zeek.org/projects/package-manager/
3. Microsoft. (2025). *Develop ASIM Parsers*. https://learn.microsoft.com/en-us/azure/sentinel/normalization-develop-parsers
4. Microsoft. (2025). *ASIM Network Session Normalization Schema*. https://learn.microsoft.com/en-us/azure/sentinel/normalization-schema-network
