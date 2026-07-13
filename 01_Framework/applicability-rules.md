# VISTA APPLICABILITY RULES (published, rule-based, never researcher discretion)

## why this exists
VISTA's question set is universal. But some criteria structurally cannot apply to some sectors
(a fintech has no showroom, no fuel type, no test drive). Without an N/A state those criteria
score zero and penalize business model instead of measuring visibility. Applicability is
governed HERE, by published flags, set once per assessment. A researcher never decides
per-criterion applicability on the fly.

## the flags
- PHYSICAL_LOCATION: brand has a physical location a customer can visit (showroom, store, branch, office open to the public).
- PHYSICAL_PRODUCT: brand's primary offering is a tangible product with distinct models or SKUs (vehicle, appliance, watch, camera). excludes services, SaaS, financial products, subscriptions.
- EV_PHEV: brand's products include electric or plug-in hybrid variants.
- BOOKABLE_EXPERIENCE: brand offers a bookable trial or consult experience (test drive, demo, in-showroom consult, sample fitting).

a criterion with no flag is universal and always applies.

## criterion mapping
PHYSICAL_LOCATION required (13 criteria):
SV31 SV32 SV33 SV34 SV35 SV36 SV37 (GBP setup), SV38 (local pack), SV39 (NAP),
DE09 (contact + showroom page, skipped whole per edge rule 1), DE36 (service network),
RC01 (GBP reviews), RC04 (review recency, GBP-framed).

PHYSICAL_PRODUCT required (10 criteria):
SV05 (model queries), SV24 (Product schema), SV43 (model URLs), SV50 (page per model),
DE02 (page per model), DE04 (service + maintenance), DE21 (self-educate on models),
DE22 (compare in-site), AV13 (resale Q), AV14 (servicing cost Q).

EV_PHEV required (2 criteria): AV16 (charging/range Q), DE39 (charging/maintenance guidance).

BOOKABLE_EXPERIENCE required (1 criterion): DE08 (test drive / consult booking page).

## edge rules (locked)
1. DE09 mixes universal contact with location-specific showroom. it is skipped ENTIRELY when
   PHYSICAL_LOCATION is off. the criterion is not split.
2. SV10 is universal, no flag. read "product-attribute term" generically per sector:
   fuel type for automotive, form factor for electronics, tier for phones.
3. a dimension whose criteria are ALL N/A is excluded from the composite: composite averages
   the remaining applicable dimensions. its radar axis reads "not scored, not applicable".
   any flag combination leaving FEWER THAN 4 applicable dimensions is invalid and the
   calculator blocks it at flag-selection time.
4. a sub-component whose applicable-criteria count is zero is dead: its points redistribute
   proportionally across the remaining live sub-components of that dimension so the dimension
   still totals 100.
5. AV13 and AV14 stay strictly PHYSICAL_PRODUCT. financial-services analogs (account fees,
   portfolio value) do not stretch the flag.

## renormalization math
within a sub-component: points split equally across APPLICABLE criteria only.
  criterion value = subComponentPoints / applicable_count.
dead sub-component: live sub-components scale by 100 / (sum of live sub-component points).
assertion (enforced at calculator load): under EVERY flag combination, each applicable
dimension's renormalized points sum to exactly 100.

## export + comparability
active flags embed in every assessment export (schema vista-v1.1).
percentile comparisons are only valid within the same schema version AND make most sense
within the same flag profile. see scoring-math.md.
