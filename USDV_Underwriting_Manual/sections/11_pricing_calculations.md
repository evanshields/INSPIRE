---
section: 11
title: Pricing & Rate Calculations
version: 1.0
last_updated: 2025-12-30
model_used: opus
guideline_sources:
  - Eastview DSCR Guidelines v7.2
  - EV DSCR S Matrix 12.29.25
  - Archwest RTL Guidelines
  - Archwest DSCR Guidelines v1.8
changelog:
  - 2025-12-30: Initial creation
---

# Section 11: Pricing & Rate Calculations

## 11.1 Overview

Pricing determines the interest rate and associated costs for each loan. The pricing methodology differs significantly between RTL (transitional) and DSCR (permanent) products. RTL pricing is primarily driven by borrower classification and loan characteristics, while DSCR pricing utilizes a sophisticated Loan Level Price Adjustment (LLPA) system based on multiple risk factors.

**INSPIRE Integration Points:**
- Phase 3-4: Quote generation, pricing calculations, rate lock management
- Phase 4: Final rate determination and term sheet generation

---

## 11.2 RTL Pricing Framework

### 11.2.1 Base Rate Structure

RTL loans (Fix & Flip, Bridge, Ground-Up Construction) are priced using a base rate plus adjustments based on borrower classification and deal characteristics.

**Base Rate Components:**
```
RTL Interest Rate = Base Rate + Classification Adjustment + Risk Adjustments
```

### 11.2.2 Rate by Borrower Classification

| Classification | Base Rate Range | Typical Spread |
|----------------|-----------------|----------------|
| A+ | 9.00% - 10.50% | +0.00% |
| A | 9.50% - 11.00% | +0.50% |
| B | 10.00% - 11.50% | +1.00% |
| C | 10.50% - 12.50% | +1.50% - 2.00% |

**Note:** Actual rates vary based on market conditions and the current rate environment.

### 11.2.3 RTL Rate Adjustments

| Condition | Rate Adjustment |
|-----------|-----------------|
| Heavy Rehab Project | +0.25% - 0.50% |
| Ground-Up Construction | +0.50% - 1.00% |
| Loan Amount $2M - $3M | +0.25% |
| 5-9 Unit Property | +0.50% |
| Bridge Plus (25-36 months) | +0.25% |
| Cash-Out Refinance | +0.25% |
| First-Time Investor (Class B/C) | +0.50% |

### 11.2.4 RTL Points Structure

**Origination Points:**

| Loan Amount | Standard Points | Minimum Points |
|-------------|-----------------|----------------|
| $100K - $500K | 2.00% | 1.50% |
| $500K - $1M | 1.75% | 1.25% |
| $1M - $2M | 1.50% | 1.00% |
| $2M - $3M | 1.25% | 1.00% |

**Extension Fees:**
- First Extension (3 months): 1.00%
- Second Extension (3 months): 1.00%
- Maximum Extensions: 2 (Fix & Flip, GUC), 1 (Bridge)

### 11.2.5 RTL Pricing Example

**Scenario:**
- Borrower: Class A (FICO 720, 6 deals)
- Product: Fix & Flip Purchase
- Loan Amount: $350,000
- Heavy Rehab: No

**Calculation:**
```
Base Rate: 10.00%
Classification Adjustment (Class A): +0.00%
Risk Adjustments: None

Final Rate: 10.00%
Origination Points: 2.00% × $350,000 = $7,000
```

---

## 11.3 DSCR Pricing Framework

### 11.3.1 Price-Based System

DSCR loans use a price-based system where the final rate is determined by:

1. **Base Price** - Determined by the spread over the 5-Year Treasury
2. **LLPAs (Loan Level Price Adjustments)** - Cumulative adjustments based on risk factors
3. **Final Price** - Base Price + Sum of All LLPAs
4. **Final Rate** - Derived from the price-to-rate conversion table

```
Final Price = Base Price + FICO LLPA + DSCR LLPA + Property LLPA + Loan Size LLPA + Prepay LLPA + Other LLPAs
```

### 11.3.2 Base Rate/Price Table

The base rate is determined by the spread over the 5-Year Treasury yield:

| Spread (5YR) | Coupon | 5/1 ARM Price | 7/1 ARM Price | Fixed 30 Price |
|--------------|--------|---------------|---------------|----------------|
| 4.320% | 8.000% | 105.616% | 105.616% | 105.616% |
| 4.195% | 7.875% | 105.187% | 105.187% | 105.187% |
| 4.070% | 7.750% | 104.758% | 104.758% | 104.758% |
| 3.945% | 7.625% | 104.330% | 104.330% | 104.330% |
| 3.820% | 7.500% | 103.903% | 103.903% | 103.903% |
| 3.695% | 7.375% | 103.477% | 103.477% | 103.477% |
| 3.570% | 7.250% | 103.051% | 103.051% | 103.051% |
| 3.445% | 7.125% | 102.626% | 102.626% | 102.626% |
| 3.320% | 7.000% | 102.201% | 102.201% | 102.201% |
| 3.195% | 6.875% | 101.777% | 101.777% | 101.777% |
| 3.070% | 6.750% | 101.354% | 101.354% | 101.354% |
| 2.945% | 6.625% | 100.932% | 100.932% | 100.932% |
| 2.820% | 6.500% | 100.510% | 100.510% | 100.510% |
| 2.695% | 6.375% | 100.090% | 100.090% | 100.090% |
| 2.570% | 6.250% | 99.420% | 99.420% | 99.420% |
| 2.445% | 6.125% | 98.876% | 98.876% | 98.876% |
| 2.320% | 6.000% | 98.332% | 98.332% | 98.332% |

**Price Constraints:**
- Minimum Price: 97.000%
- Maximum Price: 104.500%
- Maximum Price (Prepay < 3 Year): 102.000%

---

## 11.4 FICO-Based LLPAs

The FICO LLPA is the primary credit-based price adjustment. LLPAs vary by both FICO score tier and LTV.

### 11.4.1 Complete FICO LLPA Matrix

| FICO Score | 50% LTV | 55% LTV | 60% LTV | 65% LTV | 70% LTV | 75% LTV | 80% LTV |
|------------|---------|---------|---------|---------|---------|---------|---------|
| 780+ | +1.000% | +0.875% | +0.750% | +0.625% | +0.500% | +0.375% | +0.125% |
| 760-779 | +0.875% | +0.750% | +0.625% | +0.500% | +0.375% | +0.250% | +0.000% |
| 740-759 | +0.750% | +0.625% | +0.500% | +0.375% | +0.250% | +0.125% | -0.125% |
| 720-739 | +0.675% | +0.500% | +0.375% | +0.250% | +0.125% | +0.000% | -0.250% |
| 700-719 | +0.500% | +0.375% | +0.250% | +0.125% | +0.000% | -0.250% | -0.500% |
| 680-699 | +0.375% | +0.250% | +0.125% | -0.250% | -0.750% | -1.000% | N/A |
| 660-679 | +0.000% | -0.375% | -0.625% | -1.125% | -1.850% | N/A | N/A |
| Foreign National | +0.000% | -0.375% | -0.625% | -1.125% | -1.850% | N/A | N/A |

**Key Observations:**
- Higher FICO scores receive better pricing (positive LLPAs = price credits)
- Lower LTV tiers receive better pricing
- FICO 680-699 is not eligible at 80% LTV
- FICO 660-679 is not eligible above 70% LTV
- Foreign Nationals use the same matrix as FICO 660-679

### 11.4.2 FICO Determination for Pricing

| Scenario | FICO Used for Pricing |
|----------|----------------------|
| Single Guarantor | Median of three scores (or lower of two) |
| Multiple Guarantors (equal ownership) | Higher qualifying score |
| Multiple Guarantors (unequal ownership) | Score of highest ownership percentage guarantor |
| 51% Recourse Structure | Highest median score among guarantors |

---

## 11.5 DSCR-Based LLPAs

DSCR LLPAs adjust pricing based on the property's debt service coverage ratio.

### 11.5.1 DSCR LLPA Matrix

| DSCR Range | 50% LTV | 55% LTV | 60% LTV | 65% LTV | 70% LTV | 75% LTV | 80% LTV |
|------------|---------|---------|---------|---------|---------|---------|---------|
| 0.80 ≤ DSCR < 1.00 | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| 1.00 ≤ DSCR < 1.10 | +0.000% | +0.000% | +0.000% | +0.000% | -0.125% | -0.250% | -0.375% |
| DSCR ≥ 1.15 | +0.500% | +0.500% | +0.500% | +0.500% | +0.500% | +0.500% | +0.500% |

**Key Points:**
- DSCR below 1.00x is not eligible
- DSCR between 1.00x and 1.10x has pricing hits at higher LTVs
- DSCR ≥ 1.15x receives a 0.50% price credit across all LTV tiers

---

## 11.6 Loan Size LLPAs

Loan size affects pricing due to operational costs and risk concentration.

### 11.6.1 Loan Size LLPA Matrix

| Loan Size | 50% LTV | 55% LTV | 60% LTV | 65% LTV | 70% LTV | 75% LTV | 80% LTV |
|-----------|---------|---------|---------|---------|---------|---------|---------|
| UPB ≤ $150,000 | +0.000% | +0.000% | +0.000% | +0.000% | -0.250% | -0.500% | -1.000% |
| $2,000,000 < UPB ≤ $3,000,000 | -0.500% | -0.500% | -0.750% | -1.750% | -2.000% | -3.000% | N/A |

**Key Points:**
- Small loans (≤$150K) have pricing hits at higher LTVs
- Large loans ($2M-$3M) have significant pricing hits, especially at higher LTVs
- Loans $2M-$3M are not eligible at 80% LTV

---

## 11.7 Property Type LLPAs

Property type affects pricing based on marketability and risk profile.

### 11.7.1 Property Type LLPA Matrix

| Property Type | 50% LTV | 55% LTV | 60% LTV | 65% LTV | 70% LTV | 75% LTV | 80% LTV |
|---------------|---------|---------|---------|---------|---------|---------|---------|
| SFR/Townhome | +0.000% | +0.000% | +0.000% | +0.000% | +0.000% | +0.000% | +0.000% |
| Condo (Warrantable) | +0.000% | +0.000% | +0.000% | +0.000% | -0.250% | -0.500% | -1.000% |
| Condo (Non-Warrantable) | -0.500% | -0.500% | -0.500% | -0.500% | -0.500% | N/A | N/A |
| 2-4 Unit | +0.000% | +0.000% | +0.000% | +0.000% | -0.250% | -0.500% | -1.000% |
| 5-9 Unit | -4.000% | -4.250% | -4.500% | -5.375% | -6.000% | -7.500% | N/A |

**Key Points:**
- SFR and Townhomes have no property type LLPA
- Condos have pricing hits at higher LTVs
- Non-warrantable condos are not eligible above 70% LTV
- 5-9 unit properties have significant pricing hits and are not eligible at 80% LTV

---

## 11.8 Transaction Type LLPAs

### 11.8.1 Cash-Out Refinance LLPA

| Transaction | 50% LTV | 55% LTV | 60% LTV | 65% LTV | 70% LTV | 75% LTV | 80% LTV |
|-------------|---------|---------|---------|---------|---------|---------|---------|
| Cash-Out Refinance | +0.000% | +0.000% | +0.000% | -0.250% | -0.375% | -0.375% | -6.000% |

**Cash-Out Definition:**
- Net receivable funds at closing > 2% of loan amount, OR
- Net receivable funds at closing ≥ $2,000

**Rate & Term Definition:**
- Net receivable funds at closing ≤ 2% of loan amount, AND
- Net receivable funds at closing < $2,000

---

## 11.9 Interest-Only LLPAs

Interest-only (I/O) loans have pricing adjustments based on LTV.

### 11.9.1 Interest-Only LLPA Matrix

| LTV Range | I/O LLPA |
|-----------|----------|
| ≤ 65% | +0.000% |
| 70% | -0.250% |
| 75% | -0.375% |
| 80% | -0.750% |

**I/O Term Options:**
- Standard: 10-year I/O with 20-year amortization
- Other terms available with management approval

---

## 11.10 Prepayment Penalty LLPAs

Prepayment penalty structure significantly impacts pricing. Longer prepayment terms provide better pricing.

### 11.10.1 Prepayment Penalty LLPA Matrix

| Prepayment Structure | LLPA (All LTVs) |
|---------------------|-----------------|
| 7 Year (84 Months) Minimum Interest | +2.000% |
| 7 Year Step-down (7%/6%/5%/4%/3%/2%/1%) | +1.750% |
| 5 Year (60 Months) Minimum Interest | +0.750% |
| 5 Year Step-down (5%/4%/3%/2%/1%) | +0.500% |
| 3 Year Step-down (3%/2%/1%) | +0.000% |
| 2 Year Step-down (2%/1%) | -1.000% |
| 1 Year (1%) | -2.000% |
| No Prepayment Penalty | -4.000% |

**Prepayment Structure Descriptions:**

| Structure | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 | Year 6 | Year 7 |
|-----------|--------|--------|--------|--------|--------|--------|--------|
| 7-Year Step-down | 7% | 6% | 5% | 4% | 3% | 2% | 1% |
| 5-Year Step-down | 5% | 4% | 3% | 2% | 1% | - | - |
| 3-Year Step-down | 3% | 2% | 1% | - | - | - | - |
| 2-Year Step-down | 2% | 1% | - | - | - | - | - |
| 1-Year | 1% | - | - | - | - | - | - |

**Minimum Interest Calculation:**
- Penalty = Outstanding Balance × Interest Rate × Remaining Months / 12

---

## 11.11 Portfolio/Cross-Collateralized LLPAs

### 11.11.1 Cross-Collateralized Portfolio LLPA

| Scenario | 50% LTV | 55% LTV | 60% LTV | 65% LTV | 70% LTV | 75% LTV | 80% LTV |
|----------|---------|---------|---------|---------|---------|---------|---------|
| Cross-Collateralized Portfolio | -0.125% | -0.125% | -0.125% | -0.125% | -0.250% | -0.250% | -0.500% |

---

## 11.12 Complete LLPA Summary Table

| LLPA Category | Typical Range | Notes |
|---------------|---------------|-------|
| FICO | +1.000% to -1.850% | Varies by FICO tier and LTV |
| DSCR | +0.500% to -0.375% | Credit for DSCR ≥ 1.15x |
| Loan Size (Small) | +0.000% to -1.000% | ≤$150K at high LTV |
| Loan Size (Large) | -0.500% to -3.000% | $2M-$3M |
| Property Type | +0.000% to -7.500% | 5-9 units most impactful |
| Cash-Out | +0.000% to -6.000% | Significant at 80% LTV |
| Interest-Only | +0.000% to -0.750% | Based on LTV |
| Prepayment | +2.000% to -4.000% | Longest term = best price |
| Portfolio | -0.125% to -0.500% | Cross-collateralized |

---

## 11.13 Price-to-Rate Conversion

### 11.13.1 Conversion Methodology

The final interest rate is determined by finding the price in the rate sheet that most closely matches the calculated final price.

**Process:**
1. Calculate Final Price = Base Price + Sum of All LLPAs
2. Locate the closest price in the rate sheet
3. The corresponding coupon is the final interest rate

**Example:**
```
Base Price (7.250% coupon): 103.051%
FICO LLPA (720, 70% LTV): +0.125%
DSCR LLPA (1.18x): +0.500%
Prepay LLPA (5-year step-down): +0.500%
Property Type (SFR): +0.000%
Cash-Out (No): +0.000%
I/O (70% LTV): -0.250%

Final Price = 103.051% + 0.125% + 0.500% + 0.500% + 0.000% + 0.000% - 0.250%
Final Price = 103.926%

Closest price in rate sheet: 103.903% (7.500% coupon)

Final Rate: 7.500%
```

### 11.13.2 Price Rounding Rules

| Scenario | Rule |
|----------|------|
| Price between two rates | Round to nearest price |
| Price exactly between | Round to lower rate (borrower benefit) |
| Price exceeds maximum | Cap at maximum price |
| Price below minimum | Floor at minimum price |

---

## 11.14 USDV Economics

### 11.14.1 Origination Fee Structure

| Loan Type | Standard Points | Range |
|-----------|-----------------|-------|
| RTL | 2.00% | 1.00% - 3.00% |
| DSCR | 1.50% | 1.00% - 2.50% |

### 11.14.2 Yield Spread Premium (YSP)

YSP represents the premium paid to USDV for delivering loans at above-par pricing.

**YSP Calculation:**
```
YSP = (Final Price - 100.00%) × Loan Amount

Example:
Final Price: 103.50%
Loan Amount: $400,000
YSP = (103.50% - 100.00%) × $400,000 = $14,000
```

### 11.14.3 All-In Economics Example

**DSCR Loan:**
- Loan Amount: $400,000
- Final Price: 103.50%
- Origination Points: 1.50%

```
Origination Fee = $400,000 × 1.50% = $6,000
YSP = $400,000 × 3.50% = $14,000
Total USDV Revenue = $6,000 + $14,000 = $20,000
```

---

## 11.15 Rate Lock Management

### 11.15.1 Lock Periods

| Lock Period | Cost | Notes |
|-------------|------|-------|
| 30 Days | Included | Standard lock |
| 45 Days | +0.125% | Extended lock |
| 60 Days | +0.250% | Extended lock |
| 90 Days | +0.500% | Maximum lock |

### 11.15.2 Lock Extensions

| Extension | Cost | Maximum |
|-----------|------|---------|
| 15-Day Extension | 0.15% (15 bps) | Multiple extensions allowed |
| 30-Day Extension | 0.30% (30 bps) | Subject to approval |

### 11.15.3 Lock Expiration Handling

| Scenario | Action |
|----------|--------|
| Lock expires, rates improved | Re-lock at current (better) pricing |
| Lock expires, rates worsened | Re-lock at current (worse) pricing |
| Lock expires, deal not closed | Extension required or re-lock |

### 11.15.4 Rate Lock Data Structure

```python
@dataclass
class RateLock:
    """Rate lock information."""
    deal_id: str
    locked_rate: float
    locked_price: float
    lock_date: date
    expiration_date: date
    lock_period_days: int
    extension_cost: float
    status: str  # 'active', 'expired', 'exercised'
    extensions: List[RateLockExtension]
```

---

## 11.16 ARM Pricing Specifications

### 11.16.1 ARM Parameters

| Parameter | 5/1 ARM | 7/1 ARM |
|-----------|---------|---------|
| Fixed Period | 5 years | 7 years |
| Adjustment Frequency | Annual | Annual |
| Index | 30-Day Average SOFR | 30-Day Average SOFR |
| Margin | 5.00% | 5.00% |
| Initial Cap | 2% | 5% |
| Periodic Cap | 2% | 2% |
| Lifetime Cap | 5% | 5% |
| Floor | Margin (5.00%) | Margin (5.00%) |
| Lookback Days | 45 | 45 |
| Rounding Method | Up | Up |
| Rounding Factor | 0.125% | 0.125% |

### 11.16.2 ARM Rate Adjustment Example

**5/1 ARM at Year 6:**
```
Index (30-Day SOFR): 4.25%
Margin: 5.00%
Calculated Rate: 4.25% + 5.00% = 9.25%

Previous Rate: 7.50%
Initial Cap: 2%
Maximum Adjusted Rate: 7.50% + 2% = 9.50%

Since 9.25% < 9.50%, New Rate = 9.25%

Rounded: 9.25% (already at 0.125% increment)
```

---

## 11.17 Complete DSCR Pricing Example

### 11.17.1 Scenario

**Borrower:**
- FICO: 735
- Foreign National: No

**Property:**
- Type: Single Family Residence
- Value: $450,000
- Units: 1

**Loan:**
- Amount: $337,500 (75% LTV)
- Purpose: Purchase
- DSCR: 1.22x
- Rate Type: Fixed 30
- Prepayment: 5-Year Step-down
- Interest Only: Yes (10-year)

### 11.17.2 LLPA Calculation

| LLPA Category | Lookup | Value |
|---------------|--------|-------|
| Base Price (7.250% coupon) | Rate sheet | 103.051% |
| FICO LLPA (720-739, 75% LTV) | FICO matrix | +0.000% |
| DSCR LLPA (≥1.15x) | DSCR matrix | +0.500% |
| Loan Size LLPA | N/A (standard size) | +0.000% |
| Property Type LLPA (SFR) | Property matrix | +0.000% |
| Cash-Out LLPA (No) | Transaction matrix | +0.000% |
| Interest-Only LLPA (75% LTV) | I/O matrix | -0.375% |
| Prepayment LLPA (5-yr step-down) | Prepay matrix | +0.500% |

**Final Price Calculation:**
```
Final Price = 103.051% + 0.000% + 0.500% + 0.000% + 0.000% + 0.000% - 0.375% + 0.500%
Final Price = 103.676%
```

**Rate Determination:**
- Closest price in rate sheet: 103.903% → 7.500%
- Alternative: 103.477% → 7.375%
- Final Rate: **7.375%** (closer to 103.676%)

### 11.17.3 Economics Summary

| Item | Value |
|------|-------|
| Loan Amount | $337,500 |
| Interest Rate | 7.375% |
| Final Price | 103.676% |
| YSP | $337,500 × 3.676% = $12,407 |
| Origination (1.5%) | $5,063 |
| Total USDV Revenue | $17,470 |

---

## 11.18 Python Implementation

```python
"""
Pricing & Rate Calculations Module
USDV Capital Underwriting Library

This module provides comprehensive pricing functionality for both
RTL and DSCR loans, including LLPA calculations, price-to-rate
conversion, and rate lock management.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List, Dict, Tuple
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
import bisect


class RateType(Enum):
    """Interest rate type."""
    FIXED_30 = "fixed_30"
    ARM_5_1 = "5_1_arm"
    ARM_7_1 = "7_1_arm"


class PrepaymentStructure(Enum):
    """Prepayment penalty structure."""
    SEVEN_YEAR_MIN_INTEREST = "7yr_min_interest"
    SEVEN_YEAR_STEPDOWN = "7yr_stepdown"
    FIVE_YEAR_MIN_INTEREST = "5yr_min_interest"
    FIVE_YEAR_STEPDOWN = "5yr_stepdown"
    THREE_YEAR_STEPDOWN = "3yr_stepdown"
    TWO_YEAR_STEPDOWN = "2yr_stepdown"
    ONE_YEAR = "1yr"
    NO_PREPAY = "no_prepay"


class LoanPurpose(Enum):
    """Loan purpose for pricing."""
    PURCHASE = "purchase"
    RATE_TERM_REFINANCE = "rate_term_refinance"
    CASH_OUT_REFINANCE = "cash_out_refinance"


class PropertyType(Enum):
    """Property type for pricing."""
    SFR = "sfr"
    TOWNHOME = "townhome"
    CONDO_WARRANTABLE = "condo_warrantable"
    CONDO_NON_WARRANTABLE = "condo_non_warrantable"
    TWO_TO_FOUR_UNIT = "2_4_unit"
    FIVE_TO_NINE_UNIT = "5_9_unit"


@dataclass
class LLPABreakdown:
    """Detailed breakdown of all LLPAs."""
    fico_llpa: float
    dscr_llpa: float
    loan_size_llpa: float
    property_type_llpa: float
    cash_out_llpa: float
    interest_only_llpa: float
    prepayment_llpa: float
    portfolio_llpa: float
    other_llpas: Dict[str, float] = field(default_factory=dict)
    
    @property
    def total_llpa(self) -> float:
        """Calculate total LLPA."""
        base = (
            self.fico_llpa +
            self.dscr_llpa +
            self.loan_size_llpa +
            self.property_type_llpa +
            self.cash_out_llpa +
            self.interest_only_llpa +
            self.prepayment_llpa +
            self.portfolio_llpa
        )
        return base + sum(self.other_llpas.values())


@dataclass
class DSCRPricingResult:
    """Complete DSCR pricing result."""
    # Inputs
    fico: int
    ltv: float
    dscr: float
    loan_amount: float
    property_type: PropertyType
    loan_purpose: LoanPurpose
    rate_type: RateType
    prepayment: PrepaymentStructure
    is_interest_only: bool
    is_portfolio: bool
    is_foreign_national: bool
    
    # Pricing
    base_price: float
    base_coupon: float
    llpa_breakdown: LLPABreakdown
    final_price: float
    final_rate: float
    
    # Economics
    ysp: float
    ysp_amount: float
    
    # Eligibility
    is_eligible: bool
    ineligibility_reasons: List[str] = field(default_factory=list)
    
    # Notes
    notes: List[str] = field(default_factory=list)


@dataclass
class RateLockExtension:
    """Rate lock extension record."""
    extension_date: date
    days_extended: int
    cost_bps: float
    new_expiration: date


@dataclass
class RateLock:
    """Rate lock information."""
    deal_id: str
    locked_rate: float
    locked_price: float
    lock_date: date
    expiration_date: date
    lock_period_days: int
    lock_cost_bps: float
    status: str  # 'active', 'expired', 'exercised'
    extensions: List[RateLockExtension] = field(default_factory=list)
    
    @property
    def total_extension_cost(self) -> float:
        """Calculate total extension cost in bps."""
        return sum(ext.cost_bps for ext in self.extensions)
    
    @property
    def days_remaining(self) -> int:
        """Calculate days remaining until expiration."""
        return (self.expiration_date - date.today()).days


class DSCRPricingEngine:
    """
    Calculate DSCR loan pricing with all LLPAs.
    
    Implements the full DSCR pricing methodology per USDV Guidelines
    including FICO, DSCR, property type, and prepayment LLPAs.
    """
    
    # Rate sheet: spread -> (coupon, price)
    RATE_SHEET = [
        (4.320, 8.000, 105.616),
        (4.195, 7.875, 105.187),
        (4.070, 7.750, 104.758),
        (3.945, 7.625, 104.330),
        (3.820, 7.500, 103.903),
        (3.695, 7.375, 103.477),
        (3.570, 7.250, 103.051),
        (3.445, 7.125, 102.626),
        (3.320, 7.000, 102.201),
        (3.195, 6.875, 101.777),
        (3.070, 6.750, 101.354),
        (2.945, 6.625, 100.932),
        (2.820, 6.500, 100.510),
        (2.695, 6.375, 100.090),
        (2.570, 6.250, 99.420),
        (2.445, 6.125, 98.876),
        (2.320, 6.000, 98.332),
    ]
    
    # Price constraints
    MIN_PRICE = 97.000
    MAX_PRICE = 104.500
    MAX_PRICE_SHORT_PREPAY = 102.000
    
    # FICO LLPA Matrix: FICO tier -> LTV tier -> LLPA
    FICO_LLPA_MATRIX = {
        '780+': {50: 1.000, 55: 0.875, 60: 0.750, 65: 0.625, 70: 0.500, 75: 0.375, 80: 0.125},
        '760-779': {50: 0.875, 55: 0.750, 60: 0.625, 65: 0.500, 70: 0.375, 75: 0.250, 80: 0.000},
        '740-759': {50: 0.750, 55: 0.625, 60: 0.500, 65: 0.375, 70: 0.250, 75: 0.125, 80: -0.125},
        '720-739': {50: 0.675, 55: 0.500, 60: 0.375, 65: 0.250, 70: 0.125, 75: 0.000, 80: -0.250},
        '700-719': {50: 0.500, 55: 0.375, 60: 0.250, 65: 0.125, 70: 0.000, 75: -0.250, 80: -0.500},
        '680-699': {50: 0.375, 55: 0.250, 60: 0.125, 65: -0.250, 70: -0.750, 75: -1.000, 80: None},
        '660-679': {50: 0.000, 55: -0.375, 60: -0.625, 65: -1.125, 70: -1.850, 75: None, 80: None},
        'FN': {50: 0.000, 55: -0.375, 60: -0.625, 65: -1.125, 70: -1.850, 75: None, 80: None},
    }
    
    # DSCR LLPA Matrix
    DSCR_LLPA_MATRIX = {
        'below_1.00': {50: None, 55: None, 60: None, 65: None, 70: None, 75: None, 80: None},
        '1.00-1.10': {50: 0.000, 55: 0.000, 60: 0.000, 65: 0.000, 70: -0.125, 75: -0.250, 80: -0.375},
        '1.15+': {50: 0.500, 55: 0.500, 60: 0.500, 65: 0.500, 70: 0.500, 75: 0.500, 80: 0.500},
    }
    
    # Loan Size LLPA Matrix
    LOAN_SIZE_LLPA_MATRIX = {
        'small': {50: 0.000, 55: 0.000, 60: 0.000, 65: 0.000, 70: -0.250, 75: -0.500, 80: -1.000},
        'large': {50: -0.500, 55: -0.500, 60: -0.750, 65: -1.750, 70: -2.000, 75: -3.000, 80: None},
    }
    
    # Property Type LLPA Matrix
    PROPERTY_TYPE_LLPA_MATRIX = {
        PropertyType.SFR: {50: 0.000, 55: 0.000, 60: 0.000, 65: 0.000, 70: 0.000, 75: 0.000, 80: 0.000},
        PropertyType.TOWNHOME: {50: 0.000, 55: 0.000, 60: 0.000, 65: 0.000, 70: 0.000, 75: 0.000, 80: 0.000},
        PropertyType.CONDO_WARRANTABLE: {50: 0.000, 55: 0.000, 60: 0.000, 65: 0.000, 70: -0.250, 75: -0.500, 80: -1.000},
        PropertyType.CONDO_NON_WARRANTABLE: {50: -0.500, 55: -0.500, 60: -0.500, 65: -0.500, 70: -0.500, 75: None, 80: None},
        PropertyType.TWO_TO_FOUR_UNIT: {50: 0.000, 55: 0.000, 60: 0.000, 65: 0.000, 70: -0.250, 75: -0.500, 80: -1.000},
        PropertyType.FIVE_TO_NINE_UNIT: {50: -4.000, 55: -4.250, 60: -4.500, 65: -5.375, 70: -6.000, 75: -7.500, 80: None},
    }
    
    # Cash-Out LLPA Matrix
    CASHOUT_LLPA_MATRIX = {
        50: 0.000, 55: 0.000, 60: 0.000, 65: -0.250, 70: -0.375, 75: -0.375, 80: -6.000
    }
    
    # Interest-Only LLPA Matrix
    IO_LLPA_MATRIX = {
        50: 0.000, 55: 0.000, 60: 0.000, 65: 0.000, 70: -0.250, 75: -0.375, 80: -0.750
    }
    
    # Prepayment LLPA
    PREPAY_LLPA = {
        PrepaymentStructure.SEVEN_YEAR_MIN_INTEREST: 2.000,
        PrepaymentStructure.SEVEN_YEAR_STEPDOWN: 1.750,
        PrepaymentStructure.FIVE_YEAR_MIN_INTEREST: 0.750,
        PrepaymentStructure.FIVE_YEAR_STEPDOWN: 0.500,
        PrepaymentStructure.THREE_YEAR_STEPDOWN: 0.000,
        PrepaymentStructure.TWO_YEAR_STEPDOWN: -1.000,
        PrepaymentStructure.ONE_YEAR: -2.000,
        PrepaymentStructure.NO_PREPAY: -4.000,
    }
    
    # Portfolio LLPA Matrix
    PORTFOLIO_LLPA_MATRIX = {
        50: -0.125, 55: -0.125, 60: -0.125, 65: -0.125, 70: -0.250, 75: -0.250, 80: -0.500
    }
    
    def get_fico_tier(self, fico: int, is_foreign_national: bool) -> str:
        """
        Determine FICO tier for LLPA lookup.
        
        Args:
            fico: Credit score
            is_foreign_national: FN status
            
        Returns:
            FICO tier string
        """
        if is_foreign_national:
            return 'FN'
        
        if fico >= 780:
            return '780+'
        elif fico >= 760:
            return '760-779'
        elif fico >= 740:
            return '740-759'
        elif fico >= 720:
            return '720-739'
        elif fico >= 700:
            return '700-719'
        elif fico >= 680:
            return '680-699'
        elif fico >= 660:
            return '660-679'
        else:
            return 'below_660'
    
    def get_ltv_tier(self, ltv: float) -> int:
        """
        Determine LTV tier for LLPA lookup.
        
        Args:
            ltv: Loan-to-value ratio (as decimal, e.g., 0.75)
            
        Returns:
            LTV tier (50, 55, 60, 65, 70, 75, or 80)
        """
        ltv_pct = ltv * 100 if ltv <= 1 else ltv
        
        if ltv_pct <= 50:
            return 50
        elif ltv_pct <= 55:
            return 55
        elif ltv_pct <= 60:
            return 60
        elif ltv_pct <= 65:
            return 65
        elif ltv_pct <= 70:
            return 70
        elif ltv_pct <= 75:
            return 75
        else:
            return 80
    
    def get_dscr_tier(self, dscr: float) -> str:
        """
        Determine DSCR tier for LLPA lookup.
        
        Args:
            dscr: Debt service coverage ratio
            
        Returns:
            DSCR tier string
        """
        if dscr < 1.00:
            return 'below_1.00'
        elif dscr < 1.10:
            return '1.00-1.10'
        elif dscr >= 1.15:
            return '1.15+'
        else:
            return '1.10-1.15'  # No LLPA for this range
    
    def get_fico_llpa(
        self,
        fico: int,
        ltv: float,
        is_foreign_national: bool
    ) -> Tuple[Optional[float], bool]:
        """
        Get FICO-based LLPA.
        
        Args:
            fico: Credit score
            ltv: Loan-to-value ratio
            is_foreign_national: FN status
            
        Returns:
            Tuple of (LLPA value, is_eligible)
        """
        fico_tier = self.get_fico_tier(fico, is_foreign_national)
        ltv_tier = self.get_ltv_tier(ltv)
        
        if fico_tier == 'below_660':
            return (None, False)
        
        matrix = self.FICO_LLPA_MATRIX.get(fico_tier, {})
        llpa = matrix.get(ltv_tier)
        
        if llpa is None:
            return (None, False)
        
        return (llpa, True)
    
    def get_dscr_llpa(self, dscr: float, ltv: float) -> Tuple[float, bool]:
        """
        Get DSCR-based LLPA.
        
        Args:
            dscr: Debt service coverage ratio
            ltv: Loan-to-value ratio
            
        Returns:
            Tuple of (LLPA value, is_eligible)
        """
        dscr_tier = self.get_dscr_tier(dscr)
        ltv_tier = self.get_ltv_tier(ltv)
        
        if dscr_tier == 'below_1.00':
            return (None, False)
        
        if dscr_tier == '1.10-1.15':
            return (0.0, True)  # No LLPA
        
        matrix = self.DSCR_LLPA_MATRIX.get(dscr_tier, {})
        llpa = matrix.get(ltv_tier)
        
        if llpa is None:
            return (None, False)
        
        return (llpa, True)
    
    def get_loan_size_llpa(self, loan_amount: float, ltv: float) -> Tuple[float, bool]:
        """
        Get loan size LLPA.
        
        Args:
            loan_amount: Loan amount
            ltv: Loan-to-value ratio
            
        Returns:
            Tuple of (LLPA value, is_eligible)
        """
        ltv_tier = self.get_ltv_tier(ltv)
        
        if loan_amount <= 150000:
            matrix = self.LOAN_SIZE_LLPA_MATRIX['small']
        elif loan_amount > 2000000:
            matrix = self.LOAN_SIZE_LLPA_MATRIX['large']
        else:
            return (0.0, True)
        
        llpa = matrix.get(ltv_tier)
        
        if llpa is None:
            return (None, False)
        
        return (llpa, True)
    
    def get_property_type_llpa(
        self,
        property_type: PropertyType,
        ltv: float
    ) -> Tuple[float, bool]:
        """
        Get property type LLPA.
        
        Args:
            property_type: Property type
            ltv: Loan-to-value ratio
            
        Returns:
            Tuple of (LLPA value, is_eligible)
        """
        ltv_tier = self.get_ltv_tier(ltv)
        matrix = self.PROPERTY_TYPE_LLPA_MATRIX.get(property_type, {})
        llpa = matrix.get(ltv_tier)
        
        if llpa is None:
            return (None, False)
        
        return (llpa, True)
    
    def get_cashout_llpa(self, is_cashout: bool, ltv: float) -> float:
        """
        Get cash-out refinance LLPA.
        
        Args:
            is_cashout: Whether this is a cash-out refinance
            ltv: Loan-to-value ratio
            
        Returns:
            LLPA value
        """
        if not is_cashout:
            return 0.0
        
        ltv_tier = self.get_ltv_tier(ltv)
        return self.CASHOUT_LLPA_MATRIX.get(ltv_tier, 0.0)
    
    def get_io_llpa(self, is_io: bool, ltv: float) -> float:
        """
        Get interest-only LLPA.
        
        Args:
            is_io: Whether loan is interest-only
            ltv: Loan-to-value ratio
            
        Returns:
            LLPA value
        """
        if not is_io:
            return 0.0
        
        ltv_tier = self.get_ltv_tier(ltv)
        return self.IO_LLPA_MATRIX.get(ltv_tier, 0.0)
    
    def get_prepay_llpa(self, prepay_structure: PrepaymentStructure) -> float:
        """
        Get prepayment penalty LLPA.
        
        Args:
            prepay_structure: Prepayment penalty structure
            
        Returns:
            LLPA value
        """
        return self.PREPAY_LLPA.get(prepay_structure, 0.0)
    
    def get_portfolio_llpa(self, is_portfolio: bool, ltv: float) -> float:
        """
        Get portfolio/cross-collateralized LLPA.
        
        Args:
            is_portfolio: Whether this is a cross-collateralized portfolio
            ltv: Loan-to-value ratio
            
        Returns:
            LLPA value
        """
        if not is_portfolio:
            return 0.0
        
        ltv_tier = self.get_ltv_tier(ltv)
        return self.PORTFOLIO_LLPA_MATRIX.get(ltv_tier, 0.0)
    
    def get_base_price(self, target_coupon: float) -> Tuple[float, float]:
        """
        Get base price for target coupon.
        
        Args:
            target_coupon: Target interest rate coupon
            
        Returns:
            Tuple of (coupon, price)
        """
        # Find closest coupon in rate sheet
        for spread, coupon, price in self.RATE_SHEET:
            if abs(coupon - target_coupon) < 0.001:
                return (coupon, price)
        
        # If not exact match, find closest
        closest = min(self.RATE_SHEET, key=lambda x: abs(x[1] - target_coupon))
        return (closest[1], closest[2])
    
    def price_to_rate(self, final_price: float) -> float:
        """
        Convert final price to interest rate.
        
        Args:
            final_price: Calculated final price
            
        Returns:
            Interest rate (coupon)
        """
        # Find closest price in rate sheet
        prices = [(entry[2], entry[1]) for entry in self.RATE_SHEET]
        prices.sort(key=lambda x: x[0])
        
        closest = min(prices, key=lambda x: abs(x[0] - final_price))
        return closest[1]
    
    def calculate_all_llpas(
        self,
        fico: int,
        ltv: float,
        dscr: float,
        loan_amount: float,
        property_type: PropertyType,
        loan_purpose: LoanPurpose,
        prepayment: PrepaymentStructure,
        is_interest_only: bool,
        is_portfolio: bool,
        is_foreign_national: bool
    ) -> Tuple[LLPABreakdown, bool, List[str]]:
        """
        Calculate all LLPAs for a loan.
        
        Args:
            fico: Credit score
            ltv: Loan-to-value ratio
            dscr: Debt service coverage ratio
            loan_amount: Loan amount
            property_type: Property type
            loan_purpose: Loan purpose
            prepayment: Prepayment structure
            is_interest_only: I/O flag
            is_portfolio: Portfolio flag
            is_foreign_national: FN flag
            
        Returns:
            Tuple of (LLPABreakdown, is_eligible, ineligibility_reasons)
        """
        ineligibility_reasons = []
        
        # FICO LLPA
        fico_llpa, fico_eligible = self.get_fico_llpa(fico, ltv, is_foreign_national)
        if not fico_eligible:
            ineligibility_reasons.append(
                f"FICO {fico} not eligible at {ltv*100:.0f}% LTV"
            )
            fico_llpa = 0.0
        
        # DSCR LLPA
        dscr_llpa, dscr_eligible = self.get_dscr_llpa(dscr, ltv)
        if not dscr_eligible:
            ineligibility_reasons.append(f"DSCR {dscr:.2f}x below minimum 1.00x")
            dscr_llpa = 0.0
        
        # Loan Size LLPA
        size_llpa, size_eligible = self.get_loan_size_llpa(loan_amount, ltv)
        if not size_eligible:
            ineligibility_reasons.append(
                f"Loan amount ${loan_amount:,.0f} not eligible at {ltv*100:.0f}% LTV"
            )
            size_llpa = 0.0
        
        # Property Type LLPA
        prop_llpa, prop_eligible = self.get_property_type_llpa(property_type, ltv)
        if not prop_eligible:
            ineligibility_reasons.append(
                f"Property type {property_type.value} not eligible at {ltv*100:.0f}% LTV"
            )
            prop_llpa = 0.0
        
        # Cash-Out LLPA
        is_cashout = loan_purpose == LoanPurpose.CASH_OUT_REFINANCE
        cashout_llpa = self.get_cashout_llpa(is_cashout, ltv)
        
        # I/O LLPA
        io_llpa = self.get_io_llpa(is_interest_only, ltv)
        
        # Prepayment LLPA
        prepay_llpa = self.get_prepay_llpa(prepayment)
        
        # Portfolio LLPA
        portfolio_llpa = self.get_portfolio_llpa(is_portfolio, ltv)
        
        breakdown = LLPABreakdown(
            fico_llpa=fico_llpa or 0.0,
            dscr_llpa=dscr_llpa or 0.0,
            loan_size_llpa=size_llpa or 0.0,
            property_type_llpa=prop_llpa or 0.0,
            cash_out_llpa=cashout_llpa,
            interest_only_llpa=io_llpa,
            prepayment_llpa=prepay_llpa,
            portfolio_llpa=portfolio_llpa
        )
        
        is_eligible = len(ineligibility_reasons) == 0
        
        return (breakdown, is_eligible, ineligibility_reasons)
    
    def calculate_pricing(
        self,
        fico: int,
        ltv: float,
        dscr: float,
        loan_amount: float,
        property_type: PropertyType,
        loan_purpose: LoanPurpose,
        rate_type: RateType,
        prepayment: PrepaymentStructure,
        is_interest_only: bool,
        is_portfolio: bool = False,
        is_foreign_national: bool = False,
        target_coupon: float = 7.250
    ) -> DSCRPricingResult:
        """
        Complete DSCR pricing calculation.
        
        Args:
            fico: Credit score
            ltv: Loan-to-value ratio (as decimal)
            dscr: Debt service coverage ratio
            loan_amount: Loan amount
            property_type: Property type
            loan_purpose: Loan purpose
            rate_type: Rate type (Fixed, ARM)
            prepayment: Prepayment structure
            is_interest_only: I/O flag
            is_portfolio: Portfolio flag
            is_foreign_national: FN flag
            target_coupon: Target base coupon rate
            
        Returns:
            Complete DSCRPricingResult
        """
        notes = []
        
        # Get base price
        base_coupon, base_price = self.get_base_price(target_coupon)
        
        # Calculate all LLPAs
        llpa_breakdown, is_eligible, ineligibility_reasons = self.calculate_all_llpas(
            fico=fico,
            ltv=ltv,
            dscr=dscr,
            loan_amount=loan_amount,
            property_type=property_type,
            loan_purpose=loan_purpose,
            prepayment=prepayment,
            is_interest_only=is_interest_only,
            is_portfolio=is_portfolio,
            is_foreign_national=is_foreign_national
        )
        
        # Calculate final price
        final_price = base_price + llpa_breakdown.total_llpa
        
        # Apply price constraints
        max_price = self.MAX_PRICE
        if prepayment in [
            PrepaymentStructure.TWO_YEAR_STEPDOWN,
            PrepaymentStructure.ONE_YEAR,
            PrepaymentStructure.NO_PREPAY
        ]:
            max_price = self.MAX_PRICE_SHORT_PREPAY
            notes.append(f"Max price capped at {max_price}% for short prepay")
        
        if final_price > max_price:
            notes.append(f"Price capped from {final_price:.3f}% to {max_price}%")
            final_price = max_price
        
        if final_price < self.MIN_PRICE:
            notes.append(f"Price floored from {final_price:.3f}% to {self.MIN_PRICE}%")
            final_price = self.MIN_PRICE
        
        # Convert price to rate
        final_rate = self.price_to_rate(final_price)
        
        # Calculate YSP
        ysp = max(0, final_price - 100.0)
        ysp_amount = loan_amount * (ysp / 100)
        
        return DSCRPricingResult(
            fico=fico,
            ltv=ltv,
            dscr=dscr,
            loan_amount=loan_amount,
            property_type=property_type,
            loan_purpose=loan_purpose,
            rate_type=rate_type,
            prepayment=prepayment,
            is_interest_only=is_interest_only,
            is_portfolio=is_portfolio,
            is_foreign_national=is_foreign_national,
            base_price=base_price,
            base_coupon=base_coupon,
            llpa_breakdown=llpa_breakdown,
            final_price=round(final_price, 3),
            final_rate=final_rate,
            ysp=round(ysp, 3),
            ysp_amount=round(ysp_amount, 2),
            is_eligible=is_eligible,
            ineligibility_reasons=ineligibility_reasons,
            notes=notes
        )


class RTLPricingEngine:
    """
    Calculate RTL loan pricing.
    
    Implements RTL pricing methodology based on borrower
    classification and deal characteristics.
    """
    
    # Base rates by classification
    BASE_RATES = {
        'A+': 9.50,
        'A': 10.00,
        'B': 10.50,
        'C': 11.00,
    }
    
    # Rate adjustments
    ADJUSTMENTS = {
        'heavy_rehab': 0.50,
        'guc': 0.75,
        'high_loan_amount': 0.25,
        'multifamily_5_9': 0.50,
        'bridge_plus': 0.25,
        'cash_out': 0.25,
        'first_time_investor': 0.50,
    }
    
    # Origination points by loan amount
    ORIGINATION_POINTS = {
        500000: 2.00,
        1000000: 1.75,
        2000000: 1.50,
        3000000: 1.25,
    }
    
    def get_base_rate(self, classification: str) -> float:
        """Get base rate for borrower classification."""
        return self.BASE_RATES.get(classification, 11.00)
    
    def calculate_rate_adjustments(
        self,
        is_heavy_rehab: bool,
        is_guc: bool,
        loan_amount: float,
        units: int,
        is_bridge_plus: bool,
        is_cash_out: bool,
        is_first_time: bool
    ) -> Tuple[float, List[str]]:
        """
        Calculate rate adjustments.
        
        Returns:
            Tuple of (total_adjustment, list of adjustment descriptions)
        """
        total = 0.0
        adjustments = []
        
        if is_heavy_rehab:
            total += self.ADJUSTMENTS['heavy_rehab']
            adjustments.append(f"Heavy Rehab: +{self.ADJUSTMENTS['heavy_rehab']}%")
        
        if is_guc:
            total += self.ADJUSTMENTS['guc']
            adjustments.append(f"Ground-Up Construction: +{self.ADJUSTMENTS['guc']}%")
        
        if loan_amount >= 2000000:
            total += self.ADJUSTMENTS['high_loan_amount']
            adjustments.append(f"High Loan Amount: +{self.ADJUSTMENTS['high_loan_amount']}%")
        
        if 5 <= units <= 9:
            total += self.ADJUSTMENTS['multifamily_5_9']
            adjustments.append(f"5-9 Unit: +{self.ADJUSTMENTS['multifamily_5_9']}%")
        
        if is_bridge_plus:
            total += self.ADJUSTMENTS['bridge_plus']
            adjustments.append(f"Bridge Plus: +{self.ADJUSTMENTS['bridge_plus']}%")
        
        if is_cash_out:
            total += self.ADJUSTMENTS['cash_out']
            adjustments.append(f"Cash-Out: +{self.ADJUSTMENTS['cash_out']}%")
        
        if is_first_time:
            total += self.ADJUSTMENTS['first_time_investor']
            adjustments.append(f"First-Time Investor: +{self.ADJUSTMENTS['first_time_investor']}%")
        
        return (total, adjustments)
    
    def get_origination_points(self, loan_amount: float) -> float:
        """Get origination points for loan amount."""
        for threshold, points in sorted(self.ORIGINATION_POINTS.items()):
            if loan_amount <= threshold:
                return points
        return 1.25
    
    def calculate_pricing(
        self,
        classification: str,
        loan_amount: float,
        is_heavy_rehab: bool = False,
        is_guc: bool = False,
        units: int = 1,
        is_bridge_plus: bool = False,
        is_cash_out: bool = False,
        is_first_time: bool = False
    ) -> Dict:
        """
        Calculate RTL pricing.
        
        Returns:
            Dictionary with pricing details
        """
        base_rate = self.get_base_rate(classification)
        
        adjustment, adjustment_details = self.calculate_rate_adjustments(
            is_heavy_rehab=is_heavy_rehab,
            is_guc=is_guc,
            loan_amount=loan_amount,
            units=units,
            is_bridge_plus=is_bridge_plus,
            is_cash_out=is_cash_out,
            is_first_time=is_first_time
        )
        
        final_rate = base_rate + adjustment
        origination_points = self.get_origination_points(loan_amount)
        origination_fee = loan_amount * (origination_points / 100)
        
        return {
            'classification': classification,
            'base_rate': base_rate,
            'rate_adjustments': adjustment,
            'adjustment_details': adjustment_details,
            'final_rate': round(final_rate, 3),
            'origination_points': origination_points,
            'origination_fee': round(origination_fee, 2),
            'loan_amount': loan_amount,
        }


class RateLockManager:
    """
    Manage rate locks for deals.
    
    Handles lock creation, extensions, and expiration tracking.
    """
    
    # Lock period costs (bps)
    LOCK_COSTS = {
        30: 0,
        45: 12.5,
        60: 25,
        90: 50,
    }
    
    EXTENSION_COST_PER_15_DAYS = 15  # bps
    
    def create_lock(
        self,
        deal_id: str,
        rate: float,
        price: float,
        lock_days: int = 30
    ) -> RateLock:
        """
        Create a new rate lock.
        
        Args:
            deal_id: Deal identifier
            rate: Locked interest rate
            price: Locked price
            lock_days: Lock period in days
            
        Returns:
            RateLock object
        """
        lock_date = date.today()
        expiration = lock_date + timedelta(days=lock_days)
        lock_cost = self.LOCK_COSTS.get(lock_days, 50)
        
        return RateLock(
            deal_id=deal_id,
            locked_rate=rate,
            locked_price=price,
            lock_date=lock_date,
            expiration_date=expiration,
            lock_period_days=lock_days,
            lock_cost_bps=lock_cost,
            status='active',
            extensions=[]
        )
    
    def extend_lock(
        self,
        lock: RateLock,
        extension_days: int = 15
    ) -> RateLock:
        """
        Extend an existing rate lock.
        
        Args:
            lock: Existing RateLock
            extension_days: Days to extend
            
        Returns:
            Updated RateLock
        """
        cost_bps = (extension_days / 15) * self.EXTENSION_COST_PER_15_DAYS
        new_expiration = lock.expiration_date + timedelta(days=extension_days)
        
        extension = RateLockExtension(
            extension_date=date.today(),
            days_extended=extension_days,
            cost_bps=cost_bps,
            new_expiration=new_expiration
        )
        
        lock.extensions.append(extension)
        lock.expiration_date = new_expiration
        
        return lock
    
    def check_expiration(self, lock: RateLock) -> Dict:
        """
        Check lock expiration status.
        
        Returns:
            Dictionary with expiration details
        """
        days_remaining = lock.days_remaining
        
        if days_remaining < 0:
            status = 'expired'
            alert_level = 'critical'
        elif days_remaining <= 3:
            status = 'expiring_soon'
            alert_level = 'urgent'
        elif days_remaining <= 7:
            status = 'expiring'
            alert_level = 'warning'
        else:
            status = 'active'
            alert_level = 'normal'
        
        return {
            'status': status,
            'days_remaining': days_remaining,
            'alert_level': alert_level,
            'expiration_date': lock.expiration_date,
            'total_lock_cost': lock.lock_cost_bps + lock.total_extension_cost,
        }


# Convenience functions

def quick_dscr_price(
    fico: int,
    ltv: float,
    dscr: float,
    loan_amount: float,
    prepay_years: int = 5
) -> Tuple[float, float]:
    """
    Quick DSCR pricing lookup.
    
    Args:
        fico: Credit score
        ltv: LTV (as decimal)
        dscr: DSCR ratio
        loan_amount: Loan amount
        prepay_years: Prepayment term (3, 5, or 7)
        
    Returns:
        Tuple of (interest_rate, final_price)
    """
    engine = DSCRPricingEngine()
    
    prepay_map = {
        7: PrepaymentStructure.SEVEN_YEAR_STEPDOWN,
        5: PrepaymentStructure.FIVE_YEAR_STEPDOWN,
        3: PrepaymentStructure.THREE_YEAR_STEPDOWN,
    }
    
    result = engine.calculate_pricing(
        fico=fico,
        ltv=ltv,
        dscr=dscr,
        loan_amount=loan_amount,
        property_type=PropertyType.SFR,
        loan_purpose=LoanPurpose.PURCHASE,
        rate_type=RateType.FIXED_30,
        prepayment=prepay_map.get(prepay_years, PrepaymentStructure.FIVE_YEAR_STEPDOWN),
        is_interest_only=True
    )
    
    return (result.final_rate, result.final_price)


def quick_rtl_rate(
    classification: str,
    loan_amount: float,
    is_heavy_rehab: bool = False
) -> float:
    """
    Quick RTL rate lookup.
    
    Args:
        classification: Borrower classification (A+, A, B, C)
        loan_amount: Loan amount
        is_heavy_rehab: Heavy rehab flag
        
    Returns:
        Interest rate
    """
    engine = RTLPricingEngine()
    result = engine.calculate_pricing(
        classification=classification,
        loan_amount=loan_amount,
        is_heavy_rehab=is_heavy_rehab
    )
    return result['final_rate']
```

---

## 11.19 Flag Generation Rules (INSPIRE Phase 7)

The following flags are generated during automated pricing analysis:

### 11.19.1 Pricing Eligibility Flags

| Check | Pass (Green) | Warning (Yellow) | Fail (Red) |
|-------|-------------|------------------|-----------|
| FICO/LTV Eligibility | LLPA available | Edge of matrix | N/A in matrix |
| DSCR Eligibility | DSCR ≥ 1.00x | DSCR 1.00-1.10x | DSCR < 1.00x |
| Loan Size Eligibility | Standard size | Edge of range | Size/LTV N/A |
| Property Type Eligibility | Standard property | Non-warrantable | N/A at LTV |

### 11.19.2 Pricing Quality Flags

| Check | Pass (Green) | Warning (Yellow) | Fail (Red) |
|-------|-------------|------------------|-----------|
| Final Price | ≥ 100.00% | 98.00% - 99.99% | < 98.00% |
| Total LLPAs | Net positive | Neutral | Net > -2.00% |
| Rate vs Market | At or below market | Slightly above | Significantly above |

### 11.19.3 Rate Lock Flags

| Check | Pass (Green) | Warning (Yellow) | Fail (Red) |
|-------|-------------|------------------|-----------|
| Lock Status | Active, > 7 days | 3-7 days remaining | < 3 days or expired |
| Extension Count | 0-1 extensions | 2 extensions | 3+ extensions |

---

## 11.20 Cross-References

| Topic | Reference Section |
|-------|------------------|
| Borrower Classification | Section 2: Borrower Eligibility & Classification |
| DSCR Calculation | Section 7: DSCR Property & Income Analysis |
| RTL Leverage Limits | Section 9: RTL Loan Sizing & Leverage |
| DSCR Leverage Limits | Section 10: DSCR Loan Sizing & Leverage |
| Quote Generation | INSPIRE Phase 3-4 PRD |

---

## 11.21 Open Questions

1. **Rate Sheet Frequency:** Confirm how often the rate sheet is updated and whether INSPIRE should auto-refresh pricing data.

2. **YSP Calculation:** Verify whether YSP is calculated on the full price above par or only a portion.

3. **RTL Pricing Grid:** Confirm whether RTL uses a similar LLPA-based system or the simpler classification-based approach documented here.

4. **Housing Event LLPA:** The matrix shows "Housing Event 2-4 Years" - clarify whether this is an additional LLPA for borrowers with recent housing events within the seasoning period.

---

*End of Section 11: Pricing & Rate Calculations*

