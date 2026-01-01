# Quick App UX Redesign - Review Document

**Document Version:** 1.0  
**Date:** December 31, 2024  
**Author:** UX Engineer Agent  
**Status:** Ready for Review

---

## 1. Executive Summary

This document details the UX redesign of the Quick App (pre-qualification) form in `inspire-ux.html` to match the current USDV workflow at `borrow.usdvcapital.com`. The redesign also includes new Settings subpages for configuring both the Quick App and Full App forms.

### What Was Changed

| Component | Before | After |
|-----------|--------|-------|
| Quick App Steps | 6 steps (Sponsor → Co-Guarantors → Experience → Loan Type → Property → Deal Economics) | 6 steps (Contact Info → Loan Details → Property Info → Entity → Assets & Guarantor → Review) |
| Progress Indicator | Simple numbered steps with progress bar | Horizontal stepper with circular icons, checkmarks, and connecting lines |
| Form Layout | Basic form groups | White form cards with section icons and headers |
| Header | Simple "USDV Capital" with Back/Login buttons | Full USDV branding with tagline and navigation links |
| Review Step | None (direct submit from Deal Economics) | Dedicated Review step with application summary, edit buttons, and Terms checkbox |
| Settings Page | Basic list of settings categories | Full tabbed interface with Quick App Settings and Full App Settings subpages |

---

## 2. Quick App Form Redesign

### 2.1 New 6-Step Structure

The form has been restructured to match the current USDV workflow. Key change: **Assets and Guarantor are now combined into a single step** (Step 5).

#### Step 1: Contact Info
**Location in `inspire-ux.html`:** Lines ~1500-1580

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| First Name | Text input | Yes | Split from previous "Full Legal Name" |
| Last Name | Text input | Yes | Split from previous "Full Legal Name" |
| Email Address | Email input | Yes | With helper text about term sheet delivery |
| Phone Number | Tel input | Yes | - |

**Changes from Previous:**
- Split "Full Legal Name" into separate First Name and Last Name fields
- Removed "Estimated Credit Score" from this step (moved to Step 5)
- Added helper text for email field

---

#### Step 2: Loan Details
**Location in `inspire-ux.html`:** Lines ~1580-1660

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| Loan Type | Radio card group | Yes | Fix & Flip, Ground-Up Construction, DSCR Rental |
| Property Type | Select dropdown | Yes | SFR, 2-4 Unit, Townhome, Condo, Multifamily |

**Changes from Previous:**
- Combined Loan Type selection (previously Step 4) with Property Type selection
- Moved to earlier in the flow (Step 2 instead of Step 4)
- Added radio card styling for Loan Type selection

---

#### Step 3: Property Info
**Location in `inspire-ux.html`:** Lines ~1660-1800

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| Property Address | Text input (autocomplete) | Yes | Google Places API integration |
| City | Text input | Yes | - |
| State | Select dropdown | Yes | US states |
| ZIP Code | Text input | Yes | 5-digit format |
| Purchase Price | Currency input | Yes | With $ prefix |
| Current Value / ARV | Currency input | Yes | With helper text |
| Requested Loan Amount | Currency input | Yes | - |
| Purchase Date | Date input | No | Expected or actual closing date |

**Changes from Previous:**
- Expanded address fields (was single autocomplete, now includes City, State, ZIP)
- Added Purchase Price, Current/ARV, Requested Loan Amount fields (moved from Deal Economics)
- Added Purchase Date field
- Removed Bedrooms, Bathrooms, Square Footage fields (simplified)

---

#### Step 4: Entity
**Location in `inspire-ux.html`:** Lines ~1800-1880

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| Entity Name | Text input | Yes | Can enter "TBD" if not yet formed |
| Entity Type | Select dropdown | Yes | LLC, Corporation, Limited Partnership, Trust, Other, TBD |
| State of Formation | Select dropdown | Yes | Common states listed, plus TBD option |

**Changes from Previous:**
- NEW STEP - Entity information was not in the previous Quick App
- Allows "TBD" for borrowers who haven't formed an entity yet

---

#### Step 5: Assets & Guarantor (Combined)
**Location in `inspire-ux.html`:** Lines ~1880-2050

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| **Liquid Assets Section** | | | |
| Total Liquid Assets | Currency input | Yes | Cash, checking, savings, stocks, bonds, retirement |
| **Primary Guarantor Section** | | | |
| First Name | Text input | Yes | Can copy from Contact Info |
| Last Name | Text input | Yes | Can copy from Contact Info |
| Email | Email input | Yes | Can copy from Contact Info |
| Phone | Tel input | Yes | Can copy from Contact Info |
| Estimated Credit Score | Select dropdown | Yes | 780+, 740-779, 700-739, 660-699, 620-659, Below 620 |

**Key Features:**
- "Copy from Contact Info" button to auto-fill guarantor fields
- "+ Add Another Guarantor" button (up to 5 total)
- Additional guarantors appear as separate fieldsets

**Changes from Previous:**
- Combined Assets (new) with Guarantor information
- Moved Credit Score from Step 1 to here
- Removed Co-Guarantors as a separate step
- Added Total Liquid Assets field (new)

---

#### Step 6: Review
**Location in `inspire-ux.html`:** Lines ~2050-2250

This is a **NEW STEP** that displays a summary of all entered information.

| Section | Fields Displayed | Actions |
|---------|------------------|---------|
| Contact Info | Name, Email, Phone | Edit button → Step 1 |
| Loan Details | Loan Type, Property Type | Edit button → Step 2 |
| Property Info | Address, Purchase Price, ARV, Loan Amount | Edit button → Step 3 |
| Entity | Entity Name, Type, State | Edit button → Step 4 |
| Assets & Guarantor | Liquid Assets, Guarantor Name, Credit Score | Edit button → Step 5 |

**Terms and Conditions:**
- Checkbox to accept Terms of Service and Privacy Policy
- Links to Terms and Privacy modals
- Required before submission

**Submit Button:**
- "Submit Application" button
- Shows loading state during submission
- Navigates to Pre-Qualification Result page on success

---

### 2.2 Progress Indicator Redesign

**Location in `inspire-ux.html`:** Lines ~1470-1530

The progress indicator has been completely redesigned to match the USDV workflow:

```
Old Design:
┌─────────────────────────────────────────┐
│  [=====>                    ] 16.67%    │
│  ① ② ③ ④ ⑤ ⑥                           │
│  Step 1 of 6: Sponsor Information       │
└─────────────────────────────────────────┘

New Design:
┌─────────────────────────────────────────────────────────────────────┐
│  [👤]───[📄]───[🏠]───[🏢]───[💰]───[📋]                           │
│   ✓      ●      ○      ○      ○      ○                             │
│ Contact Loan  Property Entity Assets  Review                        │
│  Info  Details  Info         & Guar.                                │
└─────────────────────────────────────────────────────────────────────┘
```

**Visual States:**
| State | Circle Style | Icon Style | Connector Line |
|-------|--------------|------------|----------------|
| Completed | Blue background | White checkmark | Blue line |
| Active | Blue background | White step icon | Blue line (left), Gray line (right) |
| Pending | Gray background | Gray step icon | Gray line |

**ShadCN Component Mapping:**
- Custom stepper component (ShadCN doesn't have built-in stepper)
- Can use ShadCN Progress as base for connector lines
- Icons from Lucide (ShadCN's icon library)

---

### 2.3 Header Redesign

**Location in `inspire-ux.html`:** Lines ~1450-1470

**Old Header:**
```html
<header class="public-header">
    <div class="logo">USDV Capital</div>
    <nav>
        <button>Back to Home</button>
        <button>Login</button>
    </nav>
</header>
```

**New Header:**
```html
<header class="usdv-header">
    <div class="branding">
        <div class="logo"><strong>USDV</strong> CAPITAL</div>
        <div class="tagline">INSTITUTIONAL QUALITY. INDIVIDUAL ACCESS.</div>
    </div>
    <nav>
        <a href="#">Home</a>
        <a href="#">Consultation</a>
    </nav>
</header>
```

**Changes:**
- Added tagline "INSTITUTIONAL QUALITY. INDIVIDUAL ACCESS."
- Changed navigation to links (Home, Consultation)
- Removed Login button (available on landing page)
- Added role="banner" for accessibility

---

### 2.4 Form Card Design

Each step is now wrapped in a form card with:

```html
<article class="form-card">
    <header class="card-header">
        <span class="section-icon">👤</span>
        <h2>Contact Info</h2>
    </header>
    <div class="card-content">
        <!-- Form fields -->
    </div>
</article>
```

**ShadCN Component:** `Card` with `CardHeader` and `CardContent`

---

### 2.5 Navigation Buttons

**Old Navigation:**
```html
<div class="form-actions">
    <button class="btn-secondary">Back</button>
    <button class="btn-primary">Next</button>
</div>
```

**New Navigation:**
```html
<div class="form-navigation">
    <button class="btn-previous">← Previous</button>
    <button class="btn-next">Next →</button>
</div>
```

**Changes:**
- Added arrow indicators to buttons
- Renamed classes for clarity
- Step 6 has "Submit Application" instead of "Next"

---

## 3. Settings Page Redesign

### 3.1 Settings Tab Structure

**Location in `inspire-ux.html`:** Lines ~2700-3400

The Settings page now has a tabbed interface:

| Tab | Description |
|-----|-------------|
| General | User Profile, Notifications |
| **Loan Application** | Quick App Settings, Full App Settings |
| Team | Team Members management |
| Investors | Investor configuration |
| Templates | Email and Term Sheet templates |
| Integrations | API Keys |

---

### 3.2 Quick App Settings (Task #20)

**Location in `inspire-ux.html`:** Lines ~2800-3000

#### Step Configuration
- List of all 6 steps with drag handles for reordering
- Toggle switches to enable/disable optional steps
- Required steps are locked (cannot be disabled)

| Step | Status |
|------|--------|
| Contact Info | Required (locked) |
| Loan Details | Required (locked) |
| Property Info | Required (locked) |
| Entity | Optional (can disable) |
| Assets & Guarantor | Required (locked) |
| Review | Required (locked) |

#### Field Configuration
- Accordion sections for each step
- Each field has a visibility dropdown: Required / Optional / Hidden
- Example fields shown for Step 1 and Step 2

#### Outcome Messages
- Textarea for "Qualified" message
- Textarea for "Disqualified" message
- Textarea for "Manual Review" message
- Pre-filled with default messages

#### Preview Buttons
- "Preview Fix & Flip" - Opens Quick App with Fix & Flip pre-selected
- "Preview Ground-Up" - Opens Quick App with Ground-Up pre-selected
- "Preview DSCR" - Opens Quick App with DSCR pre-selected

---

### 3.3 Full App Settings (Task #21)

**Location in `inspire-ux.html`:** Lines ~3000-3400

#### Section Configuration
17 sections organized into categories:

**Borrower & Entity (9 sections):**
1. Borrowing Entity Information (Required)
2. Entity Ownership (Required)
3. Aggregate Experience (Required)
4. Primary Guarantor (Required)
5. Background Questions (Required)
6. Additional Guarantors (Optional)
7. Personal Financial Statement (Required)
8. Credit Authorization (Required)
9. Third-Party Contacts (Optional)

**Property & Loan (5 sections):**
10. Property Information (Required)
11. Loan Details (Required)
12. Deal Economics (Required)
13. Property Questions (Required)
14. Structural Questions (Fix & Flip Only)

**Additional (3 sections):**
15. Scope of Work / Budget (Fix & Flip / Ground-Up)
16. Investor Experience & SREO (Optional)
17. Business Purpose Certification (Required)

#### Conditional Logic Builder
- IF/THEN rule builder for showing/hiding sections
- Example rule: IF Loan Type = Fix & Flip THEN Show Structural Questions
- Add Rule button to create new rules

#### Loan Type Variations Matrix
- Table showing which sections appear for each loan type
- Checkboxes to enable/disable sections per loan type

#### Preview Buttons
- Loan type dropdown to select preview type
- "Preview Full App" button

---

## 4. JavaScript Functions Added

### 4.1 Quick App Functions

| Function | Purpose |
|----------|---------|
| `goToStep(stepNumber)` | Navigate directly to a specific step (used by Review edit buttons) |
| `validateCurrentStep()` | Validate required fields before proceeding |
| `updateProgressStepper()` | Update visual state of progress indicator |
| `markStepCompleted(stepNumber)` | Mark a step as completed in the stepper |
| `updateLoanTypeSelection(radio)` | Update visual state of loan type radio cards |
| `copyFromContactInfo()` | Copy contact fields to guarantor fields |
| `addGuarantor()` | Add an additional guarantor (up to 5) |
| `removeGuarantor(index)` | Remove an additional guarantor |
| `populateReviewSummary()` | Populate Review step with form data |
| `formatCurrency(value)` | Format numbers as currency for display |
| `submitQuickApp(event)` | Handle form submission |

### 4.2 Settings Functions

| Function | Purpose |
|----------|---------|
| `switchSettingsTab(tabId)` | Switch between Settings tabs |
| `switchAppSettingsTab(appType)` | Switch between Quick App and Full App settings |
| `previewQuickApp(loanType)` | Open Quick App preview |
| `previewFullApp(loanType)` | Open Full App preview |
| `updateFullAppPreview()` | Update section visibility based on loan type |
| `expandAllFields()` | Expand all field configuration accordions |
| `addConditionalRule()` | Add a new conditional logic rule |
| `saveQuickAppSettings()` | Save Quick App configuration |
| `resetQuickAppSettings()` | Reset to default settings |
| `saveFullAppSettings()` | Save Full App configuration |
| `resetFullAppSettings()` | Reset to default settings |

---

## 5. Accessibility Improvements

| Feature | Implementation |
|---------|----------------|
| ARIA labels | All form fields have associated labels |
| Required fields | `aria-required="true"` on required inputs |
| Error messages | `aria-describedby` linking errors to fields |
| Role attributes | `role="tablist"`, `role="tab"`, `role="tabpanel"` for tabs |
| Screen reader text | `.sr-only` class for visually hidden labels |
| Focus management | Focus moves to first field of each step |
| Keyboard navigation | Tab order follows logical flow |

---

## 6. ShadCN Component Mapping

For the UI Engineer Agent to implement in React:

| Prototype Element | ShadCN Component | Notes |
|-------------------|------------------|-------|
| Form cards | `Card`, `CardHeader`, `CardContent` | White background, subtle shadow |
| Text inputs | `Input` | With `Label` component |
| Select dropdowns | `Select` | With `SelectTrigger`, `SelectContent`, `SelectItem` |
| Radio cards | `RadioGroup` | Custom styling for card appearance |
| Checkboxes | `Checkbox` | For Terms acceptance |
| Buttons | `Button` | `variant="default"` for primary, `variant="outline"` for secondary |
| Progress stepper | Custom | Build using `Progress` as base |
| Tabs | `Tabs`, `TabsList`, `TabsTrigger`, `TabsContent` | For Settings page |
| Accordion | `Accordion`, `AccordionItem`, `AccordionTrigger`, `AccordionContent` | For field configuration |
| Toggle switches | `Switch` | For step enable/disable |
| Alerts | `Alert` | For error messages |

---

## 7. What to Review

### 7.1 Quick App Form Flow

1. **Open `inspire-ux.html` in a browser**
2. **Navigate to the Quick App form:**
   - Click "Pipeline" in sidebar
   - Click any deal card
   - Or use the navigation function: Open browser console and type `navigateTo('quick-app-form')`

3. **Test the 6-step flow:**
   - Step 1: Fill in Contact Info fields
   - Click "Next →" to proceed
   - Step 2: Select Loan Type and Property Type
   - Step 3: Enter Property Info
   - Step 4: Enter Entity Info
   - Step 5: Enter Assets and Guarantor (try "Copy from Contact Info")
   - Step 6: Review summary and accept Terms

4. **Verify:**
   - Progress indicator updates correctly
   - Previous button is disabled on Step 1
   - Review page shows entered data
   - Edit buttons navigate to correct steps

### 7.2 Settings Page

1. **Navigate to Settings:**
   - Click "Settings" in sidebar
   - Or: `navigateTo('settings')`

2. **Review Loan Application tab:**
   - Click "Loan Application" tab
   - Review Quick App Settings
   - Click "Full App Settings" sub-tab
   - Review Full App Settings

3. **Verify:**
   - Step configuration list shows all 6 steps
   - Field configuration accordion expands
   - Outcome messages are editable
   - Preview buttons work (navigate to Quick App)

---

## 8. Known Limitations

| Limitation | Notes |
|------------|-------|
| No actual form validation | Validation is placeholder only |
| No API integration | Form submission is simulated |
| No drag-and-drop | Step reordering is visual only |
| No persistence | Settings are saved to localStorage only |
| Placeholder icons | Using emoji icons instead of Lucide icons |

---

## 9. Next Steps

After UX review approval:

1. **UI Engineer Agent** applies Tailwind CSS styling
2. **Framework Converter Agent** converts to Next.js with ShadCN components
3. **QA Agent** tests the implemented components

---

## 10. File Changes Summary

| File | Changes |
|------|---------|
| `inspire-ux.html` | Complete Quick App redesign (Lines ~1411-2250), Settings page expansion (Lines ~2700-3400), New JavaScript functions (Lines ~850-1100) |

---

*End of Quick App UX Redesign Review Document*

