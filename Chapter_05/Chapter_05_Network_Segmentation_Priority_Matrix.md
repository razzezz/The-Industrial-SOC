# Network Segmentation Priority Matrix

**Book Reference:** Chapter 5 — Defensible Architecture and Segmentation  
**Purpose:** Prioritise segmentation initiatives based on risk, exposure, and feasibility.  
**Usage:** Score each segmentation initiative. Higher scores indicate higher priority.

---

## Scoring Criteria

Score each criterion 1–5. Multiply by the weight to get the weighted score.

| Criterion | Weight | Description | Scoring Guide |
|-----------|--------|-------------|---------------|
| **Crown Jewel Proximity** | x3 | Does this segmentation action protect a crown jewel attack path? | 5 = Directly on Tier 1 attack path; 4 = Directly on Tier 2; 3 = Adjacent to crown jewel; 2 = Indirectly related; 1 = No crown jewel impact |
| **Current Exposure** | x3 | How exposed is this segment currently? | 5 = Flat network, no segmentation, direct IT access; 4 = Minimal segmentation, broad firewall rules; 3 = Some segmentation, overly permissive; 2 = Reasonable segmentation, minor gaps; 1 = Well-segmented |
| **Adversary Targeting** | x2 | Is the targeted system/protocol known to be targeted by relevant threat actors? | 5 = Active campaigns against this system type in your sector; 4 = Known TTPs for this system type; 3 = General sector targeting; 2 = Theoretical risk; 1 = No known targeting |
| **Monitoring Enablement** | x2 | Will this segmentation action create new monitoring opportunities? | 5 = Creates major new detection boundary with multiple use cases; 4 = Creates new monitored conduit; 3 = Improves existing monitoring; 2 = Marginal monitoring improvement; 1 = No monitoring benefit |
| **Implementation Feasibility** | x1 | How practical is this initiative given current constraints? | 5 = No downtime, minimal change, low cost; 4 = Brief maintenance window, moderate change; 3 = Planned outage required, significant change; 2 = Extended outage, high cost/complexity; 1 = Major redesign, multi-month project |
| **Regulatory Alignment** | x1 | Does this address a specific regulatory gap or audit finding? | 5 = Addresses critical audit finding; 4 = Addresses specific regulatory requirement; 3 = Supports regulatory compliance; 2 = Indirectly supports compliance; 1 = No regulatory relevance |

---

## Segmentation Initiative Scoring

| Initiative Description | Crown Jewel Proximity (x3) | Current Exposure (x3) | Adversary Targeting (x2) | Monitoring Enablement (x2) | Feasibility (x1) | Regulatory Alignment (x1) | **Weighted Total** | **Priority** |
|----------------------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| *Example: Establish IDMZ between IT and OT* | 5 (15) | 5 (15) | 5 (10) | 5 (10) | 3 (3) | 5 (5) | **58** | **P1** |
| *Example: Isolate SIS from BPCS network* | 5 (15) | 4 (12) | 4 (8) | 4 (8) | 3 (3) | 4 (4) | **50** | **P1** |
| *Example: Segment Packaging Line from Utilities* | 2 (6) | 3 (9) | 2 (4) | 3 (6) | 4 (4) | 2 (2) | **31** | **P3** |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

---

## Priority Bands

| Weighted Score | Priority | Action Timeline |
|:---:|:---:|---|
| **46–60** | P1 — Critical | Immediate action. Include in next change window. |
| **31–45** | P2 — High | Plan within current quarter. |
| **16–30** | P3 — Medium | Include in next planning cycle (6–12 months). |
| **1–15** | P4 — Low | Document and address opportunistically. |

---

## Implementation Tracking

| Initiative | Priority | Target Date | Assigned To | Status | Completion Date | Notes |
|-----------|:---:|---|---|---|---|---|
| | | | | Not Started / In Progress / Complete / Deferred | | |
| | | | | | | |
| | | | | | | |
