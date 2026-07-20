# CSIRT Contact Roster Template
# ================================================================
# Description: Cross-functional Computer Security Incident Response
#   Team (CSIRT) roster for OT incident response. Maintains contact
#   details, decision authorities, and escalation paths for all roles.
#
# Usage: Complete and maintain quarterly. Distribute to all CSIRT 
#   members and post in the SOC. Update immediately when personnel 
#   change. Test contact details during each tabletop exercise.
#
# Reference: Chapter 11 — Purpose-Built Incident Response
# ================================================================

## Document Control

| Field | Value |
|-------|-------|
| **Version** | 1.0 |
| **Last Updated** | [DATE] |
| **Next Review** | [DATE — Quarterly recommended] |
| **Owner** | [SOC Manager / CISO] |
| **Classification** | [Internal / Restricted] |

---

## IT Security

| Role | Primary | Backup | Phone | Email | Teams | Out-of-Hours |
|------|---------|--------|-------|-------|-------|-------------|
| **SOC Manager** | [Name] | [Name] | [Number] | [Email] | [Handle] | [Procedure] |
| **Tier 2 Analyst (OT-trained)** | [Name] | [Name] | [Number] | [Email] | [Handle] | On-call rota: [Link] |
| **Detection Engineer** | [Name] | [Name] | [Number] | [Email] | [Handle] | [Procedure] |
| **Incident Response Lead** | [Name] | [Name] | [Number] | [Email] | [Handle] | [Procedure] |
| **Forensic Analyst** | [Name] | [Name] | [Number] | [Email] | [Handle] | [Procedure] |
| **CTI Analyst** | [Name] | [Name] | [Number] | [Email] | [Handle] | [Procedure] |

**Decision Authority:** Leads cybersecurity investigation. Develops containment options with risk assessment. Does NOT execute containment actions affecting Purdue Levels 0–3 without joint approval.

---

## OT Engineering

| Role | Primary | Backup | Phone | Email | Teams | Out-of-Hours |
|------|---------|--------|-------|-------|-------|-------------|
| **OT Security SME** | [Name] | [Name] | [Number] | [Email] | [Handle] | [Procedure] |
| **Engineering Liaison** | [Name] | [Name] | [Number] | [Email] | [Handle] | [Procedure] |
| **Control Systems Engineer** | [Name] | [Name] | [Number] | [Email] | [Handle] | [Procedure] |
| **Safety Engineer** | [Name] | [Name] | [Number] | [Email] | [Handle] | [Procedure] |
| **Process Engineer** | [Name] | [Name] | [Number] | [Email] | [Handle] | [Procedure] |

**Decision Authority:** Leads safety assessment. Provides operational impact assessment. Holds VETO authority on any action that creates safety risk. Leads evidence collection from Purdue Level 0–2 systems.

---

## Plant Operations

| Role | Primary | Backup | Phone | Email | Teams | Out-of-Hours |
|------|---------|--------|-------|-------|-------|-------------|
| **Operations Manager** | [Name] | [Name] | [Number] | [Email] | [Handle] | [Procedure] |
| **Shift Supervisor (current)** | Per shift rota | — | [Control Room Phone] | — | — | Always staffed |
| **Plant Manager** | [Name] | [Name] | [Number] | [Email] | [Handle] | [Procedure] |

**Decision Authority:** Communicates production status and constraints. Authorises operational mode changes, controlled shutdowns, and manual operation. Coordinates field operators.

---

## Legal and Compliance

| Role | Primary | Backup | Phone | Email | Teams | Out-of-Hours |
|------|---------|--------|-------|-------|-------|-------------|
| **Legal Counsel** | [Name] | [Name] | [Number] | [Email] | [Handle] | [Procedure] |
| **Compliance Officer** | [Name] | [Name] | [Number] | [Email] | [Handle] | [Procedure] |
| **Data Protection Officer** | [Name] | [Name] | [Number] | [Email] | [Handle] | [Procedure] |

**Decision Authority:** Classifies incident against regulatory reporting thresholds. Coordinates external notifications. Advises on evidence preservation. Manages external communications.

---

## Executive Leadership

| Role | Primary | Backup | Phone | Email | Teams | Out-of-Hours |
|------|---------|--------|-------|-------|-------|-------------|
| **CISO** | [Name] | [Name] | [Number] | [Email] | [Handle] | [Procedure] |
| **CTO / VP Engineering** | [Name] | [Name] | [Number] | [Email] | [Handle] | [Procedure] |
| **CEO / MD** | [Name] | [Name] | [Number] | [Email] | [Handle] | [Procedure] |

**Decision Authority:** Authorises controlled shutdowns. Makes risk acceptance decisions. Approves external communications. Allocates emergency resources.

---

## External Contacts

| Organisation | Purpose | Contact | Phone | Email | SLA |
|-------------|---------|---------|-------|-------|-----|
| **MSSP / MDR Provider** | 24/7 monitoring, Tier 1 triage | [Name / NOC] | [Number] | [Email] | [Response SLA] |
| **Incident Response Retainer** | Specialist IR support | [Firm / Name] | [Number] | [Email] | [Retainer terms] |
| **OT Vendor 1** | [Vendor name — e.g., Siemens] | [Support contact] | [Number] | [Email] | [Support contract ref] |
| **OT Vendor 2** | [Vendor name — e.g., Schneider Electric] | [Support contact] | [Number] | [Email] | [Support contract ref] |
| **EDR Vendor** | Endpoint response support | [Vendor name / contact] | [Number] | [Email] | [Support tier] |
| **Law Enforcement** | Cyber crime reporting | [National/regional contact] | [Number] | [Email] | — |
| **NCSC** | UK — national cyber security | NCSC Incident Management | [Number] | incidents@ncsc.gov.uk | — |
| **ISAC** | Sector information sharing | [Relevant ISAC name] | [Number] | [Email] | — |
| **Competent Authority (NIS 2)** | Regulatory incident reporting | [Authority name] | [Number] | [Email] | 24hr early warning |
| **Insurer** | Cyber insurance notification | [Insurer / broker] | [Number] | [Email] | [Notification requirement] |

---

## Escalation Quick Reference

### SEV-1 (Critical — Safety/Environmental Impact)
1. **Immediately:** OT SME + Safety Engineer + Shift Supervisor
2. **Within 15 min:** Engineering Liaison + Operations Manager
3. **Within 30 min:** CISO + Plant Director
4. **Within 1 hour:** Regulatory Authority (if NIS 2 threshold met)
5. **Within 24 hours:** NIS 2 Early Warning submitted

### SEV-2 (High — Operational Impact)
1. **Immediately:** OT SME
2. **Within 15 min:** Engineering Liaison
3. **Within 30 min:** CISO
4. **Within 1 hour:** Operations Manager

### SEV-3 (Medium — OT Boundary)
1. **Within 30 min:** OT SME (advisory)
2. **Within 1 hour:** Engineering Liaison (advisory)
3. **Daily:** CISO (summary in SOC report)

### SEV-4 (Low — Anomalous, Likely Benign)
1. Included in daily SOC report
2. No immediate escalation required

---

## Roster Validation Checklist

- [ ] All primary contacts verified (phone tested within last quarter)
- [ ] All backup contacts verified
- [ ] Out-of-hours procedures tested
- [ ] External contacts and SLAs current
- [ ] Escalation paths reviewed with all CSIRT members
- [ ] Roster distributed to all CSIRT members and posted in SOC
- [ ] Next review date scheduled

**Last validation date:** [DATE]
**Validated by:** [Name]
