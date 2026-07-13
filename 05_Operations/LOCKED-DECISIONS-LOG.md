# VISTA Locked Design Decisions Log
**Purpose:** Record of every design decision made during the build, with the reasoning. Read this before changing anything - these were deliberate choices, not defaults.

---

## Framework Decisions

### F1. 195 criteria, not 201 or 200
Original framework had 201. BA09 was deleted because it measured the earned/sponsored ratio across all BA pieces - a number that is already fully captured by the per-piece tri-state answers. Keeping BA09 would double-count the same signal and underweight the remaining BA06/BA07/BA08 sub-component.

BA now has 26 criteria. SC4.2 "Editorial quality" stayed at 15pts, split across 3 criteria instead of 4.

### F2. Unweighted composite (equal dimension weight)
No dimension is inherently more important than another - importance varies by sector, brand maturity, and business model. A weighted composite would embed the author's assumptions into the score. The unweighted average treats the researcher's configuration (which flags are on) as the weighting mechanism instead.

### F3. Zero-anchored M scale (score 1 = 0 points)
A score of 1 on a maturity scale means "absent" or "deficient." Absent is not neutral. If score 1 gave any points, the minimum achievable score for M criteria would be above zero, inflating scores for brands that have not developed that capability at all. The zero anchor makes the scale honest.

### F4. Inverted M criteria (AV10, BA26, RC07, SC14)
These four criteria are naturally phrased where high values indicate a bad state (e.g. "dominant source inaccurate"). Rather than flip the anchor text (which would confuse researchers comparing across criteria), the framework formalizes an `inverted: true` flag that reverses the semantic level order. Scoring math is unchanged: `((score-1)/4)*pts`. Level 5 is always the good/desirable state.

### F5. Outside-in only
VISTA never uses metrics the brand controls (e.g. Google Analytics, backend data). Every criterion is answerable from a public browser, a search engine, or AI tools. This is what makes VISTA auditable by any third party and comparable across brands.

### F6. Sub-component point budgets sum to 100 per dimension
This is what makes renormalization work. When a flagged criterion disappears, the surviving criteria are rescaled so the achievable maximum stays at 100. The math is: `scale = 100 / sum_of_applicable_subcomp_points`.

### F7. Minimum 4 of 6 dimensions must be active
If too many flags are off, some dimensions lose all applicable criteria. The tool enforces a minimum of 2 active flags (which ensures at least 4 dimensions remain active with applicable criteria). This guard prevents accidental zeros.

---

## Calculator Decisions

### C1. Single HTML file, no dependencies
Runs from `file://` by double-click. No npm, no CDN, no build step. This was chosen over a multi-file approach because:
- The tool needs to be distributable as a single file (email, USB, shared folder)
- It needs to work offline
- It eliminates dependency versioning problems forever

### C2. No localStorage
localStorage can be blocked by browser privacy settings, extensions, or enterprise policy. A file-based import/export pattern is always reliable and leaves an auditable paper trail. The researcher always has a `.json` file they can keep, share, or archive.

### C3. No LLM calls
Pure deterministic JS math. Same input = same output, always. This is essential for a scoring tool used in client deliverables. If the score could vary based on AI inference, it is not a score - it is an opinion.

### C4. Yes/No/NA tri-toggle (not just a checkbox)
A binary checkbox forces researchers to skip criteria they haven't checked yet - the system cannot distinguish "I checked and it's not there" from "I haven't looked yet." The tri-toggle makes intent explicit. N/A (researcher declares it not applicable) is different from No (researcher checked, it's absent). Both score 0, but the distinction matters for the evidence record.

### C5. N/A does not renormalize the denominator
When a researcher marks a criterion N/A, it scores 0 but does NOT remove that criterion from the point pool. The denominator stays fixed. This was the simpler design: renormalizing for researcher-selected N/A would require passing N/A IDs into buildPointsModel and would break the math verifier without substantial rework. The current rule is: system flags (PHYSICAL_LOCATION etc.) renormalize; researcher-selected N/A does not.

### C6. Import shallow-merge, current-state-wins
If a criterion is already answered in the current session, an imported value cannot overwrite it. This is the safe direction. The opposite (imported-wins) could silently clobber deliberate researcher input - a data-integrity failure. Skipped values are logged to console so the researcher can see what did not land.

### C7. Bought/dead-audience flag is provisional
Both ER and avg-weighted-per-post are computed on the same per-post-then-average path, so they cannot disagree. The flag fires when ER < 0.5% AND avg_weighted >= 50 (high engagement weight but low relative to follower count, which indicates bought followers). The flag carries `provisional: true` and renders "(provisional, pending calibration)" because the thresholds were set theoretically. After 5 real assessments, calibrate and remove the provisional label.

### C8. SC social inputs: named per-platform fields, no "followers on primary"
The original design had "platform" (text field) + "followers on primary" + separate "FB followers" + "IG followers" - which meant if primary was Instagram, two fields asked for the same number. Redesigned to: primary platform dropdown + Instagram followers + Facebook followers. The ER formula resolves which follower count to use based on the dropdown selection. For non-IG/FB platforms (TikTok, YouTube, LinkedIn, X), a third platform-named field appears.

### C9. Evidence notes per criterion (collapsible)
Added after it became clear that researchers need a place to record the URL or screenshot reference for each data point. The collapsible design keeps the interface uncluttered (only expanded when needed), and the content is exported in the JSON so evidence travels with the assessment.

### C10. Radar chart uses SVG `viewBox` padding
The radar hexagon uses `viewBox="-30 -30 ${s+60} ${s+60}"` to prevent axis labels (especially the top "SV" label) from being clipped at the SVG boundary. The drawn content is identical; only the viewport is wider.

### C11. Right panel fills full page height
The aside `.radar-rail` uses CSS grid `align-self: stretch` to fill the full left-column height. Without this, the dark sidebar stopped partway down the page when the criteria list was long. The `.radar-card` inside is `position: sticky; top: 50px` so it stays visible while scrolling.

### C12. Summary big card uses `.summary-score-card`, not `.radar-card`
The `.radar-card` CSS in the dark theme has `position: sticky; top: 50px; background: transparent` - designed for the aside sidebar. When the Summary page's big score card reused this class, it picked up sticky and transparent styles. Fixed by giving it its own class with `background: var(--bg-1); border: 1px solid var(--line); border-radius: var(--r);`.

### C13. Auto-scroll is forward-only
The auto-scroll to the next unanswered criterion only fires if `rect.top > window.innerHeight * 0.65` - meaning it only scrolls forward (down the page). If the next unanswered criterion is already visible or above the current viewport, no scroll happens. This prevents the jarring behavior where answering a question in the middle of the page jumped the researcher backward.

### C14. Colour scheme: black/white/orange only
Three colours strictly: `#060a0d` (near-black), `#dde4eb` (off-white), `#e28f26` (Adfactors orange). No blues, greens, purples for decoration. Gap/error states use `#d9603a` (a red-orange that stays within the orange family). Green (`#52c178`) is only used for confirmed/OK states and is desaturated enough to not compete.

### C15. Specialised Product Variant flag is fully generic
The flag was originally named "EV_PHEV" and described electric/hybrid vehicles. This was Denza-specific from the first client use. The description is now: "The brand has a sub-range or product variant with its own dedicated buyer questions and content (e.g. a premium tier, a specialist line, or a technology-specific category)." The flag key `EV_PHEV` stays in code for backward-compat with existing exports.

---

## Decisions That Were Explicitly Rejected

| Rejected | Reason |
|----------|--------|
| Per-dimension weighting | Embeds author assumptions; use flags instead |
| Renormalize for researcher N/A | Too complex, breaks verify.py without large rework |
| LLM auto-scoring | Non-deterministic, not auditable |
| Multi-file architecture | Breaks offline/distributable use case |
| localStorage persistence | Can be blocked; export/import is more reliable |
| External font CDN | Breaks offline use |
| Raw follower count criteria | Ratios are the honest comparison across different-scale brands |

---

*Last updated: 2026-07-10. Maintained by Adhit Satish.*
