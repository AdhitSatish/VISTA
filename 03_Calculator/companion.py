"""VISTA companion evidence-gatherer.

Fills the deterministic subset of [A] criteria by fetching public data.
No LLM calls. No paid APIs. Standard library only.
Output JSON imports into the VISTA calculator (Summary tab, Import JSON).
The calculator's import rule is current-state-wins, so this prefill never
overwrites answers a researcher has already entered.

Usage:
  py companion.py --url https://brand.com [--product-url https://brand.com/models/x]
                  [--psi-key YOUR_KEY] [--out brand-companion-2026-07-08.json]

Covered criteria:
  PSI (needs --psi-key):  SV16 SV17 SV18 SV19 DE28 DE29 DE33 DE34
  Homepage HTML parse:    SV21 SV22 SV25 SV29 SV23 (Organization schema)
  Product page parse:     SV24 (Product schema, needs --product-url)
  FAQ schema:             AV20 (FAQPage schema on homepage or product page)
  Plain fetches:          SV26 (sitemap) SV27 (robots.txt) SV28 (HTTPS redirect)

Everything else stays manual. See README.md for the full skip list and why.
"""

import argparse
import json
import re
import ssl
import sys
import urllib.request
import urllib.error
from datetime import date
from html.parser import HTMLParser
from urllib.parse import urlparse, quote

UA = "Mozilla/5.0 (compatible; VISTA-companion/1.0; evidence gatherer, contact site owner for audit context)"
TIMEOUT = 20

answers = {}
evidence = {}
skipped = []


def log_fill(cid, value, why):
    answers[cid] = value
    evidence[cid] = why
    print(f"  {cid}: {'YES' if value else 'NO':<3} {why}")


def log_skip(cid, why):
    skipped.append((cid, why))


def fetch(url, method="GET"):
    """Fetch a URL, return (status, final_url, body_text or '')."""
    req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as r:
            body = "" if method == "HEAD" else r.read(2_000_000).decode("utf-8", "replace")
            return r.status, r.geturl(), body
    except urllib.error.HTTPError as e:
        return e.code, url, ""
    except Exception as e:
        return None, url, str(e)


class PageScan(HTMLParser):
    """Collects title, meta description, canonical, img alt coverage, JSON-LD blocks."""

    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.meta_desc = None
        self.canonical = False
        self.img_total = 0
        self.img_with_alt = 0
        self.jsonld = []
        self.in_jsonld = False
        self._buf = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "meta" and a.get("name", "").lower() == "description":
            self.meta_desc = a.get("content", "")
        elif tag == "link" and a.get("rel", "").lower() == "canonical":
            self.canonical = True
        elif tag == "img":
            self.img_total += 1
            if a.get("alt", "").strip():
                self.img_with_alt += 1
        elif tag == "script" and a.get("type", "") == "application/ld+json":
            self.in_jsonld = True
            self._buf = ""

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "script" and self.in_jsonld:
            self.in_jsonld = False
            try:
                self.jsonld.append(json.loads(self._buf))
            except Exception:
                pass

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_jsonld:
            self._buf += data


def jsonld_types(blocks):
    """Flatten all @type values found in JSON-LD blocks (handles @graph and lists)."""
    types = set()

    def walk(node):
        if isinstance(node, dict):
            t = node.get("@type")
            if isinstance(t, str):
                types.add(t)
            elif isinstance(t, list):
                types.update(x for x in t if isinstance(x, str))
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(blocks)
    return types


def run_psi(url, key, strategy):
    """One PageSpeed Insights call. Returns the parsed JSON or None."""
    api = ("https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
           f"?url={quote(url, safe='')}&strategy={strategy}&key={key}"
           "&category=performance&category=accessibility")
    status, _, body = fetch(api)
    if status != 200:
        return None
    try:
        return json.loads(body)
    except Exception:
        return None


def psi_criteria(url, key):
    if not key:
        for cid in ["SV16", "SV17", "SV18", "SV19", "DE28", "DE29", "DE33", "DE34"]:
            log_skip(cid, "no PSI API key supplied (--psi-key)")
        return
    print("PageSpeed Insights (mobile)...")
    mob = run_psi(url, key, "mobile")
    if not mob:
        for cid in ["SV16", "SV17", "SV18", "SV19", "DE29", "DE33", "DE34"]:
            log_skip(cid, "PSI mobile call failed")
    else:
        audits = mob.get("lighthouseResult", {}).get("audits", {})
        cats = mob.get("lighthouseResult", {}).get("categories", {})

        def metric(aid):
            a = audits.get(aid, {})
            return a.get("numericValue")

        lcp = metric("largest-contentful-paint")
        if lcp is not None:
            log_fill("SV16", lcp <= 2500, f"PSI mobile LCP = {lcp/1000:.1f}s, threshold 2.5s")
        inp = metric("interaction-to-next-paint") or metric("experimental-interaction-to-next-paint")
        if inp is not None:
            log_fill("SV17", inp <= 200, f"PSI mobile INP = {inp:.0f}ms, threshold 200ms")
        else:
            log_skip("SV17", "PSI lab data has no INP metric for this page")
        cls = metric("cumulative-layout-shift")
        if cls is not None:
            log_fill("SV18", cls <= 0.1, f"PSI mobile CLS = {cls:.3f}, threshold 0.10")
        perf = cats.get("performance", {}).get("score")
        if perf is not None:
            score = round(perf * 100)
            log_fill("SV19", score >= 60, f"PSI mobile performance = {score}, threshold 60")
            log_fill("DE29", score >= 60, f"PSI mobile performance = {score}, threshold 60")
        alt_audit = audits.get("image-alt", {}).get("score")
        if alt_audit is not None:
            log_fill("DE33", alt_audit == 1, f"Lighthouse image-alt audit score = {alt_audit}")
        contrast = audits.get("color-contrast", {}).get("score")
        if contrast is not None:
            log_fill("DE34", contrast == 1, f"Lighthouse color-contrast audit score = {contrast}")
    print("PageSpeed Insights (desktop)...")
    desk = run_psi(url, key, "desktop")
    if not desk:
        log_skip("DE28", "PSI desktop call failed")
    else:
        perf = desk.get("lighthouseResult", {}).get("categories", {}).get("performance", {}).get("score")
        if perf is not None:
            score = round(perf * 100)
            log_fill("DE28", score >= 70, f"PSI desktop performance = {score}, threshold 70")


def homepage_criteria(url):
    print("Homepage fetch + parse...")
    status, final, body = fetch(url)
    if status != 200 or not body:
        for cid in ["SV21", "SV22", "SV23", "SV25", "SV29", "AV20"]:
            log_skip(cid, f"homepage fetch failed (status {status})")
        return None
    scan = PageScan()
    scan.feed(body)
    title = scan.title.strip()
    log_fill("SV21", 0 < len(title) < 60, f"title = '{title[:70]}' ({len(title)} chars, threshold <60)")
    if scan.meta_desc is None:
        log_fill("SV22", False, "no meta description tag found")
    else:
        log_fill("SV22", 0 < len(scan.meta_desc) < 160,
                 f"meta description {len(scan.meta_desc)} chars, threshold <160")
    log_fill("SV29", scan.canonical, "canonical link tag " + ("found" if scan.canonical else "not found"))
    if scan.img_total == 0:
        log_skip("SV25", "no <img> tags found on homepage (may be JS-rendered)")
    else:
        ok = scan.img_with_alt == scan.img_total
        log_fill("SV25", ok, f"{scan.img_with_alt}/{scan.img_total} homepage images have alt text")
    types = jsonld_types(scan.jsonld)
    log_fill("SV23", "Organization" in types,
             f"JSON-LD types on homepage: {sorted(types) if types else 'none'}")
    return types


def product_criteria(product_url, home_types):
    # home_types is None when the homepage fetch failed. Only pages actually
    # scanned count as evidence; a failed fetch is a skip, never a NO.
    scanned_any = home_types is not None
    types = set(home_types or [])
    if product_url:
        print("Product page fetch + parse...")
        status, _, body = fetch(product_url)
        if status == 200 and body:
            scan = PageScan()
            scan.feed(body)
            ptypes = jsonld_types(scan.jsonld)
            log_fill("SV24", "Product" in ptypes,
                     f"JSON-LD types on product page: {sorted(ptypes) if ptypes else 'none'}")
            types |= ptypes
            scanned_any = True
        else:
            log_skip("SV24", f"product page fetch failed (status {status})")
    else:
        log_skip("SV24", "no --product-url supplied")
    if scanned_any:
        log_fill("AV20", "FAQPage" in types,
                 "FAQPage schema " + ("found" if "FAQPage" in types else "not found on scanned pages"))
    else:
        log_skip("AV20", "no page was successfully scanned, cannot judge FAQPage schema")


def plumbing_criteria(url):
    print("Sitemap / robots / HTTPS...")
    p = urlparse(url)
    root = f"{p.scheme}://{p.netloc}"
    s, _, _ = fetch(root + "/sitemap.xml", method="HEAD")
    if s is None:
        log_skip("SV26", "request for /sitemap.xml failed entirely (network), not evidence of absence")
    else:
        log_fill("SV26", s == 200, f"GET /sitemap.xml returned {s}")
    s, _, _ = fetch(root + "/robots.txt", method="HEAD")
    if s is None:
        log_skip("SV27", "request for /robots.txt failed entirely (network), not evidence of absence")
    else:
        log_fill("SV27", s == 200, f"GET /robots.txt returned {s}")
    s, final, _ = fetch(f"http://{p.netloc}/")
    if s is None:
        log_skip("SV28", "plain-http request failed entirely, could not observe redirect")
    else:
        log_fill("SV28", final.startswith("https://"),
                 f"http:// request landed on {final[:60]}")


def main():
    ap = argparse.ArgumentParser(description="VISTA companion evidence-gatherer")
    ap.add_argument("--url", required=True, help="brand homepage URL")
    ap.add_argument("--product-url", help="one product/model page URL (for SV24)")
    ap.add_argument("--psi-key", help="Google PageSpeed Insights API key (free)")
    ap.add_argument("--out", help="output JSON path")
    args = ap.parse_args()

    print(f"VISTA companion run, {date.today().isoformat()}, target {args.url}\n")
    psi_criteria(args.url, args.psi_key)
    home_types = homepage_criteria(args.url)
    product_criteria(args.product_url, home_types)
    plumbing_criteria(args.url)

    brand = re.sub(r"[^a-z0-9]+", "-", urlparse(args.url).netloc.lower()).strip("-")
    out = args.out or f"{brand}-companion-{date.today().isoformat()}.json"
    payload = {
        "schema": "vista-v1.1",
        "source": "companion.py",
        "runDate": date.today().isoformat(),
        "targetUrl": args.url,
        "answers": answers,
        "evidence": evidence,
    }
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

    print(f"\nFilled {len(answers)} criteria. Skipped {len(skipped)}:")
    for cid, why in skipped:
        print(f"  {cid}: {why}")
    print(f"\nWrote {out}")
    print("Import via calculator Summary tab, Import JSON. Existing answers are never overwritten.")


if __name__ == "__main__":
    sys.exit(main())
