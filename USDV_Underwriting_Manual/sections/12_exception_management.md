---
section: 12
title: Exception Management
version: 1.0
last_updated: 2025-12-30
model_used: haiku
---

# Section 12: Exception Management

## Overview

Exception management is the framework through which USDV Capital handles loan requests that deviate from standard underwriting guidelines. Rather than declining loans that fall outside typical parameters, USDV employs a tiered approval process that evaluates the strength of compensating factors and the severity of the exception.

This section defines the exception categories, establishes clear approval authority levels, outlines the request process, and provides the framework for evaluating compensating factors.

---

## 12.1 Exception Categories

Exceptions fall into seven primary categories based on the guideline area affected:

### Credit Exceptions
Deviations from credit requirements, including:
- FICO score below minimum threshold
- Insufficient trade line history
- Recent mortgage payment lates (30/60/90 days)
- Collection accounts above limits
- Judgments or liens above thresholds
- Insufficient liquidity reserves

**Example:** FICO of 655 (5 points below RTL minimum of 660)

### Experience Exceptions
Shortfalls in real estate investment experience:
- Fewer completed deals than minimum requirement
- Limited property management experience
- First-time investor scenarios
- Insufficient experience in specific product type (e.g., RTL vs DSCR)

**Example:** 1 deal in 36 months (minimum is 1, but pattern shows limited activity)

### Leverage Exceptions
Loan sizing above maximum constraints:
- LTV exceeds maximum by 1-2%
- LTC exceeds maximum
- LTARV exceeds maximum
- DSCR below minimum requirement

**Example:** 76% LTARV (max is 75%) due to strong ARV support

### Property Exceptions
Deviations from property eligibility standards:
- C5 condition rating (C1-C4 acceptable)
- Non-warrantable condominium (pending waiver)
- Non-standard property type
- Property in declining market
- Rural property designation

**Example:** Property rated C5 with documented rehabilitation plan

### Documentation Exceptions
Missing or outdated documents:
- Credit report expired (>120 days)
- Bank statements >90 days old
- Good standing certificate >90 days old
- Appraisal aged >120 days
- Entity documents missing or incomplete

**Example:** Credit report dated 135 days prior (5 days beyond standard)

### Timing Exceptions
Administrative timing issues not affecting loan quality:
- Entity registration in property state not yet complete (but scheduled)
- Final payoff statement pending from prior lender
- Appraisal recertification in process
- Background check update in progress

**Example:** LLC registered in property state within 15 days of closing

### Derogatory Credit Exceptions
Serious credit events requiring investor review:
- Bankruptcy within seasoning period
- Foreclosure within seasoning period
- Short sale within seasoning period
- Recent fraud conviction
- Active litigation
- Federal tax liens

**Example:** Chapter 7 bankruptcy discharged 3 years ago (4-year seasoning required)

---

## 12.2 Approval Authority Tiers

### Tier 1: Internal (USDV Processor/Senior Underwriter)

**Authority Level:** Can approve without investor submission  
**Escalation Path:** None required

**Approvable Exceptions:**
| Exception Type | Criteria | Authority |
|---|---|---|
| Documentation Timing | Document 1-15 days beyond standard currency | Processor |
| Minor Credit Variance | FICO 5-10 points below threshold with strong compensating factors (liquidity >150%, experience 5+ deals) | Sr. Underwriter |
| Entity Registration Timing | Foreign entity registering in property state within 15 days of closing | Processor |
| Good Standing Timing | Good standing certificate 91-120 days old but entity currently active | Processor |
| Small Payoff Discrepancy | Closing cost estimate ±2% of actual payoff (when minor variance discovered) | Sr. Underwriter |

**Approval Process:**
1. Underwriter identifies exception
2. Documents compensating factors in loan file
3. Documents exception type and specific variance
4. Records approval with initials and date
5. No submission to investor required

---

### Tier 2: USDV Management (Underwriting Manager)

**Authority Level:** Requires USDV management sign-off; investor approval not typically required  
**Escalation Path:** Tier 1 underwriter → Underwriting Manager

**Approvable Exceptions:**
| Exception Type | Criteria | Authority |
|---|---|---|
| Experience Shortfall | 1-2 deals short of minimum with strong credit (FICO 680+) + high liquidity (>150%) + prior relationship | UW Manager |
| Modest LTV Variance | 1-2% over guideline maximum with strong DSCR (>1.25x) or heavy down payment | UW Manager |
| Property Condition C5 | C5 with detailed, appraiser-approved remediation plan + completion timeline | UW Manager |
| Non-Warrantable Condo | Non-warrantable condo with clear HOA history + no pending litigation | UW Manager |
| Market Timing | Property in declining market (-5% to -10% HPA) with strong cash flow support | UW Manager |

**Approval Process:**
1. Tier 1 underwriter completes initial evaluation
2. Creates exception memo documenting:
   - Specific guideline deviation
   - Quantified impact
   - Compensating factors
   - Risk mitigation strategy
3. Submits to Underwriting Manager for review
4. Manager approves or requests additional information
5. Exception documented in loan file with manager approval
6. **Not submitted to investor** (within USDV discretion)

---

### Tier 3: Investor Approval Required

**Authority Level:** Must be submitted to investor for written approval  
**Escalation Path:** Tier 2 manager → Investor Submission

**Exceptions Requiring Investor Approval:**
| Exception Type | Criteria | Authority |
|---|---|---|
| Credit Exception | FICO >20 points below minimum (e.g., 640 for 660 RTL minimum) | Investor |
| Major LTV Exception | >2% above guideline maximum LTV | Investor |
| Derogatory Credit | Bankruptcy or foreclosure within seasoning period | Investor |
| Property Type Exception | Property type outside eligible list (non-SFR, non-condo, etc.) | Investor |
| Experience Exception | First-time investor or significant deal count shortfall (>3 deals) | Investor |
| DSCR Exception | DSCR 0.20x+ below minimum requirement | Investor |
| Heavy Rehab (Multi-Property) | Heavy rehab definition triggered on cross-collateralized portfolio | Investor |
| Foreign National | Foreign national borrower requiring enhanced underwriting | Investor |
| Small Multifamily (5-9 Units) | 5-9 unit property on RTL (leverage reduction already applied) | Investor |

**Approval Process:**
1. Underwriting Manager prepares investor exception request
2. Uses standardized Exception Request Template (see 12.3)
3. Assembles supporting documentation:
   - Credit analysis
   - Property appraisal summary
   - Compensating factors narrative
   - Financial strength summary
4. Submits to investor via designated channel
5. Tracks submission date and investor response deadline
6. Receives written investor approval/denial
7. Documents response in loan file

---

### Tier 4: Not Approvable

**Authority Level:** USDV will not approve, regardless of compensating factors  
**Action:** Loan should be declined

**Non-Approvable Exceptions:**
| Exception Type | Reason | Authority |
|---|---|---|
| OFAC/Sanctions Match | Regulatory prohibition - no override possible | Compliance |
| Active Fraud Investigation | Active federal fraud charges | Compliance |
| Recent Fraud Conviction | Fraud conviction within 7 years | Underwriting |
| FICO Below 620 | Below all program minimums (RTL=660, DSCR=680) | Underwriting |
| Active Bankruptcy | Cannot close during active Chapter 7/13 bankruptcy | Underwriting |
| Felony Conviction (Drug/Violence) | Felony drug conviction or violent crime | Underwriting |
| Condemned Property | Property declared uninhabitable by municipality | Underwriting |
| Active Litigation (Property) | Active litigation naming borrower/property | Underwriting |

**Decision Authority:** Underwriting Manager (no escalation, decline recommended)

---

## 12.3 Exception Request Process

### Process Flow

```
Guideline Deviation Identified
         │
         ▼
Categorize Exception Type
         │
         ├─→ Tier 1 Exception? ──→ [Processor Approval] ──→ Document & Close
         │
         ├─→ Tier 2 Exception? ──→ [Manager Review] ──→ [Manager Approval] ──→ Document & Close
         │
         ├─→ Tier 3 Exception? ──→ [Manager Prepares Request] ──→ [Investor Submission] 
         │                                │
         │                                ├─→ [Investor Approved] ──→ Document & Close
         │                                │
         │                                └─→ [Investor Denied] ──→ [Escalate/Decline]
         │
         └─→ Tier 4 Exception? ──→ [DECLINE - Not Approvable]
```

### Exception Request Template

```
═══════════════════════════════════════════════════════════════════════════════
                            EXCEPTION REQUEST
═══════════════════════════════════════════════════════════════════════════════

DEAL INFORMATION
────────────────────────────────────────────────────────────────────────────────
Property Address:        [Full street address, city, state, ZIP]
Loan Type:               [Fix & Flip / Ground-Up / Bridge / DSCR]
Loan Amount:             $[Amount] (formatted with commas)
Loan Purpose:            [Purchase / Refinance / Cash-Out]
Investor:                [Eastview / ArchWest]
Loan Officer:            [Name]
Underwriter:             [Name]
Exception Requested By:  [Name and Title]
Date Submitted:          [MM/DD/YYYY]


EXCEPTION REQUESTED
────────────────────────────────────────────────────────────────────────────────

Exception Type:          [Credit / Experience / LTV / Property / Documentation / 
                          Timing / Derogatory]

Guideline Requirement:   [State the requirement exactly as written in guidelines]

Current/Actual Value:    [What the deal presents]

Requested Approval:      [What exception being requested]

Variance Magnitude:      [Quantify the gap, e.g., "15 points below FICO minimum"]


GUIDELINE REFERENCE
────────────────────────────────────────────────────────────────────────────────

Program:                 [USDV Guidelines / RTL / DSCR]

Section:                 [Section number and title from manual or investor guideline]

Exact Requirement Text:  [Quote the guideline verbatim]

Source Document:         [Investor Underwriting Guidelines - Version/Date]


DEAL SPECIFICS
────────────────────────────────────────────────────────────────────────────────

[Include specific data relevant to exception type:]

FOR CREDIT EXCEPTIONS:
  • Tri-Merge FICO Score:        [Score with tri-merge breakdown]
  • Credit Report Date:          [MM/DD/YYYY]
  • Trade Lines:                 [Number total, active, with 24+ mo history]
  • Recent 30-Day Lates:         [Number in last 12 months]
  • Bankruptcies/Foreclosures:   [Details with dates]
  • Judgments/Liens:             [Amounts and status]

FOR EXPERIENCE EXCEPTIONS:
  • Deals Completed (36 mo):     [Count]
  • Deals Completed (lifetime):  [Count]
  • Property Types Experience:   [Detail]
  • Prior Business Purpose Loans: [Yes/No; count if yes]
  • Real Estate License:         [Yes/No; type]

FOR LTV EXCEPTIONS:
  • As-Is Value:                 $[Amount]
  • ARV (if applicable):         $[Amount]
  • Loan Amount:                 $[Amount]
  • Calculated LTV:              [Percentage]%
  • Maximum Allowed LTV:         [Percentage]%
  • Variance:                    [Percentage] points over max
  • Appraisal Date:             [MM/DD/YYYY]
  • ARV Support Summary:        [Brief narrative on comps]

FOR PROPERTY EXCEPTIONS:
  • Property Type:               [Description]
  • Condition Rating:            [C1-C6]
  • Issue Description:           [What makes it non-standard]
  • Remediation Plan:            [If applicable; timeline/cost]
  • Location/Market:             [Market fundamentals]

FOR DOCUMENTATION EXCEPTIONS:
  • Document Type:               [Credit report / Appraisal / Bank Stmt / etc]
  • Required Currency:           [Days]
  • Actual Age:                  [Days]
  • Days Overdue:                [Number]
  • Reason for Delay:            [Explanation]
  • Status:                      [When expected to be current]


MITIGATING FACTORS
────────────────────────────────────────────────────────────────────────────────

Mitigating factors are strengths in the deal that offset the exception. List each
factor with quantified impact where possible.

• [Factor 1 - Quantified Impact]
  Strength: [Why this matters]
  Impact: [How it mitigates the exception]

• [Factor 2 - Quantified Impact]
  Strength: [Why this matters]
  Impact: [How it mitigates the exception]

• [Factor 3 - Quantified Impact]
  Strength: [Why this matters]
  Impact: [How it mitigates the exception]

Examples of strong mitigating factors:
  • Strong liquidity: "Verified liquidity of $285K (156% of requirement)"
  • Strong credit elsewhere: "FICO of 655 offset by 18 prior deals with perfect 
    payment history"
  • Low leverage: "70% LTARV provides 5-point cushion despite FICO shortfall"
  • Strong cash flow: "DSCR of 1.35x significantly exceeds 1.00x minimum"
  • Market support: "Property in appreciating market (+8% YoY) per county records"
  • Track record: "Guarantor has 25+ completed fix & flip projects"
  • Loan structure: "Floating rate 1% above market reduces risk; pre-approval 
    from exit lender confirms refinance capability"


COMPENSATING STRENGTHS
────────────────────────────────────────────────────────────────────────────────

Beyond mitigating factors, describe any broader strengths in borrower, property,
or deal structure:

• [Strength 1: e.g., strong relationship history, prior funded deals, etc]

• [Strength 2: e.g., property in high-demand market, unique value-add opportunity]

• [Strength 3: e.g., guarantor has significant net worth, diversified portfolio]


RISK ASSESSMENT
────────────────────────────────────────────────────────────────────────────────

Despite the exception, what risks remain and how are they managed?

Primary Risk:            [What could go wrong]
  Likelihood:            [High / Medium / Low]
  Impact if Occurs:      [Potential loss amount]
  Mitigation:            [How USDV controls this risk]
  Loan Structure Impact: [Any terms adjusted for this risk]

Secondary Risk:          [Other considerations]
  [Similar structure]


RECOMMENDATION
────────────────────────────────────────────────────────────────────────────────

USDV Capital recommends [APPROVAL / CONDITIONAL APPROVAL / DENIAL] of this 
exception based on the following:

[1-3 sentences summarizing why the exception is/isn't justified. Focus on how
compensating factors and deal fundamentals outweigh the guideline deviation.]


APPROVALS & SIGNATURES
────────────────────────────────────────────────────────────────────────────────

Underwriter:
  Name: ________________________________    Date: __________________
  Signature: ____________________________

Underwriting Manager:
  Name: ________________________________    Date: __________________
  Signature: ____________________________

Investor Response (if required):
  Received: ____________________________    Date: __________________
  Status: [Approved / Denied / Conditional]
  Conditions (if any): ________________________________________________________________
  Approved By: __________________________    Title: __________________

═══════════════════════════════════════════════════════════════════════════════
```

### Documentation Requirements for Submission

When submitting exceptions to investors, include:

**For Credit Exceptions:**
- Current tri-merge credit report
- Letters of explanation for adverse items
- Recent 2 months bank statements
- Summary of all derogatory items with seasoning dates

**For Experience Exceptions:**
- Schedule of real estate owned (detailed with dates and sale prices)
- Documentation of prior deals (HUDs, settlement statements, or proof of sales)
- Property management documentation
- Prior mortgage performance letters (if available)

**For LTV Exceptions:**
- Full appraisal with comparable analysis
- Second valuation (ARR/CDA if requested)
- Purchase/refinance documentation
- Construction budget (if applicable)

**For Property Exceptions:**
- Full appraisal with photos
- Inspection report or repair estimate (if C5 condition)
- Title commitment
- HOA documents (if condo)
- Environmental assessment (if required)

**For Derogatory Exceptions:**
- Bankruptcy discharge papers or court documents
- Foreclosure deed or settlement documents
- Tax lien release or payment agreement
- Any correspondence showing resolution status

---

## 12.4 Compensating Factors Framework

Compensating factors are strengths in the borrower profile, property, or deal structure that offset guideline deviations. To be considered a strong compensating factor, it must be:

- **Quantifiable** - Expressed as a percentage, dollar amount, or measurable metric
- **Verifiable** - Documented in loan file (bank statements, credit reports, deeds, etc.)
- **Relevant** - Directly addresses the risk created by the exception
- **Significant** - Material enough to meaningfully reduce the exception's impact

### Primary Compensating Factors

#### 1. Liquidity Reserves
**Standard Requirement:** Varies by product (typically 2-6 months PITIA/DSCR)

**Strong Compensating Factor:** 
- Liquidity >150% of requirement
- Liquid assets in diversified accounts (not dependent on single investment)
- Bank statements showing consistent balances

**Example:** "Verified liquidity of $285,000 (156% of $182,500 requirement). Sources: Chase checking ($65K), Wells Fargo money market ($95K), Vanguard brokerage ($125K). Average 6-month balance confirms stability."

#### 2. Real Estate Experience
**Standard Requirement:** Varies by product and tier (typically 1-5+ deals)

**Strong Compensating Factor:**
- 10+ completed deals in same product type
- 5+ deals in last 24 months demonstrating active portfolio
- Professional real estate license or real estate agent credential
- Property management license or designation
- Prior business-purpose loan experience

**Example:** "Guarantor has completed 18 fix & flip projects over 7 years. All projects closed on schedule. Portfolio performance: Average hold time 14 months (within target), average profit margin 18% on gross project costs. Prior relationship with USDV: 3 loans funded, all performing on schedule."

#### 3. Credit Strength (Outside of FICO)
**Standard FICO Minimum:** 660 (RTL), 680 (DSCR)

**Strong Compensating Factor:**
- 5+ years with no late payments on real estate
- Perfect payment history on all trade lines (0 lates in 24 months)
- Low overall utilization (<30% of total credit available)
- Multiple active trade lines (5+ active accounts)
- Prior relationship with USDV (good standing on prior loans)

**Example:** "While FICO of 655 is 5 points below minimum, guarantor demonstrates strong payment discipline: 8 years of on-time mortgage payments on prior investment property, all 12 trade lines current, no collections or judgments. Perfect 24-month payment history across $350K in credit facilities."

#### 4. Equity Position / Low Leverage
**Standard Maximum LTV:** Varies by product, classification, purpose (60-90%)

**Strong Compensating Factor:**
- 30%+ equity cushion (LTV ≤70%)
- Low LTARV (≤65% even if LTV is higher)
- Strong DSCR (>1.30x) even if at leverage limit
- Significant down payment (20%+ for purchase)
- Cross-collateralized portfolio with >30% aggregate equity

**Example:** "Despite modest 78% LTV due to property appreciation, deal is protected by 65% LTARV based on conservative ARV with strong comparable support. Guarantor contributing 22% equity ($175K cash). Exit strategy through sale provides substantial margin (ARV less debt = $145K equity buffer)."

#### 5. Strong Cash Flow (DSCR Loans)
**Standard Minimum DSCR:** 1.00x (FICO 700+), 1.20x (FICO <700, foreign nationals, 5-9 units)

**Strong Compensating Factor:**
- DSCR 1.25x+ significantly exceeds minimum
- Rent-to-value >0.85% indicating market-rate tenancy
- Documented 12-month history of strong collections (if refinance)
- Lease terms favorable (multi-year, no renewal risk)
- Property in appreciating market with strong absorption rates

**Example:** "Property achieves 1.38x DSCR with below-market rent assumptions (95% of market average). Lease has 2.5-year remaining term with no renewal risk. Tenant has 18-month payment history with $0 delinquency. Market fundamentals strong: MSA population +2.1% YoY, average rent growth +3.2% YoY."

#### 6. Property Fundamentals
**Strong Compensating Factor:**
- Recent significant capital improvement reducing condition risk
- Prime location in supply-constrained market
- Property type in strong local demand
- Documented market appreciation (5%+ annually)
- Essential services property or institutional tenant (DSCR)

**Example:** "Subject property C5 condition is fully offset by: (1) licensed contractor hired with $65K budget, (2) detailed scope of work with 60-day timeline, (3) appraiser confirmation that repairs will bring to C3 condition, (4) post-repair ARV of $485K supporting strong equity position. Market appreciation at 6% YoY supports stabilized value."

#### 7. Loan Structure
**Strong Compensating Factor:**
- Appropriate floating rate structure matching holding period
- Interest reserve account providing cushion
- Rate lock with exit lender confirmed pre-closing
- Loan term aligned with project timeline (no extension risk)
- Appropriate prepayment penalty structure reducing rate risk

**Example:** "Floating rate of Prime + 4.0% (currently 9.25%) is appropriate for 18-month GUC timeline. Guarantor has pre-approval from permanent DSCR lender committing to refi at 7.5% fixed for 30-year amortization at completion. Rate floor at current market minimizes extension risk."

#### 8. Prior Relationship
**Strong Compensating Factor:**
- USDV has funded prior loan(s) to guarantor
- All prior USDV loans performing on schedule
- Increased loan amount demonstrates confidence
- Demonstrated ability to manage USDV underwriting requirements
- No payment delays or covenant violations on prior USDV loans

**Example:** "USDV has funded 2 prior loans to this guarantor: $450K fix & flip in 2023 (closed on schedule, currently performing) and $380K bridge in 2022 (early payoff, no issues). Strong relationship history with USDV demonstrates ability to execute and manage investor requirements."

---

## 12.5 Exception Management Rules

### General Rules

1. **Every exception must be documented.** Verbal approvals are not sufficient. Written documentation with signature/date required for all tiers.

2. **Compensating factors must be objective.** Subjective statements like "good guy" or "strong operator" are not acceptable. Use specific, quantifiable metrics.

3. **Multiple exceptions compound the requirement level.** If a single loan has exceptions in multiple categories, escalate to next tier. Two Tier 1 exceptions may warrant Tier 2 review.

4. **Resubmission of same exception.** If an investor denies an exception, resubmission requires significant new compensating factors. Cannot resubmit with same supporting documentation.

5. **Exception approval is loan-specific.** Approval of FICO exception for one guarantor does not establish precedent for future loans with same guarantor.

6. **Documentation timing is strict.** Tier 1 exceptions require processor documentation within 2 business days of exception identification. Tier 2 requires manager review within 3 business days.

### Exception Tracking

All exceptions (regardless of tier) must be:

1. **Logged in loan management system** with:
   - Exception type
   - Specific guideline reference
   - Quantified variance
   - Tier level
   - Approval date and authority

2. **Compiled into monthly exception report** showing:
   - Count by tier
   - Count by exception type
   - Count by investor
   - Approval vs. denial rate
   - Any trends requiring guideline review

3. **Available for investor audit** - Investors periodically review USDV exception handling to ensure consistency and appropriate usage

### Exception Denial Handling

When an exception is denied (investor or internal):

1. Underwriting Manager meets with Loan Officer to discuss options:
   - Modify loan structure to eliminate exception
   - Request guarantor provide additional compensating factors
   - Decline the loan application

2. If loan is declined:
   - Document reason in CRM
   - Send professional decline letter to borrower
   - Offer to revisit if circumstances change

3. If exception is resubmitted after denial:
   - Document new compensating factors explicitly
   - Reference prior submission and new information provided
   - Note whether investor requested specific additional documentation

---

## 12.6 Python Code: Exception Management

```python
from enum import Enum
from typing import List, Optional, Dict
from dataclasses import dataclass, field
from datetime import datetime, timedelta

class ExceptionType(str, Enum):
    """Exception category enumeration."""
    CREDIT = "credit"
    EXPERIENCE = "experience"
    LEVERAGE = "leverage"
    PROPERTY = "property"
    DOCUMENTATION = "documentation"
    TIMING = "timing"
    DEROGATORY = "derogatory"

class ApprovalTier(str, Enum):
    """Approval authority tier."""
    TIER_1 = "tier_1"          # Processor/Sr. Underwriter
    TIER_2 = "tier_2"          # Underwriting Manager
    TIER_3 = "tier_3"          # Investor
    TIER_4 = "tier_4"          # Not approvable

class ExceptionStatus(str, Enum):
    """Exception lifecycle status."""
    IDENTIFIED = "identified"
    SUBMITTED = "submitted"
    APPROVED = "approved"
    DENIED = "denied"
    WITHDRAWN = "withdrawn"

@dataclass
class CompensatingFactor:
    """Represents a single compensating factor."""
    category: str
    description: str
    quantified_value: Optional[str] = None
    verification_source: str = ""
    impact_on_exception: str = ""
    strength_level: str = "moderate"  # weak, moderate, strong
    
    def is_strong(self) -> bool:
        """Determine if this is a strong compensating factor."""
        return self.strength_level == "strong" and self.quantified_value is not None

@dataclass
class ExceptionRequest:
    """Complete exception request."""
    id: str
    deal_id: str
    loan_officer: str
    underwriter: str
    
    # Exception details
    exception_type: ExceptionType
    guideline_requirement: str
    current_value: str
    requested_approval: str
    variance_description: str
    
    # Loan context
    property_address: str
    loan_type: str
    loan_amount: float
    investor: str
    
    # Supporting data
    compensating_factors: List[CompensatingFactor] = field(default_factory=list)
    mitigating_factors: List[str] = field(default_factory=list)
    supporting_documents: List[str] = field(default_factory=list)
    
    # Status tracking
    approval_tier: Optional[ApprovalTier] = None
    status: ExceptionStatus = ExceptionStatus.IDENTIFIED
    created_at: datetime = field(default_factory=datetime.now)
    submitted_at: Optional[datetime] = None
    reviewed_at: Optional[datetime] = None
    approved_at: Optional[datetime] = None
    approved_by: Optional[str] = None
    investor_response: Optional[str] = None
    investor_conditions: List[str] = field(default_factory=list)
    denial_reason: Optional[str] = None
    
    def add_compensating_factor(self, factor: CompensatingFactor) -> None:
        """Add a compensating factor to the request."""
        self.compensating_factors.append(factor)
    
    def add_mitigating_factor(self, factor: str) -> None:
        """Add a mitigating factor description."""
        self.mitigating_factors.append(factor)
    
    def strong_factors_count(self) -> int:
        """Count strong compensating factors."""
        return sum(1 for f in self.compensating_factors if f.is_strong())
    
    def is_complete(self) -> bool:
        """Check if exception request has minimal required elements."""
        return (
            len(self.compensating_factors) > 0 and
            len(self.supporting_documents) > 0 and
            self.variance_description.strip() != ""
        )

class ExceptionManager:
    """Manage exception identification and routing."""
    
    # Tier 1 approvable exceptions
    TIER_1_EXCEPTIONS = {
        ExceptionType.DOCUMENTATION: {
            "max_variance": 15,  # days
            "requires_strong_factors": False,
        },
        ExceptionType.TIMING: {
            "max_variance": 15,  # days
            "requires_strong_factors": False,
        },
    }
    
    # Tier 2 approvable exceptions
    TIER_2_EXCEPTIONS = {
        ExceptionType.CREDIT: {
            "max_fico_variance": 10,
            "requires_strong_factors": True,
            "required_factors": 3,
        },
        ExceptionType.EXPERIENCE: {
            "max_deal_shortfall": 2,
            "requires_strong_factors": True,
            "required_factors": 2,
        },
        ExceptionType.LEVERAGE: {
            "max_ltv_variance": 2,
            "requires_strong_factors": True,
            "required_factors": 2,
        },
        ExceptionType.PROPERTY: {
            "approvable_conditions": ["c5_with_plan", "non_warrantable_condo"],
            "requires_strong_factors": True,
            "required_factors": 2,
        },
    }
    
    # Tier 3 exceptions (investor submission required)
    TIER_3_EXCEPTIONS = {
        ExceptionType.CREDIT,
        ExceptionType.EXPERIENCE,
        ExceptionType.LEVERAGE,
        ExceptionType.PROPERTY,
        ExceptionType.DEROGATORY,
    }
    
    # Tier 4 exceptions (not approvable)
    TIER_4_EXCEPTIONS = {
        "ofac_match",
        "active_fraud_investigation",
        "recent_fraud_conviction",
        "fico_below_620",
        "active_bankruptcy",
        "violent_felony",
        "condemned_property",
    }
    
    def determine_approval_tier(self, exception: ExceptionRequest) -> ApprovalTier:
        """
        Determine appropriate approval tier for exception.
        
        Args:
            exception: ExceptionRequest to evaluate
            
        Returns:
            ApprovalTier indicating required approval level
        """
        # Check for Tier 4 first
        if self._is_tier_4(exception):
            return ApprovalTier.TIER_4
        
        # Check Tier 1
        if exception.exception_type in self.TIER_1_EXCEPTIONS:
            if self._qualifies_for_tier_1(exception):
                return ApprovalTier.TIER_1
        
        # Check Tier 2
        if exception.exception_type in self.TIER_2_EXCEPTIONS:
            if self._qualifies_for_tier_2(exception):
                return ApprovalTier.TIER_2
        
        # Default to Tier 3 (investor submission)
        return ApprovalTier.TIER_3
    
    def _is_tier_4(self, exception: ExceptionRequest) -> bool:
        """Check if exception is in Tier 4 (not approvable)."""
        # This would check specific deal characteristics
        # Simplified for demonstration
        return False
    
    def _qualifies_for_tier_1(self, exception: ExceptionRequest) -> bool:
        """Check if exception qualifies for Tier 1 (internal) approval."""
        if exception.exception_type not in self.TIER_1_EXCEPTIONS:
            return False
        
        tier_1_rules = self.TIER_1_EXCEPTIONS[exception.exception_type]
        
        # For documentation/timing: must be within acceptable variance
        if "max_variance" in tier_1_rules:
            # Parse variance from exception description
            # This is simplified; actual implementation would extract number
            return True
        
        return False
    
    def _qualifies_for_tier_2(self, exception: ExceptionRequest) -> bool:
        """Check if exception qualifies for Tier 2 (management) approval."""
        if exception.exception_type not in self.TIER_2_EXCEPTIONS:
            return False
        
        tier_2_rules = self.TIER_2_EXCEPTIONS[exception.exception_type]
        
        # Check strong factors requirement
        if tier_2_rules.get("requires_strong_factors", False):
            required = tier_2_rules.get("required_factors", 1)
            if exception.strong_factors_count() < required:
                return False
        
        return True
    
    def generate_exception_request(
        self,
        deal_id: str,
        loan_officer: str,
        underwriter: str,
        exception_type: ExceptionType,
        guideline_requirement: str,
        current_value: str,
        requested_approval: str,
        variance_description: str,
        property_address: str,
        loan_type: str,
        loan_amount: float,
        investor: str,
    ) -> ExceptionRequest:
        """
        Create a new exception request.
        
        Args:
            [All parameters as listed above]
            
        Returns:
            New ExceptionRequest object
        """
        request = ExceptionRequest(
            id=f"EXC-{deal_id}-{datetime.now().strftime('%Y%m%d%H%M%S')}",
            deal_id=deal_id,
            loan_officer=loan_officer,
            underwriter=underwriter,
            exception_type=exception_type,
            guideline_requirement=guideline_requirement,
            current_value=current_value,
            requested_approval=requested_approval,
            variance_description=variance_description,
            property_address=property_address,
            loan_type=loan_type,
            loan_amount=loan_amount,
            investor=investor,
        )
        
        return request
    
    def route_for_approval(self, exception: ExceptionRequest) -> Dict:
        """
        Route exception to appropriate approval authority.
        
        Args:
            exception: ExceptionRequest to route
            
        Returns:
            Dictionary with routing details:
                {
                    "tier": ApprovalTier,
                    "required_by": str,
                    "deadline": datetime,
                    "requires_investor": bool,
                }
        """
        tier = self.determine_approval_tier(exception)
        
        approval_map = {
            ApprovalTier.TIER_1: {
                "required_by": "Processor/Sr. Underwriter",
                "deadline_hours": 48,
            },
            ApprovalTier.TIER_2: {
                "required_by": "Underwriting Manager",
                "deadline_hours": 72,
            },
            ApprovalTier.TIER_3: {
                "required_by": "Investor",
                "deadline_hours": 240,  # 10 business days
            },
            ApprovalTier.TIER_4: {
                "required_by": "Decline",
                "deadline_hours": 24,
            },
        }
        
        details = approval_map[tier]
        deadline = datetime.now() + timedelta(hours=details["deadline_hours"])
        
        return {
            "tier": tier,
            "required_by": details["required_by"],
            "deadline": deadline,
            "requires_investor": tier == ApprovalTier.TIER_3,
            "is_approvable": tier != ApprovalTier.TIER_4,
        }
    
    def validate_request_completeness(
        self,
        exception: ExceptionRequest
    ) -> tuple[bool, List[str]]:
        """
        Validate that exception request has all required elements.
        
        Returns:
            Tuple of (is_complete, missing_elements)
        """
        missing = []
        
        if not exception.guideline_requirement:
            missing.append("Guideline requirement")
        
        if not exception.current_value:
            missing.append("Current/actual value")
        
        if not exception.variance_description:
            missing.append("Variance description")
        
        if len(exception.compensating_factors) == 0:
            missing.append("Compensating factors")
        
        if len(exception.supporting_documents) == 0:
            missing.append("Supporting documentation")
        
        # Tier 2 and above require multiple strong factors
        if self.determine_approval_tier(exception) in [ApprovalTier.TIER_2, ApprovalTier.TIER_3]:
            if exception.strong_factors_count() < 2:
                missing.append("Minimum 2 strong compensating factors")
        
        return (len(missing) == 0, missing)
```

---

## 12.7 Integration with INSPIRE

Exception management in INSPIRE Phase 7 operates as follows:

1. **Auto-Detection**: When AI analysis identifies red flags during document review, system categorizes them by exception type
2. **Draft Generation**: Exception request templates are auto-populated with extracted data
3. **Routing Recommendation**: System suggests approval tier based on exception characteristics
4. **Manual Review**: Underwriter reviews auto-drafted request, adds compensating factors, and routes accordingly
5. **Status Tracking**: INSPIRE tracks all exceptions from submission through investor response

---

## Open Questions

None at this time. All exception requirements have been synthesized from IMPLEMENTATION_PLAN_V2 and INSPIRE Phase 7 PRD.

---

*End of Section 12*

