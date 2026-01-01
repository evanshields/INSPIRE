# Phase 1-2 Implementation Plan: Intake & Full Application

**Document Version:** 1.0  
**PRD Reference:** INSPIRE Phase 1-2 PRD  
**Last Updated:** December 2024  
**Status:** Implementation Ready

---

## 1. Executive Summary

### 1.1 Phase Overview

Phase 1-2 establishes the borrower entry point into INSPIRE through:
- **Phase 1: Quick App (Pre-Qualification)** - Lightweight intake form for deal screening
- **Phase 2: Full Application** - Comprehensive loan application by product type (Fix & Flip, Ground-Up Construction, DSCR)

### 1.2 Success Metrics (from PRD)

| Metric | Target |
|--------|--------|
| Quick App completion rate | >85% |
| Quick App average completion time | <3 minutes |
| Full App completion rate | >80% |
| Full App average completion time | <5 minutes per property |
| Data pre-fill accuracy | >95% |
| Mobile completion rate | >40% of submissions |

### 1.3 Key Dependencies

| Dependency | Status | Notes |
|------------|--------|-------|
| Google Places API | Required | Address autocomplete |
| Google OAuth | Required | Existing client login |
| SendGrid | Required | Email notifications |
| PostgreSQL | Required | Data storage |
| Google Drive API | Required | Document storage |

---

## 2. Page/Screen Inventory

### 2.1 Complete Page List

| Page ID | Page Name | Route | User Role | Entry Point |
|---------|-----------|-------|-----------|-------------|
| P1-01 | Quick App Landing | `/` or `/apply` | Public | Direct URL, marketing links |
| P1-02 | Quick App Form | `/apply/quick` | Public | Landing page CTA |
| P1-03 | Pre-Qualification Result | `/apply/result` | Public | Quick App submission |
| P1-04 | Disqualification Page | `/apply/not-qualified` | Public | Failed pre-qual |
| P2-01 | Full App - Fix & Flip | `/application/fix-flip` | Authenticated | Qualified from Quick App |
| P2-02 | Full App - Ground-Up | `/application/ground-up` | Authenticated | Qualified from Quick App |
| P2-03 | Full App - DSCR | `/application/dscr` | Authenticated | Qualified from Quick App |
| P2-04 | Application Review | `/application/review` | Authenticated | Full App completion |
| P2-05 | Application Submitted | `/application/submitted` | Authenticated | Application submission |
| P2-06 | Existing Client Login | `/login` | Public | Quick App (existing) |
| P2-07 | Entity Selection | `/application/select-entity` | Authenticated | Post-login for existing clients |

### 2.2 Navigation Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PHASE 1-2 USER FLOWS                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  NEW CLIENT PATH                                                             │
│  ───────────────                                                             │
│  Landing → Quick App → Pre-Qual Result → Full App → Review → Submitted      │
│                              │                                               │
│                              └─→ Disqualified (if fails)                     │
│                                                                              │
│  EXISTING CLIENT PATH                                                        │
│  ────────────────────                                                        │
│  Landing → Login → Entity Selection → Quick App (pre-filled) → ...          │
│                                                                              │
│  RE CFO CLIENT PATH                                                          │
│  ──────────────────                                                          │
│  Landing → Login → Entity Selection → Quick App (max pre-fill) → ...        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Per-Page Specifications

---

### 3.1 P1-01: Quick App Landing Page

#### 3.1.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Entry point for loan applications, establishes trust and guides users to Quick App |
| **User Roles** | Public (unauthenticated), Existing Clients |
| **Entry Points** | Direct URL, marketing campaigns, referrals |
| **PRD Reference** | Phase 1-2 PRD, Section 4.1-4.2 |

#### 3.1.2 Information Architecture

**Primary Data:** None (static page)

**Content Hierarchy:**
1. Hero section with value proposition
2. Loan type options (Fix & Flip, Ground-Up, DSCR)
3. Trust indicators (rates, terms, testimonials)
4. CTA buttons (New Application, Existing Client Login)

**Navigation Structure:**
- Header: USDV Logo, Login button
- Footer: Contact info, legal links

#### 3.1.3 Component Breakdown

**ShadCN Components:**
| Component | Usage | Demo Reference |
|-----------|-------|----------------|
| `button` | Primary CTA "Start Application", Secondary "Login" | `mcp_shadcn-ui_get_component_demo("button")` |
| `card` | Loan type cards (Fix & Flip, Ground-Up, DSCR) | `mcp_shadcn-ui_get_component_demo("card")` |
| `badge` | Rate badges, "Most Popular" indicators | `mcp_shadcn-ui_get_component_demo("badge")` |
| `separator` | Section dividers | `mcp_shadcn-ui_get_component_demo("separator")` |

**React Custom Components:**

```typescript
// components/landing/HeroSection.tsx
interface HeroSectionProps {
  headline: string;
  subheadline: string;
  ctaText: string;
  ctaHref: string;
  secondaryCtaText?: string;
  secondaryCtaHref?: string;
}

// Composition: Uses ShadCN Button for CTAs
```

```typescript
// components/landing/LoanTypeCard.tsx
interface LoanTypeCardProps {
  loanType: 'fix_flip' | 'ground_up' | 'dscr';
  title: string;
  description: string;
  features: string[];
  rateRange: string;
  termRange: string;
  isPopular?: boolean;
  onSelect: () => void;
}

// Composition: Uses ShadCN Card, Badge, Button
```

```typescript
// components/landing/TrustIndicators.tsx
interface TrustIndicatorsProps {
  stats: {
    label: string;
    value: string;
    icon?: React.ReactNode;
  }[];
}

// Composition: Uses ShadCN Card for stat cards
```

#### 3.1.4 Data Requirements

**No dynamic data** - Static marketing content.

**Configuration (hardcoded or CMS):**
```typescript
interface LandingPageConfig {
  headline: string;
  subheadline: string;
  loanTypes: {
    type: 'fix_flip' | 'ground_up' | 'dscr';
    displayName: string;
    description: string;
    features: string[];
    rateRange: string;
    termRange: string;
    minLoan: number;
    maxLoan: number;
  }[];
  trustStats: {
    label: string;
    value: string;
  }[];
}
```

#### 3.1.5 State Management

| State | Type | Scope | Notes |
|-------|------|-------|-------|
| selectedLoanType | `string \| null` | Component | Pre-select loan type before navigating |

**URL Parameters:** None

#### 3.1.6 Interactions & Behaviors

| User Action | System Response | Navigation |
|-------------|-----------------|------------|
| Click "Start Application" | None | Navigate to `/apply/quick` |
| Click "Login" | None | Navigate to `/login` |
| Click loan type card | Set selectedLoanType | Navigate to `/apply/quick?type={loanType}` |
| Scroll | Animate sections into view | None |

#### 3.1.7 All States

**Empty State:** N/A (static page)

**Loading State:**
- Page-level skeleton while hydrating
- Use ShadCN `skeleton` for card placeholders

**Error State:** N/A (static page)

**Populated State:** Default view with all content

**Edge Cases:**
- Mobile viewport: Stack cards vertically, full-width CTAs
- Slow connection: Progressive image loading

#### 3.1.8 Accessibility

| Requirement | Implementation |
|-------------|----------------|
| ARIA labels | All buttons have descriptive labels |
| Keyboard navigation | Tab order: Logo → Login → Hero CTA → Loan cards → Footer |
| Focus management | Focus trap not needed (no modals) |
| Screen reader | Semantic headings (h1 → h2 → h3) |

#### 3.1.9 Responsive Design

| Breakpoint | Layout Changes |
|------------|----------------|
| Desktop (1280px+) | 3-column loan card grid, side-by-side hero |
| Tablet (768px-1279px) | 2-column loan card grid, stacked hero |
| Mobile (<768px) | Single column, full-width cards, sticky CTA |

#### 3.1.10 Mock Data Examples

```json
{
  "landingConfig": {
    "headline": "Fast, Flexible Real Estate Financing",
    "subheadline": "Close in as little as 2 weeks. Competitive rates. Expert support.",
    "loanTypes": [
      {
        "type": "fix_flip",
        "displayName": "Fix & Flip",
        "description": "Short-term financing for property renovation and resale",
        "features": [
          "Up to 90% LTC",
          "12-24 month terms",
          "Rehab draws available"
        ],
        "rateRange": "10.5% - 12.5%",
        "termRange": "12-24 months",
        "minLoan": 100000,
        "maxLoan": 3000000
      },
      {
        "type": "ground_up",
        "displayName": "Ground-Up Construction",
        "description": "New construction financing from lot to completion",
        "features": [
          "Up to 85% LTC",
          "12-24 month terms",
          "Construction draws"
        ],
        "rateRange": "11.0% - 13.0%",
        "termRange": "12-24 months",
        "minLoan": 100000,
        "maxLoan": 3000000
      },
      {
        "type": "dscr",
        "displayName": "DSCR Rental",
        "description": "Long-term financing for income-producing properties",
        "features": [
          "Up to 80% LTV",
          "30-year terms",
          "No income docs required"
        ],
        "rateRange": "6.5% - 8.5%",
        "termRange": "30 years",
        "minLoan": 100000,
        "maxLoan": 3000000
      }
    ],
    "trustStats": [
      { "label": "Loans Funded", "value": "$500M+" },
      { "label": "Average Close Time", "value": "14 days" },
      { "label": "Repeat Borrowers", "value": "78%" }
    ]
  }
}
```

---

### 3.2 P1-02: Quick App Form

#### 3.2.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Capture minimal information for deal pre-qualification |
| **User Roles** | Public (new clients), Authenticated (existing clients) |
| **Entry Points** | Landing page CTA, Direct URL with optional loan type |
| **PRD Reference** | Phase 1-2 PRD, Section 4.3-4.6 |

#### 3.2.2 Information Architecture

**Primary Data:** QuickApp submission

**Form Sections (in order):**
1. Sponsor Information
2. Co-Guarantors (optional, repeatable)
3. Experience Metrics
4. Loan Type Selection
5. Property Information
6. Deal Economics (conditional by loan type)

**Navigation Structure:**
- Progress indicator (step X of Y)
- Back/Next buttons
- Save & Exit (for authenticated users)

#### 3.2.3 Component Breakdown

**ShadCN Components:**
| Component | Usage | Demo Reference |
|-----------|-------|----------------|
| `form` | Form wrapper with validation | `mcp_shadcn-ui_get_component_demo("form")` |
| `input` | Text inputs (name, email, phone) | `mcp_shadcn-ui_get_component_demo("input")` |
| `select` | Dropdowns (credit score, property type) | `mcp_shadcn-ui_get_component_demo("select")` |
| `radio-group` | Loan type, property type, yes/no questions | `mcp_shadcn-ui_get_component_demo("radio-group")` |
| `button` | Navigation, submit | `mcp_shadcn-ui_get_component_demo("button")` |
| `progress` | Step progress indicator | `mcp_shadcn-ui_get_component_demo("progress")` |
| `card` | Section containers | `mcp_shadcn-ui_get_component_demo("card")` |
| `label` | Form field labels | `mcp_shadcn-ui_get_component_demo("label")` |
| `alert` | Validation errors, info messages | `mcp_shadcn-ui_get_component_demo("alert")` |

**React Custom Components:**

```typescript
// components/forms/QuickAppForm.tsx
interface QuickAppFormProps {
  initialValues?: Partial<QuickAppFormData>;
  onSubmit: (data: QuickAppFormData) => Promise<void>;
  isExistingClient?: boolean;
  prefilledFields?: string[]; // Field names that were pre-filled
}

// Multi-step form orchestrator
// Composition: Uses ShadCN Form, Progress, Button
```

```typescript
// components/forms/SponsorInfoSection.tsx
interface SponsorInfoSectionProps {
  control: Control<QuickAppFormData>;
  errors: FieldErrors<QuickAppFormData>;
  isPrefilled?: boolean;
}

// Composition: Uses ShadCN Input, Select, Label
```

```typescript
// components/forms/CoGuarantorSection.tsx
interface CoGuarantorSectionProps {
  control: Control<QuickAppFormData>;
  errors: FieldErrors<QuickAppFormData>;
  maxGuarantors?: number; // Default 5
}

// Repeatable section with add/remove
// Composition: Uses ShadCN Input, Select, Button
```

```typescript
// components/forms/AddressAutocomplete.tsx
interface AddressAutocompleteProps {
  value: string;
  onChange: (address: ParsedAddress) => void;
  placeholder?: string;
  error?: string;
}

interface ParsedAddress {
  fullAddress: string;
  street: string;
  city: string;
  state: string;
  zip: string;
  lat?: number;
  lng?: number;
}

// Google Places API integration
// Composition: Uses ShadCN Input, Popover for suggestions
```

```typescript
// components/forms/CurrencyInput.tsx
interface CurrencyInputProps {
  value: number | undefined;
  onChange: (value: number | undefined) => void;
  placeholder?: string;
  error?: string;
  min?: number;
  max?: number;
}

// Formatted currency input with masking
// Composition: Uses ShadCN Input
```

```typescript
// components/forms/CreditScoreSelect.tsx
interface CreditScoreSelectProps {
  value: string;
  onChange: (value: string) => void;
  error?: string;
}

// Credit score range dropdown
// Options: <620, 620-659, 660-699, 700-739, 740-779, 780+
// Composition: Uses ShadCN Select
```

```typescript
// components/forms/DealEconomicsSection.tsx
interface DealEconomicsSectionProps {
  loanType: 'fix_flip' | 'ground_up' | 'dscr';
  control: Control<QuickAppFormData>;
  errors: FieldErrors<QuickAppFormData>;
}

// Conditional fields based on loan type
// Composition: Uses CurrencyInput, ShadCN RadioGroup
```

```typescript
// components/forms/FormProgress.tsx
interface FormProgressProps {
  currentStep: number;
  totalSteps: number;
  stepLabels: string[];
}

// Visual progress indicator
// Composition: Uses ShadCN Progress
```

#### 3.2.4 Data Requirements

**Data Model (TypeScript Interface):**

```typescript
interface QuickAppFormData {
  // Section 1: Sponsor Information
  sponsor: {
    fullLegalName: string;
    email: string;
    phone: string;
    estimatedCreditScore: CreditScoreRange;
  };
  
  // Section 2: Co-Guarantors
  hasCoGuarantors: boolean;
  coGuarantors: {
    name: string;
    estimatedCreditScore: CreditScoreRange;
  }[];
  
  // Section 3: Experience Metrics
  experience: {
    fixFlipDealsLast3Years: number;
    groundUpDealsLast3Years: number;
    rentalPropertiesOwned: number;
  };
  
  // Section 4: Loan Type
  loanType: 'fix_flip' | 'ground_up' | 'dscr';
  
  // Section 5: Property Information
  property: {
    address: ParsedAddress;
    propertyType: 'single_family' | 'commercial';
    // Single Family specific
    bedrooms?: number;
    bathrooms?: number;
    squareFootage?: number;
    // Commercial specific
    commercialType?: CommercialPropertyType;
  };
  
  // Section 6: Deal Economics (conditional)
  dealEconomics: FixFlipEconomics | GroundUpEconomics | DSCREconomics;
}

type CreditScoreRange = 
  | 'below_620' 
  | '620_659' 
  | '660_699' 
  | '700_739' 
  | '740_779' 
  | '780_plus';

type CommercialPropertyType = 
  | 'multifamily' 
  | 'hospitality' 
  | 'retail' 
  | 'office' 
  | 'industrial' 
  | 'mixed_use';

interface FixFlipEconomics {
  alreadyOwned: boolean;
  purchasePrice?: number;        // If not owned
  originalPurchasePrice?: number; // If owned
  renovationBudget: number;
  afterRepairValue: number;
}

interface GroundUpEconomics {
  alreadyOwnLand: boolean;
  landPurchasePrice?: number;        // If not owned
  originalLandPurchasePrice?: number; // If owned
  constructionBudget: number;
  afterRepairValue: number;
}

interface DSCREconomics {
  currentPropertyValue: number;
  projectedMonthlyRent: number;
  annualPropertyTaxes: number;
  annualInsurance: number;
  monthlyHOA?: number;
  afterRepairValue: number;
}
```

**Field Specifications Table:**

| Field | Type | Required | Validation | Source |
|-------|------|----------|------------|--------|
| sponsor.fullLegalName | string | Yes | Min 2 chars | User input |
| sponsor.email | string | Yes | Valid email format | User input |
| sponsor.phone | string | Yes | Valid phone format | User input |
| sponsor.estimatedCreditScore | enum | Yes | Valid range | User input |
| hasCoGuarantors | boolean | Yes | - | User input |
| coGuarantors[].name | string | Conditional | Min 2 chars | User input |
| coGuarantors[].estimatedCreditScore | enum | Conditional | Valid range | User input |
| experience.fixFlipDealsLast3Years | number | Yes | ≥0, integer | User input |
| experience.groundUpDealsLast3Years | number | Yes | ≥0, integer | User input |
| experience.rentalPropertiesOwned | number | Yes | ≥0, integer | User input |
| loanType | enum | Yes | Valid type | User input |
| property.address | object | Yes | Valid US address | Google Places |
| property.propertyType | enum | Yes | Valid type | User input |
| property.bedrooms | number | Conditional | 1-20, integer | User input |
| property.bathrooms | number | Conditional | 1-20, decimal allowed | User input |
| property.squareFootage | number | Conditional | >0 | User input |
| property.commercialType | enum | Conditional | Valid type | User input |
| dealEconomics.* | varies | Conditional | See above | User input |

**Computed/Derived Fields:**
- `totalExperience`: Sum of all experience metrics
- `lowestCreditScore`: Minimum of sponsor + co-guarantor scores
- `estimatedLTV`: (purchasePrice + renovationBudget) / ARV (for display only)

#### 3.2.5 State Management

| State | Type | Scope | Notes |
|-------|------|-------|-------|
| currentStep | number | Component | Current form step (1-6) |
| formData | QuickAppFormData | Component | Form values (react-hook-form) |
| isSubmitting | boolean | Component | Submission in progress |
| prefilledFields | string[] | Component | Fields pre-filled from existing data |

**URL Parameters:**
- `?type=fix_flip|ground_up|dscr` - Pre-select loan type
- `?returnTo=` - Return URL after completion

**Form State (react-hook-form):**
```typescript
const form = useForm<QuickAppFormData>({
  resolver: zodResolver(quickAppSchema),
  defaultValues: initialValues,
  mode: 'onChange', // Real-time validation
});
```

#### 3.2.6 Interactions & Behaviors

| User Action | System Response | Navigation |
|-------------|-----------------|------------|
| Fill field | Validate on blur, show inline error if invalid | None |
| Click "Next" | Validate current section, advance if valid | Next step |
| Click "Back" | Save current values, go to previous step | Previous step |
| Click "Save & Exit" | Save to localStorage/API, show confirmation | Landing page |
| Change loan type | Reset deal economics section | None |
| Change property type | Show/hide conditional fields | None |
| Add co-guarantor | Add new co-guarantor form fields (max 5) | None |
| Remove co-guarantor | Remove co-guarantor fields | None |
| Type in address | Show Google Places autocomplete suggestions | None |
| Select address | Parse and populate address fields | None |
| Submit form | Validate all, submit to API, show loading | Result page |

**API Calls:**
```typescript
// Submit Quick App
POST /api/quick-app
Body: QuickAppFormData
Response: { dealId: string, qualified: boolean, reasons?: string[] }

// Save progress (authenticated users)
POST /api/quick-app/:dealId/save
Body: Partial<QuickAppFormData>
Response: { success: boolean }

// Get prefill data (authenticated users)
GET /api/clients/:clientId/prefill
Response: Partial<QuickAppFormData>
```

#### 3.2.7 All States

**Empty State:**
- Fresh form with no values
- All fields empty, no validation errors
- Progress at step 1

**Loading State:**
- Skeleton for form fields while loading prefill data
- Disabled submit button with spinner during submission
- "Saving..." indicator during auto-save

**Error State:**
- Inline field errors (red border, error message below)
- Section-level error summary at top of section
- Toast notification for API errors
- Retry button for failed submissions

**Populated State:**
- Fields with values
- Pre-filled fields show green checkmark indicator
- Validation passes, Next button enabled

**Edge Cases:**
| Scenario | Handling |
|----------|----------|
| All co-guarantors have low credit | Show warning but allow submission |
| Commercial property selected | Show info that manual review required |
| Address not found in Google Places | Allow manual entry with warning |
| Session timeout during form | Auto-save, prompt to re-authenticate |
| Browser back button | Confirm navigation, offer to save |
| Form data exceeds localStorage limit | Fallback to session storage |
| Network offline | Queue submission, notify user |

#### 3.2.8 Accessibility

| Requirement | Implementation |
|-------------|----------------|
| ARIA labels | All inputs have associated labels |
| Keyboard navigation | Tab through fields in logical order |
| Focus management | Focus first field of each step on navigation |
| Screen reader | Announce step changes, validation errors |
| Error association | `aria-describedby` links errors to fields |
| Required fields | `aria-required="true"` on required inputs |

**Focus Order:**
1. Progress indicator (informational)
2. Section heading
3. Form fields (in DOM order)
4. Back button
5. Next/Submit button

#### 3.2.9 Responsive Design

| Breakpoint | Layout Changes |
|------------|----------------|
| Desktop (1280px+) | 2-column form layout, side progress indicator |
| Tablet (768px-1279px) | Single column, top progress indicator |
| Mobile (<768px) | Single column, compact progress, sticky navigation |

**Mobile-Specific:**
- Numeric keyboard for number inputs (`inputMode="numeric"`)
- Tel keyboard for phone (`inputMode="tel"`)
- Email keyboard for email (`inputMode="email"`)
- Touch-friendly input heights (44px minimum)
- Swipe gestures for step navigation (optional)

#### 3.2.10 Mock Data Examples

**New Client Submission:**
```json
{
  "sponsor": {
    "fullLegalName": "John Michael Smith",
    "email": "john.smith@email.com",
    "phone": "+1 (305) 555-1234",
    "estimatedCreditScore": "700_739"
  },
  "hasCoGuarantors": true,
  "coGuarantors": [
    {
      "name": "Jane Smith",
      "estimatedCreditScore": "740_779"
    }
  ],
  "experience": {
    "fixFlipDealsLast3Years": 5,
    "groundUpDealsLast3Years": 0,
    "rentalPropertiesOwned": 3
  },
  "loanType": "fix_flip",
  "property": {
    "address": {
      "fullAddress": "123 Main Street, Miami, FL 33139",
      "street": "123 Main Street",
      "city": "Miami",
      "state": "FL",
      "zip": "33139",
      "lat": 25.7617,
      "lng": -80.1918
    },
    "propertyType": "single_family",
    "bedrooms": 3,
    "bathrooms": 2,
    "squareFootage": 1850
  },
  "dealEconomics": {
    "alreadyOwned": false,
    "purchasePrice": 340000,
    "renovationBudget": 85000,
    "afterRepairValue": 525000
  }
}
```

**Existing Client Prefill Data:**
```json
{
  "sponsor": {
    "fullLegalName": "John Michael Smith",
    "email": "john.smith@email.com",
    "phone": "+1 (305) 555-1234",
    "estimatedCreditScore": "720"
  },
  "experience": {
    "fixFlipDealsLast3Years": 8,
    "groundUpDealsLast3Years": 2,
    "rentalPropertiesOwned": 5
  },
  "prefilledFields": [
    "sponsor.fullLegalName",
    "sponsor.email",
    "sponsor.phone",
    "sponsor.estimatedCreditScore",
    "experience.fixFlipDealsLast3Years",
    "experience.groundUpDealsLast3Years",
    "experience.rentalPropertiesOwned"
  ]
}
```

---

### 3.3 P1-03: Pre-Qualification Result Page

#### 3.3.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Display pre-qualification result and guide to next steps |
| **User Roles** | Applicant (just submitted Quick App) |
| **Entry Points** | Quick App submission redirect |
| **PRD Reference** | Phase 1-2 PRD, Section 4.4-4.5 |

#### 3.3.2 Information Architecture

**Primary Data:** PreQualificationResult

**Content Hierarchy:**
1. Result status (Qualified / Not Qualified)
2. Deal summary (property, loan type, estimated terms)
3. Next steps CTA
4. Contact information

#### 3.3.3 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `card` | Result card, deal summary card |
| `badge` | Status badge (Qualified/Not Qualified) |
| `button` | Continue to Full App, Contact Us |
| `alert` | Info/warning messages |
| `separator` | Section dividers |

**React Custom Components:**

```typescript
// components/prequal/PreQualResultCard.tsx
interface PreQualResultCardProps {
  qualified: boolean;
  dealId: string;
  propertyAddress: string;
  loanType: string;
  estimatedLoanAmount?: number;
  estimatedRate?: string;
  disqualificationReasons?: string[];
}

// Composition: Uses ShadCN Card, Badge, Button
```

```typescript
// components/prequal/DealSummaryCard.tsx
interface DealSummaryCardProps {
  property: {
    address: string;
    type: string;
    bedrooms?: number;
    bathrooms?: number;
    sqft?: number;
  };
  economics: {
    purchasePrice?: number;
    rehabBudget?: number;
    arv: number;
  };
  metrics: {
    estimatedLTV?: number;
    estimatedLTC?: number;
    estimatedLTARV?: number;
  };
}

// Composition: Uses ShadCN Card, Table
```

#### 3.3.4 Data Requirements

```typescript
interface PreQualificationResult {
  dealId: string;
  qualified: boolean;
  
  // If qualified
  estimatedTerms?: {
    loanAmount: number;
    rate: string;
    term: string;
    ltv: number;
    ltc?: number;
    ltarv?: number;
  };
  
  // If not qualified
  disqualificationReasons?: string[];
  
  // Deal summary
  property: {
    address: string;
    type: string;
  };
  loanType: string;
  
  // Timestamps
  submittedAt: Date;
  expiresAt: Date; // Quote expiration
}
```

#### 3.3.5 State Management

| State | Type | Scope | Notes |
|-------|------|-------|-------|
| result | PreQualificationResult | Page | From API or route state |
| isLoading | boolean | Page | While fetching result |

**URL Parameters:**
- `?dealId=` - Deal ID to fetch result

#### 3.3.6 Interactions & Behaviors

| User Action | System Response | Navigation |
|-------------|-----------------|------------|
| Click "Continue to Full Application" | None | Navigate to `/application/{loanType}?dealId={dealId}` |
| Click "Contact Us" | Open contact modal or mailto | None |
| Click "Start New Application" | None | Navigate to `/apply/quick` |

#### 3.3.7 All States

**Loading State:**
- Skeleton card while fetching result
- "Checking your qualification..." message

**Qualified State:**
- Green success styling
- "Congratulations! You're Pre-Qualified" heading
- Estimated terms displayed
- Prominent "Continue to Full Application" CTA

**Not Qualified State:**
- Neutral/informational styling (not harsh red)
- "We couldn't match this deal to our current programs" heading
- List of reasons in friendly language
- Newsletter signup option
- "Contact Us" CTA for questions

**Error State:**
- "Unable to retrieve your result" message
- Retry button
- Contact support link

#### 3.3.8 Mock Data Examples

**Qualified Result:**
```json
{
  "dealId": "deal_abc123",
  "qualified": true,
  "estimatedTerms": {
    "loanAmount": 425000,
    "rate": "10.5% - 11.5%",
    "term": "12 months",
    "ltv": 85,
    "ltc": 85,
    "ltarv": 68
  },
  "property": {
    "address": "123 Main Street, Miami, FL 33139",
    "type": "Single Family"
  },
  "loanType": "Fix & Flip",
  "submittedAt": "2024-12-10T14:30:00Z",
  "expiresAt": "2024-12-12T14:30:00Z"
}
```

**Disqualified Result:**
```json
{
  "dealId": "deal_xyz789",
  "qualified": false,
  "disqualificationReasons": [
    "Estimated credit score below our minimum requirement of 620",
    "No prior real estate investment experience for Ground-Up Construction loans"
  ],
  "property": {
    "address": "456 Oak Avenue, Tampa, FL 33602",
    "type": "Single Family"
  },
  "loanType": "Ground-Up Construction",
  "submittedAt": "2024-12-10T15:00:00Z"
}
```

---

### 3.4 P2-01/02/03: Full Application Forms

#### 3.4.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Capture comprehensive loan application data by product type |
| **User Roles** | Authenticated applicant |
| **Entry Points** | Pre-qualification result (qualified), Direct URL with dealId |
| **PRD Reference** | Phase 1-2 PRD, Sections 5.1-5.10 |

The Full Application has three variants:
- **P2-01: Fix & Flip / Bridge** - `/application/fix-flip`
- **P2-02: Ground-Up Construction** - `/application/ground-up`
- **P2-03: DSCR Rental** - `/application/dscr`

All share common sections with product-specific variations.

#### 3.4.2 Information Architecture

**Form Sections (Common):**
1. Borrowing Entity Information
2. Borrowing Entity Ownership
3. Aggregate Experience
4. Primary Guarantor Information
5. Background Questions
6. Additional Guarantors
7. Personal Financial Statement
8. Credit Authorization
9. Third-Party Contact Information

**Form Sections (Product-Specific):**

**Fix & Flip / Bridge:**
10. Property Information
11. Loan Details
12. Deal Economics
13. Property Questions
14. Structural Questions

**Ground-Up Construction:**
10. Property Information
11. Loan Details
12. Deal Economics
13. Property Questions

**DSCR Rental:**
10. Property Information
11. Loan Details
12. Deal Economics
13. Property Questions

**Additional Sections (All):**
- Scope of Work / Budget (Fix & Flip, Ground-Up)
- Investor Experience & Portfolio (All)
- Business Purpose Certification & Signature (All)

#### 3.4.3 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `form` | Form wrapper |
| `input` | Text inputs |
| `select` | Dropdowns |
| `radio-group` | Yes/No questions, options |
| `checkbox` | Multi-select, agreements |
| `textarea` | Long text (explanations) |
| `table` | SREO, budget line items |
| `tabs` | Section navigation |
| `accordion` | Collapsible sections |
| `dialog` | Confirmations, help modals |
| `tooltip` | Field help text |
| `calendar` | Date pickers |
| `progress` | Form completion progress |

**React Custom Components:**

```typescript
// components/application/FullApplicationForm.tsx
interface FullApplicationFormProps {
  loanType: 'fix_flip' | 'ground_up' | 'dscr';
  dealId: string;
  initialValues?: Partial<FullApplicationData>;
  onSubmit: (data: FullApplicationData) => Promise<void>;
  onSave: (data: Partial<FullApplicationData>) => Promise<void>;
}
```

```typescript
// components/application/EntitySection.tsx
interface EntitySectionProps {
  control: Control<FullApplicationData>;
  errors: FieldErrors<FullApplicationData>;
  existingEntities?: Entity[]; // For existing clients
}
```

```typescript
// components/application/OwnershipTable.tsx
interface OwnershipTableProps {
  value: OwnershipEntry[];
  onChange: (entries: OwnershipEntry[]) => void;
  error?: string;
}

interface OwnershipEntry {
  firstName: string;
  lastName: string;
  ownershipPercent: number;
}

// Editable table with validation (must total 100%)
// Composition: Uses ShadCN Table, Input, Button
```

```typescript
// components/application/GuarantorForm.tsx
interface GuarantorFormProps {
  index: number;
  isPrimary: boolean;
  control: Control<FullApplicationData>;
  errors: FieldErrors<FullApplicationData>;
  onRemove?: () => void;
}

// Full guarantor form with all PII fields
// Composition: Uses ShadCN Input, Select, Calendar
```

```typescript
// components/application/BackgroundQuestionsSection.tsx
interface BackgroundQuestionsSectionProps {
  guarantorIndex: number;
  control: Control<FullApplicationData>;
  errors: FieldErrors<FullApplicationData>;
}

// Yes/No questions with conditional explanation fields
// Composition: Uses ShadCN RadioGroup, Textarea
```

```typescript
// components/application/PersonalFinancialStatement.tsx
interface PFSProps {
  control: Control<FullApplicationData>;
  errors: FieldErrors<FullApplicationData>;
  allowUpload?: boolean;
}

// In-app PFS form or file upload option
// Composition: Uses ShadCN Input, Card, file upload
```

```typescript
// components/application/CreditAuthorizationSection.tsx
interface CreditAuthorizationProps {
  control: Control<FullApplicationData>;
  errors: FieldErrors<FullApplicationData>;
  guarantorName: string;
}

// FCRA disclosure and e-signature
// Composition: Uses ShadCN Checkbox, signature component
```

```typescript
// components/application/ScopeOfWorkBuilder.tsx
interface ScopeOfWorkBuilderProps {
  control: Control<FullApplicationData>;
  errors: FieldErrors<FullApplicationData>;
  allowUpload?: boolean;
}

// Budget builder with categories and line items
// Composition: Uses ShadCN Table, Input, Accordion
```

```typescript
// components/application/SREOTable.tsx
interface SREOTableProps {
  value: SREOEntry[];
  onChange: (entries: SREOEntry[]) => void;
  type: 'current' | 'sold';
}

interface SREOEntry {
  address: string;
  cityStateZip: string;
  entityOnTitle: string;
  ownershipPercent: number;
  acquisitionDate: Date;
  investmentType: string;
  propertyType: string;
  presentMarketValue: number;
  mortgagesLiens: number;
  netRentalIncome: number;
}

// Editable SREO table
// Composition: Uses ShadCN Table, Input, Select, Calendar
```

```typescript
// components/application/PropertySection.tsx
interface PropertySectionProps {
  loanType: 'fix_flip' | 'ground_up' | 'dscr';
  control: Control<FullApplicationData>;
  errors: FieldErrors<FullApplicationData>;
  prefillFromQuickApp?: QuickAppPropertyData;
}

// Product-specific property fields
// Composition: Uses AddressAutocomplete, ShadCN Select, Input
```

```typescript
// components/application/SignatureSection.tsx
interface SignatureSectionProps {
  control: Control<FullApplicationData>;
  errors: FieldErrors<FullApplicationData>;
  disclosureText: string;
}

// Business purpose certification and e-signature
// Composition: Uses ShadCN Checkbox, signature pad component
```

#### 3.4.4 Data Requirements

**Data Model (TypeScript Interface):**

```typescript
interface FullApplicationData {
  // Meta
  dealId: string;
  loanType: 'fix_flip' | 'ground_up' | 'dscr';
  
  // Section: Borrowing Entity
  entity: {
    name: string;
    companyType: 'limited_partnership' | 'llc' | 'corporation' | 'other';
    ein: string; // XX-XXXXXXX format
    registeredStates: string[];
  };
  
  // Section: Entity Ownership
  ownership: {
    entries: OwnershipEntry[];
    hasOrgChart: boolean;
    orgChartDocumentId?: string;
  };
  
  // Section: Aggregate Experience
  aggregateExperience: {
    areasOfOperation: string[]; // Multi-select
    rentalUnitsBoughtLast3Years: number;
    totalRentalUnitsOwned: number;
    fixFlipsSoldLast3Years: number;
    newConstructionBuildsLast3Years: number;
    gcStatus: 'on_staff' | 'third_party';
  };
  
  // Section: Primary Guarantor
  primaryGuarantor: GuarantorInfo;
  
  // Section: Additional Guarantors
  additionalGuarantors: GuarantorInfo[];
  
  // Section: Personal Financial Statement
  pfs: {
    uploadedDocumentId?: string;
    inAppData?: PFSData;
  };
  
  // Section: Credit Authorization
  creditAuthorization: {
    authorized: boolean;
    signature: string; // Base64 or signature data
    signedAt: Date;
  };
  
  // Section: Third-Party Contacts
  thirdPartyContacts: {
    propertyAccess: ContactInfo;
    title: ContactInfo;
    insurance: ContactInfo;
    escrow: ContactInfo;
  };
  
  // Product-specific sections
  property: FixFlipProperty | GroundUpProperty | DSCRProperty;
  loanDetails: FixFlipLoanDetails | GroundUpLoanDetails | DSCRLoanDetails;
  dealEconomics: FixFlipEconomics | GroundUpEconomics | DSCRFullEconomics;
  propertyQuestions: FixFlipQuestions | GroundUpQuestions | DSCRQuestions;
  
  // Optional sections
  scopeOfWork?: ScopeOfWork;
  investorExperience?: InvestorExperience;
  
  // Certification
  businessPurposeCertification: {
    acknowledged: boolean;
    signature: string;
    signedAt: Date;
  };
}

interface GuarantorInfo {
  firstName: string;
  lastName: string;
  streetAddress: string;
  city: string;
  state: string;
  zip: string;
  ssn: string; // Encrypted
  dateOfBirth: Date;
  phone: string;
  email: string;
  citizenship: string;
  estimatedCreditScore: CreditScoreRange;
  backgroundQuestions: BackgroundQuestions;
}

interface BackgroundQuestions {
  felonyOrFraud: boolean;
  felonyOrFraudExplanation?: string;
  outstandingLawsuits: boolean;
  outstandingLawsuitsExplanation?: string;
  outstandingJudgments: boolean;
  outstandingJudgmentsExplanation?: string;
  bankruptcyLast4Years: boolean;
  bankruptcyExplanation?: string;
  foreclosureLast3Years: boolean;
  foreclosureExplanation?: string;
  delinquentMortgage: boolean;
  delinquentMortgageExplanation?: string;
}

interface PFSData {
  liquidAssets: {
    cash: number;
    retirementAccounts: number;
    stocksBonds: number;
    otherLiquid: number;
  };
  nonLiquidAssets: {
    realEstateAssets: number;
    autos: number;
    otherPersonalProperty: number;
  };
  liabilities: {
    realEstateDebt: number;
    revolvingDebt: number;
    installmentDebt: number;
    notesPayable: number;
    otherDebt: number;
  };
  // Computed
  totalLiquid: number;
  totalNonLiquid: number;
  totalDebt: number;
  netWorth: number;
}

interface ContactInfo {
  companyName?: string;
  contactName: string;
  phone: string;
  email: string;
}

// Fix & Flip specific
interface FixFlipProperty {
  propertyType: 'single_family' | 'multi_family' | 'townhome' | 'condo';
  units?: number;
  address: ParsedAddress;
  unitNumber?: string;
}

interface FixFlipLoanDetails {
  loanPurpose: 'purchase' | 'refinance' | 'fix_flip_rehab_in_progress' | 'bridge_no_rehab';
  exitStrategy: 'sell' | 'hold_as_rental';
  targetCloseDate: Date;
  requestedLoanAmount: number;
  entityForClosing: string;
  originalPurchaseDate?: Date;
  timeToExitMonths: number;
}

interface FixFlipQuestions {
  willRequestRehabDraws: boolean;
  permitsRequired: boolean;
  hasPermits?: boolean;
  permitsExpectedDate?: Date;
  propertyTypeChange: boolean;
  zoningChangesRequired: boolean;
  intendToSubdivide: boolean;
  existingMortgage: boolean;
  existingMortgageLender?: string;
  existingMortgageBalance?: number;
  otherLiens: boolean;
  otherLienHolders?: string;
  otherLienBalance?: number;
  underContractToSell: boolean;
  contractAmount?: number;
  usingThirdPartyGC: boolean;
  hasGCLicensing?: boolean;
  willHaveWellOrSeptic: boolean;
  relocatingMechanicals: boolean;
  // Structural questions
  removing2PlusLoadBearingWalls: boolean;
  addingLivableSF: boolean;
  expandingBuildingEnvelope: boolean;
}

// Ground-Up specific
interface GroundUpProperty {
  propertyType: 'single_family' | 'multi_family' | 'townhome' | 'condo';
  units?: number;
  address: ParsedAddress;
}

interface GroundUpLoanDetails {
  loanPurpose: 'vacant_lot_ground_up' | 'tear_down_rebuild' | 'mid_construction_refinance';
  lotStatus: 'purchasing' | 'paying_off_loan' | 'owned_free_clear';
  exitStrategy: 'sell' | 'hold_as_rental';
  requestingCashOut?: boolean;
  targetCloseDate: Date;
  requestedLoanAmount: number;
  entityForClosing: string;
  originalPurchaseDate?: Date;
  timeToExitMonths: number;
}

interface GroundUpQuestions {
  isLotZonedAndPlatted: boolean;
  hasBuildingPermits: boolean;
  permitsExpectedDate?: Date;
  constructionAlreadyCompleted: boolean;
  completedConstructionCost?: number;
  isLotReadyToBuild60Days: boolean;
  hasPlansAndSpecs: boolean;
  zoningChangesRequired: boolean;
  intendToSubdivide: boolean;
  existingMortgageOnLot: boolean;
  existingMortgageLender?: string;
  existingMortgageBalance?: number;
  otherLiens: boolean;
  underContractToSellOnCompletion: boolean;
  contractAmount?: number;
  usingThirdPartyGC: boolean;
  utilitiesAvailable: boolean;
  willHaveWellOrSeptic: boolean;
}

// DSCR specific
interface DSCRProperty {
  propertyType: 'single_family' | '2_4_unit' | 'townhome' | 'condo' | 'multifamily';
  units?: number;
  address: ParsedAddress;
}

interface DSCRLoanDetails {
  loanPurpose: 'purchase' | 'refinance_rate_term' | 'refinance_cash_out';
  originalPurchaseDate?: Date;
  targetCloseDate: Date;
  requestedLoanAmount: number;
  entityForClosing: string;
  propertyManager: 'self_managed' | 'professional_management';
}

interface DSCRFullEconomics {
  currentAsIsValue: number;
  estimatedMarketMonthlyRent: number;
  currentMonthlyRent?: number;
  annualTaxes: number;
  annualInsurance: number;
  annualHOADues?: number;
}

interface DSCRQuestions {
  allPropertiesRented: boolean | 'na';
  currentOccupancyPercent?: number;
  allPropertiesRentReady: boolean | 'na';
  subjectToLeaseOrGroundLease: boolean | 'na';
  existingMortgage: boolean | 'na';
  existingMortgageCompany?: string;
  existingMortgageBalance?: number;
  otherLiens: boolean | 'na';
  otherLienHolders?: string;
  otherLienBalance?: number;
  sponsorOccupyProperty: boolean;
  propertiesVestedInEntity?: boolean | 'na';
  currentVesting?: string;
  relationshipWithSeller?: boolean | 'na';
  downPaymentBorrowedOrEncumbered: boolean | 'na';
}

// Scope of Work
interface ScopeOfWork {
  uploadedDocumentId?: string;
  inAppBudget?: BudgetData;
}

interface BudgetData {
  date: Date;
  propertyAddress: string;
  projectDescription: string;
  lineItems: BudgetLineItem[];
  total: number;
}

interface BudgetLineItem {
  category: string;
  description: string;
  location?: string;
  quantity?: number;
  budget: number;
}

// Investor Experience
interface InvestorExperience {
  uploadedDocumentId?: string;
  inAppData?: {
    propertiesLast12Months: number;
    propertiesLast36Months: number;
    propertiesLifetime: number;
    currentSREO: SREOEntry[];
    recentlySold: SoldPropertyEntry[];
  };
}

interface SREOEntry {
  address: string;
  cityStateZip: string;
  entityOnTitle: string;
  ownershipPercent: number;
  acquisitionDate: Date;
  investmentType: string;
  propertyType: string;
  presentMarketValue: number;
  mortgagesLiens: number;
  netRentalIncome: number;
}

interface SoldPropertyEntry {
  address: string;
  cityStateZip: string;
  entityOnTitle: string;
  ownershipPercent: number;
  acquisitionDate: Date;
  dispositionDate: Date;
  purchasePrice: number;
  rehabCost: number;
  dispositionPrice: number;
}
```

**Field Specifications Table (Key Fields):**

| Field | Type | Required | Validation | Notes |
|-------|------|----------|------------|-------|
| entity.name | string | Yes | Min 2 chars | Or "TBD" if unknown |
| entity.ein | string | Yes | XX-XXXXXXX format | Masked input |
| ownership.entries | array | Yes | Must total 100% | Repeatable |
| guarantor.ssn | string | Yes | XXX-XX-XXXX format | Encrypted, masked |
| guarantor.dateOfBirth | date | Yes | Must be 18+ | Date picker |
| pfs.liquidAssets.* | number | Yes | ≥0 | Currency input |
| creditAuthorization.signature | string | Yes | Non-empty | E-signature |

#### 3.4.5 State Management

| State | Type | Scope | Notes |
|-------|------|-------|-------|
| currentSection | string | Component | Active form section |
| formData | FullApplicationData | Component | Form values |
| completedSections | string[] | Component | Sections that pass validation |
| isSubmitting | boolean | Component | Submission in progress |
| autoSaveStatus | 'saved' \| 'saving' \| 'error' | Component | Auto-save indicator |

**URL Parameters:**
- `?dealId=` - Deal ID (required)
- `?section=` - Jump to specific section

**Context:**
```typescript
interface ApplicationContext {
  dealId: string;
  loanType: 'fix_flip' | 'ground_up' | 'dscr';
  isExistingClient: boolean;
  prefilledData: Partial<FullApplicationData>;
  documentsOnFile: DocumentReference[];
}
```

#### 3.4.6 Interactions & Behaviors

| User Action | System Response | Navigation |
|-------------|-----------------|------------|
| Navigate to section | Validate current section, show target | Update URL `?section=` |
| Fill field | Validate on blur, auto-save after 2s debounce | None |
| Add guarantor | Add new guarantor form (max 5 total) | None |
| Remove guarantor | Confirm, remove guarantor | None |
| Upload document | Upload to storage, link to field | None |
| Complete in-app PFS | Calculate totals automatically | None |
| Add SREO row | Add new editable row | None |
| Add budget line item | Add new line in category | None |
| Sign authorization | Capture signature, timestamp | None |
| Submit application | Validate all, submit to API | Review page |

**API Calls:**
```typescript
// Get application data
GET /api/application/:dealId
Response: FullApplicationData

// Save progress (auto-save)
PUT /api/application/:dealId
Body: Partial<FullApplicationData>
Response: { success: boolean, savedAt: Date }

// Submit application
POST /api/application/:dealId/submit
Body: FullApplicationData
Response: { success: boolean, status: 'application' }

// Upload document
POST /api/application/:dealId/documents
Body: FormData (file)
Response: { documentId: string, url: string }

// Get existing client prefill
GET /api/clients/:clientId/prefill
Response: Partial<FullApplicationData>
```

#### 3.4.7 All States

**Empty State:**
- Fresh application with Quick App data pre-filled
- Sections show completion status (0/X complete)

**Loading State:**
- Section skeleton while loading data
- "Loading your application..." message
- Auto-save indicator: "Saving..."

**Error State:**
- Inline field errors
- Section-level error summary
- "Unable to save" toast with retry

**Populated State:**
- Fields with values
- Pre-filled fields marked with indicator
- Section completion checkmarks

**Edge Cases:**
| Scenario | Handling |
|----------|----------|
| Ownership doesn't total 100% | Show error, prevent section completion |
| SSN format invalid | Show format hint, prevent blur |
| Background question "Yes" | Expand explanation textarea, require text |
| Multiple properties | Show "Add Property" button, repeat property sections |
| Document upload fails | Show retry button, allow skip with warning |
| Session expires during form | Save to localStorage, prompt re-auth |
| PFS totals don't match | Auto-recalculate, show discrepancy warning |

#### 3.4.8 Accessibility

| Requirement | Implementation |
|-------------|----------------|
| ARIA labels | All inputs have labels, complex components have descriptions |
| Keyboard navigation | Tab through sections, Enter to expand/collapse |
| Focus management | Focus first field of section on navigation |
| Screen reader | Announce section changes, completion status |
| Error association | Errors linked to fields via `aria-describedby` |
| Form grouping | Related fields grouped with `fieldset` and `legend` |

#### 3.4.9 Responsive Design

| Breakpoint | Layout Changes |
|------------|----------------|
| Desktop (1280px+) | 2-column layout, sidebar navigation |
| Tablet (768px-1279px) | Single column, top navigation tabs |
| Mobile (<768px) | Single column, accordion sections, sticky submit |

#### 3.4.10 Mock Data Examples

**Complete Fix & Flip Application:**
```json
{
  "dealId": "deal_abc123",
  "loanType": "fix_flip",
  "entity": {
    "name": "Smith Investments LLC",
    "companyType": "llc",
    "ein": "12-3456789",
    "registeredStates": ["FL", "GA"]
  },
  "ownership": {
    "entries": [
      { "firstName": "John", "lastName": "Smith", "ownershipPercent": 60 },
      { "firstName": "Jane", "lastName": "Smith", "ownershipPercent": 40 }
    ],
    "hasOrgChart": false
  },
  "aggregateExperience": {
    "areasOfOperation": ["fix_flip", "rentals"],
    "rentalUnitsBoughtLast3Years": 5,
    "totalRentalUnitsOwned": 8,
    "fixFlipsSoldLast3Years": 12,
    "newConstructionBuildsLast3Years": 0,
    "gcStatus": "third_party"
  },
  "primaryGuarantor": {
    "firstName": "John",
    "lastName": "Smith",
    "streetAddress": "456 Oak Lane",
    "city": "Miami",
    "state": "FL",
    "zip": "33139",
    "ssn": "***-**-1234",
    "dateOfBirth": "1980-05-15",
    "phone": "+1 (305) 555-1234",
    "email": "john.smith@email.com",
    "citizenship": "US",
    "estimatedCreditScore": "700_739",
    "backgroundQuestions": {
      "felonyOrFraud": false,
      "outstandingLawsuits": false,
      "outstandingJudgments": false,
      "bankruptcyLast4Years": false,
      "foreclosureLast3Years": false,
      "delinquentMortgage": false
    }
  },
  "additionalGuarantors": [
    {
      "firstName": "Jane",
      "lastName": "Smith",
      "streetAddress": "456 Oak Lane",
      "city": "Miami",
      "state": "FL",
      "zip": "33139",
      "ssn": "***-**-5678",
      "dateOfBirth": "1982-08-22",
      "phone": "+1 (305) 555-5678",
      "email": "jane.smith@email.com",
      "citizenship": "US",
      "estimatedCreditScore": "740_779",
      "backgroundQuestions": {
        "felonyOrFraud": false,
        "outstandingLawsuits": false,
        "outstandingJudgments": false,
        "bankruptcyLast4Years": false,
        "foreclosureLast3Years": false,
        "delinquentMortgage": false
      }
    }
  ],
  "pfs": {
    "inAppData": {
      "liquidAssets": {
        "cash": 150000,
        "retirementAccounts": 250000,
        "stocksBonds": 100000,
        "otherLiquid": 25000
      },
      "nonLiquidAssets": {
        "realEstateAssets": 1200000,
        "autos": 75000,
        "otherPersonalProperty": 50000
      },
      "liabilities": {
        "realEstateDebt": 650000,
        "revolvingDebt": 15000,
        "installmentDebt": 25000,
        "notesPayable": 0,
        "otherDebt": 0
      },
      "totalLiquid": 525000,
      "totalNonLiquid": 1325000,
      "totalDebt": 690000,
      "netWorth": 1160000
    }
  },
  "creditAuthorization": {
    "authorized": true,
    "signature": "data:image/png;base64,...",
    "signedAt": "2024-12-10T14:30:00Z"
  },
  "thirdPartyContacts": {
    "propertyAccess": {
      "contactName": "Bob Builder",
      "phone": "+1 (305) 555-9999",
      "email": "bob@contractor.com"
    },
    "title": {
      "companyName": "First American Title",
      "contactName": "Sarah Title",
      "phone": "+1 (305) 555-8888",
      "email": "sarah@firstam.com"
    },
    "insurance": {
      "companyName": "State Farm",
      "contactName": "Jake Insurance",
      "phone": "+1 (305) 555-7777",
      "email": "jake@statefarm.com"
    },
    "escrow": {
      "companyName": "First American Title",
      "contactName": "Sarah Title",
      "phone": "+1 (305) 555-8888",
      "email": "sarah@firstam.com"
    }
  },
  "property": {
    "propertyType": "single_family",
    "address": {
      "fullAddress": "123 Main Street, Miami, FL 33139",
      "street": "123 Main Street",
      "city": "Miami",
      "state": "FL",
      "zip": "33139"
    }
  },
  "loanDetails": {
    "loanPurpose": "purchase",
    "exitStrategy": "sell",
    "targetCloseDate": "2024-12-20",
    "requestedLoanAmount": 425000,
    "entityForClosing": "Smith Investments LLC",
    "timeToExitMonths": 6
  },
  "dealEconomics": {
    "purchasePrice": 340000,
    "currentMarketValue": 350000,
    "totalRehabBudgetRemaining": 85000,
    "rehabAlreadyCompleted": 0,
    "estimatedAfterRepairValue": 525000
  },
  "propertyQuestions": {
    "willRequestRehabDraws": true,
    "permitsRequired": true,
    "hasPermits": false,
    "permitsExpectedDate": "2024-12-15",
    "propertyTypeChange": false,
    "zoningChangesRequired": false,
    "intendToSubdivide": false,
    "existingMortgage": false,
    "otherLiens": false,
    "underContractToSell": false,
    "usingThirdPartyGC": true,
    "willHaveWellOrSeptic": false,
    "relocatingMechanicals": false,
    "removing2PlusLoadBearingWalls": false,
    "addingLivableSF": false,
    "expandingBuildingEnvelope": false
  },
  "scopeOfWork": {
    "inAppBudget": {
      "date": "2024-12-10",
      "propertyAddress": "123 Main Street, Miami, FL 33139",
      "projectDescription": "Full interior renovation including kitchen and bathrooms",
      "lineItems": [
        { "category": "Preparation", "description": "Demolition", "budget": 5000 },
        { "category": "Kitchen", "description": "Cabinets", "budget": 12000 },
        { "category": "Kitchen", "description": "Countertops", "budget": 5000 },
        { "category": "Kitchen", "description": "Appliances", "budget": 8000 },
        { "category": "Bathroom", "description": "Master Bath Renovation", "budget": 15000 },
        { "category": "Bathroom", "description": "Guest Bath Renovation", "budget": 8000 },
        { "category": "Interior", "description": "Flooring", "budget": 12000 },
        { "category": "Interior", "description": "Paint", "budget": 6000 },
        { "category": "Mechanicals", "description": "HVAC", "budget": 8000 },
        { "category": "Completion", "description": "Contingency", "budget": 6000 }
      ],
      "total": 85000
    }
  },
  "investorExperience": {
    "inAppData": {
      "propertiesLast12Months": 4,
      "propertiesLast36Months": 12,
      "propertiesLifetime": 25,
      "currentSREO": [
        {
          "address": "789 Pine Road",
          "cityStateZip": "Miami, FL 33140",
          "entityOnTitle": "Smith Investments LLC",
          "ownershipPercent": 100,
          "acquisitionDate": "2023-06-15",
          "investmentType": "Rental",
          "propertyType": "Single Family",
          "presentMarketValue": 450000,
          "mortgagesLiens": 280000,
          "netRentalIncome": 2400
        }
      ],
      "recentlySold": [
        {
          "address": "321 Elm Street",
          "cityStateZip": "Miami, FL 33141",
          "entityOnTitle": "Smith Investments LLC",
          "ownershipPercent": 100,
          "acquisitionDate": "2024-01-10",
          "dispositionDate": "2024-08-15",
          "purchasePrice": 280000,
          "rehabCost": 65000,
          "dispositionPrice": 425000
        }
      ]
    }
  },
  "businessPurposeCertification": {
    "acknowledged": true,
    "signature": "data:image/png;base64,...",
    "signedAt": "2024-12-10T15:00:00Z"
  }
}
```

---

## 4. Cross-Page Flows

### 4.1 New Client Complete Flow

```
1. Landing Page
   └─→ Click "Start Application"
   
2. Quick App Form (6 steps)
   └─→ Complete all sections
   └─→ Submit
   
3. Pre-Qualification Result
   └─→ If Qualified: Click "Continue to Full Application"
   └─→ If Not Qualified: Newsletter signup or Contact
   
4. Full Application Form
   └─→ Complete all sections
   └─→ Submit
   
5. Application Review
   └─→ Review summary
   └─→ Confirm submission
   
6. Application Submitted
   └─→ Confirmation + Next steps
```

### 4.2 Existing Client Flow

```
1. Landing Page
   └─→ Click "Login"
   
2. Login Page
   └─→ Google OAuth or Email/Password
   
3. Entity Selection (if multiple entities)
   └─→ Select borrowing entity
   
4. Quick App Form (pre-filled)
   └─→ Verify/update pre-filled data
   └─→ Submit
   
5. Pre-Qualification Result
   └─→ Continue to Full Application
   
6. Full Application Form (pre-filled)
   └─→ Verify/update data
   └─→ Confirm documents on file
   └─→ Submit
   
7. Application Submitted
```

### 4.3 State Persistence

| Data | Storage | Duration |
|------|---------|----------|
| Quick App progress (unauthenticated) | localStorage | 7 days |
| Quick App progress (authenticated) | Database | Until submission |
| Full App progress | Database | Until submission |
| Deal ID | URL parameter | Session |
| Selected entity | Session storage | Session |

### 4.4 Deep Linking

| URL Pattern | Behavior |
|-------------|----------|
| `/apply/quick?type=fix_flip` | Start Quick App with loan type pre-selected |
| `/application/fix-flip?dealId=abc123` | Resume Full App at last saved section |
| `/application/fix-flip?dealId=abc123&section=pfs` | Jump to specific section |
| `/apply/result?dealId=abc123` | View pre-qual result |

---

## 5. API Contract (Mock)

### 5.1 Quick App Endpoints

```typescript
// POST /api/quick-app
// Create new deal from Quick App submission
interface CreateQuickAppRequest {
  body: QuickAppFormData;
}

interface CreateQuickAppResponse {
  dealId: string;
  status: 'prospect';
  createdAt: Date;
}

// POST /api/quick-app/:dealId/qualify
// Run pre-qualification logic
interface QualifyRequest {
  params: { dealId: string };
}

interface QualifyResponse {
  qualified: boolean;
  reasons?: string[];
  estimatedTerms?: {
    loanAmount: number;
    rate: string;
    term: string;
  };
}

// GET /api/quick-app/:dealId
// Get Quick App data
interface GetQuickAppResponse {
  dealId: string;
  data: QuickAppFormData;
  status: 'prospect' | 'qualified' | 'disqualified';
  createdAt: Date;
  updatedAt: Date;
}
```

### 5.2 Full Application Endpoints

```typescript
// GET /api/application/:dealId
// Get Full Application data
interface GetApplicationResponse {
  dealId: string;
  loanType: 'fix_flip' | 'ground_up' | 'dscr';
  data: Partial<FullApplicationData>;
  status: 'application' | 'submitted';
  completedSections: string[];
  createdAt: Date;
  updatedAt: Date;
}

// PUT /api/application/:dealId
// Save application progress
interface SaveApplicationRequest {
  params: { dealId: string };
  body: Partial<FullApplicationData>;
}

interface SaveApplicationResponse {
  success: boolean;
  savedAt: Date;
  completedSections: string[];
}

// POST /api/application/:dealId/submit
// Submit completed application
interface SubmitApplicationRequest {
  params: { dealId: string };
  body: FullApplicationData;
}

interface SubmitApplicationResponse {
  success: boolean;
  status: 'application';
  submittedAt: Date;
  nextSteps: string[];
}

// POST /api/application/:dealId/documents
// Upload document
interface UploadDocumentRequest {
  params: { dealId: string };
  body: FormData; // file, documentType
}

interface UploadDocumentResponse {
  documentId: string;
  filename: string;
  url: string;
  uploadedAt: Date;
}
```

### 5.3 Client Prefill Endpoints

```typescript
// GET /api/clients/:clientId/prefill
// Get existing client data for pre-fill
interface GetPrefillResponse {
  sponsor: Partial<SponsorInfo>;
  experience: Partial<ExperienceMetrics>;
  entities: Entity[];
  documentsOnFile: DocumentReference[];
  prefilledFields: string[];
}

// GET /api/clients/:clientId/entities
// Get client's borrowing entities
interface GetEntitiesResponse {
  entities: {
    id: string;
    name: string;
    type: string;
    ein: string;
    lastUsed: Date;
  }[];
}
```

### 5.4 Error Responses

```typescript
interface APIError {
  error: {
    code: string;
    message: string;
    details?: Record<string, string[]>; // Field-level errors
  };
}

// Common error codes:
// - VALIDATION_ERROR: Form validation failed
// - NOT_FOUND: Deal not found
// - UNAUTHORIZED: Authentication required
// - FORBIDDEN: Not authorized for this deal
// - DEAL_EXPIRED: Quick App quote expired
// - ALREADY_SUBMITTED: Application already submitted
```

---

## 6. Open Questions & Assumptions

### 6.1 Open Questions

| # | Question | Impact | Owner |
|---|----------|--------|-------|
| 1 | What is the exact FCRA disclosure text for credit authorization? | Legal compliance | Legal |
| 2 | Should Quick App be embeddable as iframe on partner sites? | Technical architecture | Product |
| 3 | What is the session timeout duration for forms? | UX, data loss prevention | Product |
| 4 | Should we support document camera capture on mobile? | Mobile UX | Product |
| 5 | What analytics events should be tracked? | Reporting | Product |

### 6.2 Assumptions Made

| # | Assumption | Rationale |
|---|------------|-----------|
| 1 | Google Places API is available and funded | Required for address autocomplete |
| 2 | E-signature via typed name is legally sufficient | Standard for online forms |
| 3 | PFS can be completed in-app OR uploaded | Flexibility for users |
| 4 | Maximum 5 co-guarantors supported | PRD states "up to 5" |
| 5 | All currency fields are USD | Single-market product |
| 6 | SSN validation is format-only (no verification) | Verification happens in Phase 3-4 |

### 6.3 Dependencies on External Systems

| System | Dependency Type | Fallback |
|--------|-----------------|----------|
| Google Places API | Address autocomplete | Manual address entry |
| Google OAuth | Existing client login | Email/password auth |
| SendGrid | Email notifications | Queue for retry |
| Google Drive | Document storage | S3 backup |

---

## 7. Implementation Checklist

### 7.1 Phase 1 (Quick App)

- [ ] Landing page with loan type cards
- [ ] Quick App multi-step form
- [ ] Address autocomplete integration
- [ ] Pre-qualification logic engine
- [ ] Result pages (qualified/disqualified)
- [ ] Email notifications (submission, qualification)
- [ ] Mobile responsive design
- [ ] Form validation (Zod schemas)
- [ ] API endpoints

### 7.2 Phase 2 (Full Application)

- [ ] Full Application form (Fix & Flip)
- [ ] Full Application form (Ground-Up)
- [ ] Full Application form (DSCR)
- [ ] Entity section with ownership table
- [ ] Guarantor forms with background questions
- [ ] Personal Financial Statement (in-app + upload)
- [ ] Credit authorization with e-signature
- [ ] Scope of Work builder
- [ ] SREO table (current + sold)
- [ ] Document upload integration
- [ ] Auto-save functionality
- [ ] Existing client pre-fill
- [ ] Application review page
- [ ] Submission confirmation
- [ ] API endpoints

### 7.3 Testing

- [ ] Unit tests: Form validation logic
- [ ] Unit tests: Pre-qualification rules
- [ ] Unit tests: Pre-fill mapping
- [ ] Unit tests: Calculations (PFS, ownership)
- [ ] Integration tests: API endpoints
- [ ] Integration tests: OAuth flow
- [ ] Integration tests: Document upload
- [ ] E2E tests: New client flow
- [ ] E2E tests: Existing client flow
- [ ] E2E tests: Disqualification flow
- [ ] E2E tests: Multi-property submission
- [ ] E2E tests: Mobile flow

---

## 8. UW Manual Integration

This section maps Phase 1-2 implementation components to the USDV Underwriting Manual sections. Reference these manual sections when implementing validation logic, eligibility rules, and business logic.

### 8.1 Manual Section Cross-References

| Implementation Component | UW Manual Section | Usage |
|--------------------------|-------------------|-------|
| **Quick App Pre-Qualification** | | |
| Loan product eligibility | Section 1: Investment Philosophy | RTL vs DSCR product determination |
| Property type validation | Section 5: Property Eligibility | Eligible property types, ineligible properties |
| Property location check | Section 5.3: Location Requirements | State/market eligibility, rural restrictions |
| Borrower citizenship pre-check | Section 2.2: Citizenship Requirements | US Citizen, Perm Resident, FN, ITIN rules |
| Experience tier assessment | Section 2.3: Experience Scoring | Experience calculation methodology |
| **Full Application - Borrower** | | |
| Borrower data validation | Section 2: Borrower Eligibility | Required fields, eligibility criteria |
| Credit authorization | Section 4: Credit & Background | Credit pull requirements, consent |
| Experience documentation | Section 2.3: Experience Scoring | Track record validation, project counting |
| Citizenship documentation | Section 2.2: Citizenship Requirements | Acceptable ID by citizenship type |
| Financial statement review | Section 2.4: Liquidity Requirements | PFS requirements, reserve calculations |
| **Full Application - Entity** | | |
| Entity type validation | Section 3.1: Entity Types | LLC, Corp, Trust, Series LLC rules |
| Ownership structure | Section 3.2: Ownership Structure | Percentage rules, multi-tier entities |
| Guarantor identification | Section 3.3: Guarantor Requirements | Key principal identification |
| Entity documentation | Section 3.4: Entity Documentation | Required entity docs by type |
| Good standing requirements | Section 3.5: Currency Requirements | State registration currency |
| **Full Application - Property** | | |
| Property type validation | Section 5.1: Property Types | SFR, Condo, 2-4 Unit, 5-9 Unit rules |
| Property characteristics | Section 5.2: Property Characteristics | Size, units, acreage limits |
| RTL property specifics | Section 6: RTL Property Analysis | Rehab scope, ARV, exit strategy |
| DSCR property specifics | Section 7: DSCR Property & Income | Rent, lease status, income analysis |
| Property condition assessment | Section 5.4: Condition Ratings | C1-C6 rating criteria |
| **Full Application - Loan** | | |
| Loan purpose validation | Section 1.3: Loan Purposes | Purchase, R&T Refi, Cash-Out rules |
| Loan amount limits | Section 1.4: Loan Parameters | Min/max by product |
| Term selection | Section 1.5: Term Structures | Available terms by product |
| Exit strategy validation | Section 6.4: Exit Strategy | RTL exit requirements |

### 8.2 Python Library Integration

Use these Python classes from `USDV_Underwriting_Manual/python/usdv_underwriting/` for validation:

| Validation Need | Python Class | Method |
|-----------------|--------------|--------|
| Property eligibility | `PropertyEligibilityChecker` | `check_property_type()`, `check_location()` |
| Borrower classification | `BorrowerClassifier` | `calculate_experience_score()`, `get_classification()` |
| DSCR calculations | `DSCRCalculator` | `calculate_qualifying_rent()`, `calculate_dscr()` |

### 8.3 Key Thresholds from Manual

Reference these thresholds in pre-qualification logic:

| Parameter | RTL | DSCR | Manual Reference |
|-----------|-----|------|------------------|
| Minimum FICO | 660 | 680 | Section 4.1 |
| Minimum Loan Amount | $100,000 | $100,000 | Section 1.4 |
| Maximum Loan Amount | $3,000,000 | $3,000,000 | Section 1.4 |
| Minimum Experience (Tier 1) | 5 projects | N/A | Section 2.3 |
| Minimum Liquidity | 6 months PITIA | 6 months PITIA | Section 2.4 |

### 8.4 Glossary Integration

Use Section 16 (Glossary) for:
- Tooltip definitions in UI
- Help text for form fields
- AI context for document analysis
- User education content

**Key Terms to Define in UI:**
- LTV, LTC, LTARV, DSCR
- As-Is Value, ARV
- Fix & Flip, Ground-Up, Bridge, DSCR
- Key Principal, Guarantor
- Experience Score, Borrower Classification

---

*End of Phase 1-2 Implementation Plan*

