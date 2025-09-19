```yaml
policy:
  carrier: "CFC Underwriting Limited"
  product: "Technology"
  form_code: "Technology v4.1"
  edition_date: null
  jurisdiction: null
  source:
    link: "/mnt/data/policy-specimen.pdf"
    citation: "§ Preamble/footer 'Technology v4.1'; Declarations referenced throughout :contentReference[oaicite:0]{index=0}"

coverage:
  - name: "Professional Liability — Products & Services"
    scope: "Claims-made cover for negligence, implied-term breach (care/skill; quality/fitness), product failure to perform, BI/PD arising from tech services, and any other civil liability not otherwise excluded."
    cite: "§ Insuring Clause 1, Section A, p. 1–2 :contentReference[oaicite:1]{index=1}"
  - name: "Professional Liability — Breach of Contract (Unintentional)"
    scope: "Unintentional breach of a client contract for provision of technology services."
    cite: "§ Insuring Clause 1, Section B, p. 2 :contentReference[oaicite:2]{index=2}"
  - name: "Professional Liability — Sub-contractor Vicarious Liability"
    scope: "Acts, errors or omissions of sub-contractors engaged to provide your technology services."
    cite: "§ Insuring Clause 1, Section C, p. 2 :contentReference[oaicite:3]{index=3}"
  - name: "IP & Media Liability (incl. privacy/publicity)"
    scope: "IP rights infringement (non-patent), passing off/plagiarism, trade secret misappropriation, privacy/publicity offenses, breach of confidentiality, defamation and related torts, all arising from technology services."
    cite: "§ Insuring Clause 1, Section D, p. 2–3; Definitions 27 'Intellectual property rights', p. 17 :contentReference[oaicite:4]{index=4}"
  - name: "Regulatory Costs & Fines (Tech Services)"
    scope: "Costs, expenses, and insurable fines/penalties from a regulatory investigation that solely affects the insured and arises directly out of tech services."
    cite: "§ Insuring Clause 1, Section E, p. 3; Exclusion 63 'Uninsurable fines', p. 31 :contentReference[oaicite:5]{index=5}"
  - name: "Dishonesty of Employees"
    scope: "Claims from employee dishonesty in provision of technology services."
    cite: "§ Insuring Clause 1, Section F, p. 3 :contentReference[oaicite:6]{index=6}"
  - name: "Payment of Withheld Fees"
    scope: "Reimburses withheld client fees to defuse a larger covered claim under IC1 A/B/C/F, with client’s no-claim confirmation."
    cite: "§ Insuring Clause 1, Section G, p. 3 :contentReference[oaicite:7]{index=7}"
  - name: "Network Security Liability"
    scope: "Liability from cyber events (malware transmission, DoS, unauthorized access/failure to prevent, identity theft) first discovered during policy period."
    cite: "§ Insuring Clause 2, Section A, p. 3–4; Definition 14 'Cyber event', p. 15–16 :contentReference[oaicite:8]{index=8}"
  - name: "Privacy Liability"
    scope: "Liability from privacy breaches (PII/PHI, notice failures, NDA breaches, privacy policy breaches; includes your data or data you’re responsible for)."
    cite: "§ Insuring Clause 2, Section B, p. 4; Definitions 37 'Privacy breach', p. 17 :contentReference[oaicite:9]{index=9}"
  - name: "Management Liability (Cyber Event)"
    scope: "Personal liability of senior executive officers arising out of a cyber event (excess of any other insurance)."
    cite: "§ Insuring Clause 2, Section C, p. 4 :contentReference[oaicite:10]{index=10}"
  - name: "Regulatory Investigation Costs (Cyber)"
    scope: "Fines/penalties and costs from regulatory investigations arising directly out of a cyber event."
    cite: "§ Insuring Clause 2, Section D, p. 4–5 :contentReference[oaicite:11]{index=11}"
  - name: "PCI Fines, Penalties & Assessments"
    scope: "Card brand assessments, fraud recoveries, reimbursements, case management fees after a payment card breach."
    cite: "§ Insuring Clause 2, Section E, p. 5; Definition 31 'Payment card breach', p. 16–17 :contentReference[oaicite:12]{index=12}"
  - name: "Cyber Incident Response Costs"
    scope: "24/7 hotline, incident manager, initial legal/notification, IT forensics, crisis comms, breach management for you (and for a third party you’ve indemnified), and post-breach remediation."
    cite: "§ Insuring Clause 3, Sections A–G, p. 5–7 :contentReference[oaicite:13]{index=13}"
  - name: "Cyber Crime"
    scope: "Electronic theft of your funds, third-party escrow funds, execs’ personal funds (from company network compromise/ID theft), cyber extortion (incl. ransomware), telephone hacking, push-payment fraud, and unauthorized compute use."
    cite: "§ Insuring Clause 4, Sections A–G, p. 7–8 :contentReference[oaicite:14]{index=14}"
  - name: "System Damage & Business Interruption"
    scope: "Data rebuild, forensics, system rectification; income loss/extra expense from cyber event or system failure; additional extra expense; dependent business interruption from supply-chain partner downtime; reputational harm income loss; claim prep costs; hardware replacement if firmware/software rendered unusable."
    cite: "§ Insuring Clause 5, Sections A–G, p. 8–10; Definitions 46–48 'Supply chain partner'/'System failure'/'Technology error', p. 19–20 :contentReference[oaicite:15]{index=15}"
  - name: "Commercial General Liability (CGL)"
    scope: "Occurrence-based BI/PD (except when caused directly by tech services), personal & advertising injury, products/completed ops, sudden & accidental pollution, tenants’ legal liability, medical expenses (no-fault), employee benefits liability (claims-made), hired/non-owned auto, and damage to hired/leased autos."
    cite: "§ Insuring Clause 6, Sections A–I, p. 10–11 :contentReference[oaicite:16]{index=16}"
  - name: "Loss Mitigation (Rectification)"
    scope: "Pre-claim costs (with prior consent) to rectify acts/errors/omissions under IC1 where cheaper than the expected claim."
    cite: "§ Insuring Clause 7, p. 11–12 :contentReference[oaicite:17]{index=17}"
  - name: "Reputation & Brand Protection"
    scope: "PR consultancy to mitigate brand damage tied to a covered claim."
    cite: "§ Insuring Clause 8, p. 12 :contentReference[oaicite:18]{index=18}"
  - name: "Court Attendance Costs"
    scope: "Reasonable sums to attend proceedings connected to a covered claim."
    cite: "§ Insuring Clause 9, p. 12 :contentReference[oaicite:19]{index=19}"

exclusions:
  - name: "Contractual Liability"
    carve_backs: "Carved back for IC1 (A, B, D) and IC6 where liability would attach absent the contract."
    practical_effect: "Pure SLA/liquidated-damages exposure is limited; ensure your claims fit the carve-backs."
    cite: "§ Exclusion 23, p. 25; Exclusion 39 on liquidated damages/service credits, p. 26–27; IC1 A/B/D grants, p. 1–3 :contentReference[oaicite:20]{index=20}"
  - name: "Liquidated Damages / Service Credits / Penalty Clauses"
    carve_backs: "Covered only if you’d be liable even without the clause."
    practical_effect: "Common uptime credits/penalties in SaaS MSAs may not be covered."
    cite: "§ Exclusion 39, p. 26–27 :contentReference[oaicite:21]{index=21}"
  - name: "Intellectual Property & Defamation (general)"
    carve_backs: "Carved back under IC1 Section D and IC6 Section B."
    practical_effect: "Rely on specific IP/media grants; patent infringement remains excluded."
    cite: "§ Exclusion 35, p. 26; IC1 D, p. 2–3; IC6 B, p. 10–11; Patent exclusion 44, p. 28 :contentReference[oaicite:22]{index=22}"
  - name: "Known Claims/Circumstances"
    carve_backs: "None (except continuous cover condition for certain late-notified incidents with same insurer)."
    practical_effect: "Pre-existing issues before continuity date are out."
    cite: "§ Exclusion 37, p. 25–26; Condition 7 'Continuous cover', p. 34–35 :contentReference[oaicite:23]{index=23}"
  - name: "Power & Utility Failure"
    carve_backs: "None (applies to IC2–IC5)."
    practical_effect: "Grid/ISP outages are excluded; consider true Dependent BI via named supply-chain partner/system failure."
    cite: "§ Exclusion 49, p. 28–29; IC5 D (Dependent BI), p. 9 :contentReference[oaicite:24]{index=24}"
  - name: "Core Internet Infrastructure Failure"
    carve_backs: "None (applies to IC2–IC5)."
    practical_effect: "Widespread internet/DNS/GPS outages aren’t covered."
    cite: "§ Exclusion 26, p. 25 :contentReference[oaicite:25]{index=25}"
  - name: "Privacy Statutes — Unsolicited Communications (TCPA/CAN-SPAM)"
    carve_backs: "Does not apply to IC2(A) network security liability only."
    practical_effect: "Spam/robocall suits generally excluded."
    cite: "§ Exclusion 66 and carve-back, p. 31–32 :contentReference[oaicite:26]{index=26}"
  - name: "Bodily Injury / Property Damage (BI/PD) for E&O/Cyber"
    carve_backs: "Carved back for IC1(A) and specific mental injury under IC1(D), IC2(A–C)."
    practical_effect: "Most BI/PD belongs under CGL; limited BI/PD carve-backs in tech E&O/media/cyber contexts."
    cite: "§ Exclusion 22, p. 24–25; IC6 CGL grants, p. 10–11 :contentReference[oaicite:27]{index=27}"
  - name: "Property Damage (E&O/Cyber)"
    carve_backs: "Carved back for IC1(A)."
    practical_effect: "Physical property damage tied to cyber/E&O is mostly excluded."
    cite: "§ Exclusion 52, p. 29; IC1 A, p. 1–2 :contentReference[oaicite:28]{index=28}"
  - name: "Payment Card Assessments (general)"
    carve_backs: "Carved back under PCI Insuring Clause 2(E)."
    practical_effect: "PCI exposures require the specific PCI clause to respond."
    cite: "§ Exclusion 45, p. 28; IC2 E, p. 5 :contentReference[oaicite:29]{index=29}"
  - name: "Directors & Officers Liability"
    carve_backs: "Carved back for cyber-event D&O (IC2 C)."
    practical_effect: "Corporate governance/D&O claims aren’t covered under this—only the cyber carve-back."
    cite: "§ Exclusion 28, p. 26; IC2 C, p. 4 :contentReference[oaicite:30]{index=30}"
  - name: "War / Cyber War"
    carve_backs: "Cyber war carve-back for certain incident-response and for systems physically outside an impacted state."
    practical_effect: "State-sponsored events may be constrained; some limited carve-backs remain."
    cite: "§ Exclusion 67, p. 32; Definitions 17/23 'Cyber war/Impacted state', p. 16, 17–18 :contentReference[oaicite:31]{index=31}"
  - name: "Retroactive Date"
    carve_backs: "Not a carve-back; a condition—acts on/before retro date are excluded for IC1 and IC6(G)."
    practical_effect: "Mind the retro date when switching carriers."
    cite: "§ Exclusion 56, p. 30; Definition 42 'Retroactive date', p. 18–19 :contentReference[oaicite:32]{index=32}"

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
  cite: "§ How Much We Will Pay; Your Deductible, p. 12–13; 21 'Choice of law/jurisdiction...', p. 39–40; legal action territories via Declarations, Exclusion 38, p. 25–26 :contentReference[oaicite:33]{index=33}"

definitions_and_carveouts:
  professional_services:
    text: null
    cite: null
  technology_services:
    text: "Supply by you (or on your behalf) of technology products or services incl. software dev/maintenance, hardware design/maintenance, data processing, hosting, systems analysis/integration, consulting, training, programming, IT support, network management; further described in Declarations."
    cite: "§ Definition 50 'Technology services', p. 20 :contentReference[oaicite:34]{index=34}"
  wrongful_act:
    text: null
    cite: null
  other_critical_terms:
    - term: "Cyber event"
      text: "Unauthorized access/electronic attack (DoS, malware/ransomware, hacking, phishing, etc.) or privacy breach; excludes technology error."
      cite: "§ Definition 14, p. 15–16 :contentReference[oaicite:35]{index=35}"
    - term: "System failure"
      text: "Sudden, unexpected and continuous outage of your (or supply-chain partner’s) systems due to app bug/network/hardware failure; excludes cyber event."
      cite: "§ Definition 47, p. 19–20 :contentReference[oaicite:36]{index=36}"
    - term: "Dependent Business Interruption"
      text: "Income loss/extra expense from downtime of a supply-chain partner’s systems due to cyber event or system failure beyond a waiting period."
      cite: "§ Insuring Clause 5, Section D, p. 9; Definitions 46–47, p. 19–20 :contentReference[oaicite:37]{index=37}"
    - term: "Additional insured — primary & non-contributory"
      text: "If contractually required and sole negligence is yours, third party may be treated as additional insured; policy can be primary & non-contributory."
      cite: "§ Condition 2, p. 32–33 :contentReference[oaicite:38]{index=38}"
    - term: "Loss Mitigation (rectification)"
      text: "Pre-claim rectification costs reimbursable when cheaper than expected claim; excludes salaries/profit/normal opex/goodwill payments."
      cite: "§ Insuring Clause 7, p. 11–12 :contentReference[oaicite:39]{index=39}"

mechanics:
  trigger: "Mixed: claims-made for IC1 & IC6(G); discovery-based (first discovered) for IC2–IC5; occurrence for most CGL grants."
  retroactive_date_notes: "Retroactive date applies to IC1 and IC6(G); acts on/before retro date excluded."
  erp_tail: "Automatic 60-day ERP; optional ERP available for duration shown in Declarations (purchase within 30 days)."
  defense_costs_treatment: null
  consent_to_settle_text: "Insurer won’t settle without your consent; if you refuse a recommended settlement, future costs are split 50/50 and indemnity capped at the recommended amount."
  hammer_clause:
    type: "soft_50"
    percent: 50
    cite: "§ Condition 3 'Agreement to pay claims (duty to defend)', p. 33–34 :contentReference[oaicite:40]{index=40}"
  cite: "§ Preamble 'Coverage triggers'; Insuring Clause cites above; Condition 1 (notice & 72-hour self-help for cyber), p. 32–33; Condition 11–12 (ERP), p. 36–37; How Much We Will Pay, p. 12–13 :contentReference[oaicite:41]{index=41}"

unknowns:
  - field: "policy_limit_amount / policy_limit_currency"
    what_was_searched: "Declarations; 'limit of liability'; currency symbols"
    not_found_note: "Amounts are only set on the Declarations, which are not included in the specimen excerpt."
  - field: "retention_each_claim"
    what_was_searched: "Declarations; 'deductible'"
    not_found_note: "Specific deductible is Declarations-driven; specimen provides mechanics only."
  - field: "sublimits (breach response/forensics/notification/PR/BI/dependent BI/regulatory fines/PCI)"
    what_was_searched: "Declarations; 'sublimit'; section-specific caps; PCI schedule"
    not_found_note: "All sublimits are Declarations-set; not present in the wording text provided."
  - field: "territory & jurisdiction for claims"
    what_was_searched: "Exclusion 38 'Legal action territories'; Declarations"
    not_found_note: "Legal action territories and choice of law depend on Declarations."
  - field: "defense_costs_treatment (inside vs outside limits)"
    what_was_searched: "How Much We Will Pay; Declarations; 'costs and expenses in addition to the limit'"
    not_found_note: "Form allows either inclusive or in-addition; the Declarations control this."
  - field: "edition_date"
    what_was_searched: "Footer/version; publication date"
    not_found_note: "Version shows 'Technology v4.1' and ©1999–2024, but no specific edition date."
  - field: "definition — Professional services"
    what_was_searched: "Definitions; 'professional services'"
    not_found_note: "The form uses 'technology services' as the operative defined term; no separate 'professional services' definition found."
  - field: "definition — Wrongful act"
    what_was_searched: "Definitions; 'wrongful act'"
    not_found_note: "No standalone 'wrongful act' definition; IC1 enumerates covered acts/errors/omissions instead."
  - field: "waiting period / indemnity period values"
    what_was_searched: "Definitions 26/52; Declarations"
    not_found_note: "Mechanics defined, but hour/day values are set in the Declarations."
```

# Founder Summary

This CFC “Technology” policy is a broad combined Tech E\&O + Cyber + Incident Response + Crime + System BI + CGL wording. It covers the usual E\&O mistakes in your tech services, privacy/network liabilities from cyber events, PCI assessments, incident-response costs, cybercrime, and both your own and dependent business interruption — with a classic soft-hammer consent provision and duty-to-defend. Specific limits, sublimits, deductibles, and legal territories come from the Declarations (not included here).&#x20;

**What’s covered (high level)**

* Tech E\&O: negligence, implied-term breach, product non-performance, sub-contractor vicarious, employee dishonesty, certain regulatory costs/fines, IP/media offenses tied to your services, and an option to pay withheld fees to avoid a larger claim (IC1).&#x20;
* Cyber & privacy liability, PCI, incident response (legal/forensics/PR/notifications), post-breach remediation (IC2–IC3).&#x20;
* Cybercrime (funds transfer scams, ransomware/extortion, phone hacking, push-payment fraud, cryptojacking) (IC4).&#x20;
* System damage & BI, incl. Dependent BI from supply-chain partner outages (cyber event or system failure), reputational harm, hardware replacement (IC5).&#x20;
* CGL (occurrence-based BI/PD, P\&A injury, products/completed ops, tenants’, hired/non-owned auto, EBL) (IC6).&#x20;

**What’s excluded (notable, with carve-backs)**

* Contractual liability & SLA credits/penalties, except where liability would exist anyway and IC1 A/B/D carve-backs apply (penalty/credit exposure limited).&#x20;
* Patent infringement (still excluded); other IP/defamation are granted only under specific sections (IC1 D, IC6 B).&#x20;
* Known claims/circumstances before the continuity date.&#x20;
* Utility/grid & core internet infrastructure failure (affects cyber/BI).&#x20;
* TCPA/CAN-SPAM suits (spam/robocalls) except limited carve-back for network security liability (IC2 A).&#x20;

**Limits & sublimits**

* One overall limit applies where multiple Sections respond; only the highest relevant Section limit is available, others sit within it. Deductibles apply once per “single source/event” as defined. Exact amounts, sublimits (IR/forensics/BI/Dependent BI/PCI/etc.), and currency are set on the Declarations and aren’t in the specimen text provided.&#x20;

**Definitions & carve-outs that expand coverage**

* “Technology services” is broad (software, hardware, hosting, integration, consulting, support, network mgmt.).&#x20;
* “Cyber event” vs “System failure” separation allows BI from non-malicious outages (bugs/hardware).&#x20;
* Dependent BI includes third-party supply-chain partners’ systems (if listed/qualifying).&#x20;
* Additional insured status can be primary & non-contrib if your contract requires it.&#x20;

**Pros**

* Broad Tech E\&O + Cyber + Crime + BI + CGL in one form; strong incident-response ecosystem.&#x20;
* Explicit Dependent BI and System Failure coverage (not just malicious cyber) — valuable for SaaS/API reliance.&#x20;
* Duty-to-defend and soft 50% hammer give settlement leverage without a punitive penalty.&#x20;
* PCI assessments specifically granted (rare on some forms).&#x20;

**Cons**

* SLA liquidated-damages/service-credit/penalty exposure is constrained; coverage hinges on “liability absent the clause.”&#x20;
* Utilities/core internet outages excluded — potential BI gap for widespread events.&#x20;
* Patent infringement excluded — IP-heavy products may need separate IP cover.&#x20;
* Critical details (limits, sublimits, defense-costs outside vs inside limits, territories) live on the Declarations; cannot be confirmed here.&#x20;

**Best for:** B2B/B2C SaaS and API/infra startups with third-party dependencies that need integrated E\&O + cyber (incl. PCI) and meaningful dependent-BI protection, and that can manage SLA penalty constructs in contracts.&#x20;
