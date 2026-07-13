# VISTA Calculator Changelog

## v1.4 -- Premium Visual Redesign (2026-07-13)

**What changed:** Full visual overhaul from the ground up. Every pixel reconsidered. The application now looks and feels like a high-budget, world-class product.

**Why:** The previous design was functional but visually generic. The data and scores are the core value of VISTA. They should be the wow factor, not an afterthought. This version makes the output something worth showing.

**Design system:**
- Dark theme throughout: background #0F1117 (deep charcoal, not flat black), cards at #161C2B and #1C2338
- Brand accent: #03AF97 (GINGO teal-green) on all active states, scores, progress fills, chart elements, and CTAs
- Full CSS variable token system: color, spacing, radius, and elevation all consistent
- Premium system font stack (-apple-system, BlinkMacSystemFont, Segoe UI, Inter)
- Styled scrollbars, green glow focus states, no default browser chrome anywhere

**Data visualization (the hero):**
- Circular SVG progress ring for the overall VISTA score: animated fill, glow filter, color-shifts by score range (red below 40, amber 40-59, green 60-79, teal 80+)
- Hexagonal SVG radar chart for all 6 dimensions: concentric grid lines, animated path drawing, semi-transparent brand green fill
- Horizontal animated bar chart for every sub-component, grouped by dimension, bars colored by score range
- Dimension score cards with thin animated progress bars and score badges

**Criterion cards:**
- Dark elevated cards with subtle border, hover state
- Criterion ID badge and tag pill in the header
- Collapsible hint with chevron toggle ("How to score this")
- All score inputs styled as pill selectors (yes/no/na, tri-state, checklist checkboxes, M-anchor 5-column grid) -- no default browser radio buttons visible
- Evidence note textarea with expand toggle, dark-styled
- N/A criteria shown at reduced opacity with informational label

**Tab navigation:**
- Sticky tab bar at the top, always visible on scroll
- Active tab highlighted with brand green underline
- Each tab shows dimension name and live completion percentage

**Summary section:**
- Two-column layout: score ring and radar chart on the left, dimension cards on the right
- Full-width sub-component bar chart below
- Styled flag/alert stack: red cards for critical issues, amber for caution, teal for informational
- Export controls styled as proper button components

**Files changed:** index.html (root, serves GitHub Pages), 03_Calculator/index.html (source)

---

## v1.3 -- English Quality Pass (2026-07-13)

**What changed:** English quality fixes across 20 specific criteria, plus a UX improvement to the brand launch year input field in the Summary and Export section.

**Why:** An editorial audit rated the corpus at 83-85%. Three categories prevented it from reaching 90%: metric acronyms left in hint text, inconsistent punctuation in "for example" phrases, and contradictory or ambiguous scoring instructions. All three categories have been resolved.

**Specific fixes:**
- SV16, SV17, SV18: Removed LCP, INP, and CLS acronyms entirely. Each hint now describes what the metric measures in plain English without naming the metric by its abbreviation.
- AV16, DE17, DE39, SC21: Fixed "For example:" (capital F, colon) to "for example," (lowercase, comma) to resolve the grammatical inconsistency in embedded examples.
- AV06: Recast the opening sentence as an instruction rather than an assertion. Added missing comma after "Also".
- AV10: Replaced "All correct = 5, the main source has significant errors = 1" with "Match to the level below" to make the scoring style consistent with the rest of the calculator.
- AV20 text field: "FAQ pages have structured data that Google can read" rewritten to "FAQ pages are marked up so that Google can display answers directly in search results". Removes the jargon term "structured data".
- BA06 evidence: "the article" corrected to "the articles".
- BA26: Fixed dangling participle. "One major unresolved story dominating the results scores 1" rewritten to "One major unresolved story that dominates the results scores 1".
- RC07: Rewritten to remove the ambiguous double negative. The scoring logic is now stated as two explicit sentences.
- RC08: Removed the contradictory instruction. The hint previously contained both a specific score ("Near-silence scores 1") and the general instruction ("Match to the level below"). The specific score has been removed.
- RC14: Fixed comma splice. "Zero mentions scores 1, regular active threads score 5" rewritten as two separate sentences.
- RC27: Reordered so the general instruction comes before the exception case, not after it.
- SC14: Clarified "More than 80% product posts scores 1" which read as if the posts scored 1 rather than the criterion. Now explicit: "A feed that is more than 80% product announcements, with almost no other content, scores 1."
- SC23: Removed "engagement rate" jargon. Rewritten to describe what the calculator computes in plain terms.
- SC27 hint and text: Clarified the conditional logic and rewritten the text label to remove "in a way that makes sense today" (too vague).
- Brand launch year input: Changed from a slow number spinner (type="number") to a plain text field with a placeholder ("e.g. 2018"), a 4-character limit, and a numeric keyboard on mobile. Label updated from "brand launch year" to "year the brand was founded" to remove ambiguity about whether it means the founding year or the age of the brand.

**Files changed:** index.html (root, serves GitHub Pages), 03_Calculator/index.html (source)

---

## v1.2 -- Plain Language Pass (2026-07-13)

**What changed:** Complete plain language rewrite across all 195 criteria. Three fields were updated on every single criterion: the short title, the instruction text, and the evidence note.

**Why:** The calculator was written in technical shorthand suited to an SEO or marketing professional. The goal is for anyone -- including someone with no prior training -- to pick it up and conduct an audit without needing to look anything up. Every piece of jargon, abbreviation, and compressed notation has been removed.

**Specific fixes:**
- All 195 criterion titles rewritten. Previous versions used shorthand like "pg1 for primary product-attribute term (fuel type / form factor / tier per sector)", "LCP <= 2.5s (PageSpeed)", "GBP exists for primary location", "NAP consistent across web". All replaced with plain, complete English sentences.
- All 195 hint instructions reviewed and rewritten. Technical terms like SERP, PSI, GBP, NAP, schema, canonical, robots.txt, backlink, denom, inverted were either removed, replaced, or explained inline with plain-language parentheticals.
- All 195 evidence notes rewritten. "SERP screenshot + date" became "screenshot of Google results with today's date". "GBP" became "screenshot of the Google Maps listing". "PSI" became "screenshot of PageSpeed results". "NAP" became "notes comparing the name, address, and phone across all 3 places".
- site: search operator instructions reworded to explain the syntax without using the abbreviation as a standalone term.
- validator.schema.org references kept as URLs (users just need to visit them) but surrounding language simplified.
- backlink references rewritten to "links from other websites pointing to the brand's site".

**Files changed:** index.html (root, serves GitHub Pages), 03_Calculator/index.html (source)

---

## v1.1 -- Plain Language Hints (2026-07-12)

**What changed:** All 195 criterion hint fields rewritten from technical shorthand to clear, step-by-step instructions.

**Why:** Hints like "Open pagespeed.web.dev, paste the homepage URL, run the test. Under the mobile tab, is LCP 2.5 seconds or less?" assumed the reader knew what PageSpeed and LCP were. Hints like "Collect 20 public mentions (forums, groups, comment threads) and code each positive, neutral, or negative" used research methodology language. All rewritten to plain instructions any first-time user can follow.

**Files changed:** index.html (root), 03_Calculator/index.html (source)

---

## v1.0 -- Initial Release

**What:** First published version of the VISTA Calculator. 195 criteria across 6 dimensions: Search Visibility (49), AI Visibility (27), Digital Experience (38), Brand Authority (26), Social and Content (28), Reputation and Community (27). Single self-contained HTML file, runs offline, no data leaves the file.
