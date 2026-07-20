# ML Readiness Assessment Checklist
# ================================================================
# Description: Structured assessment framework for evaluating whether
#   the prerequisites for ML deployment in OT security are met.
#   Designed to be completed collaboratively by SOC and OT engineering.
#
# Usage: Complete before Phase 1 of the ML Maturity Roadmap.
#   Score each criterion as Met / Partial / Not Met.
#   All "Critical" items must be Met before proceeding to Phase 2.
#
# Reference: Chapter 8 — Leveraging AI and Machine Learning
# ================================================================

## ASSESSMENT INFORMATION
- **Assessed By**: [SOC Lead + OT Engineering Lead]
- **Date**: [Assessment date]
- **Environment**: [Site/facility name]
- **Next Review**: [Quarterly recommended]
- **Overall Readiness**: [Ready | Conditional | Not Ready]

---

## SECTION 1: DATA QUALITY AND AVAILABILITY

### 1.1 Telemetry Coverage (Critical)
- [ ] **Met** | [ ] **Partial** | [ ] **Not Met**
- All Tier 1 crown jewel assets have active telemetry flowing to Sentinel
- Telemetry gap assessment (Chapter 7) has been completed and reviewed
- **Evidence**: Telemetry Gap Assessment query results, dated within 30 days

### 1.2 Communication Baselines Established (Critical)
- [ ] **Met** | [ ] **Partial** | [ ] **Not Met**
- Communication baselines (Chapter 7 KQL query) have been generated for crown jewel assets
- Baselines cover a minimum of 30 days of operational data
- Baselines include shift variations, weekends, and at least one maintenance window
- **Evidence**: Baseline query results, reviewed by OT engineering

### 1.3 ASIM Normalisation Validated (Critical)
- [ ] **Met** | [ ] **Partial** | [ ] **Not Met**
- Custom ASIM parsers for Zeek and Suricata data are deployed and tested
- NetworkSession, Authentication, and ProcessCreate schemas are populated
- Parsed data has been spot-checked against raw logs for accuracy
- **Evidence**: Parser validation test results

### 1.4 Time Synchronisation
- [ ] **Met** | [ ] **Partial** | [ ] **Not Met**
- All OT systems forwarding logs use NTP or equivalent time synchronisation
- Timestamp drift between IT and OT log sources is < 2 seconds
- **Evidence**: Timestamp comparison across IT/OT log sources

### 1.5 Data Completeness
- [ ] **Met** | [ ] **Partial** | [ ] **Not Met**
- Crown jewel asset telemetry shows consistent daily log volume (< 10% variance)
- No unexplained gaps exceeding 1 hour in the past 30 days
- Log ingestion latency is documented and acceptable (< 5 minutes for crown jewels)
- **Evidence**: Sentinel ingestion statistics for OT data tables

### 1.6 Process Historian Access (Required for Process Anomaly Detection)
- [ ] **Met** | [ ] **Partial** | [ ] **Not Met** | [ ] **Not Applicable**
- Process historian data (temperature, pressure, flow, level) is exportable
- Export format is documented (CSV, SQL query, API)
- Historical data covers minimum 90 days for seasonal pattern capture
- **Evidence**: Sample historian export with data dictionary

---

## SECTION 2: OPERATIONAL CONTEXT

### 2.1 OT Asset Register Complete (Critical)
- [ ] **Met** | [ ] **Partial** | [ ] **Not Met**
- OT_AssetRegister watchlist is populated in Sentinel
- All crown jewel assets have complete records (IP, hostname, Purdue level, device type, crown jewel tier, engineering owner)
- Asset register has been validated by OT engineering within the last 90 days
- **Evidence**: OT_AssetRegister watchlist export

### 2.2 Maintenance Windows Documented (Critical)
- [ ] **Met** | [ ] **Partial** | [ ] **Not Met**
- OT_MaintenanceWindows watchlist is maintained in Sentinel
- Maintenance windows are documented before they occur (not retroactively)
- Engineering team has a process for notifying the SOC of unplanned maintenance
- **Evidence**: OT_MaintenanceWindows watchlist entries, process documentation

### 2.3 Known Operational Variations Documented
- [ ] **Met** | [ ] **Partial** | [ ] **Not Met**
- Seasonal process variations are documented (e.g., summer vs winter operating parameters)
- Batch changeover patterns are documented (for batch processing environments)
- Shift change patterns are documented (communication patterns that change at shift boundaries)
- **Evidence**: Operational variation documentation, reviewed by OT engineering

### 2.4 Known False Positive Sources Identified
- [ ] **Met** | [ ] **Partial** | [ ] **Not Met**
- Current rule-based detection false positive sources are documented
- Legitimate activities that generate anomalous-looking traffic are catalogued
- Vendor remote access patterns are baselined (Chapter 5)
- **Evidence**: False positive catalogue from existing SOC operations

---

## SECTION 3: TECHNICAL INFRASTRUCTURE

### 3.1 Compute Resources for Model Training
- [ ] **Met** | [ ] **Partial** | [ ] **Not Met**
- A system is available for ML model training (minimum: 16GB RAM, 4 CPU cores)
- The training system has network access to export data from Sentinel
- Python 3.9+ is available with ability to install required libraries
- **Evidence**: System specification document

### 3.2 Sentinel Custom Table Ingestion
- [ ] **Met** | [ ] **Partial** | [ ] **Not Met**
- Log Analytics Data Collector API or Logs Ingestion API access is configured
- A custom table (OT_ML_Anomalies_CL) can be created in the Sentinel workspace
- API authentication is configured (workspace ID, shared key or managed identity)
- **Evidence**: Successful test ingestion to custom table

### 3.3 Scheduled Execution Capability
- [ ] **Met** | [ ] **Partial** | [ ] **Not Met**
- A mechanism exists for scheduling Python scripts (cron, Azure Automation, Azure Functions)
- The scheduled execution environment has access to Sentinel data and the ML models
- Alerting is configured for script execution failures
- **Evidence**: Test scheduled execution with logging

---

## SECTION 4: ORGANISATIONAL READINESS

### 4.1 Analyst Capacity (Critical)
- [ ] **Met** | [ ] **Partial** | [ ] **Not Met**
- SOC analysts have capacity to investigate ML-generated anomalies (estimated 2-5 per day initially)
- Analysts understand that ML alerts require investigation, not automatic action
- Triage procedures for ML alerts are documented (or will be before Phase 2)
- **Evidence**: Analyst workload assessment, triage procedure draft

### 4.2 OT Engineering Engagement (Critical)
- [ ] **Met** | [ ] **Partial** | [ ] **Not Met**
- OT engineering team has agreed to participate in ML baseline validation
- A named OT engineering contact is available for ML false positive review
- OT engineering understands that ML will NOT take autonomous action
- **Evidence**: Documented agreement, named contact

### 4.3 Management Sponsorship
- [ ] **Met** | [ ] **Partial** | [ ] **Not Met**
- Management understands the phased approach (no ML until Phase 2)
- Expectations are set: ML augments detection, does not replace analysts
- Budget/time is allocated for the full Phase 1-4 roadmap (minimum 18 months)
- **Evidence**: Approved project charter or programme plan

### 4.4 Model Governance
- [ ] **Met** | [ ] **Partial** | [ ] **Not Met**
- A process exists for documenting model versions, training data, and performance
- Retraining triggers are defined (quarterly minimum, plus operational changes)
- Model retirement criteria are defined (when to stop using a model)
- **Evidence**: Model governance procedure document

---

## ASSESSMENT SUMMARY

| Section | Items Met | Items Partial | Items Not Met | Critical Gaps |
|---------|-----------|---------------|---------------|---------------|
| 1. Data Quality | /6 | /6 | /6 | |
| 2. Operational Context | /4 | /4 | /4 | |
| 3. Technical Infrastructure | /3 | /3 | /3 | |
| 4. Organisational Readiness | /4 | /4 | /4 | |
| **TOTAL** | **/17** | **/17** | **/17** | |

### Readiness Determination

- **Ready**: All Critical items Met, no more than 3 Non-Critical items Partial/Not Met
- **Conditional**: All Critical items Met or Partial, remediation plan documented
- **Not Ready**: Any Critical item Not Met — address gaps before proceeding

### Remediation Plan (if Conditional or Not Ready)

| Gap | Remediation Action | Owner | Target Date |
|-----|-------------------|-------|-------------|
| | | | |
| | | | |
| | | | |

### Sign-Off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| SOC Lead | | | |
| OT Engineering Lead | | | |
| Security Manager | | | |
