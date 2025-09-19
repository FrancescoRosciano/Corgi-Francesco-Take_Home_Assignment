
### Technology E&O: Five‑Policy Comparison for Venture‑Backed Tech Startups

This document compares five Technology E&O + Cyber policy forms using normalized category metrics and profile scores tailored to startup risk. It is written for founders, GCs, and brokers making coverage trade‑offs across modern SaaS/product companies.

#### Policies included
- 09_Corvus - Smart Tech E&O
- 10_Embroker - Tech E&O - Cyber (with Everspan)
- 04_Beazley - MediaTech (Technology E&O + Cyber)
- 02_AXA XL - CyberRiskConnect (Technology & Cyber)
- 00_Corgi Given Policy (reference form provided by Corgi)

---

### Executive view: scores and normalized category metrics

The table shows each policy’s overall scores and normalized category values (0–1). Higher is better.

| Policy | Score (Default) | Score (B2B SaaS) | Score (Consumer) | n_core | n_coverage | n_defs_carves | n_limits | n_ops |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Corvus – Smart Tech E&O | 81.20 | 83.33 | 82.33 | 0.64 | 0.87 | 0.90 | 0.60 | 0.70 |
| Embroker – Tech E&O + Cyber (Everspan) | 77.00 | 79.17 | 78.17 | 0.60 | 0.83 | 0.80 | 0.60 | 0.60 |
| Beazley – MediaTech | 75.80 | 78.33 | 77.33 | 0.56 | 0.87 | 0.80 | 0.60 | 0.60 |
| AXA XL – CyberRiskConnect | 69.40 | 70.83 | 69.33 | 0.68 | 0.67 | 0.80 | 0.60 | 0.50 |
| Corgi Given Policy | 53.00 | 53.50 | 53.50 | 0.60 | 0.70 | 0.50 | 0.70 | 0.50 |

#### Column definitions

- **Score (Default)**: 100 × (0.30·n_core + 0.30·n_coverage + 0.20·n_defs_carves + 0.10·n_limits + 0.10·n_ops) plus additive bonuses/penalties.
- **Score (B2B SaaS)**: 100 × (0.25·n_core + 0.35·n_coverage + 0.25·n_defs_carves + 0.10·n_limits + 0.05·n_ops) plus bonuses/penalties.
- **Score (Consumer)**: 100 × (0.25·n_core + 0.35·n_coverage + 0.20·n_defs_carves + 0.10·n_limits + 0.10·n_ops) plus bonuses/penalties.
- **n_core**: Normalized 0–1 aggregate of core mechanics sub‑factors: `trigger`, `defense_costs`, `consent_settle_hammer`, `erp_tail`, `retro_date`.
- **n_coverage**: Normalized 0–1 aggregate of coverage breadth sub‑factors: `tech_prof_services`, `tech_products`, `media_ip`, `privacy_regulatory`, `business_interruption_dbi`, `pci_reputational`.
- **n_defs_carves**: Normalized 0–1 aggregate of `defs_clarity` and `carvebacks_major_exclusions` (clarity and practical carve‑backs against major exclusions).
- **n_limits**: Normalized 0–1 aggregate of `sublimits_breach_bi_reg_pci` and `retentions_alignment` (how sublimits and retentions align to realistic startup losses).
- **n_ops**: Normalized 0–1 aggregate of `panel_counsel_flex` and `notice_practicality_services` (operational usability for founders/legal ops).

Normalized categories n_* are computed as \(n_g = \frac{\sum_i \min(5, \max(0, s_i))}{5 \cdot N_g}\), where each sub‑factor score \(s_i\) is in [0,5].

##### Column definitions — deeper dive and startup implications

- **Score (Default)**: Balanced view across foundational terms and breadth. Higher suggests solid triggers/defense/settlement mechanics with broad coverage and clear carve‑backs. Good baseline when your product mixes B2B and consumer or is evolving.
- **Score (B2B SaaS)**: Over‑weights coverage and carve‑backs to reflect enterprise contracts, SLAs, and BI/vendor dependency. Prioritize for outbound B2B with MSA requirements, uptime commitments, and data processing obligations.
- **Score (Consumer)**: Restores operational usability (notice/panel) weight alongside coverage. Useful where incident response logistics, reporting practicality, and media/privacy modules affect customer trust and brand.
- **n_core**: Captures claims‑made/and‑reported trigger discipline, defense inside/outside limits, hammer, tail, and retro date. High values reduce denial risk from timing/control mechanics and minimize limits erosion.
- **n_coverage**: Measures how comprehensively the form covers tech/professional services, tech products, media/IP, privacy/regulatory, first‑party BI (incl. system failure/dependent providers), and PCI/reputational harm. High values map to fewer uninsured scenarios.
- **n_defs_carves**: Tests clarity in definitions and presence of practical carve‑backs to major exclusions (e.g., liability that exists absent contract, privacy policy breach, PCI, trade secret when tied to a breach). Higher lowers dispute risk at claim time.
- **n_limits**: Looks at whether key first‑party modules are meaningfully sublimited and whether retentions align with realistic startup losses. Higher indicates fewer surprises on payout caps and deductible friction.
- **n_ops**: Reflects panel counsel flexibility and notice/reporting practicality. Higher tends to speed the first 72‑hours response and reduce admin failure points for lean legal/ops teams.

##### Worked example: how a score is computed (Embroker, Default)

Given: n_core 0.60, n_coverage 0.83, n_defs_carves 0.80, n_limits 0.60, n_ops 0.60; BonusPenalty +6.

1) Weighted sum before bonuses:
   100 × (0.30×0.60 + 0.30×0.83 + 0.20×0.80 + 0.10×0.60 + 0.10×0.60)
   = 100 × (0.180 + 0.249 + 0.160 + 0.060 + 0.060)
   = 100 × 0.709 = 70.9

2) Add bonuses/penalties: 70.9 + 6 = 76.9 → rounded = 77.00.

Notes
- Bonus/Penalty adjustments (additive to the score) present: Corvus +5; Embroker +6; Beazley +5; AXA XL +2; Corgi −8.
- Scenario checks (not part of totals): SaaS API outage/SLA and UGC defamation both flagged as covered considerations across the higher‑ranked forms.

##### Glossary of sub‑factors (what each item means in practice)

- **trigger**: Claims‑made vs claims‑made‑and‑reported; defines reporting window sensitivity.
- **defense_costs**: Inside vs outside limits; inside erodes indemnity and is penalized more at ≤$2M towers.
- **consent_settle_hammer**: Carrier’s settlement leverage; hard 100% hammer is heavily penalized; soft 50% is moderate; consent‑only earns credit.
- **erp_tail**: Extended reporting period options for post‑policy claims (M&A, wind‑down).
- **retro_date**: How far back wrongful acts are covered; broader retro is better.
- **tech_prof_services / tech_products**: Errors/omissions in services and product failure tied to tech deliverables.
- **media_ip**: Defamation, copyright/trademark/trade dress, privacy/publicity torts (patents typically excluded).
- **privacy_regulatory**: Privacy liability plus regulatory defense/awards/fines where insurable.
- **business_interruption_dbi**: BI/extra expense; check triggers for system failure and dependent providers.
- **pci_reputational**: Card brand assessments under merchant agreements and reputational harm modules.
- **defs_clarity**: Precision of key definitions (professional/technology services, wrongful act).
- **carvebacks_major_exclusions**: Practical carve‑backs to exclusions (e.g., liability existing absent contract, breach of privacy policy, PCI, breach‑linked trade secret).
- **sublimits_breach_bi_reg_pci**: Practical caps for incident response, BI, regulatory, PCI; fewer/larger caps score better.
- **retentions_alignment**: Deductibles realistic for a startup’s balance sheet and claim profile.
- **panel_counsel_flex**: Ability to use preferred counsel or non‑mandatory panels.
- **notice_practicality_services**: Notice/reporting mechanics that fit lean teams; service access without onerous pre‑approvals.

---

### What drives the numbers (methodology in plain English)

- Normalized category values n_core, n_coverage, n_defs_carves, n_limits, n_ops
  - Each category contains several 0–5 sub‑factors (e.g., trigger, defense costs, hammer, definitions clarity, BI/dependent providers, PCI, sublimits, retentions alignment, panel/notice practicality).
  - We clamp each sub‑factor to [0,5], sum them, and scale by the category’s maximum possible (5 × number of items) to produce a 0–1 normalized value per category.

- Profile scores (Default, B2B SaaS, Consumer)
  - Scores are a weighted sum of the normalized categories, scaled to 0–100, plus additive bonus/penalty flags that reflect practical claims dynamics.
  - Weights
    - Default: core 0.30, coverage 0.30, defs_carves 0.20, limits 0.10, ops 0.10
    - B2B SaaS: core 0.25, coverage 0.35, defs_carves 0.25, limits 0.10, ops 0.05
    - Consumer: core 0.25, coverage 0.35, defs_carves 0.20, limits 0.10, ops 0.10

- Bonuses and penalties (additive to the score)
  - Defense inside limits: −10 if per‑claim limit ≤ $2M, else −5 (erosion risk at low limits).
  - Hammer clause: hard 100% −10; soft 50% −3; none/consent‑only +3 (settlement friction).
  - Incident response panel: +2 (practical first‑72‑hours support).
  - Dependent BI endorsement: +3 (cloud/vendor reliance common to startups).

These rules implement a coverage‑first lens: breadth of insuring agreements and clarity of carve‑backs/definitions move the needle most, while limits/ops fine‑tune fit for founder operations and claims control.

---

### Expert commentary and implications for tech startups

- Corvus – Smart Tech E&O (leader)
  - High coverage breadth (0.87) and excellent clarity on definitions/carve‑backs (0.90). Notable strengths include privacy‑linked trade secret carve‑back, strong pairing of third‑party and first‑party cyber, and dynamic loss‑prevention services. Balanced BI (including contingent and system failure) is attractive for SaaS dependencies.

- Embroker – Tech E&O + Cyber (Everspan)
  - Modern sublimits and endorsements (reputational harm, bricking, betterment) and robust definitions. Coverage breadth (0.83) and carve‑backs (0.80) support enterprise‑grade contracts and regulatory exposures typical of venture‑backed growth companies.

- Beazley – MediaTech
  - Mature integrated form with very strong media and cyber components. Coverage breadth (0.87) matches the leaders, with consistent contractual carve‑backs and clear definitions. A reliable market benchmark with broad third‑ and first‑party modules.

- AXA XL – CyberRiskConnect
  - Strong core mechanics (0.68) and solid definitions (0.80). Business interruption orientation tends to emphasize the insured’s own network; dependent provider and PCI nuances may require endorsements depending on the risk profile.

- Corgi Given Policy (reference)
  - Useful baseline but materially lower total scores. Sublimits and exclusions require careful review against SaaS/consumer data flows and dependency chains; expect negotiation and endorsements to reach parity with the above market leaders.

---

### How to read this for decision‑making

- For B2B SaaS with enterprise SLAs: prioritize higher coverage and carve‑back weightings (Corvus, Embroker, Beazley). Verify hammer terms and defense costs interaction with your limit tower.
- For consumer/data‑heavy apps: ensure privacy/regulatory/media modules are explicit and sublimits meet plausible incident magnitudes; look for clean definitions and practical notice/reporting.
- For cloud‑dependent architectures: confirm dependent business interruption and system failure triggers, and whether vendor panels are optional or required.

---

### Sources
- Metrics and scores are programmatically computed from normalized `output.yaml` extractions and aggregated via the scoring script in `scripts/score_policies.py`. See repo `policy_scores.csv` and the provided five‑policy CSV for exact values.
