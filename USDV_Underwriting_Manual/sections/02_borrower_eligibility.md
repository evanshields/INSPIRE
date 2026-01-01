---
section: 2
title: Borrower Eligibility & Classification
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

# Section 2: Borrower Eligibility & Classification

## 2.1 Overview

Borrower eligibility and classification form the foundation of USDV's underwriting framework. This section defines the standards for evaluating borrower qualifications, including credit requirements, experience verification, citizenship status, and the classification system that determines leverage limits for RTL products.

**INSPIRE Integration Points:**
- Phase 1-2: Borrower data collection and validation during Quick App and Full Application
- Phase 3-4: Classification calculation for RTL loan sizing
- Phase 7: Borrower analysis for credit memo generation

---

## 2.2 Borrower Classification Framework (RTL Products)

### 2.2.1 Classification Overview

For RTL products (Fix & Flip, Ground-Up Construction, Bridge), borrowers are classified into four tiers (A+, A, B, C) based on credit strength and verified experience. This classification directly determines maximum leverage limits as detailed in Section 9.

**Classification determines:**
- Maximum As-Is LTV
- Maximum Loan-to-Cost (LTC)
- Maximum Loan-to-ARV (LTARV)
- Leverage reduction severity for heavy rehab projects

### 2.2.2 Credit Decision Score

The Credit Decision Score evaluates borrower creditworthiness based on FICO score and citizenship status.

| FICO Range | Score | Notes |
|------------|-------|-------|
| ≥ 700 | 3 points | Strong credit profile |
| 680-699 | 1 point | Acceptable credit |
| < 680 | 0 points | Below standard threshold |
| Foreign National | 0 points | Regardless of FICO score |

**FICO Score Determination Rules:**
- For individual borrowers: Use middle score from tri-merge credit report
- For multiple guarantors: Use the FICO of the guarantor with the highest ownership percentage
- If equal ownership: Use the lesser qualifying FICO score
- Minimum FICO requirement: 660 for all guarantors on RTL loans

**Example 1: Single Guarantor**
```
Guarantor A: 100% ownership, FICO 720
Credit Decision Score = 3 points
```

**Example 2: Multiple Guarantors - Unequal Ownership**
```
Guarantor A: 60% ownership, FICO 685
Guarantor B: 40% ownership, FICO 740
Credit Decision Score = 1 point (based on Guarantor A's 60% ownership)
```

**Example 3: Multiple Guarantors - Equal Ownership**
```
Guarantor A: 50% ownership, FICO 710
Guarantor B: 50% ownership, FICO 695
Credit Decision Score = 1 point (lesser of the two qualifying scores)
```

### 2.2.3 Verified Experience Score

The Verified Experience Score measures the borrower's track record of successfully completing real estate transactions within the past 36 months.

| Experience (36 months) | Score | Notes |
|------------------------|-------|-------|
| 10+ deals | 7 points | Highly experienced investor |
| 3-9 deals | 5 points | Experienced investor |
| 0-2 deals | 1 point | Limited or first-time investor |

**What Counts as Verified Experience:**

Eligible transactions include:
- Fix & Flip projects (purchase, renovation, sale)
- Ground-Up Construction projects
- BRRRR transactions (Buy, Rehab, Rent, Refinance, Repeat)
- Rental property acquisitions and dispositions
- Wholesale assignments (with documentation)

**Documentation Requirements:**
- HUD-1 Settlement Statements (closing documents)
- Warranty Deeds showing acquisition and disposition
- Before/after photos for renovation projects
- Property addresses and transaction dates
- Profit/loss statements (optional but recommended)

**Verification Standards:**
1. **36-Month Lookback Period**: Only deals closed within 36 months prior to application date count toward experience score
2. **Completed Transactions**: Both acquisition and disposition must be documented for flip projects
3. **Arm's Length Transactions**: Related-party transactions may not count unless fully documented
4. **Geographic Relevance**: Out-of-state experience counts, but local market experience is preferred
5. **Property Type Relevance**: Single-family experience is most relevant; multifamily experience may count

**Experience Calculation Example:**
```
Borrower completed the following deals in last 36 months:
- 5 Fix & Flip projects (documented with HUD-1s)
- 3 Rental property purchases (documented)
- 1 Wholesale assignment (documented)

Total Verified Experience = 9 deals
Verified Experience Score = 5 points
```

**Deals in Progress:**
- Deals not yet completed (no disposition) do not count toward experience
- Current deal being underwritten does not count toward experience
- Deals under contract but not closed do not count

### 2.2.4 Final Classification Determination

The borrower's final classification is determined by summing the Credit Decision Score and Verified Experience Score:

| Total Score | Classification | Leverage Profile |
|-------------|----------------|------------------|
| ≥ 7 points | **A+** | Maximum leverage available |
| 5-6 points | **A** | High leverage available |
| 2-4 points | **B** | Moderate leverage available |
| < 2 points | **C** | Conservative leverage only |

**Classification Examples:**

**Example 1: A+ Borrower**
```
FICO: 725 → Credit Decision Score = 3 points
Experience: 12 deals in 36 months → Experience Score = 7 points
Total Score = 10 points → Classification = A+
```

**Example 2: A Borrower**
```
FICO: 695 → Credit Decision Score = 1 point
Experience: 8 deals in 36 months → Experience Score = 5 points
Total Score = 6 points → Classification = A
```

**Example 3: B Borrower**
```
FICO: 710 → Credit Decision Score = 3 points
Experience: 2 deals in 36 months → Experience Score = 1 point
Total Score = 4 points → Classification = B
```

**Example 4: C Borrower**
```
FICO: 675 → Credit Decision Score = 0 points
Experience: 1 deal in 36 months → Experience Score = 1 point
Total Score = 1 point → Classification = C
```

**Example 5: Foreign National**
```
FICO: 750 (Foreign National) → Credit Decision Score = 0 points
Experience: 15 deals in 36 months → Experience Score = 7 points
Total Score = 7 points → Classification = A+
Note: Foreign nationals can achieve A+ but face additional requirements (see Section 2.5)
```

### 2.2.5 DSCR Product Classification

DSCR loans do not use the A+/A/B/C classification system. Instead, DSCR eligibility and pricing are determined by:
- FICO score tiers (see Section 2.3.2)
- DSCR ratio (see Section 7)
- Loan-to-Value (LTV) limits by FICO and purpose (see Section 10)
- Loan Level Price Adjustments (LLPAs) based on risk factors (see Section 11)

---

## 2.3 Minimum Eligibility Requirements

### 2.3.1 RTL Product Minimums

| Requirement | Minimum Standard | Notes |
|-------------|------------------|-------|
| **FICO Score** | 660 (all guarantors) | Middle score from tri-merge |
| **Experience** | 1 completed deal | Or strong compensating factors |
| **Liquidity** | 6 months PITIA | Post-close reserves |
| **Net Worth** | Equal to loan amount | Verified through financial statements |
| **Citizenship** | US Citizen, Permanent Resident, or Foreign National | See Section 2.5 |
| **Age** | 18+ years | Legal capacity to contract |

**First-Time Investor Exceptions:**
- Borrowers with 0 deals may be eligible with:
  - FICO ≥ 700
  - Strong liquidity (12+ months reserves)
  - Construction/real estate industry experience
  - Detailed business plan
  - Investor approval required

### 2.3.2 DSCR Product Minimums

| Requirement | Minimum Standard | Notes |
|-------------|------------------|-------|
| **FICO Score** | 660 (absolute minimum), 680 (standard) | FICO 660-679 eligible but with reduced leverage |
| **Experience** | None required | Income-based qualification |
| **Liquidity** | 6-12 months PITIA | Based on FICO and LTV |
| **Net Worth** | Varies by investor | Typically equal to loan amount |
| **DSCR Ratio** | 1.00x - 1.20x | Based on FICO and property type |
| **Citizenship** | US Citizen, Permanent Resident, or Foreign National | See Section 2.5 |

**DSCR FICO Tiers:**

| FICO Range | Tier | Base LTV (Purchase) | Min DSCR |
|------------|------|---------------------|----------|
| 720+ | Tier 1 | 80% | 1.00x |
| 700-719 | Tier 2 | 75-80% | 1.00x |
| 680-699 | Tier 3 | 75% | 1.20x |
| 660-679 | Tier 4 | 70% | 1.20x |

**Note:** While FICO 660 is the absolute minimum, borrowers with FICO 660-679 face significantly reduced leverage (70% max LTV purchase) compared to higher FICO tiers. FICO 680+ is considered the standard minimum for competitive leverage.

**Reserve Requirements by FICO:**

| FICO | LTV ≤ 75% | LTV > 75% |
|------|-----------|-----------|
| 720+ | 6 months | 9 months |
| 700-719 | 6 months | 12 months |
| 680-699 | 9 months | 12 months |

---

## 2.4 Experience Requirements and Documentation

### 2.4.1 Experience Verification Process

**Step 1: Borrower Self-Reporting**
- Borrower completes experience questionnaire in INSPIRE application
- Lists all deals completed in last 36 months
- Provides property addresses, dates, and transaction types

**Step 2: Documentation Collection**
- HUD-1 Settlement Statements for each transaction
- Warranty Deeds (acquisition and disposition)
- Before/after photos for renovation projects
- Profit/loss statements (if available)

**Step 3: USDV Verification**
- Review all submitted documentation
- Verify transaction dates fall within 36-month window
- Confirm borrower/entity name matches on documents
- Validate property addresses and transaction types
- Calculate verified experience score

**Step 4: Experience Confirmation**
- Document verified experience in loan file
- Calculate final borrower classification
- Flag any discrepancies for underwriter review

### 2.4.2 Acceptable Experience Documentation

**Primary Documentation (Required):**

1. **HUD-1 Settlement Statements**
   - Shows borrower as buyer (acquisition) or seller (disposition)
   - Includes property address and closing date
   - Shows transaction amounts and closing costs

2. **Warranty Deeds**
   - Recorded deed showing property transfer
   - Borrower or borrower's entity as grantee/grantor
   - Matches HUD-1 transaction

**Secondary Documentation (Supporting):**

3. **Before/After Photos**
   - Demonstrates scope of renovation work
   - Timestamped if possible
   - Multiple angles of property

4. **Contractor Invoices**
   - Shows rehab work completed
   - Paid invoices with property address
   - Supports rehab budget claims

5. **Profit/Loss Statements**
   - Borrower-prepared or CPA-prepared
   - Shows deal economics
   - Demonstrates profitability

### 2.4.3 Experience Calculation Scenarios

**Scenario 1: Fix & Flip Projects**
```
Borrower completed 4 fix & flip projects:
- Property A: Purchased 01/2023, Sold 08/2023 → Counts as 1 deal
- Property B: Purchased 03/2023, Sold 11/2023 → Counts as 1 deal
- Property C: Purchased 06/2023, Still owned → Does NOT count
- Property D: Purchased 09/2023, Sold 03/2024 → Counts as 1 deal

Total Verified Experience = 3 deals
```

**Scenario 2: Mixed Transaction Types**
```
Borrower completed:
- 3 Fix & Flip projects (documented) → 3 deals
- 2 Rental acquisitions (documented) → 2 deals
- 1 Wholesale assignment (documented) → 1 deal
- 1 Personal residence sale → Does NOT count

Total Verified Experience = 6 deals
```

**Scenario 3: Incomplete Documentation**
```
Borrower claims 10 deals but provides:
- 5 deals with complete HUD-1s (acquisition + disposition) → 5 deals
- 3 deals with only acquisition HUD-1s → 0 deals (incomplete)
- 2 deals with no documentation → 0 deals

Total Verified Experience = 5 deals
```

### 2.4.4 First-Time Investor Programs

Borrowers with limited or no verified experience may qualify under enhanced scrutiny:

**First-Time Investor Criteria:**
- FICO ≥ 700 (no exceptions)
- Minimum 12 months liquidity reserves
- Detailed business plan and exit strategy
- Construction or real estate industry background (preferred)
- Lower leverage limits (typically Class B or C)
- Investor approval required

**Compensating Factors for Limited Experience:**
1. **Industry Experience**: Construction, property management, real estate sales
2. **Strong Financial Profile**: High net worth, significant liquidity
3. **Local Market Knowledge**: Demonstrated understanding of target market
4. **Conservative Deal Structure**: Low leverage, strong cash flow
5. **Professional Team**: Experienced contractor, property manager, real estate agent

---

## 2.5 Citizenship and Residency Requirements

### 2.5.1 Eligible Citizenship Categories

**Category 1: U.S. Citizens**
- Standard eligibility and leverage
- No additional documentation beyond government-issued ID
- Social Security Number required

**Category 2: Permanent Residents (Green Card Holders)**
- Standard eligibility and leverage
- Valid Permanent Resident Card (Green Card) required
- Social Security Number required
- Green Card must be valid through loan closing

**Category 3: Foreign Nationals**
- Eligible with enhanced requirements
- Additional documentation required
- Leverage and DSCR impacts (see below)
- ITIN (Individual Taxpayer Identification Number) required if no SSN

**Category 4: ITIN Borrowers**
- Eligible with same requirements as Foreign Nationals
- ITIN letter from IRS required
- May have limited investor options

### 2.5.2 Foreign National Requirements

Foreign Nationals are eligible for both RTL and DSCR products with the following adjustments:

**RTL Products - Foreign National Impact:**

| Impact Area | Standard | Foreign National |
|-------------|----------|------------------|
| Credit Decision Score | Based on FICO | Always 0 points |
| Classification | Based on total score | Can achieve A+ with 7+ experience points |
| Leverage | Standard by class | May have additional reductions |
| Documentation | Standard | Enhanced (see below) |

**DSCR Products - Foreign National Impact:**

| Impact Area | Standard | Foreign National |
|-------------|----------|------------------|
| Base LTV | 75-80% | 65% (all purposes) |
| Minimum DSCR | 1.00x - 1.20x | 1.20x (all scenarios) |
| DSCR Enhancement | N/A | +5% LTV if DSCR ≥ 1.30x |
| Reserve Requirements | 6-12 months | 12 months minimum |

**Foreign National Documentation Requirements:**

1. **Identification:**
   - Valid passport from country of citizenship
   - Visa documentation (if applicable)
   - ITIN letter from IRS

2. **Financial Documentation:**
   - Bank statements (U.S. or foreign accounts)
   - Currency conversion documentation if foreign accounts
   - Net worth verification
   - Source of funds documentation

3. **Legal Documentation:**
   - U.S. mailing address
   - U.S. bank account (required for loan servicing)
   - Power of Attorney (if not present at closing)
   - Translation of foreign documents (if applicable)

4. **Tax Compliance:**
   - ITIN or SSN
   - W-8BEN form (Certificate of Foreign Status)
   - Tax return filing commitment

### 2.5.3 ITIN Borrower Requirements

Borrowers with Individual Taxpayer Identification Numbers (ITIN) instead of Social Security Numbers are treated as Foreign Nationals for underwriting purposes.

**ITIN Documentation:**
- IRS ITIN assignment letter
- Valid passport or other identification
- U.S. tax return history (if available)

**ITIN Limitations:**
- Some investors may not accept ITIN borrowers
- May require additional reserves or lower leverage
- Enhanced documentation requirements

---

## 2.6 Prohibited Borrower Characteristics

Certain borrower characteristics result in automatic ineligibility regardless of compensating factors.

### 2.6.1 Automatic Disqualifications

| Disqualification | Reason | Exception Process |
|------------------|--------|-------------------|
| **OFAC/Sanctions Match** | Regulatory prohibition | None - Not eligible |
| **Recent Fraud Conviction** | Financial crimes (< 7 years) | None - Not eligible |
| **Active Bankruptcy** | Cannot close during bankruptcy | Wait for discharge |
| **FICO < 620** | Below all investor minimums | None - Not eligible |
| **Debarred from Federal Programs** | HUD/FHA debarment | None - Not eligible |

### 2.6.2 OFAC and Sanctions Screening

**Office of Foreign Assets Control (OFAC) Screening:**
- Required for all borrowers, guarantors, and beneficial owners
- Screening against:
  - OFAC Specially Designated Nationals (SDN) List
  - Consolidated Sanctions List
  - Foreign Sanctions Evaders List
  - Sectoral Sanctions Identifications List

**Screening Process:**
1. Automated screening during application
2. Manual review of potential matches
3. False positive resolution (common names)
4. Documentation of screening results

**Match Result Actions:**
- **No Match**: Proceed with application
- **Potential Match**: Manual review required, additional documentation
- **Confirmed Match**: Application declined immediately

### 2.6.3 Criminal History Considerations

**Financial Crimes (Automatic Decline):**
- Fraud (any type)
- Embezzlement
- Money laundering
- Mortgage fraud
- Identity theft
- Securities fraud

**Other Felonies (Case-by-Case Review):**
- Non-financial felonies may be acceptable if:
  - Conviction > 7 years ago
  - No pattern of criminal behavior
  - Full disclosure provided
  - Investor approval obtained

**Misdemeanors:**
- Generally acceptable
- Full disclosure required
- Review for pattern of behavior

### 2.6.4 Active Litigation

**Borrower as Defendant:**
- Active litigation involving the subject property: **Not eligible**
- Active litigation unrelated to property: Case-by-case review
- Judgments > $10,000: Must be resolved or on payment plan (see Section 4)

**Borrower as Plaintiff:**
- Generally acceptable
- Review for potential impact on deal
- Disclosure required

---

## 2.7 Entity Borrower Considerations

When the borrowing entity is an LLC, Corporation, Trust, or other legal entity, eligibility is determined by the guarantors (Key Principals).

### 2.7.1 Key Principal Identification

**Key Principal Definition:**
An individual who:
- Owns ≥ 20% of the borrowing entity, OR
- Has operational control of the entity, OR
- Is designated as a guarantor on the loan

**Multiple Key Principals:**
- All Key Principals must meet minimum eligibility requirements
- Classification based on highest ownership percentage guarantor
- Credit and experience evaluated for each Key Principal

### 2.7.2 Entity Borrower Classification

**For RTL Products:**
```
Step 1: Identify all Key Principals
Step 2: Determine Credit Decision Score for each
Step 3: Determine Experience Score for each
Step 4: Use highest ownership percentage Key Principal for classification
Step 5: If equal ownership, use lesser qualifying classification
```

**Example: Multiple Key Principals**
```
Entity: ABC Investments LLC

Key Principal A:
- Ownership: 60%
- FICO: 690
- Experience: 4 deals
- Credit Decision Score: 1
- Experience Score: 5
- Total Score: 6 → Classification A

Key Principal B:
- Ownership: 40%
- FICO: 740
- Experience: 15 deals
- Credit Decision Score: 3
- Experience Score: 7
- Total Score: 10 → Classification A+

Entity Classification = A (based on 60% owner, Key Principal A)
```

### 2.7.3 Guarantor Requirements

**Guarantee Coverage:**
- All Key Principals must provide personal guarantee
- Guarantee typically covers full loan amount
- Carve-out guarantees may be acceptable (investor approval)

**Guarantor Qualifications:**
- Each guarantor must meet minimum FICO requirements
- Each guarantor must meet minimum liquidity requirements
- Combined net worth must meet loan amount requirement

See Section 3 for complete entity and guarantor analysis requirements.

---

## 2.8 Liquidity and Net Worth Requirements

### 2.8.1 Liquidity Requirements

**Definition:**
Liquid assets are cash or assets easily convertible to cash within 30 days.

**Eligible Liquid Assets:**
- Cash in bank accounts (checking, savings)
- Money market accounts
- Stocks, bonds, mutual funds (publicly traded)
- Retirement accounts (with 40% haircut for early withdrawal penalties)
- CDs (certificates of deposit)

**Non-Eligible Assets:**
- Real estate equity
- Business equity
- Vehicles
- Personal property
- Restricted stock
- Cryptocurrency (unless specifically approved)

**RTL Liquidity Requirements:**

| Loan Amount | Minimum Liquidity |
|-------------|-------------------|
| Up to $500K | 6 months PITIA |
| $500K - $1M | 9 months PITIA |
| $1M - $2M | 12 months PITIA |
| $2M - $3M | 18 months PITIA |

**DSCR Liquidity Requirements:**

| FICO | LTV ≤ 75% | LTV > 75% |
|------|-----------|-----------|
| 720+ | 6 months PITIA | 9 months PITIA |
| 700-719 | 6 months PITIA | 12 months PITIA |
| 680-699 | 9 months PITIA | 12 months PITIA |
| Foreign National | 12 months PITIA | 18 months PITIA |

**PITIA Calculation for Reserves:**
```
Monthly PITIA = (Principal + Interest) + (Annual Taxes / 12) + (Annual Insurance / 12) + Monthly HOA

Reserve Requirement = Monthly PITIA × Required Months
```

### 2.8.2 Net Worth Requirements

**Definition:**
Net worth is the total value of all assets minus all liabilities.

**Standard Requirements:**
- RTL Products: Net worth ≥ loan amount
- DSCR Products: Net worth ≥ loan amount (some investors may vary)

**Net Worth Calculation:**

**Assets:**
- Cash and liquid investments (full value)
- Real estate (appraised value minus outstanding mortgages)
- Business equity (documented value)
- Retirement accounts (full value)
- Other investments

**Liabilities:**
- Mortgages and real estate debt
- Business debt
- Credit card balances
- Auto loans
- Student loans
- Other personal debt

**Net Worth = Total Assets - Total Liabilities**

**Documentation:**
- Personal Financial Statement (PFS)
- Bank statements (most recent 2 months)
- Brokerage statements
- Retirement account statements
- Real estate schedule with values and mortgages

---

## 2.9 Age and Legal Capacity

### 2.9.1 Minimum Age Requirement

- All borrowers and guarantors must be at least 18 years old
- Age verified through government-issued identification
- Legal capacity to enter into contracts required

### 2.9.2 Legal Capacity Considerations

**Competency:**
- Borrower must have legal capacity to contract
- No active guardianship or conservatorship
- Mental competency assumed unless documented otherwise

**Power of Attorney:**
- POA may be acceptable for closing if borrower cannot attend
- Must be specific to the transaction
- Must be properly executed and notarized
- Attorney-in-fact must have legal capacity

---

## 2.10 Python Implementation

### 2.10.1 Borrower Classification Module

```python
"""
Borrower Classification Module
Calculates RTL borrower classification (A+, A, B, C) based on credit and experience.
"""

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Tuple


class BorrowerClass(Enum):
    """RTL Borrower Classification"""
    A_PLUS = "A+"
    A = "A"
    B = "B"
    C = "C"


class CitizenshipType(Enum):
    """Borrower Citizenship Status"""
    US_CITIZEN = "US_CITIZEN"
    PERMANENT_RESIDENT = "PERMANENT_RESIDENT"
    FOREIGN_NATIONAL = "FOREIGN_NATIONAL"
    ITIN = "ITIN"


@dataclass
class Guarantor:
    """Individual Guarantor Information"""
    name: str
    ownership_percentage: float  # 0.0 to 1.0
    fico_score: int
    verified_deals_36mo: int
    citizenship: CitizenshipType
    is_key_principal: bool = True
    
    def __post_init__(self):
        """Validate guarantor data"""
        if not 0 <= self.ownership_percentage <= 1.0:
            raise ValueError("Ownership percentage must be between 0 and 1")
        if self.fico_score < 300 or self.fico_score > 850:
            raise ValueError("FICO score must be between 300 and 850")
        if self.verified_deals_36mo < 0:
            raise ValueError("Verified deals cannot be negative")


@dataclass
class ClassificationResult:
    """Result of borrower classification calculation"""
    classification: BorrowerClass
    total_score: int
    credit_decision_score: int
    experience_score: int
    qualifying_guarantor: Guarantor
    explanation: str


class BorrowerClassifier:
    """
    Calculate borrower classification for RTL loans.
    
    Classification is based on:
    - Credit Decision Score (0-3 points based on FICO)
    - Verified Experience Score (1-7 points based on deals in last 36 months)
    
    Total Score determines classification:
    - >= 7: A+
    - 5-6: A
    - 2-4: B
    - < 2: C
    """
    
    # Classification thresholds
    CLASSIFICATION_THRESHOLDS = {
        7: BorrowerClass.A_PLUS,
        5: BorrowerClass.A,
        2: BorrowerClass.B,
        0: BorrowerClass.C
    }
    
    # Credit Decision Score matrix
    CREDIT_SCORE_MATRIX = [
        (700, 3),  # FICO >= 700 = 3 points
        (680, 1),  # FICO 680-699 = 1 point
        (0, 0)     # FICO < 680 = 0 points
    ]
    
    # Experience Score matrix
    EXPERIENCE_MATRIX = [
        (10, 7),  # 10+ deals = 7 points
        (3, 5),   # 3-9 deals = 5 points
        (0, 1)    # 0-2 deals = 1 point
    ]
    
    def calculate_credit_decision_score(
        self, 
        fico: int, 
        citizenship: CitizenshipType
    ) -> int:
        """
        Calculate Credit Decision Score based on FICO and citizenship.
        
        Args:
            fico: Middle FICO score from tri-merge report
            citizenship: Citizenship status
            
        Returns:
            Credit Decision Score (0-3 points)
        """
        # Foreign Nationals always get 0 points regardless of FICO
        if citizenship in (CitizenshipType.FOREIGN_NATIONAL, CitizenshipType.ITIN):
            return 0
        
        # Apply FICO-based scoring
        for threshold, points in self.CREDIT_SCORE_MATRIX:
            if fico >= threshold:
                return points
        
        return 0
    
    def calculate_experience_score(self, verified_deals_36mo: int) -> int:
        """
        Calculate Verified Experience Score based on deals in last 36 months.
        
        Args:
            verified_deals_36mo: Number of verified deals completed in last 36 months
            
        Returns:
            Experience Score (1-7 points)
        """
        for threshold, points in self.EXPERIENCE_MATRIX:
            if verified_deals_36mo >= threshold:
                return points
        
        return 1  # Minimum 1 point
    
    def get_classification(
        self, 
        fico: int, 
        verified_deals_36mo: int, 
        citizenship: CitizenshipType
    ) -> Tuple[BorrowerClass, int, int, int]:
        """
        Determine borrower classification from credit and experience scores.
        
        Args:
            fico: Middle FICO score
            verified_deals_36mo: Verified deals in last 36 months
            citizenship: Citizenship status
            
        Returns:
            Tuple of (classification, total_score, credit_score, experience_score)
        """
        credit_score = self.calculate_credit_decision_score(fico, citizenship)
        experience_score = self.calculate_experience_score(verified_deals_36mo)
        total_score = credit_score + experience_score
        
        # Determine classification from total score
        classification = BorrowerClass.C  # Default
        for threshold, class_level in sorted(
            self.CLASSIFICATION_THRESHOLDS.items(), 
            reverse=True
        ):
            if total_score >= threshold:
                classification = class_level
                break
        
        return classification, total_score, credit_score, experience_score
    
    def classify_single_borrower(self, guarantor: Guarantor) -> ClassificationResult:
        """
        Classify a single borrower/guarantor.
        
        Args:
            guarantor: Guarantor information
            
        Returns:
            ClassificationResult with full details
        """
        classification, total, credit, experience = self.get_classification(
            guarantor.fico_score,
            guarantor.verified_deals_36mo,
            guarantor.citizenship
        )
        
        explanation = (
            f"Credit Decision Score: {credit} points (FICO {guarantor.fico_score})\n"
            f"Experience Score: {experience} points ({guarantor.verified_deals_36mo} deals)\n"
            f"Total Score: {total} points → Classification: {classification.value}"
        )
        
        return ClassificationResult(
            classification=classification,
            total_score=total,
            credit_decision_score=credit,
            experience_score=experience,
            qualifying_guarantor=guarantor,
            explanation=explanation
        )
    
    def classify_entity_borrower(
        self, 
        guarantors: List[Guarantor]
    ) -> ClassificationResult:
        """
        Classify entity borrower based on multiple guarantors.
        
        Classification rules:
        1. Use guarantor with highest ownership percentage
        2. If equal ownership, use lesser qualifying classification
        
        Args:
            guarantors: List of all guarantors
            
        Returns:
            ClassificationResult based on qualifying guarantor
        """
        if not guarantors:
            raise ValueError("At least one guarantor required")
        
        # Filter to key principals only
        key_principals = [g for g in guarantors if g.is_key_principal]
        if not key_principals:
            raise ValueError("At least one key principal required")
        
        # Calculate classification for each guarantor
        results = []
        for guarantor in key_principals:
            result = self.classify_single_borrower(guarantor)
            results.append((guarantor, result))
        
        # Sort by ownership percentage (descending)
        results.sort(key=lambda x: x[0].ownership_percentage, reverse=True)
        
        # Check for equal ownership at top
        max_ownership = results[0][0].ownership_percentage
        top_guarantors = [
            (g, r) for g, r in results 
            if g.ownership_percentage == max_ownership
        ]
        
        if len(top_guarantors) > 1:
            # Equal ownership - use lesser classification
            # Sort by total score (ascending) to get lesser classification
            top_guarantors.sort(key=lambda x: x[1].total_score)
            qualifying_guarantor, qualifying_result = top_guarantors[0]
            
            explanation = (
                f"Multiple guarantors with equal ownership ({max_ownership:.1%})\n"
                f"Using lesser qualifying classification\n"
                f"Qualifying Guarantor: {qualifying_guarantor.name}\n"
                f"{qualifying_result.explanation}"
            )
        else:
            # Single highest ownership
            qualifying_guarantor, qualifying_result = top_guarantors[0]
            
            explanation = (
                f"Qualifying Guarantor: {qualifying_guarantor.name} "
                f"({qualifying_guarantor.ownership_percentage:.1%} ownership)\n"
                f"{qualifying_result.explanation}"
            )
        
        return ClassificationResult(
            classification=qualifying_result.classification,
            total_score=qualifying_result.total_score,
            credit_decision_score=qualifying_result.credit_decision_score,
            experience_score=qualifying_result.experience_score,
            qualifying_guarantor=qualifying_guarantor,
            explanation=explanation
        )


class BorrowerEligibilityChecker:
    """
    Validate borrower meets minimum eligibility requirements.
    """
    
    # Minimum FICO requirements
    MIN_FICO_RTL = 660
    MIN_FICO_DSCR = 680
    
    # Minimum experience requirements
    MIN_EXPERIENCE_RTL = 0  # Can be 0 with compensating factors
    MIN_EXPERIENCE_DSCR = 0  # No experience required for DSCR
    
    def check_fico_eligibility(
        self, 
        fico: int, 
        loan_type: str
    ) -> Tuple[bool, str]:
        """
        Check if FICO meets minimum requirements.
        
        Args:
            fico: Middle FICO score
            loan_type: 'RTL' or 'DSCR'
            
        Returns:
            Tuple of (is_eligible, message)
        """
        min_fico = self.MIN_FICO_DSCR if loan_type == 'DSCR' else self.MIN_FICO_RTL
        
        if fico >= min_fico:
            return True, f"FICO {fico} meets minimum requirement of {min_fico}"
        else:
            return False, f"FICO {fico} below minimum requirement of {min_fico}"
    
    def check_experience_eligibility(
        self, 
        verified_deals: int, 
        fico: int,
        loan_type: str
    ) -> Tuple[bool, str]:
        """
        Check if experience meets minimum requirements.
        
        Args:
            verified_deals: Number of verified deals in last 36 months
            fico: FICO score (for compensating factors)
            loan_type: 'RTL' or 'DSCR'
            
        Returns:
            Tuple of (is_eligible, message)
        """
        if loan_type == 'DSCR':
            return True, "No experience required for DSCR loans"
        
        # RTL loans
        if verified_deals >= 1:
            return True, f"{verified_deals} verified deals meets requirement"
        
        # First-time investor - check compensating factors
        if verified_deals == 0 and fico >= 700:
            return True, "First-time investor eligible with FICO >= 700 (requires approval)"
        
        return False, "Minimum 1 verified deal required (or FICO >= 700 for first-time)"
    
    def check_citizenship_eligibility(
        self, 
        citizenship: CitizenshipType
    ) -> Tuple[bool, str]:
        """
        Check if citizenship status is eligible.
        
        All citizenship types are eligible with appropriate documentation.
        
        Args:
            citizenship: Citizenship status
            
        Returns:
            Tuple of (is_eligible, message)
        """
        messages = {
            CitizenshipType.US_CITIZEN: "U.S. Citizen - standard eligibility",
            CitizenshipType.PERMANENT_RESIDENT: "Permanent Resident - standard eligibility",
            CitizenshipType.FOREIGN_NATIONAL: "Foreign National - eligible with enhanced requirements",
            CitizenshipType.ITIN: "ITIN Borrower - eligible with enhanced requirements"
        }
        
        return True, messages[citizenship]
    
    def check_full_eligibility(
        self,
        guarantors: List[Guarantor],
        loan_type: str
    ) -> Tuple[bool, List[str]]:
        """
        Perform full eligibility check for all guarantors.
        
        Args:
            guarantors: List of all guarantors
            loan_type: 'RTL' or 'DSCR'
            
        Returns:
            Tuple of (is_eligible, list of messages)
        """
        messages = []
        all_eligible = True
        
        for guarantor in guarantors:
            # Check FICO
            fico_eligible, fico_msg = self.check_fico_eligibility(
                guarantor.fico_score, 
                loan_type
            )
            messages.append(f"{guarantor.name}: {fico_msg}")
            if not fico_eligible:
                all_eligible = False
            
            # Check experience (only for RTL)
            if loan_type == 'RTL':
                exp_eligible, exp_msg = self.check_experience_eligibility(
                    guarantor.verified_deals_36mo,
                    guarantor.fico_score,
                    loan_type
                )
                messages.append(f"{guarantor.name}: {exp_msg}")
                if not exp_eligible:
                    all_eligible = False
            
            # Check citizenship
            cit_eligible, cit_msg = self.check_citizenship_eligibility(
                guarantor.citizenship
            )
            messages.append(f"{guarantor.name}: {cit_msg}")
        
        return all_eligible, messages


# Example usage
if __name__ == "__main__":
    # Example 1: Single borrower classification
    classifier = BorrowerClassifier()
    
    borrower = Guarantor(
        name="John Smith",
        ownership_percentage=1.0,
        fico_score=720,
        verified_deals_36mo=8,
        citizenship=CitizenshipType.US_CITIZEN
    )
    
    result = classifier.classify_single_borrower(borrower)
    print(f"Classification: {result.classification.value}")
    print(f"Total Score: {result.total_score}")
    print(result.explanation)
    print()
    
    # Example 2: Entity with multiple guarantors
    guarantors = [
        Guarantor(
            name="Jane Doe",
            ownership_percentage=0.6,
            fico_score=695,
            verified_deals_36mo=4,
            citizenship=CitizenshipType.US_CITIZEN
        ),
        Guarantor(
            name="Bob Johnson",
            ownership_percentage=0.4,
            fico_score=740,
            verified_deals_36mo=15,
            citizenship=CitizenshipType.US_CITIZEN
        )
    ]
    
    result = classifier.classify_entity_borrower(guarantors)
    print(f"Entity Classification: {result.classification.value}")
    print(result.explanation)
    print()
    
    # Example 3: Eligibility check
    checker = BorrowerEligibilityChecker()
    eligible, messages = checker.check_full_eligibility(guarantors, 'RTL')
    print(f"Eligible: {eligible}")
    for msg in messages:
        print(f"  - {msg}")
```

### 2.10.2 Usage Examples

```python
# Example 1: Calculate classification for A+ borrower
classifier = BorrowerClassifier()
classification, total, credit, exp = classifier.get_classification(
    fico=725,
    verified_deals_36mo=12,
    citizenship=CitizenshipType.US_CITIZEN
)
print(f"Classification: {classification.value}")  # Output: A+
print(f"Total Score: {total}")  # Output: 10

# Example 2: Foreign National with high experience
classification, total, credit, exp = classifier.get_classification(
    fico=750,
    verified_deals_36mo=15,
    citizenship=CitizenshipType.FOREIGN_NATIONAL
)
print(f"Classification: {classification.value}")  # Output: A+
print(f"Credit Score: {credit}")  # Output: 0 (Foreign National)
print(f"Experience Score: {exp}")  # Output: 7

# Example 3: Check eligibility
checker = BorrowerEligibilityChecker()
eligible, msg = checker.check_fico_eligibility(fico=685, loan_type='RTL')
print(f"Eligible: {eligible}")  # Output: True
print(msg)  # Output: FICO 685 meets minimum requirement of 660
```

---

## 2.11 Cross-References

**Related Sections:**
- **Section 3**: Entity & Guarantor Analysis - Detailed entity structure requirements
- **Section 4**: Credit & Background Evaluation - Credit report analysis and derogatory events
- **Section 7**: DSCR Property & Income Analysis - DSCR calculation and minimum requirements
- **Section 9**: RTL Loan Sizing & Leverage - How classification determines leverage limits
- **Section 10**: DSCR Loan Sizing & Leverage - FICO-based LTV limits for DSCR loans
- **Section 12**: Exception Management - Exception process for borrowers not meeting standards

---

*End of Section 2*

