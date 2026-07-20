# Vendor Access Monitoring Baseline Template

**Book Reference:** Chapter 5 — Defensible Architecture and Segmentation  
**Purpose:** Document each vendor's normal access patterns to enable behavioural anomaly detection.  
**Usage:** Complete one section per vendor. Update after each maintenance engagement. Share with SOC for detection tuning.

---

## Vendor Profile

| Field | Value |
|-------|-------|
| **Vendor Name** | |
| **Contract Reference** | |
| **Primary Contact** | |
| **Emergency Contact** | |
| **Systems Supported** | |
| **Contract Expiry Date** | |
| **Last Access Review Date** | |

---

## Access Architecture

| Field | Value |
|-------|-------|
| **Access Method** | VPN to Jump Server / Direct VPN / Site Visit / Cloud-Based / Other: ______ |
| **Jump Server Used** | Hostname: __________ IP: __________ |
| **VPN Gateway** | Hostname: __________ IP: __________ |
| **MFA Enabled** | Yes / No / Partial (detail: __________) |
| **Account Type** | Named Individual / Shared Vendor Account / Service Account |
| **Account Name(s)** | |
| **Source IP Range(s)** | Known vendor IP ranges for allowlisting: |
| **Session Recording** | Enabled / Not Enabled |

---

## Normal Access Patterns

### Temporal Baseline

| Parameter | Normal Pattern | Notes |
|-----------|---------------|-------|
| **Typical Days** | e.g., Mon–Fri / Scheduled maintenance only | |
| **Typical Hours (UTC)** | e.g., 08:00–18:00 UTC | |
| **Typical Session Duration** | e.g., 30 min – 2 hours | |
| **Typical Frequency** | e.g., Weekly / Monthly / Quarterly / On-demand | |
| **Maintenance Window Required?** | Yes / No — If yes, must align with OT_MaintenanceWindows watchlist | |

### Destination Baseline

| Destination Asset | IP Address | Purdue Level | Purpose | Protocols Used |
|------------------|------------|:---:|---------|---------------|
| | | | | |
| | | | | |
| | | | | |
| | | | | |

### Protocol and Behaviour Baseline

| Parameter | Normal Pattern | Anomaly Threshold |
|-----------|---------------|-------------------|
| **Protocols Used** | e.g., RDP to jump server, then OPC-UA to historian | Alert on: any protocol not listed |
| **Data Transfer Volume** | e.g., < 50 MB per session | Alert on: > 200 MB or any outbound transfer to vendor IP |
| **Lateral Movement** | e.g., Jump server → HMI-01 only | Alert on: access to any asset not listed in destination baseline |
| **Tool Usage** | e.g., Vendor engineering software (named) | Alert on: PowerShell, cmd.exe, PsExec, WMI from vendor session |

---

## Anomaly Detection Rules

Based on the baseline above, the following detection rules should be configured:

| Detection | KQL / Rule Reference | Enabled |
|-----------|---------------------|:---:|
| Session outside maintenance window | UC-ICS-010_Vendor_Session_Anomaly.kql | ☐ |
| Access to out-of-scope assets | UC-ICS-010 (scope check) | ☐ |
| Session from unknown source IP | Custom rule based on Source IP Range above | ☐ |
| Session exceeding duration threshold | Custom rule based on Temporal Baseline above | ☐ |
| Unexpected protocol usage | UC-ICS-001 adapted for vendor source IPs | ☐ |
| Remote access followed by OT network access | UC-ICS-009 | ☐ |

---

## Incident History

| Date | Incident / Finding | Severity | Resolution |
|------|-------------------|----------|------------|
| | | | |
| | | | |

---

## Review and Approval

| Role | Name | Date |
|------|------|------|
| Vendor Relationship Owner | | |
| OT Engineering Lead | | |
| SOC Analyst / Manager | | |

**Review Frequency:** After each maintenance engagement, or annually at minimum  
**Next Review Date:** _______________
