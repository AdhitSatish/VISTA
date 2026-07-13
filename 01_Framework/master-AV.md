# MASTER CRITERIA, D2 AV AI Visibility (100)
tag key: [A]auto [S]semi [M]anchored1-5(pattern).

## PROMPT BATTERY (run before scoring, same every time)
run these across ChatGPT + Perplexity + Gemini + Claude. screenshot each. log date+model versions.
3 category prompts: "best luxury SUV in [country]" / "best [hybrid/EV] SUV [country]" / "best luxury family SUV [country]"
2 comparison: "[brand] vs [category leader]" / "[category leader] alternatives [country]"
2 buyer-Q: "is [brand] reliable" / "is [brand] worth buying"
1 control: a query where brand SHOULD NOT appear (tests relevance discipline).
AV volatile across reruns. always snapshot w/ date. reassess more often than other dims.

## PROTOCOL HARDENING (mandatory, makes AV runs repeatable + defensible)
- all prompts run in logged-out or clean sessions. no personalization contamination from researcher accounts or prior chat history.
- web-search mode explicitly ON or OFF per engine, recorded. do not mix modes within a battery.
- location context fixed and recorded (VPN/locale setting). AV answers shift by region; the region tested must be stated.
- each prompt run 2 to 3 times per engine. presence scored on MAJORITY of runs, not a single run. one lucky appearance is not presence.
- engine + model versions logged per run (e.g. "ChatGPT, GPT-5.2, search on, 2026-07-08").
- assessment export must carry an engineVersions object recording engine, model version, search mode, locale, run count, date.

## SC2.1 GEO brand mention in AI answers (25pts, 6 criteria)
AV01 [M-A] appears for primary category prompt. denom=4 engines. ev: 4 screenshots.
AV02 [M-A] appears for fuel-type category prompt. denom=4 engines. ev: screenshots.
AV03 [M-A] appears for use-case prompt. denom=4 engines. ev: screenshots.
AV04 [M-A] appears for price-bracket prompt. denom=4 engines. ev: screenshots.
AV05 [M-B] when appears, mention favorable. sample=all appearances. ev: screenshots.
AV06 [S] appears unprompted (vs only when named), cross-check control prompt. ev: screenshots.

## SC2.2 GEO source ecosystem quality (15pts, 4 criteria)
AV07 [M-A] AI answers cite 3+ distinct sources. denom=sources cited. ev: screenshots.
AV08 [S] 1+ cited source is independent editorial (not own site/PR). ev: screenshot.
AV09 [S] brand own domain cited by 1+ engine. ev: screenshot.
AV10 [M-B-inv] no dominant cited source outdated/wrong. 1=dominant wrong,5=all accurate. ev: notes.

## SC2.3 AEO buyer-Q answers exist on owned surface (20pts, 8 criteria)
AV11 [S] reliability Q answered. ev: url or documented absence.
AV12 [S] pricing Q answered. ev: url/absence.
AV13 [S] resale/residual Q answered. ev: url/absence.
AV14 [S] servicing cost Q answered. ev: url/absence.
AV15 [S] warranty terms answered. ev: url/absence.
AV16 [S] charging/range answered (EV/PHEV). ev: url/absence.
AV17 [S] safety Q answered. ev: url/absence.
AV18 [S] "why brand over [leader]" answered. ev: url/absence.

## SC2.4 AEO answer quality+structure (15pts, 4 criteria)
AV19 [S] answers in structured FAQ format not buried prose. ev: url.
AV20 [A] FAQ pages carry valid FAQPage schema. ev: validator.
AV21 [M-E] answers direct: 40-60 word answer-first (benchmark). 1=marketing prose,5=answer-first throughout. ev: page notes.
AV22 [S] answers current no outdated pricing/specs. ev: url.

## SC2.5 AEO comparison content (15pts, 3 criteria)
AV23 [S] 1+ head-to-head vs primary competitor on owned surface. ev: url/absence.
AV24 [M-D] comparison covers objection axes not just specs. set={resale,service,reliability,price,specs}. ev: page.
AV25 [A] comparison content indexed+linked not orphaned. ev: site: + internal link check.

## SC2.6 objection preemption (10pts, 2 criteria)
AV26 [M-D] known 3rd-party objections addressed in owned content. set=objections found in RC research. ev: cross-ref.
AV27 [S] brand publishes content countering single most-repeated objection. ev: url/absence.

## AV total: 27 criteria