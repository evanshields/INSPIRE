# Phase 3-4 Implementation Plan: Deal Sizing & Quote Generation

**Document Version:** 1.0  
**PRD Reference:** INSPIRE Phase 3-4 PRD  
**Last Updated:** December 2024  
**Status:** Implementation Ready

---

## 1. Executive Summary

### 1.1 Phase Overview

Phase 3-4 transforms application data into actionable loan options:
- **Phase 3: Deal Sizing** - Automated loan structuring, leverage calculations, and pricing
- **Phase 4: Quote Generation & Term Sheet** - Multi-option quotes, borrower selection, e-signature, deposit collection

### 1.2 Success Metrics (from PRD)

| Metric | Target |
|--------|--------|
| Time from Full App to Sized Deal | <5 minutes |
| Sizing accuracy vs. manual Excel | >99% |
| Quote-to-Term Sheet conversion | >70% |
| Term sheet turnaround (selection → signed) | <24 hours |
| Deposit collection rate | >90% within 48 hours |

### 1.3 Key Dependencies

| Dependency | Status | Notes |
|------------|--------|-------|
| Phase 1-2 Complete | Required | Full Application data needed |
| Eastview RTL Sizer Logic | Available | Guidelines extracted |
| Eastview DSCR Sizer Logic | Available | Guidelines extracted |
| Dropbox Sign | Required | E-signature integration |
| Stripe | Required | Payment processing |

---

## 2. Page/Screen Inventory

### 2.1 Complete Page List

| Page ID | Page Name | Route | User Role | Entry Point |
|---------|-----------|-------|-----------|-------------|
| P3-01 | Deal Sizing View | `/deals/:id/sizing` | Internal | Deal detail, auto after Full App |
| P3-02 | Manual Sizing Override | `/deals/:id/sizing/edit` | Internal | Sizing view |
| P3-03 | Rate Lock Management | `/deals/:id/rate-lock` | Internal | Sizing view |
| P4-01 | Quote Generation | `/deals/:id/quotes/generate` | Internal | Sizing view |
| P4-02 | Quote Presentation (Borrower) | `/quotes/:dealId/:token` | Public | Email link |
| P4-03 | Quote Selection Confirmation | `/quotes/:dealId/:token/confirm` | Public | Quote selection |
| P4-04 | Term Sheet View | `/deals/:id/term-sheet` | Internal | After quote selection |
| P4-05 | Deposit Payment (Borrower) | `/payment/:dealId/:token` | Public | Term sheet signed |
| P4-06 | Payment Confirmation | `/payment/:dealId/:token/success` | Public | Payment complete |

### 2.2 Navigation Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PHASE 3-4 FLOWS                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  INTERNAL FLOW (LO/Processor)                                                │
│  ────────────────────────────                                                │
│  Full App Submitted → Auto-Size → Review Sizing → Generate Quotes →          │
│  Send to Borrower → Track Selection → View Term Sheet → Track Deposit        │
│                                                                              │
│  BORROWER FLOW                                                               │
│  ─────────────                                                               │
│  Receive Quote Email → View Quote Options → Select Option → Confirm →        │
│  Sign Term Sheet (Dropbox Sign) → Pay Deposit (Stripe) → Confirmation        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Per-Page Specifications

---

### 3.1 P3-01: Deal Sizing View

#### 3.1.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Display automated sizing results and allow adjustments |
| **User Roles** | Loan Officer, Processor, Underwriter |
| **Entry Points** | Deal detail page, Pipeline card, Auto-redirect after Full App |
| **PRD Reference** | Phase 3-4 PRD, Section 3.1-3.7 |

#### 3.1.2 Information Architecture

**Primary Data:** SizingResult

**Content Hierarchy:**
1. Deal header (property, borrower, loan type)
2. Borrower classification (RTL) or DSCR metrics
3. Leverage metrics (LTV, LTC, LTARV, DSCR)
4. Loan structure (amounts, holdback)
5. Pricing (rate, points, YSP)
6. Leverage reductions applied
7. LLPAs applied
8. Eligibility status
9. Action buttons

#### 3.1.3 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `card` | Metric cards, section containers |
| `badge` | Classification badge (A+, A, B, C), status badges |
| `table` | Leverage reductions, LLPAs |
| `button` | Generate Quotes, Edit Sizing, Rate Lock |
| `alert` | Warnings, ineligibility reasons |
| `tooltip` | Metric explanations |
| `tabs` | Switch between investors (Eastview, ArchWest) |
| `separator` | Section dividers |
| `progress` | LTV/LTC/LTARV visual bars |

**React Custom Components:**

```typescript
// components/sizing/SizingResultCard.tsx
interface SizingResultCardProps {
  sizing: SizingResult;
  onEdit: () => void;
  onGenerateQuotes: () => void;
  onRateLock: () => void;
}

// Main sizing display component
// Composition: Uses ShadCN Card, Badge, Button, Table
```

```typescript
// components/sizing/BorrowerClassificationCard.tsx
interface BorrowerClassificationCardProps {
  classification: 'A+' | 'A' | 'B' | 'C';
  creditScore: number;
  experienceScore: number;
  creditDecisionScore: number;
  verifiedExperienceScore: number;
}

// RTL borrower classification display
// Composition: Uses ShadCN Card, Badge, Progress
```

```typescript
// components/sizing/LeverageMetricsCard.tsx
interface LeverageMetricsCardProps {
  metrics: {
    asIsLTV: number;
    maxAsIsLTV: number;
    ltc?: number;
    maxLTC?: number;
    ltarv?: number;
    maxLTARV?: number;
    dscr?: number;
    minDSCR?: number;
  };
  loanType: 'rtl' | 'dscr';
}

// Visual leverage metrics with progress bars
// Composition: Uses ShadCN Card, Progress
```

```typescript
// components/sizing/LoanStructureCard.tsx
interface LoanStructureCardProps {
  initialAmount: number;
  rehabHoldback?: number;
  totalAmount: number;
  term: string;
  rateType: string;
  amortization: string;
}

// Loan structure breakdown
// Composition: Uses ShadCN Card, Table
```

```typescript
// components/sizing/PricingCard.tsx
interface PricingCardProps {
  interestRate: number;
  basePrice: number;
  llpaTotal: number;
  finalPrice: number;
  originationPoints: number;
  ysp: number;
  llpasApplied: { name: string; adjustment: number }[];
}

// Pricing breakdown with LLPAs
// Composition: Uses ShadCN Card, Table, Accordion
```

```typescript
// components/sizing/LeverageReductionsTable.tsx
interface LeverageReductionsTableProps {
  reductions: {
    condition: string;
    reduction: number;
    applied: boolean;
  }[];
}

// Table of leverage reductions
// Composition: Uses ShadCN Table, Badge
```

```typescript
// components/sizing/EligibilityAlert.tsx
interface EligibilityAlertProps {
  isEligible: boolean;
  ineligibilityReasons: string[];
}

// Eligibility status with reasons
// Composition: Uses ShadCN Alert
```

#### 3.1.4 Data Requirements

**Data Model (TypeScript Interface):**

```typescript
interface SizingResult {
  id: string;
  dealId: string;
  loanType: 'fix_flip' | 'bridge' | 'ground_up' | 'dscr';
  investor: 'eastview' | 'archwest';
  
  // Borrower Classification (RTL only)
  borrowerClassification?: 'A+' | 'A' | 'B' | 'C';
  creditDecisionScore?: number;
  verifiedExperienceScore?: number;
  
  // Input values
  creditScore: number;
  experienceDeals: number;
  asIsValue: number;
  arv: number;
  purchasePrice?: number;
  rehabBudget?: number;
  constructionBudget?: number;
  
  // DSCR specific
  monthlyRent?: number;
  monthlyPITIA?: number;
  
  // Leverage Metrics
  asIsLTV: number;
  maxAsIsLTV: number;
  ltc?: number;
  maxLTC?: number;
  ltarv?: number;
  maxLTARV?: number;
  dscr?: number;
  minDSCR?: number;
  
  // Loan Structure
  maxLoanAmount: number;
  initialLoanAmount: number;
  rehabHoldback?: number;
  totalLoanAmount: number;
  
  // Pricing
  interestRate: number;
  basePrice: number;
  llpaTotal: number;
  finalPrice: number;
  
  // USDV Economics
  originationPoints: number;
  originationFee: number;
  ysp: number;
  yspAmount: number;
  
  // Constraints Applied
  leverageReductions: {
    condition: string;
    reduction: number;
    applied: boolean;
  }[];
  llpasApplied: {
    name: string;
    adjustment: number;
  }[];
  
  // Validation
  isEligible: boolean;
  ineligibilityReasons: string[];
  
  // Rate Lock
  rateLock?: RateLock;
  
  createdAt: Date;
  updatedAt: Date;
}

interface RateLock {
  id: string;
  lockedRate: number;
  lockedPrice: number;
  lockDate: Date;
  expirationDate: Date;
  status: 'active' | 'expired' | 'exercised';
  extensions: {
    date: Date;
    newExpiration: Date;
    cost: number;
  }[];
}
```

**Computed/Derived Fields:**
- `borrowerClassification`: Calculated from creditDecisionScore + verifiedExperienceScore
- `maxLoanAmount`: MIN(asIsValue × maxLTV, costBasis × maxLTC, ARV × maxLTARV)
- `finalPrice`: basePrice + llpaTotal
- `originationFee`: totalLoanAmount × originationPoints
- `yspAmount`: totalLoanAmount × ysp

#### 3.1.5 State Management

| State | Type | Scope | Notes |
|-------|------|-------|-------|
| sizing | SizingResult | Page | From API |
| selectedInvestor | string | Component | Tab selection |
| isLoading | boolean | Page | While fetching |
| showRateLockModal | boolean | Component | Rate lock modal |

**URL Parameters:**
- `?investor=eastview|archwest` - Pre-select investor tab

#### 3.1.6 Interactions & Behaviors

| User Action | System Response | Navigation |
|-------------|-----------------|------------|
| View page | Fetch sizing result, display | None |
| Switch investor tab | Re-run sizing with new investor | Update URL param |
| Click "Edit Sizing" | Open edit modal/page | `/deals/:id/sizing/edit` |
| Click "Generate Quotes" | Navigate to quote generation | `/deals/:id/quotes/generate` |
| Click "Rate Lock" | Open rate lock modal | None |
| Confirm rate lock | Lock rate, update display | None |

**API Calls:**
```typescript
// GET /api/deals/:id/sizing
// Get sizing results
interface GetSizingResponse {
  sizing: SizingResult;
  availableInvestors: string[];
}

// POST /api/deals/:id/size
// Run sizing engine
interface RunSizingRequest {
  investor?: string;
}

interface RunSizingResponse {
  sizing: SizingResult;
}

// POST /api/deals/:id/rate-lock
// Initiate rate lock
interface RateLockRequest {
  lockPeriodDays: number; // 30, 60, 90
}

interface RateLockResponse {
  rateLock: RateLock;
}
```

#### 3.1.7 All States

**Loading State:**
- Skeleton cards for all sections
- "Calculating deal sizing..." message

**Eligible State:**
- Green status badge
- All metrics displayed
- "Generate Quotes" button enabled

**Ineligible State:**
- Red status badge
- Ineligibility reasons in alert
- "Generate Quotes" button disabled
- "Request Exception" button shown

**Rate Locked State:**
- Rate lock badge with expiration countdown
- "Extend Lock" button if approaching expiration
- Locked rate highlighted

**Edge Cases:**
| Scenario | Handling |
|----------|----------|
| Missing appraisal value | Show warning, use application estimate |
| FICO below all thresholds | Show ineligible with exception option |
| Heavy rehab detected | Apply reduction, show warning |
| Loan amount exceeds max | Cap at max, show notice |

#### 3.1.8 Mock Data Examples

**RTL Fix & Flip Sizing:**
```json
{
  "id": "sizing_abc123",
  "dealId": "deal_abc123",
  "loanType": "fix_flip",
  "investor": "eastview",
  
  "borrowerClassification": "A",
  "creditDecisionScore": 3,
  "verifiedExperienceScore": 5,
  
  "creditScore": 720,
  "experienceDeals": 8,
  "asIsValue": 350000,
  "arv": 525000,
  "purchasePrice": 340000,
  "rehabBudget": 85000,
  
  "asIsLTV": 85.0,
  "maxAsIsLTV": 85.0,
  "ltc": 85.0,
  "maxLTC": 85.0,
  "ltarv": 68.6,
  "maxLTARV": 70.0,
  
  "maxLoanAmount": 425000,
  "initialLoanAmount": 340000,
  "rehabHoldback": 85000,
  "totalLoanAmount": 425000,
  
  "interestRate": 11.5,
  "basePrice": 100.0,
  "llpaTotal": 0,
  "finalPrice": 100.0,
  
  "originationPoints": 2.0,
  "originationFee": 8500,
  "ysp": 1.5,
  "yspAmount": 6375,
  
  "leverageReductions": [
    { "condition": "Heavy Rehab (Class A/B)", "reduction": 5.0, "applied": false },
    { "condition": "Loan Amount $2M-$3M", "reduction": 5.0, "applied": false },
    { "condition": "HPA Decline 0-10%", "reduction": 5.0, "applied": false }
  ],
  "llpasApplied": [],
  
  "isEligible": true,
  "ineligibilityReasons": [],
  
  "createdAt": "2024-12-10T14:30:00Z",
  "updatedAt": "2024-12-10T14:30:00Z"
}
```

**DSCR Sizing:**
```json
{
  "id": "sizing_xyz789",
  "dealId": "deal_xyz789",
  "loanType": "dscr",
  "investor": "eastview",
  
  "creditScore": 740,
  "asIsValue": 425000,
  "arv": 425000,
  
  "monthlyRent": 3200,
  "monthlyPITIA": 2568,
  "dscr": 1.25,
  "minDSCR": 1.0,
  
  "asIsLTV": 75.0,
  "maxAsIsLTV": 80.0,
  
  "maxLoanAmount": 340000,
  "initialLoanAmount": 318750,
  "totalLoanAmount": 318750,
  
  "interestRate": 7.25,
  "basePrice": 101.499,
  "llpaTotal": 0.375,
  "finalPrice": 101.874,
  
  "originationPoints": 1.5,
  "originationFee": 4781.25,
  "ysp": 1.874,
  "yspAmount": 5975.44,
  
  "llpasApplied": [
    { "name": "FICO 740-759 at 75% LTV", "adjustment": 0.125 },
    { "name": "DSCR ≥1.15", "adjustment": 0.50 },
    { "name": "5-Year Stepdown Prepay", "adjustment": 0.50 }
  ],
  
  "isEligible": true,
  "ineligibilityReasons": [],
  
  "createdAt": "2024-12-10T15:00:00Z",
  "updatedAt": "2024-12-10T15:00:00Z"
}
```

---

### 3.2 P4-01: Quote Generation

#### 3.2.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Generate and configure quote options for borrower |
| **User Roles** | Loan Officer, Processor |
| **Entry Points** | Sizing view "Generate Quotes" button |
| **PRD Reference** | Phase 3-4 PRD, Section 4.2-4.3 |

#### 3.2.2 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `card` | Quote option cards |
| `checkbox` | Select options to include |
| `select` | Prepayment structure, term options |
| `input` | Custom loan amount, rate |
| `button` | Generate, Send to Borrower |
| `switch` | Toggle options on/off |
| `slider` | LTV adjustment |
| `dialog` | Confirmation before sending |

**React Custom Components:**

```typescript
// components/quotes/QuoteGenerator.tsx
interface QuoteGeneratorProps {
  dealId: string;
  sizing: SizingResult;
  onGenerate: (quotes: Quote[]) => void;
  onSend: (quotes: Quote[]) => void;
}

// Quote generation interface
// Composition: Uses ShadCN Card, Select, Button
```

```typescript
// components/quotes/QuoteOptionCard.tsx
interface QuoteOptionCardProps {
  quote: Quote;
  optionNumber: number;
  isSelected: boolean;
  onToggle: () => void;
  onEdit: () => void;
}

// Individual quote option display
// Composition: Uses ShadCN Card, Checkbox, Button
```

```typescript
// components/quotes/DSCRQuoteConfigurator.tsx
interface DSCRQuoteConfiguratorProps {
  sizing: SizingResult;
  onConfigChange: (config: DSCRQuoteConfig) => void;
}

interface DSCRQuoteConfig {
  prepaymentStructures: string[];
  ltvTiers: number[];
  includeCashOut: boolean;
  includeInterestOnly: boolean;
  rateTypes: string[];
}

// DSCR-specific quote configuration
// Composition: Uses ShadCN Checkbox, Select, Switch
```

#### 3.2.3 Data Requirements

```typescript
interface Quote {
  id: string;
  dealId: string;
  quoteNumber: number;
  optionName: string; // "Lowest Rate", "Most Flexibility", etc.
  
  // Loan Terms
  loanAmount: number;
  interestRate: number;
  loanTerm: number; // months
  rateType: 'fixed' | '5_1_arm' | '7_1_arm';
  
  // Payment Structure
  amortization: 'interest_only' | 'amortizing';
  interestOnlyPeriod?: number;
  monthlyPayment: number;
  
  // Prepayment (DSCR)
  prepaymentStructure?: string;
  prepaymentType?: 'step_down' | 'level' | 'min_interest';
  prepaymentYears?: number;
  
  // Leverage
  ltv: number;
  ltc?: number;
  ltarv?: number;
  dscr?: number;
  
  // Cash Flow
  cashOutAmount?: number;
  
  // Economics
  originationPoints: number;
  originationFee: number;
  ysp: number;
  yspAmount: number;
  estimatedClosingCosts: number;
  cashToClose: number;
  
  // Status
  status: 'draft' | 'presented' | 'selected' | 'expired';
  expiresAt: Date;
  
  createdAt: Date;
}
```

#### 3.2.4 Mock Data - Generated Quotes

```json
{
  "quotes": [
    {
      "id": "quote_001",
      "dealId": "deal_xyz789",
      "quoteNumber": 1,
      "optionName": "Lowest Rate",
      "loanAmount": 318750,
      "interestRate": 7.25,
      "loanTerm": 360,
      "rateType": "fixed",
      "amortization": "interest_only",
      "interestOnlyPeriod": 120,
      "monthlyPayment": 1926.56,
      "prepaymentStructure": "5-4-3-2-1",
      "prepaymentType": "step_down",
      "prepaymentYears": 5,
      "ltv": 75,
      "dscr": 1.25,
      "originationPoints": 1.5,
      "originationFee": 4781.25,
      "estimatedClosingCosts": 12350,
      "cashToClose": 127850,
      "status": "draft",
      "expiresAt": "2024-12-12T14:30:00Z"
    },
    {
      "id": "quote_002",
      "dealId": "deal_xyz789",
      "quoteNumber": 2,
      "optionName": "Most Flexibility",
      "loanAmount": 318750,
      "interestRate": 7.50,
      "loanTerm": 360,
      "rateType": "fixed",
      "amortization": "interest_only",
      "interestOnlyPeriod": 120,
      "monthlyPayment": 1992.19,
      "prepaymentStructure": "3-2-1",
      "prepaymentType": "step_down",
      "prepaymentYears": 3,
      "ltv": 75,
      "dscr": 1.21,
      "originationPoints": 1.5,
      "originationFee": 4781.25,
      "estimatedClosingCosts": 12350,
      "cashToClose": 128100,
      "status": "draft",
      "expiresAt": "2024-12-12T14:30:00Z"
    },
    {
      "id": "quote_003",
      "dealId": "deal_xyz789",
      "quoteNumber": 3,
      "optionName": "Max Proceeds",
      "loanAmount": 340000,
      "interestRate": 7.75,
      "loanTerm": 360,
      "rateType": "fixed",
      "amortization": "interest_only",
      "interestOnlyPeriod": 120,
      "monthlyPayment": 2195.83,
      "prepaymentStructure": "5-4-3-2-1",
      "prepaymentType": "step_down",
      "prepaymentYears": 5,
      "ltv": 80,
      "dscr": 1.10,
      "cashOutAmount": 21250,
      "originationPoints": 2.0,
      "originationFee": 6800,
      "estimatedClosingCosts": 13100,
      "cashToClose": 103100,
      "status": "draft",
      "expiresAt": "2024-12-12T14:30:00Z"
    }
  ]
}
```

---

### 3.3 P4-02: Quote Presentation (Borrower-Facing)

#### 3.3.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Present quote options to borrower for selection |
| **User Roles** | Borrower (public, authenticated via token) |
| **Entry Points** | Email link with secure token |
| **PRD Reference** | Phase 3-4 PRD, Section 4.3 |

#### 3.3.2 Information Architecture

**Content Hierarchy:**
1. USDV branding header
2. Property summary
3. Quote cards (1-5 options)
4. Comparison table
5. Expiration countdown
6. Contact information

#### 3.3.3 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `card` | Quote option cards |
| `badge` | "Recommended", "Lowest Rate" labels |
| `button` | Select option |
| `table` | Comparison table |
| `alert` | Expiration warning |
| `dialog` | Selection confirmation |
| `separator` | Section dividers |

**React Custom Components:**

```typescript
// components/quotes/BorrowerQuotePage.tsx
interface BorrowerQuotePageProps {
  dealId: string;
  token: string;
}

// Public quote presentation page
// Composition: Uses ShadCN Card, Table, Button, Dialog
```

```typescript
// components/quotes/QuoteCard.tsx
interface QuoteCardProps {
  quote: Quote;
  optionNumber: number;
  isRecommended?: boolean;
  onSelect: () => void;
}

// Individual quote card for borrower view
// Composition: Uses ShadCN Card, Badge, Button
```

```typescript
// components/quotes/QuoteComparisonTable.tsx
interface QuoteComparisonTableProps {
  quotes: Quote[];
  highlightedFields?: string[];
}

// Side-by-side comparison
// Composition: Uses ShadCN Table
```

```typescript
// components/quotes/ExpirationCountdown.tsx
interface ExpirationCountdownProps {
  expiresAt: Date;
  onExpired: () => void;
}

// Countdown timer with urgency styling
// Composition: Uses ShadCN Badge
```

```typescript
// components/quotes/SelectionConfirmationDialog.tsx
interface SelectionConfirmationDialogProps {
  quote: Quote;
  open: boolean;
  onConfirm: () => void;
  onCancel: () => void;
}

// Confirmation modal before selection
// Composition: Uses ShadCN Dialog, Button
```

#### 3.3.4 Responsive Design

| Breakpoint | Layout |
|------------|--------|
| Desktop | 3-column quote cards, side-by-side comparison |
| Tablet | 2-column cards, scrollable comparison |
| Mobile | Stacked cards, swipeable, simplified comparison |

#### 3.3.5 Mock Data - Borrower View

```json
{
  "deal": {
    "propertyAddress": "123 Main Street, Miami, FL 33139",
    "loanType": "DSCR Rental",
    "borrowerName": "John Smith"
  },
  "quotes": [
    {
      "optionNumber": 1,
      "optionName": "Lowest Rate",
      "interestRate": 7.25,
      "loanAmount": 318750,
      "monthlyPayment": 1926.56,
      "ltv": 75,
      "prepaymentStructure": "5-4-3-2-1 Step-down",
      "term": "30 Years",
      "amortization": "10-Year Interest Only",
      "originationFee": 4781.25,
      "estimatedClosingCosts": 12350,
      "cashToClose": 127850,
      "isRecommended": true
    },
    {
      "optionNumber": 2,
      "optionName": "Most Flexibility",
      "interestRate": 7.50,
      "loanAmount": 318750,
      "monthlyPayment": 1992.19,
      "ltv": 75,
      "prepaymentStructure": "3-2-1 Step-down",
      "term": "30 Years",
      "amortization": "10-Year Interest Only",
      "originationFee": 4781.25,
      "estimatedClosingCosts": 12350,
      "cashToClose": 128100
    }
  ],
  "expiresAt": "2024-12-12T14:30:00Z",
  "contactInfo": {
    "loName": "Sarah Johnson",
    "loPhone": "+1 (305) 555-1234",
    "loEmail": "sarah@usdvcapital.com"
  }
}
```

---

### 3.4 P4-04: Term Sheet View

#### 3.4.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Display generated term sheet and track signature status |
| **User Roles** | Loan Officer, Processor |
| **Entry Points** | Deal detail, after quote selection |
| **PRD Reference** | Phase 3-4 PRD, Section 4.5-4.6 |

#### 3.4.2 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `card` | Term sheet preview, status card |
| `badge` | Signature status |
| `button` | Send for Signature, Resend, Download |
| `alert` | Status updates |
| `tabs` | View term sheet, signature history |

**React Custom Components:**

```typescript
// components/termsheet/TermSheetView.tsx
interface TermSheetViewProps {
  dealId: string;
  termSheet: TermSheet;
  onSendForSignature: () => void;
  onResend: () => void;
}

// Term sheet display and management
// Composition: Uses ShadCN Card, Badge, Button, Tabs
```

```typescript
// components/termsheet/SignatureStatusCard.tsx
interface SignatureStatusCardProps {
  status: 'pending' | 'sent' | 'viewed' | 'signed' | 'declined' | 'expired';
  sentAt?: Date;
  viewedAt?: Date;
  signedAt?: Date;
  signers: {
    name: string;
    email: string;
    status: string;
    signedAt?: Date;
  }[];
}

// Signature tracking display
// Composition: Uses ShadCN Card, Badge, Table
```

```typescript
// components/termsheet/TermSheetPreview.tsx
interface TermSheetPreviewProps {
  termSheet: TermSheet;
  showPDF?: boolean;
}

// Term sheet content preview
// Composition: Uses ShadCN Card, PDF viewer
```

#### 3.4.3 Data Requirements

```typescript
interface TermSheet {
  id: string;
  dealId: string;
  quoteId: string;
  
  // Document
  documentUrl: string;
  
  // Content
  loanAmount: number;
  interestRate: number;
  term: string;
  amortization: string;
  prepaymentPenalty?: string;
  ltv: number;
  originationFee: number;
  estimatedClosingCosts: number;
  
  // Property
  propertyAddress: string;
  propertyType: string;
  
  // Borrower
  borrowerName: string;
  entityName: string;
  guarantors: string[];
  
  // Dates
  targetCloseDate: Date;
  expiresAt: Date;
  
  // Signature (Dropbox Sign)
  signatureRequestId?: string;
  sentAt?: Date;
  viewedAt?: Date;
  signedAt?: Date;
  signedDocumentUrl?: string;
  
  status: 'draft' | 'sent' | 'viewed' | 'signed' | 'declined' | 'expired';
  
  createdAt: Date;
}
```

---

### 3.5 P4-05: Deposit Payment (Borrower-Facing)

#### 3.5.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Collect third-party report deposit from borrower |
| **User Roles** | Borrower (public, authenticated via token) |
| **Entry Points** | Email link after term sheet signed |
| **PRD Reference** | Phase 3-4 PRD, Section 4.7 |

#### 3.5.2 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `card` | Invoice summary, payment form |
| `button` | Pay Now |
| `input` | Card details (Stripe Elements) |
| `alert` | Payment status |
| `separator` | Section dividers |

**React Custom Components:**

```typescript
// components/payment/DepositPaymentPage.tsx
interface DepositPaymentPageProps {
  dealId: string;
  token: string;
}

// Deposit payment page
// Composition: Uses ShadCN Card, Stripe Elements
```

```typescript
// components/payment/InvoiceSummary.tsx
interface InvoiceSummaryProps {
  invoice: DepositInvoice;
}

// Invoice display
// Composition: Uses ShadCN Card, Table
```

```typescript
// components/payment/StripePaymentForm.tsx
interface StripePaymentFormProps {
  amount: number;
  clientSecret: string;
  onSuccess: (paymentIntent: PaymentIntent) => void;
  onError: (error: Error) => void;
}

// Stripe Elements payment form
// Composition: Uses Stripe Elements, ShadCN Button
```

#### 3.5.3 Data Requirements

```typescript
interface DepositInvoice {
  id: string;
  dealId: string;
  invoiceNumber: string;
  
  // Borrower
  borrowerName: string;
  borrowerEmail: string;
  
  // Property
  propertyAddress: string;
  
  // Amount
  amount: number;
  description: string;
  
  // Payment
  stripePaymentIntentId?: string;
  paidAt?: Date;
  paymentMethod?: string;
  
  status: 'pending' | 'paid' | 'failed' | 'refunded';
  
  createdAt: Date;
}
```

#### 3.5.4 Mock Data

```json
{
  "invoice": {
    "id": "inv_abc123",
    "dealId": "deal_abc123",
    "invoiceNumber": "INV-2024-001234",
    "borrowerName": "John Smith",
    "borrowerEmail": "john.smith@email.com",
    "propertyAddress": "123 Main Street, Miami, FL 33139",
    "amount": 2500,
    "description": "Third-Party Report Deposit (Appraisal, Title, Flood, Feasibility)",
    "status": "pending",
    "createdAt": "2024-12-10T16:00:00Z"
  },
  "disclosures": [
    "This deposit is non-refundable and covers third-party report costs.",
    "Reports will be ordered within 24 hours of payment confirmation."
  ]
}
```

---

## 4. Sizing Engine Specifications

### 4.1 RTL Sizer Logic

#### 4.1.1 Borrower Classification

```typescript
function calculateBorrowerClassification(
  fico: number,
  experienceDeals: number
): { classification: string; creditScore: number; experienceScore: number } {
  // Credit Decision Score
  let creditScore = 0;
  if (fico >= 700) creditScore = 3;
  else if (fico >= 680) creditScore = 1;
  else creditScore = 0; // <680 or Foreign National
  
  // Verified Experience Score
  let experienceScore = 0;
  if (experienceDeals >= 10) experienceScore = 7;
  else if (experienceDeals >= 3) experienceScore = 5;
  else experienceScore = 1; // 0-2 deals
  
  // Classification
  const totalScore = creditScore + experienceScore;
  let classification: string;
  if (totalScore >= 7) classification = 'A+';
  else if (totalScore >= 5) classification = 'A';
  else if (totalScore >= 2) classification = 'B';
  else classification = 'C';
  
  return { classification, creditScore, experienceScore };
}
```

#### 4.1.2 Leverage Limits

```typescript
interface LeverageLimits {
  maxAsIsLTV: number;
  maxLTC: number;
  maxLTARV: number;
}

const FIX_FLIP_PURCHASE_LIMITS: Record<string, LeverageLimits> = {
  'A+': { maxAsIsLTV: 90.0, maxLTC: 90.0, maxLTARV: 75.0 },
  'A':  { maxAsIsLTV: 85.0, maxLTC: 85.0, maxLTARV: 70.0 },
  'B':  { maxAsIsLTV: 82.5, maxLTC: 82.5, maxLTARV: 65.0 },
  'C':  { maxAsIsLTV: 75.0, maxLTC: 75.0, maxLTARV: 60.0 },
};

const FIX_FLIP_RATE_TERM_REFI_LIMITS: Record<string, LeverageLimits> = {
  'A+': { maxAsIsLTV: 75.0, maxLTC: 0, maxLTARV: 65.0 },
  'A':  { maxAsIsLTV: 72.5, maxLTC: 0, maxLTARV: 65.0 },
  'B':  { maxAsIsLTV: 70.0, maxLTC: 0, maxLTARV: 60.0 },
  'C':  { maxAsIsLTV: 60.0, maxLTC: 0, maxLTARV: 55.0 },
};

const FIX_FLIP_CASH_OUT_REFI_LIMITS: Record<string, LeverageLimits> = {
  'A+': { maxAsIsLTV: 70.0, maxLTC: 0, maxLTARV: 65.0 },
  'A':  { maxAsIsLTV: 67.5, maxLTC: 0, maxLTARV: 65.0 },
  'B':  { maxAsIsLTV: 65.0, maxLTC: 0, maxLTARV: 60.0 },
  'C':  { maxAsIsLTV: 0, maxLTC: 0, maxLTARV: 0 }, // Not eligible
};

const BRIDGE_PURCHASE_LIMITS: Record<string, LeverageLimits> = {
  'A+': { maxAsIsLTV: 82.5, maxLTC: 82.5, maxLTARV: 0 },
  'A':  { maxAsIsLTV: 80.0, maxLTC: 80.0, maxLTARV: 0 },
  'B':  { maxAsIsLTV: 80.0, maxLTC: 80.0, maxLTARV: 0 },
  'C':  { maxAsIsLTV: 75.0, maxLTC: 75.0, maxLTARV: 0 },
};

const GROUND_UP_LIMITS: LeverageLimits = {
  maxAsIsLTV: 70.0,
  maxLTC: 85.0,
  maxLTARV: 67.5,
};
```

#### 4.1.3 Leverage Reductions

```typescript
interface LeverageReduction {
  condition: string;
  reduction: number;
  check: (deal: DealData) => boolean;
}

const LEVERAGE_REDUCTIONS: LeverageReduction[] = [
  {
    condition: 'HPA Decline 0-10%',
    reduction: 5.0,
    check: (deal) => deal.hpaDecline >= 0 && deal.hpaDecline <= 10,
  },
  {
    condition: 'ZHVI Multiplier 200-300%',
    reduction: 5.0,
    check: (deal) => deal.zhviMultiplier >= 200 && deal.zhviMultiplier <= 300,
  },
  {
    condition: 'Loan Amount $2M-$3M',
    reduction: 5.0,
    check: (deal) => deal.loanAmount >= 2000000 && deal.loanAmount <= 3000000,
  },
  {
    condition: 'Heavy Rehab (Class A/B)',
    reduction: 5.0,
    check: (deal) => isHeavyRehab(deal) && ['A+', 'A', 'B'].includes(deal.classification),
  },
  {
    condition: 'Heavy Rehab (Class C)',
    reduction: 10.0,
    check: (deal) => isHeavyRehab(deal) && deal.classification === 'C',
  },
  {
    condition: 'Small Multifamily 5-9 units (RTL)',
    reduction: 5.0,
    check: (deal) => deal.units >= 5 && deal.units <= 9 && deal.loanType !== 'ground_up',
  },
  {
    condition: 'Small Multifamily 5-9 units (Construction)',
    reduction: 10.0,
    check: (deal) => deal.units >= 5 && deal.units <= 9 && deal.loanType === 'ground_up',
  },
];

function isHeavyRehab(deal: DealData): boolean {
  const baseValue = deal.loanPurpose === 'purchase' ? deal.purchasePrice : deal.asIsValue;
  return deal.rehabBudget > 50000 && deal.rehabBudget > baseValue;
}
```

#### 4.1.4 Loan Amount Calculation

```typescript
function calculateRTLLoanAmount(
  deal: DealData,
  limits: LeverageLimits,
  reductions: number
): { initialAmount: number; rehabHoldback: number; totalAmount: number } {
  // Apply reductions to limits
  const adjustedLimits = {
    maxAsIsLTV: limits.maxAsIsLTV - reductions,
    maxLTC: limits.maxLTC - reductions,
    maxLTARV: limits.maxLTARV - reductions,
  };
  
  // Calculate max by each constraint
  const maxByLTV = deal.asIsValue * (adjustedLimits.maxAsIsLTV / 100);
  const maxByLTC = deal.costBasis * (adjustedLimits.maxLTC / 100);
  const maxByLTARV = deal.arv * (adjustedLimits.maxLTARV / 100);
  
  // Initial amount is minimum of constraints
  const initialAmount = Math.min(maxByLTV, maxByLTC, maxByLTARV);
  
  // Rehab holdback (max 60% of total loan)
  const maxRehabHoldback = initialAmount * 0.6 / 0.4; // Solve for max where rehab = 60%
  const rehabHoldback = Math.min(deal.rehabBudget, maxRehabHoldback);
  
  const totalAmount = initialAmount + rehabHoldback;
  
  return { initialAmount, rehabHoldback, totalAmount };
}
```

### 4.2 DSCR Sizer Logic

#### 4.2.1 DSCR Calculation

```typescript
function calculateDSCR(
  loanAmount: number,
  interestRate: number,
  monthlyRent: number,
  annualTaxes: number,
  annualInsurance: number,
  monthlyHOA: number = 0
): number {
  const monthlyInterest = (loanAmount * (interestRate / 100)) / 12;
  const monthlyTaxes = annualTaxes / 12;
  const monthlyInsurance = annualInsurance / 12;
  
  const monthlyPITIA = monthlyInterest + monthlyTaxes + monthlyInsurance + monthlyHOA;
  
  return monthlyRent / monthlyPITIA;
}
```

#### 4.2.2 DSCR Leverage Matrix

```typescript
interface DSCRLeverageMatrix {
  [fico: string]: {
    purchase: number;
    rateTermRefi: number;
    cashOutRefi: number;
  };
}

const DSCR_LEVERAGE_MATRIX: DSCRLeverageMatrix = {
  '720+':      { purchase: 80, rateTermRefi: 80, cashOutRefi: 75 },
  '700-719':   { purchase: 75, rateTermRefi: 75, cashOutRefi: 70 },
  '680-699':   { purchase: 75, rateTermRefi: 75, cashOutRefi: 70 },
  '5+ Units':  { purchase: 75, rateTermRefi: 70, cashOutRefi: 70 },
  'Foreign':   { purchase: 65, rateTermRefi: 65, cashOutRefi: 60 },
};

const DSCR_LTV_ADJUSTMENTS = [
  { condition: '700-719 FICO with >1.20x DSCR', adjustment: 5 },
  { condition: 'Foreign National with >1.30x DSCR', adjustment: 5 },
  { condition: 'STR/Airbnb/VRBO', adjustment: -5 },
  { condition: 'Section 8 / Subsidized', adjustment: -5 },
  { condition: 'Vacant Refinance', adjustment: -5 },
  { condition: 'Luxury (>$1M UPB)', adjustment: -10 },
];
```

#### 4.2.3 DSCR Pricing (LLPA Matrix)

```typescript
interface LLPAMatrix {
  [category: string]: {
    [ltvBucket: string]: number;
  };
}

const FICO_LLPAS: LLPAMatrix = {
  '780+':    { '50': 1.000, '55': 0.875, '60': 0.750, '65': 0.625, '70': 0.500, '75': 0.375, '80': 0.125 },
  '760-779': { '50': 0.875, '55': 0.750, '60': 0.625, '65': 0.500, '70': 0.375, '75': 0.250, '80': 0.000 },
  '740-759': { '50': 0.750, '55': 0.625, '60': 0.500, '65': 0.375, '70': 0.250, '75': 0.125, '80': -0.125 },
  '720-739': { '50': 0.675, '55': 0.500, '60': 0.375, '65': 0.250, '70': 0.125, '75': 0.000, '80': -0.250 },
  '700-719': { '50': 0.500, '55': 0.375, '60': 0.250, '65': 0.125, '70': 0.000, '75': -0.250, '80': -0.500 },
  '680-699': { '50': 0.375, '55': 0.250, '60': 0.125, '65': -0.250, '70': -0.750, '75': -1.000, '80': null },
};

const PREPAY_LLPAS: Record<string, number> = {
  '7_year_min_interest': 2.000,
  '7_year_stepdown': 1.750,
  '5_year_min_interest': 0.750,
  '5_year_stepdown': 0.500,
  '3_year_stepdown': 0.000,
  '2_year_stepdown': -1.000,
  '1_year': -2.000,
  'no_prepay': -4.000,
};

function calculateDSCRPrice(
  basePrice: number,
  fico: number,
  ltv: number,
  dscr: number,
  loanAmount: number,
  loanPurpose: string,
  propertyType: string,
  prepayStructure: string,
  isInterestOnly: boolean
): { finalPrice: number; llpasApplied: { name: string; adjustment: number }[] } {
  const llpas: { name: string; adjustment: number }[] = [];
  let totalAdjustment = 0;
  
  // FICO LLPA
  const ficoBucket = getFICOBucket(fico);
  const ltvBucket = getLTVBucket(ltv);
  const ficoLLPA = FICO_LLPAS[ficoBucket]?.[ltvBucket] ?? 0;
  if (ficoLLPA !== 0) {
    llpas.push({ name: `FICO ${ficoBucket} at ${ltvBucket}% LTV`, adjustment: ficoLLPA });
    totalAdjustment += ficoLLPA;
  }
  
  // DSCR LLPA
  if (dscr >= 1.15) {
    llpas.push({ name: 'DSCR ≥1.15', adjustment: 0.50 });
    totalAdjustment += 0.50;
  } else if (dscr >= 1.00 && dscr < 1.10) {
    const dscrLLPA = getDSCRLLPA(ltv);
    if (dscrLLPA !== 0) {
      llpas.push({ name: 'DSCR 1.00-1.10', adjustment: dscrLLPA });
      totalAdjustment += dscrLLPA;
    }
  }
  
  // Prepayment LLPA
  const prepayLLPA = PREPAY_LLPAS[prepayStructure] ?? 0;
  if (prepayLLPA !== 0) {
    llpas.push({ name: `Prepay: ${prepayStructure}`, adjustment: prepayLLPA });
    totalAdjustment += prepayLLPA;
  }
  
  // Interest Only LLPA
  if (isInterestOnly && ltv > 65) {
    const ioLLPA = getIOLLPA(ltv);
    llpas.push({ name: 'Interest Only', adjustment: ioLLPA });
    totalAdjustment += ioLLPA;
  }
  
  // Additional LLPAs (loan amount, property type, etc.)
  // ... similar pattern
  
  return {
    finalPrice: basePrice + totalAdjustment,
    llpasApplied: llpas,
  };
}
```

---

## 5. API Contract (Mock)

### 5.1 Sizing Endpoints

```typescript
// POST /api/deals/:id/size
// Run sizing engine
interface SizeRequest {
  investor?: 'eastview' | 'archwest';
  overrides?: {
    asIsValue?: number;
    arv?: number;
    fico?: number;
    experience?: number;
  };
}

interface SizeResponse {
  sizing: SizingResult;
}

// GET /api/deals/:id/sizing
// Get current sizing
interface GetSizingResponse {
  sizing: SizingResult | null;
  availableInvestors: string[];
}

// PUT /api/deals/:id/sizing
// Update sizing with overrides
interface UpdateSizingRequest {
  overrides: {
    ltv?: number;
    rate?: number;
    points?: number;
  };
  exceptionNotes?: string;
}

interface UpdateSizingResponse {
  sizing: SizingResult;
  hasExceptions: boolean;
}
```

### 5.2 Rate Lock Endpoints

```typescript
// POST /api/deals/:id/rate-lock
// Initiate rate lock
interface RateLockRequest {
  lockPeriodDays: 30 | 60 | 90;
}

interface RateLockResponse {
  rateLock: RateLock;
}

// PUT /api/deals/:id/rate-lock/extend
// Extend rate lock
interface ExtendRateLockRequest {
  extensionDays: 15 | 30;
}

interface ExtendRateLockResponse {
  rateLock: RateLock;
  extensionCost: number;
}
```

### 5.3 Quote Endpoints

```typescript
// POST /api/deals/:id/quotes/generate
// Generate quote options
interface GenerateQuotesRequest {
  config?: {
    prepaymentStructures?: string[];
    ltvTiers?: number[];
    includeCashOut?: boolean;
    includeInterestOnly?: boolean;
  };
}

interface GenerateQuotesResponse {
  quotes: Quote[];
}

// GET /api/deals/:id/quotes
// Get all quotes for deal
interface GetQuotesResponse {
  quotes: Quote[];
  selectedQuote?: Quote;
}

// POST /api/deals/:id/quotes/send
// Send quotes to borrower
interface SendQuotesRequest {
  quoteIds: string[];
  expirationHours?: number;
}

interface SendQuotesResponse {
  success: boolean;
  quoteUrl: string;
  expiresAt: Date;
}

// PUT /api/quotes/:quoteId/select
// Borrower selects quote (public endpoint with token)
interface SelectQuoteRequest {
  token: string;
}

interface SelectQuoteResponse {
  success: boolean;
  termSheet: TermSheet;
}
```

### 5.4 Term Sheet Endpoints

```typescript
// POST /api/deals/:id/term-sheet
// Generate term sheet
interface GenerateTermSheetResponse {
  termSheet: TermSheet;
}

// POST /api/deals/:id/term-sheet/send
// Send for e-signature
interface SendTermSheetResponse {
  signatureRequestId: string;
  signatureUrl: string;
}

// Webhook: POST /api/webhooks/dropbox-sign
// Handle signature events
interface DropboxSignWebhook {
  event: 'signature_request_viewed' | 'signature_request_signed' | 'signature_request_declined';
  signature_request: {
    signature_request_id: string;
    // ... other fields
  };
}
```

### 5.5 Payment Endpoints

```typescript
// POST /api/deals/:id/deposit-invoice
// Generate deposit invoice
interface GenerateInvoiceResponse {
  invoice: DepositInvoice;
}

// POST /api/deals/:id/deposit/payment-intent
// Create Stripe payment intent
interface CreatePaymentIntentResponse {
  clientSecret: string;
  amount: number;
}

// Webhook: POST /api/webhooks/stripe
// Handle payment events
interface StripeWebhook {
  type: 'payment_intent.succeeded' | 'payment_intent.payment_failed';
  data: {
    object: {
      id: string;
      metadata: {
        dealId: string;
        invoiceId: string;
      };
    };
  };
}
```

---

## 6. Open Questions & Assumptions

### 6.1 Open Questions

| # | Question | Impact | Owner |
|---|----------|--------|-------|
| 1 | What is the exact term sheet template content? | Document generation | Legal |
| 2 | What Dropbox Sign template ID should be used? | E-signature integration | IT |
| 3 | What is the standard deposit amount by loan type? | Payment flow | Product |
| 4 | Should quotes auto-expire or require manual expiration? | UX | Product |

### 6.2 Assumptions Made

| # | Assumption | Rationale |
|---|------------|-----------|
| 1 | Sizing runs automatically on Full App submission | PRD states auto-size |
| 2 | Default quote expiration is 2 business days | PRD specification |
| 3 | Deposit is non-refundable | Standard industry practice |
| 4 | Rate lock default is 30 days | PRD specification |

---

## 7. Implementation Checklist

### 7.1 Phase 3 (Sizing)

- [ ] RTL Sizer engine (borrower classification)
- [ ] RTL Sizer engine (leverage limits)
- [ ] RTL Sizer engine (leverage reductions)
- [ ] RTL Sizer engine (loan amount calculation)
- [ ] DSCR Sizer engine (DSCR calculation)
- [ ] DSCR Sizer engine (leverage matrix)
- [ ] DSCR Sizer engine (LLPA calculation)
- [ ] Sizing result storage
- [ ] Sizing view UI
- [ ] Manual override functionality
- [ ] Rate lock functionality
- [ ] Rate lock alerts

### 7.2 Phase 4 (Quotes)

- [ ] Quote generation logic (RTL)
- [ ] Quote generation logic (DSCR)
- [ ] Quote generation UI
- [ ] Borrower quote page (public)
- [ ] Quote comparison table
- [ ] Quote selection flow
- [ ] Quote expiration handling

### 7.3 Phase 4 (Term Sheet)

- [ ] Term sheet generation
- [ ] Term sheet PDF template
- [ ] Dropbox Sign integration
- [ ] Signature tracking
- [ ] Webhook handlers

### 7.4 Phase 4 (Payment)

- [ ] Stripe integration
- [ ] Payment intent creation
- [ ] Borrower payment page
- [ ] Payment confirmation
- [ ] Webhook handlers
- [ ] Invoice generation

### 7.5 Testing

- [ ] Unit tests: Sizing calculations
- [ ] Unit tests: LLPA calculations
- [ ] Unit tests: Quote generation
- [ ] Integration tests: Dropbox Sign
- [ ] Integration tests: Stripe
- [ ] E2E tests: Full quote flow
- [ ] E2E tests: Payment flow

---

## 8. UW Manual Integration

This section maps Phase 3-4 implementation components to the USDV Underwriting Manual sections. These are the **most critical** manual references for this phase, as sizing and pricing logic must exactly match the manual's calculations.

### 8.1 Manual Section Cross-References

| Implementation Component | UW Manual Section | Usage |
|--------------------------|-------------------|-------|
| **RTL Deal Sizing** | | |
| Borrower classification (A+/A/B/C) | Section 2.3: Experience Scoring | Classification calculation from FICO + experience |
| Credit Decision Score | Section 9.3.1: Credit Decision Score | FICO-to-score mapping |
| Verified Experience Score | Section 9.3.2: Experience Score | Project counting rules |
| Max As-Is LTV | Section 9.4: RTL Leverage Matrices | LTV by classification and property type |
| Max LTC | Section 9.5: Cost Basis Calculation | Cost basis rules by loan purpose |
| Max LTARV | Section 9.6: LTARV Calculation | ARV-based constraint |
| Leverage reductions | Section 9.7: Leverage Adjustments | HPA, ZHVI, heavy rehab, rural, etc. |
| Rehab holdback calculation | Section 9.8: Rehab Holdback | Holdback sizing rules |
| Initial loan amount | Section 9.9: Final Loan Calculation | MIN of all constraints |
| **DSCR Deal Sizing** | | |
| Qualifying rent determination | Section 7.2: Qualifying Rent | By lease status (in-place, market, etc.) |
| PITIA calculation | Section 7.3: PITIA Components | P&I, taxes, insurance, HOA, flood |
| DSCR calculation | Section 7.4: DSCR Formula | Qualifying rent / PITIA |
| Base LTV by FICO/Purpose | Section 10.2: DSCR LTV Matrix | LTV matrix by FICO and purpose |
| LTV adjustments | Section 10.3: LTV Adjustments | DSCR, property type, cash-out, etc. |
| Minimum DSCR requirements | Section 7.5: Minimum DSCR | By FICO tier |
| **RTL Pricing** | | |
| Base interest rate | Section 11.2: RTL Pricing | Base rate structure |
| Rate adjustments | Section 11.3: RTL Adjustments | Classification, property type, etc. |
| Origination points | Section 11.4: Origination Fees | Points calculation |
| YSP calculation | Section 11.5: YSP | Yield spread premium |
| **DSCR Pricing** | | |
| Base rate (Treasury + spread) | Section 11.6: DSCR Base Rate | Treasury benchmark + margin |
| FICO LLPAs | Section 11.7: FICO LLPAs | FICO × LTV matrix |
| Property type LLPAs | Section 11.8: Property LLPAs | Condo, 2-4 unit, 5-9 unit |
| DSCR LLPAs | Section 11.9: DSCR LLPAs | By DSCR tier |
| Loan size LLPAs | Section 11.10: UPB LLPAs | Loan amount adjustments |
| Cash-out LLPAs | Section 11.11: Cash-Out LLPAs | Refi type adjustment |
| I/O LLPAs | Section 11.12: I/O LLPAs | By LTV tier |
| Prepay LLPAs | Section 11.13: Prepay LLPAs | Step-down, level, min interest |
| **Rate Lock** | | |
| Lock period options | Section 11.14: Rate Locks | Lock durations (30, 45, 60 days) |
| Extension fees | Section 11.15: Extensions | Extension costs |
| Lock expiration handling | Section 11.16: Relock | Relock process |

### 8.2 Python Library Integration

**CRITICAL:** Use these Python classes for ALL calculations. Do NOT reimplement formulas.

| Calculation Need | Python Class | Method |
|------------------|--------------|--------|
| RTL loan sizing | `RTLSizer` | `calculate_max_loan()`, `get_leverage_limits()` |
| RTL borrower classification | `RTLSizer` | `classify_borrower()` |
| DSCR calculation | `DSCRCalculator` | `calculate_dscr()`, `calculate_pitia()` |
| DSCR loan sizing | `DSCRSizer` | `calculate_max_loan()`, `apply_ltv_adjustments()` |
| RTL pricing | `RTLPricingEngine` | `calculate_rate()`, `calculate_points()` |
| DSCR pricing | `DSCRPricingEngine` | `calculate_all_llpas()`, `calculate_final_rate()` |

### 8.3 Key Formulas from Manual

**RTL Loan Amount Calculation:**
```
Loan Amount = MIN(
  As-Is Value × Max As-Is LTV,
  Cost Basis × Max LTC,
  ARV × Max LTARV
) - Leverage Reductions
```

**DSCR Calculation:**
```
DSCR = Qualifying Monthly Rent / PITIA

Where PITIA = P&I + Monthly Taxes + Monthly Insurance + Monthly HOA + Monthly Flood
```

**DSCR Final Rate:**
```
Final Rate = Base Rate + Σ(All LLPAs)

Where LLPAs include: FICO, Property Type, DSCR, Loan Size, Cash-Out, I/O, Prepay
```

### 8.4 Borrower Classification Matrix (RTL)

From Section 9.3:

| Classification | Credit Score | Experience Score | Max As-Is LTV |
|----------------|--------------|------------------|---------------|
| A+ | 3 | 3 | 90% |
| A | 3 | 2 | 87.5% |
| A | 2 | 3 | 87.5% |
| B | 3 | 1 | 85% |
| B | 2 | 2 | 85% |
| B | 1 | 3 | 85% |
| C | All other combinations | | 80% |

### 8.5 DSCR LTV Matrix

From Section 10.2 (example - reference manual for full matrix):

| FICO | Purchase | Rate & Term | Cash-Out |
|------|----------|-------------|----------|
| 780+ | 80% | 80% | 75% |
| 760-779 | 80% | 80% | 75% |
| 740-759 | 75% | 75% | 70% |
| 720-739 | 75% | 75% | 70% |
| 700-719 | 70% | 70% | 65% |
| 680-699 | 65% | 65% | 60% |

### 8.6 Validation Requirements

Implement these validation checks from the manual:

| Check | Manual Reference | Action if Failed |
|-------|------------------|------------------|
| FICO ≥ 660 (RTL) | Section 4.1 | Disqualify |
| FICO ≥ 680 (DSCR) | Section 4.1 | Disqualify |
| DSCR ≥ 1.0 | Section 7.5 | Disqualify or exception |
| Loan Amount ≥ $100K | Section 1.4 | Disqualify |
| Loan Amount ≤ $3M | Section 1.4 | Disqualify or exception |
| LTV ≤ Max for classification | Section 9/10 | Reduce loan amount |

---

*End of Phase 3-4 Implementation Plan*

