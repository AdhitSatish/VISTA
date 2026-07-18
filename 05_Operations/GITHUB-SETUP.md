# VISTA GitHub Setup Guide
**Do this today. Every minute counts for establishing timestamp.**

---

## Option A: Private Repo (Do This First, Takes 5 Minutes)

A private repo creates a cryptographically timestamped record of your authorship. Even if you never make it public, this timestamp is your strongest proof.

### Step 1: Install Git (if not installed)
Download from git-scm.com. Run the installer with default settings.

### Step 2: Create a Private GitHub Repo
1. Go to github.com, log in with your personal account (NOT your work email)
2. Click + > New repository
3. Name it: `vista-framework` or `VISTA`
4. Set to **Private**
5. Do NOT initialize with README (you have your own)
6. Click Create repository

### Step 3: Initialize and Push From Your Personal PC

Copy the VISTA folder to your personal PC first (USB drive, personal Google Drive, AirDrop, or just copy via OneDrive to personal account).

Then open a terminal (Command Prompt or PowerShell) in the VISTA folder:

```bash
# Navigate to the folder
cd "C:\Users\YourName\Documents\VISTA"

# Initialize git
git init

# Set your personal identity (use personal email, not work email)
git config user.email "adhitsatish@gmail.com"
git config user.name "Adhit Satish"

# Stage everything
git add .

# Initial commit - this is your timestamp
git commit -m "VISTA v1.1 - initial commit. Methodology and instrument authored by Adhit Satish, 2026."

# Add remote (replace URL with your actual repo URL from GitHub)
git remote add origin https://github.com/YOUR_USERNAME/VISTA.git

# Push
git branch -M main
git push -u origin main
```

That's it. You now have a private, timestamped GitHub repository under your personal account.

---

## Option B: Go Public (Establishes Prior Art, Prevents Anyone Else Claiming It)

Once on your personal PC and after the private push, you can optionally make it public.

**The case for going public:**
- Adfactors PR cannot privately claim ownership of something publicly published under your name
- GitHub timestamps are public and irrefutable
- The LICENSE file clearly marks it as proprietary (not free to use commercially)
- Anyone who copies it is in violation of your license, giving you legal standing

**The case for keeping it private:**
- Competitors cannot see implementation details
- You have full control over who sees the code

**Recommendation:** Start private. Once you are fully clear of Adfactors (resigned and settled), make it public with the proprietary license. The public timestamp is your best defense.

To make public: Settings > Danger Zone > Change repository visibility > Make public.

---

## Option C: Zip Transfer (No Git, Fastest)

If you just want to move files to your personal PC right now:

1. Open File Explorer
2. Navigate to the VISTA folder
3. Right-click > Send to > Compressed (zipped) folder
4. Name it: `VISTA-v1.1-2026-07-10.zip`
5. Copy to USB drive, personal Google Drive, or email to your personal Gmail

This is the quickest backup. Do it in parallel with the GitHub setup.

---

## What to Keep, What to Leave Behind

**Copy everything in `VISTA/`** - it's all yours.

**Do NOT copy from the company's shared drives:**
- Any client files or research that belongs to them
- Any Adfactors PR strategy documents
- Anything that is their work product, not yours

VISTA itself (the framework MD files, the calculator HTML, the verify.py) is entirely your creation. Copy all of it.

---

## After You're Set Up

Run this to confirm the repo is clean:
```bash
git status
git log --oneline
```

You should see your initial commit with today's date and time. Screenshot this. It's your proof.

---

## Ongoing: Keep It Updated

Every time you make a meaningful change to VISTA:
```bash
git add .
git commit -m "Brief description of change"
git push
```

Each commit is timestamped. Your development history becomes part of your authorship record.

---

*Set up your private repo today before anything else.*
