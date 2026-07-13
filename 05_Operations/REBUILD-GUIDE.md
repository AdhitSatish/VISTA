# VISTA Rebuild Guide
**Purpose:** Complete step-by-step instructions to set up and run VISTA from scratch on any machine.

If you have `index.html`, you already have the tool. This guide covers setup, verification, and optional enhancements.

---

## What You Need

**Mandatory:**
- `VISTA/03_Calculator/index.html` - the entire calculator
- A Chromium-based browser (Chrome, Edge, Brave, Arc)

**Optional but recommended:**
- `VISTA/03_Calculator/verify.py` - math verification script
- `VISTA/03_Calculator/companion.py` - auto-fill for [A] criteria
- Python 3.9+ (for verify.py and companion.py)
- The full `01_Framework/` directory (for methodology reference)

**Nothing else.** No npm. No build step. No internet connection required.

---

## Step 1: Copy the Files

Copy the entire `VISTA/` folder to your machine. Suggested path:
```
C:\Users\YourName\Documents\VISTA\
  00_README.md
  01_Framework\
  02_Benchmarks\
  03_Calculator\
    index.html
    verify.py
    companion.py
    README.md
  04_Assessments\
  05_Operations\
```

Open the folder in Obsidian if you use it for the framework notes.

---

## Step 2: Open the Calculator

1. Navigate to `03_Calculator\`
2. Double-click `index.html`
3. It opens in your default browser

**If it opens in Edge but you want Chrome:** right-click > Open with > Google Chrome

The tool loads entirely from the local file. You will see:
- Header: `VISTA CALCULATOR` (VISTA in orange, CALCULATOR in white)
- Tab bar: SEARCH | AI | WEBSITE | AUTHORITY | SOCIAL | REPUTATION | SUMMARY
- Status: `195 CRITERIA - 49/27/38/26/28/27`

If the status bar shows a red X or assertion error in the browser console, something is wrong with the file.

---

## Step 3: Verify the Math (recommended after any edit)

```
py "path\to\VISTA\03_Calculator\verify.py"
```

Expected output:
```
RESULT: 75 ok, 0 fail
```

Run this every time you edit `index.html`. Do not skip.

---

## Step 4: Run Your First Assessment

### 4a. Set Brand Metadata (Summary tab)
- Brand name, country, sector, launch year
- Assessment date (auto-filled to today)
- Toggle applicability flags for this brand:
  - Physical Location (has a store/office/venue)
  - Physical Products (sells physical goods)
  - Specialised Product Variant (has a sub-range or premium tier)
  - Bookable Experience (test drive / demo / consultation)

### 4b. Work Through Each Dimension Tab
- Left to right: SV, AV, DE, BA, SC, RC
- Each criterion shows: framework label, plain-English hint, evidence record prompt
- Input types:
  - Yes / No / N/A (binary criteria)
  - 1-5 scale (maturity criteria, look for [M] tag)
  - Absent / Sponsored / Earned (BA authority criteria)
  - Checkboxes (SV03 social platform presence)
- Click `+ evidence note` to add a URL or observation
- Sub-components collapse/expand by clicking the header

### 4c. SC Tab: Enter Social Data First
Before answering SC criteria:
1. Select the primary platform from the dropdown
2. Enter Instagram followers and Facebook followers
3. Fill in the last 10 posts (shares, saves, comments, likes per post)
4. The engagement rate calculates automatically

### 4d. Confirm Each Dimension
Click the CONFIRM button at the bottom of each tab when done. This locks in the score and updates the radar chart.

### 4e. View Results (Summary tab)
- 6 dimension scores + composite
- Maturity band (Invisible / Emerging / Developing / Established / Leading)
- Radar chart
- Red flag panel (if any conditions triggered)

### 4f. Export
Click `Export JSON` to download a `.json` file named `{brand}-{date}.json`. This is the permanent record.

Click `Print / PDF` to generate a printable version.

---

## Step 5: Import a Previous Assessment

1. Click `Import JSON` on the Summary tab
2. Select a `.json` file exported from this tool
3. The file is loaded with current-state-wins rule:
   - Already-answered criteria are NOT overwritten
   - Empty fields are filled from the import
4. Check the browser console for any skipped imports

---

## Editing the Calculator

All logic is in `index.html`. It is a single file. Edit it in any text editor (VS Code recommended).

**File structure inside index.html:**
```
Line 1:         Attribution comment
Line 5:         <title>
Line 7-350:     <style> - all CSS
Line 365-375:   <body> - header + tabs + main structure
Line 380-500:   Pattern definitions (M-scale anchor texts)
Line 500-780:   CRITERIA array (all 195 criteria)
Line 780-800:   APPLICABILITY_FLAGS + FLAG_DISPLAY + CRIT_FLAGS
Line 800-950:   Scoring engine functions
Line 950-970:   State object
Line 970-1100:  Render functions (tabs, sub-components)
Line 1100-1220: Criterion card renderer
Line 1220-1330: Input widget renderer (renderInput)
Line 1330-1420: SC social inputs renderer
Line 1420-1550: Radar SVG renderer
Line 1550-1650: Summary renderer
Line 1650-1730: Export JSON
Line 1730-1850: Import JSON (wireImport)
Line 1850-1900: Startup (renderAll, wireImport, assertions)
```

**After any edit:** run `py verify.py` and confirm 75/75 before using for a real assessment.

---

## Adding a New Criterion

1. Find the correct section in the CRITERIA array (by dimension + sub-component)
2. Add the criterion object with all required fields (see MASTER-TECHNICAL-SPEC.md section 4)
3. Update `criteriaInSubComponent` on ALL criteria in the same sub-component
4. Update the assertion at the top of verify.py if counts change
5. Run verify.py - must pass

---

## Fixing a Hint

Search for the criterion ID (e.g. `SV23`) in index.html. The hint is the `hint:` field on the same line. Edit the string directly.

---

## Changing the Scoring Math

The scoring engine is in the `buildPointsModel`, `critValue`, `dimensionScore`, `composite` functions. Any change there must:
1. Be mirrored in verify.py's Python equivalents
2. Pass all 75 checks before use

---

## Hosting on a Web Server (for multi-user access)

The tool runs as-is on any static host (Netlify, GitHub Pages, S3, any web server). No server-side code needed.

1. Upload `index.html` to the host
2. Access via HTTPS URL
3. Add auth layer if needed (Netlify Identity, Cloudflare Access, etc.)

For a full SaaS version with saved assessments per user, you would need a backend (database for answers, user authentication). The JSON export/import format is the data model - a backend would store these JSON objects per user.

---

## Companion Script (Auto-Fill)

```
py companion.py --url https://brand.com --psi-key YOUR_FREE_KEY
```

Get a free PSI key from Google Cloud Console (enable PageSpeed Insights API).

Output file: `brand-companion-YYYY-MM-DD.json` - import into the calculator via Import JSON.

---

*Maintained by Adhit Satish. Last updated: 2026-07-10.*
