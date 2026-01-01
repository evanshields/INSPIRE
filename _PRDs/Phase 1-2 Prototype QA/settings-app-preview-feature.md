# Settings Page - Application Preview & Configuration Feature

**Date:** December 2024  
**Purpose:** Added easy access to Quick App and Full App pages from Settings, plus outcome configuration

---

## Overview

Added a new **"Application Preview"** tab to the Settings page that allows users to:
1. **Easily preview** all Quick App and Full App pages without using JavaScript console
2. **See what borrowers see** - preview the borrower-facing application flows
3. **Configure outcomes** - customize messages shown when borrowers qualify, don't qualify, or submit applications
4. **Access all screens** - navigate to any Quick App step or Full App section with one click

---

## Features Added

### 1. Quick App Preview Section

**Location:** Settings > Application Preview tab

**Features:**
- **Quick navigation buttons** to all Quick App pages:
  - Quick App Landing
  - Quick App Form (6-step form)
  - Pre-Qual Result
  - Login Page
  - Entity Selection

- **Step-by-step navigation** - Direct buttons to each of the 6 Quick App form steps:
  - Step 1: Sponsor Information
  - Step 2: Co-Guarantors
  - Step 3: Experience Metrics
  - Step 4: Loan Type Selection
  - Step 5: Property Information
  - Step 6: Deal Economics

**How to Use:**
1. Navigate to Settings page
2. Click "Application Preview" tab
3. Click any button to navigate to that page/section
4. No JavaScript console needed!

### 2. Full App Preview Section

**Location:** Settings > Application Preview tab

**Features:**
- **Quick navigation buttons** to all Full App pages:
  - Full App - Fix & Flip
  - Full App - Ground-Up
  - Full App - DSCR
  - Application Review
  - Submission Confirmation

- **Section-by-section navigation** - Direct buttons to all 17 Full App sections:
  1. Entity
  2. Ownership
  3. Experience
  4. Guarantor
  5. Co-Guarantors
  6. PFS
  7. Credit Auth
  8. Contacts
  9. Property
  10. Loan Details
  11. Economics
  12. Questions
  13. Structural
  14. Scope
  15. SREO
  16. Sold
  17. Signature

**How to Use:**
1. Navigate to Settings page
2. Click "Application Preview" tab
3. Click any Full App button to navigate to that form
4. Click any section button to jump directly to that section

### 3. Outcome Configuration Section

**Location:** Settings > Application Preview tab

**Features:**
- **Configure Qualified Result Page:**
  - Heading text
  - Description text
  - Primary CTA button text
  - Secondary button text
  - Preview button to see changes

- **Configure Disqualified Result Page:**
  - Heading text
  - Description text
  - Alternative options text
  - Contact information
  - Preview button to see changes

- **Configure Submission Confirmation:**
  - Heading text
  - Description text
  - Next steps text
  - Preview button to see changes

**How to Use:**
1. Navigate to Settings > Application Preview tab
2. Scroll to "Outcome Configuration" section
3. Edit any text fields for qualified/disqualified/submitted pages
4. Click "Save Configuration Changes" button
5. Changes are saved to localStorage and immediately reflected in preview pages
6. Click "Preview" buttons to see the updated pages

---

## Technical Implementation

### JavaScript Functions Added

1. **`saveOutcomeConfig()`**
   - Saves configuration to localStorage
   - Updates preview pages immediately
   - Shows confirmation alert

2. **`updateOutcomePages(config)`**
   - Updates qualified result page with new config
   - Updates disqualified page with new config
   - Updates submitted page with new config

3. **`navigateToSectionUI(sectionId)`**
   - Navigates to Full App form
   - Jumps to specific section
   - Updates progress bar

### Data Persistence

- Configuration saved to `localStorage` with key `outcomeConfig`
- Configuration loaded on page load
- Changes persist across browser sessions

### Page IDs Supported

All page IDs work with the `navigateTo()` function:
- `quick-app-landing`
- `quick-app-form`
- `prequal-result`
- `disqualification`
- `login`
- `entity-selection`
- `full-app-fix-flip`
- `full-app-ground-up`
- `full-app-dscr`
- `application-review`
- `application-submitted`

---

## User Benefits

### Before This Feature:
- ❌ Had to use JavaScript console (`navigateTo('quick-app-landing')`)
- ❌ No easy way to preview borrower experience
- ❌ No way to configure outcome messages
- ❌ Difficult to test all pages and sections

### After This Feature:
- ✅ One-click navigation to any page from Settings
- ✅ Easy preview of borrower-facing flows
- ✅ Configure outcome messages directly in UI
- ✅ Quick access to all Quick App steps and Full App sections
- ✅ Changes save automatically and persist

---

## Usage Examples

### Example 1: Preview Quick App Flow
1. Go to Settings > Application Preview
2. Click "Open Quick App Landing"
3. Click through the flow as a borrower would
4. Test all 6 steps using the step buttons

### Example 2: Configure Qualified Message
1. Go to Settings > Application Preview
2. Scroll to "Qualified Result Page" section
3. Change heading to "You're Approved!"
4. Change description to custom message
5. Click "Save Configuration Changes"
6. Click "Preview" to see updated page

### Example 3: Test Full App Section
1. Go to Settings > Application Preview
2. Click "Full App - Fix & Flip"
3. Click section button "6. PFS" to jump directly to PFS section
4. Test the Personal Financial Statement form

---

## Future Enhancements

Potential improvements:
- [ ] Add more configuration options (colors, styling)
- [ ] Add preview mode toggle (show/hide admin controls)
- [ ] Add export/import configuration
- [ ] Add A/B testing for different messages
- [ ] Add analytics tracking for configuration changes

---

*Last Updated: December 2024*


