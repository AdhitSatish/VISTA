# VISTA Licensing and Ownership Strategy
**Author:** Adhit Satish
**Created:** 2026-07-10

---

## Authorship

VISTA (Visibility Intelligence & Strategic Trust Assessment) was conceived, designed, and built by **Adhit Satish**.

- Framework methodology: designed 2026
- Calculator: built and shipped 2026
- Attribution line embedded in the tool: `"VISTA v1.1. Methodology and instrument authored by Adhit Satish."`
- Attribution comment in source: line 1 of `index.html`

---

## Employment IP Consideration

VISTA was developed while Adhit Satish was employed at Adfactors PR Pvt Ltd. This creates a nuance worth being explicit about.

**Why this matters:**
In most employment contracts, work created by an employee that is:
(a) related to the employer's business, AND
(b) created using company time or resources

... may be treated as belonging to the employer (work-made-for-hire doctrine, or equivalent in your jurisdiction).

VISTA is a digital audit tool for PR/digital agency use - directly relevant to Adfactors PR's business. It was shared with colleagues via work email.

**Recommended steps before commercializing externally:**
1. Read your employment contract, specifically the IP assignment and confidentiality clauses
2. Consider having a direct conversation with your manager: "I built this as a personal project. I'd like to be clear that I retain ownership and may develop it further outside the company."
3. If they agree, get that in writing (even an email confirmation is useful)
4. If the contract assigns IP to the employer, you may need to negotiate a carve-out or exit clause

**What you can do right now without risk:**
- Keep personal copies of all files
- Continue developing VISTA on personal equipment and time
- Document your authorship
- Plan your commercial model

**What to avoid until cleared:**
- Publicly selling or licensing VISTA to third parties
- Publishing it under your name in ways that directly compete with Adfactors PR
- Claiming it as a product of a separate business entity while still employed there

---

## Commercial Model Options

### Option 1: Assessments as a Service
You run VISTA audits yourself and charge clients for the deliverable (the assessment report + recommendations).

- No licensing complexity needed
- You control quality
- Revenue: per-assessment fee (suggested range: $500-$2,500 per brand depending on scope)
- VISTA is your methodology; clients buy the insight, not the tool

### Option 2: Licensed Tool (File-Based)
Sell or license access to `index.html` to other researchers or agencies.

- Clients pay for the right to use the tool
- Could be a one-time fee or annual renewal
- The single-file design is perfect for this: hand them one file
- Revenue: $200-$500/year per license
- Risk: hard to enforce; clients can share the file
- Protection: the attribution embedded in the source, and a separate license agreement document

### Option 3: SaaS (Hosted, Auth-Gated)
Host VISTA on a web server with user authentication. Clients log in, run assessments, access their history.

- Requires backend: database, auth, hosting
- Clients pay monthly (suggested: $50-$200/month per seat)
- You retain full control; clients never have the file
- This is the highest-value and most defensible model
- Tech stack suggestion: Next.js + Supabase (auth + database) + Vercel (hosting)
- The export JSON format is already the data model for storage

### Option 4: White-Label for Agencies
License VISTA to agencies who rebrand it and use it with their own clients.

- Agency pays for the right to run assessments under their brand
- Revenue: $1,000-$5,000/year per agency license
- Requires a formal license agreement
- Strongest fit once VISTA has a track record

### Recommended path:
Start with Option 1 (run assessments yourself). Use revenue and credibility to fund Option 3 (SaaS). Option 2 and 4 become viable once there is proven demand.

---

## How to Protect VISTA Without Registering

You do not need to register copyright to own it (in most countries, copyright attaches automatically at creation). But documentation helps prove authorship if challenged.

**Do these:**
1. Keep dated versions of `index.html` (commit to a private GitHub repository with timestamps)
2. The attribution comment on line 1 is your embedded claim
3. Email yourself a copy with the creation date in the subject line (creates a timestamped record)
4. Consider a private GitHub repo: private repos are timestamped by GitHub's servers
5. If you publish publicly, include a `LICENSE` file stating that this is proprietary, all rights reserved
6. For future clients/agencies, use a simple written agreement that names VISTA as your tool and defines what they are licensed to do

**The `LICENSE` file to add to the folder:**
```
VISTA Calculator
Copyright (c) 2026 Adhit Satish. All rights reserved.

This software and its methodology are proprietary and confidential.
Unauthorized use, distribution, or reproduction in any form is prohibited.
Contact: adhitsatish@gmail.com for licensing inquiries.
```

---

## Subscription Model - How It Would Work

If you build the SaaS version:

**Tech requirements:**
- Auth: Clerk or Supabase Auth (handles login, user management)
- Database: Supabase or PlanetScale (stores assessment JSON per user)
- Hosting: Vercel (free tier covers prototype scale)
- Payments: Stripe (subscriptions, invoicing)
- Domain: vistaaudit.com or similar

**Tier example:**
| Tier | Price | Assessments/month | Users |
|------|-------|-------------------|-------|
| Solo | $49/mo | 3 | 1 |
| Agency | $199/mo | Unlimited | 5 |
| Enterprise | Custom | Unlimited | Unlimited |

**Migration from file-based to SaaS:**
The current tool's JSON export format becomes the database record format. The UI stays the same. You add a login screen and an assessment history/dashboard page. The core `index.html` logic is essentially unchanged - it just reads/writes to a database instead of to a local file.

---

## Migration Checklist (Personal PC)

- [ ] Copy `VISTA/` folder from OneDrive to personal machine
- [ ] Confirm `index.html` opens and runs (double-click in Chrome)
- [ ] Run `py verify.py` - must show `75 ok, 0 fail`
- [ ] Copy `.json` exports from `04_Assessments/` if any exist
- [ ] Open the vault in Obsidian on personal machine
- [ ] Remove from work OneDrive (or leave a copy - this is your call based on IP discussion above)
- [ ] Set up a private GitHub repo: `git init`, `git add .`, `git commit -m "VISTA v1.1"`
- [ ] Push to private repo (this timestamps and backs up your work)

---

*Maintained by Adhit Satish. Last updated: 2026-07-10.*
