```yaml
policy:
  carrier: "Beazley"
  product: "MediaTech (Technology E&O + Cyber)"
  form_code: "F00731"
  edition_date: "2019-02"
  jurisdiction: null
  source:
    link: "https://www.beazley.com/globalassets/product-documents/policy-form/beazley-media-tech-policy-us.pdf"
    citation: "§ Cover & footer F00731 022019; Declarations notice, p. 1"

coverage:
  - name: "Media, Tech, Data & Network Liability"
    scope: "Damages and Claims Expenses for Claims alleging Tech & Professional Services Wrongful Act, Tech Product Wrongful Act, Media Wrongful Act, or Data & Network Wrongful Act."
    cite: "§ Insuring Agreements — Media, Tech, Data & Network Liability, p. 1"
  - name: "Breach Response"
    scope: "Breach response costs (legal, forensics/PCI, notification, call-center, credit monitoring, PR) for actual or reasonably suspected Data/Security Breach first discovered during the Policy Period."
    cite: "§ Insuring Agreements — Breach Response; § Breach Response Costs (items 1–7), p. 1 & p. 3"
  - name: "Regulatory Defense & Penalties"
    scope: "Penalties and Claims Expenses for Regulatory Proceedings arising from a Data Breach or Security Breach."
    cite: "§ Insuring Agreements — Regulatory Defense & Penalties, p. 1"
  - name: "Payment Card Liabilities & Costs"
    scope: "PCI Fines, Expenses and Costs owed under a Merchant Services Agreement due to a Claim."
    cite: "§ Insuring Agreements — Payment Card Liabilities & Costs, p. 1"
  - name: "First Party Data & Network Loss — Business Interruption"
    scope: "Income Loss, Forensic Expenses, Extra Expense from Security Breach or System Failure after Waiting Period."
    cite: "§ Insuring Agreements — First Party Data & Network Loss (Business Interruption Loss); § Business Interruption Loss, p. 2 & p. 3–4"
  - name: "First Party Data & Network Loss — Dependent Business Interruption"
    scope: "Dependent Business Loss from Dependent Security Breach or Dependent System Failure after Waiting Period."
    cite: "§ Insuring Agreements — First Party Data & Network Loss (Dependent); § Dependent Business/Dependent Business Loss, p. 2 & p. 6–7"
  - name: "First Party Data & Network Loss — Cyber Extortion"
    scope: "Extortion payments/expenses with Underwriters’ consent responding to Extortion Threat."
    cite: "§ Insuring Agreements — Cyber Extortion Loss; § Cyber Extortion Loss/Extortion Threat, p. 2 & p. 7–8"
  - name: "First Party Data & Network Loss — Data Recovery Costs"
    scope: "Reasonable costs to regain access to, replace, or restore Data due to Security Breach/System Failure."
    cite: "§ Insuring Agreements — Data Recovery Costs; § Data Recovery Costs, p. 2 & p. 6"
  - name: "eCrime"
    scope: "Direct financial loss from Fraudulent Instruction, Funds Transfer Fraud, or Telephone Fraud first discovered during the Policy Period."
    cite: "§ Insuring Agreements — eCrime; § Fraudulent Instruction/Funds Transfer Fraud, p. 2 & p. 8–9"
  - name: "Criminal Reward"
    scope: "Criminal reward funds for information leading to arrest/conviction related to covered illegal acts."
    cite: "§ Insuring Agreements — Criminal Reward; § Criminal Reward Funds, p. 2 & p. 5"

exclusions:
  - name: "Contractual Liability"
    carve_backs: "Obligation to perform Professional or Tech Services; implied-contract misappropriation of ideas; liability the Insured would have absent the contract."
    practical_effect: "SLA/warranty failures aren’t covered unless they also amount to negligence or fit a carve-back."
    cite: "§ Exclusions — Contractual, p. 17–18"
  - name: "Patent & Misappropriation of Information"
    carve_backs: "None for patent; trade-secret exclusion tied to Tech Products/other products; limits for Data & Network Wrongful Acts."
    practical_effect: "Product-IP (patent/trade-secret) suits are largely outside coverage; rely on separate IP policy."
    cite: "§ Exclusions — Patent & Misappropriation of Information, p. 16–17"
  - name: "Infrastructure Failure (utilities/Internet not under your control)"
    carve_backs: "None; separate coverage exists for Dependent Business Interruption when caused by a Dependent Security Breach/Dependent System Failure."
    practical_effect: "Pure cloud/ISP/power outages are excluded unless they qualify as a covered dependent event."
    cite: "§ Exclusions — Infrastructure Failure, p. 18; § Dependent definitions, p. 6–7"
  - name: "Deceptive Business Practices/Antitrust/Consumer Protection"
    carve_backs: "Does not apply to Breach Response; also does not apply to Data/Security Breach coverage if no Control Group collusion."
    practical_effect: "False advertising/UDAP exposure is mostly excluded; privacy/security incidents remain covered if no insider collusion."
    cite: "§ Exclusions — Deceptive Business Practices..., p. 15"
  - name: "Governmental Actions"
    carve_backs: "Regulatory Defense & Penalties; Claims by a government entity as a customer."
    practical_effect: "General government suits are excluded except regulatory/privacy actions and customer-capacity claims."
    cite: "§ Exclusions — Governmental Actions, p. 17"
  - name: "Criminal/Intentional/Fraudulent Acts"
    carve_backs: "Defense until final non-appealable adjudication; ‘innocent insured’ protection; imputation limited to Control Group."
    practical_effect: "Coverage defends allegations but drops after adjudicated fraud; protects individuals who didn’t know/participate."
    cite: "§ Exclusions — Criminal, Intentional or Fraudulent Acts, p. 16"
  - name: "Distribution of Unsolicited Communications/Recording/Telemarketing"
    carve_backs: "Defense costs for unlawful audio/video recording allegations."
    practical_effect: "TCPA/CAN-SPAM-type risks are mostly out; limited defense carve-back for recording claims."
    cite: "§ Exclusions — Distribution of Information, p. 15"
  - name: "Trading Losses & Loss of Money"
    carve_backs: "Does not apply to eCrime insuring agreement."
    practical_effect: "Lost funds outside narrowly-defined eCrime triggers are excluded."
    cite: "§ Exclusions — Trading Losses & Loss of Money, p. 17"
  - name: "First-party physical perils & improvement costs"
    carve_backs: "None; first-party section excludes acts of God/physical events and costs to improve systems beyond pre-loss."
    practical_effect: "Cyber BI/Data recovery won’t fund upgrades or non-cyber physical events."
    cite: "§ Exclusions — First Party Data & Network Loss, p. 19"
  - name: "Retroactive Date"
    carve_backs: "None."
    practical_effect: "Acts first occurring before the Retroactive Date are excluded."
    cite: "§ Exclusions — Retroactive Date, p. 18"

limits:
  policy_limit_amount: null
  policy_limit_currency: null
  retention_each_claim: null
  sublimits:
    breach_response: null
    forensics: null
    notification: null
    public_relations: null
    business_interruption: null
    dependent_bi: null
    regulatory_fines: null
    pci: null
  territory: null
  jurisdiction: null
  cite: "§ Limit of Liability and Coverage; Retentions; Dependent BI part of BI limit, p. 19"

definitions_and_carveouts:
  professional_services:
    text: "Professional services performed for others by or on behalf of the Insured Organization for a fee; excludes certain professions (e.g., accountant, lawyer, healthcare provider, real estate/insurance agent, architect/engineer)."
    cite: "§ Definitions — Professional Services, p. 12–13"
  technology_services:
    text: "Computer/cloud/electronic technology services for others for a fee, including SaaS/PaaS/IaaS/NaaS; hosting; analysis; consulting; training; custom software; install/integration."
    cite: "§ Definitions — Tech Services, p. 14"
  wrongful_act:
    text: "Tech & Professional Services Wrongful Act includes negligent act/error/omission/misstatement/misrepresentation or unintentional breach of contractual obligation in providing Professional or Tech Services; Tech Product Wrongful Act includes negligent failure of Tech Products to perform or software copyright infringement; Data & Network Wrongful Act covers Data Breach, Security Breach, failure to disclose, or Privacy Policy Violation; Media Wrongful Act lists defamation/privacy/IP-like offenses."
    cite: "§ Definitions — Tech & Professional Services Wrongful Act; Tech Product Wrongful Act; Data & Network Wrongful Act; Media Wrongful Act, p. 10–11 & p. 14"
  other_critical_terms:
    - term: "Claims-made & reported; defense costs erode limits"
      text: "Liability insuring agreements are claims-made & reported; Claims Expenses reduce/exhaust the limit."
      cite: "§ Introductory notices, p. 1"
    - term: "Duty to defend (except PCI)"
      text: "Underwriters have the right and duty to defend covered Claims; PCI handled on an indemnity basis."
      cite: "§ Defense of Claims, p. 22"
    - term: "Hammer clause (soft 60%)"
      text: "If the Insured refuses a recommended settlement, Underwriters pay: amount of recommended settlement (less Retention) plus 60% of post-refusal Damages/Penalties/PCI amounts and 60% of post-refusal Claims Expenses."
      cite: "§ Settlement of Claims, p. 22"
    - term: "Damages include service credits"
      text: "With consent, Damages include direct net cost of future service credits offered in lieu of money."
      cite: "§ Definitions — Damages, p. 6"
    - term: "Penalties insurability"
      text: "Penalties are covered for Regulatory Proceedings; insurability per law in the venue that most favors coverage."
      cite: "§ Definitions — Penalties, p. 11"
    - term: "Additional Insured primary & non-contributory (by contract)"
      text: "Policy becomes primary & non-contributory for an Additional Insured if required by contract for liability IA Claims."
      cite: "§ Other Insurance, p. 23"

mechanics:
  trigger: "claims-made & reported"
  retroactive_date_notes: "Coverage applies to acts on/after the Retroactive Date listed in the Declarations; pre-Retroactive Date acts excluded."
  erp_tail: "Optional Extension Period available for additional premium for the period listed in the Declarations; must be purchased within 60 days of termination; does not increase limits."
  defense_costs_treatment: "Inside limits (Claims Expenses reduce/exhaust the limit)."
  consent_to_settle_text: "Refusal of recommended settlement caps Underwriters’ liability at the recommended amount (less Retention) plus 60% of further Damages/Penalties/PCI and 60% of post-refusal Claims Expenses; Underwriters may withdraw from defense."
  hammer_clause:
    type: "soft_60"
    percent: 60
    cite: "§ Settlement of Claims, p. 22"
  cite: "§ Introductory notices; § Optional Extension Period; § Defense of Claims, p. 1, 19–20, 22"

unknowns:
  - field: "limits.policy_limit_amount"
    what_was_searched: "Declarations; numbers; 'Policy Aggregate Limit of Liability' with USD values"
    not_found_note: "Specimen references Declarations but does not include dollar amounts."
  - field: "limits.policy_limit_currency"
    what_was_searched: "Declarations; 'USD', '$', currency codes"
    not_found_note: "No currency shown in specimen Declarations."
  - field: "limits.retention_each_claim"
    what_was_searched: "Declarations; 'Retention', 'Each Claim', dollar amounts"
    not_found_note: "Retentions described but actual amounts appear only in Declarations."
  - field: "limits.sublimits.*"
    what_was_searched: "Declarations; sublimit tables for breach response/forensics/notification/PR/BI/Dependent BI/regulatory/PCI"
    not_found_note: "Specimen states limits per IA but lists no specific sublimits."
  - field: "limits.territory"
    what_was_searched: "'Territory', 'Worldwide', 'Where coverage applies'"
    not_found_note: "No territory clause located."
  - field: "limits.jurisdiction"
    what_was_searched: "'Jurisdiction', 'Applicable law', 'Service of suit'"
    not_found_note: "No forum/jurisdiction clause in specimen."
  - field: "mechanics.erp_tail (duration & premium %)"
    what_was_searched: "'Optional Extension Period', 'percentage', 'months', 'years'"
    not_found_note: "Specimen says the period and % are in Declarations."
  - field: "mechanics.retroactive_date_notes (actual date)"
    what_was_searched: "Declarations; 'Retroactive Date'"
    not_found_note: "Actual date is in Declarations only."
  - field: "Waiting Period (hours)"
    what_was_searched: "'Waiting Period', 'hours', Declarations"
    not_found_note: "Definition references hours in Declarations; not stated here."
```

# Founder Summary

**Overview.** Beazley’s MediaTech is a combined Tech E\&O + Media + Cyber form with first-party (BI, extortion, data recovery), PCI, eCrime, and regulatory coverage. It is claims-made & reported and **defense costs eat into the limit**. It has a **duty to defend** and a **soft 60% hammer** if you reject a recommended settlement (§ p. 1; § p. 22).

**What’s covered (high level).**

* Tech/Professional Services, Tech Products, Media, and Data/Network wrongful acts (§ p. 1; defs p. 10–14).
* Breach response (legal, forensics/PCI, notification, call-center, monitoring, PR) (§ p. 1, 3).
* Regulatory defense & penalties for privacy/security events (§ p. 1, 11).
* PCI assessments (§ p. 1).
* First-party: cyber **business interruption**, **dependent BI** (vendors), **extortion**, **data recovery** (§ p. 2, 3–7).
* eCrime (fraudulent instruction, funds transfer fraud, telephone fraud) (§ p. 2, 8–9).
* Criminal reward (§ p. 2, 5).

**What’s excluded (founder-relevant).**

* **Contractual liability** with narrow carve-backs (SLA risk remains material) (§ p. 17–18).
* **Patent/trade-secret (product)** IP exposures (§ p. 16–17).
* **Infrastructure failure** (utilities/Internet not under your control), separate from dependent-vendor cyber events (§ p. 18; defs p. 6–7).
* **UDAP/antitrust** (privacy/security incidents still covered absent collusion) (§ p. 15).
* **Gov’t actions** (except regulatory coverage and when government is your customer) (§ p. 17).
* **Intentional fraud/crime** post-adjudication, with innocent-insured protections (§ p. 16).
* **Spam/telemarketing** (limited defense carve-back for recording) (§ p. 15).
* First-party **acts of God** and **improvement costs** (§ p. 19).

**Limits & sublimits.**

* One policy aggregate; each insuring agreement shares or has its own aggregate **as listed in the Declarations**; **defense costs erode** (§ p. 1, 19).
* **Dependent BI sits inside BI limit** (§ p. 19).
* Retentions apply per incident/related events (amounts in Declarations) (§ p. 19).
* Waiting Period hours and ERP duration/premium are set in Declarations (§ p. 15; p. 19–20).
* Numeric limits/sublimits not in specimen Declarations → unknown.

**Definitions & carve-outs that expand coverage.**

* **Tech Services** explicitly include SaaS/PaaS/IaaS/NaaS, hosting, consulting, custom dev, install/integration (§ p. 14).
* **Wrongful Acts** include unintentional **breach of contract** within Tech/Professional Services Wrongful Act (helps with some SLA disputes) (§ p. 14).
* **Damages** can include **service credits** (with consent) — helpful for SaaS remedying outages (§ p. 6).
* **Penalties** insurable where allowed by law (§ p. 11).
* **Additional Insured primary & non-contrib** when required by contract (liability IA only) — helps with enterprise deals (§ p. 23).
* **Duty to defend** (except PCI, which is indemnity) (§ p. 22).
* **Soft 60% hammer** gives more leverage if you think a settlement is unreasonable (§ p. 22).

**Pros.**

* Broad, integrated form (Tech E\&O + Media + Cyber + PCI + eCrime + first-party).
* Includes **dependent BI** for vendor outages caused by covered cyber events (good for API/SaaS dependencies).
* **Duty to defend** and Beazley’s breach response capability.
* **Service credits count as Damages** (with consent) — pragmatic for SaaS remediation.
* **Soft 60% hammer** offers negotiating room compared to hard hammers.

**Cons.**

* **Defense costs erode limits**; large investigations/litigation can burn limits fast.
* **Contractual/SLA exposure** remains; carve-backs are narrow.
* **Infrastructure failure** exclusion leaves gaps for pure utility/Internet outages not tied to a covered cyber event.
* **Product IP (patent/trade-secret)** claims are largely excluded.
* Many **specific numbers** (limits, sublimits, retentions, waiting period) live in Declarations — confirm before binding.

**Best for:** B2B/B2C **SaaS/API** companies with enterprise contracts and modern cloud stacks that need blended Tech E\&O + privacy/cyber, want vendor-dependent BI, and value a strong incident-response ecosystem.
