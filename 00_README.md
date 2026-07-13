# VISTA, Visibility Intelligence & Strategic Trust Assessment
**Author:** Adhit Satish | **Version:** v1.1 | **Created:** 2026

---

## What VISTA Is
External digital brand audit. Measures online presence from the OUTSIDE IN.
What a customer sees when they research a brand. No internal access needed.
No GA4, no GSC, no CRM. Only publicly observable information.

## Core Rule
Every score = evidence a stranger can find online in approximately 2 hours.
If a customer cannot observe it, VISTA does not measure it.

## Why VISTA Is Different
Other maturity models measure INTERNAL readiness (leadership, culture, technology). They need interviews, workshops, access.
VISTA measures EXTERNAL reality. It needs nothing but a browser and public information.
Positioning: "public digital intelligence methodology" - NOT "digital maturity model".

## 6 Dimensions (Radar Chart Axes)
1. **SV** - Search Visibility (traditional SEO)
2. **AV** - AI Visibility (GEO + AEO)
3. **DE** - Digital Experience (owned website)
4. **BA** - Brand Authority (3rd party credibility)
5. **SC** - Social & Content (owned publishing)
6. **RC** - Reputation & Community (what others say)

**195 criteria total: SV 49 / AV 27 / DE 38 / BA 26 / SC 28 / RC 27**

## Scoring
- Each dimension = 0-100 points
- Composite = unweighted average of the 6 dimensions
- Sector percentile comparison (activates once enough brands are assessed in a sector)

## Maturity Bands
| Band | Range |
|------|-------|
| Invisible | 0-19 |
| Emerging | 20-39 |
| Developing | 40-59 |
| Established | 60-79 |
| Leading | 80-100 |

## Key Design Decisions (LOCKED)
- Question set 100% hardcoded and universal. No per-client question changes = no bias.
- Applicability governed by published sector rules (see `01_Framework/applicability-rules.md`), never researcher discretion. A criterion that cannot structurally apply to a sector is marked N/A by rule; its points renormalize. The question set is universal.
- Category context via FIXED published rules, not researcher discretion
- Scoring on RATIOS + consistency, never raw counts (follower count never scores directly)
- Engagement hierarchy: shares/sends > saves > comments > likes
- 3 input types: [A] auto/quick-check, [S] spot-check, [M] anchored 1-5 scale
- Pure freehand scoring BANNED
- M criteria zero-anchored: score 1 = 0 points
- No LLM calls in scoring loop. Deterministic. Same inputs = same output forever.
- No localStorage. Export/import JSON file for persistence.
- Single HTML file. No dependencies. Runs from file:// by double-click.

## Folder Map
```
00_README.md          This file
01_Framework/         Dimensions, master tables, anchor patterns, scoring math (195 criteria)
02_Benchmarks/        Cited research, thresholds, sources
03_Calculator/        index.html (the tool), verify.py, companion.py
04_Assessments/       Completed assessment exports (one JSON per brand)
05_Operations/        Technical spec, rebuild guide, decisions log, licensing strategy
```

## Deliverables - Standing Disclosures (Every Report Carries These)
- **Dark social disclosure** (mandatory, verbatim or near-verbatim): "This assessment measures publicly observable discourse only. Private channels (WhatsApp, Viber, Telegram, closed groups) are structurally unobservable from outside and are not reflected in any score, including Reputation & Community."
- **Engagement rate methodology citation** (see `01_Framework/scoring-math.md` locked ER definition) so every number is falsifiable and repeatable.
- Where the market is multilingual, state which languages were sampled for RC discourse coding.

## Attribution
VISTA methodology and instrument authored by Adhit Satish, 2026.
Attribution line embedded in tool source: `VISTA v1.1. Methodology and instrument authored by Adhit Satish.`
Copyright (c) 2026 Adhit Satish. All rights reserved. See LICENSE for terms.