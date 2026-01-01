# Phase 6: Browser Testing Guide for INSPIRE HTML Prototype

**For:** User Manual Testing
**Purpose:** Test the HTML prototype in your browser before converting to Next.js
**Time Needed:** 3-5 hours total
**Your Experience Level:** Beginner-friendly - No coding required!

---

## 📋 What You'll Be Doing

You'll be opening the HTML prototype in your web browser and testing it like a real user would. You're looking for:
- ✅ Things that work correctly
- ❌ Things that don't work or look wrong
- 💡 Things that could be improved

**Don't worry!** You don't need to fix anything - just test and write down what you find.

---

## 🚀 Getting Started (5 minutes)

### Step 1: Open the Prototype

1. **Find the file**: Navigate to `C:\Users\evana\inspire\inspire-ui-analytical.html`
2. **Open in browser**: Right-click the file → Open with → **Google Chrome** (recommended)
3. **Bookmark it**: Press `Ctrl+D` to bookmark for easy access

### Step 2: Open Browser DevTools (for later)

1. Press `F12` on your keyboard (this opens Developer Tools)
2. Click the **Console** tab - you'll check this for errors
3. Click the **Network** tab - you'll use this for performance testing
4. You can close DevTools for now (press `F12` again)

### Step 3: Prepare to Take Notes

Open a new document (Word, Notepad, Google Docs) to write down:
- What you're testing
- What you expected to happen
- What actually happened
- Screenshots (use Windows+Shift+S to take screenshots)

---

## ✅ CRITICAL PRIORITY TESTING (Must Do - 2-3 hours)

### Test 1: Full Application Form (90-120 minutes) ⚠️ MOST IMPORTANT

**Why this matters:** This is the most complex part and highest risk for bugs.

**What to do:**

1. **Start the form:**
   - Look for a link/button to "Full Application Form" in the navigation
   - Click it to start

2. **Complete ALL 17 sections one by one:**
   - Fill in every required field (marked with red asterisk *)
   - Try to click "Next" or navigate to the next section
   - Make sure the form lets you continue

3. **Test specific features:**

   **A. Ownership Table (if you see one):**
   - Click "Add Owner" or similar button
   - Fill in owner details
   - Click "Remove" on an owner
   - Verify it works correctly

   **B. Add/Remove Co-Guarantor:**
   - Look for "Add Guarantor" or "Add Co-Guarantor" button
   - Click it - does a new section appear?
   - Fill it in
   - Try to remove it
   - Does it work?

   **C. Validation Testing:**
   - Try clicking "Next" with empty required fields
   - Does it show an error message?
   - Does it prevent you from continuing?
   - Screenshot any error messages

   **D. Data Persistence:**
   - Fill in Section 1
   - Go to Section 2
   - Click "Back" or "Previous" to Section 1
   - Is your data still there?

4. **Submit the form:**
   - Fill in all sections
   - Click the final "Submit" button
   - What happens?

**What to write down:**
- ✅ Sections that worked perfectly
- ❌ Sections that had errors or didn't work
- ⚠️ Sections that were confusing
- 📝 Any error messages you saw
- 📸 Screenshots of any problems

**EXAMPLE NOTES:**
```
Section 3 - Borrower Info:
✅ All fields filled in correctly
❌ Phone number field doesn't accept (555) 555-5555 format
⚠️ Not sure what "Liquidity" means - maybe add help text?
📸 Screenshot saved: error-phone-format.png
```

---

### Test 2: Quick App Form (30 minutes)

**Why this matters:** This is the main public-facing form.

**What to do:**

1. **Find the Quick App Form** (6-step wizard)
2. **Complete all 6 steps:**
   - Step 1: Contact Info
   - Step 2: Loan Details
   - Step 3: Property Info
   - Step 4: Entity
   - Step 5: Assets & Guarantor
   - Step 6: Review

3. **Watch for:**
   - Does the progress stepper (1-2-3-4-5-6 at top) update as you progress?
   - Do Previous/Next buttons work?
   - Does the Review step show all your data correctly?
   - Can you click to edit from the Review step?

4. **Try to break it:**
   - Leave required fields empty and click Next - does it prevent you?
   - Enter invalid email (like "notanemail") - does it catch it?
   - Enter letters in the phone number - what happens?

**What to write down:**
- Did all 6 steps work?
- Did validation work properly?
- Did the progress indicator update?
- Any bugs or errors?

---

### Test 3: Flag Manager Modal (15 minutes) - HIGH-001

**Why this matters:** This was a specific issue we needed to verify.

**What to do:**

1. **Navigate to Deal Detail:**
   - Find "Pipeline" or "Deals" in navigation
   - Click on any deal card
   - This should open the Deal Detail view

2. **Go to Analysis Tab:**
   - Click the "Analysis" tab (might have a small "1" badge)

3. **Test the Flag Cards:**
   - You should see 3 colored cards: Green, Yellow, Red (with numbers like "28", "5", "2")
   - **Click the GREEN card** → Does a modal/popup open showing green flags?
   - **Close the modal** → Click X or click outside - does it close?
   - **Click the YELLOW card** → Does modal open showing yellow flags?
   - **Close it**
   - **Click the RED card** → Does modal open showing red flags?
   - **Close it**

4. **Check the browser console:**
   - Press F12
   - Look at the Console tab
   - Are there any red error messages?
   - Screenshot any errors

**What to write down:**
- ✅ Which color cards opened modals successfully
- ❌ Which ones didn't work
- 📝 Any console errors (copy the exact text)
- 📸 Screenshots of the working modals

---

## 🎯 HIGH PRIORITY TESTING (Should Do - 1-2 hours)

### Test 4: Mobile Responsive (60 minutes) - MED-003

**Why this matters:** Many users will access on phones/tablets.

**How to test mobile without a phone:**

1. **Open Chrome DevTools:**
   - Press `F12`
   - Press `Ctrl+Shift+M` (this is "Toggle Device Toolbar")
   - You'll see your page in a phone-sized frame!

2. **Test at different sizes:**

   **A. iPhone SE (375px):**
   - Click the dropdown at top that says "Responsive"
   - Select "iPhone SE"
   - Navigate through the app - does everything fit?

   **B. iPhone Pro Max (414px):**
   - Select "iPhone 12 Pro" or similar
   - Check layout again

   **C. iPad (768px):**
   - Select "iPad"
   - How does it look?

3. **What to check:**
   - ✅ No horizontal scrolling (unless it's a table - those can scroll)
   - ✅ Text is readable (not too small)
   - ✅ Buttons are big enough to tap (not tiny)
   - ✅ Forms work (inputs aren't cut off)
   - ✅ Navigation menu works

**What to write down:**
- Layout issues at each size
- Things that are too small to read
- Buttons too small to tap
- Screenshots of any layout problems

---

### Test 5: Deal Detail Tabs (15 minutes)

**What to do:**

1. Navigate to any Deal Detail view
2. Click through ALL tabs:
   - Overview
   - Sizing & Quote
   - Checklist
   - Documents
   - Analysis
   - Credit Memo
   - Exceptions
   - Tasks

3. **For each tab:**
   - Does it switch when clicked?
   - Does the active tab show (usually underlined or highlighted)?
   - Does content appear?
   - Any errors?

**What to write down:**
- ✅ Tabs that worked
- ❌ Tabs that didn't work or had no content
- Any visual issues

---

### Test 6: Visual Verification (30 minutes)

**What to look for:**

1. **Number Alignment:**
   - Look at the Analysis Dashboard
   - Look at any tables with numbers
   - **Do numbers in columns line up vertically?** (They should!)
   - Example: $1,000 should align with $10,000 and $100,000

2. **Colors:**
   - Primary blue should be `#0171e2` (a bright blue)
   - Do all buttons use the same blue?
   - Are colors consistent throughout?

3. **Spacing:**
   - Does spacing look consistent?
   - Are cards evenly spaced?
   - Do margins look the same?

4. **Typography:**
   - Is text readable?
   - Are headings clearly larger than body text?
   - Does font look professional?

**What to write down:**
- Any numbers that don't align
- Color inconsistencies
- Spacing that looks off
- Screenshots of visual issues

---

## 📊 MEDIUM PRIORITY TESTING (If Time Permits - 30-60 minutes)

### Test 7: Performance (30 minutes) - MED-001

**What to do:**

1. **Clear your cache:**
   - Press `Ctrl+Shift+Delete`
   - Select "Cached images and files"
   - Click "Clear data"

2. **Open DevTools Network Tab:**
   - Press `F12`
   - Click "Network" tab
   - Check "Disable cache" checkbox at top

3. **Reload the page:**
   - Press `Ctrl+Shift+R` (hard refresh)
   - Watch the Network tab load resources

4. **Check the numbers at bottom:**
   - Look for: "Finish: X s" (total load time)
   - Should be under 3 seconds

5. **Test interactions:**
   - Click buttons - do they respond instantly?
   - Type in forms - is there any lag?
   - Switch tabs - smooth or choppy?

**What to write down:**
- Total load time (from Network tab)
- Whether the app feels fast or slow
- Any laggy interactions

---

### Test 8: Credit Memo & Exceptions (20 minutes)

**Credit Memo Tab:**
1. Navigate to Deal Detail → Credit Memo tab
2. Verify you see sections like:
   - Executive Summary
   - Borrower Analysis
   - Property Analysis
   - Deal Economics
   - Risk Assessment
3. Click "Export to PDF" or "Export to Word" buttons
   - What happens? (Might just show an alert - that's okay for prototype)

**Exceptions Tab:**
1. Navigate to Deal Detail → Exceptions tab
2. Verify you see:
   - Summary cards with numbers (Active, Pending, Approved, Denied)
   - List of exceptions
3. Click "New Exception Request" button
   - Does a modal open?

**What to write down:**
- Missing sections
- Export button behavior
- Whether modals work

---

### Test 9: Cross-Browser (Optional - 30-60 minutes)

If you have other browsers installed, test in:
- ✅ **Chrome** (already tested)
- ✅ **Firefox** (if you have it)
- ✅ **Edge** (comes with Windows)
- ✅ **Safari** (if on Mac)

**What to check:**
- Does it look the same?
- Do all features work?
- Any browser-specific bugs?

---

## 📝 How to Report Issues

### Format for Each Issue:

```markdown
## Issue #X: [Short Title]

**Where:** [Which page/section]
**Priority:** Critical / High / Medium / Low
**What I did:** [Steps you took]
**Expected:** [What should happen]
**Actual:** [What actually happened]
**Screenshot:** [filename.png or "none"]
**Browser:** Chrome / Firefox / Edge / Safari

Example:

## Issue #1: Phone Number Validation Too Strict

**Where:** Full Application Form - Section 3 - Borrower Info
**Priority:** Medium
**What I did:**
1. Entered phone number as (555) 555-5555
2. Clicked Next
**Expected:** Should accept standard phone format with parentheses
**Actual:** Shows error "Invalid phone number format"
**Screenshot:** phone-validation-error.png
**Browser:** Chrome
```

---

## ✅ Completion Checklist

Before you finish Phase 6, make sure you've:

- [ ] Tested Full Application Form (all 17 sections)
- [ ] Tested Quick App Form (all 6 steps)
- [ ] Tested Flag Manager Modal (green, yellow, red cards)
- [ ] Tested mobile responsive (375px, 414px, 768px)
- [ ] Tested all Deal Detail tabs
- [ ] Checked visual alignment (especially numbers)
- [ ] Measured performance (load time)
- [ ] Documented all issues found
- [ ] Taken screenshots of problems
- [ ] Noted what works well (not just problems!)

---

## 🎉 What Happens Next

After you complete testing:

1. **Share your findings** with the development team (Claude!)
2. **Prioritize issues** - Which must be fixed before Next.js conversion?
3. **Provide UX feedback** - What would make it better?
4. **Approve for conversion** - Is it ready to become a real app?

---

## 💡 Tips for Success

1. **Take breaks** - This is 3-5 hours of testing, don't do it all at once
2. **Be thorough** - Better to find bugs now than after conversion
3. **Be honest** - Report what you find, even if it's bad news
4. **Screenshot everything** - Pictures are worth 1000 words
5. **Ask questions** - If something is unclear, note it!

---

## 🆘 Need Help?

If you get stuck:
- **Can't find something?** Check the navigation menu or search the page
- **Something broke?** Refresh the page (F5) and try again
- **Console errors?** Copy the exact text - it helps debugging
- **Not sure if it's a bug?** Document it anyway - we'll decide later

---

## 📊 Where to Submit Your Results

Create a file: `docs/phase-6-user-testing-results.md`

Use this template:

```markdown
# Phase 6: User Browser Testing Results

**Tester:** [Your Name]
**Date:** [Date]
**Browser:** Chrome [Version]
**Time Spent:** [Hours]

---

## Summary

- **Tests Completed:** X of Y
- **Issues Found:** X
  - Critical: X
  - High: X
  - Medium: X
  - Low: X

---

## Detailed Results

### Full Application Form
[Your findings here]

### Quick App Form
[Your findings here]

### Flag Manager Modal
[Your findings here]

... etc for each test

---

## Issues Found

### Issue #1: [Title]
[Details using format above]

### Issue #2: [Title]
[Details]

---

## Overall Impressions

**What works well:**
- [List positives]

**What needs improvement:**
- [List improvements]

**Ready for Next.js conversion?** Yes / No / Needs fixes first

**Notes:**
[Any other feedback]
```

---

**Good luck with testing! You've got this! 🚀**

*Remember: You're helping make this application better for real users. Your fresh perspective as someone new to coding is actually valuable - you'll spot things developers miss!*
