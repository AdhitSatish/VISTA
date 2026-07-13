# VISTA READ ORDER, for Claude Code + humans

## read in THIS sequence. each depends on prior.
1. 00_README.md             , what VISTA is, locked decisions
2. 01_Framework/dimensions.md, the 6 dims, attribution rule
3. 01_Framework/scoring-math.md, weighting, formulas, red-flags, ER formula
4. 01_Framework/anchor-patterns.md, the 6 M-patterns + 2 bespoke
5. 02_Benchmarks/thresholds.md, cited numbers used in criteria
6. 02_Benchmarks/sources.md   , citation list
7. master-SV / AV / DE / BA / SC / RC .md, the 200 criteria (any order, independent of each other)
8. 03_Calculator/BUILD-INSTRUCTIONS.md, how to build the tool

## dependency notes
- master files USE thresholds.md numbers + anchor-patterns.md patterns. read those first.
- BUILD-INSTRUCTIONS reads ALL master files + scoring-math + anchor-patterns.
- AV master references RC research (objections). run RC research before scoring AV26.
- calculator needs NOTHING except these md files. no external docs.
- BA09 was retired to eliminate double-counting with the BA sponsorable tri-state; SC4.2 now splits 15 pts across BA06/BA07/BA08 (5 pts each).
- Current criterion counts: SV 49 / AV 27 / DE 38 / BA 26 / SC 28 / RC 27 = 195 total.
- verify.py enforces 75 math checks against the live index.html. must pass 75/75 before any release.

## build trigger
point Claude Code here first. it reads this, then follows the order. then executes BUILD-INSTRUCTIONS.

## session context (for Claude Code resuming work)
- Calculator is at 03_Calculator/index.html, schema v1.1, build f53fb6c9
- verify.py lives at 03_Calculator/verify.py, run with: py verify.py
- Preview server: port 8437 (start from Desktop/Claude working directory)
- No em dashes anywhere. No localStorage. No LLM calls in scoring.
- For full technical detail: read 05_Operations/MASTER-TECHNICAL-SPEC.md