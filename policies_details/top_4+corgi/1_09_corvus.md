```yaml
policy:
  carrier: "Corvus Insurance (by Travelers)"
  product: "Smart Tech E&O – Technology and Professional Services Liability Coverage Endorsement"
  form_code: null
  edition_date: null
  jurisdiction: null
  source:
    link: "https://www.corvusinsurance.com/hubfs/Tech%20E-O/Corvus%20-%20Smart%20Tech%20EO%20specimen.pdf"
    citation: "§ Smart Tech E&O Coverage Endorsement, pp. 1–5"

coverage:
  - name: "Technology and Professional Services Liability"
    scope: "Pays Damages and Defense Expenses the insured is legally obligated to pay for Claims arising from a Technology and Professional Services Wrongful Act that first occurs on/after the Retroactive Date."
    cite: "§ Item 4. Third Party Insuring Agreements — F. Technology and Professional Services Liability, p. 1"

exclusions:
  - name: "Insured vs. Insured"
    carve_backs: "Employee claims outside the Control Group arising from a Privacy Breach or Security Breach are carved back."
    practical_effect: "Internal disputes are largely excluded; narrow carve-back preserves coverage for employee privacy/security breach Claims."
    cite: "§ Item 5. Insured vs Insured, pp. 1–2"
  - name: "Breach of Contract (replaced wording)"
    carve_backs: "Liability existing absent contract; breach of the insured’s privacy policy; PCI DSS Assessment Expenses; unintentional breach of a written contract to provide Technology/Professional Services or Technology Products (no coverage for hold harmless/indemnity)."
    practical_effect: "Typical SLA/warranty breach is excluded, but negligent service missteps and certain written-contract slips may be covered."
    cite: "§ Item 6. Breach of Contract (replacement), p. 2"
  - name: "Express warranties/guarantees/ROI promises"
    carve_backs: "Agreement to perform to reasonable standard of care is not excluded."
    practical_effect: "Do not promise specific outcomes, savings, or ROI; keep contracts framed around standard of care."
    cite: "§ Item 7.a (i–iii), pp. 2–3"
  - name: "Delay/failure to deliver or perform"
    carve_backs: "Carve-back if delay/failure results from a Technology Services Wrongful Act and you made diligent efforts."
    practical_effect: "Missed deadlines are excluded unless tied to a covered tech-services error and you can show diligence."
    cite: "§ Item 7.b, p. 2"
  - name: "Funds transfer & consumer protection"
    carve_backs: "None in this endorsement."
    practical_effect: "Loss/theft/transfer of funds and unfair competition/false advertising/consumer protection law violations are out under this Insuring Agreement."
    cite: "§ Item 7.i, p. 3"
  - name: "Product/service recall or rework costs"
    carve_backs: "None."
    practical_effect: "Costs to withdraw/repair/replace products or re-perform work are excluded."
    cite: "§ Item 7.l, p. 3"
  - name: "Unauthorized/surreptitious data collection or notice/consent failures"
    carve_backs: "None in this endorsement."
    practical_effect: "Allegations around stealth data collection or missing consents are excluded under this Insuring Agreement."
    cite: "§ Item 7.h, p. 3"
  - name: "Pre–Retroactive Date acts"
    carve_backs: "None."
    practical_effect: "Acts before the Retro Date are not covered; confirm Retro Date aligns with your operations history."
    cite: "§ Item 7.j, p. 3"

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
  cite: "§ Item 2. Declarations table (limits/retention placeholders) and C. Maximum Policy Aggregate Limit (placeholder), p. 1"

definitions_and_carveouts:
  professional_services:
    text: "Services performed for others for a fee; excludes certain licensed professions (e.g., accountant, architect, lawyer, etc.)."
    cite: "§ Item 9. Professional Services, p. 4"
  technology_services:
    text: "IT services for others for a fee, including systems analysis/design, hosting/SaaS/PaaS/NaaS, integration, project management, backup/processing, security consulting/training, custom dev, install/support, and network management."
    cite: "§ Item 9. Technology Services, p. 5"
  wrongful_act:
    text: "Acts/errors/omissions/neglect/misstatements or unintentional breach of duty/written contract or Privacy Injury in rendering Technology/Professional Services; failure of Technology Products to perform; limited IP (software/code/firmware marks/titles/slogans); certain defamation/privacy-related emotional distress."
    cite: "§ Item 9. Technology and Professional Services Wrongful Act (a–d), pp. 4–5"
  other_critical_terms:
    - term: "Technology Products"
      text: "Computer/telecom hardware or software (including updates/maintenance releases) created/sold/distributed by the insured for a fee."
      cite: "§ Item 9. Technology Products, p. 5"
    - term: "Privacy Injury"
      text: "Unauthorized disclosure/access to protected personal information (incl. phishing/social engineering) or failure to protect/provide required notices/consents per privacy laws."
      cite: "§ Item 9. Privacy Injury, p. 4"
    - term: "Damages — carve-outs"
      text: "Damages do not include re-performance/correction costs for services, excess liquidated damages beyond what would otherwise arise, discounts/prizes/incentives, or amounts without legal recourse."
      cite: "§ Item 8. Damages shall not include (h–k), p. 4"
    - term: "Innocent Insured"
      text: "Coverage preserved for natural-person insureds not personally involved in deliberate acts, if notice duties are met."
      cite: "§ Item 10. General Conditions — Innocent Insured, p. 5"
    - term: "Retroactive Date"
      text: "Defined as the date shown in Declarations; coverage grant requires acts on/after this date."
      cite: "§ Item 3. Retroactive Date (Declarations), p. 1; § Item 9. Retroactive date, p. 4"

mechanics:
  trigger: null
  retroactive_date_notes: "Endorsement adds a Retroactive Date in Declarations; coverage applies to acts on/after that date."
  erp_tail: null
  defense_costs_treatment: null
  consent_to_settle_text: null
  hammer_clause:
    type: null
    percent: null
    cite: null
  cite: "§ Item 3 (Retro Date), p. 1; § Item 4 (coverage requires act on/after Retro Date), p. 1"

unknowns:
  - field: "limits.policy_limit_amount"
    what_was_searched: "Declarations table; 'Limit of Liability' numeric amounts"
    not_found_note: "Only placeholders shown (e.g., $X,XXX,XXX)."
  - field: "limits.policy_limit_currency"
    what_was_searched: "Declarations; currency symbols/ISO codes"
    not_found_note: "No explicit currency stated."
  - field: "limits.retention_each_claim"
    what_was_searched: "Declarations table; 'Retention'"
    not_found_note: "Only placeholders shown."
  - field: "limits.sublimits.breach_response"
    what_was_searched: "Endorsement and Declarations for breach/response/notification/PR sublimits"
    not_found_note: "Not addressed in this endorsement."
  - field: "limits.sublimits.forensics"
    what_was_searched: "Keywords 'forensic', 'forensics', 'incident response'"
    not_found_note: "Not addressed in this endorsement."
  - field: "limits.sublimits.notification"
    what_was_searched: "Keywords 'notification', 'notify', 'credit monitoring'"
    not_found_note: "Not addressed in this endorsement."
  - field: "limits.sublimits.public_relations"
    what_was_searched: "Keywords 'public relations', 'PR', 'reputation'"
    not_found_note: "Not addressed in this endorsement."
  - field: "limits.sublimits.business_interruption"
    what_was_searched: "Keywords 'business interruption', 'system failure'"
    not_found_note: "Not addressed in this endorsement."
  - field: "limits.sublimits.dependent_bi"
    what_was_searched: "Keywords 'contingent', 'dependent', 'outage', 'provider'"
    not_found_note: "Not addressed in this endorsement."
  - field: "limits.sublimits.regulatory_fines"
    what_was_searched: "Keywords 'regulatory', 'fines', 'penalties'"
    not_found_note: "Not addressed in this endorsement."
  - field: "limits.sublimits.pci"
    what_was_searched: "Keywords 'PCI', 'DSS'"
    not_found_note: "PCI DSS referenced for carve-back only; no sublimit shown here."
  - field: "limits.territory"
    what_was_searched: "Keywords 'territory', 'territorial', 'worldwide'"
    not_found_note: "Not in this endorsement."
  - field: "limits.jurisdiction"
    what_was_searched: "Keywords 'jurisdiction', 'venue', 'choice of law'"
    not_found_note: "Not in this endorsement."
  - field: "mechanics.trigger"
    what_was_searched: "Keywords 'claims made', 'claims-made and reported'"
    not_found_note: "Trigger not stated in this endorsement."
  - field: "mechanics.defense_costs_treatment"
    what_was_searched: "Keywords 'defense costs', 'outside limits', 'erode'"
    not_found_note: "Treatment not stated in this endorsement."
  - field: "mechanics.erp_tail"
    what_was_searched: "Keywords 'extended reporting', 'ERP', 'tail'"
    not_found_note: "Not stated in this endorsement."
  - field: "mechanics.consent_to_settle_text"
    what_was_searched: "Keywords 'consent to settle', 'settle', 'hammer'"
    not_found_note: "Not in this endorsement."
  - field: "mechanics.hammer_clause"
    what_was_searched: "Keywords 'hammer', 'consent', 'settlement'"
    not_found_note: "Not in this endorsement."
```

# Founder Summary

**Overview.** This endorsement plugs Technology & Professional Services Liability into the Smart Cyber base form. It covers your negligent tech/services work (and some limited IP and privacy injuries within the *Wrongful Act* definition) but keeps tight guardrails around warranties/guarantees, delays, rework/recall, and funds-transfer/consumer-law exposures. Concrete limit numbers and key mechanics (claims trigger, defense-cost erosion, hammer clause) are not shown here and would come from the base policy. § Items 1–10, pp. 1–5.&#x20;

**What’s covered (insuring agreement).**

* Technology & Professional Services Liability for Claims arising from a *Technology and Professional Services Wrongful Act* occurring on/after the Retro Date; Damages and Defense Expenses included in the grant. § Item 4, p. 1.&#x20;

**What’s excluded (high-impact).**

* Insured vs. Insured (with carve-back for employee privacy/security breach Claims). § Item 5, pp. 1–2.&#x20;
* Contract/SLA breaches (with carve-backs for liability existing absent contract, privacy policy breach, PCI DSS assessment, and *unintentional* breach of written tech/services contracts; no indemnity/hold-harmless). § Item 6, p. 2.&#x20;
* Express warranties/guarantees/ROI promises; delay/failure to perform (narrow diligence carve-back); funds transfer & unfair competition/consumer-law claims; recall/rework costs; stealth data collection/notice-consent failures; pre-Retro acts. § Item 7 (a–l), pp. 2–3.&#x20;

**Limits & sublimits.**

* Endorsement table shows insuring agreement limit, retention, and a maximum policy aggregate, but only as placeholders—no actual numbers. § Item 2 & “Maximum Policy Aggregate Limit,” p. 1.&#x20;
* No sublimits or territory/jurisdiction terms appear here; look to base policy.

**Definitions & carve-outs (coverage expanders).**

* *Wrongful Act* is broad: negligent acts/omissions, unintentional breach of duty or written contract in rendering tech/prof services; failure of tech products; limited software-related IP; privacy-linked emotional distress. § Item 9, pp. 4–5.&#x20;
* *Professional Services* and *Technology Services* are enumerated (incl. SaaS/PaaS/NaaS, hosting, security consulting/training, custom dev, install/support, network mgmt). § Item 9, pp. 4–5.&#x20;
* *Damages* carve-outs exclude re-performance, excess liquidated damages, incentives/discounts, and amounts without legal recourse. § Item 8, p. 4.&#x20;
* *Innocent Insured* preserves coverage for uninvolved individuals despite deliberate acts by others (if notice met). § Item 10, p. 5.&#x20;

**Pros.**

* Clear, dedicated Tech/Professional Services Insuring Agreement tied to your actual services/products. § Item 4, p. 1.&#x20;
* Helpful carve-back for *unintentional* breach of written service contracts; avoids some SLA-only exclusions. § Item 6(d), p. 2.&#x20;
* Diligent-efforts carve-back for delay/failure to perform caused by a covered tech-services error. § Item 7(b), p. 2.&#x20;
* Employee privacy/security breach carve-back under Insured vs. Insured. § Item 5(A), pp. 1–2.&#x20;
* Innocent-Insured protection for individuals. § Item 10, p. 5.&#x20;

**Cons.**

* Broad exclusions for warranties/guarantees/ROI and many contractual exposures; careful contract drafting still essential. § Item 7(a), p. 2.&#x20;
* No coverage for rework/recall/replacement or missed milestone costs absent narrow carve-backs. § Item 7(l), p. 3.&#x20;
* Funds-transfer and consumer-law claims excluded under this Insuring Agreement. § Item 7(i), p. 3.&#x20;
* Key mechanics (trigger, defense-cost erosion, consent/hammer, ERP tail) and actual limits/retentions are not shown here—must be confirmed in the base policy/declarations. § Items 1–3, p. 1.&#x20;

**Best for.** B2B SaaS and IT services with standard-of-care contracts (not guarantees) that want E\&O protection integrated with cyber; good fit if you can document diligence on delivery and keep SLAs modest.
