# VISTA Calculator + Companion

**The companion's output is a starting point, not a settled answer.** Every criterion the companion pre-fills must still be reviewed and confirmed by a researcher before it counts. Rubber-stamping companion output erases the "human confirms evidence" step the framework is built on. The calculator's import rule (current state wins) guarantees the tool never overwrites an answer you have already entered, but nothing stops a researcher from importing and confirming without looking. That responsibility sits with the researcher.

## What is in this folder
- `index.html` - the VISTA calculator. Open by double-click, runs fully offline, zero tokens, deterministic. Methodology and instrument authored by Adhit Satish.
- `companion.py` - optional evidence-gatherer that pre-fills the deterministic subset of [A] criteria.
- `BUILD-INSTRUCTIONS.md` - the build spec the calculator was built from.

## What the companion does
It fetches public data and answers the [A] criteria that a script can answer honestly:

| Group | Criteria | Needs |
|---|---|---|
| Core Web Vitals + perf | SV16, SV17, SV18, SV19, DE28, DE29 | free PSI API key |
| Accessibility audits | DE33 (image alt), DE34 (contrast) | free PSI API key |
| Homepage tags | SV21 (title), SV22 (meta desc), SV25 (img alt), SV29 (canonical) | nothing |
| Schema | SV23 (Organization), SV24 (Product, needs --product-url), AV20 (FAQPage) | nothing |
| Plumbing | SV26 (sitemap), SV27 (robots.txt), SV28 (HTTPS redirect) | nothing |

## What it deliberately does not do
- SERP rank checks (SV01 to SV15, SV38, SV44 to SV48): need a paid SERP API. Manual search per the criterion hints.
- Google Business Profile criteria (SV31 to SV37, RC01 to RC04): need GBP ownership or a Places API key. Manual.
- AI visibility criteria (AV01 to AV10): need LLM prompts, which the framework excludes from the scoring pipeline. Run the prompt battery manually per master-AV.md protocol.
- Social platform criteria (SC02, SC05, SC06, SC20): platform APIs are gated. Manual.

## Getting a free PSI API key
1. Go to console.cloud.google.com, create or pick a project.
2. Enable "PageSpeed Insights API" (APIs & Services, Library).
3. Create an API key (APIs & Services, Credentials). Takes about two minutes.

Without a key the script still runs and simply skips the PSI-dependent criteria.

## Running it
```
py companion.py --url https://brand.com --product-url https://brand.com/models/x --psi-key YOUR_KEY
```
Output: `[brand-domain]-companion-[date].json` with two blocks, `answers` (the pre-filled criteria) and `evidence` (one line per criterion recording what was fetched and why the answer landed, paste-ready for reports).

## Importing into the calculator
Open `index.html`, go to the Summary tab, click Import JSON, pick the companion output. Pre-filled checkboxes tick. Any criterion you had already answered keeps your answer; discarded import values are logged in the browser console (F12).

## Failure modes
- PSI down or key invalid: PSI criteria are skipped with a reason line, everything else still runs.
- Site blocks the script's user agent: affected fetch group is skipped with the HTTP status recorded.
- Heavily JS-rendered site: the HTML parser sees the pre-render page. If the homepage shows zero images or no JSON-LD, treat those results as "unknown", not "no", and check manually.
- robots.txt disallowing audit fetches does not block the script (it makes about six requests, all top-level pages); if you prefer strict robots compliance, run the affected checks manually.
