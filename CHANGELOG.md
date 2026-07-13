# VISTA Calculator Changelog

## V.02.02.01 -- Summary Unified Box (2026-07-13)

**What changed:** Replaced the three separate floating cards in the summary (score ring, radar, dimension scores) with a single unified container. All three sections now sit inside one card with thin vertical dividers between them. No individual card backgrounds, borders, or border radii on the sections themselves. The atmospheric glow behind the score ring is hidden in this context (it was designed for a full-width hero, not a narrow column). The dimension score card names now wrap instead of truncating with an ellipsis. The radar SVG scales responsively via CSS max-width so it does not overflow its column. Responsive: stacks vertically below 960px with horizontal dividers between sections.

**Files changed:** index.html (root, serves GitHub Pages), 03_Calculator/index.html (source)

---

## V.02.02.00 -- Input UX + Summary Layout (2026-07-13)

**What changed:** Three UX fixes to eliminate input friction and reduce wasted space in the Summary.

Social media number inputs: All follower count and post metric fields (shares, saves, comments, likes for 10 posts across Instagram, Facebook, and the primary platform) previously re-rendered the page on every keystroke, scrolling the user back to the top mid-entry. All social inputs now use `onchange` (fires on blur or Enter), so the user can type a full number without any interruption.

Year founded field: Previously accepted any text and re-rendered on every character, causing the page to scroll up after each digit. Now digits-only (non-numeric characters are stripped in place without triggering a re-render), and the re-render only fires when the field loses focus. All other metadata fields (brand name, country, sector, assessment date) also switched to `onchange` for the same reason.

Summary layout: The hero score ring and the data grid (radar chart and six dimension stat cards) now sit side by side in a flex row instead of stacking vertically. The hero (300px ring, band label, subtitle) occupies a fixed 380px left column. The data grid fills the remaining width. This removes a full page of vertical scroll and keeps the score reveal and dimension detail visible together. Responsive: stacks to a single column below 1100px.

**Files changed:** index.html (root, serves GitHub Pages), 03_Calculator/index.html (source)

---

## V.02.01.00 -- UX Polish + Bug Fixes (2026-07-13)

**What changed:** Five targeted fixes to the input and navigation experience.

Header legibility: The subtitle text and status indicator were using a near-invisible muted color on the dark background. Both now use a readable mid-gray.

Sidebar rail: Compressed the score ring (200px to 140px) and radar chart (290px to 200px), and tightened padding, so the full rail -- ring, band label, radar, and dimension legend -- fits in one viewport column without scrolling.

Fixed bottom bar: The score and Confirm Section button are now pinned to the bottom of the screen at all times during input, so the user never has to scroll to find it. Clears the rail on the right. Restores to static position for print/PDF.

Auto-advance on confirm: Clicking Confirm Section now automatically moves to the next dimension tab. After the last dimension (Reputation), it advances to the Summary tab.

Bug fix -- sponsorable criteria pre-select: All sponsorable criteria (absent/sponsored/earned inputs) were visually showing "absent" as pre-selected on unanswered questions due to a fallback in the render logic. This gave the false impression that answers had been entered. Fixed: no button is highlighted until the user makes an explicit choice.

**Files changed:** index.html (root, serves GitHub Pages), 03_Calculator/index.html (source)

---

## V.02.00.00 -- Cinematic Summary Redesign (2026-07-13)

**What changed:** Complete overhaul of the Summary tab and a new version numbering system. The Summary is now a cinematic, full-bleed dashboard experience, not a form with a score tucked to the side.

**Why:** The previous design, while functional, looked like a developer had put dark mode on a form. The score ring was buried in a sidebar. The radar chart was undersized. The data, which is the entire point of the tool, was not given the visual weight it deserves. This version makes opening the Summary tab feel like a reveal moment.

**Versioning format introduced:** V.MM.mm.pp -- first block for major/huge changes, second for mid-level, third for minor patches. This is the first major version: V.02.00.00.

**What changed in the Summary:**

Score hero section: The Summary now opens with a full-width dark panel with an atmospheric radial glow behind the score ring. The ring is 300px (up from 200px), centred, with a drop-shadow glow halo. The maturity band label sits directly below the ring. This is the first thing you see when you enter the tab -- the number, not a form.

Radar chart: 480px (up from 320px), given its own full-height card on the left side of the data grid. Labels and polygon are dramatically more readable at this size.

Dimension score cards: Replaced the stacked bar-label layout with six large stat cards in a 2x3 grid. Each card has a 32px score number, a left accent bar colour-coded to the score range, and a thin animated bar. These sit alongside the radar in a two-column layout.

Structure reordered: Hero score reveal first, then data grid (radar + dimension cards), then metadata and flags inputs, then sub-component breakdown, then warning signals and focus areas. The user sees the output before the inputs, not the other way around.

**Input view:** No changes. All dimension tabs and the sidebar radar rail work exactly as before.

**CSS additions:** New classes: .summary-hero, .summary-hero-glow, .summary-hero-glow-floor, .summary-hero-content, .summary-hero-label, .summary-hero-ring, .summary-hero-band, .summary-hero-subtitle, .summary-data-grid, .summary-radar-panel, .summary-radar-panel-label, .summary-dim-panel, .summary-dim-panel-label, .dim-grid-6, .dim-stat-card, .dim-stat-code, .dim-stat-score, .dim-stat-name, .dim-stat-bar-bg, .dim-stat-bar-fill. Summary view panel gets max-width: 1360px centred.

**Version strings updated:** header-sub div, schema key, console.info -- all updated from v1.1 / v1 to V.02.00.00 / vista-v2.0.0.

**Files changed:** index.html (root, serves GitHub Pages), 03_Calculator/index.html (source)

---

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
