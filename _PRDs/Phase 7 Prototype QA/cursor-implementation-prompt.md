** (scrollable, max-height: 500px)
   - Columns: [Checkbox] | Severity | Category | Flag Description | Status | Actions
   - Each row should display:
     - Checkbox for bulk selection
     - Severity badge (🔴 Red, ⚠️ Yellow, ✅ Green)
     - Category name
     - Flag desc# Cursor Implementation Prompt: Phase 7 HTML Prototype Fixes

**Context:** A comprehensive code review has identified critical issues and improvements needed in the Phase 7 HTML prototype (`inspire-ui-analytical.html`). This prompt provides detailed instructions for implementing all required fixes.

---

## CRITICAL PRIORITY 1: Add Missing Flag Manager Modal

**ISSUE:** The Flag Manager Modal is completely missing from the codebase, but it's referenced throughout the Analysis Dashboard.

### Implementation Requirements:

**Location:** Add after the Exception Request Modal (around line 4736 in `inspire-ui-analytical.html`)

**Modal Structure:**
```html
<!-- MODAL: FLAG MANAGER - Phase 7 -->
<div id="modal-flag-manager" class="fixed inset-0 z-50 hidden overflow-y-auto" aria-labelledby="modal-flag-manager-title" role="dialog" aria-modal="true">
```

**Required Features:**

1. **Modal Header**
   - Title: "Flag Manager"
   - Close button (X) that calls `closeModal('modal-flag-manager')`
   - Count display showing total flags

2. **Filter Toolbar** (3 dropdowns side-by-side)
   - **By Severity:** Dropdown with options: All, Red Flags, Yellow Flags, Green Flags
   - **By Category:** Dropdown with options: All, Credit, Background, Property, Valuation, Title, Insurance, Financial, Experience, Documentation
   - **By Status:** Dropdown with options: All, Open, Acknowledged, Resolved, Exception Requested, Exception Approved

3. **Flag Tableription (truncated if too long)
     - Status badge (Open, Acknowledged, Resolved, Exception Pending, etc.)
     - Actions: "Resolve" button, "Add Note" button
   - Include 10-15 sample flag rows representing the 35 total flags (2 Red, 5 Yellow, 28 Green)

4. **Bulk Actions Bar** (at bottom of modal)
   - "Bulk Acknowledge" button (calls `bulkAcknowledge()`)
   - "Export CSV" button (calls `exportFlagsCSV()`)
   - Checkbox to "Select All"

5. **Styling Requirements:**
   - Use existing modal patterns from Document Analysis Detail Modal
   - Modal should be `max-w-6xl` width (wider than standard modals)
   - Use ShadCN table styling with hover states
   - Flag severity badges should match existing badge styles from Analysis Dashboard

### JavaScript Function to Add:

```javascript
// Open Flag Manager Modal
function openFlagManager() {
    showModal('modal-flag-manager');
}
```

### Update Existing References:

**Find and update these locations:**
1. Line ~2904 (Green flag summary button): Change `onclick="filterFlags('green')"` to `onclick="openFlagManager()"`
2. Line ~2911 (Yellow flag summary button): Change `onclick="filterFlags('yellow')"` to `onclick="openFlagManager()"`
3. Line ~2918 (Red flag summary button): Change `onclick="filterFlags('red')"` to `onclick="openFlagManager()"`
4. Any "Manage Flags" buttons should call `openFlagManager()`

**Keep existing filterFlags() function** - it can be used within the modal for filtering.

---

## CRITICAL PRIORITY 2: Add Missing Credit Memo Section 5

**ISSUE:** Credit Memo jumps from Section 4 (Deal Economics, line 4016) directly to Section 6 (Risk Assessment, line 4018). Section 5 (Third-Party Reports) is completely missing.

### Implementation Requirements:

**Location:** Insert between line 4016 (end of Section 4) and line 4018 (start of Section 6)

**Section Structure:**

```html
<!-- SECTION 5: THIRD-PARTY REPORTS -->
<section class="space-y-6 border-t border-border pt-6">
    <h2 class="text-2xl font-bold text-foreground border-b border-border pb-2">5. Third-Party Reports</h2>
```

**Required Subsections:**

1. **Credit Report Summary**
   - Report date, bureau(s), FICO scores (all 3 bureaus shown)
   - Trade lines count, derogatories summary
   - Key findings (mortgage lates, bankruptcy, foreclosure status)
   - Flag reference: FICO 655 below minimum

2. **Appraisal Summary**
   - Appraiser name, company, date
   - Property type, square footage
   - As-Is Value: $425,000
   - ARV: $485,000
   - Methodology (Sales Comparison Approach)
   - Comps used (3-5 comparables)
   - Flag reference: 8% ARV variance

3. **Title Report Summary**
   - Title company, examiner, date
   - Title status: Clear/Clouded
   - Exceptions noted (standard utility easement)
   - Liens: None
   - Key findings from title search

4. **Insurance Summary**
   - Insurance company, policy number
   - Coverage amount, deductible
   - Policy term/expiration
   - Flag reference (if any): Policy renewal needed

5. **Document Status Table** (optional but recommended)
   - Table showing all third-party reports with status, date received, confidence score
   - Can reference data from Document Analysis table in Analysis Dashboard

**Content Guidelines:**
- Use realistic but consistent mock data that matches the deal (123 Main Street, Austin, TX)
- Ensure FICO scores match (655 middle score) from other sections
- Ensure ARV values match ($485,000) from other sections
- Include 2-3 flags that correspond to flags shown in Analysis Dashboard
- Use grid layouts for key metrics (similar to Section 1 Executive Summary style)
- Use tables for detailed comparables data (similar to Section 2 Borrower Analysis style)

**Styling:**
- Follow exact same spacing and typography as other credit memo sections
- Use `space-y-6` for section spacing
- Use `border-t border-border pt-6` for section separator
- Use `bg-card border border-border rounded-lg p-4` for subsection cards
- Include flag indicators where relevant (🔴, ⚠️)

---

## HIGH PRIORITY 3: Fix Minor Issues

### 3.1 Add tabular-nums Class to All Numeric Displays

**ISSUE:** Numeric values don't use `tabular-nums` class for proper alignment

**Locations to Update:**

1. **Analysis Dashboard (tab-analysis section)**
   - Line ~2894: Risk score "35" - add class `tabular-nums`
   - Lines ~2909, 2916, 2923: Flag counts (28, 5, 2) - add class `tabular-nums`
   - Line ~2938: Documents count "12 / 14" - add class `tabular-nums`
   - Line ~2950: Exceptions count "2" - add class `tabular-nums`
   - Category score displays (lines ~3775, 3786, 3797, 3808, 3819, 3830) - add class `tabular-nums`

2. **Credit Memo (tab-credit-memo section)**
   - Line ~3624: Loan Amount "$382,500" - add class `tabular-nums`
   - Line ~3649: Interest Rate "10.6%" - add class `tabular-nums`
   - Line ~3650: Term "12 Months" - add class `tabular-nums`
   - Lines ~4002, 4007, 4012: LTV/LTC/LTARV percentages - add class `tabular-nums`
   - Line ~4023: Risk score "35" - add class `tabular-nums`
   - All loan amounts, percentages, and numeric metrics throughout credit memo

3. **Exception Cards (tab-exceptions section)**
   - Lines ~3848, 3852, 3856, 3860: Exception counts - add class `tabular-nums`

**Pattern to Follow:**
```html
<!-- Before -->
<div class="text-5xl font-bold text-warning mb-2">35</div>

<!-- After -->
<div class="text-5xl font-bold text-warning mb-2 tabular-nums">35</div>
```

### 3.2 Add Missing Fields to Exception Request Modal

**Location:** Modal `modal-exception-request` (lines 4691-4736)

**Changes Required:**

1. **Add Supporting Documents Upload Field**
   - Insert after Compensating Factors section (around line 4728)
   ```html
   <div>
       <label class="block text-sm font-medium text-gray-700 mb-2">Supporting Documents</label>
       <div class="border-2 border-dashed border-gray-300 rounded-lg p-4 text-center">
           <input type="file" id="exception-docs" multiple class="hidden" accept=".pdf,.doc,.docx,.jpg,.png">
           <label for="exception-docs" class="cursor-pointer">
               <svg class="mx-auto h-12 w-12 text-gray-400" stroke="currentColor" fill="none" viewBox="0 0 48 48">
                   <path d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
               </svg>
               <p class="mt-1 text-sm text-gray-600">Click to upload or drag and drop</p>
               <p class="text-xs text-gray-500">PDF, Word, or Images up to 10MB</p>
           </label>
       </div>
       <div id="file-list" class="mt-2 text-sm text-gray-600"></div>
   </div>
   ```

2. **Add Approval Tier Display**
   - Insert before Compensating Factors section (around line 4721)
   ```html
   <div class="bg-blue-50 border border-blue-200 rounded-lg p-4">
       <div class="flex items-center justify-between">
           <div>
               <span class="text-sm font-medium text-gray-700">Required Approval Tier:</span>
           </div>
           <div>
               <span class="px-3 py-1 bg-blue-600 text-white rounded-full text-sm font-bold">Tier 2 - Portfolio Manager</span>
           </div>
       </div>
       <p class="text-xs text-gray-600 mt-2">FICO exceptions require Portfolio Manager approval (Tier 2)</p>
   </div>
   ```

---

## MEDIUM PRIORITY 4: Improve Consistency

### 4.1 Update Category Score Names (Optional - for consistency with PRD)

**Current vs. Expected:**
- Current: "Borrower" → PRD expects: "Borrower Eligibility"
- Current: "Property" → PRD expects: "Property Eligibility"
- Current: "Financial" → PRD expects: "Loan Parameters"
- Current: "Title" + "Insurance" (separate) → PRD expects: "Title & Insurance" (combined)

**Decision Required:** Choose one approach:
- **Option A:** Keep current implementation (cleaner, more concise names)
- **Option B:** Update to match PRD exactly (requires renaming 6 category cards around lines 3772-3836)

**Recommendation:** Option A - Keep current implementation. It's cleaner and the functionality is identical.

### 4.2 Consider Refactoring Document Analysis from Table to Cards (Optional)

**Current:** Document analysis is displayed as a table (lines 3600-3763)
**PRD Expects:** Individual document cards (like summary cards at top of page)

**Decision Required:**
- **Option A:** Keep table format (more compact, shows all documents at once)
- **Option B:** Refactor to card-based layout (more visual, easier to scan)

**Recommendation:** Option A - Keep table format. Tables are better for comparing multiple documents side-by-side.

---

## IMPLEMENTATION CHECKLIST

Use this checklist to track your implementation progress:

### Critical Priority
- [ ] **CRITICAL 1:** Add Flag Manager Modal with all required features
- [ ] **CRITICAL 1:** Add `openFlagManager()` JavaScript function
- [ ] **CRITICAL 1:** Update all flag summary buttons to call `openFlagManager()`
- [ ] **CRITICAL 2:** Add Credit Memo Section 5 (Third-Party Reports)
- [ ] **CRITICAL 2:** Verify Section 5 content is realistic and matches other sections

### High Priority
- [ ] **HIGH 3.1:** Add `tabular-nums` class to all risk scores
- [ ] **HIGH 3.1:** Add `tabular-nums` class to all flag counts
- [ ] **HIGH 3.1:** Add `tabular-nums` class to all document counts
- [ ] **HIGH 3.1:** Add `tabular-nums` class to all exception counts
- [ ] **HIGH 3.1:** Add `tabular-nums` class to all category scores
- [ ] **HIGH 3.1:** Add `tabular-nums` class to all credit memo numeric values (LTV, LTC, LTARV, loan amounts, etc.)
- [ ] **HIGH 3.2:** Add supporting documents upload field to Exception Request Modal
- [ ] **HIGH 3.2:** Add approval tier display to Exception Request Modal
- [ ] **HIGH 3.2:** Add file upload handler JavaScript (can be simulated)

### Medium Priority (Optional)
- [ ] **MEDIUM 4.1:** Decide on category naming convention (keep current or match PRD)
- [ ] **MEDIUM 4.2:** Decide on document analysis layout (keep table or refactor to cards)

---

## TESTING AFTER IMPLEMENTATION

After making these changes, verify:

1. **Flag Manager Modal**
   - [ ] Opens when clicking flag summary buttons
   - [ ] Displays table with all flags
   - [ ] Filter dropdowns are present (functionality can be simulated)
   - [ ] Bulk action buttons are present
   - [ ] Close button works
   - [ ] Modal styling matches other modals

2. **Credit Memo Section 5**
   - [ ] Section appears between Section 4 and Section 6
   - [ ] All subsections are present (Credit, Appraisal, Title, Insurance)
   - [ ] Data is consistent with Analysis Dashboard
   - [ ] Flags are referenced appropriately
   - [ ] Styling matches other credit memo sections

3. **Tabular Nums**
   - [ ] All numeric values use monospaced font
   - [ ] Numbers align properly in tables and lists
   - [ ] Particularly check LTV/LTC/LTARV percentages align correctly

4. **Exception Request Modal**
   - [ ] File upload area displays correctly
   - [ ] Approval tier badge displays correctly
   - [ ] Modal still functions with new fields

---

## CODE STYLE GUIDELINES

**Maintain Consistency:**
- Use existing HTML structure patterns from the file
- Follow existing spacing (4-space indentation for HTML)
- Use existing class naming conventions (Tailwind CSS utility classes)
- Match existing color schemes:
  - Red flags: `bg-red-50`, `text-red-800`, `border-red-200`
  - Yellow flags: `bg-yellow-50`, `text-yellow-800`, `border-yellow-200`
  - Green flags: `bg-green-50`, `text-green-800`, `border-green-200`
  - Cards: `bg-card border border-border rounded-lg shadow-sm`
  - Primary buttons: `bg-primary text-white hover:bg-blue-600`
  - Secondary buttons: `border border-gray-300 text-gray-700 hover:bg-gray-50`

**Accessibility:**
- Include proper ARIA attributes on modals (`role="dialog"`, `aria-modal="true"`, `aria-labelledby`)
- Ensure all interactive elements are keyboard accessible
- Use semantic HTML (`<table>`, `<th>`, `<td>` for tabular data)

**JavaScript:**
- Place new functions in the existing JavaScript section (after line 4600)
- Use existing function patterns (alert() for simulated actions)
- Keep functions simple and consistent with existing code style

---

## EXPECTED OUTCOME

After implementation, the Phase 7 HTML prototype should have:

✅ **All critical features complete:**
- Fully functional Flag Manager Modal
- Complete 7-section Credit Memo (including Section 5)

✅ **Improved visual consistency:**
- All numbers properly aligned with `tabular-nums`
- Exception Request Modal with complete fields

✅ **Ready for manual testing:**
- All automated checklist items verified
- User can proceed with browser-based manual QA

---

## QUESTIONS OR CLARIFICATIONS

If you encounter any ambiguity during implementation:

1. **For Flag Manager Modal:** Use the Document Analysis Detail Modal as a reference for modal structure and styling
2. **For Section 5 Content:** Use Section 2 (Borrower Analysis) as a reference for table layouts and Section 1 (Executive Summary) for key metrics cards
3. **For Numeric Styling:** Look at existing `tabular-nums` usage in other parts of the file (if any exist)
4. **For File Upload:** Use standard HTML5 file input with Tailwind styling, functionality can be simulated

**Priority Order:** Focus on CRITICAL items first, then HIGH priority, then MEDIUM if time permits.

---

**END OF IMPLEMENTATION PROMPT**
