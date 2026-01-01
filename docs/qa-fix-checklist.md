# QA Fix Checklist - Prioritized

**Document Version:** 1.0  
**Last Updated:** January 2026  
**Purpose:** Prioritized list of all fixes needed before Next.js conversion

---

## Overview

This checklist organizes all identified issues by priority (Critical → High → Medium → Low) with exact code fixes required.

**Total Issues:** 25+  
**Critical:** 2  
**High:** 20+  
**Medium:** 3+  
**Low:** 0+

---

## Critical Issues (Must Fix Before Conversion)

### CRIT-001: Missing `tabular-nums` in Phase 7
- **Phase:** Phase 7
- **File:** `inspire-ui-analytical.html`
- **Priority:** Critical
- **Status:** ✅ Completed
- **Description:** Numeric displays in Phase 7 do not have `tabular-nums` class
- **Impact:** Financial data may not align properly
- **Fix Required:**
  - Add `tabular-nums` class to risk score displays
  - Add `tabular-nums` class to flag count displays
  - Add `tabular-nums` class to loan amounts in credit memo
  - Add `tabular-nums` class to percentages (LTV, DSCR)
  - Add `tabular-nums` class to all numeric columns in analysis tables
- **Estimated Effort:** 30 minutes
- **Example Fix:**
  ```html
  <!-- Before -->
  <span class="text-2xl font-bold">35</span>
  
  <!-- After -->
  <span class="text-2xl font-bold tabular-nums">35</span>
  ```

### CRIT-002: Missing ARIA Attributes
- **Phase:** All phases (1-8)
- **File:** `inspire-ux.html`, `inspire-ui-analytical.html`
- **Priority:** Critical
- **Status:** ⚠️ Pending
- **Description:** Missing ARIA attributes for accessibility compliance (WCAG 2.1 AA)
- **Impact:** Accessibility compliance issues
- **Fix Required:**
  - Add `aria-required="true"` to all required form fields
  - Add `aria-describedby` linking errors to inputs
  - Add `aria-expanded` to dropdowns/accordions
  - Add `aria-selected` to tabs
  - Add `aria-label` to icon-only buttons
- **Estimated Effort:** 2-3 hours
- **Example Fixes:**
  ```html
  <!-- Required field -->
  <input type="text" id="sponsor-name" required aria-required="true" aria-describedby="sponsor-name-error">
  
  <!-- Dropdown -->
  <button aria-expanded="false" aria-haspopup="true">Menu</button>
  
  <!-- Tab -->
  <button role="tab" aria-selected="true">Tab Name</button>
  
  <!-- Icon button -->
  <button aria-label="Close modal">
    <svg>...</svg>
  </button>
  ```

---

## High Priority Issues (Fix During Conversion)

### HIGH-001: Flag Manager Modal Functionality Verification
- **Phase:** Phase 7
- **File:** `inspire-ui-analytical.html`
- **Priority:** High
- **Status:** ⚠️ Pending Verification
- **Description:** Flag Manager Modal exists but functionality needs verification
- **Impact:** Feature may not work as expected
- **Fix Required:** Verify modal functionality through manual testing (Phase 5)
- **Estimated Effort:** 30 minutes (testing)

### HIGH-002: Spacing Inconsistencies
- **Phase:** All phases
- **File:** `inspire-ui-analytical.html`
- **Priority:** High
- **Status:** ⚠️ Minor Issues
- **Description:** Minor spacing inconsistencies across phases
- **Impact:** Visual consistency
- **Fix Required:** Standardize spacing during Next.js conversion
- **Estimated Effort:** 1 hour

### HIGH-003: Typography Inconsistencies
- **Phase:** All phases
- **File:** `inspire-ui-analytical.html`
- **Priority:** High
- **Status:** ⚠️ Minor Issues
- **Description:** Minor typography inconsistencies across phases
- **Impact:** Visual consistency
- **Fix Required:** Standardize typography during Next.js conversion
- **Estimated Effort:** 1 hour

### HIGH-004: Component Pattern Mismatches
- **Phase:** All phases
- **File:** `inspire-ui-analytical.html`
- **Priority:** High
- **Status:** ⚠️ Minor Issues
- **Description:** Some custom components should use ShadCN patterns
- **Impact:** Code consistency
- **Fix Required:** Replace with ShadCN components during Next.js conversion
- **Estimated Effort:** 2-3 hours

---

## Medium Priority Issues (Fix Post-Conversion)

### MED-001: Performance Optimizations
- **Phase:** All phases
- **Priority:** Medium
- **Status:** ⚠️ Not Yet Tested
- **Description:** Performance testing not yet completed
- **Impact:** User experience
- **Fix Required:** Performance testing in Phase 5 (Claude Code manual testing)
- **Estimated Effort:** TBD

### MED-002: Advanced Accessibility Features
- **Phase:** All phases
- **Priority:** Medium
- **Status:** ⚠️ Not Yet Implemented
- **Description:** Skip links, enhanced landmark regions, improved focus management
- **Impact:** Accessibility compliance
- **Fix Required:** Implement during Next.js conversion
- **Estimated Effort:** 2-3 hours

### MED-003: Responsive Design Refinements
- **Phase:** All phases
- **Priority:** Medium
- **Status:** ⚠️ Visual Testing Needed
- **Description:** Responsive breakpoints defined, visual testing needed
- **Impact:** Mobile user experience
- **Fix Required:** Visual testing in Phase 5 (Claude Code manual testing)
- **Estimated Effort:** TBD

---

## Fix Implementation Order

### Step 1: Critical Fixes (Before Phase 3)
1. ✅ CRIT-001: Add `tabular-nums` to Phase 7 numeric displays
2. ✅ CRIT-002: Add missing ARIA attributes across all phases

### Step 2: Verification (Phase 4)
1. ✅ Re-run agent reviews on fixed files
2. ✅ Verify all critical issues resolved
3. ✅ Check for regressions

### Step 3: Manual Testing (Phase 5)
1. ✅ HIGH-001: Verify Flag Manager Modal functionality
2. ✅ MED-001: Performance testing
3. ✅ MED-003: Responsive design visual testing

### Step 4: During Next.js Conversion
1. ✅ HIGH-002: Standardize spacing
2. ✅ HIGH-003: Standardize typography
3. ✅ HIGH-004: Replace custom components with ShadCN
4. ✅ MED-002: Implement advanced accessibility features

---

## Issue Tracking

| Issue ID | Priority | Status | Phase | File | Estimated Effort |
|----------|----------|--------|-------|------|-----------------|
| CRIT-001 | Critical | ⚠️ Pending | Phase 7 | inspire-ui-analytical.html | 30 min |
| CRIT-002 | Critical | ⚠️ Pending | All | inspire-ux.html, inspire-ui-analytical.html | 2-3 hours |
| HIGH-001 | High | ⚠️ Pending Verification | Phase 7 | inspire-ui-analytical.html | 30 min |
| HIGH-002 | High | ⚠️ Minor Issues | All | inspire-ui-analytical.html | 1 hour |
| HIGH-003 | High | ⚠️ Minor Issues | All | inspire-ui-analytical.html | 1 hour |
| HIGH-004 | High | ⚠️ Minor Issues | All | inspire-ui-analytical.html | 2-3 hours |
| MED-001 | Medium | ⚠️ Not Yet Tested | All | - | TBD |
| MED-002 | Medium | ⚠️ Not Yet Implemented | All | - | 2-3 hours |
| MED-003 | Medium | ⚠️ Visual Testing Needed | All | - | TBD |

---

## Notes

- **Critical issues** must be fixed before Next.js conversion
- **High priority issues** should be fixed during Next.js conversion
- **Medium priority issues** can be fixed post-conversion
- All fixes should be verified in browser after implementation
- Update this checklist as fixes are completed

---

*End of QA Fix Checklist*

