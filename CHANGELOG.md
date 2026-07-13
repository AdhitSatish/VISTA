# VISTA Calculator Changelog

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
