# INSPIRE - Phase 3-4 Product Requirements Document

**Product Name:** INSPIRE  
**Company:** USDV Capital  
**Document Type:** Phase 3-4 PRD (Deal Sizing + Quote & Term Sheet)  
**Version:** 1.0  
**Last Updated:** November 2025

---

## 1. Overview

This PRD covers Phases 3 and 4 of INSPIRE's loan origination workflow:

- **Phase 3: Deal Sizing** - Automated loan structuring and pricing calculations
- **Phase 4: Quote Generation & Term Sheet** - Multi-option quote presentation, borrower selection, automated term sheet, e-signature, and deposit collection

These phases transform application data into actionable loan options and secure borrower commitment.

---

## 2. Goals & Success Metrics

### Goals

1. Eliminate manual Excel-based deal sizing
2. Auto-populate sizers from Full Application data
3. Generate multiple quote scenarios for borrower flexibility
4. Automate term sheet generation and e-signature
5. Streamline deposit collection to accelerate deal progression

### Success Metrics

| Metric | Target |
|--------|--------|
| Time from Full App to Sized Deal | <5 minutes |
| Sizing accuracy vs. manual Excel | >99% |
| Quote-to-Term Sheet conversion | >70% |
| Term sheet turnaround (selection → signed) | <24 hours |
| Deposit collection rate | >90% within 48 hours |

---

## 3. Phase 3: Deal Sizing

### 3.1 Overview

Deal sizing takes application data and calculates loan structure, leverage limits, interest rate, and economics based on investor guidelines. INSPIRE replaces manual Excel sizers with an automated engine that applies the correct logic per loan type and investor.

### 3.2 Sizer Types

| Loan Type | Sizer | Investors |
|-----------|-------|-----------|
| Fix & Flip | RTL Sizer | Eastview, ArchWest |
| Ground-Up Construction | RTL Sizer (Construction) | Eastview, ArchWest |
| Bridge | RTL Sizer | Eastview, ArchWest |
| DSCR Permanent | DSCR Sizer | Eastview, ArchWest |

### 3.3 Data Pre-Fill from Full Application

The sizer auto-populates from Phase 2 data:

**Property Data:**
| Application Field | Sizer Field |
|-------------------|-------------|
| Property Address | Subject Property |
| Property Type | Property Type |
| # Units | Unit Count |
| Square Footage | GLA |

**Deal Economics:**
| Application Field | Sizer Field |
|-------------------|-------------|
| Purchase Price | Purchase Price |
| Current Market Value | As-Is Value |
| Rehab Budget Remaining | Rehab Budget |
| Rehab Completed | Completed Rehab |
| Construction Budget | Construction Budget |
| Lot Purchase Price | Lot Cost |
| ARV | After Repair Value |
| Projected Rent (DSCR) | Market Rent |
| Annual Taxes | Property Taxes |
| Annual Insurance | Insurance |
| HOA | Association Fees |

**Borrower Data:**
| Application Field | Sizer Field |
|-------------------|-------------|
| Estimated Credit Score | FICO |
| # Guarantors | Guarantor Count |
| Each Guarantor FICO | Individual FICOs |
| Experience (deals last 36mo) | Verified Experience |
| Entity Type | Borrowing Entity Type |

**Loan Request:**
| Application Field | Sizer Field |
|-------------------|-------------|
| Loan Purpose | Transaction Type |
| Loan Amount Requested | Requested Loan Amount |
| Exit Strategy | Exit Strategy |
| Target Close Date | Target Close |

---

### 3.4 RTL Sizer Logic (Fix & Flip / Bridge / Ground-Up)

#### 3.4.1 Borrower Classification

Borrower classification determines maximum leverage. Calculated as:

**Credit Decision Score:**
| FICO Range | Score |
|------------|-------|
| ≥700 | 3 |
| 680-699 | 1 |
| <680 or Foreign National | 0 |

**Verified Experience Score:**
| Experience (36 months) | Score |
|------------------------|-------|
| 10+ deals | 7 |
| 3-9 deals | 5 |
| 0-2 deals | 1 |

**Borrower Classification:**
| Total Score | Class |
|-------------|-------|
| ≥7 | A+ |
| 5-6 | A |
| 2-4 | B |
| <2 | C |

#### 3.4.2 Leverage Limits by Product & Classification

**Fix & Flip (Purchase):**
| Class | Max As-Is LTV | Max LTC | Max LTARV |
|-------|---------------|---------|-----------|
| A+ | 90.0% | 90.0% | 75.0% |
| A | 85.0% | 85.0% | 70.0% |
| B | 82.5% | 82.5% | 65.0% |
| C | 75.0% | 75.0% | 60.0% |

**Fix & Flip (Rate & Term Refinance):**
| Class | Max As-Is LTV | Max LTC | Max LTARV |
|-------|---------------|---------|-----------|
| A+ | 75.0% | N/A | 65.0% |
| A | 72.5% | N/A | 65.0% |
| B | 70.0% | N/A | 60.0% |
| C | 60.0% | N/A | 55.0% |

**Fix & Flip (Cash-Out Refinance):**
| Class | Max As-Is LTV | Max LTC | Max LTARV |
|-------|---------------|---------|-----------|
| A+ | 70.0% | N/A | 65.0% |
| A | 67.5% | N/A | 65.0% |
| B | 65.0% | N/A | 60.0% |
| C | N/A | N/A | N/A |

**Bridge (Purchase):**
| Class | Max As-Is LTV | Max LTC |
|-------|---------------|---------|
| A+ | 82.5% | 82.5% |
| A | 80.0% | 80.0% |
| B | 80.0% | 80.0% |
| C | 75.0% | 75.0% |

**Ground-Up Construction:**
| Metric | Limit |
|--------|-------|
| Max LT As-Is Value | 70.0% |
| Max LTC | 85.0% |
| Max LTARV | 67.5% |

#### 3.4.3 Leverage Reductions

Apply the following reductions cumulatively:

| Condition | Reduction |
|-----------|-----------|
| HPA decline 0-10% | -5% |
| ZHVI Multiplier 200-300% | -5% |
| Loan Amount $2M-$3M | -5% |
| Heavy Rehab (Class A/B) | -5% |
| Heavy Rehab (Class C) | -10% |
| Small Multifamily (5-9 units) | -5% (RTL) / -10% (Construction) |

**Heavy Rehab Definition:**
- Rehab budget >$50,000 AND
- Rehab budget >100% of purchase price (or as-is value for refi)

#### 3.4.4 Loan Amount Calculation

```
Initial Loan Amount = MIN(
  As-Is Value × Max LTV,
  Cost Basis × Max LTC,
  ARV × Max LTARV
)

Total Loan Amount = Initial Loan Amount + Rehab Holdback

Rehab Holdback = MIN(
  Rehab Budget,
  60% of Total Loan Amount  // Max rehab % rule
)
```

**Cost Basis Calculation:**
- Purchase: Total closing costs per HUD (excluding origination points) + assignment fees (≤5% or $40k)
- Refinance: Original purchase price + verified completed rehab

#### 3.4.5 RTL Product Parameters

| Parameter | Fix & Flip | Bridge | Bridge Plus |
|-----------|------------|--------|-------------|
| Min Loan | $100,000 | $100,000 | $100,000 |
| Max Loan | $3,000,000 | $3,000,000 | $3,000,000 |
| Term | 12-24 months | 12-24 months | 25-36 months |
| Structure | Interest Only | Interest Only | Interest Only |
| Rate Type | Fixed | Fixed | Fixed |
| Min Experience | 1 deal (36mo) | 1 deal (36mo) | 1 deal (36mo) |
| Min FICO | 660 | 660 | 660 |

---

### 3.5 DSCR Sizer Logic

#### 3.5.1 DSCR Calculation

```
DSCR = Qualifying Monthly Rent / Monthly PITIA

Monthly PITIA = Interest + Taxes + Insurance + HOA

Interest = (Loan Amount × Interest Rate) / 12
Taxes = Annual Property Taxes / 12
Insurance = Annual Insurance / 12
HOA = Monthly HOA
```

**Qualifying Rent Rules:**
| Scenario | Qualifying Rent |
|----------|-----------------|
| Leased (purchase) | MIN(In-place rent, 100% Market rent) |
| Leased (refi) | MIN(In-place rent, 100% Market rent) |
| Unleased (purchase) | 100% Market rent |
| Unleased (refi) | 90% Market rent (+ 5% LTV reduction) |
| Vacation Rental | MIN(125% Market rent, 12mo avg income) |

#### 3.5.2 Minimum DSCR Requirements

| FICO | Min DSCR |
|------|----------|
| ≥700 | 1.00x |
| <700 | 1.20x |
| 5-9 Unit | 1.20x NCF |

#### 3.5.3 DSCR Leverage Matrix

**By Credit Score & Loan Purpose:**

| FICO | Purchase | Refi (R&T) | Refi (Cash-Out) |
|------|----------|------------|-----------------|
| 720+ | 80% | 80% | 75% |
| 700-719 | 75% | 75% | 70% |
| 680-699 | 75% | 75% | 70% |
| 5+ Units | 75% | 70% | 70% |
| Foreign National | 65% | 65% | 60% |

**LTV Adjustments:**
| Condition | Adjustment |
|-----------|------------|
| 700-719 FICO with >1.20x DSCR | +5% LTV |
| Foreign National with >1.30x DSCR | +5% LTV |
| STR/Airbnb/VRBO | -5% LTV |
| Section 8 / Subsidized | -5% LTV |
| Vacant Refinance | -5% LTV |
| Luxury (>$1M UPB) | -10% LTV |

#### 3.5.4 DSCR Pricing (Eastview Matrix)

**Base Rate by Spread:**
| Spread (5YR) | Coupon | 5/1 ARM | 7/1 ARM | Fixed 30 |
|--------------|--------|---------|---------|----------|
| 4.260% | 8.000% | 104.906% | 104.906% | 104.906% |
| 3.760% | 7.500% | 103.197% | 103.197% | 103.197% |
| 3.260% | 7.000% | 101.499% | 101.499% | 101.499% |
| 2.760% | 6.500% | 99.812% | 99.812% | 99.812% |
| 2.260% | 6.000% | 98.138% | 98.138% | 98.138% |

**FICO LLPAs (Price Adjustments by LTV):**
| FICO | 50% | 55% | 60% | 65% | 70% | 75% | 80% |
|------|-----|-----|-----|-----|-----|-----|-----|
| 780+ | 1.000% | 0.875% | 0.750% | 0.625% | 0.500% | 0.375% | 0.125% |
| 760-779 | 0.875% | 0.750% | 0.625% | 0.500% | 0.375% | 0.250% | 0.000% |
| 740-759 | 0.750% | 0.625% | 0.500% | 0.375% | 0.250% | 0.125% | -0.125% |
| 720-739 | 0.675% | 0.500% | 0.375% | 0.250% | 0.125% | 0.000% | -0.250% |
| 700-719 | 0.500% | 0.375% | 0.250% | 0.125% | 0.000% | -0.250% | -0.500% |
| 680-699 | 0.375% | 0.250% | 0.125% | -0.250% | -0.750% | -1.000% | N/A |

**Additional LLPAs:**
| Adjustment | 50% | 60% | 65% | 70% | 75% | 80% |
|------------|-----|-----|-----|-----|-----|-----|
| DSCR 1.00-1.10 | 0.00% | 0.00% | 0.00% | -0.125% | -0.250% | -0.375% |
| DSCR ≥1.15 | 0.50% | 0.50% | 0.50% | 0.50% | 0.50% | 0.50% |
| UPB ≤$150k | 0.00% | 0.00% | 0.00% | -0.25% | -0.50% | -1.00% |
| UPB $2M-$3M | -0.50% | -0.75% | -1.75% | -2.00% | -3.00% | N/A |
| Cash-Out Refi | 0.00% | 0.00% | -0.25% | -0.375% | -0.375% | -6.00% |
| Condo | 0.00% | 0.00% | 0.00% | -0.25% | -0.50% | -1.00% |
| 2-4 Unit | 0.00% | 0.00% | 0.00% | -0.25% | -0.50% | -1.00% |
| 5-9 Unit | -4.00% | -4.50% | -5.375% | -6.00% | -7.50% | N/A |

**Prepayment Penalty LLPAs:**
| Structure | Adjustment |
|-----------|------------|
| 7 Year (84mo) Min Interest | +2.000% |
| 7 Year Step-down (7/6/5/4/3/2/1) | +1.750% |
| 5 Year (60mo) Min Interest | +0.750% |
| 5 Year Step-down (5/4/3/2/1) | +0.500% |
| 3 Year Step-down (3/2/1) | 0.000% |
| 2 Year Step-down (2/1) | -1.000% |
| 1 Year (1%) | -2.000% |
| No Prepayment | -4.000% |

**Interest Only LLPA:**
| LTV Range | IO Adjustment |
|-----------|---------------|
| ≤65% | 0.000% |
| 70% | -0.250% |
| 75% | -0.375% |
| 80% | -0.750% |

#### 3.5.5 DSCR Product Parameters

| Parameter | Value |
|-----------|-------|
| Min Loan | $100,000 |
| Max Loan | $3,000,000 |
| Term | 30 years |
| Min DSCR | 1.00x (700+ FICO) / 1.20x (<700) |
| Min FICO | 680 |
| Rate Types | Fixed 30, 5/1 ARM, 7/1 ARM |
| Amortization | 30-year or 10-year IO + 20-year amort |

---

### 3.6 Sizer Output

The sizing engine produces the following output:

```typescript
interface SizingResult {
  dealId: string;
  loanType: 'fix_flip' | 'bridge' | 'ground_up' | 'dscr';
  investor: 'eastview' | 'archwest';
  
  // Borrower Classification (RTL)
  borrowerClassification?: 'A+' | 'A' | 'B' | 'C';
  creditScore: number;
  experienceScore: number;
  
  // Leverage Metrics
  asIsLTV: number;
  ltc: number;
  ltarv?: number;
  dscr?: number;
  
  // Loan Structure
  maxLoanAmount: number;
  initialLoanAmount: number;
  rehabHoldback?: number;
  
  // Pricing
  interestRate: number;
  basePrice: number;
  llpaTotal: number;
  finalPrice: number;
  
  // USDV Economics
  originationPoints: number;
  ysp: number;
  
  // Constraints Applied
  leverageReductions: string[];
  llpasApplied: string[];
  
  // Validation
  isEligible: boolean;
  ineligibilityReasons: string[];
  
  createdAt: Date;
}
```

---

### 3.7 Sizing UI

#### 3.7.1 Auto-Sizing on Application Submit

When Full Application is submitted:
1. System auto-sizes deal with default investor (Eastview)
2. Sizing results stored on Deal record
3. Notification sent (email + Roam) to assigned LO/Processor

#### 3.7.2 Manual Sizing Adjustments

Internal users can adjust:
- Override investor selection
- Adjust LTV/LTC manually (with exception flag)
- Toggle rate lock
- Select prepayment structure (DSCR)
- Add manual exceptions with notes

#### 3.7.3 Sizing Summary View

Display sizing output in digestible format:

```
┌─────────────────────────────────────────────────────────────┐
│  DEAL SIZING: 123 Main St                                   │
│  Loan Type: Fix & Flip | Investor: Eastview                 │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  BORROWER                        LEVERAGE                    │
│  ─────────                       ────────                    │
│  Classification: A               As-Is LTV: 85.0%           │
│  FICO: 720                       LTC: 85.0%                 │
│  Experience: 5 deals             LTARV: 70.0%               │
│                                                              │
│  LOAN STRUCTURE                  PRICING                     │
│  ──────────────                  ───────                     │
│  Initial Amount: $425,000        Rate: 10.50%               │
│  Rehab Holdback: $75,000         Points: 2.0%               │
│  Total Loan: $500,000            YSP: 1.25%                 │
│                                                              │
│  ⚠️ Leverage Reductions Applied:                            │
│     • Heavy Rehab Project (-5%)                             │
│                                                              │
│  [Generate Quotes]  [Export to Excel]  [Edit Sizing]        │
└─────────────────────────────────────────────────────────────┘
```

---

### 3.8 Rate Lock

#### 3.8.1 Rate Lock Initiation

- User can lock rate at sizing stage
- Lock period: 30 days (default), extendable to 90 days
- Extension cost: 15 bps per 15 days

#### 3.8.2 Rate Lock Tracking

```typescript
interface RateLock {
  dealId: string;
  lockedRate: number;
  lockedPrice: number;
  lockDate: Date;
  expirationDate: Date;
  extensions: {
    date: Date;
    newExpiration: Date;
    cost: number;
  }[];
  status: 'active' | 'expired' | 'exercised';
}
```

#### 3.8.3 Rate Lock Alerts

- 7 days before expiration: Warning email
- 3 days before expiration: Urgent alert
- On expiration: Lock expired notification

---

## 4. Phase 4: Quote Generation & Term Sheet

### 4.1 Overview

Phase 4 presents sizing results to the borrower as selectable quote options, captures their selection, auto-generates a term sheet, collects e-signature, and initiates third-party report deposit collection.

### 4.2 Quote Generation

#### 4.2.1 Quote Scenarios

**RTL Loans (Fix & Flip / Bridge / Ground-Up):**
- Limited flexibility - typically 1 primary quote
- Variations possible: loan amount tiers, term length

**DSCR Loans:**
- Multiple variables create 3-5 quote options:
  - Prepayment structure
  - LTV tier
  - Cash-out vs. Rate/Term
  - Interest-only vs. Amortizing
  - Rate type (Fixed vs. ARM)

#### 4.2.2 Quote Data Structure

```typescript
interface Quote {
  id: string;
  dealId: string;
  quoteNumber: number; // 1, 2, 3, etc.
  
  // Loan Terms
  loanAmount: number;
  interestRate: number;
  loanTerm: number; // months
  rateType: 'fixed' | '5_1_arm' | '7_1_arm';
  
  // Payment Structure
  amortization: 'interest_only' | 'amortizing';
  interestOnlyPeriod?: number; // months
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
  
  // Cash Flow (DSCR)
  cashOutAmount?: number;
  
  // USDV Economics
  originationPoints: number;
  originationFee: number;
  ysp: number;
  yspAmount: number;
  
  // Borrower Costs
  estimatedClosingCosts: number;
  cashToClose: number;
  
  // Status
  status: 'draft' | 'presented' | 'selected' | 'expired';
  expiresAt: Date;
  selectedAt?: Date;
  
  createdAt: Date;
}
```

#### 4.2.3 Quote Generation Logic

For DSCR, system generates quotes based on borrower priorities captured in application:

```typescript
function generateDSCRQuotes(sizing: SizingResult, preferences: BorrowerPreferences): Quote[] {
  const quotes: Quote[] = [];
  
  // Option 1: Lowest Rate (longer prepay)
  quotes.push(buildQuote({
    prepay: '5_year_stepdown',
    io: true,
    ltv: sizing.maxLTV
  }));
  
  // Option 2: Most Flexibility (shorter prepay)
  quotes.push(buildQuote({
    prepay: '3_year_stepdown',
    io: true,
    ltv: sizing.maxLTV
  }));
  
  // Option 3: Max Proceeds (if cash-out eligible)
  if (preferences.wantsCashOut) {
    quotes.push(buildQuote({
      prepay: '5_year_stepdown',
      io: true,
      ltv: sizing.maxLTV,
      cashOut: true
    }));
  }
  
  // Option 4: Lowest Payment (amortizing)
  quotes.push(buildQuote({
    prepay: '5_year_stepdown',
    io: false,
    ltv: sizing.maxLTV * 0.9 // Lower LTV for better rate
  }));
  
  return quotes.slice(0, 5); // Max 5 options
}
```

---

### 4.3 Quote Presentation UI

#### 4.3.1 Borrower-Facing Quote Page

Professional web page at unique URL: `quotes.usdvcapital.com/{deal_id}/{token}`

**Design Requirements:**
- USDV Capital branding
- Mobile responsive
- Clean comparison layout
- Clear CTAs

**Quote Card Layout:**
```
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│  OPTION 1: LOWEST RATE                                      │
│  ─────────────────────                                       │
│                                                              │
│  Interest Rate        7.25%                                 │
│  Loan Amount          $425,000                              │
│  Monthly Payment      $2,568                                │
│  LTV                  75%                                   │
│                                                              │
│  Prepayment           5-4-3-2-1 Step-down                   │
│  Term                 30 Years                              │
│  Amortization         10-Year Interest Only                 │
│                                                              │
│  ───────────────────────────────────────────────────────    │
│                                                              │
│  Origination Fee      $8,500 (2 points)                     │
│  Est. Closing Costs   $12,350                               │
│  Cash to Close        $127,850                              │
│                                                              │
│            [ SELECT THIS OPTION ]                           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

#### 4.3.2 Quote Comparison View

Side-by-side comparison of all options with key metrics highlighted:

| | Option 1 | Option 2 | Option 3 |
|---|----------|----------|----------|
| **Rate** | 7.25% | 7.50% | 7.75% |
| **Loan Amount** | $425,000 | $425,000 | $450,000 |
| **Monthly Payment** | $2,568 | $2,656 | $2,906 |
| **Prepayment** | 5-year | 3-year | 5-year |
| **Cash Out** | - | - | $25,000 |
| **Cash to Close** | $127,850 | $128,100 | $103,100 |

#### 4.3.3 Quote Expiration

- Default expiration: 2 business days from presentation
- Configurable per deal
- Countdown timer displayed on quote page
- Expired quotes show "Quote Expired - Contact Us"

---

### 4.4 Quote Selection Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    QUOTE SELECTION FLOW                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. Borrower receives quote link (email + SMS)              │
│                    │                                        │
│                    ▼                                        │
│  2. Borrower reviews options on quote page                  │
│                    │                                        │
│                    ▼                                        │
│  3. Borrower clicks "Select This Option"                    │
│                    │                                        │
│                    ▼                                        │
│  4. Confirmation modal: "You're selecting Option X"         │
│     - Summary of terms                                      │
│     - "Confirm Selection" button                            │
│                    │                                        │
│                    ▼                                        │
│  5. Selection recorded → Deal status updated                │
│                    │                                        │
│                    ▼                                        │
│  6. Auto-generate Term Sheet (immediate)                    │
│                    │                                        │
│                    ▼                                        │
│  7. Term Sheet sent for e-signature (Dropbox Sign)          │
│                    │                                        │
│                    ▼                                        │
│  8. Invoice for third-party deposit generated               │
│                    │                                        │
│                    ▼                                        │
│  9. Borrower signs Term Sheet + Pays Deposit                │
│                    │                                        │
│                    ▼                                        │
│  10. Deal moves to Phase 5 (Third-Party Reports)            │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

### 4.5 Term Sheet Generation

#### 4.5.1 Auto-Generation Trigger

Term sheet generates automatically when borrower selects quote. Zero manual intervention.

#### 4.5.2 Term Sheet Data Mapping

| Quote Field | Term Sheet Field |
|-------------|------------------|
| Loan Amount | Loan Amount |
| Interest Rate | Interest Rate |
| Loan Term | Term |
| Amortization | Payment Structure |
| Prepayment | Prepayment Penalty |
| LTV | Loan-to-Value |
| Origination Fee | Origination Fee |
| Est. Closing Costs | Estimated Closing Costs |
| Property Address | Property Address |
| Borrower Name | Borrower |
| Entity Name | Borrowing Entity |
| Close Date | Target Closing Date |

**Additional Term Sheet Fields (from Application):**
- Guarantor(s)
- Property Type
- Loan Purpose
- Exit Strategy (RTL)
- DSCR (DSCR loans)
- Escrow requirements
- Insurance requirements
- Standard conditions

#### 4.5.3 Term Sheet Template

Term sheet generated as PDF from template with dynamic field insertion.

**Sections:**
1. Loan Summary
2. Property Information
3. Borrower / Guarantor Information
4. Loan Terms
5. Fees & Costs
6. Conditions Precedent to Closing
7. Standard Terms & Conditions
8. Expiration & Acceptance
9. Signature Block

#### 4.5.4 Term Sheet Expiration

- Term sheet expires: 2 business days from generation
- Configurable per deal
- Expired term sheets require re-generation

---

### 4.6 E-Signature Integration (Dropbox Sign)

#### 4.6.1 Signature Request Flow

```typescript
async function sendTermSheetForSignature(termSheet: TermSheet): Promise<SignatureRequest> {
  const signatureRequest = await dropboxSign.signatureRequest.createEmbedded({
    template_id: TERM_SHEET_TEMPLATE_ID,
    subject: `USDV Capital - Term Sheet for ${termSheet.propertyAddress}`,
    signers: [
      {
        email: termSheet.borrowerEmail,
        name: termSheet.borrowerName,
        role: 'Borrower'
      },
      // Add co-guarantors as additional signers
      ...termSheet.guarantors.map(g => ({
        email: g.email,
        name: g.name,
        role: 'Guarantor'
      }))
    ],
    custom_fields: [
      { name: 'loan_amount', value: formatCurrency(termSheet.loanAmount) },
      { name: 'interest_rate', value: `${termSheet.interestRate}%` },
      // ... all dynamic fields
    ]
  });
  
  return signatureRequest;
}
```

#### 4.6.2 Signature Status Tracking

| Status | Description |
|--------|-------------|
| `sent` | Signature request sent to borrower |
| `viewed` | Borrower opened the document |
| `signed` | All parties have signed |
| `declined` | Borrower declined to sign |
| `expired` | Signature request expired |

#### 4.6.3 Signature Webhooks

Listen for Dropbox Sign webhooks:
- `signature_request_viewed` → Update deal, notify team
- `signature_request_signed` → Trigger deposit invoice
- `signature_request_declined` → Alert team, update deal status

---

### 4.7 Third-Party Report Deposit

#### 4.7.1 Deposit Invoice Generation

After term sheet signed, auto-generate invoice for third-party report deposit.

**Invoice Contents:**
- Invoice number
- Borrower name & contact
- Property address
- Deposit amount (configurable, typically $1,500-$3,000)
- Payment instructions
- Non-refundable disclosure

#### 4.7.2 Payment Integration (Stripe)

```typescript
async function createDepositPayment(deal: Deal, invoice: Invoice): Promise<PaymentIntent> {
  const paymentIntent = await stripe.paymentIntents.create({
    amount: invoice.amount * 100, // cents
    currency: 'usd',
    customer: deal.borrower.stripeCustomerId,
    metadata: {
      dealId: deal.id,
      invoiceId: invoice.id,
      type: 'third_party_deposit'
    }
  });
  
  return paymentIntent;
}
```

**Payment Methods:**
- Credit Card
- ACH Bank Transfer
- Wire Transfer (manual confirmation)

#### 4.7.3 Payment Confirmation Flow

```
Payment Received (Stripe webhook)
        │
        ▼
Update Invoice Status → "Paid"
        │
        ▼
Update Deal Status → "Initial UW" (Phase 5 ready)
        │
        ▼
Notify Team (email + Roam)
        │
        ▼
Notify Borrower (receipt email)
        │
        ▼
Trigger Phase 5: Auto-order third-party reports
```

---

### 4.8 Notifications

#### 4.8.1 Borrower Notifications

| Event | Channel | Template |
|-------|---------|----------|
| Quotes Ready | Email + SMS | "Your loan quotes are ready" with link |
| Quote Selected | Email | "Thank you for selecting - term sheet incoming" |
| Term Sheet Sent | Email | "Please sign your term sheet" (via Dropbox Sign) |
| Term Sheet Signed | Email | "Term sheet signed - deposit invoice attached" |
| Deposit Invoice | Email | Invoice PDF + payment link |
| Payment Received | Email | Receipt + next steps |
| Quote Expiring (24hr) | Email + SMS | "Your quotes expire tomorrow" |
| Quote Expired | Email | "Quotes expired - contact us to refresh" |

#### 4.8.2 Internal Notifications

| Event | Channel | Recipients |
|-------|---------|------------|
| Quote Presented | Email, Roam | Assigned LO |
| Quote Selected | Email, Roam | LO, Processor |
| Term Sheet Signed | Email, Roam | LO, Processor |
| Payment Received | Email, Roam | LO, Processor, Accounting |
| Quote Expired | Email, Roam | LO |

---

## 5. Technical Requirements

### 5.1 API Endpoints

```
# Phase 3: Sizing
POST   /api/deals/:id/size
       → Run sizing engine, store results

GET    /api/deals/:id/sizing
       → Get sizing results

PUT    /api/deals/:id/sizing
       → Update/override sizing

POST   /api/deals/:id/rate-lock
       → Initiate rate lock

PUT    /api/deals/:id/rate-lock/extend
       → Extend rate lock

# Phase 4: Quotes
POST   /api/deals/:id/quotes/generate
       → Generate quote options from sizing

GET    /api/deals/:id/quotes
       → Get all quotes for deal

GET    /api/quotes/:quoteId
       → Get single quote

PUT    /api/quotes/:quoteId/select
       → Mark quote as selected (borrower action)

# Phase 4: Term Sheet
POST   /api/deals/:id/term-sheet
       → Generate term sheet from selected quote

GET    /api/deals/:id/term-sheet
       → Get term sheet

POST   /api/deals/:id/term-sheet/send
       → Send for e-signature via Dropbox Sign

# Phase 4: Deposit
POST   /api/deals/:id/deposit-invoice
       → Generate deposit invoice

POST   /api/deals/:id/deposit/payment-intent
       → Create Stripe payment intent

POST   /api/webhooks/stripe
       → Handle Stripe payment webhooks

POST   /api/webhooks/dropbox-sign
       → Handle signature webhooks
```

### 5.2 Data Models

*Add to Master PRD models:*

```typescript
// Sizing Result
model SizingResult {
  id              String   @id @default(uuid())
  dealId          String   @unique
  deal            Deal     @relation(fields: [dealId], references: [id])
  
  loanType        LoanType
  investor        Investor
  
  // Classification
  borrowerClass   String?
  creditScore     Int
  experienceScore Int
  
  // Leverage
  asIsLTV         Float
  ltc             Float?
  ltarv           Float?
  dscr            Float?
  
  // Amounts
  maxLoanAmount   Float
  initialAmount   Float
  rehabHoldback   Float?
  
  // Pricing
  interestRate    Float
  basePrice       Float
  llpaTotal       Float
  finalPrice      Float
  
  // USDV Economics
  originationPts  Float
  ysp             Float
  
  // Flags
  isEligible      Boolean
  reasons         String[] // ineligibility reasons
  reductions      String[] // leverage reductions applied
  llpasApplied    String[]
  
  createdAt       DateTime @default(now())
  updatedAt       DateTime @updatedAt
}

// Rate Lock
model RateLock {
  id              String   @id @default(uuid())
  dealId          String   @unique
  deal            Deal     @relation(fields: [dealId], references: [id])
  
  lockedRate      Float
  lockedPrice     Float
  lockDate        DateTime
  expirationDate  DateTime
  status          RateLockStatus
  
  extensions      RateLockExtension[]
  
  createdAt       DateTime @default(now())
}

// Quote
model Quote {
  id              String   @id @default(uuid())
  dealId          String
  deal            Deal     @relation(fields: [dealId], references: [id])
  
  quoteNumber     Int
  
  // Terms
  loanAmount      Float
  interestRate    Float
  loanTerm        Int
  rateType        RateType
  amortization    AmortizationType
  ioperiod        Int?
  monthlyPayment  Float
  
  // Prepay
  prepayStructure String?
  prepayType      PrepayType?
  prepayYears     Int?
  
  // Leverage
  ltv             Float
  ltc             Float?
  ltarv           Float?
  dscr            Float?
  cashOutAmount   Float?
  
  // Economics
  originationPts  Float
  originationFee  Float
  ysp             Float
  yspAmount       Float
  closingCosts    Float
  cashToClose     Float
  
  // Status
  status          QuoteStatus
  expiresAt       DateTime
  selectedAt      DateTime?
  
  termSheet       TermSheet?
  
  createdAt       DateTime @default(now())
}

// Term Sheet
model TermSheet {
  id              String   @id @default(uuid())
  dealId          String   @unique
  deal            Deal     @relation(fields: [dealId], references: [id])
  quoteId         String   @unique
  quote           Quote    @relation(fields: [quoteId], references: [id])
  
  documentUrl     String
  
  // Signature
  signatureReqId  String?  // Dropbox Sign ID
  sentAt          DateTime?
  viewedAt        DateTime?
  signedAt        DateTime?
  signedDocUrl    String?
  
  status          TermSheetStatus
  expiresAt       DateTime
  
  createdAt       DateTime @default(now())
}

// Deposit Invoice
model DepositInvoice {
  id              String   @id @default(uuid())
  dealId          String   @unique
  deal            Deal     @relation(fields: [dealId], references: [id])
  
  invoiceNumber   String   @unique
  amount          Float
  
  // Payment
  stripePaymentId String?
  paidAt          DateTime?
  paymentMethod   String?
  
  status          InvoiceStatus
  
  createdAt       DateTime @default(now())
}
```

### 5.3 External Integrations

| Service | Purpose | Priority |
|---------|---------|----------|
| Dropbox Sign | E-signatures | High |
| Stripe | Payment processing | High |
| SendGrid | Transactional email | High |
| Twilio | SMS notifications | Medium |

### 5.4 Security

- Quote URLs include secure token (UUID + hash)
- Tokens expire with quote expiration
- Payment data handled by Stripe (PCI compliant)
- Term sheet access logged
- SSN/PII never displayed on quote page

---

## 6. Testing Requirements

### 6.1 Sizing Engine Tests

- Borrower classification calculation
- Leverage limits by product/class
- Leverage reduction application
- DSCR calculation accuracy
- LLPA calculation accuracy
- Final rate/price calculation
- Edge cases: max loan, min loan, ineligible scenarios

### 6.2 Quote Generation Tests

- Multi-option generation logic
- Expiration handling
- Selection flow
- Concurrent selection prevention

### 6.3 Integration Tests

- Dropbox Sign signature flow
- Stripe payment flow
- Webhook handling
- Email delivery

### 6.4 E2E Tests

1. Full flow: Sizing → Quotes → Selection → Term Sheet → Sign → Pay
2. Quote expiration handling
3. Rate lock flow
4. Payment failure recovery

---

## 7. Dependencies

| Dependency | Status | Notes |
|------------|--------|-------|
| Phase 1-2 Complete | Required | Full Application data needed for sizing |
| Eastview RTL Sizer Excel | Pending Upload | For logic validation |
| Eastview DSCR Sizer Excel | Pending Upload | For logic validation |
| Quote HTML Templates | Pending Upload | For presentation layer |
| Term Sheet Template | Pending | Legal review needed |
| Dropbox Sign Account | Needed | API credentials required |
| Stripe Account | Needed | API credentials required |

---

## 8. Launch Checklist

- [ ] Sizing engine tested against manual Excel calculations
- [ ] Investor guidelines (Eastview, ArchWest) fully implemented
- [ ] Quote page designed and responsive
- [ ] Term sheet template approved by legal
- [ ] Dropbox Sign integration tested
- [ ] Stripe payment flow tested
- [ ] Webhook endpoints secured and tested
- [ ] Email templates created
- [ ] SMS templates created
- [ ] Rate lock logic implemented
- [ ] Expiration handling tested
- [ ] Internal notifications working
- [ ] UAT sign-off

---

*End of Phase 3-4 PRD*
