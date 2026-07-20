# OT Incident Communication Template Library
# ================================================================
# Description: Pre-formatted communication templates for OT
#   security incidents. Covers internal alerts, regulatory
#   notifications, executive briefings, and vendor communications.
#
# Usage: Customise with organisation-specific details (names,
#   contacts, regulatory authority). Pre-populate where possible
#   and store in accessible location (SOC wiki, Teams, SharePoint).
#
# Reference: Chapter 11 — Purpose-Built Incident Response
# ================================================================

---

## Template 1: Internal Alert to Operations

**Use when:** SOC identifies activity that may affect OT operations.

```
SUBJECT: [SEV-X] Security Alert — [Brief Description]

TO:       Operations Shift Supervisor, Plant Manager
CC:       OT SME, Engineering Liaison, CISO
PRIORITY: [Urgent / High / Normal]

SUMMARY:
At [TIME] on [DATE], the SOC detected [brief description of
activity] affecting [asset name] ([IP address]) at Purdue Level
[X]. This asset is classified as Crown Jewel Tier [X] and
supports [process function description].

CURRENT STATUS:
• Production impact: [None observed / Describe impact]
• Safety system status: [Normal / Under assessment / Alarmed]
• Investigation status: [Active — assigned to [analyst name]]

ACTIONS TAKEN:
• [List actions taken — e.g., "Enhanced monitoring deployed on
  affected subnet", "EDR telemetry collected from source system"]

ACTIONS REQUESTED FROM OPERATIONS:
• [Specific requests — e.g., "Confirm process operating normally",
  "Prepare for potential mode change to manual control",
  "Stand by for containment decision"]

NEXT UPDATE: [TIME] or sooner if status changes.

SOC CONTACT: [Analyst name] — [Phone] — [Teams]
```

---

## Template 2: NIS 2 Early Warning (24 Hours)

**Use when:** Incident meets NIS 2 "significant incident" threshold. Submit within 24 hours of becoming aware.

```
SUBJECT: NIS 2 Early Warning — Cybersecurity Incident — 
         [Organisation Name]

TO:       [National Competent Authority / National CSIRT]
FROM:     [Organisation Name — Compliance / Legal Team]
DATE:     [Date and Time of Submission]

Pursuant to Article 23(4)(a) of Directive (EU) 2022/2555:

1. REPORTING ENTITY
   Name:       [Organisation legal name]
   Sector:     [Energy / Water / Transport / etc.]
   Designation:[Essential Entity / Important Entity]
   Member State:[Country]

2. DATE AND TIME OF AWARENESS
   The organisation became aware of this incident at [TIME]
   on [DATE].

3. NATURE OF INCIDENT
   [Brief description — e.g., "Suspected targeted intrusion
   affecting industrial control system infrastructure. Confirmed
   adversary presence on engineering workstations with access to
   process control networks."]

4. SUSPECTED CAUSE
   [If determinable — e.g., "Compromised vendor remote access
   credentials", "Spear-phishing leading to lateral movement",
   "Under investigation"]

5. CROSS-BORDER IMPACT ASSESSMENT
   [Assessment of potential impact on other member states or
   entities — e.g., "No cross-border impact identified at this
   stage" or "Potential impact on interconnected grid operators
   in [country]"]

6. INITIAL RESPONSE ACTIONS
   [Summary — e.g., "Cross-functional CSIRT activated. Affected
   systems at IT/OT boundary contained. Enhanced monitoring
   deployed. Forensic investigation in progress."]

7. POINT OF CONTACT (24/7)
   Name:  [Name]
   Role:  [Role — e.g., CISO, Incident Response Lead]
   Phone: [Number]
   Email: [Email]

NOTE: This is an early warning pursuant to Article 23(4)(a). 
Incident notification (72-hour) and final report (1-month) 
will follow per the prescribed timeline.
```

---

## Template 3: NIS 2 Incident Notification (72 Hours)

**Use when:** Follow-up to the early warning. Submit within 72 hours of becoming aware.

```
SUBJECT: NIS 2 Incident Notification — [Organisation Name] — 
         [Incident Reference]

TO:       [National Competent Authority / National CSIRT]
FROM:     [Organisation Name — Compliance / Legal Team]
DATE:     [Date and Time of Submission]
REF:      Early Warning submitted [DATE] — [Reference number]

Pursuant to Article 23(4)(b) of Directive (EU) 2022/2555:

1. INCIDENT UPDATE
   Assessment of severity and impact has [been updated / 
   remained unchanged] since the early warning.

2. SEVERITY AND IMPACT
   Severity: [As classified — SEV-1/2/3]
   Operational impact: [Description of impact to essential service]
   Duration: [Ongoing / Resolved at TIME on DATE]
   Affected systems: [High-level description — e.g., "Engineering
   workstations and SCADA system components"]
   Service disruption: [Yes — describe / No]

3. ROOT CAUSE (Preliminary)
   [Current understanding — e.g., "Initial access via compromised
   vendor remote access credentials. Lateral movement using
   living-off-the-land techniques. No custom malware identified."]

4. INDICATORS OF COMPROMISE
   [Share at TLP:AMBER unless advised otherwise by authority.
   Include hashes, IPs, domains, TTPs as appropriate.]

5. REMEDIATION ACTIONS
   [Summary of containment, eradication, and recovery actions
   taken and in progress.]

6. FOLLOW-UP ACTIONS PLANNED
   [Summary of remaining investigation, hardening, and monitoring
   activities.]

7. ASSISTANCE REQUIRED
   [Yes — specify / No]

8. POINT OF CONTACT
   [Same as early warning or updated]

NOTE: Final report will be submitted within one month per 
Article 23(4)(d).
```

---

## Template 4: Executive Briefing (During Active Incident)

**Use when:** Providing structured updates to executive leadership during an active OT security incident.

```
OT SECURITY INCIDENT BRIEFING
==============================
Incident:  [ID]
Severity:  [SEV-X]
Briefing:  #[Number] — [DATE] [TIME]
Status:    [Active / Contained / Eradicated / Recovering]

SITUATION SUMMARY (2–3 sentences):
[Plain-language summary for non-technical audience. E.g., "An 
adversary gained access to engineering workstations through 
compromised vendor credentials. They accessed but did not modify
process control systems. The affected systems have been contained
and production is unaffected."]

PRODUCTION IMPACT:
[None / Degraded — [describe] / Disrupted — [describe]]
[Estimated duration of impact if applicable]

SAFETY STATUS:
[Normal / Safety systems operating normally / Under assessment]

FINANCIAL IMPACT (Estimated):
[Production loss: £X / Response costs: £X / Unknown]

REGULATORY STATUS:
[NIS 2 early warning: Submitted / Not required]
[Sector regulator notification: [Status]]

KEY DECISIONS MADE:
• [Decision 1 — who decided, rationale]
• [Decision 2 — who decided, rationale]

DECISIONS REQUIRED FROM LEADERSHIP:
• [Decision needed — options and recommendations]

NEXT BRIEFING: [TIME] or sooner if status changes.
```

---

## Template 5: Vendor Notification (Supply Chain Incident)

**Use when:** An incident involves a third-party vendor's systems, credentials, or access.

```
SUBJECT: URGENT — Security Incident Involving [Vendor Name] Access

TO:       [Vendor Security Contact / Account Manager]
CC:       [Internal Legal, CISO, Procurement]

Dear [Vendor Contact],

We are writing to inform you of a security incident involving 
access associated with [Vendor Name] to our operational 
technology environment.

INCIDENT SUMMARY:
On [DATE] at [TIME], our security operations centre detected 
[brief description — e.g., "an unauthorised session using 
[Vendor] remote access credentials that accessed engineering 
workstations outside contracted support hours"].

IMMEDIATE ACTIONS REQUIRED:
1. Confirm whether the session at [TIME] on [DATE] was 
   authorised by [Vendor Name]
2. Investigate the security of your remote access credentials 
   and infrastructure
3. Provide a point of contact for joint investigation
4. Provide incident response findings within [X] business days

ACTIONS WE HAVE TAKEN:
[Summary — e.g., "We have suspended all [Vendor] remote access 
pending investigation. Enhanced monitoring has been deployed."]

CONTRACTUAL OBLIGATIONS:
Per [contract reference / MSA clause], [Vendor Name] is obligated 
to [reference relevant security obligations].

POINT OF CONTACT:
[Name, Role, Phone, Email]

We request acknowledgement of this notification within 
[4/8/24] hours and a response to the above within 
[timeframe].

Regards,
[Name, Title]
```

---

## Template 6: ISAC Information Sharing

**Use when:** Sharing incident intelligence with sector Information Sharing and Analysis Centre.

```
SUBJECT: [TLP:AMBER] Incident Intelligence — [Brief Description]

TO:       [ISAC distribution — e.g., E-ISAC, WaterISAC, relevant ISAC]
TLP:      AMBER (Recipients may share within their organisation 
          and with clients on a need-to-know basis)

SECTOR:   [Energy / Water / Manufacturing / etc.]
DATE:     [DATE]
SOURCE:   [Anonymous / Named — per organisational policy]

INCIDENT TYPE:
[Targeted intrusion / Ransomware / Supply chain / etc.]

SUMMARY:
[2–3 sentence description sufficient for members to assess 
relevance to their environment. E.g., "Targeted intrusion using 
compromised vendor remote access credentials to access DCS 
engineering workstations. Adversary exfiltrated process 
documentation and control logic. No process manipulation observed."]

TTPS OBSERVED (ATT&CK for ICS):
• [T0XXXX — Technique Name — Description]
• [T0XXXX — Technique Name — Description]

INDICATORS OF COMPROMISE:
[Share at agreed TLP level]
• File hashes: [SHA256]
• IP addresses: [IPs]
• Domains: [Domains]
• Other: [Tools, command patterns, etc.]

AFFECTED TECHNOLOGIES:
• Vendor/Product: [e.g., Siemens SIMATIC S7, Schneider Electric Modicon]
• Protocol: [e.g., Modbus TCP, S7Comm, OPC UA]
• Platform: [e.g., Windows Server 2019, specific SCADA version]

RECOMMENDED ACTIONS FOR MEMBERS:
1. [Specific action — e.g., "Review vendor remote access logs for 
   sessions outside contracted hours"]
2. [Specific action — e.g., "Deploy detection rule for [technique]"]
3. [Specific action — e.g., "Validate DCS configuration against 
   known-good baseline"]

QUESTIONS / COORDINATION:
Contact [Name/Anonymous] via [ISAC secure channel] for additional 
technical details.
```
