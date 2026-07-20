# OT Credential Risk Assessment Checklist

**Book Reference:** Chapter 5 — Defensible Architecture and Segmentation  
**Purpose:** Document the identity management reality in OT environments and identify detection opportunities.  
**Usage:** Complete per site or per process area. Use findings to inform detection engineering priorities.

---

## Section 1: Shared Accounts Assessment

For each Purdue level, document shared account usage.

### Level 2 — HMIs and SCADA Servers

| System Name | IP Address | Shared Account Name | Users Sharing | Individual Attribution Possible? | Authentication Logged? |
|------------|------------|-------------------|:---:|:---:|:---:|
| | | | | Yes / No | Yes / No |
| | | | | | |
| | | | | | |
| | | | | | |

**Risk Rating:** ☐ Critical (all shared, no logging) ☐ High (mostly shared) ☐ Medium (some shared) ☐ Low (named accounts)

**Compensating Controls:**
- ☐ Session recording on shared account systems
- ☐ Physical access logs correlated with logon times
- ☐ Network-based monitoring of actions taken during shared sessions
- ☐ Other: _______________

### Level 3 — Historians and Site Operations

| System Name | IP Address | Shared Account Name | Users Sharing | Individual Attribution Possible? | Authentication Logged? |
|------------|------------|-------------------|:---:|:---:|:---:|
| | | | | | |
| | | | | | |

### Level 3.5 — IDMZ Systems

| System Name | IP Address | Shared Account Name | Users Sharing | Individual Attribution Possible? | Authentication Logged? |
|------------|------------|-------------------|:---:|:---:|:---:|
| | | | | | |
| | | | | | |

---

## Section 2: Default Credentials Assessment

| Device Type | Vendor / Model | Purdue Level | Default Credentials Changed? | Can Credentials Be Changed? | If No, Vendor Ticket Ref |
|------------|---------------|:---:|:---:|:---:|---|
| PLC | | L1 | Yes / No / Unknown | Yes / No / Vendor Required | |
| RTU | | L1 | | | |
| HMI | | L2 | | | |
| Managed Switch | | L1–L3 | | | |
| Other | | | | | |

**Count Summary:**
- Devices with default credentials: _____ / _____ total
- Devices where credentials cannot be changed: _____
- Devices where vendor involvement is required to change: _____

**Risk Rating:** ☐ Critical (>50% default) ☐ High (25–50%) ☐ Medium (10–25%) ☐ Low (<10%)

**Detection Response:**
- ☐ UC-ICS-004 (Credential Brute Force) deployed for all systems with default/weak credentials
- ☐ Network-based access monitoring for systems where authentication cannot be changed
- ☐ Physical access controls as compensating measure

---

## Section 3: Service Accounts Assessment

| Service Account Name | Purpose | Systems Used On | Password Last Rotated | Password Stored In | Privileges |
|---------------------|---------|----------------|----------------------|-------------------|------------|
| | e.g., SCADA-to-Historian replication | | | e.g., Project file / Config / Vault | e.g., Admin / Read / Write |
| | | | | | |
| | | | | | |
| | | | | | |

**Key Findings:**
- Service accounts with administrative privileges: _____
- Service accounts with passwords in project files: _____
- Service accounts never rotated: _____
- Service accounts with password known to >5 people: _____

**Risk Rating:** ☐ Critical ☐ High ☐ Medium ☐ Low

---

## Section 4: Engineering Workstation Credentials

| Workstation Name | IP Address | Domain Joined? | Cached Credentials? | Local Admin Accounts | EDR Deployed? |
|-----------------|------------|:---:|:---:|---|:---:|
| | | Yes / No | Yes / No | | Yes / No |
| | | | | | |
| | | | | | |

**Key Findings:**
- Workstations with cached domain admin credentials: _____
- Workstations with local admin accounts shared across staff: _____
- Workstations without EDR: _____

---

## Section 5: Authentication Telemetry Coverage

| Purdue Level | Systems Present | Windows Auth Events Forwarded to SIEM? | EDR Deployed? | Other Auth Telemetry? | Coverage Assessment |
|:---:|:---:|:---:|:---:|---|---|
| L3.5 (IDMZ) | | Yes / Partial / No | Yes / No | | Full / Partial / None |
| L3 | | | | | |
| L2 | | | | | |
| L1 | | N/A (no Windows) | N/A | | |
| L0 | | N/A | N/A | | |

---

## Section 6: Gap Summary and Recommendations

| Gap Identified | Risk Level | Recommended Action | Detection Workaround | Priority |
|---------------|:---:|---|---|:---:|
| *Example: All HMIs use shared "Operator" account* | High | Implement named accounts or session recording | Monitor logon source IP + time correlation | P2 |
| *Example: 12 PLCs with unchanged default credentials* | Critical | Change where possible; deploy UC-ICS-004 | Network monitoring for all PLC access | P1 |
| | | | | |
| | | | | |
| | | | | |

---

## Approval and Review

| Role | Name | Date |
|------|------|------|
| SOC Manager | | |
| OT Engineering Lead | | |

**Review Frequency:** Annually or after significant changes  
**Next Review Date:** _______________
