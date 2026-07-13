# VISTA Subscription Protection Strategy
**The honest professional answer to: "how do I stop people copying my HTML?"**

---

## The Core Problem

VISTA is a single HTML file. Anyone who receives it can hit F12 or View Source and read every line. There is no technical barrier that is truly unbreakable. A determined developer could read the source and rebuild the UI in a weekend.

This sounds like a fatal flaw. It is not - and here is why.

---

## What Actually Protects a Software Product

Protection comes in three layers, in order of strength:

### Layer 1: The Moat Is the Methodology, Not the Code

The HTML is a UI. It is the container. What makes VISTA valuable is:
- 195 carefully researched criteria with plain-language hints
- The scoring logic (zero-anchoring, renormalization, tri-state, inverted criteria)
- The red flag definitions and thresholds
- The 5+ hours of structured research discipline the tool enforces
- The author's credibility and track record behind the assessments

A developer can copy the HTML in a weekend. They cannot copy the 2 years of thinking about what to measure, why, and how. They certainly cannot claim the methodology belongs to them.

The MD files in `01_Framework/` are MORE valuable IP than the HTML. Protect those too.

### Layer 2: Legal Protection (License + Copyright)

- Copyright attaches automatically at creation. You own it.
- The LICENSE file makes the terms explicit: source visible, commercial use prohibited without permission.
- A license agreement that users must accept before using creates a contractual relationship.
- Even if someone copies the code, they are in violation of your license. You can send a cease-and-desist.
- You do not need to register copyright in most countries (including Sri Lanka) for it to be enforceable, but registration (if available in your jurisdiction) makes enforcement much simpler.

### Layer 3: Technical Obfuscation (For Distributed Copies)

If you distribute VISTA as a file (per-license model), obfuscate the JavaScript before distribution.

**Tool: javascript-obfuscator**
```bash
npm install -g javascript-obfuscator
javascript-obfuscator index.html --output index.dist.html
```

What obfuscation does:
- Renames all variables and functions to gibberish (`a1b2`, `_0x3f7e`, etc.)
- Removes all comments
- Adds dead code and anti-debugging traps
- Makes reverse engineering a multi-day professional effort instead of a weekend project

You keep `index.html` (the readable source). You distribute `index.dist.html` (the obfuscated copy).

**Limitation:** A skilled engineer can still deobfuscate with enough effort. This is a deterrent, not a lock.

---

## The Strongest Protection: SaaS (Never Distribute the File)

If VISTA runs on a server you control and users access it through a browser, they never get the file. They get a rendered interface. No file = nothing to copy.

**How this works:**
1. Host VISTA on a server (Vercel, Netlify, AWS, your own VPS)
2. Add authentication (Clerk, Auth0, Supabase Auth)
3. Users log in with email + password
4. They get access to the tool through a URL, not a file
5. Their assessment data lives in a database you control
6. Cancel their subscription = their access ends immediately

This is the model that companies like Ahrefs, SEMrush, and Screaming Frog use. You never ship the code. You ship access.

**Tech required to build this:**
- Frontend: the current `index.html` logic, ported to React or kept as-is
- Auth: Clerk (easiest, free tier available) or Supabase Auth
- Database: Supabase or PlanetScale (store assessments as JSON per user)
- Hosting: Vercel (free tier handles prototype scale)
- Payments: Stripe (subscriptions, $49-$199/mo tiers)
- Domain: vistaaudit.io or similar (check availability)

Estimated cost to build MVP SaaS: 2-3 weeks of development, ~$0-20/month hosting at small scale.

---

## On the Specific Adfactors Question

You are asking: if I share VISTA with clients, will Adfactors see it, copy it, and launch a competing product?

**Realistic assessment:**
1. They already have an older version of the HTML from July 7
2. They do not have v1.1 with all the features, but they have enough to see the concept
3. Building a competing tool would require them to: understand the methodology, hire a developer, maintain it, market it, and compete with you
4. PR agencies are not software companies. Their incentive is to use a tool, not to build one.
5. The more pressing risk is not that they build a clone - it is that they keep using the old version without paying you. That is a licensing violation once you have a license in place.

**What to do about it:**
- Send them a formal notice when you launch VISTA commercially: "VISTA is now a licensed product. Continued use of any version requires a license."
- Offer them a founding client rate (goodwill, and it converts them from a threat to a paying customer)
- The public GitHub with your name and a timestamp on it is your insurance policy

---

## The Open Source Question: Should You Publish on GitHub?

**Short answer: Yes - but with a proprietary license, not MIT or Apache.**

"Open source" has a specific meaning: free to use, modify, and distribute. That is NOT what you want.

What you want is "source available": the code is visible, but commercial use requires permission from you.

**Why publish at all?**
1. **Prior art.** A public GitHub repo with your name and a July 2026 timestamp is irrefutable proof that you created VISTA. Adfactors cannot counter this.
2. **Credibility.** For a methodology product, showing your work builds trust with buyers.
3. **License enforcement.** Once it is public with a clear license, anyone using it commercially is visibly in violation. This gives you legal standing.
4. **Discoverability.** Potential clients or agency partners can find it.

**What license to use:**

| License | What It Means | Good For VISTA? |
|---------|--------------|-----------------|
| MIT / Apache 2.0 | Free to use, modify, redistribute commercially | NO - gives it away |
| GPL v3 | Free to use but derivatives must also be open | NO - still gives it away |
| Business Source License (BSL 1.1) | Source available, converts to open source after X years | Maybe - complex |
| Commons Clause + Apache | Source available, no commercial use | YES |
| Custom proprietary | Source visible, all commercial rights reserved | YES - what is in your LICENSE file |

**The license in your LICENSE file is correct.** Keep it.

**Publication sequence:**
1. Today: push to PRIVATE GitHub (timestamp secured)
2. When you resign and are fully clear: make it public
3. When you launch commercially: add a license acceptance screen to the tool itself

---

## License Acceptance Screen (Add to the Tool)

Before the tool loads, show a modal:

```
VISTA v1.1 - Visibility Intelligence & Strategic Trust Assessment
Copyright (c) 2026 Adhit Satish. All rights reserved.

This software is licensed, not sold. By clicking "I Agree", you confirm that:
- You are using this tool under a valid license from Adhit Satish
- You will not redistribute this software or methodology without written permission
- Commercial use requires a separate commercial license

[ I Agree ] [ Learn More ]
```

This creates a click-wrap agreement. It is legally enforceable as a contract in most jurisdictions.

---

## Summary: What to Do in Order

1. **Today:** Copy VISTA to personal PC + push to private GitHub. This is your timestamp.
2. **When you leave Adfactors:** Make the GitHub repo public with the current proprietary license.
3. **When you have 2-3 paying clients:** Build the SaaS version. Never distribute the file again.
4. **When you have enough clients:** Hire a lawyer to draft a proper EULA and formalize the licensing.

The file-based model works at small scale (under 10 clients). The SaaS model is where you need to be at any meaningful scale. Every month you stay on the file-based model is a month someone could share your file. Every month on SaaS is a month you have perfect control.

---

*Written for Adhit Satish, VISTA author. 2026-07-10.*
