# Human Attack Surface Assessment Checklist
# ================================================================
# Description: Structured checklist for evaluating the human
#   dimensions of ICS security risk: insider threat indicators,
#   social engineering susceptibility, credential hygiene, physical
#   access controls, and vendor/contractor access management.
#
# Usage: Complete jointly by the SOC and OT engineering teams.
#   Review quarterly or following any personnel, vendor, or
#   physical access change. Results feed into the threat model
#   (Chapter 10) and detection coverage planning (Chapter 7).
# ================================================================

## ASSESSMENT METADATA

- **Facility / Site**: [Name]
- **Assessment Date**: [Date]
- **IT Security Assessor**: [Name / Role]
- **OT Engineering Assessor**: [Name / Role]
- **Last Assessment Date**: [Date or "First Assessment"]
- **Next Scheduled Review**: [Date]

---

## 1. CREDENTIAL HYGIENE

### 1.1 Shared and Default Credentials

| # | Assessment Item | Status | Evidence / Notes | Risk Level |
|---|----------------|--------|-----------------|------------|
| 1.1.1 | Are default credentials changed on ALL PLCs, RTUs, and controllers? | ☐ Yes ☐ No ☐ Partial | | |
| 1.1.2 | Are default credentials changed on ALL HMIs and engineering workstations? | ☐ Yes ☐ No ☐ Partial | | |
| 1.1.3 | Are shared/generic accounts used for OT system access? | ☐ Yes ☐ No ☐ Partial | [List accounts if applicable] | |
| 1.1.4 | Is there a documented inventory of all shared credentials in the OT environment? | ☐ Yes ☐ No | | |
| 1.1.5 | Are shared credentials rotated on a defined schedule? | ☐ Yes ☐ No ☐ N/A | [Rotation frequency:] | |
| 1.1.6 | Are credentials stored securely (not written on labels, not in plaintext files)? | ☐ Yes ☐ No ☐ Partial | | |

### 1.2 Authentication Controls

| # | Assessment Item | Status | Evidence / Notes | Risk Level |
|---|----------------|--------|-----------------|------------|
| 1.2.1 | Do OT Windows systems use individual named accounts (not shared "operator" logins)? | ☐ Yes ☐ No ☐ Partial | | |
| 1.2.2 | Is multi-factor authentication (MFA) enforced for remote access to OT systems? | ☐ Yes ☐ No | | |
| 1.2.3 | Are administrative privileges on OT systems restricted to authorised personnel? | ☐ Yes ☐ No ☐ Partial | | |
| 1.2.4 | Is there a process for revoking credentials when personnel leave or change roles? | ☐ Yes ☐ No | [Timeframe for revocation:] | |
| 1.2.5 | Are OT system credentials separate from enterprise IT credentials? | ☐ Yes ☐ No ☐ Partial | | |

---

## 2. INSIDER THREAT INDICATORS

### 2.1 Access Controls and Monitoring

| # | Assessment Item | Status | Evidence / Notes | Risk Level |
|---|----------------|--------|-----------------|------------|
| 2.1.1 | Is access to engineering workstations limited to authorised engineers? | ☐ Yes ☐ No ☐ Partial | | |
| 2.1.2 | Are PLC programming operations logged and attributable to individual users? | ☐ Yes ☐ No ☐ Partial | | |
| 2.1.3 | Is there monitoring for after-hours access to OT control rooms or systems? | ☐ Yes ☐ No | | |
| 2.1.4 | Are changes to PLC/DCS logic tracked with version control? | ☐ Yes ☐ No ☐ Partial | | |
| 2.1.5 | Is there a process for peer review of control logic changes? | ☐ Yes ☐ No | | |

### 2.2 Personnel Risk Factors

| # | Assessment Item | Status | Evidence / Notes | Risk Level |
|---|----------------|--------|-----------------|------------|
| 2.2.1 | Is there an HR process for flagging personnel changes that may create insider risk (terminations, disciplinary actions, grievances)? | ☐ Yes ☐ No | | |
| 2.2.2 | Is the SOC notified of personnel departures with OT system access? | ☐ Yes ☐ No | [Notification timeframe:] | |
| 2.2.3 | Are exit procedures documented for personnel with OT administrative access? | ☐ Yes ☐ No | | |
| 2.2.4 | Is there a background check process for personnel with access to safety-critical systems? | ☐ Yes ☐ No | | |

---

## 3. SOCIAL ENGINEERING SUSCEPTIBILITY

### 3.1 Awareness and Training

| # | Assessment Item | Status | Evidence / Notes | Risk Level |
|---|----------------|--------|-----------------|------------|
| 3.1.1 | Have OT operators and engineers received security awareness training in the past 12 months? | ☐ Yes ☐ No ☐ Partial | [Completion %:] | |
| 3.1.2 | Does security awareness training include OT-specific scenarios (USB drops, vendor impersonation, phone-based social engineering)? | ☐ Yes ☐ No | | |
| 3.1.3 | Has a phishing simulation been conducted that includes OT-adjacent personnel? | ☐ Yes ☐ No | [Click rate:] | |
| 3.1.4 | Are OT personnel aware of the reporting process for suspicious emails, calls, or visits? | ☐ Yes ☐ No ☐ Unknown | | |

### 3.2 Information Exposure

| # | Assessment Item | Status | Evidence / Notes | Risk Level |
|---|----------------|--------|-----------------|------------|
| 3.2.1 | Is OT network architecture documentation stored securely with access controls? | ☐ Yes ☐ No | | |
| 3.2.2 | Are PLC project files and control logic backups stored with restricted access? | ☐ Yes ☐ No ☐ Partial | | |
| 3.2.3 | Is OT vendor/product information available publicly (e.g., job postings, social media, public tenders) that could aid adversary reconnaissance? | ☐ Yes ☐ No ☐ Unknown | | |
| 3.2.4 | Are engineering workstation screenshots or HMI displays shared externally (marketing materials, conference presentations)? | ☐ Yes ☐ No ☐ Unknown | | |

---

## 4. PHYSICAL ACCESS CONTROLS

### 4.1 Control Room and Plant Floor Access

| # | Assessment Item | Status | Evidence / Notes | Risk Level |
|---|----------------|--------|-----------------|------------|
| 4.1.1 | Is physical access to the control room restricted to authorised personnel? | ☐ Yes ☐ No | [Access control method:] | |
| 4.1.2 | Is physical access to OT network infrastructure (switches, TAPs, servers) restricted? | ☐ Yes ☐ No ☐ Partial | | |
| 4.1.3 | Are server rooms / network cabinets in the OT environment locked? | ☐ Yes ☐ No ☐ Partial | | |
| 4.1.4 | Is visitor access to OT areas logged and escorted? | ☐ Yes ☐ No ☐ Partial | | |
| 4.1.5 | Are USB ports on HMIs and engineering workstations physically or logically disabled? | ☐ Yes ☐ No ☐ Partial | | |

### 4.2 Removable Media Controls

| # | Assessment Item | Status | Evidence / Notes | Risk Level |
|---|----------------|--------|-----------------|------------|
| 4.2.1 | Is there a policy governing removable media use in the OT environment? | ☐ Yes ☐ No | | |
| 4.2.2 | Are USB drives scanned before use in OT systems? | ☐ Yes ☐ No ☐ Partial | [Scanning method:] | |
| 4.2.3 | Is removable media usage monitored (Sysmon, EDR, Windows Event Logs)? | ☐ Yes ☐ No ☐ Partial | | |
| 4.2.4 | Are personal devices (phones, laptops, USB drives) prohibited in the control room? | ☐ Yes ☐ No ☐ Partial | | |

---

## 5. VENDOR AND CONTRACTOR ACCESS MANAGEMENT

### 5.1 Remote Access

| # | Assessment Item | Status | Evidence / Notes | Risk Level |
|---|----------------|--------|-----------------|------------|
| 5.1.1 | Is vendor remote access to OT systems controlled through a dedicated access gateway? | ☐ Yes ☐ No | [Gateway type:] | |
| 5.1.2 | Is vendor remote access time-limited (enabled only during active sessions)? | ☐ Yes ☐ No | | |
| 5.1.3 | Are vendor remote sessions logged and monitored? | ☐ Yes ☐ No ☐ Partial | | |
| 5.1.4 | Do vendors use individual named accounts (not shared vendor credentials)? | ☐ Yes ☐ No ☐ Partial | | |
| 5.1.5 | Is the SOC notified when vendor remote access sessions are scheduled? | ☐ Yes ☐ No | [Notification method:] | |

### 5.2 On-Site Vendor Access

| # | Assessment Item | Status | Evidence / Notes | Risk Level |
|---|----------------|--------|-----------------|------------|
| 5.2.1 | Are vendor laptops scanned or inspected before connection to the OT network? | ☐ Yes ☐ No ☐ Partial | | |
| 5.2.2 | Are vendor on-site activities supervised by an engineering team member? | ☐ Yes ☐ No ☐ Partial | | |
| 5.2.3 | Is there a documented process for granting and revoking temporary vendor access? | ☐ Yes ☐ No | | |
| 5.2.4 | Are vendor activities during maintenance windows logged in the change management system? | ☐ Yes ☐ No ☐ Partial | | |

---

## RISK SUMMARY

| Category | Items Assessed | Compliant | Non-Compliant | Partial | Overall Risk |
|----------|---------------|-----------|---------------|---------|-------------|
| 1. Credential Hygiene | | | | | ☐ High ☐ Medium ☐ Low |
| 2. Insider Threat | | | | | ☐ High ☐ Medium ☐ Low |
| 3. Social Engineering | | | | | ☐ High ☐ Medium ☐ Low |
| 4. Physical Access | | | | | ☐ High ☐ Medium ☐ Low |
| 5. Vendor/Contractor | | | | | ☐ High ☐ Medium ☐ Low |
| **OVERALL** | | | | | **☐ High ☐ Medium ☐ Low** |

---

## PRIORITY REMEDIATION ACTIONS

| Priority | Finding | Category | Recommended Action | Owner | Target Date |
|----------|---------|----------|-------------------|-------|-------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
