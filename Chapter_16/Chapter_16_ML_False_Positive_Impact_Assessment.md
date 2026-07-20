# ML False Positive Impact Assessment for OT Environments
# ================================================================
# Description: Scoring framework for evaluating the operational
#   consequence of ML false positives in OT environments. Unlike IT
#   where false positives cost analyst time, OT false positives
#   that are acted upon can cause operational disruption, safety
#   incidents, or regulatory consequences.
#
# Usage: Complete for each false positive (or representative sample)
#   during the quarterly model evaluation cycle. Feed aggregate
#   scores into the Model Evaluation Metrics template.
#
# Reference: Chapter 8 — Leveraging AI and Machine Learning
# ================================================================

## PURPOSE

In IT security, the cost of a false positive is analyst time. In OT security, the cost of a false positive that is acted upon without proper engineering validation can be operational disruption, safety compromise, or regulatory consequence. This assessment framework scores each false positive not by the fact that it occurred — all models produce false positives — but by the operational impact it *would have caused* if an analyst had taken containment action based solely on the ML alert, without proper OT engineering validation.

This scoring directly supports the critical principle that ML output must always be validated by human judgment before operational action is taken. The aggregate FP-OIS (False Positive Operational Impact Score) provides a safety-relevant metric that complements standard precision/recall measurements.

---

## ASSESSMENT RECORD

- **Model**: [Model name and version]
- **False Positive ID**: [FP-YYYY-NNN]
- **Date of Alert**: [Date/time the ML alert fired]
- **Assessed By**: [SOC analyst + OT engineer]
- **Assessment Date**: [Date this assessment was completed]

---

## SECTION 1: ALERT DETAILS

| Field | Value |
|-------|-------|
| **Alert Type** | [AssetBehaviour / ProcessAnomaly / ProtocolAnomaly] |
| **Affected Asset IP** | |
| **Affected Asset Hostname** | |
| **Crown Jewel Tier** | [Tier 1–5] |
| **Purdue Level** | [L0–L5] |
| **Anomaly Score** | [0.0–1.0] |
| **Alert Description** | [From the ML alert output] |
| **Actual Cause** | [What the investigation determined — e.g., "planned batch changeover", "seasonal ambient temperature change", "vendor firmware update"] |

---

## SECTION 2: IMPACT SCORING

Score each dimension on a scale of 0–10. The dimensions are weighted to reflect the OT security priority hierarchy: safety > operational continuity > regulatory compliance > cost.

### 2.1 Safety Impact (Weight: 3x)

*"If containment had been executed without engineering validation, what would the safety consequence have been?"*

| Score | Criteria |
|-------|----------|
| 0 | No safety impact — asset is at L3+ or not safety-related |
| 1–2 | Negligible — asset supports non-critical monitoring functions |
| 3–4 | Minor — containment would disable a non-safety alarm or monitoring point |
| 5–6 | Moderate — containment would affect a process control loop, but safety systems would compensate |
| 7–8 | Significant — containment would disable a control function that safety systems must compensate for |
| 9–10 | Critical — containment could directly affect a safety instrumented system or leave a hazardous process uncontrolled |

**Score**: _____ / 10

### 2.2 Operational Impact (Weight: 2x)

*"If containment had been executed, what would the production consequence have been?"*

| Score | Criteria |
|-------|----------|
| 0 | No operational impact — asset is non-production |
| 1–2 | Negligible — minor monitoring disruption, no production effect |
| 3–4 | Minor — reduced visibility or degraded mode, production continues |
| 5–6 | Moderate — partial production disruption or manual workaround required |
| 7–8 | Significant — production line or unit shutdown required |
| 9–10 | Critical — plant-wide shutdown or cascading failure across processes |

**Score**: _____ / 10

### 2.3 Regulatory Impact (Weight: 1x)

*"If containment had caused a disruption, would it trigger regulatory reporting or compliance consequences?"*

| Score | Criteria |
|-------|----------|
| 0 | No regulatory relevance |
| 1–3 | Internal reporting only |
| 4–6 | Regulatory notification may be required (NIS 2 24-hour reporting) |
| 7–8 | Regulatory investigation likely |
| 9–10 | Regulatory enforcement action likely (environmental release, public safety) |

**Score**: _____ / 10

### 2.4 Recovery Complexity (Weight: 1x)

*"If containment had caused a disruption, how complex would recovery have been?"*

| Score | Criteria |
|-------|----------|
| 0 | Immediate — undo containment action and normal operations resume |
| 1–3 | Simple — standard restart procedure, < 1 hour |
| 4–6 | Moderate — requires engineering intervention, 1–4 hours |
| 7–8 | Complex — multi-step recovery, 4–24 hours, potential for secondary issues |
| 9–10 | Extended — full process restart required, > 24 hours, specialist intervention |

**Score**: _____ / 10

---

## SECTION 3: COMPOSITE SCORE CALCULATION

| Dimension | Raw Score | Weight | Weighted Score |
|-----------|-----------|--------|----------------|
| Safety Impact | /10 | × 3 | /30 |
| Operational Impact | /10 | × 2 | /20 |
| Regulatory Impact | /10 | × 1 | /10 |
| Recovery Complexity | /10 | × 1 | /10 |
| **TOTAL** | | | **/70** |

### Normalised FP-OIS (0–10 scale)

**FP-OIS = Total Weighted Score / 7 = _____ / 10**

### Impact Category

| FP-OIS Range | Category | Interpretation |
|-------------|----------|----------------|
| 8.0–10.0 | **Critical** | This false positive, if acted upon, would have caused safety or catastrophic operational consequences. Model tuning is urgent. |
| 5.0–7.9 | **High** | This false positive, if acted upon, would have caused significant production disruption. Model tuning is a priority. |
| 3.0–4.9 | **Medium** | This false positive, if acted upon, would have caused moderate disruption with manageable recovery. Track trend. |
| 1.0–2.9 | **Low** | This false positive, if acted upon, would have caused minor disruption. Acceptable within normal model performance. |
| 0.0–0.9 | **Negligible** | This false positive had no meaningful operational impact potential. |

---

## SECTION 4: ROOT CAUSE AND REMEDIATION

### Why did the model generate this false positive?

- [ ] Legitimate operational change not reflected in training data
- [ ] Seasonal/environmental variation not captured by model
- [ ] Maintenance window activity not excluded
- [ ] New asset or communication path not in baseline
- [ ] Batch changeover or process transition
- [ ] Vendor remote access session
- [ ] Model drift — training data no longer representative
- [ ] Edge case in normal operations
- [ ] Unknown — requires further investigation
- [ ] Other: ________________________________

### Recommended Remediation

- [ ] No action needed — acceptable false positive
- [ ] Update OT_MaintenanceWindows watchlist process
- [ ] Add operational variation to training data and retrain
- [ ] Adjust anomaly threshold for this asset/variable
- [ ] Add exclusion rule for this specific pattern
- [ ] Retrain model with current data
- [ ] Escalate to model governance review
- [ ] Other: ________________________________

### Implementation Notes

[Document any threshold changes, exclusions, or retraining actions taken]

---

## BATCH ASSESSMENT SUMMARY

*Use this section when assessing multiple false positives in a single review cycle.*

| FP ID | Asset | Tier | FP-OIS | Category | Root Cause | Action |
|-------|-------|------|--------|----------|------------|--------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

**Aggregate FP-OIS** (mean of all FP-OIS scores): _____ / 10

**Target**: Aggregate FP-OIS ≤ 3.0

**Status**: ☐ Met ☐ Not Met
