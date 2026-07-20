# EDR Configuration Checklist for OT Environments

## Purpose

This checklist ensures that EDR deployments on OT systems are configured safely, with appropriate exclusions, performance safeguards, and engineering coordination. Complete each section before, during, and after deployment.

---

## Section 1: Pre-Deployment Planning

### Engineering Coordination
- [ ] OT engineering team informed of planned deployment
- [ ] Deployment window agreed with OT engineering (during maintenance window if Level 2)
- [ ] Engineering contact identified and available during deployment
- [ ] Rollback procedure documented and agreed
- [ ] Change management ticket raised and approved

### System Assessment
- [ ] Target system identified in OT_AssetRegister with correct Purdue level and device type
- [ ] Target system's crown jewel tier confirmed
- [ ] Target system's operating system version confirmed and documented
- [ ] Baseline performance metrics recorded (CPU%, memory%, disk I/O, network)
- [ ] Target system's role in the physical process documented
- [ ] Redundancy status confirmed (is there a backup HMI/SCADA server if this one fails?)

### Vendor Compatibility (Level 2 Systems Only)
- [ ] HMI/SCADA vendor contacted regarding EDR compatibility
- [ ] Vendor compatibility statement received (document reference: _____________)
- [ ] Known vendor-recommended exclusions documented
- [ ] EDR tested on non-production system running the same vendor application
- [ ] Test confirmed: no application conflicts during normal operation
- [ ] Test confirmed: no application conflicts during engineering operations (programme upload/download, configuration changes)

---

## Section 2: EDR Policy Configuration

### Mode Selection
- [ ] Initial deployment mode set to **DETECT-ONLY** (no blocking, no quarantine)
- [ ] Automated remediation actions **DISABLED** for OT asset group
- [ ] Network isolation capability available but **NOT** set to auto-trigger

### Exclusion Configuration

Configure the following exclusions BEFORE deploying the agent:

#### Engineering Software Exclusions (Configure per vendor)
- [ ] Rockwell Automation: Studio 5000, FactoryTalk, RSLinx
  - Paths: `C:\Program Files (x86)\Rockwell Software\*`
  - Processes: `Studio5000.exe`, `FactoryTalkView.exe`, `RSLinx.exe`
- [ ] Siemens: TIA Portal, WinCC, STEP 7
  - Paths: `C:\Program Files\Siemens\*`
  - Processes: `Siemens.Automation.Portal.exe`, `WinCCExplorer.exe`
- [ ] Schneider Electric: ControlExpert, ClearSCADA
  - Paths: `C:\Program Files\Schneider Electric\*`
  - Processes: `ControlExpert.exe`, `ClearSCADA.exe`
- [ ] ABB: Ability Symphony Plus, 800xA
  - Paths: `C:\ABB\*`, `C:\Program Files\ABB\*`
- [ ] Other vendor applications: ________________________________
  - Paths: ________________________________
  - Processes: ________________________________

#### OT Application Exclusions
- [ ] Historian software (OSIsoft PI, Wonderware, GE Proficy)
  - Paths: ________________________________
  - Processes: ________________________________
- [ ] OPC servers/clients
  - Paths: ________________________________
  - Processes: ________________________________
- [ ] Data archival and reporting applications
  - Paths: ________________________________

#### System Exclusions
- [ ] Engineering project file directories (PLC programmes, SCADA configurations)
  - Paths: ________________________________
- [ ] Real-time data exchange directories (if applicable)
  - Paths: ________________________________

### Scan Schedule Configuration
- [ ] Real-time scanning: **ENABLED** (with exclusions above)
- [ ] Full disk scans: **DISABLED** or scheduled during maintenance windows only
- [ ] CPU throttling: **ENABLED** — set maximum CPU usage during scans to ≤ 20%
- [ ] Scan windows: If scheduled scans are enabled, schedule during lowest-operational-load period
  - Scheduled time: ________________________________

### Alerting and Notification
- [ ] Alert routing configured to include OT SOC team
- [ ] High-severity alerts on OT systems trigger immediate notification
- [ ] Alert enrichment includes OT_AssetRegister context (Purdue level, crown jewel tier)

---

## Section 3: Deployment Execution

### Deployment Steps
- [ ] Pre-deployment performance baseline captured (timestamp: _____________)
- [ ] Agent installer staged on target system (or pushed via management console)
- [ ] Agent installed successfully
- [ ] Agent registered in management console and assigned to OT policy group
- [ ] Exclusions verified active on the deployed agent
- [ ] Mode confirmed as DETECT-ONLY in management console

### Immediate Post-Deployment Validation (First 24 Hours)
- [ ] System rebooted successfully (if required by installer)
- [ ] OT application started and running normally
- [ ] HMI displays responsive (for HMI deployments — operator confirmation)
- [ ] Engineering software opens and functions correctly (for workstation deployments)
- [ ] CPU usage within acceptable range (< 5% increase over baseline)
- [ ] Memory usage within acceptable range (< 200MB agent footprint)
- [ ] Disk I/O within acceptable range (no noticeable degradation)
- [ ] Network connectivity to SIEM/management console confirmed
- [ ] Telemetry data appearing in Sentinel/SIEM
- [ ] No EDR-related errors in Windows Event Log
- [ ] OT engineering team confirmed no operational impact

---

## Section 4: Tuning Period (4–8 Weeks)

### Weekly Review
- [ ] Week 1: Review all alerts generated — document false positives
- [ ] Week 2: Add exclusions for identified legitimate activity causing false positives
- [ ] Week 3: Review updated alert volume — verify false positive reduction
- [ ] Week 4: Assess overall alert quality and performance metrics

### False Positive Documentation

| Date | Alert Type | Process/File | Legitimate Activity | Exclusion Added? |
|------|-----------|-------------|---------------------|-----------------|
| | | | | |
| | | | | |
| | | | | |

### Performance Monitoring
- [ ] Weekly performance comparison against pre-deployment baseline
- [ ] No performance degradation trends observed
- [ ] No operator/engineer complaints received

---

## Section 5: Blocking Mode Evaluation (After Tuning Period)

### Prerequisites for Enabling Blocking
- [ ] Minimum 4 weeks in detect-only mode (8+ weeks for HMIs)
- [ ] False positive rate below acceptable threshold (< 2 per week)
- [ ] All known false positive sources excluded
- [ ] Engineering team approval obtained (document reference: _____________)
- [ ] Change management ticket raised for mode change
- [ ] Rollback procedure documented (revert to detect-only within < 5 minutes)
- [ ] First blocking enablement scheduled during maintenance window

### Blocking Mode Configuration
- [ ] Blocking enabled for malware detection
- [ ] Blocking enabled for known exploit prevention
- [ ] Blocking **DISABLED** for behavioural detection (too high FP risk on OT)
- [ ] Network isolation remains manual-only (no auto-isolation)
- [ ] Process termination requires analyst confirmation (no auto-kill on OT assets)

### Post-Blocking Validation
- [ ] OT application functioning normally with blocking enabled
- [ ] No legitimate processes blocked in first 48 hours
- [ ] Engineering operations (programme upload, configuration) tested and working
- [ ] Operator confirmation that HMI responsiveness is unaffected (HMI deployments)

---

## Section 6: Ongoing Maintenance

### Quarterly Review
- [ ] EDR agent version current (update during maintenance windows)
- [ ] Exclusion list reviewed — remove exclusions no longer needed, add new ones
- [ ] Alert volume and quality reviewed
- [ ] Performance metrics reviewed against baseline
- [ ] OT_AssetRegister updated with current EDR deployment status
- [ ] Telemetry Source Inventory updated

### Annual Review
- [ ] EDR vendor compatibility re-confirmed with OT application vendor
- [ ] Deployment mode reviewed (is blocking now appropriate where detect-only is deployed?)
- [ ] Coverage gaps reviewed (are there new systems that should have EDR?)
- [ ] Integration with SIEM detection rules reviewed (are all EDR data sources consumed by analytics rules?)
