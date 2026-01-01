---
section: 4
title: Credit & Background Evaluation
version: 1.0
last_updated: 2025-12-30
model_used: sonnet
guideline_sources:
  - Archwest RTL Guidelines
  - Eastview RTL Guidelines v4.1
  - Eastview DSCR Guidelines v7.2
  - Archwest DSCR Guidelines v1.8
changelog:
  - 2025-12-30: Initial creation
---

# Section 4: Credit & Background Evaluation

## 4.1 Overview

Credit and background evaluation is a critical component of borrower underwriting. This section establishes standards for analyzing credit reports, evaluating payment history, assessing derogatory credit events, and conducting background checks. These standards directly support INSPIRE Phase 7's automated analysis and flag generation capabilities.

**INSPIRE Integration Points:**
- Phase 3-4: FICO score extraction for classification and pricing
- Phase 7: Automated credit report analysis and flag generation
- Phase 7: Background check review and risk assessment

---

## 4.2 Credit Report Requirements

### 4.2.1 Required Report Type

**Tri-Merge Credit Report:**
- Must include data from all three bureaus: Equifax, Experian, TransUnion
- Residential Mortgage Credit Report (RMCR) format preferred
- Soft pull acceptable for pre-qualification; hard pull required for final underwriting
- Report must include:
  - Credit scores from all three bureaus
  - Complete trade line history
  - Public records (bankruptcies, judgments, liens)
  - Inquiries (last 24 months)
  - Address history

**Report Currency:**
- Maximum age: 120 days from note date
- If report expires during processing, new report required
- No exceptions to 120-day rule

**Required for All:**
- All borrowers (individual loans)
- All guarantors (entity loans)
- All individuals with ≥20% ownership
- All individuals with operational control

### 4.2.2 Credit Score Determination

**FICO Score Extraction:**

For each borrower/guarantor, obtain scores from all three bureaus:
- Equifax Beacon 5.0
- Experian Fair Isaac
- TransUnion FICO Risk Score Classic 04

**Representative Score Selection:**

| Number of Scores | Representative Score |
|------------------|---------------------|
| 3 scores available | Middle (median) score |
| 2 scores available | Lower of the two scores |
| 1 score available | That score (requires explanation) |
| 0 scores available | Not eligible (see Section 4.2.3) |

**Example Score Determinations:**

```
Example 1: Three Scores Available
Equifax: 720
Experian: 705
TransUnion: 715
Representative Score = 715 (middle score)

Example 2: Two Scores Available
Equifax: 695
Experian: 710
TransUnion: No score
Representative Score = 695 (lower of two)

Example 3: One Score Available
Equifax: 680
Experian: No score
TransUnion: No score
Representative Score = 680 (requires underwriter review)
```

### 4.2.3 Insufficient Credit History

**No Credit Score Scenarios:**

If borrower has no credit score from any bureau:
- **RTL Loans**: Not eligible (minimum 1 score required)
- **DSCR Loans**: Not eligible (minimum 1 score required)
- **Exception**: Foreign Nationals with foreign credit history may be eligible with:
  - Foreign credit report with translation
  - Minimum 3 trade lines with 24-month history
  - Alternative documentation of creditworthiness
  - Investor approval required

**Thin File (Limited Credit History):**
- Borrower has score but limited trade lines
- See Section 4.3 for minimum trade line requirements
- May require additional compensating factors

---

## 4.3 Trade Line Requirements

### 4.3.1 Minimum Trade Line Standards

**Trade Line Definitions:**

| Trade Line Type | Description | Counts Toward Minimum? |
|-----------------|-------------|------------------------|
| **Revolving** | Credit cards, lines of credit | Yes |
| **Installment** | Auto loans, personal loans, student loans | Yes |
| **Mortgage** | First mortgages, HELOCs | Yes |
| **Authorized User** | Credit card where borrower is authorized user | No (unless primary borrower) |
| **Closed** | Paid-off accounts | Yes (if within 24 months) |

**Minimum Requirements:**

| Requirement | Standard | Notes |
|-------------|----------|-------|
| **Total Trade Lines** | Minimum 3 | Active or closed within 24 months |
| **Active Trade Lines** | Minimum 1 | Currently open and reporting |
| **24-Month History** | Minimum 1 trade line | Continuous reporting for 24+ months |
| **Authorized User Accounts** | Do not count | Unless borrower is also primary |

### 4.3.2 Trade Line Analysis

**Payment History Review:**

For each trade line, evaluate:
- Current status (current, 30 days late, 60 days late, etc.)
- Payment history (last 24 months minimum)
- High balance and current balance
- Credit limit (for revolving accounts)
- Original loan amount (for installment accounts)

**Red Flags:**
- Multiple recent late payments (last 12 months)
- High credit utilization (>80% of available credit)
- Recent charge-offs or collections
- Accounts in default status

**Green Flags:**
- All accounts current
- Low credit utilization (<30%)
- Long credit history (10+ years)
- Mix of credit types (revolving and installment)

### 4.3.3 Authorized User Considerations

**Authorized User Accounts:**
- Do not count toward minimum trade line requirements
- May be considered for credit score purposes (bureau-dependent)
- Underwriter may request removal if inflating score significantly

**Primary vs. Authorized User:**
- Credit report should indicate account status
- If unclear, request documentation from creditor
- Primary accounts count; authorized user accounts do not

---

## 4.4 Mortgage History Analysis

### 4.4.1 Housing Payment History Standards

Mortgage payment history is the strongest predictor of future mortgage performance. Strict standards apply to housing lates.

**RTL Product Standards:**

| Late Payment History (12 months) | Status | Notes |
|----------------------------------|--------|-------|
| 0x30 | Acceptable | Preferred |
| 1x30 | Acceptable with review | Requires explanation |
| 2x30 or 1x60 | Not acceptable | Exception required |
| 1x90+ | Not acceptable | No exceptions |

**DSCR Product Standards:**

| Late Payment History (12 months) | Status | Notes |
|----------------------------------|--------|-------|
| 0x30 | Acceptable | Preferred |
| 1x30 | Acceptable | Standard |
| 2x30 | Acceptable with review | Requires explanation |
| 1x60 | Not acceptable | Exception required |
| 1x90+ | Not acceptable | No exceptions |

**Housing Payment History (24 months):**

| Late Payment History (13-24 months ago) | Status | Notes |
|-----------------------------------------|--------|-------|
| 0x30 | Acceptable | Preferred |
| 1-2x30 | Acceptable | Standard |
| 1x60 | Acceptable with review | Requires explanation |
| 2x60 or 1x90+ | Not acceptable | Exception required |

### 4.4.2 Mortgage Late Payment Definitions

**30-Day Late (1x30):**
- Payment received 30-59 days after due date
- Reported to credit bureaus as "30 days late"

**60-Day Late (1x60):**
- Payment received 60-89 days after due date
- Reported as "60 days late"

**90-Day Late (1x90):**
- Payment received 90+ days after due date
- Reported as "90 days late"
- Severe derogatory event

**Current After Late:**
- Account brought current after late payment
- Late payment remains on credit report for 7 years
- Recent lates (last 12 months) more impactful than older lates

### 4.4.3 No Mortgage History

**Borrower with No Mortgage History:**
- Not automatically disqualifying
- Review rent payment history if available
- Evaluate other installment loan payment history
- May require additional compensating factors

**Rent Payment History:**
- 12-month rent payment history acceptable as substitute
- Must be verified through:
  - Cancelled checks or bank statements
  - Landlord verification letter
  - Rent payment service records
- Must show 0x30 in last 12 months

---

## 4.5 Derogatory Credit Events

### 4.5.1 Bankruptcy

Bankruptcy is a significant derogatory event requiring seasoning (time elapsed since discharge or dismissal).

**Chapter 7 Bankruptcy (Liquidation):**

| Timeframe | Eligibility | Documentation Required |
|-----------|-------------|------------------------|
| < 4 years from discharge | Not eligible | N/A |
| 4+ years from discharge | Eligible | Discharge papers, Schedule of Creditors |
| Dismissed (not discharged) | 2+ years from dismissal | Dismissal order |

**Chapter 13 Bankruptcy (Reorganization):**

| Timeframe | Eligibility | Documentation Required |
|-----------|-------------|------------------------|
| < 2 years from discharge | Not eligible | N/A |
| 2-4 years from discharge | Eligible with review | Discharge papers, payment history |
| 4+ years from discharge | Eligible | Discharge papers |
| < 4 years from filing (if dismissed) | Not eligible | N/A |
| Active Chapter 13 | Not eligible | Cannot close during active bankruptcy |

**Required Documentation:**
- Bankruptcy petition (all schedules)
- Discharge order or dismissal order
- Schedule of creditors (Schedule F)
- Explanation letter from borrower
- Evidence of re-established credit

**Underwriting Considerations:**
- Reason for bankruptcy (job loss, medical, business failure)
- Credit re-establishment since discharge
- Current financial stability
- Compensating factors

**Example Timeline:**
```
Chapter 7 Filed: January 1, 2020
Discharge Date: April 15, 2020
Eligible Date: April 15, 2024 (4 years from discharge)
Application Date: June 1, 2024 → Eligible
```

### 4.5.2 Foreclosure

Foreclosure is the lender's repossession of property due to mortgage default.

**Foreclosure Seasoning Requirements:**

| Timeframe | Eligibility | Documentation Required |
|-----------|-------------|------------------------|
| < 4 years from completion | Not eligible | N/A |
| 4+ years from completion | Eligible | Foreclosure documentation, explanation |

**Foreclosure Completion Date:**
- Date of foreclosure sale, OR
- Date of deed-in-lieu of foreclosure, OR
- Date of short sale closing

**Required Documentation:**
- Foreclosure notice or trustee's sale documents
- Final disposition documentation
- Credit report showing account status
- Explanation letter from borrower
- Evidence of re-established credit

**Extenuating Circumstances:**
- Job loss (with 6+ months unemployment)
- Serious illness or death in family
- Natural disaster
- May reduce seasoning to 3 years with investor approval

### 4.5.3 Short Sale and Deed-in-Lieu

**Short Sale:**
- Sale of property for less than mortgage balance
- Lender agrees to accept proceeds as full satisfaction
- Same seasoning as foreclosure: 4 years from closing

**Deed-in-Lieu of Foreclosure (DIL):**
- Borrower voluntarily transfers deed to lender
- Avoids formal foreclosure process
- Same seasoning as foreclosure: 4 years from transfer

**Documentation Required:**
- HUD-1 or closing statement (short sale)
- Lender approval letter showing deficiency waived
- Deed transfer documents (DIL)
- Credit report showing account status
- Explanation letter

### 4.5.4 Judgments and Liens

**Judgments:**

| Judgment Status | Amount | Eligibility | Action Required |
|-----------------|--------|-------------|-----------------|
| **Unpaid** | < $5,000 | Eligible | Document in file |
| **Unpaid** | $5,000 - $10,000 | Eligible with review | Payment plan or payoff |
| **Unpaid** | > $10,000 | Not eligible | Must be paid or on payment plan |
| **Paid** | Any amount | Eligible | Satisfaction of judgment required |
| **Payment Plan** | Any amount | Eligible | 6+ months payment history required |

**Required Documentation:**
- Court documents showing judgment details
- Satisfaction of judgment (if paid)
- Payment plan agreement (if on plan)
- Proof of 6+ months payments (if on plan)
- Explanation of circumstances

**Judgment Payment Plan Requirements:**
- Written agreement with creditor
- Minimum 6 months of on-time payments
- Payments must be current
- Payment amount included in debt-to-income (if applicable)

**Tax Liens:**

| Lien Type | Status | Eligibility | Action Required |
|-----------|--------|-------------|-----------------|
| **Federal Tax Lien** | Unpaid | Not eligible | Must be paid or subordinated |
| **Federal Tax Lien** | Paid | Eligible | Release of lien required |
| **State Tax Lien** | Unpaid | Not eligible | Must be paid or subordinated |
| **State Tax Lien** | Paid | Eligible | Release of lien required |
| **IRS Payment Plan** | Active | Eligible | 12+ months payment history |

**Tax Lien Documentation:**
- Notice of federal/state tax lien
- Release of lien (if paid)
- IRS payment plan agreement (if on plan)
- Proof of 12+ months payments (if on plan)
- Subordination agreement (if applicable)

**Mechanic's Liens:**
- Must be resolved prior to closing
- Cannot close with open mechanic's lien on subject property
- Lien on other properties: case-by-case review

**UCC Filings:**
- Review for potential conflicts with collateral
- Business-related UCC filings generally acceptable
- UCC on subject property may require subordination

### 4.5.5 Collections

**Collection Account Standards:**

| Total Collections | Status | Eligibility | Action Required |
|-------------------|--------|-------------|-----------------|
| < $2,000 total | Unpaid | Eligible | Document in file |
| $2,000 - $5,000 | Unpaid | Eligible with review | Explanation required |
| > $5,000 total | Unpaid | Not eligible | Must pay or payment plan |
| Any amount | Paid | Eligible | Paid in full letter |
| Medical collections | Any amount | Eligible | Generally disregarded |

**Collection Payment Requirements:**
- Collections > $5,000 must be paid in full or on payment plan
- Payment plan requires 3+ months payment history
- Medical collections generally disregarded regardless of amount
- Disputed collections: provide dispute documentation

**Required Documentation:**
- Credit report showing collection details
- Paid in full letter (if paid)
- Payment plan agreement (if on plan)
- Proof of payments (if on plan)
- Dispute documentation (if disputed)

**Medical Collections Exception:**
- Medical collections of any amount generally disregarded
- Must be clearly identified as medical on credit report
- If unclear, request documentation from borrower

---

## 4.6 Credit Exception Framework

### 4.6.1 Exception Categories

**Minor Credit Exceptions (Tier 1 - Internal Approval):**
- FICO 5-10 points below minimum with strong compensating factors
- 1x30 housing late 13-24 months ago
- Collections $2,000-$5,000 (explanation provided)
- Judgment < $5,000 (documented)

**Moderate Credit Exceptions (Tier 2 - Management Approval):**
- FICO 10-20 points below minimum with compensating factors
- 2x30 housing lates (not in last 12 months)
- 1x60 housing late (13-24 months ago)
- Collections $5,000-$10,000 (payment plan)
- Judgment $5,000-$10,000 (payment plan)

**Major Credit Exceptions (Tier 3 - Investor Approval Required):**
- FICO > 20 points below minimum
- Recent bankruptcy (3-4 years)
- Recent foreclosure (3-4 years)
- 1x90+ housing late (any timeframe)
- Multiple derogatory events

**Not Approvable (Tier 4):**
- FICO < 620
- Active bankruptcy
- Foreclosure < 3 years
- Recent fraud conviction
- OFAC match

### 4.6.2 Compensating Factors for Credit Exceptions

Strong compensating factors may support credit exception approval:

**Financial Strength:**
- Significant liquidity (150%+ of requirement)
- High net worth (200%+ of loan amount)
- Low debt-to-income ratio
- Substantial cash reserves

**Experience and Track Record:**
- Extensive real estate experience (10+ deals)
- Successful track record with USDV
- Strong business plan and exit strategy

**Deal Strength:**
- Conservative leverage (LTV < 70%)
- Strong property fundamentals
- Significant equity investment
- Strong DSCR (>1.30x for DSCR loans)

**Credit Re-establishment:**
- All accounts current for 12+ months
- New credit established since derogatory event
- Positive payment history on recent accounts

---

## 4.7 Background Check Evaluation

### 4.7.1 Background Check Requirements

**Required for All:**
- All borrowers (individual loans)
- All guarantors (entity loans)
- All individuals with ≥20% ownership
- All individuals with operational control

**Background Check Components:**
- Criminal history (federal and state)
- Civil litigation history
- OFAC/sanctions screening
- Sex offender registry
- Terrorist watch list

**Report Currency:**
- Maximum age: 120 days from note date
- Must be current as of closing

### 4.7.2 Criminal History Review

**Financial Crimes (Automatic Decline):**

The following convictions result in automatic decline regardless of timeframe:
- Fraud (any type)
- Embezzlement
- Money laundering
- Mortgage fraud
- Bank fraud
- Wire fraud
- Identity theft
- Securities fraud
- Tax evasion (felony)

**Other Felonies (Case-by-Case Review):**

| Conviction Type | Timeframe | Eligibility | Requirements |
|-----------------|-----------|-------------|--------------|
| Non-financial felony | < 7 years | Not eligible | Wait for 7-year seasoning |
| Non-financial felony | 7+ years | Eligible with review | Full disclosure, explanation |
| Multiple felonies | Any | Not eligible | Pattern of behavior concern |

**Misdemeanors:**
- Generally acceptable
- Full disclosure required
- Review for pattern of behavior
- DUI/DWI: acceptable if not pattern (3+ in 7 years = pattern)

**Required Documentation:**
- Court documents (conviction, sentencing)
- Proof of sentence completion
- Explanation letter from borrower
- Evidence of rehabilitation

### 4.7.3 Civil Litigation Review

**Active Litigation:**

| Litigation Type | Borrower Role | Eligibility | Notes |
|-----------------|---------------|-------------|-------|
| **Property-related** | Defendant | Not eligible | Cannot close with active litigation on subject property |
| **Financial dispute** | Defendant | Case-by-case | Review for potential judgment |
| **Business dispute** | Defendant | Eligible with review | Assess impact on deal |
| **Any type** | Plaintiff | Generally eligible | Assess distraction factor |

**Historical Litigation:**
- Litigation resolved > 2 years ago: Generally acceptable
- Multiple lawsuits: Review for pattern
- Judgments: See Section 4.5.4

**Required Documentation:**
- Court documents (complaint, answer, judgment)
- Settlement agreement (if applicable)
- Explanation of circumstances
- Current status update

### 4.7.4 OFAC and Sanctions Screening

**Office of Foreign Assets Control (OFAC):**

OFAC screening is mandatory for all borrowers and guarantors. Screening is conducted against:
- Specially Designated Nationals (SDN) List
- Consolidated Sanctions List
- Foreign Sanctions Evaders List
- Sectoral Sanctions Identifications List

**Screening Results:**

| Result | Action | Timeline |
|--------|--------|----------|
| **No Match** | Proceed with application | Immediate |
| **Potential Match** | Manual review required | 24-48 hours |
| **False Positive** | Clear with documentation | 48-72 hours |
| **Confirmed Match** | Decline immediately | Immediate |

**False Positive Resolution:**
- Common with common names (e.g., "John Smith")
- Requires additional documentation:
  - Full legal name with middle name
  - Date of birth
  - Social Security Number
  - Current address
  - Passport or government ID
- Documented clearance required in file

**Confirmed Match:**
- Application declined immediately
- No exceptions possible (regulatory requirement)
- Funds returned if already collected
- Cannot proceed under any circumstances

### 4.7.5 Sex Offender and Terrorist Watch Lists

**Sex Offender Registry:**
- Screening against national and state registries
- Match results in automatic decline
- No exceptions

**Terrorist Watch List:**
- Screening against FBI Terrorist Screening Database
- Match results in automatic decline
- No exceptions (regulatory requirement)

---

## 4.8 Flag Generation Rules for INSPIRE Phase 7

This section provides explicit flag generation rules for INSPIRE's automated credit and background analysis.

### 4.8.1 Credit Report Flags

| Check | Pass (Green) | Warning (Yellow) | Fail (Red) |
|-------|--------------|------------------|------------|
| **Report Currency** | ≤ 90 days | 91-120 days | > 120 days |
| **FICO Score (RTL)** | ≥ 680 | 660-679 | < 660 |
| **FICO Score (DSCR)** | ≥ 700 | 680-699 | < 680 |
| **Total Trade Lines** | ≥ 4 | 3 | < 3 |
| **Active Trade Lines** | ≥ 2 | 1 | 0 |
| **24-Month History** | ≥ 2 trade lines | 1 trade line | 0 trade lines |
| **Housing Lates (12mo)** | 0x30 | 1x30 | ≥ 2x30 or 1x60+ |
| **Housing Lates (24mo)** | 0x30 | 1-2x30 | 1x60+ |
| **Bankruptcy** | None or > 4 years | N/A | < 4 years |
| **Foreclosure** | None or > 4 years | N/A | < 4 years |
| **Judgments** | None or paid | < $5,000 unpaid | ≥ $5,000 unpaid |
| **Tax Liens** | None or paid | Payment plan (12+ mo) | Unpaid, no plan |
| **Collections** | < $2,000 or paid | $2,000-$5,000 | > $5,000 unpaid |
| **Credit Inquiries (6mo)** | ≤ 3 | 4-6 | > 6 |

### 4.8.2 Background Check Flags

| Check | Pass (Green) | Warning (Yellow) | Fail (Red) |
|-------|--------------|------------------|------------|
| **Report Currency** | ≤ 90 days | 91-120 days | > 120 days |
| **Criminal - Financial** | None | N/A | Any conviction |
| **Criminal - Other Felony** | None or > 7 years | N/A | < 7 years |
| **Criminal - Misdemeanor** | None or > 3 years | 1-3 years ago | Multiple recent |
| **OFAC Screening** | No match | Potential match (cleared) | Confirmed match |
| **Active Litigation** | None | Plaintiff | Defendant (property) |
| **Sex Offender** | No match | N/A | Match |
| **Terrorist Watch** | No match | N/A | Match |

### 4.8.3 Flag Priority and Escalation

**Red Flags:**
- Require immediate underwriter review
- May require exception approval
- Some red flags are automatic decline (OFAC, financial crimes)

**Yellow Flags:**
- Require underwriter review
- May require explanation from borrower
- Generally acceptable with documentation

**Green Flags:**
- No action required
- Standard processing

**Multiple Flags:**
- Multiple yellow flags may escalate to red flag status
- Underwriter discretion on overall risk assessment
- Document rationale for approval with multiple flags

---

## 4.9 Python Implementation

### 4.9.1 Credit Analysis Module

```python
"""
Credit Analysis Module
Analyzes credit reports and generates flags for INSPIRE Phase 7.
"""

from dataclasses import dataclass
from datetime import date, datetime, timedelta
from enum import Enum
from typing import List, Optional, Dict, Tuple


class FlagType(Enum):
    """Analysis flag types"""
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    RED = "RED"


class FlagCategory(Enum):
    """Flag categories"""
    CREDIT_REPORT = "CREDIT_REPORT"
    BACKGROUND_CHECK = "BACKGROUND_CHECK"
    TRADE_LINES = "TRADE_LINES"
    PAYMENT_HISTORY = "PAYMENT_HISTORY"
    DEROGATORY = "DEROGATORY"


@dataclass
class AnalysisFlag:
    """Individual analysis flag"""
    category: FlagCategory
    flag_type: FlagType
    check_name: str
    message: str
    value: any
    threshold: any = None
    
    def __str__(self):
        return f"[{self.flag_type.value}] {self.check_name}: {self.message}"


@dataclass
class CreditScores:
    """Credit scores from tri-merge report"""
    equifax: Optional[int] = None
    experian: Optional[int] = None
    transunion: Optional[int] = None
    representative_score: Optional[int] = None
    
    def __post_init__(self):
        """Calculate representative score"""
        scores = [s for s in [self.equifax, self.experian, self.transunion] if s is not None]
        
        if len(scores) == 0:
            self.representative_score = None
        elif len(scores) == 1:
            self.representative_score = scores[0]
        elif len(scores) == 2:
            self.representative_score = min(scores)
        else:  # 3 scores
            self.representative_score = sorted(scores)[1]  # Middle score


@dataclass
class TradeLine:
    """Individual trade line from credit report"""
    account_type: str  # REVOLVING, INSTALLMENT, MORTGAGE
    creditor_name: str
    account_number: str
    date_opened: date
    current_balance: float
    high_balance: float
    credit_limit: Optional[float] = None  # For revolving accounts
    original_amount: Optional[float] = None  # For installment accounts
    monthly_payment: float = 0.0
    status: str = "CURRENT"  # CURRENT, 30, 60, 90, 120, CHARGEOFF, COLLECTION
    is_closed: bool = False
    is_authorized_user: bool = False
    payment_history_24mo: List[str] = None  # List of payment statuses
    
    def __post_init__(self):
        if self.payment_history_24mo is None:
            self.payment_history_24mo = []
    
    @property
    def age_months(self) -> int:
        """Calculate account age in months"""
        today = date.today()
        return (today.year - self.date_opened.year) * 12 + (today.month - self.date_opened.month)
    
    @property
    def utilization(self) -> Optional[float]:
        """Calculate credit utilization for revolving accounts"""
        if self.account_type == "REVOLVING" and self.credit_limit and self.credit_limit > 0:
            return self.current_balance / self.credit_limit
        return None
    
    def count_lates(self, months: int = 12) -> Dict[str, int]:
        """Count late payments in recent history"""
        recent_history = self.payment_history_24mo[-months:] if self.payment_history_24mo else []
        return {
            "30": recent_history.count("30"),
            "60": recent_history.count("60"),
            "90": recent_history.count("90"),
            "120": recent_history.count("120+")
        }


@dataclass
class DerogatoryEvent:
    """Derogatory credit event"""
    event_type: str  # BANKRUPTCY_CH7, BANKRUPTCY_CH13, FORECLOSURE, SHORT_SALE, JUDGMENT, LIEN, COLLECTION
    date_filed: Optional[date] = None
    date_discharged: Optional[date] = None
    date_satisfied: Optional[date] = None
    amount: float = 0.0
    status: str = "OPEN"  # OPEN, DISCHARGED, SATISFIED, DISMISSED
    description: str = ""
    
    @property
    def years_since_discharge(self) -> Optional[float]:
        """Calculate years since discharge/completion"""
        if self.date_discharged:
            return (date.today() - self.date_discharged).days / 365.25
        return None
    
    @property
    def years_since_filing(self) -> Optional[float]:
        """Calculate years since filing"""
        if self.date_filed:
            return (date.today() - self.date_filed).days / 365.25
        return None


@dataclass
class CreditReport:
    """Complete credit report data"""
    report_date: date
    borrower_name: str
    scores: CreditScores
    trade_lines: List[TradeLine]
    derogatory_events: List[DerogatoryEvent]
    inquiries_6mo: int = 0
    public_records: List[Dict] = None
    
    def __post_init__(self):
        if self.public_records is None:
            self.public_records = []
    
    @property
    def age_days(self) -> int:
        """Calculate report age in days"""
        return (date.today() - self.report_date).days
    
    @property
    def active_trade_lines(self) -> List[TradeLine]:
        """Get list of active (open) trade lines"""
        return [tl for tl in self.trade_lines if not tl.is_closed]
    
    @property
    def primary_trade_lines(self) -> List[TradeLine]:
        """Get list of primary (non-authorized-user) trade lines"""
        return [tl for tl in self.trade_lines if not tl.is_authorized_user]
    
    @property
    def mortgage_trade_lines(self) -> List[TradeLine]:
        """Get list of mortgage trade lines"""
        return [tl for tl in self.trade_lines if tl.account_type == "MORTGAGE"]


class CreditAnalyzer:
    """
    Analyze credit reports and generate flags for INSPIRE Phase 7.
    """
    
    # FICO thresholds
    MIN_FICO_RTL = 660
    MIN_FICO_DSCR = 680
    PREFERRED_FICO_RTL = 680
    PREFERRED_FICO_DSCR = 700
    
    # Trade line requirements
    MIN_TOTAL_TRADE_LINES = 3
    MIN_ACTIVE_TRADE_LINES = 1
    MIN_24MO_HISTORY_LINES = 1
    PREFERRED_TOTAL_TRADE_LINES = 4
    PREFERRED_ACTIVE_TRADE_LINES = 2
    PREFERRED_24MO_HISTORY_LINES = 2
    
    # Derogatory seasoning requirements (years)
    BANKRUPTCY_CH7_SEASONING = 4.0
    BANKRUPTCY_CH13_SEASONING_DISCHARGE = 2.0
    BANKRUPTCY_CH13_SEASONING_FILING = 4.0
    FORECLOSURE_SEASONING = 4.0
    SHORT_SALE_SEASONING = 4.0
    
    # Collection and judgment thresholds
    COLLECTION_MINOR_THRESHOLD = 2000.0
    COLLECTION_MAJOR_THRESHOLD = 5000.0
    JUDGMENT_MINOR_THRESHOLD = 5000.0
    JUDGMENT_MAJOR_THRESHOLD = 10000.0
    
    def check_report_currency(self, report: CreditReport) -> AnalysisFlag:
        """
        Check if credit report is within acceptable age.
        
        Args:
            report: Credit report to check
            
        Returns:
            AnalysisFlag with currency status
        """
        age_days = report.age_days
        
        if age_days <= 90:
            return AnalysisFlag(
                category=FlagCategory.CREDIT_REPORT,
                flag_type=FlagType.GREEN,
                check_name="Report Currency",
                message=f"Report is {age_days} days old (within 90 days)",
                value=age_days,
                threshold=90
            )
        elif age_days <= 120:
            return AnalysisFlag(
                category=FlagCategory.CREDIT_REPORT,
                flag_type=FlagType.YELLOW,
                check_name="Report Currency",
                message=f"Report is {age_days} days old (acceptable but aging)",
                value=age_days,
                threshold=120
            )
        else:
            return AnalysisFlag(
                category=FlagCategory.CREDIT_REPORT,
                flag_type=FlagType.RED,
                check_name="Report Currency",
                message=f"Report is {age_days} days old (exceeds 120-day maximum)",
                value=age_days,
                threshold=120
            )
    
    def check_fico_score(self, report: CreditReport, loan_type: str) -> AnalysisFlag:
        """
        Check if FICO score meets minimum requirements.
        
        Args:
            report: Credit report with scores
            loan_type: 'RTL' or 'DSCR'
            
        Returns:
            AnalysisFlag with FICO status
        """
        fico = report.scores.representative_score
        
        if fico is None:
            return AnalysisFlag(
                category=FlagCategory.CREDIT_REPORT,
                flag_type=FlagType.RED,
                check_name="FICO Score",
                message="No credit score available",
                value=None,
                threshold=self.MIN_FICO_RTL if loan_type == 'RTL' else self.MIN_FICO_DSCR
            )
        
        min_fico = self.MIN_FICO_RTL if loan_type == 'RTL' else self.MIN_FICO_DSCR
        preferred_fico = self.PREFERRED_FICO_RTL if loan_type == 'RTL' else self.PREFERRED_FICO_DSCR
        
        if fico >= preferred_fico:
            return AnalysisFlag(
                category=FlagCategory.CREDIT_REPORT,
                flag_type=FlagType.GREEN,
                check_name="FICO Score",
                message=f"FICO {fico} meets preferred threshold",
                value=fico,
                threshold=preferred_fico
            )
        elif fico >= min_fico:
            return AnalysisFlag(
                category=FlagCategory.CREDIT_REPORT,
                flag_type=FlagType.YELLOW,
                check_name="FICO Score",
                message=f"FICO {fico} meets minimum but below preferred",
                value=fico,
                threshold=min_fico
            )
        else:
            return AnalysisFlag(
                category=FlagCategory.CREDIT_REPORT,
                flag_type=FlagType.RED,
                check_name="FICO Score",
                message=f"FICO {fico} below minimum requirement of {min_fico}",
                value=fico,
                threshold=min_fico
            )
    
    def check_trade_lines(self, report: CreditReport) -> List[AnalysisFlag]:
        """
        Check if trade line requirements are met.
        
        Args:
            report: Credit report with trade lines
            
        Returns:
            List of AnalysisFlags for trade line checks
        """
        flags = []
        
        # Check total trade lines (primary only)
        primary_tls = report.primary_trade_lines
        total_count = len(primary_tls)
        
        if total_count >= self.PREFERRED_TOTAL_TRADE_LINES:
            flags.append(AnalysisFlag(
                category=FlagCategory.TRADE_LINES,
                flag_type=FlagType.GREEN,
                check_name="Total Trade Lines",
                message=f"{total_count} primary trade lines (preferred)",
                value=total_count,
                threshold=self.PREFERRED_TOTAL_TRADE_LINES
            ))
        elif total_count >= self.MIN_TOTAL_TRADE_LINES:
            flags.append(AnalysisFlag(
                category=FlagCategory.TRADE_LINES,
                flag_type=FlagType.YELLOW,
                check_name="Total Trade Lines",
                message=f"{total_count} primary trade lines (meets minimum)",
                value=total_count,
                threshold=self.MIN_TOTAL_TRADE_LINES
            ))
        else:
            flags.append(AnalysisFlag(
                category=FlagCategory.TRADE_LINES,
                flag_type=FlagType.RED,
                check_name="Total Trade Lines",
                message=f"{total_count} primary trade lines (below minimum of {self.MIN_TOTAL_TRADE_LINES})",
                value=total_count,
                threshold=self.MIN_TOTAL_TRADE_LINES
            ))
        
        # Check active trade lines
        active_tls = [tl for tl in primary_tls if not tl.is_closed]
        active_count = len(active_tls)
        
        if active_count >= self.PREFERRED_ACTIVE_TRADE_LINES:
            flags.append(AnalysisFlag(
                category=FlagCategory.TRADE_LINES,
                flag_type=FlagType.GREEN,
                check_name="Active Trade Lines",
                message=f"{active_count} active trade lines (preferred)",
                value=active_count,
                threshold=self.PREFERRED_ACTIVE_TRADE_LINES
            ))
        elif active_count >= self.MIN_ACTIVE_TRADE_LINES:
            flags.append(AnalysisFlag(
                category=FlagCategory.TRADE_LINES,
                flag_type=FlagType.YELLOW,
                check_name="Active Trade Lines",
                message=f"{active_count} active trade lines (meets minimum)",
                value=active_count,
                threshold=self.MIN_ACTIVE_TRADE_LINES
            ))
        else:
            flags.append(AnalysisFlag(
                category=FlagCategory.TRADE_LINES,
                flag_type=FlagType.RED,
                check_name="Active Trade Lines",
                message=f"{active_count} active trade lines (below minimum)",
                value=active_count,
                threshold=self.MIN_ACTIVE_TRADE_LINES
            ))
        
        # Check 24-month history
        history_tls = [tl for tl in primary_tls if tl.age_months >= 24]
        history_count = len(history_tls)
        
        if history_count >= self.PREFERRED_24MO_HISTORY_LINES:
            flags.append(AnalysisFlag(
                category=FlagCategory.TRADE_LINES,
                flag_type=FlagType.GREEN,
                check_name="24-Month History",
                message=f"{history_count} trade lines with 24+ month history (preferred)",
                value=history_count,
                threshold=self.PREFERRED_24MO_HISTORY_LINES
            ))
        elif history_count >= self.MIN_24MO_HISTORY_LINES:
            flags.append(AnalysisFlag(
                category=FlagCategory.TRADE_LINES,
                flag_type=FlagType.YELLOW,
                check_name="24-Month History",
                message=f"{history_count} trade lines with 24+ month history (meets minimum)",
                value=history_count,
                threshold=self.MIN_24MO_HISTORY_LINES
            ))
        else:
            flags.append(AnalysisFlag(
                category=FlagCategory.TRADE_LINES,
                flag_type=FlagType.RED,
                check_name="24-Month History",
                message=f"{history_count} trade lines with 24+ month history (below minimum)",
                value=history_count,
                threshold=self.MIN_24MO_HISTORY_LINES
            ))
        
        return flags
    
    def check_mortgage_history(self, report: CreditReport, loan_type: str) -> AnalysisFlag:
        """
        Check mortgage payment history for late payments.
        
        Args:
            report: Credit report with trade lines
            loan_type: 'RTL' or 'DSCR'
            
        Returns:
            AnalysisFlag for mortgage payment history
        """
        mortgage_tls = report.mortgage_trade_lines
        
        if not mortgage_tls:
            return AnalysisFlag(
                category=FlagCategory.PAYMENT_HISTORY,
                flag_type=FlagType.GREEN,
                check_name="Mortgage History",
                message="No mortgage history (not required)",
                value="N/A"
            )
        
        # Analyze last 12 months
        max_late_12mo = 0
        for tl in mortgage_tls:
            lates = tl.count_lates(12)
            if lates["120"]:
                max_late_12mo = max(max_late_12mo, 120)
            elif lates["90"]:
                max_late_12mo = max(max_late_12mo, 90)
            elif lates["60"]:
                max_late_12mo = max(max_late_12mo, 60)
            elif lates["30"]:
                max_late_12mo = max(max_late_12mo, 30)
        
        # Apply standards based on loan type
        if loan_type == 'RTL':
            if max_late_12mo == 0:
                return AnalysisFlag(
                    category=FlagCategory.PAYMENT_HISTORY,
                    flag_type=FlagType.GREEN,
                    check_name="Mortgage History (12mo)",
                    message="0x30 in last 12 months (preferred)",
                    value="0x30"
                )
            elif max_late_12mo == 30:
                return AnalysisFlag(
                    category=FlagCategory.PAYMENT_HISTORY,
                    flag_type=FlagType.YELLOW,
                    check_name="Mortgage History (12mo)",
                    message="1x30 in last 12 months (acceptable with review)",
                    value="1x30"
                )
            else:
                return AnalysisFlag(
                    category=FlagCategory.PAYMENT_HISTORY,
                    flag_type=FlagType.RED,
                    check_name="Mortgage History (12mo)",
                    message=f"Late payments exceed acceptable threshold (max {max_late_12mo} days)",
                    value=f"{max_late_12mo}+ days late"
                )
        else:  # DSCR
            if max_late_12mo == 0:
                return AnalysisFlag(
                    category=FlagCategory.PAYMENT_HISTORY,
                    flag_type=FlagType.GREEN,
                    check_name="Mortgage History (12mo)",
                    message="0x30 in last 12 months (preferred)",
                    value="0x30"
                )
            elif max_late_12mo == 30:
                return AnalysisFlag(
                    category=FlagCategory.PAYMENT_HISTORY,
                    flag_type=FlagType.GREEN,
                    check_name="Mortgage History (12mo)",
                    message="1x30 in last 12 months (acceptable)",
                    value="1x30"
                )
            elif max_late_12mo < 60:
                return AnalysisFlag(
                    category=FlagCategory.PAYMENT_HISTORY,
                    flag_type=FlagType.YELLOW,
                    check_name="Mortgage History (12mo)",
                    message="2x30 in last 12 months (acceptable with review)",
                    value="2x30"
                )
            else:
                return AnalysisFlag(
                    category=FlagCategory.PAYMENT_HISTORY,
                    flag_type=FlagType.RED,
                    check_name="Mortgage History (12mo)",
                    message=f"Late payments exceed acceptable threshold",
                    value=f"{max_late_12mo}+ days late"
                )
    
    def check_derogatory_events(self, report: CreditReport) -> List[AnalysisFlag]:
        """
        Check for derogatory credit events and seasoning.
        
        Args:
            report: Credit report with derogatory events
            
        Returns:
            List of AnalysisFlags for derogatory events
        """
        flags = []
        
        for event in report.derogatory_events:
            if event.event_type == "BANKRUPTCY_CH7":
                years_since = event.years_since_discharge
                if years_since is None:
                    flags.append(AnalysisFlag(
                        category=FlagCategory.DEROGATORY,
                        flag_type=FlagType.RED,
                        check_name="Bankruptcy Chapter 7",
                        message="Chapter 7 bankruptcy not discharged",
                        value="Not discharged"
                    ))
                elif years_since >= self.BANKRUPTCY_CH7_SEASONING:
                    flags.append(AnalysisFlag(
                        category=FlagCategory.DEROGATORY,
                        flag_type=FlagType.GREEN,
                        check_name="Bankruptcy Chapter 7",
                        message=f"Chapter 7 discharged {years_since:.1f} years ago (meets seasoning)",
                        value=f"{years_since:.1f} years",
                        threshold=self.BANKRUPTCY_CH7_SEASONING
                    ))
                else:
                    flags.append(AnalysisFlag(
                        category=FlagCategory.DEROGATORY,
                        flag_type=FlagType.RED,
                        check_name="Bankruptcy Chapter 7",
                        message=f"Chapter 7 discharged {years_since:.1f} years ago (requires {self.BANKRUPTCY_CH7_SEASONING} years)",
                        value=f"{years_since:.1f} years",
                        threshold=self.BANKRUPTCY_CH7_SEASONING
                    ))
            
            elif event.event_type == "FORECLOSURE":
                years_since = event.years_since_discharge or event.years_since_filing
                if years_since is None:
                    flags.append(AnalysisFlag(
                        category=FlagCategory.DEROGATORY,
                        flag_type=FlagType.RED,
                        check_name="Foreclosure",
                        message="Foreclosure date unknown",
                        value="Unknown"
                    ))
                elif years_since >= self.FORECLOSURE_SEASONING:
                    flags.append(AnalysisFlag(
                        category=FlagCategory.DEROGATORY,
                        flag_type=FlagType.GREEN,
                        check_name="Foreclosure",
                        message=f"Foreclosure {years_since:.1f} years ago (meets seasoning)",
                        value=f"{years_since:.1f} years",
                        threshold=self.FORECLOSURE_SEASONING
                    ))
                else:
                    flags.append(AnalysisFlag(
                        category=FlagCategory.DEROGATORY,
                        flag_type=FlagType.RED,
                        check_name="Foreclosure",
                        message=f"Foreclosure {years_since:.1f} years ago (requires {self.FORECLOSURE_SEASONING} years)",
                        value=f"{years_since:.1f} years",
                        threshold=self.FORECLOSURE_SEASONING
                    ))
            
            elif event.event_type == "JUDGMENT":
                if event.status == "SATISFIED":
                    flags.append(AnalysisFlag(
                        category=FlagCategory.DEROGATORY,
                        flag_type=FlagType.GREEN,
                        check_name="Judgment",
                        message=f"Judgment satisfied (${event.amount:,.0f})",
                        value="Satisfied"
                    ))
                elif event.amount < self.JUDGMENT_MINOR_THRESHOLD:
                    flags.append(AnalysisFlag(
                        category=FlagCategory.DEROGATORY,
                        flag_type=FlagType.YELLOW,
                        check_name="Judgment",
                        message=f"Unpaid judgment ${event.amount:,.0f} (below ${self.JUDGMENT_MINOR_THRESHOLD:,.0f} threshold)",
                        value=event.amount,
                        threshold=self.JUDGMENT_MINOR_THRESHOLD
                    ))
                elif event.amount < self.JUDGMENT_MAJOR_THRESHOLD:
                    flags.append(AnalysisFlag(
                        category=FlagCategory.DEROGATORY,
                        flag_type=FlagType.YELLOW,
                        check_name="Judgment",
                        message=f"Unpaid judgment ${event.amount:,.0f} (requires payment plan)",
                        value=event.amount,
                        threshold=self.JUDGMENT_MAJOR_THRESHOLD
                    ))
                else:
                    flags.append(AnalysisFlag(
                        category=FlagCategory.DEROGATORY,
                        flag_type=FlagType.RED,
                        check_name="Judgment",
                        message=f"Unpaid judgment ${event.amount:,.0f} (exceeds ${self.JUDGMENT_MAJOR_THRESHOLD:,.0f} threshold)",
                        value=event.amount,
                        threshold=self.JUDGMENT_MAJOR_THRESHOLD
                    ))
            
            elif event.event_type == "COLLECTION":
                if event.status == "PAID":
                    flags.append(AnalysisFlag(
                        category=FlagCategory.DEROGATORY,
                        flag_type=FlagType.GREEN,
                        check_name="Collection",
                        message=f"Collection paid (${event.amount:,.0f})",
                        value="Paid"
                    ))
                elif "MEDICAL" in event.description.upper():
                    flags.append(AnalysisFlag(
                        category=FlagCategory.DEROGATORY,
                        flag_type=FlagType.GREEN,
                        check_name="Collection",
                        message=f"Medical collection ${event.amount:,.0f} (disregarded)",
                        value="Medical"
                    ))
                elif event.amount < self.COLLECTION_MINOR_THRESHOLD:
                    flags.append(AnalysisFlag(
                        category=FlagCategory.DEROGATORY,
                        flag_type=FlagType.GREEN,
                        check_name="Collection",
                        message=f"Collection ${event.amount:,.0f} (below threshold)",
                        value=event.amount,
                        threshold=self.COLLECTION_MINOR_THRESHOLD
                    ))
                elif event.amount < self.COLLECTION_MAJOR_THRESHOLD:
                    flags.append(AnalysisFlag(
                        category=FlagCategory.DEROGATORY,
                        flag_type=FlagType.YELLOW,
                        check_name="Collection",
                        message=f"Collection ${event.amount:,.0f} (requires explanation)",
                        value=event.amount,
                        threshold=self.COLLECTION_MAJOR_THRESHOLD
                    ))
                else:
                    flags.append(AnalysisFlag(
                        category=FlagCategory.DEROGATORY,
                        flag_type=FlagType.RED,
                        check_name="Collection",
                        message=f"Collection ${event.amount:,.0f} (exceeds threshold, requires payment)",
                        value=event.amount,
                        threshold=self.COLLECTION_MAJOR_THRESHOLD
                    ))
        
        return flags
    
    def generate_all_flags(self, report: CreditReport, loan_type: str) -> List[AnalysisFlag]:
        """
        Generate all credit analysis flags for a report.
        
        Args:
            report: Complete credit report
            loan_type: 'RTL' or 'DSCR'
            
        Returns:
            List of all AnalysisFlags
        """
        flags = []
        
        # Report currency
        flags.append(self.check_report_currency(report))
        
        # FICO score
        flags.append(self.check_fico_score(report, loan_type))
        
        # Trade lines
        flags.extend(self.check_trade_lines(report))
        
        # Mortgage history
        flags.append(self.check_mortgage_history(report, loan_type))
        
        # Derogatory events
        flags.extend(self.check_derogatory_events(report))
        
        return flags


class BackgroundChecker:
    """
    Analyze background check results and generate flags.
    """
    
    FELONY_SEASONING_YEARS = 7.0
    MISDEMEANOR_SEASONING_YEARS = 3.0
    
    def check_criminal_history(
        self, 
        convictions: List[Dict]
    ) -> List[AnalysisFlag]:
        """
        Check criminal history for disqualifying convictions.
        
        Args:
            convictions: List of conviction records with type, date, description
            
        Returns:
            List of AnalysisFlags
        """
        flags = []
        
        if not convictions:
            flags.append(AnalysisFlag(
                category=FlagCategory.BACKGROUND_CHECK,
                flag_type=FlagType.GREEN,
                check_name="Criminal History",
                message="No criminal convictions found",
                value="None"
            ))
            return flags
        
        for conviction in convictions:
            conviction_type = conviction.get("type", "").upper()
            conviction_date = conviction.get("date")
            description = conviction.get("description", "")
            
            # Check for financial crimes (automatic decline)
            financial_crimes = ["FRAUD", "EMBEZZLEMENT", "MONEY LAUNDERING", 
                              "MORTGAGE FRAUD", "IDENTITY THEFT", "SECURITIES"]
            if any(crime in description.upper() for crime in financial_crimes):
                flags.append(AnalysisFlag(
                    category=FlagCategory.BACKGROUND_CHECK,
                    flag_type=FlagType.RED,
                    check_name="Criminal History",
                    message=f"Financial crime conviction: {description}",
                    value="Financial Crime"
                ))
                continue
            
            # Check felony seasoning
            if "FELONY" in conviction_type:
                if conviction_date:
                    years_since = (date.today() - conviction_date).days / 365.25
                    if years_since >= self.FELONY_SEASONING_YEARS:
                        flags.append(AnalysisFlag(
                            category=FlagCategory.BACKGROUND_CHECK,
                            flag_type=FlagType.YELLOW,
                            check_name="Criminal History",
                            message=f"Felony conviction {years_since:.1f} years ago (meets seasoning)",
                            value=f"{years_since:.1f} years",
                            threshold=self.FELONY_SEASONING_YEARS
                        ))
                    else:
                        flags.append(AnalysisFlag(
                            category=FlagCategory.BACKGROUND_CHECK,
                            flag_type=FlagType.RED,
                            check_name="Criminal History",
                            message=f"Felony conviction {years_since:.1f} years ago (requires {self.FELONY_SEASONING_YEARS} years)",
                            value=f"{years_since:.1f} years",
                            threshold=self.FELONY_SEASONING_YEARS
                        ))
            
            # Misdemeanors generally acceptable
            elif "MISDEMEANOR" in conviction_type:
                if conviction_date:
                    years_since = (date.today() - conviction_date).days / 365.25
                    if years_since >= self.MISDEMEANOR_SEASONING_YEARS:
                        flags.append(AnalysisFlag(
                            category=FlagCategory.BACKGROUND_CHECK,
                            flag_type=FlagType.GREEN,
                            check_name="Criminal History",
                            message=f"Misdemeanor conviction {years_since:.1f} years ago (acceptable)",
                            value=f"{years_since:.1f} years"
                        ))
                    else:
                        flags.append(AnalysisFlag(
                            category=FlagCategory.BACKGROUND_CHECK,
                            flag_type=FlagType.YELLOW,
                            check_name="Criminal History",
                            message=f"Recent misdemeanor conviction {years_since:.1f} years ago",
                            value=f"{years_since:.1f} years"
                        ))
        
        return flags
    
    def check_ofac(self, ofac_result: str) -> AnalysisFlag:
        """
        Check OFAC screening result.
        
        Args:
            ofac_result: 'NO_MATCH', 'POTENTIAL_MATCH', or 'CONFIRMED_MATCH'
            
        Returns:
            AnalysisFlag for OFAC screening
        """
        if ofac_result == "NO_MATCH":
            return AnalysisFlag(
                category=FlagCategory.BACKGROUND_CHECK,
                flag_type=FlagType.GREEN,
                check_name="OFAC Screening",
                message="No OFAC match found",
                value="Clear"
            )
        elif ofac_result == "POTENTIAL_MATCH":
            return AnalysisFlag(
                category=FlagCategory.BACKGROUND_CHECK,
                flag_type=FlagType.YELLOW,
                check_name="OFAC Screening",
                message="Potential OFAC match (requires manual review)",
                value="Potential Match"
            )
        else:  # CONFIRMED_MATCH
            return AnalysisFlag(
                category=FlagCategory.BACKGROUND_CHECK,
                flag_type=FlagType.RED,
                check_name="OFAC Screening",
                message="CONFIRMED OFAC MATCH - NOT ELIGIBLE",
                value="Confirmed Match"
            )


# Example usage
if __name__ == "__main__":
    # Example credit report
    scores = CreditScores(
        equifax=720,
        experian=705,
        transunion=715
    )
    
    trade_lines = [
        TradeLine(
            account_type="REVOLVING",
            creditor_name="Chase Credit Card",
            account_number="****1234",
            date_opened=date(2018, 1, 1),
            current_balance=2500.0,
            high_balance=5000.0,
            credit_limit=10000.0,
            monthly_payment=100.0,
            status="CURRENT"
        ),
        TradeLine(
            account_type="MORTGAGE",
            creditor_name="Wells Fargo Mortgage",
            account_number="****5678",
            date_opened=date(2019, 6, 1),
            current_balance=250000.0,
            high_balance=280000.0,
            original_amount=280000.0,
            monthly_payment=1800.0,
            status="CURRENT",
            payment_history_24mo=["CURRENT"] * 24
        )
    ]
    
    derogatory_events = [
        DerogatoryEvent(
            event_type="COLLECTION",
            amount=1500.0,
            status="PAID",
            description="Medical collection"
        )
    ]
    
    report = CreditReport(
        report_date=date(2024, 12, 1),
        borrower_name="John Smith",
        scores=scores,
        trade_lines=trade_lines,
        derogatory_events=derogatory_events,
        inquiries_6mo=2
    )
    
    # Analyze report
    analyzer = CreditAnalyzer()
    flags = analyzer.generate_all_flags(report, 'RTL')
    
    print("Credit Analysis Flags:")
    print("=" * 60)
    for flag in flags:
        print(flag)
```

---

## 4.10 Cross-References

**Related Sections:**
- **Section 2**: Borrower Eligibility & Classification - FICO requirements and citizenship considerations
- **Section 3**: Entity & Guarantor Analysis - Guarantor requirements and ownership structure
- **Section 12**: Exception Management - Credit exception process and compensating factors
- **Section 14**: Third-Party Report Analysis - Complete report analysis framework
- **Section 15**: Credit Memo & Risk Assessment - Integration of credit analysis into credit memo

---

*End of Section 4*

