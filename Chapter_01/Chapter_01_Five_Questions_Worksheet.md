# Chapter 1 Toolkit: The Five Questions to Ask Your OT Team

## Purpose

This worksheet exists for a single moment: your first substantive conversation with the OT engineering team whose environment you are now expected to help defend. It is designed for the SOC practitioner who has read Chapter 1, who understands the components of an ICS environment in concept, and who has not yet sat down with the engineers who actually run one.

You will not arrive at this conversation as the expert. You will arrive as a visitor in a domain that prizes stability, safety, and operational continuity above almost everything else. The questions below are constructed to help you listen, learn, and demonstrate respect for what the engineering team has built and is responsible for. They are also constructed to produce specific, actionable inputs that you will use across the remainder of this book.

The structure is deliberate. Five questions only. Each one is broad enough to invite the engineer to talk, narrow enough to keep the conversation grounded, and connected to a downstream artefact you will need later. If you ask these five questions well and listen carefully to the answers, you will leave the meeting with the foundations of a crown jewel scoring exercise, an asset prioritisation, a change management baseline, and a relationship that will pay back across every chapter that follows.

## How to Use This Worksheet

This is not a questionnaire to be filled in by email. It is a conversation guide. The engineering team should not see the worksheet itself, only your interest in their work.

Before the meeting, read each question and the associated notes. Understand why you are asking it and what you should listen for. During the meeting, ask the questions in your own words. Take handwritten notes if possible, laptops in OT engineering meetings often signal "this is an audit," which is the opposite of the tone you want. After the meeting, transcribe your notes into the capture sections at the end of this worksheet and identify which downstream activities each answer informs.

A useful rule of thumb: if you find yourself talking more than the engineer, stop and reset. The objective is to understand their environment, not to demonstrate your knowledge of yours.

## Setting the Conversation

Before you ask the first question, set the conversation. The opening matters more than any single question that follows.

Introduce yourself by role and remit, briefly. Explain that you are not there to assess, scan, audit, or recommend anything today. State plainly that your job is to help defend this environment and that you cannot do that without understanding it first. Ask whether they would prefer to talk in a meeting room, on the plant floor, or in their control room. The answer will tell you something about how they want to be engaged. Accept whatever they offer.

If you have time before the first question, ask the engineer how long they have worked here and what their background is. Most OT engineers have decades of experience and process engineering credentials that they are quietly proud of. Acknowledging this changes the dynamic of the conversation.

## The Five Questions

### Question 1: Tell me about what this facility produces or controls, and what would happen to the wider world if it stopped?

**Why this question matters.** Every conversation about OT security should begin with the physical process, not the technology that controls it. This question grounds the engineer in familiar territory and grounds you in the operational reality you are being asked to defend. The answer tells you what is at stake in language that is not abstract. It is also the question most likely to surface the sector context, the customer base, the regulatory drivers, and the public service dependency that will frame every subsequent discussion about risk.

**Listen for.** The downstream consequences of an outage, who depends on the output, how long an unplanned stoppage can be tolerated before secondary impacts begin, whether the process can be safely shut down at all or must be brought down through a controlled sequence, the seasonal or operational patterns that change the risk profile (peak demand, harvest cycles, batch production windows), and any regulated outputs (water quality, emissions, pharmaceutical purity, food safety).

**Useful follow-ups.** "What does a normal operating day look like?" "When is the busiest period of the year, and what changes during it?" "If you had to stop the process for an emergency, how long would that take?" "Who is the customer or beneficiary of what this facility produces?"

**Where the answer goes.** This is the foundational input to the Crown Jewel Identification Worksheet (Chapter 5), the regulatory applicability mapping (Chapter 4), and the operational impact assessment that will shape your incident response prioritisation (Chapter 11).

**Capture space.**

```
Process or output:

Who depends on it:

Tolerance for unplanned outage:

Seasonal or operational patterns:

Regulated outputs or sector-specific obligations:
```

### Question 2: Which systems or processes here would cause the most harm if they were manipulated, disrupted, or denied?

**Why this question matters.** OT engineers know their crown jewels. They may not call them that, and they will almost certainly not describe them through the lens of adversary objectives, but they know which systems must never fail, which interlocks protect human life, and which controllers, if compromised, would create consequences they have spent their careers preventing. This question lets them tell you, in their own terms. It also reveals the systems that will demand the highest detection coverage, the most careful change management, and the most considered incident response.

You are not asking them to score risk. You are asking them to tell you which systems they worry about most. The scoring comes later, and it comes from you, informed by their answer.

**Listen for.** Safety instrumented systems and the safety case they support, single points of failure (a single PLC, a single HMI, a single historian that, if lost, breaks an essential function), systems that cannot be safely restarted or rebuilt without a planned outage, legacy controllers with bespoke or undocumented logic, systems that integrate with external parties (vendor remote access, regulatory data submissions), and any systems where the engineer hesitates, the hesitation often signals genuine concern.

**Useful follow-ups.** "What would have to go wrong, and in what order, for a catastrophic event here?" "Are there interlocks or other safeguards that would catch it before it became serious?" "Is there a system you wish you could replace but cannot?" "If you had to evacuate the site, which systems would you want to verify were in a safe state first?"

**Where the answer goes.** Directly into the Crown Jewel Identification Worksheet (Chapter 5) and the prioritisation of the asset register (Chapter 6). Indirectly into the detection engineering backlog (Chapter 8), where crown jewel assets command the highest coverage priority, and into the IR playbook scope (Chapter 11).

**Capture space.**

```
Systems identified as highest consequence:

Safety instrumented systems present (yes / no / unsure):

Known single points of failure:

Systems engineer hesitated on:

Interlocks or safeguards mentioned:
```

### Question 3: What keeps you up at night, and what are your top three operational concerns for the year ahead?

**Why this question matters.** This question almost never produces an answer about cyber attacks, and that is precisely why it is essential. The honest answers will be about process safety, equipment reliability, the ageing skilled workforce, the obsolete controller that has not been supported by the vendor for fifteen years, the capital project that is over budget, the regulatory inspection that is overdue, or the new mandate from headquarters that the engineer cannot see how to meet.

You need to hear these answers because they tell you the priorities of the person whose cooperation determines whether your security programme succeeds. If you can frame your work as helping with the things that keep them up at night, rather than as adding new things to that list, you will find the working relationship transforms.

**Listen for.** Process safety incidents or near-misses (these are rarely volunteered but sometimes hinted at), ageing infrastructure and equipment reliability concerns, supply chain or spare parts availability, workforce and succession risk, regulatory pressure (especially safety regulators rather than cyber regulators), pressure from finance or operations on uptime targets, and recent or upcoming organisational change.

**Useful follow-ups.** "Has any of this changed in the last twelve months?" "What is outside your control that you wish you could influence?" "If you could fix one thing about how this site operates, what would it be?"

**Where the answer goes.** This shapes how you frame every subsequent security conversation. It also informs the business case work in Chapter 4 (regulatory leverage) and the metrics framework in Chapter 14 (joint KPIs that matter to OT, not just to security). Note the answers carefully; you will refer back to them throughout your engagement with this team.

**Capture space.**

```
Top three operational concerns:
1.
2.
3.

Process safety or reliability themes:

Workforce or succession risk:

External or regulatory pressure:

Recent or imminent change:
```

### Question 4: Walk me through how a change gets made to a control system here, from the request through to it going live.

**Why this question matters.** Change management in OT is fundamentally different from change management in IT, and you need to understand the local reality before you suggest any security activity that will require a change. The answer to this question tells you who has authority, what validation is required, what timelines are realistic, and what kinds of change are simply not acceptable without extensive preparation. It is also the question that most accurately predicts what the engineering team will tolerate from a security programme.

This question is the foundation of the Do No Harm checklist developed in Chapter 2. If you do not understand how change works here, you cannot design a security activity that respects it.

**Listen for.** Engineering approval gates, the role of the Management of Change process (most regulated OT environments have a formal MOC), validation or qualification requirements (especially in pharma, nuclear, food and water), factory acceptance testing and site acceptance testing for new equipment, vendor involvement and contractual constraints, the use of maintenance windows and outage schedules, who has the authority to halt a change, and how emergency changes are handled.

**Useful follow-ups.** "What is the longest a change has taken, and why?" "What is the fastest, and what made that possible?" "Who has the authority to stop a change, and when have they used it?" "What changes happen outside the normal process, and how are they controlled?"

**Where the answer goes.** This populates the Do No Harm checklist (Chapter 2), informs the maintenance window watchlist that underpins multiple detection use cases (Chapters 7, 8 and beyond), and shapes the pilot programme design for any new security tool (Chapter 13). It also feeds the RACI matrix and engineering liaison role definition in Chapter 14.

**Capture space.**

```
Change process overview:

Approval authorities:

Validation or qualification requirements:

Maintenance window cadence:

Authority to halt a change:

Emergency change handling:
```

### Question 5: Has any IT or security activity ever caused operational disruption here, or anywhere in the organisation you have heard about?

**Why this question matters.** Every experienced OT engineer has at least one story. The vulnerability scan that knocked a PLC offline. The endpoint agent that consumed CPU on an engineering workstation and caused an HMI to freeze. The network change that broke a vendor's remote support session during a critical maintenance window. The "harmless" patch that, on the third reboot, finally broke a control application that had run for eight years. The vendor consultant who connected an unauthorised device and triggered an arc flash investigation.

You need to hear these stories because they explain the wariness you are encountering. They are not paranoia. They are scar tissue from genuine harm. Acknowledging them changes the dynamic of the relationship in a way that no presentation about the threat landscape ever will.

This is also the question that most clearly demonstrates that you understand what is at stake. Ask it sincerely, listen without defensiveness, and you have begun to earn trust.

**Listen for.** Specific incidents (scan-induced controller faults, agent-related performance issues, network changes that broke OT-IT integrations), near-misses where a routine IT activity nearly caused a process upset, vendor or contractor missteps, audit activities that interfered with operations, and the changes the engineering team made to their working relationship with IT as a result.

**Useful follow-ups.** "How was it discovered, and what was the immediate impact?" "What changed afterwards, in process, tooling, or relationship?" "What would you want a new security colleague to do differently?" "Is there anything you have been asked to do, or had done to your environment, that you would not allow today?"

**Where the answer goes.** This informs every tool deployment decision (Chapter 13), every pilot design, and the Do No Harm checklist (Chapter 2). It also feeds the conflict resolution escalation path (Chapter 14), because the agreements that emerged from past incidents often define the operating constraints you will work within.

**Capture space.**

```
Incidents or near-misses described:

Tools or activities flagged as unacceptable:

Changes made to working relationship with IT or security:

Engineer's preferences for how security should engage:
```

## After the Conversation

Within twenty-four hours of the meeting, complete the following.

**Transcribe and structure your notes.** The capture sections under each question are the starting point. Add detail while the conversation is fresh. Flag any answers that surprised you or that contradict the assumptions you arrived with.

**Identify your three biggest takeaways.** From everything you heard, what are the three things that most change your understanding of this environment? These are what you will reference in your next conversation with this engineer and what you will brief your own management on.

**Map the answers to downstream artefacts.** For each question, note which Chapter and which specific artefact each answer feeds. This is how the conversation becomes operational rather than informational.

**Send a brief, sincere follow-up.** A short note thanking the engineer for their time, summarising the two or three points you found most useful, and identifying any commitments you made. Keep it short. Engineers tend to respect brevity.

**Schedule the next conversation before this one fades.** A second meeting within two weeks, focused on a specific topic the engineer raised, is one of the highest-leverage trust-building actions available to you.

## Three Things to Avoid

**Do not arrive with recommendations.** You have not earned the right yet, and the recommendations will almost certainly be wrong because they will not reflect the constraints you are about to learn.

**Do not use IT security jargon unless you are sure it will land.** "Crown jewels" is fine if you explain you mean the systems they identified as highest consequence. "Adversary tradecraft" is not. The vocabulary of MITRE ATT&CK is for your notes, not for this conversation.

**Do not promise what you cannot deliver.** Engineering teams remember commitments. If you cannot commit to coordinated maintenance windows, named engineering approval for every change in their environment, and a "no surprises" rule on detected anomalies, do not commit to them. If you can, write them down and keep them.

## What This Worksheet Produces

When used well, the five questions produce the following inputs to subsequent chapters:

| Output | Used In |
|--------|---------|
| Physical process description and consequence model | Chapter 4 (regulatory mapping), Chapter 5 (Crown Jewel Identification Worksheet), Chapter 11 (IR prioritisation) |
| Initial crown jewel candidates and engineer's hesitation list | Chapter 5 (Crown Jewel Identification Worksheet), Chapter 6 (asset register prioritisation) |
| Operational priorities and concerns of the engineering team | Chapter 2 (trust-building), Chapter 14 (joint KPIs), Chapter 4 (regulatory leverage) |
| Change management process, authorities, and validation requirements | Chapter 2 (Do No Harm checklist), Chapter 13 (pilot programme planning), Chapter 14 (RACI matrix) |
| Historical incidents and engineering team's operating preferences | Chapter 2 (Do No Harm checklist), Chapter 13 (tool selection criteria), Chapter 14 (conflict resolution) |

The conversation that produces these outputs is, in itself, the beginning of the working relationship that every subsequent chapter depends upon. The five questions are not the goal. The trust they begin to build is the goal. Treat the conversation accordingly.

## Companion Note for the SOC Practitioner

The first time you use this worksheet, you will probably not get through all five questions. The engineer will go deep on Question 2 or Question 5 and you will run out of time. That is fine. The remaining questions become the agenda for the second meeting, which the engineer will be more willing to schedule because the first one was not what they expected an IT security person to bring.

The second time you use this worksheet, with a different engineer at the same site or with a counterpart at a different site, you will hear different answers. Those differences are signal, not noise. Pay attention to what is consistent and what diverges. The consistencies tell you what is true about the organisation; the divergences tell you where local context has shaped local practice. Both inform your security programme.

The goal is not to complete the worksheet. The goal is to understand the environment well enough to defend it, and to be trusted by the people who run it. The worksheet is the beginning of a conversation that does not end.
