# Current USDV Pre-Qualification Workflow Reference

**Source**: `borrow.usdvcapital.com/Apply for Commercial Real Estate Funding`  
**Purpose**: Reference document for redesigning INSPIRE Quick App to match current USDV workflow

---

## Workflow Structure (6 Steps - Assets & Guarantor Combined)

### Step 1: Contact Info
**Icon**: Person icon  
**Fields**:
- First Name
- Last Name
- Email Address
- Phone Number

**Helper Text**: "Let's start with your contact information so we can save your progress and reach out with your pre-approval."

---

### Step 2: Loan Details
**Icon**: Document icon  
**Fields**:
- Loan Type (dropdown: "Select loan type")
- Property Type (dropdown: "Select property type")

---

### Step 3: Property Info
**Icon**: House/building icon  
**Fields**:
- Property Address (with three-dot button/icon)
- City
- State (dropdown)
- ZIP Code
- Purchase Price
- Current/After Repair Value
- Requested Loan Amount
  - Helper text: "The total loan amount you are requesting"
- Purchase Date (if already purchased) (date picker with calendar icon)

---

### Step 4: Entity
**Icon**: Building/stack icon  
**Fields**:
- Entity Name
- Entity Type (dropdown: "Select entity type")
- State of Formation (dropdown: "Select state")

---

### Step 5: Assets & Guarantor (Combined)
**Icon**: Dollar sign icon + Two people icon  
**Fields**:

**Assets Section:**
- Total Liquid Assets
  - Helper text: "Include cash, savings, stocks, bonds, and other easily accessible funds."

**Guarantor Section:**
- **Guarantor 1** (sub-heading)
  - "Copy from Contact Info" button (with person icon)
  - First Name
  - Last Name
  - Email
  - Phone
  - Credit Score Range (dropdown, e.g., "700-739")
  - Real Estate Experience (dropdown, e.g., "1-2 projects")
- "+ Add Another Guarantor" button (with plus icon)
- Additional Comments (Optional) - Large textarea
  - Placeholder: "Any additional information about your loan request..."

---

### Step 6: Review
**Icon**: Shield/magnifying glass icon  
**Content**:

**Application Summary:**
- **Contact Information:**
  - Name
  - Email
  - Phone

- **Loan Details:**
  - Loan Type
  - Property Type
  - Property Address
  - Purchase Price
  - Current Value
  - Requested Loan
  - Entity
  - Liquid Assets
  - Guarantors (count)

**Terms & Conditions:**
- Checkbox: "I agree to the Terms of Service and Privacy Policy"
- Error message (if unchecked): "You must accept the terms of service" (red text)

**Navigation:**
- "← Previous" button (gray)
- "Submit" button (blue primary)

---

## Visual Design Elements

### Header
- **Logo**: "USDV CAPITAL" (black, prominent)
- **Tagline**: "INSTITUTIONAL QUALITY. INDIVIDUAL ACCESS." (smaller text below logo)
- **Navigation Links**: "Home" and "Consultation" (top right)

### Main Title Section
- **Title**: "Get Pre-Qualified" (large, elegant serif font, centered)
- **Subtitle**: "Complete this form to receive your term sheet in as little as 48 hours" (smaller, dark gray)
- **Info Link**: "Not sure which market to invest in? Explore our market data first." (blue, underlined)

### Progress Indicator
- **Layout**: Horizontal row of circular icons with labels below
- **Completed Steps**: 
  - Blue circle with white checkmark
  - Blue text label
  - Blue connecting line to next step
- **Active Step**:
  - Blue circle with white icon (matching step type)
  - Blue, bold text label
  - Gray connecting line to next step
- **Pending Steps**:
  - Gray circle with gray icon
  - Gray text label
  - Gray connecting line to next step

### Form Card
- **Container**: White rectangular card with rounded corners
- **Border**: Light gray, subtle
- **Shadow**: Subtle shadow for depth
- **Section Title**: 
  - Icon on left (matching progress indicator)
  - Text label (blue color)
- **Form Fields**:
  - Labels above inputs
  - White input fields with light gray borders
  - Dropdown arrows on select fields
  - Helper text below fields (small, gray)
  - Icons next to some fields (three dots, calendar)

### Navigation Buttons
- **Previous**: Gray button, left-aligned, with left arrow icon "← Previous"
- **Next**: Blue primary button, right-aligned, with right arrow icon "Next →"
- **Submit**: Blue primary button, right-aligned, "Submit" text

### Color Scheme
- **Primary Blue**: Used for active/completed steps, primary buttons, links
- **Gray**: Used for inactive steps, secondary buttons, borders, helper text
- **White**: Background, form cards
- **Red**: Error messages
- **Green**: Success states (checkmarks)

### Typography
- **Headings**: Large, elegant serif font for main title
- **Body**: Clean sans-serif for form content
- **Labels**: Medium weight, dark gray
- **Helper Text**: Small, light gray

---

## Key Features & Interactions

1. **Progress Tracking**: Visual progress indicator shows completed, active, and pending steps
2. **Form Validation**: Error messages appear (e.g., "You must accept the terms of service")
3. **Copy Functionality**: "Copy from Contact Info" button for Guarantor section
4. **Dynamic Fields**: "+ Add Another Guarantor" allows multiple guarantors
5. **Date Picker**: Calendar icon for date fields
6. **Address Helper**: Three-dot button/icon next to Property Address field
7. **Terms Checkbox**: Required checkbox on Review page with validation
8. **Application Summary**: Review page shows all entered data in organized sections

---

## Responsive Considerations

- Form cards are centered and have max-width constraints
- Fields stack vertically on smaller screens
- Progress indicator may need horizontal scrolling on mobile
- Navigation buttons stack on mobile

---

## Notes for Implementation

- **Assets & Guarantor Combined**: These are on the same step/page, not separate
- **6 Steps Total**: Contact Info → Loan Details → Property Info → Entity → Assets & Guarantor → Review
- **Clean, Minimal Design**: Focus on clarity and ease of use
- **Professional Appearance**: Matches institutional quality branding
- **Clear Visual Hierarchy**: Progress indicator, section titles, form fields, navigation

