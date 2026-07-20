# Sample MOU Between IT Security and OT Engineering

**Chapter 2 Practitioner's Toolkit Asset
Format:** Template Memorandum of Understanding

## How to Use This Template

This is a template Memorandum of Understanding (MOU) between an organisation's IT Security function and its OT Engineering function. It is *bilateral* by design, governing the day-to-day working relationship between two functions that must collaborate for OT cyber defence to work.

Placeholders are marked `\[LIKE\_THIS]`. Replace them with your organisation's specifics before use. The MOU should be reviewed annually, signed by the named heads of both functions, and held jointly.

The MOU is distinct from, and should be completed *before*, the following:

* The CSIRT Charter (Chapter 11 toolkit), which is multi-party (IT Security, OT Engineering, Operations, Legal, Executive) and operational for incidents.
* The RACI Matrix for Hybrid SOC Model (Chapter 14 toolkit), which sits at the programme level for managed service or hybrid delivery.
* The Engineering Liaison Role Charter (Chapter 14 toolkit), which defines the named bridging role between the two functions.

The MOU establishes the foundation. The other instruments build on it.

## Template Begins

\---

# Memorandum of Understanding

## Between \[ORGANISATION\_NAME] IT Security and \[ORGANISATION\_NAME] OT Engineering

**Document Reference:** \[MOU\_REF\_NUMBER]
**Version:** \[VERSION\_NUMBER]
**Effective Date:** \[EFFECTIVE\_DATE]
**Review Date:** \[REVIEW\_DATE] (annually thereafter)

## 1\. Purpose

This Memorandum of Understanding establishes the working relationship, roles, responsibilities, decision authorities, and information sharing protocols between \[ORGANISATION\_NAME] IT Security and \[ORGANISATION\_NAME] OT Engineering for the protection of operational technology assets that support \[DESCRIBE\_OPERATIONAL\_REMIT, e.g., water treatment and supply, power generation, manufacturing of X].

The purpose of this MOU is to ensure that:

1. Cyber security activities affecting OT assets are conducted with the operational, safety, and process knowledge of the engineering function.
2. OT engineering decisions affecting cyber security posture are made with the threat, detection, and response context of the security function.
3. Both functions operate against a shared understanding of authority boundaries, particularly the principle that any action affecting process control requires explicit OT engineering approval.
4. Information necessary to protect the organisation's OT assets flows between functions in a structured, predictable, and trusted manner.

This MOU operates in support of, and consistent with, \[REFERENCE\_OVERARCHING\_POLICIES, e.g., the Information Security Policy, the OT Safety Management System, the Incident Response Policy].

## 2\. Parties

|Party|Function|Lead Signatory|Operational Owner|
|-|-|-|-|
|IT Security|\[IT Security function description]|\[Chief Information Security Officer name and title]|\[SOC Manager name and title]|
|OT Engineering|\[OT Engineering function description]|\[Head of Engineering / OT Director name and title]|\[OT Engineering Lead name and title]|

The signatories accept that the MOU is binding on their respective functions and that they are accountable for its operation and review.

## 3\. Scope

### 3.1 In Scope

This MOU applies to:

1. All \[ORGANISATION\_NAME] OT assets at \[SITES\_IN\_SCOPE], including industrial control systems, supervisory systems, engineering workstations, human machine interfaces, historians, safety instrumented systems, and supporting network infrastructure.
2. All security-related activities affecting those assets, including monitoring, detection, threat hunting, incident response, vulnerability management, change management, and tooling deployment.
3. All operational changes to those assets that may affect cyber security posture, including new device installations, network re-architecture, vendor remote access provisioning, and software updates.

### 3.2 Out of Scope

This MOU does not cover:

1. IT-only assets and services not interacting with OT (those operate under the standard IT Security mandate).
2. Physical security and access control to OT facilities (covered separately by \[REFERENCE\_PHYSICAL\_SECURITY\_POLICY]).
3. Functional safety system design and validation (covered by \[REFERENCE\_FUNCTIONAL\_SAFETY\_PROCESS]). Cyber security inputs to safety reviews are addressed under Section 7.

## 4\. Roles and Responsibilities

### 4.1 IT Security Responsibilities

IT Security is responsible for:

1. **Detection.** Operating the Security Operations Centre, including SIEM (Microsoft Sentinel), network monitoring (Zeek and Suricata at IT/OT boundaries), endpoint detection on IT-managed Windows assets in OT zones, and threat intelligence enrichment.
2. **Triage and investigation.** Receiving, triaging, and investigating security events affecting OT assets according to the OT Alert Triage SOP and the agreed severity matrix.
3. **Threat intelligence.** Providing OT-relevant threat intelligence to OT Engineering, including sector-specific adversary profiles (using Microsoft threat actor naming), vulnerability advisories applicable to deployed OT products, and indicators of compromise observed in similar environments.
4. **Detection engineering.** Developing, tuning, and maintaining detection rules for OT-relevant threats, using the ICS Detection Use Case Template, with engineering input on false positive characterisation and operational context.
5. **Tooling.** Selecting, deploying, and operating security tooling (network sensors, SIEM connectors, threat intelligence platforms) in accordance with the Chapter 2 "Do No Harm" Checklist and the Safe vs. Unsafe Security Activities reference.
6. **Reporting and assurance.** Producing security reporting, regulatory submissions (NIS 2, NCSC CAF, sector regulator submissions), and audit evidence relating to OT cyber security.
7. **Continuous improvement.** Tracking detection coverage against ATT\&CK for ICS, identifying gaps, and proposing improvements with engineering input.

### 4.2 OT Engineering Responsibilities

OT Engineering is responsible for:

1. **Operational context.** Providing the SOC with the operational context required to triage, investigate, and respond to OT security events, including asset criticality, process function, maintenance schedules, and known vendor activity.
2. **Approval authority.** Approving or rejecting proposed security activities affecting OT assets, including tooling deployments, network changes, account changes, and incident response actions, in accordance with the authority framework in Section 5.
3. **Safety position.** Maintaining and providing fail-safe position documentation for crown jewel assets, in support of incident response decision-making.
4. **Asset inventory.** Maintaining the operational asset inventory in support of the OT Asset Register watchlist used by the SOC, including notifying the SOC of new assets, decommissioned assets, and configuration changes.
5. **Maintenance windows.** Maintaining the OT Maintenance Windows watchlist used by the SOC for alert suppression and authorised activity correlation. Notifying the SOC of planned and emergency maintenance.
6. **Operational change notification.** Notifying the SOC of operational changes with cyber security implications (new vendor remote access, new network paths, new software installations) before they occur.
7. **Investigation support.** Providing engineering support to security investigations on OT assets, including log retrieval from devices not directly integrated to the SIEM, console access to engineering workstations and HMIs, and protocol analysis support.
8. **Incident response participation.** Participating in the OT CSIRT during incident response, providing the engineering decision-maker role for any action affecting process control.

## 5\. Approval Authority Framework

Decisions affecting OT cyber security follow the authority framework below. The framework follows the principle that authority scales with operational risk: routine activities are unilateral, cross-functional activities are joint, and process-affecting activities require explicit engineering approval.

### 5.1 IT Security Sole Authority

IT Security may proceed without OT Engineering approval for:

1. Detection rule development and tuning that does not affect alert volumes received by engineering.
2. Investigation of security events confined to IT-managed Windows assets in OT zones (engineering workstations, HMIs) where investigation activity does not require interaction with the device beyond standard EDR telemetry collection.
3. Threat intelligence production and dissemination.
4. SOC internal process changes.

### 5.2 Joint Approval Required

Both IT Security and OT Engineering must approve:

1. Deployment of new security tooling in OT zones (sensors, agents, log forwarders).
2. Changes to the OT Asset Register schema or population.
3. Changes to the OT Maintenance Windows watchlist process.
4. New detection rules that may generate alerts requiring engineering investigation.
5. Network changes affecting OT segments, including SPAN port additions, firewall rule changes at the IDMZ, and VLAN modifications.
6. Vulnerability management actions affecting OT assets, including patch deployments and configuration changes.

### 5.3 OT Engineering Veto Authority

OT Engineering retains absolute authority to veto or defer any action proposed by IT Security where:

1. The action could affect process safety.
2. The action could affect process availability during a production-critical period.
3. The action involves a Level 0, Level 1, or Level 2 asset (PLC, RTU, DCS controller, safety instrumented system).
4. The action involves a vendor-certified configuration that would be invalidated by the change.

The veto authority is not optional and is not negotiable. The structure of this authority is the foundation on which the rest of the working relationship rests.

### 5.4 Incident Response Authority

During an active incident, the CSIRT charter (Chapter 11) takes precedence. The Incident Commander role rotates by incident type, with OT-impacting incidents commanded jointly by IT Security and OT Engineering. Engineering retains the safety veto on all containment and response actions affecting OT assets.

## 6\. Operating Mechanisms

The functions will operate the following structured touchpoints:

### 6.1 Weekly Operational Sync

**Cadence:** Weekly, 30 minutes.
**Attendees:** SOC Manager (or delegate), OT Security Engineering Liaison, on-call OT Engineering representative.
**Purpose:** Operational handover of the past week, upcoming planned activities, current detection tuning state, false positive rate against engineering, and immediate-term tooling or change plans.

### 6.2 Monthly Joint Review

**Cadence:** Monthly, 60 minutes.
**Attendees:** SOC Manager, OT Engineering Lead, Engineering Liaison, representative from Operations (rotating site).
**Purpose:** Review monthly metrics (detection coverage, MTTD/MTTR, false positive escalation rate), tabletop and incident review outcomes, programme maturity progression, and forward-looking change pipeline.

### 6.3 Quarterly Programme Review

**Cadence:** Quarterly, 90 minutes.
**Attendees:** CISO, Head of Engineering / OT Director, SOC Manager, OT Engineering Lead, Operations leadership, plus executive sponsor by invitation.
**Purpose:** Strategic review of programme health, maturity assessment outcomes, audit and regulatory standing, resource needs, and any escalations requiring leadership attention.

### 6.4 Annual MOU Review

**Cadence:** Annually, on or before the anniversary of the effective date.
**Attendees:** Signatories of this MOU and named operational owners.
**Purpose:** Review of the MOU's effectiveness, update of placeholders and named individuals, ratification or amendment.

## 7\. Information Sharing Protocols

### 7.1 What IT Security Shares with OT Engineering

1. **Detection alerts affecting OT assets.** Pushed in real time via the agreed channel (\[CHANNEL\_NAME, e.g., a dedicated Microsoft Teams channel or ServiceNow queue]).
2. **Threat intelligence relevant to deployed OT products and the organisation's sector.** Delivered weekly in a structured briefing format using the Strategic Intelligence Briefing Template (Chapter 10).
3. **Vulnerability advisories applicable to deployed OT assets.** Delivered as they are issued, with applicability assessment using the Vulnerability Intelligence Assessment Template (Chapter 10).
4. **Detection coverage and gap reporting.** Delivered quarterly via the joint programme review.
5. **Incident summaries and lessons learned.** Delivered within ten working days of incident closure.

### 7.2 What OT Engineering Shares with IT Security

1. **Asset register updates.** Pushed at the point of change, with weekly summary reconciliation.
2. **Maintenance window schedule.** Maintained as a Microsoft Sentinel watchlist (`OT\_MaintenanceWindows`) consumed by detection rules and triage workflows.
3. **Vendor remote access activity.** Notification of planned vendor sessions in advance; out-of-hours emergency access notified within 24 hours.
4. **Operational changes with cyber implications.** Notification at the point the change is proposed, in advance of approval.
5. **Process events that may correlate with security events.** Notification at the point of awareness, particularly for events that may explain anomalous telemetry.

### 7.3 Confidentiality and Handling

Information shared under this MOU is for the protection of \[ORGANISATION\_NAME] OT assets. Sensitive information (asset register, threat intelligence, vulnerability details) is handled in accordance with \[REFERENCE\_INFORMATION\_CLASSIFICATION\_POLICY]. The TLP (Traffic Light Protocol) markings apply for external-origin threat intelligence and may not be redistributed contrary to source markings.

## 8\. Escalation Procedures

### 8.1 Operational Escalation Path

For operational disagreements (a proposed action or denial that one party believes should be revisited):

1. **Level 1.** SOC Manager and OT Security Engineering Liaison attempt resolution. Target: within one working day.
2. **Level 2.** Head of SOC and OT Engineering Lead attempt resolution. Target: within three working days.
3. **Level 3.** CISO and Head of Engineering / OT Director attempt resolution. Target: within five working days.
4. **Level 4.** Joint escalation to the Executive Sponsor or designated decision-maker. Decision is binding.

### 8.2 Incident Escalation

During an active incident, the CSIRT activation procedure (Chapter 11) supersedes this escalation path. Incident-time disputes are resolved by the Incident Commander, with engineering retaining the safety veto.

### 8.3 Conflict Resolution Principles

When the functions disagree, the resolution process operates on three principles:

1. **Operational continuity is the default outcome of disagreement.** Where the functions cannot agree on a proposed security action affecting OT, the default is that the action is not taken until agreement is reached. The exception is an active incident where the safety veto framework applies.
2. **The party proposing change carries the burden of justification.** Where IT Security proposes a change, the SOC must articulate the threat, the proposed control, the operational risk, and the compensating controls. Where OT Engineering proposes change (or deferral), engineering must articulate the operational rationale.
3. **Disagreements are documented.** Recurring disagreements indicate a structural gap and are surfaced to the quarterly programme review for systemic resolution.

## 9\. Performance Measurement

The effectiveness of this MOU is measured through the joint metrics maintained by both functions, including (but not limited to):

1. **Mean time to detect (MTTD)** for OT security events.
2. **OT false positive rate** measured as alerts escalated to engineering divided by alerts where engineering investigation confirmed a true positive or required action.
3. **Engineering availability for security triage** measured as the percentage of OT security alerts triaged within the agreed SLA with engineering input.
4. **Cross-functional tabletop participation** measured as the number of joint exercises conducted per quarter and the participation rate of named CSIRT members.
5. **MOU annual review completion** as a programme health indicator.

Targets for these metrics are set in the joint programme review and reviewed quarterly.

## 10\. Term, Amendment, and Termination

### 10.1 Term

This MOU is effective from the date signed below and remains in force until amended or terminated.

### 10.2 Amendment

This MOU may be amended at any time with the written agreement of both signatories. Amendments are subject to the same review and approval process as the original MOU. Minor amendments (updates to named individuals, contact details, scoping changes) may be made by the operational owners and ratified at the next annual review.

### 10.3 Termination

Termination of this MOU requires the written agreement of both signatories and the executive sponsor. Termination does not relieve either function of the underlying organisational obligation to defend OT assets cooperatively; it requires that a replacement governance instrument is in place.

## 11\. Signatures

|Function|Name|Title|Signature|Date|
|-|-|-|-|-|
|IT Security|\[Name]|\[Chief Information Security Officer]|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|
|OT Engineering|\[Name]|\[Head of Engineering / OT Director]|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|
|Executive Sponsor (acknowledgement)|\[Name]|\[Chief Operating Officer / Executive Director]|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_|

## Template Ends

\---

## Customisation Notes

**On sectors with regulatory specifics.** For organisations subject to NIS 2, NCSC CAF, NERC CIP, or sector regulator obligations (Ofwat, Ofgem, HSE, FDA), add a section referencing the relevant obligations and the role each function plays in evidencing them. This is particularly important for incident notification timelines, where the 24-hour NIS 2 threshold makes the speed of cross-functional escalation a regulatory matter.

**On MSSP and hybrid delivery.** Where the SOC capability is delivered by a managed security services provider, this MOU should be supplemented by:

1. A tri-party operating agreement involving the MSSP, IT Security (as the client function holding the MSSP contract), and OT Engineering.
2. A RACI Matrix for the Hybrid SOC Model (Chapter 14 toolkit) that clarifies which activities are MSSP-delivered and which are client-retained.
3. Explicit handling of out-of-hours engineering availability, which is the single most common point of friction in MSSP/OT engagements.

**On multi-site organisations.** Where the organisation operates multiple OT sites with different engineering teams (a typical pattern in water utilities, distributed generation, and multi-plant manufacturing), the MOU should be supplemented by site-level operating annexes that capture local specifics: named local engineering contacts, site-specific maintenance window practices, local change management interfaces, and any site-specific regulatory considerations.

**On the trust foundation.** This MOU is the formalisation of a trust relationship, not a substitute for it. Its real value is in the conversation that produces it, the working through of authority boundaries, escalation paths, and information sharing protocols. A signed MOU without that conversation is paperwork. A working trust relationship without an MOU survives the people who built it but does not survive their departure. Build the relationship, then formalise it.

