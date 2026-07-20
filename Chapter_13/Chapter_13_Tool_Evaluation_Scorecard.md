# Tool Evaluation Scorecard

## OT Security Tool Assessment

**Assessment Date:** _______________
**Assessor(s):** _______________
**Capability Being Assessed:** _______________
**Tier:** ☐ Tier 1 (Essential) | ☐ Tier 2 (Enhance Detection) | ☐ Tier 3 (Advanced)

---

## Candidate Tools Under Evaluation

| # | Tool Name | Vendor | Version | Licence Model |
|---|-----------|--------|---------|---------------|
| A | | | | |
| B | | | | |
| C | | | | |

---

## Criterion 1: Safety (MANDATORY — Fail = Eliminate)

*Any tool that fails the safety assessment is eliminated regardless of other scores.*

| Assessment Question | Tool A | Tool B | Tool C |
|---|---|---|---|
| Does the tool operate in passive mode by default? | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Does the tool require agents on devices at Purdue Levels 0–2? | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No |
| If agents are required, does the vendor provide explicit OT vendor compatibility certification? | ☐ Yes ☐ No ☐ N/A | ☐ Yes ☐ No ☐ N/A | ☐ Yes ☐ No ☐ N/A |
| What is the failure mode? | ☐ Fail-Open ☐ Fail-Closed ☐ Unknown | ☐ Fail-Open ☐ Fail-Closed ☐ Unknown | ☐ Fail-Open ☐ Fail-Closed ☐ Unknown |
| Does the tool inject any traffic onto OT network segments? | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Has the tool been deployed in a comparable OT environment without operational impact? | ☐ Yes ☐ No ☐ Unknown | ☐ Yes ☐ No ☐ Unknown | ☐ Yes ☐ No ☐ Unknown |
| Can the tool be deployed and removed without affecting OT operations? | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No |

**Safety Assessment Result:**

| Tool | PASS / FAIL | Notes |
|---|---|---|
| A | | |
| B | | |
| C | | |

*Tools that FAIL the safety assessment should not proceed to further evaluation.*

---

## Criterion 2: Protocol Support

*Map against protocols identified in your OT environment (from Chapter 6 asset discovery).*

| Protocol | Required? | Tool A | Tool B | Tool C |
|---|---|---|---|---|
| Modbus TCP/RTU | ☐ Yes ☐ No | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None |
| DNP3 | ☐ Yes ☐ No | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None |
| EtherNet/IP / CIP | ☐ Yes ☐ No | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None |
| OPC UA | ☐ Yes ☐ No | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None |
| OPC DA/Classic | ☐ Yes ☐ No | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None |
| Siemens S7Comm/S7Comm+ | ☐ Yes ☐ No | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None |
| Profinet | ☐ Yes ☐ No | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None |
| BACnet | ☐ Yes ☐ No | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None |
| IEC 61850 | ☐ Yes ☐ No | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None |
| IEC 60870-5-104 | ☐ Yes ☐ No | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None |
| CODESYS | ☐ Yes ☐ No | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None |
| _______________ (Other) | ☐ Yes ☐ No | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None |
| _______________ (Other) | ☐ Yes ☐ No | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None | ☐ Full ☐ Partial ☐ None |

**Protocol depth assessment (for supported protocols):**

| Depth Level | Description | Tool A | Tool B | Tool C |
|---|---|---|---|---|
| Connection-level | Source/destination/port logging | ☐ | ☐ | ☐ |
| Protocol identification | Identifies ICS protocol in use | ☐ | ☐ | ☐ |
| Function code parsing | Extracts individual commands (read/write/diagnostic) | ☐ | ☐ | ☐ |
| Register/address parsing | Extracts target register or memory addresses | ☐ | ☐ | ☐ |
| Value extraction | Extracts actual process values from protocol payloads | ☐ | ☐ | ☐ |

**Protocol Support Score (1–5):**

| Tool | Score | Justification |
|---|---|---|
| A | /5 | |
| B | /5 | |
| C | /5 | |

---

## Criterion 3: Integration

| Assessment Question | Tool A | Tool B | Tool C |
|---|---|---|---|
| Native Microsoft Sentinel data connector available? | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No |
| CEF/Syslog forwarding supported? | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No |
| REST API available for custom integration? | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Log format (JSON, CEF, Syslog, proprietary)? | | | |
| ASIM parser available or development required? | ☐ Available ☐ Dev Required | ☐ Available ☐ Dev Required | ☐ Available ☐ Dev Required |
| MITRE ATT&CK for ICS mapping provided in alerts? | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Asset data exportable to OT_AssetRegister format? | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No |
| STIX/TAXII support for threat intelligence? | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Authentication (Azure AD, SAML, API Key, Cert)? | | | |

**Integration Score (1–5):**

| Tool | Score | Justification |
|---|---|---|
| A | /5 | |
| B | /5 | |
| C | /5 | |

---

## Criterion 4: Scalability

| Assessment Question | Tool A | Tool B | Tool C |
|---|---|---|---|
| Maximum monitored asset count | | | |
| Maximum network throughput (Gbps) | | | |
| Multi-site support? | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Centralised management console? | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Cloud-managed or on-premises? | ☐ Cloud ☐ On-Prem ☐ Both | ☐ Cloud ☐ On-Prem ☐ Both | ☐ Cloud ☐ On-Prem ☐ Both |
| FTEs required to operate and maintain | | | |
| Current sites: _____ Target sites (3yr): _____ | Scales? ☐ Y ☐ N | Scales? ☐ Y ☐ N | Scales? ☐ Y ☐ N |

**Scalability Score (1–5):**

| Tool | Score | Justification |
|---|---|---|
| A | /5 | |
| B | /5 | |
| C | /5 | |

---

## Criterion 5: Vendor Support

| Assessment Question | Tool A | Tool B | Tool C |
|---|---|---|---|
| Vendor demonstrates OT environment understanding? | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Reference deployments in comparable OT environments? | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Support response time SLA | | | |
| Emergency support during plant incidents? | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Training programme available? | ☐ Yes ☐ No | ☐ Yes ☐ No | ☐ Yes ☐ No |
| Vendor financial stability / market position | ☐ Strong ☐ Moderate ☐ Concern | ☐ Strong ☐ Moderate ☐ Concern | ☐ Strong ☐ Moderate ☐ Concern |
| Product roadmap alignment with your needs? | ☐ Strong ☐ Moderate ☐ Weak | ☐ Strong ☐ Moderate ☐ Weak | ☐ Strong ☐ Moderate ☐ Weak |

**Vendor Support Score (1–5):**

| Tool | Score | Justification |
|---|---|---|
| A | /5 | |
| B | /5 | |
| C | /5 | |

---

## Criterion 6: Total Cost of Ownership (3-Year)

| Cost Component | Tool A | Tool B | Tool C |
|---|---|---|---|
| Year 1 licensing | £ | £ | £ |
| Year 2 licensing | £ | £ | £ |
| Year 3 licensing | £ | £ | £ |
| Hardware (sensors, appliances, TAPs) | £ | £ | £ |
| Professional services (deployment) | £ | £ | £ |
| Professional services (integration/ASIM) | £ | £ | £ |
| Training (initial) | £ | £ | £ |
| Training (ongoing/annual) | £ | £ | £ |
| Estimated internal FTE effort (hrs/month × rate) | £ | £ | £ |
| **3-Year Total** | **£** | **£** | **£** |

**TCO Score (1–5):** *(Lower cost relative to capability = higher score)*

| Tool | Score | Justification |
|---|---|---|
| A | /5 | |
| B | /5 | |
| C | /5 | |

---

## Summary Comparison

| Criterion | Weight | Tool A | Tool B | Tool C |
|---|---|---|---|---|
| Safety | MANDATORY | ☐ PASS ☐ FAIL | ☐ PASS ☐ FAIL | ☐ PASS ☐ FAIL |
| Protocol Support | 25% | /5 | /5 | /5 |
| Integration | 25% | /5 | /5 | /5 |
| Scalability | 15% | /5 | /5 | /5 |
| Vendor Support | 15% | /5 | /5 | /5 |
| Total Cost of Ownership | 20% | /5 | /5 | /5 |
| **Weighted Total** | **100%** | **/5** | **/5** | **/5** |

*Weights are guidance — adjust based on organisational priorities. Safety is always MANDATORY.*

---

## Recommendation

**Recommended Tool:** _______________

**Justification:**

_______________

**Conditions/Caveats:**

_______________

**Approved By:** _______________ **Date:** _______________
