# Crown Jewel Identification Worksheet

**Book Reference:** Chapter 5 — Defensible Architecture and Segmentation  
**Purpose:** Structured scoring framework for identifying and prioritising crown jewel processes.  
**Usage:** Complete in collaboration with OT Engineering, Plant Operations, and Safety teams. Review quarterly or after significant operational changes.

---

## Section 1: Rapid Decision Tree

Use this decision tree for initial screening. Any process answering "Yes" to Question 1 or 2 is automatically a crown jewel candidate and should proceed to full scoring.

```
START: Can this process cause physical harm to people if it malfunctions?
  ├─ YES → CROWN JEWEL CANDIDATE → Proceed to Full Scoring
  └─ NO ↓

Does this process have a Safety Instrumented System (SIS)?
  ├─ YES → CROWN JEWEL CANDIDATE → Proceed to Full Scoring
  └─ NO ↓

Would disruption of this process cause >£1M/day financial loss?
  ├─ YES → CROWN JEWEL CANDIDATE → Proceed to Full Scoring
  └─ NO ↓

Would disruption trigger mandatory regulatory reporting?
  ├─ YES → CROWN JEWEL CANDIDATE → Proceed to Full Scoring
  └─ NO ↓

Could disruption cause environmental contamination?
  ├─ YES → CROWN JEWEL CANDIDATE → Proceed to Full Scoring
  └─ NO ↓

Would disruption affect >10,000 end users/customers?
  ├─ YES → CROWN JEWEL CANDIDATE → Proceed to Full Scoring
  └─ NO → STANDARD PRIORITY → Document in asset register, monitor via zone-level controls
```

---

## Section 2: Full Scoring Framework

For each crown jewel candidate, score across four impact dimensions. Each dimension is scored 1–5.

### Scoring Scale

| Score | Impact Level | Description |
|-------|-------------|-------------|
| **5** | Catastrophic | Loss of life, major environmental disaster, existential financial loss, national-level regulatory consequence |
| **4** | Critical | Serious injury, significant environmental impact, >£5M loss, mandatory regulatory reporting and investigation |
| **3** | Major | Minor injury potential, contained environmental impact, £1M–5M loss, regulatory notification required |
| **2** | Moderate | No injury, no environmental impact, £100K–1M loss, internal audit finding |
| **1** | Minor | No safety impact, no environmental impact, <£100K loss, no regulatory implication |

### Impact Assessment

| Process / System Name | Safety Impact (1–5) | Financial Impact (1–5) | Environmental Impact (1–5) | Regulatory Impact (1–5) | **Total Score** |
|----------------------|--------------------|-----------------------|---------------------------|------------------------|----------------|
| *Example: Primary Water Treatment* | 5 | 4 | 5 | 5 | **19** |
| *Example: Packaging Line 3* | 1 | 2 | 1 | 1 | **5** |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

### Crown Jewel Tier Assignment

| Total Score | Tier | Monitoring Requirement | Segmentation Priority |
|------------|------|----------------------|----------------------|
| **16–20** | Tier 1 — Critical | Full coverage: network + endpoint + protocol analysis. All alerts critical severity. | Immediate — dedicated segment, monitored conduits |
| **11–15** | Tier 2 — High | Network monitoring + endpoint where possible. Alerts high severity. | High — prioritised in next segmentation phase |
| **6–10** | Tier 3 — Elevated | Zone-level network monitoring. Alerts medium severity. | Medium — included in segmentation roadmap |
| **1–5** | Standard | General zone monitoring. Standard alert severity. | Normal change cycle |

---

## Section 3: Crown Jewel Asset Register

For each Tier 1 and Tier 2 process, document the complete set of associated assets.

### Process: ______________________ (Tier: ___)

| Asset Name | IP Address | Purdue Level | Device Type | Function | Vendor / Model | Monitoring Status |
|-----------|------------|-------------|-------------|----------|---------------|------------------|
| | | | PLC / RTU / HMI / EWS / Historian / Other | | | Monitored / Gap |
| | | | | | | |
| | | | | | | |
| | | | | | | |

**Associated Network Segments:**
- VLAN(s): _______________
- Subnet(s): _______________
- Firewall policies: _______________

**Associated Maintenance Vendors:**
- Vendor name: _______________
- Access method: _______________
- Typical maintenance frequency: _______________

---

## Section 4: Review and Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| OT Engineering Lead | | | |
| Plant Operations Manager | | | |
| Safety Manager | | | |
| SOC Manager / Security Lead | | | |

**Review Frequency:** Quarterly, or upon significant operational change  
**Next Review Date:** _______________  
**Change Log:**

| Date | Change Description | Approved By |
|------|-------------------|-------------|
| | | |
