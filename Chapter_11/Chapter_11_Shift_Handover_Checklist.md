# OT SOC Shift Handover Checklist
# ================================================================
# Description: Structured checklist ensuring every OT-relevant
#   element is covered during SOC shift transitions. Extends
#   standard IT SOC handover with OT-specific operational context.
#
# Usage: Complete at every shift change. Both outgoing and incoming
#   shift leads sign off. Archive in SOC log. Handover should take
#   15–20 minutes maximum.
#
# Reference: Chapter 11 — Purpose-Built Incident Response
# ================================================================

---

## Handover Details

| Field | Value |
|-------|-------|
| **Date** | |
| **Outgoing Shift** | [Shift ID / Lead Name] |
| **Incoming Shift** | [Shift ID / Lead Name] |
| **Handover Time** | |

---

## 1. Active OT Incidents

| Incident ID | Severity | Asset(s) Affected | Purdue Level | Crown Jewel Tier | Engineering Engaged? | Status | Pending Actions |
|-------------|----------|-------------------|-------------|-----------------|---------------------|--------|----------------|
| | | | | | | | |
| | | | | | | | |

**Key details for active incidents:**
- [ ] Operational context communicated (which process, what's the impact)
- [ ] Containment decisions pending or in progress
- [ ] Engineering team engagement status (who, when last contacted)
- [ ] Expected next steps and timeline

---

## 2. Active and Upcoming Maintenance Windows

| Maintenance ID | Description | Affected Assets | Purdue Level | Start (UTC) | End (UTC) | Engineer | Status |
|---------------|-------------|-----------------|-------------|-------------|-----------|----------|--------|
| | | | | | | | |
| | | | | | | | |

**Key details:**
- [ ] Active maintenance windows reviewed — incoming shift aware of expected activity
- [ ] Upcoming maintenance windows in next 12 hours identified
- [ ] Maintenance window closures in next 12 hours identified (alerts may change from "expected" to "suspicious")

---

## 3. Known Operational Changes

- [ ] Process changes affecting normal traffic patterns: [Details or "None"]
- [ ] Commissioning activities in progress: [Details or "None"]
- [ ] Firmware upgrades or control logic modifications planned: [Details or "None"]
- [ ] New devices or systems recently connected: [Details or "None"]
- [ ] Any operational anomalies reported by plant operations: [Details or "None"]

---

## 4. Threat Intelligence Updates

- [ ] New advisories relevant to our sector: [Advisory IDs or "None"]
- [ ] Threat actor updates (Volt Typhoon, Seashell Blizzard, etc.): [Summary or "None"]
- [ ] Active hunting hypotheses in progress: [Hypothesis IDs or "None"]
- [ ] New IOCs ingested requiring monitoring: [Details or "None"]
- [ ] ISAC alerts received: [Summary or "None"]

---

## 5. Detection and Monitoring Status

- [ ] All data sources reporting normally: [Yes / Issues noted below]
- [ ] Zeek/Suricata sensors operational: [Yes / Issues]
- [ ] EDR agents reporting on OT workstations: [Yes / Issues]
- [ ] SIEM ingestion healthy — no data gaps: [Yes / Issues]
- [ ] Any detection rules recently deployed or modified: [Details or "None"]
- [ ] Any detection rules in tuning phase generating expected false positives: [Details or "None"]

**Data Source Issues:**
| Source | Issue | Impact | Action Taken |
|--------|-------|--------|-------------|
| | | | |

---

## 6. Open Investigations (Non-Incident)

| Investigation | Source | Priority | Status | Assigned To |
|--------------|--------|----------|--------|-------------|
| | | | | |

---

## 7. Upcoming Activities

- [ ] Scheduled tabletop exercises: [Date/Details or "None"]
- [ ] Planned detection rule deployments: [Details or "None"]
- [ ] Scheduled threat hunts: [Details or "None"]
- [ ] Vendor visits or remote access sessions: [Details or "None"]
- [ ] Regulatory audits or assessments: [Details or "None"]

---

## 8. Any Other Business

[Free text for anything not covered above]

---

## Sign-Off

| Role | Name | Signature | Time |
|------|------|-----------|------|
| **Outgoing Shift Lead** | | | |
| **Incoming Shift Lead** | | | |
