---
section: 9
title: RTL Loan Sizing & Leverage
version: 1.0
last_updated: 2025-12-30
model_used: opus
guideline_sources:
  - Archwest RTL Guidelines v6.0
  - Eastview RTL Guidelines v4.1
  - RTL Program Guidelines 07.09.2025
changelog:
  - 2025-12-30: Initial creation
---

# Section 9: RTL Loan Sizing & Leverage

## 9.1 Overview

RTL (Residential Transition Loan) sizing determines the maximum loan amount based on multiple leverage constraints. The loan amount is calculated as the minimum of several metrics, each designed to ensure appropriate risk mitigation based on borrower strength and deal characteristics.

**INSPIRE Integration Points:**
- Phase 3-4: RTL loan sizing engine for Fix & Flip, Bridge, and Ground-Up Construction products

---

## 9.2 Leverage Metrics Definitions

### 9.2.1 As-Is Loan-to-Value (LTV)

The ratio of the initial loan amount to the property's current market value.

```
As-Is LTV = Initial Loan Amount / As-Is Value
```

**As-Is Value Determination:**
| Loan Purpose | As-Is Value Definition |
|--------------|----------------------|
| Purchase | Lesser of Purchase Price or Appraised As-Is Value |
| Refinance (acquired <6mo) | Lesser of Original Purchase Price or Appraised As-Is Value |
| Refinance (acquired >6mo) | Appraised As-Is Value |

### 9.2.2 Loan-to-Cost (LTC)

The ratio of the initial loan amount to the total cost basis of the property.

```
LTC = Initial Loan Amount / Cost Basis
```

**Cost Basis Calculation:**

**Purchase Transactions:**
```
Cost Basis = Purchase Price + Allowable Closing Costs + Assignment Fees

Where:
- Allowable Closing Costs = HUD closing costs excluding origination points
- Assignment Fees = MIN(Assignment Fee, 5% of Purchase Price, $40,000)
```

**Refinance Transactions:**
```
Cost Basis = Original Purchase Price + Verified Completed Rehab

Where:
- Verified Completed Rehab = Rehabilitation costs with before/after photos
```

### 9.2.3 Loan-to-After-Repair Value (LTARV)

The ratio of the total loan amount (including rehab holdback) to the projected after-repair value.

```
LTARV = Total Loan Amount / After-Repair Value (ARV)

Where:
- Total Loan Amount = Initial Loan Amount + Rehab Holdback
```

---

## 9.3 Borrower Classification System

Borrower classification determines maximum leverage limits. Classification is calculated from Credit Decision Score and Verified Experience Score.

### 9.3.1 Credit Decision Score

| FICO Range | Score |
|------------|-------|
| >= 700 | 3 |
| 680-699 | 1 |
| < 680 or Foreign National | 0 |

**FICO Score Determination:**
- Use the lower of two scores or median of three scores per guarantor
- Loan's Credit Decision Score = Score of highest ownership percentage guarantor
- If equal ownership, use the lesser qualifying Credit Decision Score
- Minimum FICO: 660 for all guarantors

### 9.3.2 Verified Experience Score

| Experience (Last 36 Months) | Score |
|----------------------------|-------|
| 10+ completed deals | 7 |
| 3-9 completed deals | 5 |
| 0-2 completed deals | 1 |

**Experience Qualification:**
| Experience Type | Qualifying Points |
|-----------------|-------------------|
| Property rehab completed and sold | 1.00 |
| Property rehab completed and refinanced as rental | 1.00 |
| Property acquired as rental (lease or >1yr ownership) | 0.50 |
| Property rehab as General Contractor (not owner) | 0.50 |

**Experience Requirements:**
- Combined experience of all entity owners is used
- Experience must be within 36 months of origination
- At least one verified exit of a like-and-kind project required
- Individual must be a guarantor to count toward track record
- Must have been on title for the qualifying transaction

### 9.3.3 Borrower Classification Calculation

```
Total Score = Credit Decision Score + Verified Experience Score
```

| Total Score | Classification |
|-------------|----------------|
| >= 7 | A+ |
| 5-6 | A |
| 2-4 | B |
| < 2 | C |

**Classification Examples:**

| Scenario | FICO | Credit Score | Experience | Exp Score | Total | Class |
|----------|------|--------------|------------|-----------|-------|-------|
| Strong | 740 | 3 | 12 deals | 7 | 10 | A+ |
| Good | 720 | 3 | 5 deals | 5 | 8 | A+ |
| Moderate | 690 | 1 | 4 deals | 5 | 6 | A |
| Limited | 680 | 1 | 1 deal | 1 | 2 | B |
| New | 750 | 3 | 0 deals | 1 | 4 | B |
| Weak | 670 | 0 | 1 deal | 1 | 1 | C |

---

## 9.4 Leverage Matrices by Product

### 9.4.1 Fix & Flip Leverage Limits

**Fix & Flip - Purchase:**

| Class | Max As-Is LTV | Max LTC | Max LTARV |
|-------|---------------|---------|-----------|
| A+ | 90.0% | 90.0% | 75.0% |
| A | 85.0% | 85.0% | 70.0% |
| B | 82.5% | 82.5% | 65.0% |
| C | 75.0% | 75.0% | 60.0% |

**Fix & Flip - Rate & Term Refinance:**

| Class | Max As-Is LTV | Max LTC | Max LTARV |
|-------|---------------|---------|-----------|
| A+ | 75.0% | N/A | 65.0% |
| A | 72.5% | N/A | 65.0% |
| B | 70.0% | N/A | 60.0% |
| C | 60.0% | N/A | 55.0% |

**Fix & Flip - Cash-Out Refinance:**

| Class | Max As-Is LTV | Max LTC | Max LTARV |
|-------|---------------|---------|-----------|
| A+ | 70.0% | N/A | 65.0% |
| A | 67.5% | N/A | 65.0% |
| B | 65.0% | N/A | 60.0% |
| C | N/A | N/A | N/A |

**Note:** Class C borrowers are not eligible for cash-out refinance on Fix & Flip products.

### 9.4.2 Bridge Leverage Limits

**Bridge - Purchase:**

| Class | Max As-Is LTV | Max LTC |
|-------|---------------|---------|
| A+ | 82.5% | 82.5% |
| A | 80.0% | 80.0% |
| B | 80.0% | 80.0% |
| C | 75.0% | 75.0% |

**Bridge - Rate & Term Refinance:**

| Class | Max As-Is LTV |
|-------|---------------|
| A+ | 77.5% |
| A | 75.0% |
| B | 75.0% |
| C | 65.0% |

**Bridge - Cash-Out Refinance:**

| Class | Max As-Is LTV |
|-------|---------------|
| A+ | 72.5% |
| A | 70.0% |
| B | 70.0% |
| C | 60.0% |

### 9.4.3 Bridge Plus Leverage Limits

Bridge Plus is designed for stabilized rental properties with terms of 25-36 months.

**Bridge Plus - Purchase:**

| Class | Max As-Is LTV | Max LTC |
|-------|---------------|---------|
| A+ | 77.5% | 77.5% |
| A | 75.0% | 75.0% |
| B | 75.0% | 75.0% |
| C | 70.0% | 70.0% |

**Bridge Plus - Rate & Term Refinance:**

| Class | Max As-Is LTV |
|-------|---------------|
| A+ | 72.5% |
| A | 70.0% |
| B | 70.0% |
| C | 60.0% |

**Bridge Plus - Cash-Out Refinance:**

| Class | Max As-Is LTV |
|-------|---------------|
| A+ | 67.5% |
| A | 65.0% |
| B | 65.0% |
| C | 55.0% |

### 9.4.4 Ground-Up Construction Leverage Limits

| Metric | Maximum |
|--------|---------|
| LT As-Is Value (Land) | 70.0% |
| LTC | 85.0% |
| LTARV | 67.5% |

**Additional GUC Requirements:**
- Maximum Initial Draw to Land: 60% (70% with issued building permits, case-by-case)
- Minimum Experience: 3 deals in last 36 months (or 2 if licensed GC with 2x liquidity and 720+ FICO)
- Small Multifamily (5-9 units): Additional -10% reduction

---

## 9.5 Leverage Reductions

Leverage reductions are applied cumulatively to the base leverage limits.

### 9.5.1 Standard Leverage Reductions

| Condition | Reduction | Applies To |
|-----------|-----------|------------|
| Heavy Rehab (Class A+ / A / B) | -5% | All metrics |
| Heavy Rehab (Class C) | -10% | All metrics |
| HPA Decline 0% to -10% | -5% | All metrics |
| ZHVI Multiplier 200% - 300% | -5% | All metrics |
| Loan Amount $2M - $3M | -5% | All metrics |
| Small Multifamily 5-9 Units (RTL) | -5% | All metrics |
| Small Multifamily 5-9 Units (GUC) | -10% | All metrics |

### 9.5.2 Heavy Rehab Definition

A project qualifies as **Heavy Rehab** when BOTH conditions are met:

1. Rehab budget exceeds **$50,000**, AND
2. Rehab budget exceeds **100%** of:
   - Purchase price (for purchase transactions), OR
   - As-is value (for refinance transactions)

**Additional Heavy Rehab Trigger:**
- Work increases Gross Living Area (GLA) by 25% or more

### 9.5.3 Market Condition Indicators

**Home Price Appreciation (HPA):**
- Measures percentage change in median home value for the zip code
- HPA between 0% and -10% triggers -5% leverage reduction
- HPA below -10% may require additional review or decline

**Zillow Home Value Index (ZHVI) Multiplier:**
```
ZHVI Multiplier = Property Value / Zip Code ZHVI
```

| ZHVI Multiplier | Impact |
|-----------------|--------|
| < 200% | No reduction |
| 200% - 300% | -5% leverage reduction |
| > 300% | Ineligible without exception |

### 9.5.4 Geographic Leverage Reductions

**5% LTC Reduction Markets:**
- Bay Area, CA
- Austin, TX
- Boise, ID
- Baltimore, MD
- Chicago suburbs
- Detroit, MI
- Sacramento, CA
- San Jose, CA (case-by-case)
- State of Florida (LTC/LTARV & LTAIV on no-rehab bridge)

**Ineligible Areas:**
- Western Florida (Port Charlotte, Cape Coral, Lehigh Acres)
- NYC 5 Boroughs
- Chicago (city limits)

**Elevated Risk Areas (case-by-case):**
- Jersey City, NJ
- Philadelphia, PA
- NYC suburbs
- Texas

---

## 9.6 Loan Amount Calculation

### 9.6.1 Initial Loan Amount Formula

The initial loan amount is the **minimum** of all applicable leverage constraints:

```
Initial Loan Amount = MIN(
    As-Is Value × Adjusted Max As-Is LTV,
    Cost Basis × Adjusted Max LTC,
    ARV × Adjusted Max LTARV
)
```

Where "Adjusted Max" = Base Max - Sum of All Applicable Reductions

### 9.6.2 Rehab Holdback Calculation

For Fix & Flip loans with rehabilitation:

```
Rehab Holdback = MIN(
    Rehab Budget,
    60% × Total Loan Amount
)
```

**Note:** Maximum rehab percentage is 60% of total loan amount.

### 9.6.3 Total Loan Amount

```
Total Loan Amount = Initial Loan Amount + Rehab Holdback
```

### 9.6.4 Iterative Calculation for Rehab Constraint

Since rehab holdback depends on total loan amount, which includes rehab holdback, an iterative calculation is required:

```
Step 1: Calculate Initial Loan Amount (ignoring rehab)
Step 2: Tentative Total = Initial + Rehab Budget
Step 3: Check if Rehab Budget > 60% of Tentative Total
Step 4: If yes, reduce Rehab Holdback to 60% of Total
Step 5: Recalculate Total Loan Amount
Step 6: Verify all leverage constraints are still met
```

---

## 9.7 Sizing Examples

### 9.7.1 Example 1: Standard Fix & Flip Purchase

**Scenario:**
- Borrower: Class A (FICO 720, 6 deals in 36mo)
- Purchase Price: $300,000
- As-Is Value: $310,000
- Rehab Budget: $50,000
- ARV: $420,000
- Closing Costs: $6,000

**Leverage Limits (Class A, Purchase):**
- Max As-Is LTV: 85.0%
- Max LTC: 85.0%
- Max LTARV: 70.0%

**Calculations:**

```
Cost Basis = $300,000 + $6,000 = $306,000

As-Is Constraint = $310,000 × 85% = $263,500
LTC Constraint = $306,000 × 85% = $260,100
ARV Constraint (Total) = $420,000 × 70% = $294,000

Initial Loan Amount = MIN($263,500, $260,100, $294,000) = $260,100 (LTC constraint binds)

Tentative Total = $260,100 + $50,000 = $310,100
Max Rehab (60% rule) = $310,100 × 60% = $186,060

Since $50,000 < $186,060, full rehab is financed.

Total Loan Amount = $260,100 + $50,000 = $310,100

Verify LTARV: $310,100 / $420,000 = 73.8% ✓ (< 70% max)
```

Wait - LTARV exceeds the 70% limit. Let's recalculate with LTARV as the binding constraint:

```
Total Loan from LTARV = $420,000 × 70% = $294,000

If Total Loan = $294,000 and Rehab = $50,000:
Initial Loan = $294,000 - $50,000 = $244,000

Verify As-Is LTV: $244,000 / $310,000 = 78.7% ✓ (< 85%)
Verify LTC: $244,000 / $306,000 = 79.7% ✓ (< 85%)

Final:
- Initial Loan Amount: $244,000
- Rehab Holdback: $50,000
- Total Loan Amount: $294,000
- Binding Constraint: LTARV
```

### 9.7.2 Example 2: Heavy Rehab Purchase

**Scenario:**
- Borrower: Class B (FICO 695, 2 deals in 36mo)
- Purchase Price: $200,000
- As-Is Value: $195,000
- Rehab Budget: $220,000 (Heavy Rehab: >$50K AND >100% of PP)
- ARV: $500,000
- Closing Costs: $5,000

**Leverage Limits (Class B, Purchase with Heavy Rehab):**
- Base Max As-Is LTV: 82.5% - 5% = 77.5%
- Base Max LTC: 82.5% - 5% = 77.5%
- Base Max LTARV: 65.0% - 5% = 60.0%

**Calculations:**

```
Cost Basis = $200,000 + $5,000 = $205,000

As-Is Constraint = $195,000 × 77.5% = $151,125
LTC Constraint = $205,000 × 77.5% = $158,875
ARV Constraint (Total) = $500,000 × 60% = $300,000

Initial Loan Amount = MIN($151,125, $158,875, $300,000) = $151,125

Tentative Total = $151,125 + $220,000 = $371,125
Max Rehab (60% rule) = $371,125 × 60% = $222,675

Since $220,000 < $222,675, full rehab can be financed.

Verify LTARV: $371,125 / $500,000 = 74.2% > 60% ❌

LTARV Constrains:
Total Loan = $500,000 × 60% = $300,000
Rehab Holdback = MIN($220,000, $300,000 × 60%) = MIN($220,000, $180,000) = $180,000
Initial Loan = $300,000 - $180,000 = $120,000

Verify As-Is LTV: $120,000 / $195,000 = 61.5% ✓
Verify LTC: $120,000 / $205,000 = 58.5% ✓

Final:
- Initial Loan Amount: $120,000
- Rehab Holdback: $180,000 (borrower must fund $40,000 of rehab)
- Total Loan Amount: $300,000
- Binding Constraint: LTARV
```

### 9.7.3 Example 3: Bridge Rate & Term Refinance

**Scenario:**
- Borrower: Class A+ (FICO 750, 15 deals in 36mo)
- Property acquired 8 months ago for $400,000
- Current As-Is Value: $420,000
- No rehab
- Existing debt payoff: $310,000

**Leverage Limits (Class A+, R&T Refi):**
- Max As-Is LTV: 77.5%

**Calculations:**

```
Max Loan = $420,000 × 77.5% = $325,500

Since $310,000 payoff < $325,500 max, loan is eligible.

Cash to Borrower = $325,500 - $310,000 - Closing Costs
If Closing Costs = $8,000:
Cash to Borrower = $325,500 - $310,000 - $8,000 = $7,500

Check R&T vs Cash-Out threshold:
$7,500 > 2% of $325,500 ($6,510) → This would be Cash-Out

For Rate & Term treatment:
Max Cash Back = MIN(2% of loan, $2,000) = MIN($6,510, $2,000) = $2,000

Adjusted Loan for R&T = $310,000 + $8,000 + $2,000 = $320,000
LTV: $320,000 / $420,000 = 76.2% ✓
```

---

## 9.8 Product Parameters Summary

| Parameter | Fix & Flip | Bridge | Bridge Plus | GUC |
|-----------|------------|--------|-------------|-----|
| Min Loan | $100,000 | $100,000 | $100,000 | $150,000 |
| Max Loan | $3,000,000 | $3,000,000 | $3,000,000 | $5,000,000 |
| Term | 12-24 months | 12-24 months | 25-36 months | 12-24 months |
| Extensions | Up to 2 × 3mo | Up to 1 × 3mo | N/A | Up to 2 × 3mo |
| Structure | Interest Only | Interest Only | Interest Only | Interest Only |
| Rate Type | Fixed | Fixed | Fixed | Fixed |
| Min Experience | 1 deal (36mo) | 1 deal (36mo) | 1 deal (36mo) | 3 deals (36mo) |
| Min FICO | 660 | 660 | 660 | 660 |
| Max Rehab % | 60% | N/A | N/A | N/A |

---

## 9.9 Python Implementation

```python
"""
RTL Loan Sizing & Leverage Module
USDV Capital Underwriting Library

This module provides comprehensive RTL loan sizing functionality
including borrower classification, leverage calculation, and
constraint analysis for Fix & Flip, Bridge, and GUC products.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List, Tuple, Dict
from decimal import Decimal, ROUND_HALF_UP


class LoanProduct(Enum):
    """RTL loan product types."""
    FIX_AND_FLIP = "fix_and_flip"
    BRIDGE = "bridge"
    BRIDGE_PLUS = "bridge_plus"
    GROUND_UP_CONSTRUCTION = "guc"


class LoanPurpose(Enum):
    """Loan purpose classification."""
    PURCHASE = "purchase"
    RATE_TERM_REFINANCE = "rate_term_refinance"
    CASH_OUT_REFINANCE = "cash_out_refinance"


class BorrowerClass(Enum):
    """Borrower classification tiers."""
    A_PLUS = "A+"
    A = "A"
    B = "B"
    C = "C"


@dataclass
class BorrowerClassification:
    """Result of borrower classification calculation."""
    fico_score: int
    credit_decision_score: int
    verified_experience: int
    experience_score: int
    total_score: int
    classification: BorrowerClass
    is_foreign_national: bool = False


@dataclass
class LeverageLimits:
    """Leverage limits for a specific scenario."""
    max_as_is_ltv: float
    max_ltc: Optional[float]
    max_ltarv: Optional[float]
    reductions_applied: List[str] = field(default_factory=list)
    total_reduction: float = 0.0


@dataclass
class CostBasis:
    """Cost basis calculation result."""
    purchase_price: float
    closing_costs: float
    assignment_fee: float
    completed_rehab: float
    total_cost_basis: float
    calculation_method: str


@dataclass
class SizingConstraint:
    """Individual sizing constraint result."""
    constraint_type: str  # "as_is_ltv", "ltc", "ltarv"
    base_value: float
    max_percentage: float
    max_loan_amount: float
    actual_percentage: float
    is_binding: bool


@dataclass
class RTLSizingResult:
    """Complete RTL sizing analysis result."""
    # Loan identification
    product: LoanProduct
    purpose: LoanPurpose

    # Borrower
    borrower_classification: BorrowerClassification

    # Property values
    as_is_value: float
    arv: Optional[float]
    cost_basis: CostBasis

    # Leverage limits
    leverage_limits: LeverageLimits

    # Sizing constraints
    constraints: List[SizingConstraint]
    binding_constraint: str

    # Loan amounts
    initial_loan_amount: float
    rehab_holdback: float
    total_loan_amount: float

    # Final metrics
    actual_as_is_ltv: float
    actual_ltc: Optional[float]
    actual_ltarv: Optional[float]

    # Eligibility
    is_eligible: bool
    ineligibility_reasons: List[str] = field(default_factory=list)

    # Notes
    notes: List[str] = field(default_factory=list)


class BorrowerClassifier:
    """
    Calculate borrower classification for RTL loans.

    Classification is based on Credit Decision Score and
    Verified Experience Score per USDV Guidelines.
    """

    # Credit Decision Score thresholds
    FICO_HIGH_THRESHOLD = 700
    FICO_MID_THRESHOLD = 680

    # Experience Score thresholds
    EXP_INSTITUTIONAL = 10
    EXP_EXPERIENCED = 3

    # Classification thresholds
    CLASS_A_PLUS_MIN = 7
    CLASS_A_MIN = 5
    CLASS_B_MIN = 2

    def calculate_credit_score_points(
        self,
        fico: int,
        is_foreign_national: bool = False
    ) -> int:
        """
        Calculate Credit Decision Score from FICO.

        Args:
            fico: Credit score (use lower of 2 or median of 3)
            is_foreign_national: FN status

        Returns:
            Credit Decision Score (0, 1, or 3)
        """
        if is_foreign_national:
            return 0

        if fico >= self.FICO_HIGH_THRESHOLD:
            return 3
        elif fico >= self.FICO_MID_THRESHOLD:
            return 1
        else:
            return 0

    def calculate_experience_points(self, deals_36mo: int) -> int:
        """
        Calculate Verified Experience Score.

        Args:
            deals_36mo: Number of verified deals in last 36 months

        Returns:
            Experience Score (1, 5, or 7)
        """
        if deals_36mo >= self.EXP_INSTITUTIONAL:
            return 7
        elif deals_36mo >= self.EXP_EXPERIENCED:
            return 5
        else:
            return 1

    def get_classification(self, total_score: int) -> BorrowerClass:
        """
        Determine classification from total score.

        Args:
            total_score: Sum of credit and experience scores

        Returns:
            BorrowerClass enum value
        """
        if total_score >= self.CLASS_A_PLUS_MIN:
            return BorrowerClass.A_PLUS
        elif total_score >= self.CLASS_A_MIN:
            return BorrowerClass.A
        elif total_score >= self.CLASS_B_MIN:
            return BorrowerClass.B
        else:
            return BorrowerClass.C

    def classify_borrower(
        self,
        fico: int,
        deals_36mo: int,
        is_foreign_national: bool = False
    ) -> BorrowerClassification:
        """
        Complete borrower classification.

        Args:
            fico: Credit score
            deals_36mo: Verified deals in last 36 months
            is_foreign_national: Foreign national status

        Returns:
            BorrowerClassification with all details
        """
        credit_score = self.calculate_credit_score_points(fico, is_foreign_national)
        experience_score = self.calculate_experience_points(deals_36mo)
        total_score = credit_score + experience_score
        classification = self.get_classification(total_score)

        return BorrowerClassification(
            fico_score=fico,
            credit_decision_score=credit_score,
            verified_experience=deals_36mo,
            experience_score=experience_score,
            total_score=total_score,
            classification=classification,
            is_foreign_national=is_foreign_national
        )


class RTLSizer:
    """
    Calculate RTL loan sizing with all constraints.

    Implements the full RTL sizing methodology per USDV Guidelines
    including leverage matrices, reductions, and constraint analysis.
    """

    # Base leverage matrices
    FF_PURCHASE_LEVERAGE: Dict[BorrowerClass, Dict[str, float]] = {
        BorrowerClass.A_PLUS: {'as_is_ltv': 0.90, 'ltc': 0.90, 'ltarv': 0.75},
        BorrowerClass.A: {'as_is_ltv': 0.85, 'ltc': 0.85, 'ltarv': 0.70},
        BorrowerClass.B: {'as_is_ltv': 0.825, 'ltc': 0.825, 'ltarv': 0.65},
        BorrowerClass.C: {'as_is_ltv': 0.75, 'ltc': 0.75, 'ltarv': 0.60},
    }

    FF_RT_REFI_LEVERAGE: Dict[BorrowerClass, Dict[str, float]] = {
        BorrowerClass.A_PLUS: {'as_is_ltv': 0.75, 'ltc': None, 'ltarv': 0.65},
        BorrowerClass.A: {'as_is_ltv': 0.725, 'ltc': None, 'ltarv': 0.65},
        BorrowerClass.B: {'as_is_ltv': 0.70, 'ltc': None, 'ltarv': 0.60},
        BorrowerClass.C: {'as_is_ltv': 0.60, 'ltc': None, 'ltarv': 0.55},
    }

    FF_CASHOUT_LEVERAGE: Dict[BorrowerClass, Dict[str, float]] = {
        BorrowerClass.A_PLUS: {'as_is_ltv': 0.70, 'ltc': None, 'ltarv': 0.65},
        BorrowerClass.A: {'as_is_ltv': 0.675, 'ltc': None, 'ltarv': 0.65},
        BorrowerClass.B: {'as_is_ltv': 0.65, 'ltc': None, 'ltarv': 0.60},
        BorrowerClass.C: {'as_is_ltv': None, 'ltc': None, 'ltarv': None},
    }

    BRIDGE_PURCHASE_LEVERAGE: Dict[BorrowerClass, Dict[str, float]] = {
        BorrowerClass.A_PLUS: {'as_is_ltv': 0.825, 'ltc': 0.825, 'ltarv': None},
        BorrowerClass.A: {'as_is_ltv': 0.80, 'ltc': 0.80, 'ltarv': None},
        BorrowerClass.B: {'as_is_ltv': 0.80, 'ltc': 0.80, 'ltarv': None},
        BorrowerClass.C: {'as_is_ltv': 0.75, 'ltc': 0.75, 'ltarv': None},
    }

    BRIDGE_RT_REFI_LEVERAGE: Dict[BorrowerClass, Dict[str, float]] = {
        BorrowerClass.A_PLUS: {'as_is_ltv': 0.775, 'ltc': None, 'ltarv': None},
        BorrowerClass.A: {'as_is_ltv': 0.75, 'ltc': None, 'ltarv': None},
        BorrowerClass.B: {'as_is_ltv': 0.75, 'ltc': None, 'ltarv': None},
        BorrowerClass.C: {'as_is_ltv': 0.65, 'ltc': None, 'ltarv': None},
    }

    BRIDGE_CASHOUT_LEVERAGE: Dict[BorrowerClass, Dict[str, float]] = {
        BorrowerClass.A_PLUS: {'as_is_ltv': 0.725, 'ltc': None, 'ltarv': None},
        BorrowerClass.A: {'as_is_ltv': 0.70, 'ltc': None, 'ltarv': None},
        BorrowerClass.B: {'as_is_ltv': 0.70, 'ltc': None, 'ltarv': None},
        BorrowerClass.C: {'as_is_ltv': 0.60, 'ltc': None, 'ltarv': None},
    }

    BRIDGE_PLUS_PURCHASE_LEVERAGE: Dict[BorrowerClass, Dict[str, float]] = {
        BorrowerClass.A_PLUS: {'as_is_ltv': 0.775, 'ltc': 0.775, 'ltarv': None},
        BorrowerClass.A: {'as_is_ltv': 0.75, 'ltc': 0.75, 'ltarv': None},
        BorrowerClass.B: {'as_is_ltv': 0.75, 'ltc': 0.75, 'ltarv': None},
        BorrowerClass.C: {'as_is_ltv': 0.70, 'ltc': 0.70, 'ltarv': None},
    }

    GUC_LEVERAGE = {
        'as_is_ltv': 0.70,  # Land value
        'ltc': 0.85,
        'ltarv': 0.675,
    }

    # Reduction factors
    HEAVY_REHAB_REDUCTION_AB = 0.05
    HEAVY_REHAB_REDUCTION_C = 0.10
    HPA_DECLINE_REDUCTION = 0.05
    ZHVI_MULTIPLIER_REDUCTION = 0.05
    HIGH_LOAN_AMOUNT_REDUCTION = 0.05
    SMALL_MF_REDUCTION_RTL = 0.05
    SMALL_MF_REDUCTION_GUC = 0.10

    # Thresholds
    HEAVY_REHAB_MIN_BUDGET = 50000
    HIGH_LOAN_AMOUNT_THRESHOLD = 2000000
    MAX_LOAN_AMOUNT = 3000000
    MIN_LOAN_AMOUNT = 100000
    MAX_REHAB_PERCENTAGE = 0.60
    MAX_ASSIGNMENT_FEE_PERCENT = 0.05
    MAX_ASSIGNMENT_FEE_DOLLARS = 40000
    MIN_FICO = 660

    def __init__(self):
        """Initialize the RTL Sizer."""
        self.classifier = BorrowerClassifier()

    def get_leverage_matrix(
        self,
        product: LoanProduct,
        purpose: LoanPurpose
    ) -> Dict[BorrowerClass, Dict[str, float]]:
        """
        Get the appropriate leverage matrix.

        Args:
            product: Loan product type
            purpose: Loan purpose

        Returns:
            Leverage matrix dictionary
        """
        if product == LoanProduct.FIX_AND_FLIP:
            if purpose == LoanPurpose.PURCHASE:
                return self.FF_PURCHASE_LEVERAGE
            elif purpose == LoanPurpose.RATE_TERM_REFINANCE:
                return self.FF_RT_REFI_LEVERAGE
            else:
                return self.FF_CASHOUT_LEVERAGE

        elif product == LoanProduct.BRIDGE:
            if purpose == LoanPurpose.PURCHASE:
                return self.BRIDGE_PURCHASE_LEVERAGE
            elif purpose == LoanPurpose.RATE_TERM_REFINANCE:
                return self.BRIDGE_RT_REFI_LEVERAGE
            else:
                return self.BRIDGE_CASHOUT_LEVERAGE

        elif product == LoanProduct.BRIDGE_PLUS:
            if purpose == LoanPurpose.PURCHASE:
                return self.BRIDGE_PLUS_PURCHASE_LEVERAGE
            elif purpose == LoanPurpose.RATE_TERM_REFINANCE:
                # Use same as purchase for simplicity
                return {
                    BorrowerClass.A_PLUS: {'as_is_ltv': 0.725, 'ltc': None, 'ltarv': None},
                    BorrowerClass.A: {'as_is_ltv': 0.70, 'ltc': None, 'ltarv': None},
                    BorrowerClass.B: {'as_is_ltv': 0.70, 'ltc': None, 'ltarv': None},
                    BorrowerClass.C: {'as_is_ltv': 0.60, 'ltc': None, 'ltarv': None},
                }
            else:
                return {
                    BorrowerClass.A_PLUS: {'as_is_ltv': 0.675, 'ltc': None, 'ltarv': None},
                    BorrowerClass.A: {'as_is_ltv': 0.65, 'ltc': None, 'ltarv': None},
                    BorrowerClass.B: {'as_is_ltv': 0.65, 'ltc': None, 'ltarv': None},
                    BorrowerClass.C: {'as_is_ltv': 0.55, 'ltc': None, 'ltarv': None},
                }

        # GUC uses fixed leverage, not class-based
        return {}

    def is_heavy_rehab(
        self,
        rehab_budget: float,
        purchase_price: float,
        as_is_value: float,
        is_purchase: bool
    ) -> bool:
        """
        Determine if project qualifies as heavy rehab.

        Args:
            rehab_budget: Total rehabilitation budget
            purchase_price: Purchase price (for purchases)
            as_is_value: Current appraised value
            is_purchase: Whether this is a purchase transaction

        Returns:
            True if heavy rehab criteria met
        """
        if rehab_budget <= self.HEAVY_REHAB_MIN_BUDGET:
            return False

        comparison_value = purchase_price if is_purchase else as_is_value

        if comparison_value <= 0:
            return False

        return rehab_budget > comparison_value

    def calculate_leverage_reductions(
        self,
        classification: BorrowerClass,
        product: LoanProduct,
        is_heavy_rehab: bool,
        hpa_decline: float,
        zhvi_multiplier: float,
        loan_amount: float,
        units: int
    ) -> Tuple[float, List[str]]:
        """
        Calculate total leverage reduction.

        Args:
            classification: Borrower classification
            product: Loan product
            is_heavy_rehab: Heavy rehab flag
            hpa_decline: HPA decline percentage (negative = decline)
            zhvi_multiplier: Property value / ZHVI ratio
            loan_amount: Estimated loan amount
            units: Number of units

        Returns:
            Tuple of (total_reduction, list of reduction descriptions)
        """
        total_reduction = 0.0
        reductions = []

        # Heavy rehab reduction
        if is_heavy_rehab:
            if classification == BorrowerClass.C:
                total_reduction += self.HEAVY_REHAB_REDUCTION_C
                reductions.append(f"Heavy Rehab (Class C): -{self.HEAVY_REHAB_REDUCTION_C*100:.1f}%")
            else:
                total_reduction += self.HEAVY_REHAB_REDUCTION_AB
                reductions.append(f"Heavy Rehab (Class A/B): -{self.HEAVY_REHAB_REDUCTION_AB*100:.1f}%")

        # HPA decline reduction
        if -0.10 <= hpa_decline < 0:
            total_reduction += self.HPA_DECLINE_REDUCTION
            reductions.append(f"HPA Decline ({hpa_decline*100:.1f}%): -{self.HPA_DECLINE_REDUCTION*100:.1f}%")

        # ZHVI multiplier reduction
        if 2.0 <= zhvi_multiplier <= 3.0:
            total_reduction += self.ZHVI_MULTIPLIER_REDUCTION
            reductions.append(f"ZHVI Multiplier ({zhvi_multiplier:.1f}x): -{self.ZHVI_MULTIPLIER_REDUCTION*100:.1f}%")

        # High loan amount reduction
        if self.HIGH_LOAN_AMOUNT_THRESHOLD <= loan_amount <= self.MAX_LOAN_AMOUNT:
            total_reduction += self.HIGH_LOAN_AMOUNT_REDUCTION
            reductions.append(f"Loan Amount ${loan_amount:,.0f}: -{self.HIGH_LOAN_AMOUNT_REDUCTION*100:.1f}%")

        # Small multifamily reduction
        if 5 <= units <= 9:
            if product == LoanProduct.GROUND_UP_CONSTRUCTION:
                total_reduction += self.SMALL_MF_REDUCTION_GUC
                reductions.append(f"5-9 Unit GUC: -{self.SMALL_MF_REDUCTION_GUC*100:.1f}%")
            else:
                total_reduction += self.SMALL_MF_REDUCTION_RTL
                reductions.append(f"5-9 Unit RTL: -{self.SMALL_MF_REDUCTION_RTL*100:.1f}%")

        return (total_reduction, reductions)

    def get_leverage_limits(
        self,
        classification: BorrowerClass,
        product: LoanProduct,
        purpose: LoanPurpose,
        total_reduction: float,
        reductions: List[str]
    ) -> LeverageLimits:
        """
        Get adjusted leverage limits.

        Args:
            classification: Borrower classification
            product: Loan product
            purpose: Loan purpose
            total_reduction: Total reduction to apply
            reductions: List of reduction descriptions

        Returns:
            LeverageLimits with adjusted values
        """
        if product == LoanProduct.GROUND_UP_CONSTRUCTION:
            base_limits = self.GUC_LEVERAGE
            return LeverageLimits(
                max_as_is_ltv=max(0, base_limits['as_is_ltv'] - total_reduction),
                max_ltc=max(0, base_limits['ltc'] - total_reduction) if base_limits['ltc'] else None,
                max_ltarv=max(0, base_limits['ltarv'] - total_reduction) if base_limits['ltarv'] else None,
                reductions_applied=reductions,
                total_reduction=total_reduction
            )

        matrix = self.get_leverage_matrix(product, purpose)
        base_limits = matrix.get(classification, {})

        if not base_limits or base_limits.get('as_is_ltv') is None:
            return LeverageLimits(
                max_as_is_ltv=0,
                max_ltc=None,
                max_ltarv=None,
                reductions_applied=["Scenario not eligible"],
                total_reduction=0
            )

        return LeverageLimits(
            max_as_is_ltv=max(0, base_limits['as_is_ltv'] - total_reduction),
            max_ltc=max(0, base_limits['ltc'] - total_reduction) if base_limits.get('ltc') else None,
            max_ltarv=max(0, base_limits['ltarv'] - total_reduction) if base_limits.get('ltarv') else None,
            reductions_applied=reductions,
            total_reduction=total_reduction
        )

    def calculate_cost_basis(
        self,
        purchase_price: float,
        closing_costs: float,
        assignment_fee: float,
        is_purchase: bool,
        completed_rehab: float = 0
    ) -> CostBasis:
        """
        Calculate cost basis for LTC calculation.

        Args:
            purchase_price: Property purchase price
            closing_costs: HUD closing costs (excl. origination)
            assignment_fee: Assignment fee amount
            is_purchase: Whether this is a purchase
            completed_rehab: Completed rehab (for refinance)

        Returns:
            CostBasis with calculation details
        """
        # Cap assignment fee
        max_assignment = min(
            assignment_fee,
            purchase_price * self.MAX_ASSIGNMENT_FEE_PERCENT,
            self.MAX_ASSIGNMENT_FEE_DOLLARS
        )

        if is_purchase:
            total = purchase_price + closing_costs + max_assignment
            method = "Purchase: PP + Closing + Assignment"
        else:
            total = purchase_price + completed_rehab
            method = "Refinance: Original PP + Completed Rehab"

        return CostBasis(
            purchase_price=purchase_price,
            closing_costs=closing_costs if is_purchase else 0,
            assignment_fee=max_assignment if is_purchase else 0,
            completed_rehab=completed_rehab if not is_purchase else 0,
            total_cost_basis=total,
            calculation_method=method
        )

    def calculate_rehab_holdback(
        self,
        rehab_budget: float,
        total_loan_tentative: float
    ) -> float:
        """
        Calculate rehab holdback with 60% rule.

        Args:
            rehab_budget: Requested rehab budget
            total_loan_tentative: Tentative total loan amount

        Returns:
            Maximum rehab holdback allowed
        """
        max_rehab = total_loan_tentative * self.MAX_REHAB_PERCENTAGE
        return min(rehab_budget, max_rehab)

    def size_loan(
        self,
        # Borrower
        fico: int,
        deals_36mo: int,
        is_foreign_national: bool,
        # Property
        as_is_value: float,
        arv: Optional[float],
        units: int,
        # Deal
        product: LoanProduct,
        purpose: LoanPurpose,
        purchase_price: float,
        closing_costs: float,
        assignment_fee: float,
        rehab_budget: float,
        completed_rehab: float,
        # Market
        hpa_decline: float = 0.0,
        zhvi_multiplier: float = 1.0
    ) -> RTLSizingResult:
        """
        Complete RTL loan sizing analysis.

        Args:
            fico: Credit score
            deals_36mo: Verified experience
            is_foreign_national: FN status
            as_is_value: Current property value
            arv: After-repair value (if applicable)
            units: Number of units
            product: Loan product type
            purpose: Loan purpose
            purchase_price: Purchase price
            closing_costs: Closing costs
            assignment_fee: Assignment fee
            rehab_budget: Rehab budget
            completed_rehab: Completed rehab (for refi)
            hpa_decline: HPA decline (negative = decline)
            zhvi_multiplier: Value/ZHVI ratio

        Returns:
            Complete RTLSizingResult
        """
        ineligibility_reasons = []
        notes = []

        # Step 1: Classify borrower
        classification = self.classifier.classify_borrower(
            fico, deals_36mo, is_foreign_national
        )

        # Check minimum FICO
        if fico < self.MIN_FICO:
            ineligibility_reasons.append(f"FICO {fico} below minimum {self.MIN_FICO}")

        # Step 2: Calculate cost basis
        is_purchase = purpose == LoanPurpose.PURCHASE
        cost_basis = self.calculate_cost_basis(
            purchase_price=purchase_price,
            closing_costs=closing_costs,
            assignment_fee=assignment_fee,
            is_purchase=is_purchase,
            completed_rehab=completed_rehab
        )

        # Step 3: Determine heavy rehab
        heavy_rehab = self.is_heavy_rehab(
            rehab_budget=rehab_budget,
            purchase_price=purchase_price,
            as_is_value=as_is_value,
            is_purchase=is_purchase
        )

        if heavy_rehab:
            notes.append("Heavy Rehab: Budget exceeds $50K and 100% of base value")

        # Step 4: Calculate leverage reductions
        # Use estimated loan for high loan amount check
        estimated_loan = as_is_value * 0.80  # Rough estimate

        total_reduction, reductions = self.calculate_leverage_reductions(
            classification=classification.classification,
            product=product,
            is_heavy_rehab=heavy_rehab,
            hpa_decline=hpa_decline,
            zhvi_multiplier=zhvi_multiplier,
            loan_amount=estimated_loan,
            units=units
        )

        # Step 5: Get leverage limits
        limits = self.get_leverage_limits(
            classification=classification.classification,
            product=product,
            purpose=purpose,
            total_reduction=total_reduction,
            reductions=reductions
        )

        if limits.max_as_is_ltv <= 0:
            ineligibility_reasons.append("Scenario not eligible for this classification")

        # Step 6: Calculate constraints
        constraints = []

        # As-Is LTV constraint
        if limits.max_as_is_ltv > 0 and as_is_value > 0:
            as_is_max = as_is_value * limits.max_as_is_ltv
            constraints.append(SizingConstraint(
                constraint_type="as_is_ltv",
                base_value=as_is_value,
                max_percentage=limits.max_as_is_ltv,
                max_loan_amount=as_is_max,
                actual_percentage=0,  # Set later
                is_binding=False
            ))

        # LTC constraint (purchase only)
        if limits.max_ltc and cost_basis.total_cost_basis > 0:
            ltc_max = cost_basis.total_cost_basis * limits.max_ltc
            constraints.append(SizingConstraint(
                constraint_type="ltc",
                base_value=cost_basis.total_cost_basis,
                max_percentage=limits.max_ltc,
                max_loan_amount=ltc_max,
                actual_percentage=0,
                is_binding=False
            ))

        # Step 7: Calculate initial loan (min of constraints)
        initial_constraints = [c for c in constraints]

        if not initial_constraints:
            initial_loan = 0
        else:
            initial_loan = min(c.max_loan_amount for c in initial_constraints)

        # Step 8: Calculate with rehab and LTARV
        rehab_holdback = 0.0

        if rehab_budget > 0 and product == LoanProduct.FIX_AND_FLIP:
            # Iterative calculation for rehab
            tentative_total = initial_loan + rehab_budget
            rehab_holdback = self.calculate_rehab_holdback(rehab_budget, tentative_total)
            total_loan = initial_loan + rehab_holdback

            # Check LTARV constraint
            if limits.max_ltarv and arv and arv > 0:
                max_total_from_arv = arv * limits.max_ltarv

                if total_loan > max_total_from_arv:
                    # LTARV constrains - recalculate
                    total_loan = max_total_from_arv

                    # Determine split between initial and rehab
                    max_rehab_from_total = total_loan * self.MAX_REHAB_PERCENTAGE
                    rehab_holdback = min(rehab_budget, max_rehab_from_total)
                    initial_loan = total_loan - rehab_holdback

                    constraints.append(SizingConstraint(
                        constraint_type="ltarv",
                        base_value=arv,
                        max_percentage=limits.max_ltarv,
                        max_loan_amount=max_total_from_arv,
                        actual_percentage=total_loan / arv if arv > 0 else 0,
                        is_binding=True
                    ))
        else:
            total_loan = initial_loan

        # Step 9: Determine binding constraint
        binding = "as_is_ltv"
        min_amount = float('inf')

        for c in constraints:
            if c.max_loan_amount < min_amount:
                min_amount = c.max_loan_amount
                binding = c.constraint_type
                c.is_binding = True
            else:
                c.is_binding = False

        # Step 10: Calculate actual metrics
        actual_as_is_ltv = initial_loan / as_is_value if as_is_value > 0 else 0
        actual_ltc = initial_loan / cost_basis.total_cost_basis if cost_basis.total_cost_basis > 0 else None
        actual_ltarv = total_loan / arv if arv and arv > 0 else None

        # Update constraint actual percentages
        for c in constraints:
            if c.constraint_type == "as_is_ltv":
                c.actual_percentage = actual_as_is_ltv
            elif c.constraint_type == "ltc":
                c.actual_percentage = actual_ltc if actual_ltc else 0
            elif c.constraint_type == "ltarv":
                c.actual_percentage = actual_ltarv if actual_ltarv else 0

        # Step 11: Final eligibility checks
        if total_loan < self.MIN_LOAN_AMOUNT:
            ineligibility_reasons.append(f"Loan amount ${total_loan:,.0f} below minimum ${self.MIN_LOAN_AMOUNT:,.0f}")

        if total_loan > self.MAX_LOAN_AMOUNT:
            ineligibility_reasons.append(f"Loan amount ${total_loan:,.0f} exceeds maximum ${self.MAX_LOAN_AMOUNT:,.0f}")

        if zhvi_multiplier > 3.0:
            ineligibility_reasons.append(f"ZHVI Multiplier {zhvi_multiplier:.1f}x exceeds maximum 300%")

        if hpa_decline < -0.10:
            ineligibility_reasons.append(f"HPA decline {hpa_decline*100:.1f}% exceeds maximum -10%")

        is_eligible = len(ineligibility_reasons) == 0

        return RTLSizingResult(
            product=product,
            purpose=purpose,
            borrower_classification=classification,
            as_is_value=as_is_value,
            arv=arv,
            cost_basis=cost_basis,
            leverage_limits=limits,
            constraints=constraints,
            binding_constraint=binding,
            initial_loan_amount=round(initial_loan, 2),
            rehab_holdback=round(rehab_holdback, 2),
            total_loan_amount=round(total_loan, 2),
            actual_as_is_ltv=round(actual_as_is_ltv, 4),
            actual_ltc=round(actual_ltc, 4) if actual_ltc else None,
            actual_ltarv=round(actual_ltarv, 4) if actual_ltarv else None,
            is_eligible=is_eligible,
            ineligibility_reasons=ineligibility_reasons,
            notes=notes
        )


# Convenience functions

def quick_classification(fico: int, deals: int, is_fn: bool = False) -> str:
    """Quick borrower classification lookup."""
    classifier = BorrowerClassifier()
    result = classifier.classify_borrower(fico, deals, is_fn)
    return result.classification.value


def quick_max_ltv(
    classification: str,
    product: str,
    purpose: str
) -> float:
    """Quick max LTV lookup without reductions."""
    sizer = RTLSizer()

    class_map = {
        'A+': BorrowerClass.A_PLUS,
        'A': BorrowerClass.A,
        'B': BorrowerClass.B,
        'C': BorrowerClass.C
    }

    product_map = {
        'fix_and_flip': LoanProduct.FIX_AND_FLIP,
        'bridge': LoanProduct.BRIDGE,
        'bridge_plus': LoanProduct.BRIDGE_PLUS,
        'guc': LoanProduct.GROUND_UP_CONSTRUCTION
    }

    purpose_map = {
        'purchase': LoanPurpose.PURCHASE,
        'rate_term': LoanPurpose.RATE_TERM_REFINANCE,
        'cash_out': LoanPurpose.CASH_OUT_REFINANCE
    }

    limits = sizer.get_leverage_limits(
        classification=class_map.get(classification, BorrowerClass.B),
        product=product_map.get(product, LoanProduct.FIX_AND_FLIP),
        purpose=purpose_map.get(purpose, LoanPurpose.PURCHASE),
        total_reduction=0,
        reductions=[]
    )

    return limits.max_as_is_ltv
```

---

## 9.10 Flag Generation Rules (INSPIRE Phase 7)

The following flags are generated during automated RTL sizing analysis:

### 9.10.1 Classification Flags

| Check | Pass (Green) | Warning (Yellow) | Fail (Red) |
|-------|-------------|------------------|-----------|
| FICO Score | >= 700 | 660-699 | < 660 |
| Experience | >= 3 deals | 1-2 deals | 0 deals |
| Classification | A+ or A | B | C |

### 9.10.2 Leverage Flags

| Check | Pass (Green) | Warning (Yellow) | Fail (Red) |
|-------|-------------|------------------|-----------|
| As-Is LTV | < Max - 5% | Within Max | > Max |
| LTC | < Max - 5% | Within Max | > Max |
| LTARV | < Max - 5% | Within Max | > Max |
| Rehab % | < 50% | 50-60% | > 60% |

### 9.10.3 Market Condition Flags

| Check | Pass (Green) | Warning (Yellow) | Fail (Red) |
|-------|-------------|------------------|-----------|
| HPA | Positive | 0% to -10% | < -10% |
| ZHVI Multiplier | < 200% | 200-300% | > 300% |
| Days on Market | < 90 | 90-180 | > 180 |

---

## 9.11 Cross-References

| Topic | Reference Section |
|-------|------------------|
| Borrower Eligibility Details | Section 2: Borrower Eligibility & Classification |
| Credit Requirements | Section 4: Credit & Background Evaluation |
| Property Eligibility | Section 5: Property Eligibility Standards |
| RTL Property Analysis | Section 6: RTL Property Analysis |
| Pricing Calculations | Section 11: Pricing & Rate Calculations |
| Document Requirements | Section 13: Document Requirements |

---

## 9.12 Open Questions

1. **GUC Experience Verification:** Confirm whether GC license experience counts toward the 3-deal minimum for GUC products.

2. **ZHVI Data Source:** Confirm whether Zillow API or manual lookup is used for ZHVI/HPA data in INSPIRE.

3. **Leverage Reduction Caps:** Determine if there's a maximum cumulative reduction (e.g., can't reduce below 60% LTV even with multiple reductions).

---

*End of Section 9: RTL Loan Sizing & Leverage*
