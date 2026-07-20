# Regulatory Applicability Checklist for ICS/OT Environments

**Purpose:** Systematically determine which cybersecurity frameworks and regulations apply to your organisation based on sector, geography, and supply chain relationships.

**Instructions:** Work through each section with input from legal, compliance, risk management, and operations teams. Mark each framework as Applicable, Potentially Applicable, or Not Applicable. Where applicable, record the competent authority or regulator and any known compliance deadlines.

---

## Section 1: Organisation Profile

| Field | Response |
|-------|----------|
| **Organisation Name** | |
| **Primary Sector(s)** | |
| **Countries of Operation** | |
| **Number of ICS/OT Sites** | |
| **Designated as CNI Operator?** | Yes / No / Under Assessment |
| **Designated as Operator of Essential Services (OES)?** | Yes / No / Under Assessment |
| **Provides Managed Services to CNI Operators?** | Yes / No |
| **Assessment Completed By** | |
| **Date** | |

---

## Section 2: Global Frameworks (Voluntary but Strongly Recommended)

| Framework | Applicable? | Notes / Justification | Action Required |
|-----------|------------|----------------------|-----------------|
| **NIST SP 800-82r3** (OT Security Guide) | Yes / No / Partial | Applicable to any organisation operating OT systems. Recommended as baseline good practice regardless of regulatory obligation. | |
| **ISA/IEC 62443** (ICS Security Standard) | Yes / No / Partial | Applicable to any organisation operating ICS. May be contractually required by customers or regulators. Check supply chain obligations. | |
| **MITRE ATT&CK for ICS** | Yes / No / Partial | Applicable to any organisation building detection or threat intelligence capability for OT. CAF v4.0 requires intelligence-led threat hunting referencing TTPs. | |
| **NIST Cybersecurity Framework (CSF)** | Yes / No / Partial | Voluntary. Widely used as common language for risk management. SP 800-82r3 aligns to CSF structure. | |
| **IEC 61508 / IEC 61511** (Functional Safety) | Yes / No / Partial | Applicable to organisations with Safety Instrumented Systems (SIS). Defines Safety Integrity Levels (SIL). Security must not compromise safety functions. | |

---

## Section 3: European Union Regulations

| Regulation | Applicable? | Sector / Entity Classification | Competent Authority | Compliance Deadline | Notes |
|-----------|------------|-------------------------------|--------------------|--------------------|-------|
| **NIS 2 Directive** (Directive 2022/2555) | Yes / No | Essential Entity / Important Entity | | Member state transposition: Oct 2024 | Check national transposition law for specific requirements |
| **EU Cyber Resilience Act** (CRA) | Yes / No | | | Phased: 2025–2027 | Applies to manufacturers and importers of products with digital elements |
| **GDPR** (Data Protection) | Yes / No | | | Ongoing | Relevant where OT systems process personal data (e.g., access control, CCTV) |

**NIS 2 Sector Applicability Check:**

| NIS 2 Sector | Does your organisation operate in this sector? |
|--------------|-----------------------------------------------|
| Energy (electricity, oil, gas, hydrogen, district heating) | Yes / No |
| Transport (air, rail, water, road) | Yes / No |
| Banking and Financial Market Infrastructure | Yes / No |
| Health (healthcare providers, EU reference labs, pharma R&D/manufacturing) | Yes / No |
| Drinking Water | Yes / No |
| Wastewater | Yes / No |
| Digital Infrastructure (DNS, TLD, cloud, data centres, CDN, trust services) | Yes / No |
| ICT Service Management (MSPs, MSSPs) | Yes / No |
| Public Administration | Yes / No |
| Space | Yes / No |
| Postal and Courier Services | Yes / No |
| Waste Management | Yes / No |
| Manufacturing of Critical Products (medical devices, chemicals, electronics) | Yes / No |
| Food Production and Distribution | Yes / No |
| Research | Yes / No |

---

## Section 4: United Kingdom Regulations

| Regulation / Framework | Applicable? | Competent Authority | Assessment Frequency | Notes |
|-----------------------|------------|--------------------|--------------------|-------|
| **NIS Regulations 2018** (as Operator of Essential Services) | Yes / No | | | Check designation letter from competent authority |
| **NCSC Cyber Assessment Framework (CAF) v4.0** | Yes / No | | | Primary assessment framework for UK CNI. Target profile set by competent authority |
| **Cyber Security and Resilience Bill** (when enacted) | Yes / No | | Expected 2026 | Expands NIS scope to MSPs, data centres, critical suppliers |
| **PSTI Act 2022** (Product Security) | Yes / No | | In force | Relevant to OT product procurement — vendor obligations |
| **GovAssure** | Yes / No | | Annual | Applies to central government departments |

**UK CNI Sector Check:**

| UK CNI Sector | Does your organisation operate in this sector? |
|--------------|-----------------------------------------------|
| Chemicals | Yes / No |
| Civil Nuclear | Yes / No |
| Communications | Yes / No |
| Defence | Yes / No |
| Emergency Services | Yes / No |
| Energy | Yes / No |
| Finance | Yes / No |
| Food | Yes / No |
| Government | Yes / No |
| Health | Yes / No |
| Space | Yes / No |
| Transport | Yes / No |
| Water | Yes / No |

---

## Section 5: United States Regulations

| Regulation | Applicable? | Regulatory Body | Notes |
|-----------|------------|-----------------|-------|
| **NERC CIP** (Bulk Electric System) | Yes / No | NERC / FERC | Applies to owners/operators of BES assets above defined thresholds |
| **TSA Security Directives** (Pipeline) | Yes / No | TSA | Mandatory for pipeline operators. 12-hour incident reporting |
| **TSA Security Directives** (Rail) | Yes / No | TSA | Mandatory for designated freight rail and passenger rail operators |
| **TSA Security Directives** (Aviation) | Yes / No | TSA | Mandatory for designated airport and airline operators |
| **FDA 21 CFR Part 11** | Yes / No | FDA | Electronic records and signatures in pharma manufacturing |
| **CFATS** (Chemical Facility Anti-Terrorism) | Yes / No | CISA | High-risk chemical facilities |
| **NRC Regulations** (Nuclear) | Yes / No | NRC | Cybersecurity requirements for nuclear power plants |
| **AWIA** (America's Water Infrastructure Act) | Yes / No | EPA | Risk and resilience assessments for community water systems |

---

## Section 6: Supply Chain Obligations

| Question | Response | Framework Implication |
|----------|----------|---------------------|
| Do any of your customers require ISA/IEC 62443 compliance? | Yes / No | 62443-2-4 (service provider requirements) |
| Do you provide managed services to OES or CNI operators? | Yes / No | CS&R Bill scope, NIS 2 ICT service management |
| Do your contracts require specific cybersecurity standards? | Yes / No | Document contractual obligations |
| Do you supply software or firmware to OT environments? | Yes / No | PSTI Act, CRA, CAF v4.0 software security expectations |
| Do your customers require incident notification? | Yes / No | Document contractual notification timescales |

---

## Section 7: Summary and Next Steps

| Framework / Regulation | Applicable? | Priority (High/Med/Low) | Current Compliance Status | Gap Analysis Completed? | Owner |
|-----------------------|------------|------------------------|--------------------------|------------------------|-------|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

**Immediate Actions:**

1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

**Review Date:** _______________

**Approved By:** _______________

---

*This checklist accompanies Chapter 4: The Regulatory Roadmap. Use it alongside the Framework Mapping Matrix to build an integrated compliance roadmap.*
