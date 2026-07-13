# VISTA SCORING MATH

## sub-component weighting (LOCKED)
each dimension split into sub-components with fixed point totals.
criteria inside a sub-component split ITS total equally.
criterion point value = sub-component total / number of criteria in it.
example: sub-comp worth 25pts, 8 criteria → each = 25/8 = 3.13pts.
this preserves strategic weighting. important sub-comps worth more.

## input types
[A] auto: tool outputs a fact. no human judgment. checkbox.
[S] semi: tool gathers, human confirms with evidence. checkbox.
[M] anchored 1-5: human matches evidence to defined level. radio 1-5.

## binary scoring ([A] and [S])
yes = full criterion points. no = 0.

## M criterion scoring (1-5 anchored, zero-anchored)
formula: points = (score - 1) / 4 * criterion_value
score 1 = 0% (0 pts), effectively absent, flag as gap
score 2 = 25%
score 3 = 50%
score 4 = 75%
score 5 = 100% (full)
example on 3.13pt criterion: score 3 → (3-1)/4*3.13 = 1.56pts.

## dimension score
sum all criterion points in dimension. max = 100.

## composite VISTA score
unweighted average of 6 dimension scores.
= (SV + AV + DE + BA + SC + RC) / 6

## sector percentile (phase 2)
activates once >= N brands assessed in a sector (suggest N>=5).
percentile = where brand's composite falls in sector's score array.
absolute score always shown. percentile added alongside.
questions NEVER change by sector. only comparison set changes.
percentile comparisons are only valid within the same export schema version
(schema field in the assessment JSON, currently vista-v1.1). scores produced
under different schema versions are not comparable; renormalization and
applicability rules can differ between versions.

## applicability + renormalization (see applicability-rules.md)
criteria marked N/A by published sector flags are excluded from scoring.
within a sub-component, points split equally across APPLICABLE criteria only.
a sub-component with zero applicable criteria redistributes its points
proportionally across the remaining sub-components of its dimension.
a dimension with zero applicable criteria is excluded from the composite,
which then averages the remaining applicable dimensions (minimum 4).

## red-flag outputs (separate from score)
some findings = signal something broken, surface separately:
- follower/engagement mismatch (huge followers, tiny engagement) → bought followers or dead audience
- zero AEO answers on owned surface → invisible to AI
- no dedicated domain → structural ceiling
- 10:1+ FB:IG skew for new brand → wrong-era audience building
- zero category-community presence → not in the room where buyers decide
red flags shown as flags, not deductions. high client impact.

## engagement rate, LOCKED definition (avoid the 10x methodology gap)
VISTA uses ONE definition. per-post engagement rate by reach where available, else by followers.
formula (followers basis): ER = (weighted engagements / followers) * 100
weighted engagements = shares*W_share + saves*W_save + comments*W_comment + likes*W_like
weights (from 2025-26 algorithm evidence, Mosseri confirmed shares 3-5x likes):
W_share = 5
W_save = 3
W_comment = 2
W_like = 1
watch time handled separately for video (see benchmarks).
sample = last 10 posts minimum.
CITE this definition in every report so it is falsifiable + repeatable.