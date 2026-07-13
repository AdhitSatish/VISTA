# VISTA Master Technical Specification
**Version:** v1.1 (July 2026)
**Author:** Adhit Satish
**Status:** Live - single-file calculator operational

This document is the authoritative technical brain for the VISTA calculator. It contains every design decision, data structure, function signature, and implementation detail needed to rebuild the calculator from scratch on any machine. Read this alongside the framework master files in `01_Framework/`.

---

## 1. What VISTA Is

VISTA (Visibility Intelligence & Strategic Trust Assessment) is an outside-in digital brand audit framework. It measures how visible, credible, and well-positioned a brand is across the digital ecosystem, using only publicly observable signals - no internal analytics, no platform API access required.

**Six dimensions:**

| Dim | Full Name | Criteria | Time |
|-----|-----------|----------|------|
| SV | Search Visibility | 49 | 45 min |
| AV | AI Visibility | 27 | 90 min |
| DE | Digital Experience | 38 | 30 min |
| BA | Brand Authority | 26 | 45 min |
| SC | Social & Content | 28 | 30 min |
| RC | Reputation & Community | 27 | 45 min |
| **Total** | | **195** | **~5 hrs** |

**Maturity bands (composite score):**

| Band | Range |
|------|-------|
| Invisible | 0-19 |
| Emerging | 20-39 |
| Developing | 40-59 |
| Established | 60-79 |
| Leading | 80-100 |

---

## 2. Files

```
VISTA/
  00_README.md                    Framework overview
  01_Framework/
    _INDEX.md                     Reading order
    dimensions.md                 6-dim overview
    scoring-math.md               Formulas
    thresholds.md                 Pass/fail thresholds
    sources.md                    Evidence sources
    anchor-patterns.md            M-scale anchor definitions
    applicability-rules.md        Flag logic
    master-SV.md                  49 SV criteria
    master-AV.md                  27 AV criteria
    master-DE.md                  38 DE criteria
    master-BA.md                  26 BA criteria
    master-SC.md                  28 SC criteria
    master-RC.md                  27 RC criteria
    BUILD-INSTRUCTIONS.md         Original build spec
  02_Benchmarks/                  Sector percentile data (stub)
  03_Calculator/
    index.html                    THE CALCULATOR (single file, all logic)
    verify.py                     Math verification script (75 checks)
    companion.py                  Auto-fill helper for [A] criteria
    README.md                     Companion usage guide
  04_Assessments/                 Completed assessment exports
  05_Operations/
    MASTER-TECHNICAL-SPEC.md      This file
    REBUILD-GUIDE.md              Step-by-step rebuild instructions
    LICENSING-STRATEGY.md         IP, ownership, monetization
```

**The calculator is entirely contained in `index.html`.** All other files are supplementary. If you have `index.html`, you have VISTA.

---

## 3. Architecture Principles (Non-Negotiable)

These were locked decisions during the build and must be preserved in any rebuild:

1. **Single HTML file.** No external JS, no CDN, no npm, no build step. Runs from `file://` by double-click in any Chromium browser.
2. **No LLM calls.** Pure JS math. Deterministic. Same input always produces same output.
3. **No localStorage.** State persists only in memory. Export/import JSON file for persistence.
4. **No network requests.** No analytics, no telemetry, no external fonts.
5. **Offline-first.** Works with no internet connection.
6. **No em dashes (U+2014) anywhere** in the tool text, hints, or comments.

---

## 4. CRITERIA Array - Data Format

Every criterion is an object in the `const CRITERIA = [...]` array inlined in `index.html`. Each object has these fields:

```javascript
{
  id: "SV01",                        // Unique ID: dim+2-digit-number
  dimension: "SV",                   // One of: SV | AV | DE | BA | SC | RC
  subComponent: "SC1.1",             // Sub-component grouping key
  subComponentPoints: 15,            // Total points allocated to this sub-component
  criteriaInSubComponent: 7,         // Count of criteria in this sub-component (used to split points)
  text: "brand name query returns owned site pos 1",  // Terse framework label
  hint: "Google the brand name. Is the brand's own website the first non-ad result?",  // Plain-English action prompt
  tag: "A",                          // A (auto/quick-check) | S (spot-check) | M (maturity scale)
  pattern: null,                     // null | "A".."F" | "bespoke-DE18" | "bespoke-DE23" | "bespoke-RC8"
  inverted: false,                   // true for AV10, BA26, RC07, SC14 (5=good, 1=deficient)
  inlineAnchors: null,               // null | { 1: "text", 2: "text", 3: "text", 4: "text", 5: "text" }
  evidence: "SERP screenshot + date", // What to record as evidence
  sponsorable: false,                // true ONLY for BA01-BA05, BA18-BA20, BA27-BA28
  checklist: null                    // null | ["Instagram","Facebook",...] for checklist-type criteria
}
```

**Key rules:**
- `subComponentPoints / criteriaInSubComponent` = points per criterion (computed at runtime, never hardcoded)
- Per-dimension sum of all sub-component point allocations = **100** always
- `inverted: true` reverses the M-scale semantic: level 5 is always the good state, level 1 is always deficient
- `checklist` criteria score binary: any item ticked = full points; empty array = 0
- `sponsorable: true` enables the tri-state BA widget (Absent / Sponsored / Earned)

---

## 5. Applicability Flags

Four flags gate which criteria are shown and scored. Criteria that are not applicable for the brand type are hidden and score 0, and the point pool is renormalized so the achievable maximum stays 100.

```javascript
const APPLICABILITY_FLAGS = {
  PHYSICAL_LOCATION:  "The brand has a physical location customers can visit (store, branch, office, or venue).",
  PHYSICAL_PRODUCT:   "The brand sells tangible products with specific models (e.g. consumer electronics, appliances, vehicles). Not for pure services, software, or financial products.",
  EV_PHEV:            "The brand has a sub-range or product variant with its own dedicated buyer questions and content (e.g. a premium tier, a specialist line, or a technology-specific category).",
  BOOKABLE_EXPERIENCE:"The brand offers a bookable appointment, trial, or demonstration (e.g. product demo, consultation, site visit, or test experience)."
};
```

**Display names:**
```javascript
const FLAG_DISPLAY = {
  PHYSICAL_LOCATION:  "Physical Location",
  PHYSICAL_PRODUCT:   "Physical Products",
  EV_PHEV:            "Specialised Product Variant",
  BOOKABLE_EXPERIENCE:"Bookable Experience"
};
```

**The flag-to-criterion mapping** is in `const CRIT_FLAGS = { SV31: "PHYSICAL_LOCATION", ... }` - 26 criteria are gated this way. The rules:
- Any flag combination (2^4 = 16 possible) must still produce a per-dimension total of exactly 100 achievable points
- At least 4 of 6 dimensions must remain active (minimum 2 flags always on - enforced in UI)

---

## 6. State Object (Complete Structure)

```javascript
const state = {
  answers: {},
  // Criterion ID -> value:
  //   Binary [A]/[S]: "yes" | "no" | "na"  (backward-compat: true=yes, false=no)
  //   [M] scale: "1" | "2" | "3" | "4" | "5"  (string)
  //   BA tri-state: "absent" | "sponsored" | "earned"
  //   Checklist: ["Instagram", "Facebook", ...]  (array of ticked strings)

  flags: {
    PHYSICAL_LOCATION: true,
    PHYSICAL_PRODUCT: true,
    EV_PHEV: true,
    BOOKABLE_EXPERIENCE: true
  },
  // All default to true. User can toggle. Minimum 2 must stay true.

  flagsTouched: false,
  // Set to true when user manually edits flags.
  // Guards import: if flagsTouched=false, import can overwrite flags.
  // If flagsTouched=true, import cannot overwrite flags.

  engineVersions: { ChatGPT: "", Perplexity: "", Gemini: "", Claude: "" },
  // AV protocol: researcher logs which model version was used.
  // Embedded in export JSON.

  confirmed: { SV: false, AV: false, DE: false, BA: false, SC: false, RC: false },
  // Tracks whether the CONFIRM button was clicked for each dimension.
  // Only confirmed dimensions appear on the radar chart.

  radarVals: { SV: 0, AV: 0, DE: 0, BA: 0, SC: 0, RC: 0 },
  // The values currently displayed on the radar (animate toward dimensionScore).

  collapsed: {},
  // subComponent key -> true when user collapses that group.

  activeTab: "SV",
  // Currently visible tab. One of: "SV"|"AV"|"DE"|"BA"|"SC"|"RC"|"SUMMARY"

  meta: {
    brand: "",
    country: "",
    sector: "",
    launchYear: "",
    assessmentDate: new Date().toISOString().slice(0, 10)
  },
  // Brand metadata. Embedded in export JSON and used for filename.

  social: {
    primary: {
      platform: "Instagram",
      // Selected from: Instagram | Facebook | TikTok | YouTube | LinkedIn | X / Twitter
      followers: 0,
      // Used for ER calculation ONLY when platform is not Instagram or Facebook.
      // For Instagram: use igFollowers. For Facebook: use fbFollowers.
      posts: [
        { shares: 0, saves: 0, comments: 0, likes: 0 },  // post 1
        { shares: 0, saves: 0, comments: 0, likes: 0 },  // post 2
        // ... 10 total
      ]
    },
    fbFollowers: 0,   // Facebook follower count (FB:IG ratio + ER if primary=Facebook)
    igFollowers: 0    // Instagram follower count (FB:IG ratio + ER if primary=Instagram)
  },
  // SC dimension social data. Drives ER calculation and 2 red flags.

  notes: {}
  // Criterion ID -> string (evidence note text).
  // Stored per-criterion. Exported in JSON. Import fills blanks only.
};
```

---

## 7. Scoring Engine

### 7.1 buildPointsModel(flags)
**Purpose:** Compute the per-criterion point value for a given flag combination. Renormalizes so each dimension always sums to 100 across applicable criteria.

```
for each criterion c:
  count how many criteria share c.subComponent and are applicable
  if 0 applicable in sub-component: pts[c.id] = 0
  else:
    scale = 100 / sum(subComponentPoints for applicable sub-components in dim)
    pts[c.id] = c.subComponentPoints * scale / count_applicable_in_subComponent
```

Returns: `{ pts_of: { "SV01": 2.14, ... }, dim_appl: { "SV": true, ... } }`

### 7.2 isApplicable(c, flags)
```
flag = CRIT_FLAGS[c.id]
return (!flag) || flags[flag] === true
```

### 7.3 critValue(c, answers, pts_of)
```
pts = pts_of[c.id]
if pts === 0: return 0

v = answers[c.id]
if c.tag === "M":
  s = parseInt(v); return ((s-1)/4) * pts
if c.checklist:
  return (Array.isArray(v) && v.length > 0) ? pts : 0
if c.sponsorable:
  if v === "earned": return pts
  if v === "sponsored": return 0.5 * pts
  return 0
return (v === true || v === "yes") ? pts : 0
```

### 7.4 dimensionScore(dim, state)
```
pts_of, dim_appl = buildPointsModel(state.flags)
if !dim_appl[dim]: return null
score = sum(critValue(c, state.answers, pts_of) for c in CRITERIA where c.dimension === dim)
return min(score, 100)
```

### 7.5 composite(state)
```
scores = [dimensionScore(d, state) for d in RADAR_DIMS if score !== null]
return sum(scores) / scores.length
```

### 7.6 isAnswered(c)
```
v = state.answers[c.id]
if c.checklist: return Array.isArray(v) && v.length > 0
if c.tag === "M": return parseInt(v) >= 1 && parseInt(v) <= 5
if c.sponsorable: return v === "absent" || v === "sponsored" || v === "earned"
return v === true || v === false || v === "yes" || v === "no" || v === "na"
```

---

## 8. UI Architecture

### 8.1 Tab System
7 tabs: SV | AV | DE | BA | SC | RC | SUMMARY
- Each dimension tab shows a progress counter: `"SV 12/49"`
- SUMMARY tab shows: `"195 total"`
- Only one tab visible at a time (`state.activeTab`)
- Clicking a tab sets `state.activeTab` and calls `renderAll()`

### 8.2 Criterion Card Rendering
Each criterion renders as a horizontal row:
```
[ID box][Body: text + hint + evidence + input widget + evidence note toggle]
```

**ID box** contains:
- Criterion ID (e.g. "SV01")
- Pattern tag: `[A]`, `[S]`, `[M-B]`, `[M-D-inv]`, etc.
- N/A badge if criterion is not applicable (greyed out)

**Body** contains:
- `.crit-text`: the terse framework label
- `.crit-hint`: plain-English action prompt (what to do + what "yes" looks like)
- `.crit-ev`: "Record: [evidence type]"
- Input widget (see 8.3)
- Evidence note toggle (collapsible textarea, stored in `state.notes[c.id]`)

### 8.3 Input Widgets

**Binary [A]/[S] (Yes/No/NA tri-toggle):**
Three radio-style pill buttons: Yes | No | N/A
- Yes = orange border + orange text
- No = red/coral border + red text
- N/A = muted border + muted text
- Stored as: `"yes"` | `"no"` | `"na"`
- Backward-compat: old imports with `true`/`false` also accepted

**[M] Maturity Scale:**
5 radio options in a grid, each showing the anchor text for that level.
- Inverted criteria (`inverted: true`): same scale but semantics reversed (5=good is already correct)
- Pattern anchors loaded from inline JS constants or `inlineAnchors` field
- Inverted note shown above scale: "5 = good · 1 = deficient"
- Stored as string `"1"` through `"5"`
- Score 1 = 0 points (zero-anchored)

**BA Tri-State Sponsorable:**
Three radio buttons: Absent | Sponsored | Earned
- Absent = 0 pts
- Sponsored = 0.5x pts (grey accent)
- Earned = full pts (green accent)
- Only for BA01-BA05, BA18-BA20, BA27-BA28

**Checklist (SV03 etc.):**
Checkbox group from `c.checklist` array.
- Any box ticked = full pts for that criterion
- Nothing ticked = 0 pts
- Stored as array of ticked strings: `["Instagram", "YouTube"]`
- SV03 checklist: `["Instagram","Facebook","LinkedIn","YouTube","TikTok","X / Twitter","Pinterest"]`

### 8.4 Sub-Component Grouping
Criteria are grouped under collapsible headers:
```
[- SC1.1 Brand keyword performance - 15pts]   [0/7]
  SV01 ... SV07
[+ SC1.2 Non-brand category keyword - 25pts]  [0/8]  (collapsed)
  ...
```
Header shows: sub-component name, point budget, answered/total counter.
Clicking header toggles `state.collapsed[subComponent]`.

### 8.5 SC Social Inputs (above SC criteria)
Platform selector + follower counts + 10-post engagement table.

**Follower fields:**
- Dropdown: primary platform (Instagram / Facebook / TikTok / YouTube / LinkedIn / X / Twitter)
- "Instagram followers" field (always shown - used for FB:IG ratio + ER if primary=Instagram)
- "Facebook followers" field (always shown - used for FB:IG ratio + ER if primary=Facebook)
- "[Platform] followers" field (only shown if primary is NOT Instagram or Facebook - stored in `state.social.primary.followers`)

**Primary followers resolution for ER:**
```
if primary === "Instagram": primaryFollowers = igFollowers
else if primary === "Facebook": primaryFollowers = fbFollowers
else: primaryFollowers = state.social.primary.followers
```

**Post table (10 rows):**
Each row: shares | saves | comments | likes | weighted | ER%
- `weighted = shares*5 + saves*3 + comments*2 + likes*1`
- `ER% = (weighted / primaryFollowers) * 100`

**Readout bar (3 values):**
- Weighted ER = mean of per-post (weighted/followers*100)
- Avg weighted / post = mean of per-post weighted
- FB:IG ratio = fbFollowers / igFollowers (or "–" if igFollowers=0)

### 8.6 AV Protocol Block (above AV criteria)
Four text inputs for engine version strings:
- ChatGPT, Perplexity, Gemini, Claude
- Stored in `state.engineVersions`
- Embedded in export JSON
- Instructs researcher to log model version + locale + run count

### 8.7 Confirm Button
Each dimension tab has a CONFIRM button at the bottom.
- On click: computes `dimensionScore(dim, state)`, sets `state.confirmed[dim] = true`, animates radar axis from current to new value
- Sets `state.radarVals[dim]` = new score
- CONFIRM is required before the radar updates

### 8.8 Radar Chart (SVG)
Hand-drawn SVG hexagonal radar. 6 axes (one per dimension).
- Axis order: SV (top/12 o'clock), then AV/DE/BA/SC/RC clockwise
- `viewBox="-30 -30 ${s+60} ${s+60}"` (padded to prevent label clipping)
- Center: `(s/2, s/2)`, radius: `s * 0.42`
- Grid: 5 concentric hexagons at 20/40/60/80/100
- Fill: orange at 15% opacity
- Unconfirmed dimensions show a dashed "pending" dot at score position
- Labels: dimension short name + score value (or "–" if not confirmed)

---

## 9. Red Flag Logic

Flags are computed fresh on every render. They do not affect scoring - they surface as warning chips.

### 9.1 Bought/Dead Audience
**Fires when:** weighted ER < 0.5% AND avg weighted engagements per post >= 50

Both values are computed on the SAME per-post-then-average path:
```
for each of 10 posts:
  w_i = shares_i*5 + saves_i*3 + comments_i*2 + likes_i
  er_i = (w_i / primaryFollowers) * 100

ER = mean(er_i)
avgWeighted = mean(w_i)

FIRES if ER < 0.5 AND avgWeighted >= 50
```
The flag carries `provisional: true` - renders with "(provisional, pending calibration)" label. Calibrate after ~5 assessments.

### 9.2 Invisible to AI
**Fires when:** AV11 through AV18 are ALL unanswered OR all = "no" / false

Checks: none of AV11-AV18 has answer `true` or `"yes"`.

### 9.3 Structural SEO Ceiling
**Fires when:** SV40 = "no" or `false`

Does not fire on unanswered (only explicit No).

### 9.4 Wrong-Era Audience
**Fires when:** fbFollowers / igFollowers >= 10 AND state.meta.launchYear >= 2020

Logic: `state.social.fbFollowers / state.social.igFollowers >= 10 && Number(state.meta.launchYear) >= 2020`
Guard: only fires when igFollowers > 0.

### 9.5 Absent Where Buyers Decide
**Fires when:** RC14 score = "1" (level 1 on the maturity scale)

---

## 10. Export / Import JSON Format

### 10.1 Export Schema (`"schema": "vista-v1.1"`)
```json
{
  "schema": "vista-v1.1",
  "buildId": "BUILD_ID_CONSTANT",
  "exportedAt": "2026-07-10T12:00:00.000Z",
  "meta": {
    "brand": "Brand Name",
    "country": "Country",
    "sector": "Sector",
    "launchYear": "2010",
    "assessmentDate": "2026-07-10"
  },
  "applicabilityFlags": {
    "PHYSICAL_LOCATION": true,
    "PHYSICAL_PRODUCT": true,
    "EV_PHEV": true,
    "BOOKABLE_EXPERIENCE": false
  },
  "engineVersions": {
    "ChatGPT": "GPT-4o",
    "Perplexity": "Online",
    "Gemini": "1.5 Pro",
    "Claude": "Sonnet"
  },
  "social": {
    "primary": {
      "platform": "Instagram",
      "followers": 0,
      "posts": [ ...10 post objects... ]
    },
    "fbFollowers": 12000,
    "igFollowers": 45000
  },
  "answers": {
    "SV01": "yes",
    "SV02": "no",
    "SV03": ["Instagram", "YouTube"],
    "AV05": "3",
    "BA01": "earned"
  },
  "notes": {
    "SV01": "https://screenshot.com/evidence-url",
    "AV05": "Tested on 3 runs, majority returned level 3 response"
  },
  "dimensions": {
    "SV": { "score": 72.4, "confirmed": true },
    "AV": { "score": 48.1, "confirmed": true }
  },
  "composite": 61.2,
  "maturityBand": "Established",
  "flags": [ ...red flag objects... ]
}
```

Filename format: `{brand-slug}-{YYYY-MM-DD}.json`

### 10.2 Import Rules (shallow-merge, current-state-wins)
- `answers`: import fills only UNANSWERED criteria. Already-answered criteria are not overwritten.
- `meta`: import fills only EMPTY fields. Non-empty fields are preserved.
- `social`: import fills only if ALL social inputs are at zero. If any value exists, entire social block is preserved.
- `applicabilityFlags`: import fills only if `state.flagsTouched === false`.
- `engineVersions`: import fills only empty engine version strings.
- `notes`: import fills only criteria with no existing note.
- Any skipped value is logged to browser console: `"import skipped for SV01, existing state value = true"`

---

## 11. Design System (CSS Variables)

```css
:root {
  --bg:           #060a0d;   /* Deepest background */
  --bg-1:         #0b1218;   /* Panel / aside background */
  --bg-2:         #101a22;   /* Input / card background */
  --fg:           #dde4eb;   /* Primary text */
  --fg-2:         #8aa0b4;   /* Secondary text / hints */
  --muted:        #3d5264;   /* Placeholder / labels / muted text */
  --accent:       #e28f26;   /* Orange - Adfactors brand colour */
  --accent-dim:   rgba(226,143,38,0.10);  /* Orange fill for yes-selected */
  --accent-border:rgba(226,143,38,0.30);  /* Orange border */
  --line:         rgba(255,255,255,0.055); /* Subtle dividers */
  --line-strong:  rgba(255,255,255,0.11);  /* Stronger borders */
  --gap:          #d9603a;   /* Red/coral - gap indicator / No selection */
  --ok:           #52c178;   /* Green - OK / confirmed */
  --r:            10px;      /* Default border radius */
  --r-sm:         6px;       /* Small radius (inputs) */
  --r-pill:       20px;      /* Pill-shaped buttons */
}
```

**Key structural CSS:**
```css
/* Full-height right panel */
main { display: grid; grid-template-columns: 1fr 300px; min-height: calc(100vh - 50px); }
aside.radar-rail { align-self: stretch; background: var(--bg-1); border-left: 1px solid var(--line); }
.radar-card { position: sticky; top: 50px; padding: 22px; background: transparent; }

/* Header */
header { height: 50px; background: var(--bg-1); border-bottom: 1px solid var(--line); }
header h1 { font-size: 18px; letter-spacing: 2.5px; }
header h1 span { color: var(--accent); }  /* "VISTA" is orange, "CALCULATOR" is white */

/* Criterion layout */
.criterion { display: grid; grid-template-columns: 60px 1fr; gap: 16px; padding: 16px 0; }
.crit-id { font-size: 11px; letter-spacing: 1px; color: var(--muted); }
.crit-id .pat { color: var(--accent); font-weight: 600; }

/* Yes/No/NA pills */
.yn-tri { display: flex; gap: 8px; flex-wrap: wrap; }
.yn-sel-yes { border-color: var(--accent); background: var(--accent-dim); color: var(--accent); }
.yn-sel-no  { border-color: var(--gap);    background: rgba(217,96,58,0.10); color: var(--gap); }
.yn-sel-na  { border-color: var(--line-strong); background: var(--bg-2); color: var(--fg-2); }

/* Print / PDF */
@media print {
  body { background: #fff !important; color: #111 !important; }
  header, nav.tabs, aside.radar-rail, .confirm-btn, .crit-note-btn { display: none !important; }
  main { display: block !important; }
}
```

---

## 12. JavaScript Constants and Build Markers

```javascript
const BUILD_ID = "f53fb6c9";     // Build identifier (embedded in exports)
const SCHEMA_VERSION = "vista-v1.1";
```

**Assessment load-time assertions (halt on failure):**
- Criteria counts: SV=49, AV=27, DE=38, BA=26, SC=28, RC=27 (total=195)
- Per-dimension sub-component points sum to 100
- BA sub-components with criteriaInSubComponent values must reconcile
- Zero em dashes in loaded HTML (self-test)

**Attribution line (in browser console on load):**
```
VISTA v1.1. Methodology and instrument authored by Adhit Satish.
```

---

## 13. verify.py (Math Verification Script)

Standalone Python script. Parses `index.html`, mirrors the JS scoring engine in Python, runs 75 checks.

**Must always pass 75/75 before releasing any change to index.html.**

Run with: `py verify.py`

**Check groups:**
1. Structure: criterion counts per dimension, total=195, CRIT_FLAGS count
2. All-max: every criterion at max value, all flags on = each dim 100, composite 100
3. All-zero: every criterion at zero, all flags on = each dim 0, composite 0
4. SV partial hand-recompute: alternating yes/no, M at 3 = matches hand math
5. BA tri-state half-weight: Sponsored = exactly 0.5x pts per criterion
6. Weighted ER per-post path: 10 posts shares=10, followers=1000, ER=5.0%, avgWeighted=50
7. Bought/dead-audience flag: 4 test cases (2 non-fire, 1 non-fire, 1 MUST fire)
8. Inverted criteria: exactly 4, all named (AV10, BA26, RC07, SC14)
9. Renormalization: all 16 flag combos produce per-dim total exactly 100
10. PHYSICAL_LOCATION off: all dims still = 100, renormalized SV01 correct
11. Hint quality: all 195 non-empty, no trivially similar to canonical text, SV03 checklist correct
12. File-level: zero em dashes, schema string, buildId, engineVersions, applicabilityFlags, no localStorage

---

## 14. companion.py (Auto-Fill Helper)

Fills deterministic [A] criteria by fetching public data. No LLM calls. Runs independently.

**Coverage (~18 criteria):**
- SV16/SV17/SV18/SV19: PageSpeed Insights (LCP, INP, CLS, mobile perf)
- DE28/DE29: Desktop/mobile PageSpeed
- DE33/DE34: Lighthouse accessibility (alt text, WCAG AA contrast)
- SV21/SV22/SV25/SV29: Homepage HTML parsing (title length, meta desc, alt coverage, canonical)
- SV23/SV24/AV20: JSON-LD schema detection (Organization, Product, FAQPage)
- SV26/SV27: Sitemap + robots.txt presence (HEAD requests)
- SV28: HTTPS redirect confirmation

**CLI usage:**
```
py companion.py --url https://brand.com --product-url https://brand.com/product --psi-key YOUR_KEY
```

**Output:** `brand-companion-YYYY-MM-DD.json` - compatible with Import JSON button.

---

## 15. Planned / Possible Future Enhancements

These were discussed but not yet built. Documenting so they can be built later:

| Feature | Notes |
|---------|-------|
| Sector percentiles | Scoring relative to benchmarks. 02_Benchmarks/ is the stub. |
| Hosted SaaS version | Auth layer + database, multiple users/assessments |
| SERP rank checks | Requires paid SERP API (SerpAPI, DataForSEO) |
| GBP criteria auto-fill | Requires Places API or GBP access |
| Social platform metrics auto-fill | Requires platform API |
| AV buyer question checklist | AV11-AV18 as checklist not just binary |
| SC content pillar checklist | SC13 as checklist |
| Rationale documentation | 01_Framework/rationale-*.md (Rev 3 plan) |
| White-label licensing | Custom branding + hosted deployment for agencies |

---

*Last updated: 2026-07-10. Maintained by Adhit Satish.*
