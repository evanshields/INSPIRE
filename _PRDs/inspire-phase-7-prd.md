# INSPIRE - Phase 7 Product Requirements Document

**Product Name:** INSPIRE  
**Company:** USDV Capital  
**Document Type:** Phase 7 PRD (AI Analysis & Credit Memo)  
**Version:** 1.0  
**Last Updated:** November 2025

---

## 1. Overview

Phase 7 is the intelligence layer of INSPIRE. As documents flow into the data room (Phase 5-6), AI continuously analyzes each file against USDV underwriting guidelines and investor requirements. The system flags issues in real-time, generates comprehensive credit memos, and identifies exceptions needed for investor approval.

### Core Capabilities

1. **Real-Time Document Analysis** - Every document reviewed against guidelines as it arrives
2. **Red/Green Flag System** - Issues and confirmations surfaced immediately
3. **Automated Credit Memo** - ~6-page deal summary generated when package is complete
4. **Exception Identification** - Auto-detect guideline deviations requiring investor approval
5. **Continuous Monitoring** - Re-analyze when documents are updated or added

---

## 2. Goals & Success Metrics

### Goals

1. Eliminate manual document-by-document review for compliance
2. Surface deal issues immediately rather than at final underwriting
3. Auto-generate investor-ready credit memos
4. Reduce time-to-decision on exception requests
5. Ensure no deal goes to closing with unaddressed red flags

### Success Metrics

| Metric | Target |
|--------|--------|
| Document analysis accuracy | >95% |
| Red flag detection rate | >98% |
| Credit memo generation time | <5 minutes |
| Manual underwriting review reduction | >60% |
| Exception identification accuracy | >95% |
| Time from complete package to credit memo | <1 hour |

---

## 3. Underwriting Guidelines Framework

### 3.1 Guidelines Hierarchy

```
┌─────────────────────────────────────────────────────────────┐
│                 GUIDELINES HIERARCHY                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Level 1: USDV Capital Internal Guidelines                  │
│  ─────────────────────────────────────────                  │
│  • Master underwriting manual (to be created)               │
│  • Internal risk tolerances                                 │
│  • House policies                                           │
│                                                              │
│  Level 2: Investor-Specific Guidelines                      │
│  ─────────────────────────────────────────                  │
│  • Eastview RTL Guidelines                                  │
│  • Eastview DSCR Guidelines                                 │
│  • ArchWest RTL Guidelines                                  │
│  • ArchWest DSCR Guidelines                                 │
│                                                              │
│  Level 3: Regulatory Requirements                           │
│  ─────────────────────────────────────────                  │
│  • FCRA compliance                                          │
│  • State-specific lending rules                             │
│  • OFAC/AML requirements                                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Guideline Categories

| Category | What It Covers |
|----------|---------------|
| Borrower Eligibility | FICO, experience, background, liquidity, entity structure |
| Property Eligibility | Property type, location, condition, size, zoning |
| Loan Parameters | LTV, LTC, LTARV, DSCR, loan amount, term |
| Valuation | Appraisal requirements, ARV support, market analysis |
| Title | Clear title, liens, encumbrances, insurance coverage |
| Insurance | Coverage amounts, mortgagee clause, policy type |
| Documentation | Required docs, currency, completeness |

---

## 4. Real-Time Document Analysis

### 4.1 Analysis Trigger

Analysis runs automatically when:
- Document uploaded to data room
- Document version updated
- Third-party report received
- Manual re-analysis requested

### 4.2 Analysis Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│                 DOCUMENT ANALYSIS PIPELINE                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  1. Document Received                                       │
│        │                                                    │
│        ▼                                                    │
│  2. Text Extraction (OCR if needed)                         │
│        │                                                    │
│        ▼                                                    │
│  3. Document Classification (Phase 6)                       │
│        │                                                    │
│        ▼                                                    │
│  4. Data Extraction                                         │
│     • Key fields parsed                                     │
│     • Values normalized                                     │
│        │                                                    │
│        ▼                                                    │
│  5. Guideline Matching                                      │
│     • Load applicable rules for doc type                    │
│     • Load investor-specific rules                          │
│        │                                                    │
│        ▼                                                    │
│  6. Rule Evaluation                                         │
│     • Check each requirement                                │
│     • Compare extracted values to thresholds                │
│        │                                                    │
│        ▼                                                    │
│  7. Flag Generation                                         │
│     • Green flags for passing checks                        │
│     • Red flags for failures                                │
│     • Yellow flags for warnings/exceptions                  │
│        │                                                    │
│        ▼                                                    │
│  8. Store Results + Notify                                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 4.3 Document-Specific Analysis Rules

#### 4.3.1 Credit Report Analysis

| Check | Rule | Flag |
|-------|------|------|
| FICO Score | ≥680 (DSCR), ≥660 (RTL) | 🔴 if below |
| Trade Lines | Min 3 total, 1 active, 1 with 24mo history | 🔴 if not met |
| Housing History | ≤1x30 in last 12 months | 🔴 if exceeded |
| Bankruptcy | None in 3-4 years (investor dependent) | 🔴 if found |
| Foreclosure | None in 3-4 years | 🔴 if found |
| Short Sale | None in 3-4 years | 🔴 if found |
| Judgments | None >$10k active | 🔴 if found |
| Collections | None >$10k unpaid | 🟡 if found |
| Report Currency | Within 90-120 days | 🔴 if expired |

**Extracted Data:**
```typescript
interface CreditReportExtraction {
  guarantorName: string;
  equifaxScore: number;
  experianScore: number;
  transunionScore: number;
  middleScore: number;
  
  tradeLines: {
    total: number;
    active: number;
    oldest: Date;
  };
  
  derogatories: {
    bankruptcies: { date: Date; chapter: string; status: string }[];
    foreclosures: { date: Date; status: string }[];
    shortSales: { date: Date }[];
    judgments: { amount: number; date: Date; status: string }[];
    collections: { amount: number; date: Date; status: string }[];
    lates: { count30: number; count60: number; count90: number }[];
  };
  
  mortgageHistory: {
    lates30Last12Mo: number;
    lates60Last12Mo: number;
    lates90Last12Mo: number;
  };
  
  reportDate: Date;
}
```

#### 4.3.2 Background Check Analysis

| Check | Rule | Flag |
|-------|------|------|
| Criminal - Financial Fraud | None | 🔴 if found |
| Criminal - Felony | None (or review on exception) | 🔴 if found |
| Active Litigation | None | 🔴 if found |
| OFAC Match | None | 🔴 CRITICAL if found |
| Liens >$10k | Must be resolved or on payment plan | 🔴 if unresolved |
| Judgments | Must be paid or on payment plan (6mo min) | 🔴 if unresolved |
| UCC Filings | Review for conflicts | 🟡 if found |

#### 4.3.3 Appraisal Analysis

| Check | Rule | Flag |
|-------|------|------|
| Report Currency | Within 120 days of note date | 🔴 if expired |
| As-Is Value vs. Sizing | Within 10% of application estimate | 🟡 if >10% variance |
| ARV vs. Sizing | Within 10% of application estimate | 🟡 if >10% variance |
| ARV Support | Comps within 6mo, same neighborhood | 🟡 if weak support |
| Property Condition | C1-C4 acceptable | 🔴 if C5-C6 |
| Property Type | Matches eligible types | 🔴 if ineligible |
| Square Footage | SFR ≥600sf, Condo ≥500sf/unit | 🔴 if below |
| Rural Designation | Not rural | 🔴 if rural |
| Photos | Interior + exterior present | 🟡 if missing |
| Appraiser License | State certified (not trainee) | 🔴 if invalid |

**Value Impact Analysis:**
```typescript
interface AppraisalImpact {
  // Compare to sizing
  asIsVariance: {
    appraised: number;
    applicationEstimate: number;
    variancePercent: number;
    impact: 'none' | 'ltv_change' | 'deal_killer';
  };
  
  arvVariance: {
    appraised: number;
    applicationEstimate: number;
    variancePercent: number;
    impact: 'none' | 'ltarv_change' | 'deal_killer';
  };
  
  // Recalculated metrics if needed
  revisedLTV?: number;
  revisedLTC?: number;
  revisedLTARV?: number;
  revisedLoanAmount?: number;
  
  proceedsImpact?: number; // Dollar change
}
```

#### 4.3.4 Title Commitment Analysis

| Check | Rule | Flag |
|-------|------|------|
| Title Type | Fee simple | 🔴 if leasehold |
| Existing Liens | None (or being paid at closing) | 🔴 if unreleased |
| Tax Liens | None | 🔴 if found |
| Mechanic's Liens | None | 🔴 if found |
| Judgment Liens | None | 🔴 if found |
| HOA Liens | Current | 🔴 if delinquent |
| Easements | No adverse easements | 🟡 if unusual |
| Encroachments | None | 🟡 if found |
| Zoning | Compliant | 🔴 if violation |
| Legal Access | Confirmed | 🔴 if no access |
| Policy Amount | ≥ Loan amount | 🔴 if insufficient |
| ALTA Form | 2006 standard or equivalent | 🟡 if non-standard |

**Schedule B Review:**
```typescript
interface TitleScheduleBAnalysis {
  standardExceptions: string[];
  
  requirementsToClose: {
    item: string;
    status: 'pending' | 'satisfied' | 'waived';
    notes: string;
  }[];
  
  liens: {
    type: string;
    holder: string;
    amount: number;
    position: number;
    toBeReleased: boolean;
  }[];
  
  specialExceptions: {
    description: string;
    riskLevel: 'low' | 'medium' | 'high';
    recommendation: string;
  }[];
}
```

#### 4.3.5 Insurance Certificate Analysis

| Check | Rule | Flag |
|-------|------|------|
| Coverage Amount | ≥ Loan amount OR 100% replacement cost | 🔴 if insufficient |
| Mortgagee Clause | Correct investor clause + ISAOA/ATIMA | 🔴 if wrong/missing |
| Named Insured | Matches borrowing entity | 🔴 if mismatch |
| Property Address | Matches subject property | 🔴 if mismatch |
| Policy Effective Date | Active at closing | 🔴 if not active |
| Policy Expiration | ≥6mo forward (purchase), ≥3mo (refi) | 🔴 if insufficient |
| Liability Coverage (RTL) | ≥$500,000 | 🔴 if below |
| Flood Coverage | Required if in flood zone | 🔴 if missing when required |
| Rent Loss Coverage (DSCR) | 6 months | 🟡 if missing |
| Condo Master Policy | Required for condos | 🔴 if missing |
| HO6/Walls-In (Condo) | Required for condos | 🔴 if missing |

**Mortgagee Clause Validation:**
```typescript
interface MortgageeClauseCheck {
  investor: 'eastview' | 'archwest';
  expectedClause: string;
  foundClause: string;
  hasISAOA_ATIMA: boolean;
  isCorrect: boolean;
  correctionNeeded?: string;
}
```

#### 4.3.6 Feasibility Study Analysis (RTL)

| Check | Rule | Flag |
|-------|------|------|
| Budget Alignment | Within 10% of application budget | 🟡 if variance |
| Timeline | Realistic for scope | 🟡 if concerns |
| Contingency | ≥5% hard + soft costs | 🔴 if below |
| Permits | All required permits identified | 🟡 if unclear |
| GC Qualification | Licensed if required | 🔴 if unlicensed |
| Scope Completeness | All work items priced | 🟡 if gaps |

#### 4.3.7 Bank Statement Analysis

| Check | Rule | Flag |
|-------|------|------|
| Currency | Within 90 days | 🔴 if older |
| Account Holder | Matches guarantor or entity | 🔴 if mismatch |
| Liquidity | Meets reserve requirements | 🔴 if insufficient |
| Large Deposits | Sourced if >175% avg or >$10k | 🟡 if unsourced |
| NSF/Overdrafts | Review frequency | 🟡 if excessive |
| Consecutive Months | 2 months minimum | 🔴 if incomplete |

**Liquidity Calculation:**
```typescript
interface LiquidityAnalysis {
  // Sources found
  bankAccounts: { institution: string; balance: number; accountType: string }[];
  investmentAccounts: { institution: string; value: number; type: string }[];
  retirementAccounts: { institution: string; value: number; type: string }[];
  
  // Calculated totals
  cashLiquidity: number;           // 100% of bank
  investmentLiquidity: number;     // 75% of stocks/bonds
  retirementLiquidity: number;     // 50% (or 70% if >59.5yo)
  totalVerifiedLiquidity: number;
  
  // Requirements
  requiredLiquidity: {
    downPayment: number;           // If purchase
    closingCosts: number;
    reserves: number;              // PITIA × months required
    liensToSatisfy: number;        // If any >$5k
    total: number;
  };
  
  // Result
  surplusDeficit: number;
  meetsRequirement: boolean;
}
```

#### 4.3.8 Entity Document Analysis

| Check | Rule | Flag |
|-------|------|------|
| Articles of Org | Present and matches entity name | 🔴 if missing/mismatch |
| Operating Agreement | Present, shows ownership | 🔴 if missing |
| Good Standing | Current (within 90 days) | 🔴 if expired |
| EIN Letter/W-9 | Present, EIN matches | 🔴 if missing |
| State Registration | Active in property state | 🟡 if not registered |
| Authorized Signers | Documented | 🟡 if unclear |

#### 4.3.9 Lease Analysis (DSCR)

| Check | Rule | Flag |
|-------|------|------|
| Arm's Length | No related party | 🔴 if related party |
| Lease Term | ≤3 years | 🟡 if longer |
| Purchase Option | None | 🔴 if present |
| Rent Amount | Matches application / within market | 🟡 if variance |
| Tenant Occupancy | Verified | 🟡 if unverified |
| Security Deposit | Collected | 🟡 if not collected |
| First Month Rent | Paid (proof required) | 🔴 if not proven |

---

## 5. Flag System

### 5.1 Flag Types

| Flag | Meaning | Action Required |
|------|---------|-----------------|
| 🟢 **Green** | Requirement met, no issues | None |
| 🟡 **Yellow** | Warning, may need exception or clarification | Review recommended |
| 🔴 **Red** | Requirement not met, blocks closing | Must resolve or get exception |
| ⚫ **Critical** | Immediate stop (OFAC, fraud, etc.) | Escalate immediately |

### 5.2 Flag Data Structure

```typescript
interface AnalysisFlag {
  id: string;
  dealId: string;
  documentId: string;
  documentType: string;
  
  // Flag details
  flagType: 'green' | 'yellow' | 'red' | 'critical';
  category: string;        // e.g., "credit", "title", "insurance"
  ruleId: string;          // Reference to specific rule
  ruleName: string;        // Human-readable rule name
  
  // Finding
  finding: string;         // What was found
  expected: string;        // What was expected
  actual: string;          // Actual value
  
  // Impact
  impactDescription: string;
  affectsLoanAmount: boolean;
  affectsEligibility: boolean;
  
  // Resolution
  requiresException: boolean;
  exceptionType?: string;
  suggestedResolution: string;
  
  // Status
  status: 'open' | 'acknowledged' | 'resolved' | 'exception_requested' | 'exception_approved';
  resolvedAt?: Date;
  resolvedBy?: string;
  resolutionNotes?: string;
  
  createdAt: Date;
}
```

### 5.3 Flag Aggregation by Deal

```typescript
interface DealFlagSummary {
  dealId: string;
  
  counts: {
    green: number;
    yellow: number;
    red: number;
    critical: number;
  };
  
  openRed: AnalysisFlag[];
  openYellow: AnalysisFlag[];
  
  byCategory: {
    [category: string]: {
      green: number;
      yellow: number;
      red: number;
    };
  };
  
  readyForCreditMemo: boolean;  // True if no open red/critical
  readyForClosing: boolean;     // True if all flags resolved
  
  lastAnalyzedAt: Date;
}
```

### 5.4 Real-Time Flag Notifications

| Flag Type | Notification | Recipients |
|-----------|--------------|------------|
| 🟢 Green | None (silent) | - |
| 🟡 Yellow | In-app badge update | Processor |
| 🔴 Red | Email + Roam + In-app | Processor, LO, Underwriter |
| ⚫ Critical | Immediate email + Roam + SMS | Processor, LO, Underwriter, Compliance |

**Alert Email Template (Red Flag):**
```
Subject: 🔴 Red Flag Alert - [Property Address]

Deal: [Property Address]
Document: [Document Type]
Issue: [Rule Name]

Finding: [Description]
Expected: [Expected value]
Actual: [Actual value]

Impact: [Impact description]

Suggested Resolution: [Suggestion]

[View Deal] [View Document] [Request Exception]
```

---

## 6. Exception Management

### 6.1 Exception Types

| Exception Type | Description | Typical Approver |
|----------------|-------------|------------------|
| Credit Exception | FICO below threshold, derog history | Investor |
| Experience Exception | Below minimum deal count | Investor |
| LTV Exception | Above max leverage | Investor |
| Property Exception | Non-standard property type/condition | Investor |
| Documentation Exception | Missing or alternative docs | Investor or USDV |
| Timing Exception | Expired documents | USDV |
| Market Exception | Non-standard market/location | Investor |

### 6.2 Auto-Generated Exception Requests

When red flags are identified, system auto-drafts exception requests:

```typescript
interface ExceptionRequest {
  id: string;
  dealId: string;
  flagId: string;
  
  // Exception details
  exceptionType: ExceptionType;
  investor: 'eastview' | 'archwest';
  
  // Request content
  subject: string;
  description: string;
  mitigatingFactors: string[];
  compensatingStrengths: string[];
  
  // Supporting data (auto-populated)
  guidelineReference: string;
  actualValue: string;
  requestedValue: string;
  
  // Status
  status: 'draft' | 'submitted' | 'approved' | 'denied' | 'withdrawn';
  submittedAt?: Date;
  respondedAt?: Date;
  approvedBy?: string;
  conditions?: string[];
  
  createdAt: Date;
}
```

### 6.3 Exception Request Template

```
EXCEPTION REQUEST

Deal: [Address]
Loan Type: [Fix & Flip / Ground-Up / DSCR]
Loan Amount: $[Amount]
Investor: [Eastview / ArchWest]

EXCEPTION REQUESTED:
[Exception Type]: [Current Value] → Requesting approval at [Requested Value]

GUIDELINE REFERENCE:
Per [Investor] [RTL/DSCR] Guidelines, Section [X], the requirement is [requirement].
The subject deal does not meet this requirement because [reason].

MITIGATING FACTORS:
• [Factor 1 - e.g., Strong liquidity of $X exceeds requirement by Y%]
• [Factor 2 - e.g., Guarantor has 15+ completed projects]
• [Factor 3 - e.g., Low LTV of X% provides cushion]

COMPENSATING STRENGTHS:
• [Strength 1]
• [Strength 2]

RECOMMENDATION:
USDV Capital recommends approval of this exception based on the above factors.

Submitted by: [User Name]
Date: [Date]
```

---

## 7. Credit Memo Generation

### 7.1 Trigger Conditions

Credit memo auto-generates when:
1. All required documents received (diligence checklist 100%)
2. All third-party reports received
3. No open critical flags
4. All red flags either resolved or exception requested

### 7.2 Credit Memo Structure (~6 pages)

```
┌─────────────────────────────────────────────────────────────┐
│                     CREDIT MEMORANDUM                        │
│                                                              │
│  Property: [Address]                                        │
│  Loan Type: [Type]                                          │
│  Investor: [Investor]                                       │
│  Date: [Date]                                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  SECTION 1: EXECUTIVE SUMMARY (½ page)                      │
│  ─────────────────────────────────────                      │
│  • Deal snapshot                                            │
│  • Loan terms summary                                       │
│  • Recommendation                                           │
│  • Key strengths                                            │
│  • Key risks / exceptions                                   │
│                                                              │
│  SECTION 2: BORROWER ANALYSIS (1 page)                      │
│  ─────────────────────────────────────                      │
│  • Sponsor background                                       │
│  • Entity structure                                         │
│  • Credit summary (FICO, history)                          │
│  • Background check summary                                 │
│  • Experience / track record                                │
│  • Financial strength (PFS, liquidity)                     │
│                                                              │
│  SECTION 3: PROPERTY ANALYSIS (1 page)                      │
│  ─────────────────────────────────────                      │
│  • Property description                                     │
│  • Location / market analysis                               │
│  • Appraisal summary (As-Is, ARV)                          │
│  • Business plan (RTL: rehab scope; DSCR: rental strategy) │
│  • Comparable analysis                                      │
│                                                              │
│  SECTION 4: DEAL ECONOMICS (1 page)                         │
│  ─────────────────────────────────────                      │
│  • Loan structure                                           │
│  • Sources & uses                                           │
│  • LTV / LTC / LTARV calculations                          │
│  • DSCR calculation (if applicable)                        │
│  • Exit strategy analysis                                   │
│  • Profitability projection                                 │
│                                                              │
│  SECTION 5: THIRD-PARTY REPORT SUMMARY (1 page)            │
│  ─────────────────────────────────────                      │
│  • Appraisal findings                                       │
│  • Title summary (Schedule B items)                        │
│  • Insurance confirmation                                   │
│  • Feasibility summary (RTL)                               │
│  • Flood determination                                      │
│                                                              │
│  SECTION 6: RISK ASSESSMENT (1 page)                        │
│  ─────────────────────────────────────                      │
│  • Green flags summary                                      │
│  • Yellow flags (warnings)                                  │
│  • Red flags / exceptions required                          │
│  • Mitigants for each risk                                  │
│  • Overall risk rating                                      │
│                                                              │
│  SECTION 7: CONDITIONS & EXCEPTIONS (½ page)                │
│  ─────────────────────────────────────                      │
│  • Conditions precedent to closing                          │
│  • Exceptions requested                                     │
│  • Exception status                                         │
│                                                              │
│  APPENDIX                                                   │
│  ─────────────────────────────────────                      │
│  • Document checklist                                       │
│  • Detailed flag report                                     │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 7.3 Credit Memo Data Model

```typescript
interface CreditMemo {
  id: string;
  dealId: string;
  version: number;
  
  // Metadata
  generatedAt: Date;
  generatedBy: 'system' | string;  // User ID if manual
  investor: 'eastview' | 'archwest';
  
  // Content sections
  sections: {
    executiveSummary: ExecutiveSummarySection;
    borrowerAnalysis: BorrowerAnalysisSection;
    propertyAnalysis: PropertyAnalysisSection;
    dealEconomics: DealEconomicsSection;
    thirdPartyReports: ThirdPartyReportSection;
    riskAssessment: RiskAssessmentSection;
    conditionsExceptions: ConditionsSection;
  };
  
  // Flags snapshot at generation
  flagsSnapshot: DealFlagSummary;
  
  // Output
  pdfUrl: string;
  
  // Status
  status: 'draft' | 'final' | 'superseded';
  
  // Approval (optional)
  approvedBy?: string;
  approvedAt?: Date;
  approvalNotes?: string;
}

interface ExecutiveSummarySection {
  propertyAddress: string;
  loanType: string;
  loanAmount: number;
  interestRate: number;
  term: string;
  ltv: number;
  ltc?: number;
  ltarv?: number;
  dscr?: number;
  
  recommendation: 'approve' | 'approve_with_conditions' | 'decline';
  recommendationRationale: string;
  
  keyStrengths: string[];
  keyRisks: string[];
  exceptionsRequired: number;
}

interface BorrowerAnalysisSection {
  sponsors: {
    name: string;
    ownershipPercent: number;
    fico: number;
    experienceDeals: number;
    backgroundClear: boolean;
    role: string;
  }[];
  
  entityName: string;
  entityType: string;
  entityState: string;
  
  creditHighlights: string[];
  creditConcerns: string[];
  
  experienceSummary: string;
  trackRecordDeals: number;
  
  liquidityVerified: number;
  liquidityRequired: number;
  liquiditySurplus: number;
  
  netWorth?: number;
}

interface PropertyAnalysisSection {
  address: string;
  propertyType: string;
  units: number;
  squareFootage: number;
  yearBuilt: number;
  condition: string;
  
  marketAnalysis: {
    msa: string;
    medianHomePrice: number;
    marketTrend: 'appreciating' | 'stable' | 'declining';
    daysOnMarket: number;
  };
  
  appraisalSummary: {
    asIsValue: number;
    arv: number;
    appraiser: string;
    appraisalDate: Date;
    comparablesUsed: number;
  };
  
  businessPlan: string;  // Narrative
  
  // RTL specific
  rehabScope?: string;
  rehabBudget?: number;
  rehabTimeline?: string;
  
  // DSCR specific
  rentStrategy?: string;
  marketRent?: number;
  inPlaceRent?: number;
  occupancy?: string;
}

interface DealEconomicsSection {
  sourcesAndUses: {
    sources: { description: string; amount: number }[];
    uses: { description: string; amount: number }[];
  };
  
  loanMetrics: {
    loanAmount: number;
    ltv: number;
    ltc?: number;
    ltarv?: number;
    dscr?: number;
  };
  
  pricing: {
    interestRate: number;
    originationPoints: number;
    ysp: number;
  };
  
  exitStrategy: string;
  projectedExitValue: number;
  projectedProfit: number;
  projectedROI: number;
  
  // DSCR specific
  cashFlow?: {
    monthlyRent: number;
    monthlyPITIA: number;
    netCashFlow: number;
  };
}

interface RiskAssessmentSection {
  overallRiskRating: 'low' | 'moderate' | 'elevated' | 'high';
  ratingRationale: string;
  
  greenFlags: { category: string; description: string }[];
  yellowFlags: { category: string; description: string; mitigant: string }[];
  redFlags: { category: string; description: string; resolution: string }[];
  
  strengthsNarrative: string;
  risksNarrative: string;
}

interface ConditionsSection {
  conditionsPrecedent: {
    condition: string;
    status: 'pending' | 'satisfied';
    notes?: string;
  }[];
  
  exceptionsRequested: {
    type: string;
    description: string;
    status: 'pending' | 'approved' | 'denied';
    approvedBy?: string;
    conditions?: string[];
  }[];
}
```

### 7.4 Credit Memo Generation Prompt

```typescript
const creditMemoPrompt = `
Generate a comprehensive credit memorandum for a real estate loan.

DEAL DATA:
${JSON.stringify(dealData, null, 2)}

BORROWER DATA:
${JSON.stringify(borrowerData, null, 2)}

PROPERTY DATA:
${JSON.stringify(propertyData, null, 2)}

THIRD-PARTY REPORTS SUMMARY:
${JSON.stringify(reportsSummary, null, 2)}

FLAGS:
${JSON.stringify(flags, null, 2)}

INVESTOR GUIDELINES REFERENCE:
${investorGuidelinesContext}

Generate each section of the credit memo following this structure:

1. EXECUTIVE SUMMARY
- 3-4 sentence deal overview
- Key loan terms in bullet points
- Clear recommendation (Approve / Approve with Conditions / Decline)
- Top 3 strengths
- Top 3 risks/concerns

2. BORROWER ANALYSIS
- Sponsor backgrounds (experience, track record)
- Credit analysis (scores, history, any derogatories)
- Background check results
- Financial strength (liquidity, net worth)
- Entity structure overview

3. PROPERTY ANALYSIS
- Property description
- Market conditions
- Appraisal findings
- Business plan viability

4. DEAL ECONOMICS
- Sources and uses
- All leverage metrics
- Exit strategy analysis
- Profitability projection

5. THIRD-PARTY REPORTS
- Key findings from each report
- Any concerns identified

6. RISK ASSESSMENT
- Categorize all flags
- Provide mitigants for each risk
- Overall risk rating with rationale

7. CONDITIONS & EXCEPTIONS
- List all conditions to close
- List all exceptions and status

Write in professional, concise underwriting language. Be specific with numbers and dates.
`;
```

---

## 8. Analysis UI

### 8.1 Deal Analysis Dashboard

```
┌─────────────────────────────────────────────────────────────┐
│  AI ANALYSIS: 123 Main St                                   │
│  Last analyzed: 2 minutes ago                               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  OVERALL STATUS                                             │
│  ─────────────                                              │
│  🟢 12 Green  │  🟡 3 Yellow  │  🔴 2 Red  │  ⚫ 0 Critical │
│                                                              │
│  [Generate Credit Memo]  [Re-Analyze All]  [Export Flags]   │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  RED FLAGS (Action Required)                        [2]     │
│  ───────────────────────────                                │
│                                                              │
│  🔴 Insurance - Mortgagee Clause Incorrect                  │
│     Found: "ABC Lender" | Expected: "Eastview Capital..."   │
│     [Request Correction]  [View Document]                   │
│                                                              │
│  🔴 Credit - FICO Below Threshold                           │
│     Found: 655 | Required: ≥660                             │
│     [Request Exception]  [View Report]                      │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  YELLOW FLAGS (Review Recommended)                  [3]     │
│  ─────────────────────────────────                          │
│                                                              │
│  🟡 Appraisal - ARV Variance                                │
│     Appraised ARV: $485,000 | Application: $520,000 (-7%)   │
│     Impact: LTARV increases from 68% to 73%                 │
│     [Acknowledge]  [View Appraisal]                         │
│                                                              │
│  🟡 Bank Statement - Large Deposit                          │
│     $45,000 deposit on 11/15 needs sourcing                 │
│     [Request LOE]  [View Statement]                         │
│                                                              │
│  🟡 Title - Easement Noted                                  │
│     Utility easement on rear 10ft of property               │
│     [Acknowledge]  [View Title]                             │
│                                                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  GREEN FLAGS (Confirmed)                           [12]     │
│  ───────────────────────                                    │
│                                                              │
│  ✅ Credit Report current (dated 11/20/2024)                │
│  ✅ Background check clear - no derogatories                │
│  ✅ Appraisal current (dated 11/18/2024)                    │
│  ✅ Title clear - no liens                                  │
│  ✅ Entity in good standing                                 │
│  ✅ Liquidity verified: $185,000 (required: $142,000)       │
│  ✅ Experience: 8 deals in 36 months                        │
│  ... [Show All]                                             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 8.2 Document-Level Analysis View

When viewing a specific document:

```
┌─────────────────────────────────────────────────────────────┐
│  DOCUMENT: Appraisal_2024-11-18.pdf                         │
│  Type: Appraisal | Analyzed: 11/18/2024 3:45 PM            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  EXTRACTED DATA                                             │
│  ──────────────                                             │
│  As-Is Value:        $425,000                               │
│  After-Repair Value: $485,000                               │
│  Property Type:      Single Family                          │
│  Square Footage:     1,850 sf                               │
│  Condition:          C4                                     │
│  Appraiser:          John Smith, SRA                        │
│  License #:          FL-12345                               │
│  Report Date:        11/18/2024                             │
│                                                              │
│  ANALYSIS RESULTS                                           │
│  ────────────────                                           │
│  ✅ Report within 120 days                                  │
│  ✅ Appraiser properly licensed                             │
│  ✅ Property type eligible                                  │
│  ✅ Square footage meets minimum                            │
│  ✅ Condition acceptable (C4)                               │
│  🟡 ARV 7% below application estimate                       │
│     → LTARV increases from 68% to 73%                       │
│     → Still within guidelines (max 75%)                     │
│  ✅ Comps within 6 months                                   │
│  ✅ Comps from same neighborhood                            │
│                                                              │
│  [View PDF]  [Re-Analyze]  [Override Flag]                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 9. Technical Requirements

### 9.1 API Endpoints

```
# Analysis
POST   /api/deals/:id/analyze
       → Run full analysis on all documents

POST   /api/documents/:id/analyze
       → Analyze single document

GET    /api/deals/:id/analysis
       → Get analysis results and flags

GET    /api/deals/:id/flags
       → Get all flags for deal

PUT    /api/flags/:id/resolve
       → Mark flag as resolved

PUT    /api/flags/:id/acknowledge
       → Acknowledge yellow flag

# Exceptions
POST   /api/deals/:id/exceptions
       → Create exception request

GET    /api/deals/:id/exceptions
       → Get all exceptions for deal

PUT    /api/exceptions/:id
       → Update exception status

# Credit Memo
POST   /api/deals/:id/credit-memo/generate
       → Generate credit memo

GET    /api/deals/:id/credit-memo
       → Get current credit memo

GET    /api/deals/:id/credit-memo/versions
       → Get all versions

PUT    /api/credit-memos/:id/approve
       → Approve credit memo
```

### 9.2 Data Models

```typescript
// Add to existing models

model AnalysisResult {
  id                String   @id @default(uuid())
  dealId            String
  deal              Deal     @relation(fields: [dealId], references: [id])
  documentId        String?
  document          Document? @relation(fields: [documentId], references: [id])
  
  analysisType      AnalysisType  // document, deal_level, credit_memo
  
  // Results
  extractedData     Json?
  rulesEvaluated    Int
  rulesPassed       Int
  rulesFailed       Int
  rulesWarning      Int
  
  // Timing
  startedAt         DateTime
  completedAt       DateTime
  durationMs        Int
  
  // AI details
  modelUsed         String
  promptTokens      Int
  completionTokens  Int
  
  createdAt         DateTime @default(now())
}

model AnalysisFlag {
  id                String   @id @default(uuid())
  dealId            String
  deal              Deal     @relation(fields: [dealId], references: [id])
  documentId        String?
  document          Document? @relation(fields: [documentId], references: [id])
  analysisResultId  String
  analysisResult    AnalysisResult @relation(fields: [analysisResultId], references: [id])
  
  // Flag details
  flagType          FlagType  // green, yellow, red, critical
  category          String
  ruleId            String
  ruleName          String
  
  // Finding
  finding           String
  expected          String?
  actual            String?
  
  // Impact
  impactDescription String?
  affectsLoanAmount Boolean  @default(false)
  affectsEligibility Boolean @default(false)
  
  // Resolution
  requiresException Boolean  @default(false)
  exceptionType     String?
  suggestedResolution String?
  
  // Status
  status            FlagStatus // open, acknowledged, resolved, exception_requested, exception_approved
  acknowledgedAt    DateTime?
  acknowledgedBy    String?
  resolvedAt        DateTime?
  resolvedBy        String?
  resolutionNotes   String?
  
  exceptionId       String?
  exception         ExceptionRequest? @relation(fields: [exceptionId], references: [id])
  
  createdAt         DateTime @default(now())
  updatedAt         DateTime @updatedAt
}

model ExceptionRequest {
  id                String   @id @default(uuid())
  dealId            String
  deal              Deal     @relation(fields: [dealId], references: [id])
  flagId            String   @unique
  flag              AnalysisFlag @relation(fields: [flagId], references: [id])
  
  exceptionType     String
  investor          String
  
  // Request
  subject           String
  description       String   @db.Text
  mitigatingFactors String[] 
  compensatingStrengths String[]
  
  guidelineReference String
  actualValue       String
  requestedValue    String
  
  // Status
  status            ExceptionStatus // draft, submitted, approved, denied, withdrawn
  submittedAt       DateTime?
  submittedBy       String?
  respondedAt       DateTime?
  respondedBy       String?
  approvalConditions String[]
  denialReason      String?
  
  createdAt         DateTime @default(now())
  updatedAt         DateTime @updatedAt
}

model CreditMemo {
  id                String   @id @default(uuid())
  dealId            String
  deal              Deal     @relation(fields: [dealId], references: [id])
  
  version           Int      @default(1)
  
  // Content
  content           Json     // Full memo content
  flagsSnapshot     Json     // Flags at time of generation
  
  // Output
  pdfUrl            String?
  
  // Generation
  generatedAt       DateTime @default(now())
  generatedBy       String   // 'system' or user ID
  modelUsed         String?
  
  // Status
  status            MemoStatus // draft, final, superseded
  
  // Approval
  approvedAt        DateTime?
  approvedBy        String?
  approvalNotes     String?
  
  createdAt         DateTime @default(now())
  updatedAt         DateTime @updatedAt
}

enum FlagType {
  green
  yellow
  red
  critical
}

enum FlagStatus {
  open
  acknowledged
  resolved
  exception_requested
  exception_approved
}

enum ExceptionStatus {
  draft
  submitted
  approved
  denied
  withdrawn
}

enum MemoStatus {
  draft
  final
  superseded
}
```

### 9.3 Background Jobs

| Job | Trigger | Purpose |
|-----|---------|---------|
| `analyze-document` | Document upload | Analyze new document |
| `analyze-deal` | On demand / schedule | Full deal re-analysis |
| `generate-credit-memo` | All docs complete | Auto-generate memo |
| `check-flag-expiration` | Daily | Re-flag if docs expire |
| `sync-exception-status` | Webhook | Update from investor response |

### 9.4 LLM Configuration

```typescript
interface AnalysisLLMConfig {
  // Document analysis
  documentAnalysis: {
    model: 'claude-3-5-sonnet' | 'gpt-4o';
    temperature: 0.1;  // Low for consistency
    maxTokens: 4000;
  };
  
  // Credit memo generation
  creditMemo: {
    model: 'claude-3-5-sonnet';
    temperature: 0.3;  // Slightly higher for narrative
    maxTokens: 8000;
  };
  
  // Data extraction
  extraction: {
    model: 'gpt-4o';
    temperature: 0;
    maxTokens: 2000;
  };
}
```

---

## 10. Notifications

### 10.1 Internal Notifications

| Event | Channel | Recipients |
|-------|---------|------------|
| Red Flag Created | Email, Roam, In-app | Processor, LO, Underwriter |
| Critical Flag Created | Email, Roam, SMS, In-app | All + Compliance |
| Yellow Flag Created | In-app | Processor |
| Credit Memo Ready | Email, Roam | LO, Underwriter |
| Exception Approved | Email, Roam | LO, Processor |
| Exception Denied | Email, Roam | LO, Processor, Underwriter |
| All Flags Resolved | Email, Roam | LO, Processor |

### 10.2 Notification Templates

**Credit Memo Ready:**
```
Subject: Credit Memo Ready - [Property Address]

The credit memorandum for [Property Address] has been generated.

Deal Summary:
• Loan Amount: $[Amount]
• LTV: [X]%
• Recommendation: [Approve / Approve with Conditions]
• Open Flags: [X] Yellow, [X] Red

[View Credit Memo] [View Deal]
```

---

## 11. Security & Compliance

- Analysis results contain sensitive borrower data - encrypted at rest
- Credit memos access-logged
- Exception requests tracked for audit
- PII redacted from any external-facing outputs
- Model prompts do not expose full SSN (last 4 only)

---

## 12. Testing Requirements

### 12.1 Analysis Accuracy Tests

- Test each rule against known pass/fail scenarios
- Validate extraction accuracy per document type
- Verify flag generation logic
- Test edge cases (borderline values)

### 12.2 Integration Tests

- Document upload → Analysis → Flag creation flow
- Exception request → Approval → Flag resolution
- Credit memo generation with various flag combinations

### 12.3 E2E Tests

1. Complete deal flow with all green flags → Memo generated
2. Deal with red flags → Exception flow → Memo generated
3. Document update → Re-analysis → Flag status change

---

## 13. Dependencies

| Dependency | Status | Notes |
|------------|--------|-------|
| Phase 5-6 Complete | Required | Documents must be in data room |
| USDV Underwriting Manual | Pending | For USDV-specific rules |
| Investor Guidelines | ✅ Uploaded | Eastview + ArchWest |
| LLM API Access | Required | Claude and/or GPT-4 |
| PDF Generation | Required | For credit memo output |

---

## 14. Launch Checklist

- [ ] All document analysis rules implemented
- [ ] Rules tested against investor guidelines
- [ ] Flag system working end-to-end
- [ ] Exception request flow complete
- [ ] Credit memo template finalized
- [ ] Credit memo generation tested
- [ ] PDF output quality verified
- [ ] Notifications configured
- [ ] Performance tested (analysis < 30 seconds)
- [ ] UAT sign-off

---

*End of Phase 7 PRD*
