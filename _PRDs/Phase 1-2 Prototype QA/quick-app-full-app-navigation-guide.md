# Quick App & Full App Navigation Guide

**Purpose:** How to access and test Quick App and Full App pages in the HTML prototype

---

## Quick Access Methods

### Method 1: Browser Console (Recommended)

1. Open the HTML file (`inspire-ui-analytical.html`) in your browser
2. Open browser console (F12 or Right-click > Inspect > Console tab)
3. Type one of these commands and press Enter:

```javascript
// Quick App Pages
navigateTo('quick-app-landing')      // Quick App Landing Page
navigateTo('quick-app-form')         // Quick App 6-Step Form

// Full App Pages
navigateTo('full-app-fix-flip')      // Full App Fix & Flip Form
navigateTo('full-app-ground-up')    // Full App Ground-Up Form
navigateTo('full-app-dscr')         // Full App DSCR Form

// Other Pages
navigateTo('prequal-result')        // Pre-qualification Result Page
navigateTo('login')                 // Login Page
navigateTo('entity-selection')      // Entity Selection Page
navigateTo('application-review')    // Application Review Page
navigateTo('application-submitted') // Submission Confirmation Page

// Dashboard (default view)
navigateTo('dashboard')             // Dashboard View
```

### Method 2: Direct Navigation Buttons

- **From Dashboard:** No direct link (use console)
- **From Quick App Landing:** Click "Start Application" button
- **From Login Page:** Click "New client? Start your application" link
- **From Pre-qual Result:** Click "Continue to Full Application" button

---

## Available Page IDs

| Page ID | Description | How to Access |
|---------|-------------|---------------|
| `dashboard` | Dashboard view (default) | Default view when file loads |
| `quick-app-landing` | Quick App Landing Page | Console: `navigateTo('quick-app-landing')` |
| `quick-app-form` | Quick App 6-Step Form | Click "Start Application" or console |
| `prequal-result` | Pre-qualification Result | Submit Quick App form |
| `login` | Login Page | Console or navigation button |
| `entity-selection` | Entity Selection Page | After login |
| `full-app-fix-flip` | Full App Fix & Flip Form | From prequal result or console |
| `full-app-ground-up` | Full App Ground-Up Form | From prequal result or console |
| `full-app-dscr` | Full App DSCR Form | From prequal result or console |
| `application-review` | Application Review Page | From Full App form |
| `application-submitted` | Submission Confirmation | After submitting Full App |

---

## Testing Form Functionality

### Quick App Form Testing

1. Navigate to Quick App form: `navigateTo('quick-app-form')`
2. **Step 2 - Co-Guarantors:**
   - Click "Add Co-Guarantor" button
   - Click "Remove" button to test removal
   - Verify maximum 5 co-guarantors limit

3. **Step 4 - Loan Type Selection:**
   - Select "Fix & Flip" → Verify deal economics fields change
   - Select "Ground-Up" → Verify deal economics fields change
   - Select "DSCR" → Verify deal economics fields change

4. **Step 5 - Property Information:**
   - Select different property types (Single Family, Commercial, etc.)
   - Verify conditional fields appear/disappear

5. **Form Submission:**
   - Fill out required fields
   - Click "Submit Application" button
   - Should navigate to `prequal-result` page

### Full App Form Testing

1. Navigate to Full App form: `navigateTo('full-app-fix-flip')`
2. **Section 1 - Entity Information:**
   - Test ownership table add/remove functionality
   - Verify ownership total percentage validation

3. **Section 6 - Personal Financial Statement:**
   - Toggle between "Upload PFS" and "Complete in-app" radio buttons
   - Verify form sections show/hide correctly

4. **Section 17 - Signature:**
   - Interact with signature canvas
   - Test "Clear" button
   - Verify signature saves

5. **All 17 Sections:**
   - Click through all section tabs
   - Verify active tab highlighting
   - Verify progress bar updates

---

## Testing Error Messages

### How to View Error Messages

Error messages appear via browser default HTML5 validation when you try to submit a form with invalid/empty required fields.

**To test:**
1. Navigate to Quick App form: `navigateTo('quick-app-form')`
2. **Without filling any fields**, click "Submit Application" button
3. Browser will show validation tooltips on required fields
4. Fill fields incorrectly (e.g., invalid email format) and try submitting again

**Note:** These are browser default messages. In production, custom error messages should be implemented.

---

## Mobile Testing

### Browser Dev Tools Simulation (Recommended)

1. Open HTML file in Chrome
2. Press F12 to open DevTools
3. Press Ctrl+Shift+M (or click Toggle Device Toolbar icon)
4. Select device preset (iPhone, iPad, etc.) or set custom dimensions
5. Test touch interactions and responsive layout

### Actual Device Testing

1. Transfer HTML file to mobile device
2. Open file in mobile browser
3. Test touch interactions, form functionality, and styling

**Note:** Cannot test Safari on PC (requires Mac). Use browser dev tools to simulate Safari.

---

## Common Issues & Solutions

### Issue: Can't see Quick App/Full App pages
**Solution:** The HTML loads with Dashboard view by default. Use browser console to navigate: `navigateTo('quick-app-landing')`

### Issue: Error messages not showing
**Solution:** Error messages only appear when you try to submit a form with invalid/empty required fields. Try submitting without filling fields.

### Issue: Can't test on mobile device
**Solution:** Use browser dev tools device simulation (F12 > Ctrl+Shift+M) or transfer HTML file to actual device.

### Issue: Footer missing on some pages
**Status:** Footer only exists on Quick App Landing page. This is a known issue documented in the checklist.

---

*Last Updated: December 2024*

