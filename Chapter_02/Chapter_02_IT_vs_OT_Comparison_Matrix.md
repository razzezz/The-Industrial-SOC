# IT vs. OT Comparison Matrix

**Chapter 2 Practitioner's Toolkit Asset
Format:** Printable quick-reference card

## Purpose

This matrix is the single-page distillation of the IT versus OT divergence that Chapter 2 explores in depth. It is designed for three purposes:

1. **Reference for SOC practitioners** moving into OT for the first time, as a desk-side reminder of where their IT instincts will mislead them.
2. **Onboarding material** for new SOC analysts joining the OT shift, alongside the *5 Questions to Ask Your OT Team* worksheet from Chapter 1.
3. **A shared artefact** for the first joint working session between IT Security and OT Engineering, where the matrix becomes the agenda for "where do we actually disagree, and why?".

Print it. Laminate it. Pin it next to the SOC console.

## How to Use This Matrix

For each row, identify which dimension a current discussion, alert, or proposed control touches. The "SOC Implication" column translates the difference into the operating behaviour the SOC must adopt. If your instinct sits in the IT column, pause and check the OT column before acting.

## The Twelve Dimensions

|#|Dimension|Enterprise IT|Operational Technology|SOC Implication|
|-|-|-|-|-|
|1|**Priorities**|Confidentiality, Integrity, Availability (CIA). Data protection is the primary currency.|Safety, Availability, Integrity, Confidentiality (SAIC). Safety overarches everything; process must run.|Triage and response decisions must weight safety and process availability above data containment. A "successful" containment that takes a process offline can be a worse outcome than the threat itself.|
|2|**Asset Lifecycle**|3 to 5 years for servers and endpoints. Refresh cycles are budgeted and routine.|15 to 30 years for PLCs, RTUs, DCS controllers. HMIs may run end-of-life operating systems certified by vendors against specific control applications.|The OT estate spans multiple technology generations. Detection and response strategies cannot assume modern OS support, current EDR compatibility, or vendor security updates.|
|3|**Patching Cadence**|Monthly Patch Tuesday cycles. Critical CVEs deployed within days.|Vendor-certified patches only. Deployed during planned maintenance windows. May only be available quarterly or during annual shutdowns.|A "critical CVE unpatched on an HMI" is not the same finding as on a corporate laptop. Compensating controls and exposure analysis matter more than patch status. Detection must assume the vulnerable population persists.|
|4|**Protocols**|TLS, HTTPS, SSH, Kerberos. Mostly authenticated and encrypted.|Modbus, DNP3, EtherNet/IP, OPC, S7Comm, BACnet, Profinet. Largely unauthenticated, unencrypted, designed for reliability not security.|Network monitoring at the OT boundary needs protocol-aware parsers (Zeek with the CISA ICSNPP parsers, Suricata with ICS rule sets). Standard NetFlow and TLS metadata are not enough.|
|5|**Endpoint Protection**|Standard EDR or XDR on workstations and servers. Agent-based detection is the default.|Limited or no agent coverage. EDR is conditional on engineering workstations and HMIs. Never deployed on PLCs, RTUs, DCS controllers, or safety instrumented systems.|Endpoint visibility on Level 0 to Level 2 assets is functionally absent. Network-level monitoring at IDMZ and process-zone boundaries carries the detection load that EDR carries in IT.|
|6|**Incident Response**|Isolate immediately. Containment first, investigation second. SOAR automation acceptable.|Coordinate with engineering before any containment action. Safety assessment first, then containment. Human-in-the-loop for any action affecting Level 0 to Level 3.|OT incident response playbooks (Chapter 11) require an explicit safety gate. Any automated containment that can affect OT assets must have an engineering approval step or be removed from the playbook.|
|7|**Change Velocity**|Rapid iteration. Deploy fast, fix fast, iterate. Continuous delivery and DevOps culture.|Slow, tested, validated. Change carries the risk of process disruption. Stability is the professional pride.|Security changes in OT move at the pace of the OT change management process, not the SOC's. Build that timing into detection rule deployment, sensor tuning, and tooling rollouts.|
|8|**Risk Tolerance**|Brief disruptions are acceptable. A service restart, a network blip, a rebooted server are normal cost of business.|Zero tolerance for unplanned process disruption. A security-induced outage is a safety event, a production loss, or a regulatory reportable incident.|False positives that trigger automated action are not "noise to be tuned later"; they are direct operational risk. The false positive escalation rate to OT engineering is a top-line SOC metric.|
|9|**Authority Structure**|Security can act unilaterally on hosts, traffic, accounts, and configurations within agreed remit.|Engineering and operations retain ultimate authority over anything that affects process control. Security advises and escalates; engineering decides.|The SOC cannot "make OT do" anything. Influence is earned through trust, evidence, and respect for engineering's mandate. The MOU in this toolkit formalises this authority boundary.|
|10|**Regulatory Drivers**|GDPR, PCI DSS, SOX, ISO 27001. Data-centric and confidentiality-centric.|NIS 2, NCSC CAF v4.0, NERC CIP, ISA/IEC 62443, NIST SP 800-82r3, TSA Security Directives, sector regulators (Ofwat, Ofgem, HSE). Availability and safety centric.|The framework basket is wider and the reporting timelines are tighter. NIS 2 requires initial notification within 24 hours of awareness. Detection capability is no longer a security question, it is a regulatory one. Chapter 4 develops this.|
|11|**Technology Refresh**|Continuous. Cloud, SaaS, container, ephemeral infrastructure. New tooling adopted within quarters.|Decadal and vendor-dependent. Replacement of a control system can be a multi-year capital project requiring re-validation of process safety.|Procurement leverage is rare and precious. The opportunity to embed security requirements (logging, authentication, secure development evidence) into a new control system purchase comes once a decade. Use it.|
|12|**Operational Culture**|"Move fast, deny by default." Security identity is built on speed and decisive action.|"Don't touch what works, allow by default for process." Engineering identity is built on reliability and safety. Decades of well-meaning IT initiatives causing process disruption have produced earned wariness.|The cultural divide is the harder gap to close. Start by listening (the *5 Questions* worksheet from Chapter 1). Demonstrate "Do No Harm" before proposing changes. Deliver value before asking for changes.|

## How the Matrix Connects to Later Chapters

|Dimension|Develops in|
|-|-|
|Priorities (#1), Risk Tolerance (#8)|Chapter 11 (Purpose-Built Incident Response), Chapter 5 (Defensible Architecture)|
|Asset Lifecycle (#2), Technology Refresh (#11)|Chapter 6 (Asset Inventory), Chapter 13 (Tooling)|
|Patching Cadence (#3)|Chapter 4 (Regulatory Roadmap), Chapter 5 (Defensible Architecture)|
|Protocols (#4), Endpoint Protection (#5)|Chapter 7 (Visibility and Telemetry), Chapter 8 (Detection Engineering)|
|Incident Response (#6)|Chapter 11 (Purpose-Built Incident Response)|
|Change Velocity (#7), Authority Structure (#9)|Chapter 14 (Cross-Functional Collaboration)|
|Regulatory Drivers (#10)|Chapter 4 (The Regulatory Roadmap)|
|Operational Culture (#12)|Chapter 2 (this chapter), Chapter 14 (Cross-Functional Collaboration)|

## The One-Sentence Test

If your team is debating a proposed action in an OT environment, the matrix gives you the test: *Which column does this instinct sit in?* If it sits in the IT column and the asset is below Purdue Level 3, stop and apply the "Do No Harm" Checklist from Chapter 2 before proceeding.

## Customisation Notes

Adapt this matrix to your sector and your estate. The dimensions are stable; the specifics vary:

* **Water utilities** should add a row on regulatory inspection cadence (Ofwat, Environment Agency, DWI) and SCADA polling intervals that drive the definition of "normal" timing patterns.
* **Power generation** should add a row on NCSC CAF, grid code obligations and NERC CIP (where applicable) reporting thresholds.
* **Manufacturing** should add a row on Overall Equipment Effectiveness (OEE) impact, the operational metric against which any security-induced downtime is measured.
* **Oil and gas** should add a row on functional safety classification (SIL ratings) and the implications for any control that touches a safety instrumented system.

The matrix is a starting point. The conversation with OT engineering it provokes is the actual asset.

