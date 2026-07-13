PREREQUISITE: read _INDEX.md first, follow its order.

# CLAUDE CODE BUILD INSTRUCTIONS, VISTA Calculator

## goal
build a zero-token, offline, single-folder HTML calculator.
reads 200 criteria from a data file. researcher ticks/scores. outputs 6 dimension scores + composite + live radar chart.
NO LLM calls anywhere. pure JS math. deterministic. same input=same output.

## step 1: build the data file
read all 6 master files: master-SV, master-AV, master-DE, master-BA, master-SC, master-RC.
extract every criterion into a data file `criteria.json`.
each criterion object:
{
  id: "SV01",
  dimension: "SV",
  subComponent: "SC1.1 Brand keyword performance",
  subComponentPoints: 15,
  criteriaInSubComponent: 7,   // for point calc
  text: "brand name query returns owned site pos 1",
  tag: "A",                     // A | S | M
  pattern: null,               // for M only: A|B|C|D|E|F|bespoke-DE23|bespoke-RC8
  evidence: "SERP screenshot+date"
}
point value computed at runtime = subComponentPoints / criteriaInSubComponent. DO NOT hardcode.
verify counts: SV52 AV27 DE39 BA27 SC28 RC27 = 200 total (BA09 retired, see master-BA.md). if mismatch, STOP and report.

## step 2: scoring logic (pure functions)
binary (tag A or S): checked=full points, unchecked=0.
  points = subComponentPoints / criteriaInSubComponent
M (tag M): input 1-5. zero-anchored.
  points = ((score-1)/4) * (subComponentPoints / criteriaInSubComponent)
dimension score = sum of all criterion points in dimension. cap 100.
composite = (SV+AV+DE+BA+SC+RC)/6.
round display to 1 decimal. keep full precision internally.

## step 3: anchor pattern definitions
read anchor-patterns.md. store the 6 patterns + 2 bespoke as data.
when rendering an M criterion, show its pattern's 5 level definitions next to the 1-5 radio.
researcher sees the observable anchors, not just numbers. critical for no-bias.

## step 4: UI (tabbed, one dimension per screen)
stack: single self-contained index.html. vanilla JS. NO framework. NO npm. NO external libs. NO internet needed.
radar chart = hand-drawn SVG (no chart library). 6 axes fixed from start.
tabs: one per dimension (SV AV DE BA SC RC) + final SUMMARY tab.
on each dimension tab: list its criteria grouped by sub-component.
  A/S criteria = checkbox.
  M criteria = 1-5 radio with anchor definitions shown inline.
each dimension tab has a CONFIRM button.
on CONFIRM: compute that dimension score, animate its radar axis from 0 to score.
radar shows all 6 axes always; unconfirmed sit at 0; confirmed fill in.
SUMMARY tab: full radar, 6 scores, composite, maturity band, red-flag panel.

## step 5: red-flag panel
compute + display separately from scores (read scoring-math.md red-flags):
- follower:engagement mismatch (needs manual follower + ER input) => "bought/dead audience"
- zero AEO answers (AV11-18 all unchecked) => "invisible to AI"
- no dedicated domain (SV40 unchecked) => "structural SEO ceiling"
- FB:IG >10:1 (needs manual input) => "wrong-era audience"
- zero category-community (RC14 score 1) => "absent where buyers decide"
show as flags with plain-language meaning. not deductions.

## step 6: aesthetic (LOCKED, follow exactly)
base background: #ffffff
all font color: #1e1e1e
highlight/accent: #e28f26
font: Roboto (or system sans fallback)
feel: clean futuristic minimal. "Krypton/Superman", crisp, luminous, uncluttered, lots of whitespace.
radar: thin lines, accent fill low-opacity, smooth axis animation on confirm.
no decorative clutter. every element earns its place.
mobile responsive but desktop-first (assessment is desk work).

## step 7: output/export
SUMMARY tab: button to export results as JSON (the 200 scores + 6 dims + composite + flags + date).
this JSON = one assessment record. saved to 04_Assessments/[brand]-[date].json.
these records build the sector percentile set over time.

## step 8: persistence
use in-memory state during session. allow JSON export/import so an assessment can be saved + reloaded.
do NOT use localStorage (may be blocked). export/import file instead.

## constraints recap
0 tokens. offline. deterministic. no LLM. no framework. no external calls. single folder.
comment every non-obvious line. flag any code that could be simpler.
if any master file criterion is ambiguous, STOP and ask, do not guess.

## phase 2 (not now, design the slot)
sector percentile: once N>=5 brands in a sector assessed, load their JSON records,
compute where current brand composite falls. show percentile beside absolute score.
build the UI slot for it now (empty), wire later.