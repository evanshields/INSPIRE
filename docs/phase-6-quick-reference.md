# Phase 6 Quick Reference - What You Need to Test

**⏱️ Time Estimate:** 3-5 hours total
**🎯 Your Goal:** Find bugs before we build the real app!

---

## 🚨 MUST TEST (Critical - 2 hours)

### 1. Full Application Form (90 min) ⭐ HIGHEST PRIORITY
- **Where:** Click "Full Application Form" in navigation
- **What to do:** Fill out all 17 sections
- **Look for:**
  - Can you move between sections?
  - Can you add/remove owners and guarantors?
  - Does validation work? (try skipping required fields)
  - Does data stay when you go back?
- **Write down:** Any section that doesn't work

### 2. Quick App Form (30 min)
- **Where:** Click "Quick Application" in navigation
- **What to do:** Complete all 6 steps
- **Look for:**
  - Does the progress bar update? (1→2→3→4→5→6)
  - Can you click Previous/Next?
  - Does Review step show your data?
  - Does validation catch empty fields?

### 3. Flag Manager Modal (15 min) - HIGH-001 Issue
- **Where:** Deal Detail → Analysis Tab
- **What to do:** Click the GREEN, YELLOW, and RED flag cards
- **Look for:**
  - Does each one open a popup/modal?
  - Does the modal show the right colored flags?
  - Can you close it (X button or click outside)?

---

## 📱 SHOULD TEST (High Priority - 1 hour)

### 4. Mobile Testing (45 min)
- **How:** Press F12 → Press Ctrl+Shift+M (device mode)
- **Test At:**
  - iPhone SE (375px)
  - iPhone 12 Pro (414px)
  - iPad (768px)
- **Look for:**
  - Everything fits on screen (no horizontal scroll)
  - Text is readable (not tiny)
  - Buttons aren't too small to tap

### 5. All Deal Tabs (15 min)
- **Where:** Click any deal → Top tabs
- **What to do:** Click each tab (Overview, Sizing, Documents, Analysis, Credit Memo, Exceptions, Tasks)
- **Look for:**
  - Does it switch?
  - Does content appear?

---

## ✅ NICE TO TEST (If You Have Time - 30-60 min)

### 6. Performance (15 min)
- **How:** Press F12 → Click "Network" tab → Press Ctrl+Shift+R
- **Look at:** Bottom of Network tab - how many seconds to load?
- **Expect:** Under 3 seconds

### 7. Visual Check (15 min)
- **What:** Do numbers in columns align vertically?
- **Where:** Analysis Dashboard, any tables with money amounts
- **Look for:** Numbers should line up like:
  ```
  $ 1,000
  $10,000
  $ 5,500  ← These should align
  ```

### 8. Credit Memo & Exceptions (15 min)
- **Where:** Deal Detail → Credit Memo tab and Exceptions tab
- **What to do:** Click around, click buttons
- **Look for:** Anything broken or missing

---

## 📋 How to Report Issues

**Simple Format:**
```
What: [Quick description]
Where: [Which page/section]
How bad: Critical / High / Medium / Low
What happened: [Describe]
Screenshot: [Optional - use Windows+Shift+S]
```

**Example:**
```
What: Phone number won't accept spaces
Where: Full Application Form - Section 3
How bad: Medium
What happened: I typed (305) 555-1234 and got error "Invalid format"
Screenshot: saved as phone-error.png
```

---

## 💡 Pro Tips

1. **Take Breaks** - Don't do all 3-5 hours at once!
2. **Screenshot Everything** - Windows+Shift+S is your friend
3. **Check the Console** - Press F12 and look for red errors
4. **Try to Break It** - Enter weird data, skip steps, click fast
5. **Note Good Things Too!** - Not just problems - what works well?

---

## ✅ Before You Say "I'm Done"

- [ ] Tested Full Application Form (all 17 sections)
- [ ] Tested Quick App Form (all 6 steps)
- [ ] Tested Flag Manager Modal (all 3 colors)
- [ ] Tested mobile (375px, 414px, 768px)
- [ ] Clicked all Deal tabs
- [ ] Took notes on what I found
- [ ] Took screenshots of problems

---

##  🆘 If You Get Stuck

- **App won't load?** Refresh (F5)
- **Something broke?** Refresh and start over
- **Not sure if it's a bug?** Write it down anyway!
- **Can't find something?** Check the main navigation menu

---

## 📝 Where to Save Your Results

Create a new file: `docs/phase-6-user-testing-results.md`

Start with this:

```markdown
# My Phase 6 Testing Results

**Date:** [Today's date]
**Time Spent:** [How long]

## Summary
- Tests completed: X of Y
- Bugs found: X

## What I Found

### Full Application Form
[Write what happened]

### Quick App Form
[Write what happened]

### Flag Manager Modal
[Write what happened]

... etc for each test

## Issues
1. [Issue description]
2. [Issue description]

## Overall
- What works well: [List]
- What needs fixing: [List]
- Ready for Next.js? Yes / No / Not sure
```

---

**You've got this! 🎉**

Remember: You're not expected to fix anything - just test and report what you find. Your fresh perspective is super valuable!
