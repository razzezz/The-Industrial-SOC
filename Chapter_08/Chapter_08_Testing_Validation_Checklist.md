# Detection Rule Testing and Validation Checklist
# ================================================================
# Description: Three-phase testing checklist for OT detection rules.
#   Covers unit testing, integration testing, and operational validation.
#   Must be completed before any rule is deployed to production.
#
# Usage: Complete one checklist per detection rule. File alongside 
#   the ICS Detection Use Case Template in the detection library.
# ================================================================

## Rule Identification
- **Use Case ID**: UC-ICS-[number]
- **Title**: [Rule title]
- **Detection Layer**: [Sentinel KQL | Suricata Signature | Zeek Behavioural | Multi-layer]
- **Developer**: [Name]
- **Test Start Date**: [Date]
- **Test End Date**: [Date]

---

## Phase 1: Unit Testing

**Objective:** Validate that the rule fires correctly on synthetic test data and does not fire on known-good data.

### Pre-Test Setup
- [ ] Test data created that matches the rule's trigger conditions
- [ ] Test data created that represents known-good (non-alerting) activity
- [ ] Development/test workspace available (not production)
- [ ] Required watchlists populated in test workspace (OT_AssetRegister, OT_MaintenanceWindows)

### KQL Analytics Rules
- [ ] Rule executes without syntax errors
- [ ] Rule fires on synthetic test data matching trigger conditions
- [ ] Rule does NOT fire on known-good test data
- [ ] ASIM schema references resolve correctly (_Im_NetworkSession, _Im_Authentication, etc.)
- [ ] OT_AssetRegister watchlist join returns expected enrichment fields
- [ ] OT_MaintenanceWindows watchlist join correctly excludes maintenance periods
- [ ] Dynamic severity assignment produces correct values per CrownJewelTier
- [ ] Output fields are complete and correctly named
- [ ] Lookback period and schedule frequency are appropriate for the detection
- [ ] Query execution time is acceptable (<30 seconds on test data)

### Suricata Signature Rules
- [ ] Rule loads without errors in Suricata configuration test (suricata -T)
- [ ] Rule fires on PCAP replay containing target protocol operations
- [ ] Rule does NOT fire on PCAP containing only legitimate protocol traffic
- [ ] SID is unique and within the allocated range
- [ ] Metadata tags are correct (mitre_technique, purdue_level, severity)
- [ ] Protocol keywords are appropriate for the target protocol
- [ ] Flow direction is correctly specified (to_server, established)

### Zeek Behavioural Scripts
- [ ] Script loads without errors in Zeek (-a flag)
- [ ] Script generates expected Notice events on test PCAP
- [ ] Script does NOT generate false notices on legitimate traffic PCAP
- [ ] State tracking operates correctly (if stateful detection)
- [ ] Module configuration variables are documented and tunable
- [ ] Notice metadata includes ATT&CK technique and severity

### Unit Test Results
- **Pass / Fail**: [Result]
- **Issues Found**: [Description of any issues and resolution]
- **Tester**: [Name]
- **Date Completed**: [Date]

---

## Phase 2: Integration Testing

**Objective:** Validate that the rule operates correctly against live telemetry over an extended observation period.

### Pre-Test Setup
- [ ] Rule deployed in non-production mode (logging results, not generating incidents)
- [ ] Alert output routed to a monitoring location accessible to the tester
- [ ] Observation period defined (minimum 2 weeks, recommended 4 weeks)
- [ ] Baseline alert rate expectations documented

### Observation Period
- **Start Date**: [Date]
- **End Date**: [Date]
- **Duration**: [Weeks]

### Alert Classification (complete during observation period)

| Date | Alert Details | Source | Destination | Classification | Notes |
|------|---------------|--------|-------------|----------------|-------|
| | | | | TP / FP / Indeterminate | |
| | | | | TP / FP / Indeterminate | |
| | | | | TP / FP / Indeterminate | |

*(Add rows as needed. Maintain this log for all alerts during the integration period.)*

### Integration Test Metrics
- **Total Alerts**: [Count]
- **True Positives**: [Count]
- **False Positives**: [Count]
- **Indeterminate**: [Count]
- **Precision (TP / (TP + FP))**: [Percentage]
- **Average Alerts per Day**: [Count]

### False Positive Analysis
For each false positive identified, document:

| FP # | Date | Root Cause | Mitigation | Applied? |
|------|------|------------|------------|----------|
| 1 | | | | Yes / No / Deferred |
| 2 | | | | Yes / No / Deferred |
| 3 | | | | Yes / No / Deferred |

### Integration Test Assessment
- [ ] Precision meets minimum threshold (>80% for initial deployment)
- [ ] Alert volume is manageable for the SOC team
- [ ] All identified false positive sources have documented mitigations
- [ ] No unexpected data source issues encountered
- [ ] Watchlist enrichment working correctly with live data
- [ ] Query execution time is acceptable on production data volume

### Integration Test Results
- **Pass / Fail**: [Result]
- **Recommendation**: [Deploy / Tune and Retest / Redesign]
- **Tester**: [Name]
- **Date Completed**: [Date]

---

## Phase 3: Operational Validation

**Objective:** Validate the rule's operational impact with OT engineering and obtain deployment approval.

### Engineering Liaison Review
- [ ] Integration test results shared with OT engineering liaison
- [ ] Engineering liaison has reviewed all alerts (or a representative sample)
- [ ] False positives reviewed: are these expected engineering activities?
- [ ] Engineering liaison has confirmed triage guidance is accurate
- [ ] Engineering liaison has confirmed escalation path is appropriate
- [ ] Any additional false positive sources identified by engineering are documented

### Engineering Feedback

**Liaison Name**: [Name]
**Review Date**: [Date]

**Feedback on false positives:**
[Document engineering team's assessment of false positive alerts]

**Feedback on triage guidance:**
[Document any corrections or additions to the analyst triage steps]

**Additional operational context:**
[Document any operational patterns, schedules, or activities that affect the rule]

### Operational Validation Assessment
- [ ] Engineering liaison approves the rule for production deployment
- [ ] Use Case Template updated with engineering feedback
- [ ] Known FP Sources section updated
- [ ] Tuning Notes section updated
- [ ] Triage Guidance section validated or corrected

### Operational Validation Results
- **Approved for Production / Not Approved**: [Result]
- **Conditions (if any)**: [e.g., "Deploy with additional exclusion for quarterly SIS testing"]
- **Engineering Liaison Sign-off**: [Name and Date]

---

## Production Deployment

### Deployment Checklist
- [ ] All three test phases completed and passed
- [ ] Use Case Template is fully updated with test findings
- [ ] Analytics rule configured in production workspace with correct schedule
- [ ] Incident creation settings configured (severity, grouping)
- [ ] SOC team briefed on the new detection (what it detects, how to triage)
- [ ] Detection Tuning Log created for ongoing false positive tracking
- [ ] Coverage assessment updated (ATTCK_ICS_Coverage_Assessment.kql re-run)
- [ ] Rule documented in the detection library index

### Deployment Record
- **Deployed to Production**: [Date]
- **Deployed By**: [Name]
- **First Review Scheduled**: [Date, typically 2 weeks post-deployment]
- **Quarterly Review Scheduled**: [Date]
