# Sensor Placement Decision Tree

**Book Reference:** Chapter 5 — Defensible Architecture and Segmentation  
**Purpose:** Structured decision framework for determining where to deploy monitoring sensors and agents.  
**Usage:** Walk through each decision tree for each network boundary or asset group.

---

## Decision Tree 1: Network Monitoring Sensor Placement

For each network boundary or conduit, determine whether and how to deploy passive monitoring.

```
Is this boundary on a crown jewel attack path?
  ├─ YES → PRIORITY DEPLOYMENT
  │    │
  │    Is a hardware TAP feasible at this boundary?
  │    ├─ YES → Deploy TAP + Zeek + Suricata
  │    │    │
  │    │    Is this the IDMZ boundary?
  │    │    ├─ YES → Deploy on BOTH IT-facing and OT-facing firewall links
  │    │    └─ NO → Deploy on the conduit link
  │    │
  │    └─ NO (TAP not feasible)
  │         │
  │         Is a SPAN port available on the switch?
  │         ├─ YES → Configure SPAN port + deploy Zeek + Suricata
  │         │    ⚠ Document SPAN port limitations (potential packet loss)
  │         └─ NO → Rely on firewall log analysis for this boundary
  │              ⚠ Document as detection gap — escalate TAP deployment
  │
  └─ NO (not on crown jewel path)
       │
       Is this boundary between Purdue levels?
       ├─ YES → INCLUDE IN ROADMAP (Phase 4+)
       │    Document as future deployment target
       └─ NO → STANDARD MONITORING
            Rely on existing firewall/switch logging
```

### Sensor Configuration Guide

| Boundary Type | Zeek Configuration | Suricata Configuration | SIEM Integration |
|---|---|---|---|
| **IDMZ (Priority 1)** | Full protocol analysis, ICSNPP disabled (IT protocols only at this boundary unless ICS traffic expected) | ET Open + custom IDMZ rules (UC-ICS-012) | ASIM NetworkSession + custom parser |
| **L3/L2 Boundary (Priority 2)** | Full protocol analysis + ICSNPP (Modbus, DNP3, S7Comm, EtherNet/IP) | ET Open + ICS protocol rules (UC-ICS-005, 006, 007) | ASIM NetworkSession + ICS custom tables |
| **L2/L1 Boundary (Priority 3)** | ICSNPP full deployment — primary value is ICS protocol metadata | ICS protocol rules focused on write/config operations | ICS custom tables + ASIM enrichment |
| **Safety Zone (Priority 4)** | Minimal — connection logging only. All connections are anomalous. | Alert on ANY traffic to/from safety zone | Critical severity alerts only |

---

## Decision Tree 2: Endpoint Agent Deployment (EDR / Sysmon)

For each system or system group, determine whether and how to deploy endpoint agents.

```
What Purdue level is this system?
  │
  ├─ Level 4–5 (Enterprise IT)
  │    → Deploy EDR in STANDARD mode (block + detect)
  │    → Deploy Sysmon with full configuration
  │    → Standard IT deployment procedures apply
  │
  ├─ Level 3.5 (IDMZ)
  │    → Deploy EDR in DETECT-ONLY mode initially
  │    → Deploy Sysmon
  │    → Forward Windows Security Events to SIEM
  │    → Validate compatibility with IDMZ services (jump server, historian replica)
  │    → After 30-day observation: consider enabling blocking
  │
  ├─ Level 3 (Site Operations)
  │    → Deploy EDR in DETECT-ONLY mode
  │    → Deploy Sysmon
  │    → Forward Windows Security Events to SIEM
  │    → Validate with OT engineering — test in maintenance window
  │    → After 60-day observation: consider enabling blocking with engineering approval
  │
  ├─ Level 2 (Supervisory Control — HMIs, SCADA, Engineering Workstations)
  │    │
  │    Is this a Windows-based system?
  │    ├─ YES
  │    │    │
  │    │    Has the control system vendor certified the EDR product?
  │    │    ├─ YES → Deploy in DETECT-ONLY mode
  │    │    │    → Whitelist vendor engineering software
  │    │    │    → Schedule any scans during maintenance windows ONLY
  │    │    │    → 90-day observation minimum before considering blocking
  │    │    │    → NEVER enable auto-quarantine without explicit engineering approval
  │    │    │
  │    │    └─ NO (vendor has not certified)
  │    │         → Deploy Sysmon only (lightweight, no blocking capability)
  │    │         → Forward Windows Security Events
  │    │         → Request vendor certification for preferred EDR product
  │    │         → Document as gap in detection coverage assessment
  │    │
  │    └─ NO (Linux, RTOS, or proprietary OS)
  │         → Network monitoring only — no endpoint agent
  │         → Forward syslog where available
  │         → Document as gap
  │
  ├─ Level 1 (PLCs, RTUs, DCS Controllers)
  │    → DO NOT deploy standard EDR agents
  │    → Network monitoring is the primary detection method
  │    │
  │    Does the vendor offer an approved telemetry agent?
  │    ├─ YES → Evaluate with vendor support in test environment
  │    │    → Deploy only with explicit vendor agreement
  │    │    → Monitor performance impact continuously
  │    └─ NO → Network monitoring only
  │
  └─ Level 0 (Physical Process — sensors, actuators)
       → NO AGENT DEPLOYMENT — these are not computing systems
       → Detection relies entirely on network monitoring of Level 1 traffic
```

### EDR Deployment Checklist

Before deploying EDR at Level 2 or Level 3:

| Step | Complete? | Notes |
|------|:---------:|-------|
| Control system vendor consulted on compatibility | ☐ | |
| EDR product tested in representative lab/test environment | ☐ | |
| Engineering software exclusions configured | ☐ | |
| Scan schedules aligned with maintenance windows | ☐ | |
| Auto-quarantine DISABLED (detect-only mode) | ☐ | |
| Change management ticket raised and approved | ☐ | |
| OT engineering sign-off obtained | ☐ | |
| Rollback plan documented | ☐ | |
| Performance baseline captured (CPU, memory, response time) | ☐ | |
| Post-deployment performance validation scheduled | ☐ | |
| Observation period defined (minimum 60–90 days) | ☐ | |

---

## Decision Tree 3: Firewall Log Forwarding

```
Does this firewall sit on a zone boundary?
  ├─ YES
  │    Are firewall logs forwarded to the SIEM?
  │    ├─ YES → Verify ASIM NetworkSession parser is configured
  │    │    → Verify deny logs AND allow logs are forwarded
  │    │    → Verify logs include source IP, destination IP, port, protocol, action
  │    └─ NO → CRITICAL GAP — prioritise log forwarding immediately
  │
  └─ NO (internal / non-boundary firewall)
       → Include in log source roadmap but lower priority
```

---

## Deployment Summary Template

| Location | Sensor Type | Status | Deployment Date | Notes |
|----------|-----------|--------|----------------|-------|
| IDMZ (IT-facing) | TAP + Zeek + Suricata | | | |
| IDMZ (OT-facing) | TAP + Zeek + Suricata | | | |
| IDMZ FW (IT-facing) | Log forwarding | | | |
| IDMZ FW (OT-facing) | Log forwarding | | | |
| L3/L2 Boundary | TAP/SPAN + Zeek | | | |
| L2/L1 Boundary | TAP/SPAN + Zeek + ICSNPP | | | |
| Safety Zone Conduit | TAP + alert-on-any | | | |
| Jump Server | EDR + Sysmon + Auth logs | | | |
| Historian (L3) | EDR + Sysmon + Auth logs | | | |
| Engineering WS (L2) | EDR (detect-only) or Sysmon | | | |
| HMIs (L2) | Sysmon + Auth logs (minimum) | | | |
