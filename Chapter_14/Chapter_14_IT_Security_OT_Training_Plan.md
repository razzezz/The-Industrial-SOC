# IT Security OT Training Plan

## Purpose

This training plan develops the OT-specific competencies that SOC analysts, detection engineers, and threat hunters require to effectively monitor, triage, and investigate alerts in industrial control system environments. It is designed for cybersecurity professionals who are competent in IT security operations but have limited or no prior exposure to operational technology.

The plan follows a progressive structure: foundational knowledge first, then operational competency, then advanced skills. Each module includes learning objectives, delivery method, assessment criteria, and estimated time.

---

## Training Tracks

### Track 1: Foundational OT Knowledge (All SOC Analysts — Complete Within 60 Days)

| Module | Learning Objectives | Delivery Method | Duration | Assessment |
|--------|-------------------|-----------------|----------|------------|
| **1.1 — Plant Floor Orientation** | Physically visit the operational environment. Identify PLCs, HMIs, RTUs, SIS, historians, and engineering workstations. Understand the physical process being controlled. | Guided site visit with OT Engineering escort | 4 hours | Debrief with OT SME; analyst describes the process and identifies 5 key assets |
| **1.2 — The Purdue Model** | Describe all Purdue Levels (0–5). Identify where key assets sit. Understand the IDMZ concept. Explain why network segmentation matters for OT. | Self-study (Chapter 1 + Chapter 5) + classroom session | 2 hours | Written quiz: map a provided network diagram to Purdue Levels |
| **1.3 — ICS Protocols Overview** | Identify Modbus TCP/RTU, DNP3, OPC UA, S7Comm, EtherNet/IP, and Profinet. Understand the basic function of each. Recognise common function codes (Modbus read/write coils, read/write registers). | Classroom session with packet capture examples | 3 hours | Identify protocols and function codes from provided Zeek/PCAP samples |
| **1.4 — Crown Jewels & Asset Criticality** | Understand the crown jewel classification system (Tiers 1–5). Explain why Safety Instrumented Systems are Tier 1. Use the OT_AssetRegister and OT_CrownJewels watchlists in Sentinel. | Self-study (Chapter 6) + hands-on Sentinel lab | 2 hours | Given an alert, correctly identify the asset's Purdue Level and crown jewel tier using watchlists |
| **1.5 — The ICS Cyber Kill Chain** | Describe Stage 1 and Stage 2 of the ICS Cyber Kill Chain. Understand how IT compromises translate to OT access. Recognise the key transition points. | Classroom session (Chapter 1 + Chapter 3 case studies) | 2 hours | Given a scenario, identify the Kill Chain stage and likely next adversary action |
| **1.6 — OT Threat Landscape** | Identify the primary threat actors targeting ICS (Volt Typhoon/VOLTZITE, Seashell Blizzard/ELECTRUM, Sandworm). Understand their TTPs at a high level. Recognise sector-specific targeting. | Briefing from CTI function (Chapter 10) | 2 hours | Name 3 threat actors relevant to the organisation's sector and describe their primary objective |

**Total Track 1:** ~15 hours over 60 days

---

### Track 2: Operational OT Competency (All SOC Analysts — Complete Within 120 Days)

| Module | Learning Objectives | Delivery Method | Duration | Assessment |
|--------|-------------------|-----------------|----------|------------|
| **2.1 — OT Alert Triage Framework** | Apply the four-dimension triage framework (Indicator Confidence, Asset Criticality, Potential Consequence, Operational Context). Follow the triage decision flow for OT alerts. | Classroom + scenario-based exercises (Chapter 11) | 3 hours | Correctly triage 10 simulated OT alerts with documented rationale |
| **2.2 — Maintenance Window Awareness** | Query the OT_MaintenanceWindows watchlist. Understand how maintenance windows affect alert triage. Recognise legitimate engineering patterns during maintenance. | Hands-on Sentinel lab | 2 hours | Given 5 alerts during and outside maintenance windows, make correct triage decisions |
| **2.3 — Engineering Escalation** | Construct a structured escalation to engineering (asset, activity, context, question, urgency). Understand when escalation is mandatory (Tier 1 assets, Purdue L0–2). | Role-play exercise with OT SME | 2 hours | Deliver a simulated escalation that receives satisfactory feedback from the OT SME |
| **2.4 — Shadow Engineering Session** | Observe a maintenance window or engineering session from the SOC perspective. Correlate observed engineering activity with telemetry in Sentinel. | Scheduled observation during actual maintenance window | 4 hours | Written debrief documenting what engineering activity was observed and how it appeared in the SIEM |
| **2.5 — SOAR Containment Boundary** | Understand which automated containment actions are permitted at each Purdue Level. Explain why automated isolation below L3.5 is prohibited. | Self-study (Chapter 11) + lab exercise | 1 hour | Correctly identify permitted vs. prohibited automated actions for 5 scenarios |
| **2.6 — ICS Detection Rules** | Understand the structure of ICS-specific detection rules in Sentinel. Review 5 live OT detection rules, understand their logic, and explain what they detect. | Guided walkthrough with Detection Engineer | 3 hours | Explain 3 detection rules in plain language to a non-technical colleague |

**Total Track 2:** ~15 hours over 120 days (builds on Track 1)

---

### Track 3: Advanced OT Security (Detection Engineers, Threat Hunters, OT SME — Complete Within 180 Days)

| Module | Learning Objectives | Delivery Method | Duration | Assessment |
|--------|-------------------|-----------------|----------|------------|
| **3.1 — ICS Protocol Deep Dive** | Parse Modbus, DNP3, and S7Comm at the packet level. Identify normal vs. anomalous protocol behaviour. Write Zeek scripts for protocol analysis. | Hands-on lab with PCAPs + Zeek | 8 hours |Write a Zeek notice for an anomalous Modbus function code pattern |
| **3.2 — OT Detection Engineering** | Write ICS-specific detection rules using the ICS Detection Use Case Template. Account for maintenance windows, asset criticality, and operational context in rule logic. | Hands-on Sentinel lab (Chapter 7) | 8 hours | Develop and deploy 2 new ICS detection rules that pass testing and peer review |
| **3.3 — OT Threat Hunting** | Develop hunting hypotheses from OT threat intelligence. Execute structured hunts in OT telemetry. Document findings using the hunting template. | Guided hunt with OT SME (Chapter 9) | 8 hours | Conduct an independent OT threat hunt and present findings to the team |
| **3.4 — OT Incident Response** | Lead the cybersecurity response for an OT incident. Coordinate with engineering on containment decisions. Manage evidence collection from both IT and OT sources. | Tabletop exercise (lead role) + Chapter 11/12 study | 4 hours | Successfully lead a tabletop exercise and produce an acceptable AAR |

**Total Track 3:** ~28 hours over 180 days (builds on Tracks 1 and 2)

---

### Track 4: External Training (Budget-Dependent)

| Course | Provider | Target Audience | Duration | Recommended Priority |
|--------|----------|----------------|----------|---------------------|
| **ICS410: ICS/SCADA Security Essentials** | SANS Institute | All SOC analysts handling OT alerts | 5 days | High — foundational certification for OT security |
| **ICS515: ICS Visibility, Detection, and Response** | SANS Institute | Detection Engineers, Threat Hunters, OT SME | 5 days | High — directly aligned to this book's methodology |
| **ICS456: Essentials for NERC Critical Infrastructure Protection** | SANS Institute | Analysts in power/energy sector | 5 days | Medium — sector-specific |
| **Vendor-Specific Training** | OT platform vendor (e.g., Siemens, Schneider, Rockwell) | OT SME, Detection Engineers | Varies | Medium — deepens protocol and architecture knowledge |

---

## Competency Assessment Framework

Each analyst is assessed against the following competency levels:

| Level | Description | Criteria |
|-------|-------------|----------|
| **Awareness** | Can recognise OT assets, protocols, and concepts when encountered | Track 1 complete; quiz score ≥ 80% |
| **Practitioner** | Can triage OT alerts, escalate appropriately, and participate in OT investigations | Tracks 1 + 2 complete; scenario assessment passed |
| **Specialist** | Can write OT detection rules, conduct OT threat hunts, and lead OT incident response | Tracks 1 + 2 + 3 complete; SANS ICS410 or ICS515 certified |

**Minimum competency for OT alert triage:** Practitioner level.
**Minimum competency for OT detection engineering:** Specialist level.

---

## Ongoing Development

- **Quarterly:** Participate in at least one monthly tabletop exercise involving an OT scenario.
- **Semi-annually:** Conduct or participate in at least one shadow engineering session.
- **Annually:** Complete a refresher assessment (10 OT triage scenarios) to maintain Practitioner or Specialist certification.
- **Ongoing:** Attend weekly IT/OT sync meetings to maintain operational context and engineering relationships.

---

*Training records are maintained by the CSIRT Lead and reported at the quarterly programme review. Training completion is tracked as a collaboration metric (Joint Training Completion %).*
