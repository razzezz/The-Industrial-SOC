# Legacy OS Log Collection Decision Tree

## Purpose

This decision tree provides a structured approach for determining the optimal log collection method for legacy Windows operating systems commonly found in OT environments. Legacy systems persist in OT because control system applications have not been certified on newer operating systems, the cost and risk of migration exceeds the perceived benefit, or the physical process cannot be taken offline for the duration required to upgrade.

The goal is to extract the maximum security telemetry from each legacy system using the safest available method.

---

## Decision Tree

```
START: What operating system is the OT asset running?
│
├── Windows XP / Server 2003
│   │
│   ├── Q1: Is the system domain-joined?
│   │   ├── YES → Use Windows Event Forwarding (WEF)
│   │   │         Configure as WEF source, forward to a modern
│   │   │         Windows Event Collector server in the IDMZ.
│   │   │         Collect: Security, System, Application logs.
│   │   │         Note: Limited Event IDs available (no 4688 
│   │   │         command-line auditing on XP/2003).
│   │   │
│   │   └── NO → Q2: Can a scheduled task run on the system?
│   │       ├── YES → Use scripted log export
│   │       │         Schedule a task to export Event Logs to a
│   │       │         network share using wevtutil or custom script.
│   │       │         Ingest from share using Filebeat/AMA on a
│   │       │         collector server.
│   │       │         Frequency: Every 15 minutes minimum.
│   │       │
│   │       └── NO → DOCUMENT AS GAP
│   │                Record in Telemetry Source Inventory.
│   │                Compensate: Deploy network TAP on the
│   │                switch port serving this system.
│   │                Monitor all traffic to/from the device
│   │                via Zeek/Suricata.
│   │
│   └── ALWAYS: Supplement with network monitoring.
│       XP/2003 endpoint telemetry is inherently limited.
│       Network monitoring around the device is essential.
│
├── Windows Server 2008 / 2008 R2
│   │
│   ├── Q1: Can the Azure Monitor Agent (legacy) be installed?
│   │   ├── YES → Deploy legacy Log Analytics Agent (MMA)
│   │   │         Note: MMA is approaching deprecation — plan
│   │   │         for migration to newer OS where possible.
│   │   │         Collect: Security, System, Application logs.
│   │   │         Event ID 4688 with command-line auditing IS
│   │   │         available on Server 2008 R2 with updates.
│   │   │
│   │   └── NO → Q2: Is the system domain-joined?
│   │       ├── YES → Use Windows Event Forwarding (WEF)
│   │       │         More reliable on 2008/R2 than on XP/2003.
│   │       │         Configure subscription on modern collector.
│   │       │
│   │       └── NO → Use scripted log export or Syslog agent
│   │                NXLog Community Edition supports Server 2008.
│   │                Forward Windows Event Logs as syslog to the
│   │                SIEM via a collector in the IDMZ.
│   │
│   ├── Q3: Does the EDR vendor support Server 2008 R2?
│   │   ├── YES → Consider EDR deployment (detect-only mode)
│   │   │         Some vendors (e.g., CrowdStrike) maintain
│   │   │         legacy agent support for 2008 R2.
│   │   │         Validate with OT engineering before deploying.
│   │   │
│   │   └── NO → Deploy Sysmon if system supports it
│   │            Sysmon supports Server 2008 R2 with .NET 4.5+.
│   │            Provides process creation, network connections,
│   │            and file system monitoring.
│   │
│   └── ALWAYS: Plan for OS migration on the roadmap.
│       Server 2008/R2 is deeply unsupported. Every month
│       it remains increases vulnerability exposure.
│
├── Windows Embedded / IoT Enterprise
│   │
│   ├── Q1: Which embedded variant?
│   │   ├── Windows Embedded Standard 7 / POSReady 7
│   │   │   → Treat as Windows 7. Most agents work.
│   │   │     WEF, MMA (legacy), Sysmon all viable.
│   │   │     EDR: Check vendor support matrix.
│   │   │
│   │   ├── Windows 10 IoT Enterprise LTSC
│   │   │   → Treat as standard Windows 10.
│   │   │     Full agent support (AMA, Sysmon, EDR).
│   │   │     This is the modern HMI standard OS.
│   │   │
│   │   └── Windows Embedded Compact / CE
│   │       → DOCUMENT AS GAP
│   │         No standard agent support.
│   │         Network monitoring is the only option.
│   │         Deploy TAP on network segment.
│   │
│   └── ALWAYS: Validate any agent deployment with the
│       HMI/SCADA vendor. Embedded systems may have
│       write filters or reduced resources that affect
│       agent operation.
│
├── Proprietary RTOS / Embedded Linux (PLCs, RTUs)
│   │
│   └── DOCUMENT AS GAP — No endpoint agents possible.
│       Compensate entirely with network monitoring:
│       - Deploy Zeek + Suricata TAP on network segment
│       - Build communication baseline for the device
│       - Alert on any deviation from baseline
│       - Monitor ICS protocol function codes (UC-ICS-001,
│         UC-ICS-002, UC-ICS-005, UC-ICS-006, UC-ICS-007)
│
└── Non-Windows (Linux-based OT systems)
    │
    ├── Q1: Is rsyslog or syslog-ng available?
    │   ├── YES → Forward auth.log, syslog, kern.log
    │   │         to SIEM via syslog connector.
    │   │         Enable auditd for detailed process
    │   │         and file access logging.
    │   │
    │   └── NO → Use scripted log export if possible.
    │            Otherwise, DOCUMENT AS GAP and
    │            compensate with network monitoring.
    │
    └── Q2: Does the EDR vendor support this Linux version?
        ├── YES → Deploy EDR (detect-only mode).
        └── NO → Deploy OSSEC or Wazuh as lightweight
                 host-based IDS alternative.
```

---

## Key Principles

1. **Document every gap.** A known gap can be compensated for. An unknown gap is an adversary blind spot.

2. **Network monitoring compensates for endpoint gaps.** When you cannot see what is happening ON a device, monitor what is happening AROUND it via network traffic analysis.

3. **Plan for migration.** Every legacy system should have a migration plan on the long-term roadmap, even if migration is years away. Include the security limitations of the current OS in the business case for migration.

4. **Validate with engineering.** Any agent deployment or configuration change on a legacy OT system must be tested and approved by OT engineering. Legacy systems are often the most fragile and the most critical.

5. **Prioritise crown jewel adjacency.** If a legacy system interacts with crown jewel assets (engineering workstations that programme Tier 1 PLCs, for example), its telemetry gap is a high priority. If it is isolated from crown jewels, the gap may be acceptable with network monitoring as compensation.
