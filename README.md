# Security Operations Centre for Operational Technology
## Practitioner's Toolkit, GitHub Companion Repository

This repository contains the templates, scripts, detection rules, hunting queries, and checklists referenced in **Security Operations Centre for Operational Technology: A Practitioner's Guide to Defending Industrial Control Systems**.

Each chapter has its own folder. Assets are organised so they can be deployed alongside the chapter that introduces them.

## Status Conventions

Every asset in the tables below is annotated with one of:

| Marker | Meaning |
|---|---|
| Available | The file is present in this folder and matches the name used in the book. |
| Planned | The file is referenced in the book but is not yet present in this folder. |

A full audit of referenced vs. present assets, naming inconsistencies, and structural recommendations is captured in `ASSET_AUDIT_REPORT.md` in this folder.

## Repository Structure

```
├── README.md
├── Chapter_01/   Defining the Industrial Landscape
├── Chapter_02/   The IT vs. OT Divergence
├── Chapter_03/   Case Studies of Landmark Incidents
├── Chapter_04/   The Regulatory Roadmap
├── Chapter_05/   Defensible Architecture and Segmentation
├── Chapter_06/   Phase 1, Know (Asset Inventory)
├── Chapter_07/   Phase 2, Assess and Observe
├── Chapter_08/   Detection Engineering
├── Chapter_09/   The OT Threat Hunting Mindset
├── Chapter_10/   Cyber-Physical Intelligence
├── Chapter_11/   Purpose-Built Incident Response
├── Chapter_12/   Digital Forensics and Lessons Learned
├── Chapter_13/   Tooling Selection and Integration
├── Chapter_14/   Cross-Functional Collaboration
├── Chapter_15/   The Continuous Improvement Cycle
├── Chapter_16/   Leveraging AI and Machine Learning
├── templates/    Shared cross-chapter templates (Planned)
└── watchlists/   Microsoft Sentinel watchlist schemas
```

Detection rules are kept inside each chapter folder under `detection-rules/{kql,suricata,zeek}/` where a chapter introduces multiple rules. Single rules live at the chapter root. The canonical detection library that supports the whole book (UC-ICS-001 through UC-ICS-009 plus `ATTCK_ICS_Coverage_Assessment.kql`) is targeted at `Chapter_07/detection-rules/` as the chapter where the rules are introduced.

## Chapter 1: Defining the Industrial Landscape

Foundational reference assets for understanding ICS environments.

| Asset | Description | Filepath | Status |
|---|---|---|---|
| Purdue Model Reference | Visual reference for the Purdue Enterprise Reference Architecture used throughout the book | `Chapter_01/Chapter_01_Purdue_Model_Reference.pdf` | Available |
| Five Questions to Ask Your OT Team | Structured worksheet for the SOC analyst's first conversation with OT engineering | `Chapter_01/Chapter_01_Five_Questions_Worksheet.md` | Available |
| Glossary of Essential OT Terms | Glossary of ICS/OT terminology for SOC teams | `Chapter_01/Chapter_01_Glossary.md` | Rename pending (currently at `Book/` root) |

## Chapter 2: The IT vs. OT Divergence

Materials for translating between IT security practice and OT operational reality.

| Asset | Description | Filepath | Status |
|---|---|---|---|
| IT vs. OT Comparison Matrix | Side-by-side comparison of priorities, lifecycles, patching, and trust models | `Chapter_02/Chapter_02_IT_vs_OT_Comparison_Matrix.md` | Available |
| Safe vs. Unsafe Security Activities | Quick reference for which IT security activities are safe to perform in OT and which are not | `Chapter_02/Chapter_02_Safe_Unsafe_Security_Activities.md` | Available |
| IT Security to OT MOU Template | Sample memorandum of understanding between IT Security and OT teams | `Chapter_02/Chapter_02_IT_Security_OT_MOU_Template.md` | Available |

## Chapter 3: Case Studies of Landmark Incidents

Templates for analysing and learning from historical ICS incidents.

| Asset | Description | Filepath | Status |
|---|---|---|---|
| Incident Timeline Template | Template for laying out incident progression alongside the ICS Cyber Kill Chain | `Chapter_03/Chapter_03_Incident_Timeline_Template.md` | Available |
| OT Kill Chain Mapping Worksheet | Worksheet for mapping adversary tradecraft to the ICS Cyber Kill Chain | `Chapter_03/Chapter_03_OT_Kill_Chain_Mapping_Worksheet.md` | Available |
| Human Attack Surface Assessment | Checklist for assessing insider, social engineering, and physical access risks in OT | `Chapter_03/Chapter_03_Human_Attack_Surface_Assessment.md` | Available |

## Chapter 4: The Regulatory Roadmap

Templates and checklists for navigating OT security compliance.

| Asset | Description | Filepath | Status |
|---|---|---|---|
| Regulatory Applicability Checklist | Structured checklist for determining which frameworks apply by sector, geography, and supply chain | `Chapter_04/Chapter_04_Regulatory_Applicability_Checklist.md` | Available |
| NCSC CAF SOC Self-Assessment | Self-assessment template covering Objectives C and D with evidence tracking | `Chapter_04/Chapter_04_NCSC_CAF_SOC_Self_Assessment.md` | Available |
| NIS 2 SOC Compliance Checklist | NIS 2 requirements that directly impact SOC operations | `Chapter_04/Chapter_04_NIS2_SOC_Compliance_Checklist.md` | Available |
| Framework Mapping Matrix | Cross-reference of overlapping requirements across NCSC CAF v4.0, NIS 2, NIST SP 800-82r3, and ISA/IEC 62443 | `Chapter_04/Chapter_04_Framework_Mapping_Matrix.md` | Available |
| Vendor Security Requirements Template | Template for setting security requirements with OT vendors, aligned to PSTI Act and ISA/IEC 62443-4-2 | `Chapter_04/Chapter_04_Vendor_Security_Requirements_Template.md` | Available |

## Chapter 5: Defensible Architecture and Segmentation

Assets for implementing defensible architecture and monitoring critical boundaries.

| Asset | Description | Filepath | Status |
|---|---|---|---|
| Crown Jewel Identification Worksheet | Scoring framework for prioritising crown jewel processes across safety, financial, environmental, and regulatory dimensions | `Chapter_05/Chapter_05_Crown_Jewel_Identification_Worksheet.md` | Available |
| Network Segmentation Priority Matrix | Scoring template for prioritising segmentation based on crown jewel proximity and threat intelligence | `Chapter_05/Chapter_05_Network_Segmentation_Priority_Matrix.md` | Available |
| Vendor Access Monitoring Baseline | Structured format for documenting vendor normal access patterns | `Chapter_05/Chapter_05_Vendor_Access_Monitoring_Baseline.md` | Available |
| OT Credential Risk Assessment | Checklist for shared accounts, defaults, and service accounts in OT environments | `Chapter_05/Chapter_05_OT_Credential_Risk_Assessment.md` | Available |
| Attack Path Documentation Template | Template for documenting attack paths from initial access to crown jewel assets | `Chapter_05/Chapter_05_Attack_Path_Documentation_Template.md` | Available |
| Sensor Placement Decision Tree | Decision tree for placing passive sensors across the Purdue Model | `Chapter_05/Chapter_05_Sensor_Placement_Decision_Tree.md` | Available |
| UC-ICS-010, Vendor Session Anomaly | KQL rule correlating vendor authentication with `OT_MaintenanceWindows` | `Chapter_05/detection-rules/kql/UC-ICS-010_Vendor_Session_Anomaly.kql` | Available |
| UC-ICS-011, IDMZ Jump Server Anomaly | KQL rule for baseline jump server authentication patterns | `Chapter_05/detection-rules/kql/UC-ICS-011_IDMZ_Jump_Server_Anomaly.kql` | Available |
| UC-ICS-012, IDMZ Boundary Monitor | Suricata signatures for ICS protocol violations at the IDMZ | `Chapter_05/detection-rules/suricata/UC-ICS-012_IDMZ_Boundary_Monitor.rules` | Available |
| IDMZ Connection Pair Baseline | Zeek script for connection pair baseline monitoring at the IDMZ | `Chapter_05/detection-rules/zeek/Chapter_05_IDMZ_Connection_Baseline.zeek` | Available |

Note: UC-ICS-010 and UC-ICS-011 are also used by Chapter 7 for different rule purposes ("Anomalous Authentication on OT Systems" and "SIS Communication Anomaly"). Two distinct rules currently share the same UC-ICS number. This is flagged in `ASSET_AUDIT_REPORT.md`.

## Chapter 6: Phase 1, Know (Asset Inventory)

Templates and queries for building and maintaining the OT asset inventory.

| Asset | Description | Filepath | Status |
|---|---|---|---|
| OT Asset Register Template | CSV schema defining minimum viable OT asset register fields for `OT_AssetRegister` watchlist | `Chapter_06/Chapter_06_OT_AssetRegister_Template.csv` | Available |
| Known Knowns Interview Guide | Structured questionnaire for discovery sessions with OT engineering | `Chapter_06/Chapter_06_Known_Knowns_Interview_Guide.md` | Available |
| Crown Jewel Decision Tree | Rapid-assessment tree for initial crown jewel classification during interviews | `Chapter_06/Chapter_06_Crown_Jewel_Decision_Tree.md` | Available |
| Asset Visibility Maturity Self-Assessment | Checklist for evaluating maturity level 1 to 5 of OT asset visibility | `Chapter_06/Chapter_06_Maturity_Self_Assessment.md` | Available |
| Attack Path Mapping Worksheet | Template for documenting attack paths from initial access to crown jewels | `Chapter_06/Chapter_06_Attack_Path_Mapping_Worksheet.md` | Available |
| IT/OT Asset Discovery Query | KQL queries mining AD, DHCP, and network sessions for OT-connected assets | `Chapter_06/detection-rules/kql/Chapter_06_IT_OT_Asset_Discovery.kql` | Available |
| AD Authentication Discovery | KQL query for OT-relevant authentication signals in Active Directory | `Chapter_06/Chapter_06_AD_Auth_Discovery.kql` | Available |
| DHCP Discovery | KQL query for DHCPACK events on OT subnets | `Chapter_06/Chapter_06_DHCP_Discovery.kql` | Available |
| Firewall Discovery | KQL query for identifying OT-active devices from firewall logs | `Chapter_06/Chapter_06_Firewall_Discovery.kql` | Available |
| UC-ICS-013, New OT Device Detection | KQL rule detecting network sessions involving IPs not in `OT_AssetRegister` | `Chapter_06/detection-rules/kql/UC-ICS-013_New_OT_Device_Detection.kql` | Available |

## Chapter 7: Phase 2, Assess and Observe

Detection rules, telemetry deployment guides, and SIEM use cases for OT monitoring. The canonical detection library (UC-ICS-001 through UC-ICS-009 plus `ATTCK_ICS_Coverage_Assessment.kql`) is targeted at this chapter's `detection-rules/` subfolder.

| Asset | Description | Filepath | Status |
|---|---|---|---|
| Telemetry Source Inventory Template | Template for inventorying current telemetry sources and mapping to ATT&CK for ICS | `Chapter_07/Chapter_07_Telemetry_Source_Inventory_Template.csv` | Available |
| Legacy OS Log Collection Decision Tree | Decision framework for collecting logs from legacy OT systems | `Chapter_07/Chapter_07_Legacy_OS_Log_Collection_Decision_Tree.md` | Available |
| EDR Deployment Decision Tree | Decision tree for determining EDR deployment appropriateness on OT systems | `Chapter_07/Chapter_07_EDR_Deployment_Decision_Tree.md` | Available |
| EDR Configuration Checklist for OT | Configuration checklist ensuring EDR operates safely in OT | `Chapter_07/Chapter_07_EDR_Configuration_Checklist.md` | Available |
| Zeek ICS Parser Deployment Guide | Step-by-step guide for deploying CISA ICSNPP parsers with Microsoft Sentinel | `Chapter_07/Chapter_07_Zeek_ICS_Parser_Deployment_Guide.md` | Available |
| ATT&CK for ICS Detection Coverage Matrix | CSV matrix mapping detection coverage to ATT&CK for ICS techniques | `Chapter_07/Chapter_07_ATTCK_ICS_Detection_Coverage_Matrix.csv` | Available |
| Telemetry Gap Assessment | KQL query identifying OT assets in `OT_AssetRegister` without corresponding telemetry | `Chapter_07/detection-rules/kql/Chapter_07_Telemetry_Gap_Assessment.kql` | Available (duplicate exists at chapter root, see audit report) |
| Logging Coverage Assessment | KQL query summarising logging coverage by source and asset type | `Chapter_07/Chapter_07_Logging_Coverage_Assessment.kql` | Available |
| Communication Baseline | KQL query producing a 30-day communication baseline for OT assets | `Chapter_07/Chapter_07_Communication_Baseline.kql` | Available |
| ASIM Parser for Zeek Conn | Custom ASIM parser KQL projecting Zeek conn.log into ASIM `NetworkSession` | `Chapter_07/Chapter_07_ASIM_Parser_Zeek_Conn.kql` | Available |
| Maintenance Window Annotation | Reusable KQL pattern joining detections with `OT_MaintenanceWindows` for suppression with auditability | `Chapter_07/Chapter_07_Maintenance_Window_Annotation.kql` | Available |
| UC-ICS-010, Anomalous Authentication on OT Systems | KQL rule detecting authentication anomalies on OT-registered assets | `Chapter_07/detection-rules/kql/UC-ICS-010_Anomalous_Authentication_OT_Systems.kql` | Available |

### Core Detection Library (introduced in Chapter 7)

| Asset | Description | Target Path | Status |
|---|---|---|---|
| UC-ICS-001, Unauthorised ICS Protocol Communication | Detects new source to controller communication (T0886, T0822) | `Chapter_07/detection-rules/kql/UC-ICS-001_Unauthorised_ICS_Protocol_Communication.kql` | Rename pending (currently at `Book/` root) |
| UC-ICS-002, ICS Write Command Outside Maintenance | Detects write commands outside maintenance windows (T0855, T0821) | `Chapter_07/detection-rules/kql/UC-ICS-002_ICS_Write_Command_Outside_Maintenance.kql` | Rename pending (currently at `Book/` root) |
| UC-ICS-003, IT/OT Boundary Traversal | Detects direct IT-to-OT communication bypassing IDMZ (T0886, T0822) | `Chapter_07/detection-rules/kql/UC-ICS-003_IT_OT_Boundary_Traversal.kql` | Rename pending (currently at `Book/` root) |
| UC-ICS-004, Credential Brute Force Against OT | Detects brute force attempts against OT systems (T0812, T0859) | `Chapter_07/detection-rules/kql/UC-ICS-004_Credential_Brute_Force_OT.kql` | Rename pending (currently at `Book/` root) |
| UC-ICS-005, Modbus Diagnostic Function Abuse | Suricata rules detecting Modbus FC8 diagnostic abuse (T0814, T0816) | `Chapter_07/detection-rules/suricata/UC-ICS-005_Modbus_Diagnostic_Functions.rules` | Rename pending (currently at `Book/` root) |
| UC-ICS-006, DNP3 Unauthorised Operations | Suricata rules detecting DNP3 write/control/restart (T0855, T0831, T0816) | `Chapter_07/detection-rules/suricata/UC-ICS-006_DNP3_Unauthorised_Operations.rules` | Rename pending (currently at `Book/` root) |
| UC-ICS-007, CIP Programme Operations | Suricata rules detecting EtherNet/IP CIP programme upload/download (T0821, T0845) | `Chapter_07/detection-rules/suricata/UC-ICS-007_CIP_Programme_Operations.rules` | Rename pending (currently at `Book/` root) |
| UC-ICS-008, Modbus Function Code Scan | Zeek-based behavioural detection via Sentinel (T0840, T0846) | `Chapter_07/detection-rules/kql/UC-ICS-008_Modbus_Function_Code_Scan.kql` | Rename pending (currently at `Book/` root) |
| UC-ICS-009, Cross-Domain Lateral Movement | Cross-domain lateral movement correlation (T0822, T0859) | `Chapter_07/detection-rules/kql/UC-ICS-009_Cross_Domain_Lateral_Movement.kql` | Rename pending (currently at `Book/` root) |
| ATT&CK for ICS Coverage Assessment | Detection coverage gap analysis query mapping enabled rules to ATT&CK for ICS tactics | `Chapter_07/detection-rules/kql/ATTCK_ICS_Coverage_Assessment.kql` | Rename pending (currently at `Book/` root) |

## Chapter 8: Detection Engineering

Detection engineering lifecycle, testing, tuning, and the SIS use case introduced in this chapter.

| Asset | Description | Filepath | Status |
|---|---|---|---|
| Detection Engineering Lifecycle | Description of the intake to retirement detection engineering lifecycle for OT | `Chapter_08/Chapter_08_Detection_Engineering_Lifecycle.md` | Planned |
| Testing and Validation Checklist | Structured checklist for validating detection rules before production | `Chapter_08/Chapter_08_Testing_Validation_Checklist.md` | Available |
| Detection Tuning Log | CSV template for recording detection tuning events, rule ID, date, outcome | `Chapter_08/Chapter_08_Detection_Tuning_Log.csv` | Available |
| Threat-to-Detection Priority Matrix | Matrix mapping threat actor TTPs to detection priorities | `Chapter_08/Chapter_08_Threat_Detection_Priority_Matrix.md` | Available |
| UC-ICS-011, SIS Communication Anomaly | KQL rule detecting anomalous communication to safety instrumented systems | `Chapter_08/UC-ICS-011_SIS_Communication_Anomaly.kql` | Available (note: UC-ICS-011 number is reused in Ch 5; see audit report) |

## Chapter 9: The OT Threat Hunting Mindset

Hunting methodologies, queries, and frameworks for proactive threat detection.

| Asset | Description | Filepath | Status |
|---|---|---|---|
| Hunting Hypothesis Template | Template for hypothesis-driven hunt documentation | `Chapter_09/Chapter_09_Hunting_Hypothesis_Template.md` | Available |
| Hunt Report Template | Comprehensive hunt execution and findings template | `Chapter_09/Chapter_09_Hunt_Report_Template.md` | Available |
| ATT&CK for ICS Technique Coverage | Technique-level coverage assessment including hunting | `Chapter_09/Chapter_09_ATTCK_ICS_Technique_Coverage.kql` | Available |
| Hunting Query Library | KQL hunting queries for firmware ops, covert channels, network reconnaissance | `Chapter_09/Chapter_09_Hunting_Queries.kql` | Available |
| Hunt-ICS-001, Firmware Operations (KQL) | KQL hunting query for Modbus function codes 43 and 23 indicating firmware operations | `Chapter_09/Chapter_09_Hunt_ICS_001_Firmware_Ops.kql` | Available |
| Hunt-ICS-001, Firmware Operations (Zeek) | Zeek script for local detection of firmware-related Modbus operations | `Chapter_09/Chapter_09_Hunt_ICS_001_Firmware_Ops.zeek` | Available |
| Hunt-ICS-002, Covert Channels in Modbus | KQL hunting query for covert channels in Modbus register usage | `Chapter_09/Chapter_09_Hunt_ICS_002_Covert_Channels.kql` | Available |
| Hunt-ICS-003, Network Reconnaissance | KQL hunting query for passive recon from compromised workstations | `Chapter_09/Chapter_09_Hunt_ICS_003_Reconnaissance.kql` | Available |
| Hunt-ICS-003, EtherNet/IP Discovery | Suricata rules for OT-specific reconnaissance including EtherNet/IP and Profinet DCP | `Chapter_09/Chapter_09_Hunt_ICS_003_EtherNetIP_Discovery.rules` | Available |
| Zeek Hunting Scripts | Zeek scripts for firmware detection and protocol anomaly identification | `Chapter_09/Chapter_09_Zeek_Hunting.zeek` | Available |
| Suricata Hunting Signatures | Suricata rules for OT reconnaissance | `Chapter_09/Chapter_09_Suricata_Hunting.rules` | Available |
| NetworkX Anomaly Hunt | Python script using NetworkX to identify structural anomalies in communication graphs | `Chapter_09/Chapter_09_NetworkX_Anomaly_Hunt.py` | Available |

## Chapter 10: Cyber-Physical Intelligence

CTI frameworks, templates, and detections for OT security operations.

| Asset | Description | Filepath | Status |
|---|---|---|---|
| Intelligence Requirements Template | Template for documenting intelligence requirements with priority and satisfaction status | `Chapter_10/Chapter_10_Intelligence_Requirements_Template.md` | Available |
| Collection Management Framework Worksheet | Mapping worksheet connecting intelligence requirements to collection sources | `Chapter_10/Chapter_10_CMF_Worksheet.md` | Available |
| Intrusion Analysis Report Template | Standardised format for processing threat intelligence into structured, actionable data | `Chapter_10/Chapter_10_Intrusion_Analysis_Report_Template.md` | Available |
| Threat Model Template | Template for scenario-based threat models populated with adversary TTPs | `Chapter_10/Chapter_10_Threat_Model_Template.md` | Available |
| Adversary Profile Template | Living document template for maintaining threat actor profiles | `Chapter_10/Chapter_10_Adversary_Profile_Template.md` | Available |
| Vulnerability Intelligence Assessment Template | Structured format for ICS vulnerability intelligence workflow | `Chapter_10/Chapter_10_Vulnerability_Intelligence_Assessment_Template.md` | Available |
| Strategic Briefing Template | One-to-two page template for delivering strategic intelligence to leadership | `Chapter_10/Chapter_10_Strategic_Briefing_Template.md` | Available |
| CTI-ICS-001, Credential Extraction to OT Pivot | CTI-driven KQL rule for the Volt Typhoon (VOLTZITE) credential extraction to OT pivot pattern | `Chapter_10/Chapter_10_CTI_ICS_001_Credential_Extraction_OT_Pivot.kql` | Available |
| Hunt-CTI-001, OT Documentation Access | Hunting query for first-time access to OT engineering documentation repositories | `Chapter_10/Chapter_10_Hunt_CTI_001_OT_Documentation_Access.kql` | Available |

Note: These files were renamed from the canonical `CTI-ICS-001_*.kql` and `Hunt-CTI-001_*.kql` form to the `Chapter_10_*` form so the filenames match the references in the chapter body. Deprecation stubs sit at the old paths and should be hard-deleted via Windows Explorer.

## Chapter 11: Purpose-Built Incident Response

IR playbooks, tabletop scenarios, and communication templates for OT environments.

| Asset | Description | Filepath | Status |
|---|---|---|---|
| IR Playbook Template | Customisable eight-phase playbook for OT incident response | `Chapter_11/Chapter_11_IR_Playbook_Template.md` | Available |
| Tabletop Scenario Library | Facilitator guides for six tabletop exercise scenarios | `Chapter_11/Chapter_11_Tabletop_Scenario_Library.md` | Available |
| Safe vs. Unsafe Actions Reference | Printable matrix of common response actions with OT safety assessments | `Chapter_11/Chapter_11_Safe_Unsafe_Actions_Reference.md` | Available |
| Communication Templates | Templates for internal operations alerts, regulatory notifications, and escalation | `Chapter_11/Chapter_11_Communication_Templates.md` | Available |
| CSIRT Charter Template | Template defining CSIRT composition, roles, and activation criteria | `Chapter_11/Chapter_11_CSIRT_Charter_Template.md` | Available |
| CSIRT Roster Template | Template for tracking on-call CSIRT membership | `Chapter_11/Chapter_11_CSIRT_Roster_Template.md` | Available |
| OT Incident Severity Matrix | Four-level severity classification accounting for cyber and physical impact | `Chapter_11/Chapter_11_OT_Incident_Severity_Matrix.md` | Available |
| EDR Response Decision Trees | Visual decision trees for common EDR response scenarios in OT | `Chapter_11/Chapter_11_EDR_Response_Decision_Trees.md` | Available |
| OT Alert Triage SOP | Standard operating procedure for OT alert triage | `Chapter_11/Chapter_11_OT_Alert_Triage_SOP.md` | Available |
| OT Escalation Template | Template for cross-functional escalation in OT incidents | `Chapter_11/Chapter_11_OT_Escalation_Template.md` | Available |
| Shift Handover Checklist | Checklist for SOC analyst shift handover with OT context preservation | `Chapter_11/Chapter_11_Shift_Handover_Checklist.md` | Available |
| Fail-Safe Position Template | Template for documenting fail-safe positions for crown jewel assets | `Chapter_11/Chapter_11_5_Failsafe_Position_Template.csv` | Available (filename rename pending, see audit) |
| SOAR Containment Boundary | Reference for the safe boundary of SOAR-led containment actions in OT | `Chapter_11/Chapter_11_SOAR_Containment_Boundary.md` | Available |
| UC-IR-001, OT Incident Enrichment | Sentinel automation rule logic for enriching OT incidents with asset and crown jewel context | `Chapter_11/UC-IR-001_OT_Incident_Enrichment.kql` | Available (draft body still references this as `Chapter_11_OT_Incident_Enrichment_Automation.kql`; replacement queued in `DRAFT_FIND_REPLACE.md`) |

## Chapter 12: Digital Forensics and Lessons Learned

Forensic investigation frameworks and after-action review processes.

| Asset | Description | Filepath | Status |
|---|---|---|---|
| EDR Forensic Investigation Checklist | Six-step EDR forensic workflow from triage to lateral movement tracking | `Chapter_12/Chapter_12_EDR_Forensic_Investigation_Checklist.md` | Available |
| EDR and SIEM Correlation Queries | KQL queries correlating EDR telemetry with Windows Event Logs, Sysmon, and Zeek | `Chapter_12/Chapter_12_EDR_SIEM_Correlation_Queries.kql` | Available |
| Forensic Report Template | Unified investigative report template combining endpoint, network, and OT engineering forensics | `Chapter_12/Chapter_12_Forensic_Report_Template.md` | Available |
| After-Action Review Template | Nine-section AAR template covering executive summary, timeline, and root cause analysis | `Chapter_12/Chapter_12_AAR_Template.md` | Available |
| IOC Extraction Checklist | Checklist for extracting indicators of compromise from forensic evidence | `Chapter_12/Chapter_12_IOC_Extraction_Checklist.md` | Available |
| OT Evidence Request Template | Template for requesting OT-side evidence from engineering teams | `Chapter_12/Chapter_12_OT_Evidence_Request_Template.md` | Available |
| ISAC Sharing Template | Template for sharing IOCs and observations with sector ISACs | `Chapter_12/Chapter_12_ISAC_Sharing_Template.md` | Planned |

## Chapter 13: Tooling Selection and Integration

Tool evaluation frameworks and integration guidance for OT security platforms.

| Asset | Description | Filepath | Status |
|---|---|---|---|
| Tool Evaluation Scorecard | Scorecard for evaluating OT security tooling against defined criteria | `Chapter_13/Chapter_13_Tool_Evaluation_Scorecard.md` | Available |
| Tool Capability Gap Assessment | Worksheet for assessing capability gaps in the current tool stack | `Chapter_13/Chapter_13_Tool_Capability_Gap_Assessment.md` | Available |
| Pilot Programme Plan | Template for planning a tool pilot, including success criteria and exit conditions | `Chapter_13/Chapter_13_Pilot_Programme_Plan.md` | Available |
| Integration Health Check | Checklist for verifying integration health between SIEM, NDR, EDR, and watchlists | `Chapter_13/Chapter_13_Integration_Health_Check.md` | Available |
| Tool Inventory Tracker | CSV tracker for the current tool stack | `Chapter_13/Chapter_13_Tool_Inventory_Tracker.csv` | Available |

## Chapter 14: Cross-Functional Collaboration

Templates and frameworks for building effective IT/OT collaboration structures.

| Asset | Description | Filepath | Status |
|---|---|---|---|
| CSIRT Charter Template (Extended) | Comprehensive charter including day-to-day collaboration provisions | `Chapter_14/Chapter_14_CSIRT_Charter_Template.md` | Available |
| Meeting Agenda Templates | Agendas for weekly IT/OT sync, monthly tabletop, and quarterly programme review | `Chapter_14/Chapter_14_Meeting_Agenda_Templates.md` | Available |
| IT Security OT Training Plan | Training programme for SOC analysts covering ICS fundamentals and plant orientation | `Chapter_14/Chapter_14_IT_Security_OT_Training_Plan.md` | Available |
| OT Engineering Security Training Plan | Training programme for OT engineers covering detection capabilities and incident response | `Chapter_14/Chapter_14_OT_Engineering_Security_Training_Plan.md` | Available |
| Cross-Functional Tabletop Guide | Guide for joint IT/OT tabletop exercises using Chapter 11 scenarios | `Chapter_14/Chapter_14_Cross_Functional_Tabletop_Guide.md` | Available |
| Conflict Resolution and Escalation | Framework for resolving cross-functional conflicts in incident response | `Chapter_14/Chapter_14_Conflict_Resolution_Escalation.md` | Available |
| Metrics Definitions List | Comprehensive list of operational, security, and collaboration metrics | `Chapter_14/Chapter_14_Metrics_Definitions_List.md` | Available |
| Joint KPIs Dashboard Template | Dashboard template for tracking programme health across IT Security, OT Engineering, and Operations | `Chapter_14/Chapter_14_Joint_KPIs_Dashboard_Template.md` | Rename pending (current file has `.md.md` double extension) |
| Joint KPIs and Metrics | Combined KPIs and metrics view referenced by the draft | `Chapter_14/Chapter_14_Joint_KPIs_Metrics.md` | Planned (or resolve via rename of the dashboard file, see audit) |
| RACI Hybrid Model | RACI for a hybrid IT/OT SOC | `Chapter_14/Chapter_14_RACI_Hybrid_Model.md` | Available |
| SOC Analyst OT Quick Reference | Pocket reference for SOC analysts handling OT alerts | `Chapter_14/Chapter_14_SOC_Analyst_OT_Quick_Reference.md` | Available |
| Engineering Liaison Charter | Role definition for the interface position between SOC and OT Engineering | `Chapter_14/Chapter_14_Engineering_Liaison_Charter.md` | Available |

## Chapter 15: The Continuous Improvement Cycle

Maturity models, continuous improvement frameworks, and programme metrics.

| Asset | Description | Filepath | Status |
|---|---|---|---|
| Maturity Self-Assessment | Programme-level maturity self-assessment across SOC for OT capabilities | `Chapter_15/Chapter_15_Maturity_Self_Assessment.md` | Available |
| Improvement Roadmap Template | Template for building a multi-quarter improvement roadmap | `Chapter_15/Chapter_15_Improvement_Roadmap_Template.md` | Available |
| Purple Team Exercise Guide | Guide for conducting purple team exercises in OT contexts | `Chapter_15/Chapter_15_Purple_Team_Exercise_Guide.md` | Available |
| Metrics Definitions | Programme metrics, KPIs, and definitions for continuous improvement | `Chapter_15/Chapter_15_Metrics_Definitions.md` | Available |
| Quarterly Review Template | Template for the quarterly review of detection coverage, hunts, and incidents | `Chapter_15/Chapter_15_Quarterly_Review_Template.md` | Available |

## Chapter 16: Leveraging AI and Machine Learning

Machine learning scripts and frameworks for OT security analytics. The files on disk use `Chapter_16_*`. The draft body still references seven of them with the legacy `Chapter_08_` prefix; the replacements are queued in `DRAFT_FIND_REPLACE.md` for Word's Find and Replace.

| Asset | Description | Filepath | Status |
|---|---|---|---|
| ML Readiness Assessment Checklist | Assessment for evaluating prerequisites for ML deployment in OT security | `Chapter_16/Chapter_16_ML_Readiness_Assessment_Checklist.md` | Available |
| Asset Behaviour Profiling | Python implementation using NetworkX and Isolation Forest for OT communication pattern analysis | `Chapter_16/Chapter_16_Asset_Behaviour_Profiling.py` | Available |
| Process Anomaly Detection | Python implementation using ARIMA and Prophet for time-series anomaly detection on process historian data | `Chapter_16/Chapter_16_Process_Anomaly_Detection.py` | Available |
| Protocol Anomaly Detection | Python LSTM implementation for sequence-based anomaly detection on ICS protocol command logs | `Chapter_16/Chapter_16_Protocol_Anomaly_Detection.py` | Available |
| Model Evaluation Metrics | Template for tracking ML model performance with OT-specific metrics | `Chapter_16/Chapter_16_Model_Evaluation_Metrics.md` | Available |
| ML False Positive Impact Assessment | Scoring framework for operational consequences of ML false positives | `Chapter_16/Chapter_16_ML_False_Positive_Impact_Assessment.md` | Available |
| ML Implementation Roadmap | Five-phase ML maturity roadmap with milestones and decision gates | `Chapter_16/Chapter_16_ML_Implementation_Roadmap.md` | Available |
| ML Rule Correlation | KQL pattern for correlating ML model output with existing detection rules | `Chapter_16/Chapter_16_ML_Rule_Correlation.kql` | Available |
| ML Anomalies Schema | KQL schema for the `ML_Anomalies` custom table feeding Sentinel from external ML pipelines | `Chapter_16/Chapter_16_ML_Anomalies_Schema.kql` | Available |

## Watchlists

Microsoft Sentinel watchlists for OT context enrichment, used by detection rules across multiple chapters.

| Asset | Description | Filepath | Status |
|---|---|---|---|
| OT_AssetRegister Schema | Asset inventory watchlist schema (introduced in Chapter 6) | `watchlists/OT_AssetRegister_Schema.csv` | Available |
| OT_CrownJewels Schema | Crown jewel subset watchlist for dynamic severity assignment | `watchlists/OT_CrownJewels_Schema.csv` | Available |
| OT_MaintenanceWindows Schema | Maintenance window scheduling watchlist with sample data | `watchlists/OT_MaintenanceWindows_Schema.csv` | Available |

## Shared Templates

Cross-chapter templates used by multiple chapters.

| Asset | Description | Filepath | Status |
|---|---|---|---|
| ICS Detection Use Case Template | Standard template for documenting all ICS detection rules | `templates/ICS_Detection_Use_Case_Template.md` | Rename pending (currently at `Book/` root) |

## Detection and Hunt Library at a Glance

### KQL Analytics Rules (Microsoft Sentinel, ASIM-aligned)
- UC-ICS-001, Unauthorised ICS Protocol Communication to Controller
- UC-ICS-002, ICS Write Command Outside Maintenance Window
- UC-ICS-003, IT/OT Boundary Traversal
- UC-ICS-004, Credential Brute Force Against OT Systems
- UC-ICS-008, Modbus Function Code Scan (Zeek-based via Sentinel)
- UC-ICS-009, Cross-Domain Lateral Movement Correlation
- UC-ICS-010, Vendor Session Anomaly (Chapter 5)
- UC-ICS-010, Anomalous Authentication on OT Systems (Chapter 7, number collision flagged)
- UC-ICS-011, IDMZ Jump Server Anomaly (Chapter 5)
- UC-ICS-011, SIS Communication Anomaly (Chapter 8, number collision flagged)
- UC-ICS-013, New OT Device Detection
- CTI-ICS-001, Credential Extraction to OT Pivot
- UC-IR-001, OT Incident Enrichment
- ATTCK_ICS_Coverage_Assessment, Detection Coverage Gap Analysis

### Suricata Signature Rules
- UC-ICS-005, Modbus Diagnostic Function Abuse
- UC-ICS-006, DNP3 Unauthorised Operations
- UC-ICS-007, CIP Programme Operations
- UC-ICS-012, IDMZ Boundary Monitoring
- Hunt-ICS-003, EtherNet/IP Discovery

### Zeek Scripts
- Chapter_05, IDMZ Connection Pair Baseline
- Chapter_09, Zeek Hunting (general)
- Hunt-ICS-001, Firmware Operations

### Hunt Queries
- Hunt-ICS-001, Firmware Operations (KQL and Zeek)
- Hunt-ICS-002, Covert Channels in Modbus
- Hunt-ICS-003, Network Reconnaissance (KQL and Suricata)
- Hunt-CTI-001, OT Documentation Access

## Usage Guidelines

### Prerequisites
- Microsoft Sentinel workspace configured with ASIM normalisation
- Zeek network sensors with CISA ICSNPP parsers deployed
- Suricata IDS for signature-based detection
- Python 3.10+ for ML and hunting scripts
- NetworkX, scikit-learn, Prophet, and statsmodels for analytics

### Deployment Sequence
1. Build the asset inventory (Chapter 6) and populate the `OT_AssetRegister` watchlist
2. Identify crown jewels (Chapter 5) and populate the `OT_CrownJewels` watchlist
3. Populate `OT_MaintenanceWindows` (Chapter 7) with a working change management feed
4. Deploy the core detection library (UC-ICS-001 through UC-ICS-009) aligned to your available telemetry
5. Deploy EDR on Purdue Levels 2 to 3 workstations and HMIs following Chapter 7 guidance
6. Begin hunting (Chapter 9) using gaps identified by `ATTCK_ICS_Coverage_Assessment`
7. Introduce ML (Chapter 16) only once baseline data quality is established

### Customisation Required
Every asset is a template. Customise:
- IP address ranges for your OT networks
- Purdue level assignments for your architecture
- Protocol-specific parameters for your ICS devices
- Threshold values tuned to your operational baselines
- Watchlist populations with your actual assets

## About This Repository

This repository accompanies **Security Operations Centre for Operational Technology: A Practitioner's Guide to Defending Industrial Control Systems**, providing ready-to-deploy assets that translate the book's guidance into operational capability.

Every asset has been designed with OT safety as the primary consideration. The book's core principle applies: *security supports operational safety; it never compromises it.*

**Version:** 1.1
**Last Updated:** 2026-05-16
**Chapters Covered:** 1 to 16
**Total Assets Catalogued:** see chapter tables above. Planned and Rename pending items are tracked in `ASSET_AUDIT_REPORT.md`.
