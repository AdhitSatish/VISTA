# VISTA - Visibility Intelligence & Strategic Trust Assessment

> A deterministic, outside-in digital brand audit framework. 195 criteria. Zero AI in the scoring loop. Same inputs, same output, every time.

**Author:** Adhit Satish | **Version:** v1.1 | **Built:** 2026  
**Contact:** adhitsatish@gmail.com

---

## What Is VISTA?

VISTA is a structured methodology for measuring a brand's external digital presence across six dimensions. It answers the question: *what does a customer see when they research this brand online?*

No internal access. No Google Analytics. No CRM data. Everything measured is publicly observable.

### Six Dimensions

| Code | Name | Criteria | What It Measures |
|------|------|----------|-----------------|
| SV | Search Visibility | 49 | How findable the brand is on Google, Maps, and traditional search |
| AV | AI Visibility | 27 | How the brand appears in AI tools (ChatGPT, Perplexity, Gemini) |
| DE | Digital Experience | 38 | Quality and functionality of the owned website |
| BA | Brand Authority | 26 | Third-party credibility, earned media, editorial coverage |
| SC | Social & Content | 28 | Publishing quality, engagement rate, content strategy |
| RC | Reputation & Community | 27 | Reviews, community presence, what others say |

**Total: 195 criteria. Each dimension scored 0-100. Composite = unweighted average.**

### Maturity Bands
`Invisible (0-19)` `Emerging (20-39)` `Developing (40-59)` `Established (60-79)` `Leading (80-100)`

---

## The Calculator

A single HTML file. No dependencies. No build step. Runs offline by double-click.

**Features:**
- Yes / No / N/A input for binary criteria
- 1-5 anchored maturity scale for [M] criteria
- Absent / Sponsored / Earned tri-state for BA authority criteria
- Platform-specific engagement rate calculator (last 10 posts)
- Collapsible evidence notes per criterion
- Live radar chart across 6 dimensions
- Red flag panel (bought audience, AI invisibility, SEO ceiling, wrong-era audience)
- JSON export/import with shallow-merge (current state always wins)
- Print / PDF export

**To run:** Open `03_Calculator/index.html` in Chrome or Edge.

**To verify math:** `py 03_Calculator/verify.py` (requires Python 3). Must pass 75/75.

---

## Repository Structure

```
VISTA/
  00_README.md              Framework overview and locked decisions
  LICENSE                   Proprietary source-available license
  01_Framework/             
    _INDEX.md               Read order and session context
    dimensions.md           6-dimension overview and attribution rule
    scoring-math.md         Formulas, ER definition, red flag thresholds
    anchor-patterns.md      M-scale anchor patterns (A-F + 2 bespoke)
    applicability-rules.md  Flag-to-criterion gating rules
    master-SV.md            49 SV criteria with hints and evidence
    master-AV.md            27 AV criteria
    master-DE.md            38 DE criteria
    master-BA.md            26 BA criteria
    master-SC.md            28 SC criteria
    master-RC.md            27 RC criteria
    BUILD-INSTRUCTIONS.md   Original calculator build specification
  02_Benchmarks/
    thresholds.md           Pass/fail thresholds with citations
    sources.md              Research citations
  03_Calculator/
    index.html              THE CALCULATOR (single file, all logic inline)
    verify.py               75-check math verifier
    companion.py            Auto-fill helper for [A] criteria (no API key needed for most)
    README.md               Companion usage guide
  04_Assessments/           Completed assessment JSON exports (one per brand)
  05_Operations/
    MASTER-TECHNICAL-SPEC.md    Complete technical documentation
    REBUILD-GUIDE.md            Step-by-step rebuild instructions
    LOCKED-DECISIONS-LOG.md     Every design decision with reasoning
    LICENSING-AND-OWNERSHIP.md  IP, commercial strategy, migration checklist
```

---

## Design Principles

- **Deterministic.** Same inputs, same output. No randomness, no AI in the scoring loop.
- **Outside-in.** Every criterion is publicly observable. No internal access ever needed.
- **Single file.** `index.html` contains everything. No npm, no CDN, no build step.
- **No localStorage.** State lives in memory. Persist via JSON export.
- **Universal question set.** No per-client modifications. Applicability managed by sector flags.

---

## License

**Source Available - All Rights Reserved.**  
This software may be viewed and evaluated for personal, non-commercial purposes.  
Commercial use, redistribution, and derivative works require written permission.  
See [LICENSE](LICENSE) for full terms.

For licensing: adhitsatish903@gmail.com

---

*VISTA methodology and instrument authored by Adhit Satish, 2026.*
