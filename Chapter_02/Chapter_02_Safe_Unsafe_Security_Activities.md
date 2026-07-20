# Safe vs. Unsafe Security Activities in OT

**Chapter 2 Practitioner's Toolkit Asset
Format:** One-page classification reference

## Purpose

This reference classifies the routine security operations activities that an IT-trained SOC will consider deploying into an OT environment, and tells you whether each is *Safe*, *Conditionally Safe*, or *Unsafe* by default. For each activity, it also defines the minimum approval level required before the activity is performed.

This is a planning and design reference, used when scoping tooling, telemetry, or process changes. It is distinct from the *Safe vs. Unsafe Actions Matrix* in Chapter 11's toolkit, which covers incident response actions during a live event (isolate host, kill process, force password reset, and so on).

## Classification Definitions

**Safe.** The activity is suitable for OT environments with no greater caution than would be applied in IT. Standard SOC change management is sufficient.

**Conditionally Safe.** The activity can operate in OT, but only with configuration changes, scoping limits, or compensating controls. The Chapter 2 "Do No Harm" Checklist must be completed before deployment.

**Unsafe.** The activity should not be performed against OT assets in its default form. Either an alternative method exists, or the activity is acceptable only in a controlled test environment off the live process network.

## Approval Levels

|Level|Description|Typical Approver|
|-|-|-|
|**L1**|SOC internal approval. Activity is IT-only or has no path to OT assets.|SOC Manager|
|**L2**|SOC plus Engineering Liaison approval. Activity crosses the IT/OT boundary or affects shared services.|SOC Manager and OT Security Engineering Liaison (Chapter 14)|
|**L3**|Joint approval. Activity directly touches OT assets at Purdue Level 3 or above.|SOC Manager, OT Engineering Lead, Operations Manager|
|**L4**|Change Advisory Board approval. Activity affects Purdue Level 2 or below, or affects safety instrumented systems.|Joint CSIRT, Plant Manager, Change Advisory Board, OT engineering sign-off documented|

## The Activity Classification

### Scanning

|Activity|Status|Approval|Notes|
|-|-|-|-|
|Passive network monitoring via SPAN port or network TAP|**Safe**|L2|The foundational OT visibility method. Zeek with CISA ICSNPP parsers is the recommended toolchain. Develops in Chapter 7.|
|Protocol-aware passive parsing (Zeek, Suricata in IDS mode)|**Safe**|L2|No packets sent to OT devices. Approval level reflects the need to coordinate sensor placement with engineering.|
|Authenticated vulnerability scanning of IT assets in OT-adjacent zones (Level 3.5, Level 4)|**Conditionally Safe**|L2|Acceptable on IT-managed assets in the IDMZ and corporate zones, with credentialed scanning only.|
|Active vulnerability scanning of OT assets (Tenable, Qualys, Rapid7 in default mode)|**Unsafe**|L4 if ever|Documented to crash legacy PLCs, fault HMIs, and disrupt control communications. NIST SP 800-82r3 explicitly warns against active scanning of control system networks without coordination. Use passive methods.|
|Port scanning (nmap, masscan) of OT segments|**Unsafe**|L4 if ever|Even SYN scans and ARP scans have caused device faults. If absolutely required, conducted in a maintenance window with engineering present and rollback agreed.|
|Asset discovery via SNMP polling of OT devices|**Conditionally Safe**|L3|Acceptable on network infrastructure (switches, firewalls) using read-only community strings or SNMPv3 with rate limiting. Not safe against PLCs and RTUs.|
|Asset discovery via ICS-native protocol queries (Modbus function code 43 device identification, EtherNet/IP List Identity)|**Conditionally Safe**|L3|OT-aware discovery tools (Nozomi, Claroty, Armis) use these methods carefully. Manual or unconstrained use is unsafe.|

### Agent Deployment

|Activity|Status|Approval|Notes|
|-|-|-|-|
|EDR on engineering workstations (Windows, Level 3)|**Conditionally Safe**|L3|Deploy in detect-only mode first. Tune extensively before enabling any blocking or response. Co-ordinate exclusions for control system applications with the vendor.|
|EDR on HMIs (Windows, often Level 2)|**Conditionally Safe**|L3|Higher operational risk than engineering workstations because HMI unavailability removes operator visibility. Detect-only mode mandatory until extensively validated.|
|Sysmon on Windows systems in OT|**Conditionally Safe**|L2|Lightweight telemetry generator. Acceptable on engineering workstations and HMIs with a defined configuration that excludes high-volume process control event sources.|
|Log forwarders (syslog, Windows Event Forwarding, file beats) on OT-zone Windows hosts|**Conditionally Safe**|L2|Resource impact must be measured. Buffer locally and forward asynchronously. Never forward in a mode that blocks on transport failure.|
|Software agents on PLCs, RTUs, DCS controllers, safety instrumented systems|**Unsafe**|Never|These devices run real-time or embedded operating systems that cannot accommodate additional software loads. Vendor support is voided. Process stability is at risk.|
|Discovery agents in the OT vendor's recommended architecture (e.g. Nozomi sensor appliances)|**Safe**|L3|Vendor-engineered passive sensors are different from "agents on controllers". Approval level reflects deployment co-ordination, not the technical risk.|

### Log Collection

|Activity|Status|Approval|Notes|
|-|-|-|-|
|Forwarding Windows Event Logs from OT-zone Windows hosts to Sentinel|**Safe**|L2|Foundational telemetry. Use Windows Event Forwarding or Azure Monitor Agent with buffering. ASIM normalisation applies. Develops in Chapter 7.|
|Forwarding syslog from network infrastructure (switches, firewalls, IDMZ devices)|**Safe**|L2|Network device logging is mature and well-understood. Approval reflects co-ordination, not risk.|
|Native OT device logs (where supported by PLCs, controllers, historians)|**Conditionally Safe**|L3|Where the device exposes a logging capability, use it. The "conditional" status reflects the need to validate that log retrieval does not affect process performance, particularly on resource-constrained devices.|
|Firewall logs at the IDMZ|**Safe**|L2|Critical telemetry source. The IDMZ is the primary boundary monitored for IT/OT traversal attempts.|
|Protocol logs from Zeek and Suricata sensors at OT network boundaries|**Safe**|L2|The passive sensors generate these logs locally; collection is from the sensor, not from OT assets.|
|Historian database queries for process data correlation|**Conditionally Safe**|L3|Acceptable using read-only accounts with rate-limited queries. Must not interfere with the historian's primary process data collection function.|

### Network Changes

|Activity|Status|Approval|Notes|
|-|-|-|-|
|Deploying a new passive monitoring sensor on a new SPAN port|**Conditionally Safe**|L3|Cabling work in operational environments must be scheduled with engineering. SPAN configuration on production switches requires change approval.|
|Adding new firewall rules at the IDMZ (deny rules, logging rules)|**Conditionally Safe**|L3|Always test in monitor mode first. Validate that legitimate maintenance and vendor traffic is not blocked. Co-ordinate with the OT change management process.|
|Modifying existing firewall rules in OT zones (Level 3 and below)|**Conditionally Safe**|L4|Higher risk because legitimate process communication paths may be affected. Engineering sign-off mandatory. Rollback plan tested.|
|VLAN reconfigurations affecting OT segments|**Unsafe**|L4 if ever|Communication paths between controllers and supervisory systems can be disrupted. Performed only during planned maintenance windows.|
|Inline IPS or NGFW blocking mode in OT segments|**Unsafe**|L4 if ever|Even legitimate-looking ICS traffic can match generic signatures. Use IDS detect-only mode for OT. Inline blocking is acceptable at the IDMZ boundary only, with extensive tuning and engineering acceptance.|
|SPAN port configuration on production OT switches|**Conditionally Safe**|L3|Most managed switches support SPAN without impact, but legacy switches and some vendor-specific platforms can experience degraded performance. Validate with the network vendor.|

### Password and Account Management

|Activity|Status|Approval|Notes|
|-|-|-|-|
|Resetting IT account passwords for users in IT zones|**Safe**|L1|Standard IT practice. No OT-side impact.|
|Resetting passwords for OT service accounts (HMI service accounts, historian accounts, engineering tool accounts)|**Unsafe**|L4|Authentication failures cause control system communication failures. Must be scheduled during maintenance windows with the OT change management process.|
|Forcing MFA on IT-side identities used to access OT systems via the IDMZ|**Safe**|L2|A core IDMZ control. Co-ordinate roll-out with the user population so that engineering and vendor access is not unexpectedly interrupted.|
|Account lockout policies (AD Group Policy) affecting operator accounts used at HMIs|**Unsafe**|L4 if ever|An operator locked out of an HMI mid-shift cannot manage a process upset. Operator account policies must be designed jointly with OT engineering and explicitly exempt safety-critical account types where appropriate.|
|AD-based password complexity changes affecting OT-used service accounts|**Conditionally Safe**|L3|Coordinate with the OT change management process. Some legacy control system applications cannot handle modern complexity requirements without code changes.|
|Forcing password rotation on accounts used by vendor remote access|**Conditionally Safe**|L3|Co-ordinate with the vendor management process. Failed vendor access during a critical maintenance window has direct production consequences.|

### Automated Response

|Activity|Status|Approval|Notes|
|-|-|-|-|
|SOAR automated enrichment of OT incidents (asset context, crown jewel tier, maintenance window status)|**Safe**|L1|Enrichment is read-only and improves analyst decisions. No action is taken on OT assets.|
|SOAR automated alerting and ticketing (notify CSIRT, raise ServiceNow ticket)|**Safe**|L1|Notification automation is uncontroversial. Ensure the OT engineering on-call rotation is in the notification path.|
|SOAR automated host isolation via EDR on engineering workstations|**Conditionally Safe**|L3|A human approval gate is required for any isolation action on a Level 3 asset. Engineering must be notified within the playbook.|
|SOAR automated host isolation via EDR on HMIs|**Unsafe**|L4 if ever|HMI isolation removes operator visibility. Manual decision with engineering input is mandatory.|
|Automated firewall blocking of suspicious IPs at the IDMZ|**Conditionally Safe**|L3|Acceptable for inbound blocking from internet sources. Never automated for OT-originating traffic (egress) because legitimate vendor and process traffic may be blocked.|
|Automated account disablement for OT service accounts or operator accounts|**Unsafe**|L4 if ever|Authentication-based response in OT is fundamentally different from IT. Disabled accounts can leave operators unable to manage a process upset. Manual decision only.|
|Automated quarantine of files on engineering workstations|**Conditionally Safe**|L3|Acceptable only if the quarantine action cannot interfere with control system executables, libraries, or configuration files. Maintain a tested whitelist of control application paths.|

## The Operating Principle

When in doubt, the principle is *passive over active, observe over intervene, advise over automate.* The mature OT SOC accepts that detection is its strongest contribution to OT cyber defence; *response* is a joint exercise with engineering, not a unilateral SOC action.

## How to Use This Reference

1. **Before deploying any tool or change in OT,** locate the activity in this reference. Confirm the status and the approval level required.
2. **For Conditionally Safe activities,** complete the *Chapter 2 "Do No Harm" Checklist* before proceeding. Engineering sign-off is a deployment gate, not a courtesy.
3. **For Unsafe activities,** the default is "do not perform". If the activity is genuinely required, escalate to the joint Change Advisory Board with a documented compensating control proposal, a rollback plan, and engineering acceptance recorded in the change ticket.
4. **Tailor this reference to your environment.** The classifications above are generic baselines. Your specific control systems, vendor support agreements, and risk appetite may dictate different ratings for specific activities. The format is the asset; the content is yours to adapt.

## Customisation Notes

Adapt the approval level definitions (L1 through L4) to match your organisation's actual governance structure. Some organisations operate with a different number of approval gates, or with named approvers different from those listed. The principle of an escalating gate as the activity moves closer to the live process is what matters; the specific labels are local.

For organisations subject to regulatory regimes that constrain OT changes (NERC CIP, NIS 2 incident reporting, sector regulator approvals), add a column to this reference identifying the regulatory implications of each activity. A SOC activity that triggers a regulatory reporting threshold is not just an operational decision.

