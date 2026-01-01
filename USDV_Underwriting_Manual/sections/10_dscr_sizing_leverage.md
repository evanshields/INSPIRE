# Section 10: DSCR Loan Sizing & Leverage

## Document Control

| Field | Value |
|-------|-------|
| **Section Number** | 10 |
| **Section Title** | DSCR Loan Sizing & Leverage |
| **Document Version** | 2.0 |
| **Effective Date** | 2025-01-01 |
| **Last Reviewed** | 2024-12-30 |
| **Section Owner** | USDV Capital - Underwriting |
| **Classification** | Internal Use Only |
| **INSPIRE Integration** | Phase 3-4: DSCR Sizer Engine |
| **Related Sections** | Section 7 (DSCR Property Income), Section 11 (Pricing) |

---

## 10.1 DSCR Sizing Approach

### Overview

DSCR loan sizing determines the maximum loan amount a borrower can receive based on the property's income-generating capacity and the borrower's credit profile. Unlike RTL loans which focus on cost basis and exit value, DSCR loans are sized using a dual-constraint methodology that considers both collateral value (LTV) and debt service capacity (DSCR).

### Dual-Constraint Methodology

DSCR loan sizing employs two parallel constraints that work together to determine the maximum loan amount:

```
Maximum Loan Amount = MIN(LTV-Constrained Loan, DSCR-Constrained Loan)
```

#### Constraint 1: LTV-Constrained Maximum

The LTV-constrained maximum loan is determined by:

```
LTV-Constrained Loan = Property Value × Maximum LTV
```

Where:
- **Property Value** = Appraised "As-Is" value (or lesser of appraised value and purchase price for purchases within 6 months)
- **Maximum LTV** = Base LTV adjusted for all applicable leverage reductions

The Maximum LTV is calculated as:

```
Maximum LTV = Base LTV + Σ(Leverage Reductions)
```

#### Constraint 2: DSCR-Constrained Maximum

The DSCR-constrained maximum loan is the amount where the resulting DSCR equals the minimum required DSCR:

```
DSCR-Constrained Loan = Maximum loan where DSCR ≥ Minimum DSCR
```

This is calculated iteratively or algebraically by solving for the loan amount where:

```
Qualifying Rent / PITIA = Minimum DSCR
```

### Binding Constraint Determination

The binding constraint is whichever produces the lower maximum loan amount:

| Scenario | Binding Constraint | Implication |
|----------|-------------------|-------------|
| LTV-Constrained < DSCR-Constrained | LTV | Property value limits loan; DSCR exceeds minimum |
| DSCR-Constrained < LTV-Constrained | DSCR | Income limits loan; LTV below maximum allowed |
| LTV-Constrained = DSCR-Constrained | Both | Optimal sizing where both constraints are met exactly |

**INSPIRE Integration:** The DSCR Sizer Engine calculates both constraints in parallel and displays which constraint is binding, along with the "headroom" on the non-binding constraint.

---

## 10.2 Base LTV by FICO & Purpose

### FICO Tier Definitions

DSCR loans use FICO tiers to determine base leverage. The applicable FICO score is the **lowest middle score** among all guarantors (see Section 4 for credit scoring methodology).

| FICO Tier | FICO Range | Description |
|-----------|------------|-------------|
| Tier 1 | 780+ | Exceptional credit |
| Tier 2 | 760-779 | Excellent credit |
| Tier 3 | 740-759 | Very good credit |
| Tier 4 | 720-739 | Good credit |
| Tier 5 | 700-719 | Standard credit |
| Tier 6 | 680-699 | Acceptable credit |
| Tier 7 | 660-679 | Minimum standard |

**Note:** FICO scores below 660 are not eligible for DSCR loans under program guidelines.

### Base LTV Matrix

The following matrix establishes the base maximum LTV by FICO tier and loan purpose. This matrix synthesizes requirements across program guidelines to establish unified USDV standards:

| FICO Tier | Purchase | Rate & Term Refinance | Cash-Out Refinance |
|-----------|----------|----------------------|-------------------|
| **780+** | 80% | 80% | 80% |
| **760-779** | 80% | 80% | 80% |
| **740-759** | 80% | 80% | 80% |
| **720-739** | 80% | 80% | 80% |
| **700-719** | 80% | 80% | 75% |
| **680-699** | 75%* | 75%* | 70% |
| **660-679** | 70% | 70% | 65% |

*Note: While base LTV for 680-699 FICO is 75%, pricing availability (LLPAs) may restrict maximum LTV to 75% for certain scenarios. See Section 11 for pricing constraints.

### Maximum LTV by FICO (Pricing-Constrained)

The pricing matrix imposes additional LTV constraints based on LLPA availability:

| FICO Tier | Maximum LTV (Pricing Available) |
|-----------|--------------------------------|
| **780+** | 80% |
| **760-779** | 80% |
| **740-759** | 80% |
| **720-739** | 80% |
| **700-719** | 80% |
| **680-699** | 75% (N/A at 80%) |
| **660-679** | 70% (N/A at 75%+) |
| **Foreign National** | 70% (N/A at 75%+) |

### Purpose Definitions

| Loan Purpose | Definition | Documentation Required |
|--------------|------------|----------------------|
| **Purchase** | Acquisition of property within 6 months of loan origination | Purchase contract, HUD/settlement statement |
| **Rate & Term Refinance** | Refinance where borrower receives ≤2% of loan amount or <$2,000 net proceeds | Existing loan payoff, ownership documentation |
| **Cash-Out Refinance** | Refinance where borrower receives >2% of loan amount or ≥$2,000 net proceeds | Same as R&T plus use of funds statement |
| **Delayed Purchase** | Financing of property owned free & clear, acquired within 6 months | Settlement statement confirming no mortgage; max 120% LTC |

### Special FICO Tier Rules

#### 5-9 Unit Properties

For properties with 5-9 units, leverage is reduced and pricing constraints apply:

| Parameter | 1-4 Units | 5-9 Units |
|-----------|-----------|-----------|
| **Base LTV Reduction** | None | -5% from base |
| **Maximum LTV** | Per FICO tier | 75% maximum |
| **Pricing Availability** | All LTV tiers | N/A at 80% LTV |

#### Foreign National Borrowers

Foreign National borrowers are treated equivalently to the **660-679 FICO tier** for LTV purposes:

| Parameter | Standard Borrower | Foreign National |
|-----------|-------------------|------------------|
| **Base LTV (Purchase)** | Per FICO tier | 70% |
| **Base LTV (R&T Refi)** | Per FICO tier | 70% |
| **Base LTV (Cash-Out)** | Per FICO tier | 65% |
| **Maximum LTV** | Per FICO tier | 70% (pricing N/A at 75%+) |

**Note:** Foreign Nationals with DSCR ≥1.30x may qualify for +5% LTV increase (see Section 10.3).

---

## 10.3 Leverage Reductions & Adjustments

### Overview

Base LTV is adjusted based on various loan, property, and borrower characteristics. Leverage reductions are **cumulative** and applied to the base LTV to arrive at the maximum allowable LTV.

### Leverage Reduction Table

| Condition | Reduction | Notes |
|-----------|-----------|-------|
| **Unleased Refinance** | -10% | Property classified as "unleased" with refinance purpose (EastView standard) |
| **Non-Warrantable Condo** | -10% | Does not apply to pending litigation scenarios |
| **5-9 Units** | -5% | Multi-unit complexity |
| **Market-Specific (Chicago/Detroit/Baltimore/Flint)** | -5% | Higher-risk markets |
| **STR/Airbnb/VRBO** | -5% | Short-term rental income volatility |
| **Section 8 / Subsidized Leases** | -5% | Government program dependency |
| **Luxury Rental (>$1M UPB)** | -10% | Requires >1.20x DSCR, 12-month lease |

### LTV Increase Opportunities

Certain scenarios qualify for LTV increases:

| Condition | Increase | Requirements |
|-----------|----------|--------------|
| **700-719 FICO with DSCR ≥1.20x** | +5% | Strong debt service coverage offsets credit tier |
| **Foreign National with DSCR ≥1.30x** | +5% | Strong debt service coverage offsets FN risk |

### Leased vs. Unleased Determination

A property's lease status affects leverage. The following table defines minimum units required to be leased for a property to qualify as "leased":

| Property Type | Units Required to be Leased |
|---------------|----------------------------|
| SFR/Townhome/Condo/PUD | 1 |
| 2 Unit | 1 |
| 3 Unit | 2 |
| 4 Unit | 2 |
| 5 Unit | 3 |
| 6 Unit | 3 |
| 7 Unit | 4 |
| 8 Unit | 4 |
| 9 Unit | 5 |

**Cross-Collateralized Portfolios:** For multi-property loans, the majority of properties must be leased for the loan to avoid the unleased refinance leverage reduction.

### Adjustment Application Rules

1. **Cumulative Application:** All applicable reductions are summed and applied to base LTV
2. **Floor Constraint:** Maximum LTV cannot exceed 80% under any circumstance
3. **Pricing Constraint:** Final LTV must have available pricing (see LLPA matrix in Section 11)
4. **Rounding:** Final LTV is rounded down to nearest 5% increment for pricing lookup

### Example Calculations

**Example 1: Standard Purchase**
- FICO: 740 (Tier 3)
- Purpose: Purchase
- Property: SFR, leased
- Loan Amount: $400,000

```
Base LTV (740 FICO, Purchase):     80%
No leverage reductions applicable
                                  ------
Maximum LTV:                       80%
```

**Example 2: Unleased Refinance with Non-Warrantable Condo**
- FICO: 720 (Tier 4)
- Purpose: Cash-Out Refinance
- Property: Non-warrantable condo, unleased
- Loan Amount: $350,000

```
Base LTV (720 FICO, Cash-Out):     80%
Unleased Refinance:                -10%
Non-Warrantable Condo:             -10%
                                  ------
Maximum LTV:                       60%
```

**Example 3: 5-9 Unit Property in Detroit**
- FICO: 760 (Tier 2)
- Purpose: Purchase
- Property: 6-unit apartment in Detroit
- Loan Amount: $800,000

```
Base LTV (760 FICO, Purchase):     80%
5-9 Units:                         -5%
Market-Specific (Detroit):         -5%
                                  ------
Maximum LTV:                       70%
```

**Example 4: Foreign National with Strong DSCR**
- Borrower: Foreign National
- Purpose: Purchase
- DSCR: 1.35x
- Property: SFR, leased

```
Base LTV (FN, Purchase):           70%
FN with DSCR ≥1.30x:              +5%
                                  ------
Maximum LTV:                       75%
Note: Pricing N/A at 75% for FN - max practical LTV is 70%
```

---

## 10.4 DSCR-Constrained Maximum Loan

### Formula Derivation

The DSCR-constrained maximum loan is the loan amount where the resulting DSCR exactly equals the minimum required DSCR. This is derived algebraically from the DSCR formula:

```
DSCR = Qualifying Rent / PITIA
```

Where PITIA = Principal + Interest + Taxes + Insurance + Association Dues

For a fully amortizing loan:

```
Monthly P&I = Loan Amount × [r(1+r)^n] / [(1+r)^n - 1]
```

Where:
- r = Monthly interest rate (Annual Rate / 12)
- n = Total number of payments (Term in years × 12)

### Maximum Loan Calculation

Solving for the maximum loan amount where DSCR = Minimum DSCR:

```
Max Loan = (Qualifying Rent / Min DSCR - Taxes - Insurance - HOA) / Payment Factor
```

Where:

```
Payment Factor = [r(1+r)^n] / [(1+r)^n - 1]
```

For **Interest-Only** loans, the formula simplifies:

```
Monthly I/O Payment = Loan Amount × (Annual Rate / 12)
Max Loan (I/O) = (Qualifying Rent / Min DSCR - Taxes - Insurance - HOA) / (Annual Rate / 12)
```

### Minimum DSCR Requirements

| Condition | Minimum DSCR | Notes |
|-----------|--------------|-------|
| **Standard** | 1.00x | All borrowers meeting standard eligibility |
| **DSCR < 1.00** | Not Permitted | No sub-1.00 DSCR loans allowed |

**Important:** Unlike some programs that allow sub-1.00 DSCR for higher FICO borrowers, USDV program guidelines require a **minimum 1.00x DSCR** for all loans. The pricing matrix shows N/A for DSCR < 1.00 across all LTV tiers.

### DSCR-Based Pricing Tiers

While minimum DSCR is 1.00x, pricing varies by DSCR tier:

| DSCR Range | Pricing Impact | Notes |
|------------|----------------|-------|
| **DSCR ≥ 1.15** | +0.50% price improvement | Best pricing tier |
| **DSCR 1.10-1.14** | Standard pricing | No adjustment |
| **DSCR 1.00-1.09** | Price reduction at higher LTVs | -0.125% to -0.375% at 70-80% LTV |
| **DSCR < 1.00** | Not Available | Loan ineligible |

### Qualifying Rent Rules

| Scenario | Qualifying Rent Calculation |
|----------|----------------------------|
| **Leased (Purchase)** | Lower of in-place rent and appraised market rent |
| **Leased (Refinance)** | Lower of in-place rent and appraised market rent |
| **Unleased (Purchase)** | 100% of appraised market rent |
| **Unleased (Refinance)** | 100% of appraised market rent (with -10% LTV reduction) |
| **Short-Term Rental** | 100% of monthly market rent for 12-month lease (capped) |

### Example Calculation

**Scenario:**
- Qualifying Rent: $3,500/month
- Minimum DSCR: 1.00x
- Interest Rate: 7.50%
- Term: 30 years (fully amortizing)
- Monthly Taxes: $400
- Monthly Insurance: $150
- Monthly HOA: $0

**Step 1: Calculate available debt service**
```
Available for P&I = $3,500 / 1.00 - $400 - $150 - $0 = $2,950/month
```

**Step 2: Calculate payment factor**
```
r = 0.075 / 12 = 0.00625
n = 30 × 12 = 360
Payment Factor = [0.00625 × (1.00625)^360] / [(1.00625)^360 - 1]
Payment Factor = 0.006992
```

**Step 3: Calculate maximum loan**
```
Max Loan = $2,950 / 0.006992 = $421,911
```

**INSPIRE Integration:** The DSCR Sizer automatically performs this calculation using the borrower's quoted rate and displays both the DSCR-constrained maximum and the resulting DSCR at any user-specified loan amount.

---

## 10.5 Foreign National Sizing

### Overview

Foreign National (FN) borrowers face additional constraints in DSCR loan sizing due to increased documentation complexity and risk profile. These constraints are applied in addition to standard sizing rules.

### FN Sizing Constraints

| Parameter | Standard Borrower | Foreign National |
|-----------|-------------------|------------------|
| **Effective LTV Tier** | Per FICO | Equivalent to 660-679 FICO |
| **Minimum DSCR** | 1.00x | 1.00x |
| **Maximum LTV (Purchase)** | Per FICO tier | 70% |
| **Maximum LTV (R&T Refi)** | Per FICO tier | 70% |
| **Maximum LTV (Cash-Out)** | Per FICO tier | 65% |
| **Maximum Loan Amount** | $3,000,000 | $3,000,000 |
| **Pricing Availability** | Per FICO tier | N/A at 75%+ LTV |

### FN LTV Enhancement

Foreign Nationals with strong debt service coverage may qualify for enhanced leverage:

| DSCR | LTV Enhancement | Maximum LTV |
|------|-----------------|-------------|
| < 1.30x | None | 70% (Purchase/R&T), 65% (Cash-Out) |
| ≥ 1.30x | +5% | 75% (Purchase/R&T), 70% (Cash-Out) |

**Note:** Even with the +5% enhancement, pricing availability may limit practical maximum LTV to 70%.

### Additional FN Requirements

1. **Background Report:** Mandatory even if system returns null check
2. **Credit Documentation:** International credit reports or alternative credit documentation acceptable
3. **Entity Structure:** Same entity requirements as US citizens
4. **Guaranty:** 100% personal guarantee required

### FN Sizing Example

**Scenario:**
- Borrower: Foreign National
- Property Value: $500,000
- Qualifying Rent: $3,200/month
- DSCR: 1.15x
- Purpose: Purchase

**Step 1: Determine Maximum LTV**
```
Base LTV (FN, Purchase):           70%
DSCR 1.15x (< 1.30x threshold):    No enhancement
                                  ------
Maximum LTV:                       70%
```

**Step 2: Calculate LTV-Constrained Loan**
```
LTV-Constrained Loan = $500,000 × 70% = $350,000
```

**Step 3: Verify DSCR at Maximum Loan**
```
At $350,000 loan, verify DSCR ≥ 1.00x
If DSCR < 1.00x, reduce loan until DSCR = 1.00x
```

---

## 10.6 5-9 Unit Sizing

### Overview

Properties with 5-9 units are classified as small multi-family and require specialized sizing treatment due to increased operational complexity, tenant management requirements, and income concentration risk.

### 5-9 Unit Constraints

| Parameter | 1-4 Units | 5-9 Units |
|-----------|-----------|-----------|
| **Base LTV Reduction** | None | -5% |
| **Maximum LTV** | Per FICO tier | 75% (pricing constraint) |
| **Minimum DSCR** | 1.00x | 1.00x (NCF-based) |
| **Appraisal Type** | Standard with market rent | Full commercial narrative |
| **Pricing Impact** | Standard | -4.00% to -7.50% LLPA |

### 5-9 Unit LTV Constraints

The pricing matrix imposes severe constraints on 5-9 unit properties:

| LTV | 5-9 Unit LLPA | Availability |
|-----|---------------|--------------|
| 50% | -4.000% | Available |
| 55% | -4.250% | Available |
| 60% | -4.500% | Available |
| 65% | -5.375% | Available |
| 70% | -6.000% | Available |
| 75% | -7.500% | Available |
| 80% | N/A | Not Available |

### Income Calculation for 5-9 Units

For 5-9 unit properties, qualifying income uses the **NCF (Net Cash Flow) DSCR** methodology:

```
NCF DSCR = Net Operating Income / Annual Debt Service
```

Where:
```
Net Operating Income = Gross Potential Rent - Vacancy - Operating Expenses
```

Standard assumptions for 5-9 units:
- **Vacancy Factor:** 5% of Gross Potential Rent
- **Operating Expenses:** 35% of Effective Gross Income (or actual if documented)
- **Management Fee:** Included in operating expenses (typically 8-10%)

See Section 7.6 for detailed NCF DSCR calculation methodology.

### 5-9 Unit Sizing Example

**Scenario:**
- FICO: 750
- Property: 6-unit apartment
- Property Value: $1,200,000
- Gross Potential Rent: $9,000/month
- Purpose: Purchase

**Step 1: Calculate Net Operating Income**
```
Gross Potential Rent:              $9,000/month
Less Vacancy (5%):                 -$450
Effective Gross Income:            $8,550
Less Operating Expenses (35%):     -$2,993
Net Operating Income:              $5,557/month
```

**Step 2: Determine Maximum LTV**
```
Base LTV (750 FICO, Purchase):     80%
5-9 Unit Reduction:                -5%
                                  ------
Calculated Maximum LTV:            75%
Pricing Maximum (5-9 units):       75%
Final Maximum LTV:                 75%
```

**Step 3: Calculate LTV-Constrained Loan**
```
LTV-Constrained Loan = $1,200,000 × 75% = $900,000
```

**Step 4: Calculate DSCR-Constrained Loan**
```
Minimum DSCR: 1.00x
Maximum Annual Debt Service = $5,557 × 12 / 1.00 = $66,684
DSCR-Constrained Loan: ~$860,000 (at 7.5%, 30-year amortization)
```

**Step 5: Determine Final Sizing**
```
Maximum Loan = MIN($900,000, $860,000) = $860,000
Binding Constraint: DSCR
Final LTV: 71.7%
```

---

## 10.7 Product Parameters

### Loan Amount Limits

| Parameter | Minimum | Maximum | Notes |
|-----------|---------|---------|-------|
| **Standard Loan Amount** | $100,000 | $3,000,000 | All borrower types |
| **High Balance Tier 1** | $2,000,001 | $3,000,000 | Pricing impact, N/A at 80% LTV |
| **Low Balance** | $100,000 | $150,000 | Pricing impact at higher LTVs |

### Loan Term Options

| Term | Rate Type | Amortization | Notes |
|------|-----------|--------------|-------|
| **30 Year** | Fixed | 30-year | Standard term |
| **30 Year** | Fixed | Interest-Only (10 yr) | I/O period followed by 20-year amortization |
| **30 Year** | 5/1 ARM | 30-year | Fixed 5 years, adjusts annually |
| **30 Year** | 7/1 ARM | 30-year | Fixed 7 years, adjusts annually |

### ARM Parameters

| Parameter | 5/1 ARM | 7/1 ARM |
|-----------|---------|---------|
| **Fixed Period** | 5 years | 7 years |
| **Adjustment Frequency** | Annual | Annual |
| **Index** | 30-Day Average SOFR | 30-Day Average SOFR |
| **Margin** | 5.00% | 5.00% |
| **Initial Cap** | 2% | 5% |
| **Periodic Cap** | 2% | 2% |
| **Lifetime Cap** | 5% | 5% |
| **Floor** | Margin (5.00%) | Margin (5.00%) |
| **Lookback Days** | 45 | 45 |
| **Rounding** | Up to nearest 0.125% | Up to nearest 0.125% |

### Interest-Only Eligibility

Interest-only periods are subject to additional constraints:

| Constraint | Requirement |
|------------|-------------|
| **Maximum I/O Period** | 10 years |
| **Amortization After I/O** | Accelerated (remaining term) |
| **Balloon Payment** | None - fully amortizing after I/O |
| **Pricing Impact** | -0.25% to -0.75% LLPA at higher LTVs |

**I/O Pricing by LTV:**

| LTV | I/O LLPA |
|-----|----------|
| ≤65% | 0.000% |
| 70% | -0.250% |
| 75% | -0.375% |
| 80% | -0.750% |

### Prepayment Penalty Options

| Option | Structure | Pricing Impact |
|--------|-----------|----------------|
| **7-Year Min Interest** | 84 months minimum interest | +2.000% |
| **7-Year Step-down** | 7%/6%/5%/4%/3%/2%/1% | +1.750% |
| **5-Year Min Interest** | 60 months minimum interest | +0.750% |
| **5-Year Step-down** | 5%/4%/3%/2%/1% | +0.500% |
| **3-Year Step-down** | 3%/2%/1% | 0.000% (base) |
| **2-Year Step-down** | 2%/1% | -1.000% |
| **1-Year** | 1% | -2.000% |
| **No Prepayment** | None | -4.000% |

**Note:** Prepayment penalty is calculated on outstanding principal balance, not original loan amount.

### Rate Lock Parameters

| Parameter | Value |
|-----------|-------|
| **Initial Lock Period** | 30 days |
| **Maximum Lock Period** | 90 days |
| **Extension Cost** | 15 BPS per 15 days |
| **Relock Policy** | Worse of original or current pricing |

### Pricing Constraints

| Parameter | Value |
|-----------|-------|
| **Minimum Price** | 97.000% |
| **Maximum Price** | 104.500% |
| **Maximum Price (PPP < 3 Year)** | 102.000% |

---

## 10.8 INSPIRE Integration

### DSCR Sizer Engine Components

The INSPIRE DSCR Sizer Engine implements the sizing methodology through the following workflow:

```
┌─────────────────────────────────────────────────────────────────┐
│                    DSCR SIZER ENGINE                            │
├─────────────────────────────────────────────────────────────────┤
│  INPUTS                                                         │
│  ├── Borrower Profile (FICO, citizenship, entity type)          │
│  ├── Property Data (value, type, units, rent, location)         │
│  └── Loan Request (purpose, amount, term, rate type)            │
├─────────────────────────────────────────────────────────────────┤
│  PROCESSING                                                     │
│  ├── 1. Determine FICO Tier                                     │
│  ├── 2. Check Foreign National / 5-9 Unit overrides             │
│  ├── 3. Look up Base LTV from matrix                            │
│  ├── 4. Calculate all applicable leverage reductions            │
│  ├── 5. Apply pricing-based LTV constraints                     │
│  ├── 6. Calculate LTV-Constrained Maximum                       │
│  ├── 7. Calculate DSCR-Constrained Maximum (min 1.00x)          │
│  └── 8. Apply binding constraint                                │
├─────────────────────────────────────────────────────────────────┤
│  OUTPUTS                                                        │
│  ├── Maximum Loan Amount                                        │
│  ├── Binding Constraint (LTV or DSCR)                           │
│  ├── Resulting LTV at max loan                                  │
│  ├── Resulting DSCR at max loan                                 │
│  ├── Headroom on non-binding constraint                         │
│  ├── All leverage reductions applied                            │
│  └── Pricing eligibility confirmation                           │
└─────────────────────────────────────────────────────────────────┘
```

### User Interface Display

The INSPIRE sizing results display includes:

1. **Primary Sizing Output:**
   - Maximum loan amount (formatted with currency)
   - Binding constraint indicator
   - Resulting LTV and DSCR

2. **Constraint Details:**
   - LTV-constrained maximum with breakdown
   - DSCR-constrained maximum with breakdown
   - Visual indicator of which is binding

3. **Leverage Reduction Transparency:**
   - List of all reductions applied
   - Impact of each reduction
   - "What-if" scenario capability

4. **Pricing Validation:**
   - Confirmation that LTV/FICO combination has available pricing
   - Warning if approaching pricing boundaries
   - LLPA summary for selected scenario

---

## 10.9 Python Implementation

### DSCRSizer Class

```python
"""
DSCR Loan Sizing Module

This module provides comprehensive DSCR loan sizing calculations including
LTV-constrained and DSCR-constrained maximum loan amounts.

Source Guidelines:
    - Eastview DSCR Guidelines v7.2 (November 2025)
    - EV DSCR S Matrix (Effective 12/29/2025)
    - Archwest DSCR Guidelines v1.8 (July 2025)
    - Churchill DSCR Guidelines (August 2023)

Dependencies:
    - Section 7: DSCRCalculator for DSCR and qualifying rent calculations
    
INSPIRE Integration:
    - Phase 3-4: DSCR Sizer Engine
    - Interfaces with pricing engine for rate-dependent calculations
"""

from dataclasses import dataclass, field
from decimal import Decimal, ROUND_DOWN, ROUND_HALF_UP
from enum import Enum
from typing import Optional, Dict, List, Tuple, Set
import math


class LoanPurpose(Enum):
    """Loan purpose enumeration for LTV matrix lookup."""
    PURCHASE = "purchase"
    RATE_TERM_REFI = "rate_term_refi"
    CASH_OUT_REFI = "cash_out_refi"
    DELAYED_PURCHASE = "delayed_purchase"


class PropertyType(Enum):
    """Property type enumeration for adjustment calculations."""
    SFR = "sfr"
    TOWNHOUSE = "townhouse"
    PUD = "pud"
    CONDO_WARRANTABLE = "condo_warrantable"
    CONDO_NON_WARRANTABLE = "condo_non_warrantable"
    MULTI_2_4 = "multi_2_4"
    MULTI_5_9 = "multi_5_9"


class CitizenshipType(Enum):
    """Borrower citizenship type enumeration."""
    US_CITIZEN = "us_citizen"
    PERMANENT_RESIDENT = "permanent_resident"
    FOREIGN_NATIONAL = "foreign_national"


class BindingConstraint(Enum):
    """Indicates which constraint limits the loan amount."""
    LTV = "ltv"
    DSCR = "dscr"
    BOTH = "both"
    PRICING = "pricing"


class RateType(Enum):
    """Interest rate type enumeration."""
    FIXED_30 = "fixed_30"
    ARM_5_1 = "arm_5_1"
    ARM_7_1 = "arm_7_1"


# High-risk markets requiring leverage reduction
HIGH_RISK_MARKETS: Set[str] = {"chicago", "detroit", "baltimore", "flint"}


@dataclass
class Borrower:
    """Borrower information for sizing calculations.
    
    Attributes:
        fico_score: Lowest middle FICO score among all guarantors
        citizenship: Borrower citizenship type
        is_first_time_investor: True if borrower has no prior investment property experience
    """
    fico_score: int
    citizenship: CitizenshipType
    is_first_time_investor: bool = False


@dataclass
class Property:
    """Property information for sizing calculations.
    
    Attributes:
        value: Appraised "As-Is" property value
        property_type: Type of property
        units: Number of units (1-9)
        qualifying_rent: Monthly qualifying rent (from Section 7 calculation)
        monthly_taxes: Monthly property tax amount
        monthly_insurance: Monthly hazard insurance amount
        monthly_hoa: Monthly HOA/association dues
        market: Property market/city (for market-specific adjustments)
        is_str: True if property is operated as short-term rental
        is_section8: True if property has Section 8 or subsidized tenants
        is_leased: True if property meets leased requirements
        is_luxury: True if single-asset property with >$1M UPB
    """
    value: Decimal
    property_type: PropertyType
    units: int
    qualifying_rent: Decimal
    monthly_taxes: Decimal
    monthly_insurance: Decimal
    monthly_hoa: Decimal = Decimal("0")
    market: str = ""
    is_str: bool = False
    is_section8: bool = False
    is_leased: bool = True
    is_luxury: bool = False


@dataclass
class LoanRequest:
    """Loan request parameters for sizing.
    
    Attributes:
        purpose: Loan purpose (purchase, R&T refi, cash-out refi)
        interest_rate: Annual interest rate as decimal (e.g., 0.075 for 7.5%)
        term_years: Loan term in years
        rate_type: Type of interest rate (fixed, ARM)
        is_interest_only: True if loan has interest-only period
        io_period_years: Length of interest-only period in years
        requested_amount: Optional borrower-requested loan amount
    """
    purpose: LoanPurpose
    interest_rate: Decimal
    term_years: int = 30
    rate_type: RateType = RateType.FIXED_30
    is_interest_only: bool = False
    io_period_years: int = 0
    requested_amount: Optional[Decimal] = None


@dataclass
class LeverageReduction:
    """Individual leverage reduction with description.
    
    Attributes:
        condition: Description of the condition triggering reduction
        reduction: Reduction percentage (negative value)
        applied: Whether this reduction was applied
    """
    condition: str
    reduction: Decimal
    applied: bool


@dataclass
class DSCRSizingResult:
    """Complete DSCR sizing result.
    
    Attributes:
        max_loan_amount: Maximum loan amount after all constraints
        binding_constraint: Which constraint is binding (LTV, DSCR, pricing, or both)
        ltv_constrained_loan: Maximum loan based on LTV constraint
        dscr_constrained_loan: Maximum loan based on DSCR constraint
        pricing_constrained_loan: Maximum loan based on pricing availability
        resulting_ltv: LTV at maximum loan amount
        resulting_dscr: DSCR at maximum loan amount
        base_ltv: Base LTV from matrix before reductions
        adjusted_ltv: Maximum LTV after all reductions
        pricing_max_ltv: Maximum LTV with available pricing
        fico_tier: FICO tier used for calculations
        min_dscr: Minimum DSCR requirement applied
        leverage_reductions: List of all leverage reductions considered
        monthly_payment: Monthly P&I payment at max loan
        monthly_pitia: Monthly PITIA at max loan
        is_eligible: Whether the loan meets all eligibility requirements
        ineligibility_reasons: List of reasons if not eligible
    """
    max_loan_amount: Decimal
    binding_constraint: BindingConstraint
    ltv_constrained_loan: Decimal
    dscr_constrained_loan: Decimal
    pricing_constrained_loan: Decimal
    resulting_ltv: Decimal
    resulting_dscr: Decimal
    base_ltv: Decimal
    adjusted_ltv: Decimal
    pricing_max_ltv: Decimal
    fico_tier: str
    min_dscr: Decimal
    leverage_reductions: List[LeverageReduction]
    monthly_payment: Decimal
    monthly_pitia: Decimal
    is_eligible: bool
    ineligibility_reasons: List[str]


class DSCRSizer:
    """
    Calculate DSCR loan sizing with all constraints.
    
    This class implements the dual-constraint methodology for DSCR loan sizing,
    considering both LTV-based and DSCR-based maximum loan amounts, as well as
    pricing availability constraints.
    
    Source Guidelines:
        - Eastview DSCR Guidelines v7.2
        - EV DSCR S Matrix (12/29/2025)
        - Archwest DSCR Guidelines v1.8
    
    Attributes:
        BASE_LTV_MATRIX: Base LTV percentages by FICO tier and loan purpose
        PRICING_MAX_LTV: Maximum LTV with available pricing by FICO tier
        MIN_DSCR: Minimum required DSCR (1.00x for all scenarios)
    
    Example:
        >>> sizer = DSCRSizer()
        >>> borrower = Borrower(fico_score=720, citizenship=CitizenshipType.US_CITIZEN)
        >>> property = Property(
        ...     value=Decimal("500000"),
        ...     property_type=PropertyType.SFR,
        ...     units=1,
        ...     qualifying_rent=Decimal("3500"),
        ...     monthly_taxes=Decimal("400"),
        ...     monthly_insurance=Decimal("150")
        ... )
        >>> loan = LoanRequest(
        ...     purpose=LoanPurpose.PURCHASE,
        ...     interest_rate=Decimal("0.075"),
        ...     term_years=30
        ... )
        >>> result = sizer.size_loan(borrower, property, loan)
        >>> print(f"Max Loan: ${result.max_loan_amount:,.2f}")
    """
    
    # Base LTV Matrix from Eastview Guidelines v7.2
    # {fico_tier: {purpose: ltv}}
    BASE_LTV_MATRIX: Dict[str, Dict[str, Decimal]] = {
        "780+": {
            "purchase": Decimal("0.80"),
            "rate_term_refi": Decimal("0.80"),
            "cash_out_refi": Decimal("0.80"),
        },
        "760-779": {
            "purchase": Decimal("0.80"),
            "rate_term_refi": Decimal("0.80"),
            "cash_out_refi": Decimal("0.80"),
        },
        "740-759": {
            "purchase": Decimal("0.80"),
            "rate_term_refi": Decimal("0.80"),
            "cash_out_refi": Decimal("0.80"),
        },
        "720-739": {
            "purchase": Decimal("0.80"),
            "rate_term_refi": Decimal("0.80"),
            "cash_out_refi": Decimal("0.80"),
        },
        "700-719": {
            "purchase": Decimal("0.75"),
            "rate_term_refi": Decimal("0.75"),
            "cash_out_refi": Decimal("0.75"),
        },
        "680-699": {
            "purchase": Decimal("0.75"),
            "rate_term_refi": Decimal("0.75"),
            "cash_out_refi": Decimal("0.70"),
        },
        "660-679": {
            "purchase": Decimal("0.70"),
            "rate_term_refi": Decimal("0.70"),
            "cash_out_refi": Decimal("0.65"),
        },
        "foreign_national": {
            "purchase": Decimal("0.70"),
            "rate_term_refi": Decimal("0.70"),
            "cash_out_refi": Decimal("0.65"),
        },
    }
    
    # Maximum LTV with available pricing (from EV DSCR S Matrix)
    PRICING_MAX_LTV: Dict[str, Decimal] = {
        "780+": Decimal("0.80"),
        "760-779": Decimal("0.80"),
        "740-759": Decimal("0.80"),
        "720-739": Decimal("0.80"),
        "700-719": Decimal("0.80"),
        "680-699": Decimal("0.75"),  # N/A at 80%
        "660-679": Decimal("0.70"),  # N/A at 75%+
        "foreign_national": Decimal("0.70"),  # N/A at 75%+
        "5-9_units": Decimal("0.75"),  # N/A at 80%
    }
    
    # FICO tier boundaries
    FICO_TIERS: List[Tuple[str, int, int]] = [
        ("780+", 780, 850),
        ("760-779", 760, 779),
        ("740-759", 740, 759),
        ("720-739", 720, 739),
        ("700-719", 700, 719),
        ("680-699", 680, 699),
        ("660-679", 660, 679),
    ]
    
    # Minimum DSCR - 1.00x for all scenarios (no sub-1.00 DSCR allowed)
    MIN_DSCR: Decimal = Decimal("1.00")
    
    # Product limits
    MIN_LOAN_AMOUNT: Decimal = Decimal("100000")
    MAX_LOAN_AMOUNT: Decimal = Decimal("3000000")
    MAX_LTV_CAP: Decimal = Decimal("0.80")
    MIN_FICO: int = 660
    
    # Leverage reduction values
    REDUCTION_UNLEASED_REFI: Decimal = Decimal("-0.10")
    REDUCTION_NON_WARRANTABLE_CONDO: Decimal = Decimal("-0.10")
    REDUCTION_5_9_UNITS: Decimal = Decimal("-0.05")
    REDUCTION_HIGH_RISK_MARKET: Decimal = Decimal("-0.05")
    REDUCTION_STR: Decimal = Decimal("-0.05")
    REDUCTION_SECTION8: Decimal = Decimal("-0.05")
    REDUCTION_LUXURY: Decimal = Decimal("-0.10")
    
    # LTV increase thresholds
    DSCR_THRESHOLD_700_719: Decimal = Decimal("1.20")
    DSCR_THRESHOLD_FN: Decimal = Decimal("1.30")
    LTV_INCREASE: Decimal = Decimal("0.05")
    
    def get_fico_tier(self, fico: int) -> str:
        """
        Determine FICO tier based on score.
        
        Args:
            fico: FICO score (660-850)
            
        Returns:
            FICO tier string (e.g., "780+", "720-739")
            
        Raises:
            ValueError: If FICO score is below minimum (660)
        """
        if fico < self.MIN_FICO:
            raise ValueError(f"FICO score {fico} is below minimum requirement of {self.MIN_FICO}")
        
        for tier_name, tier_min, tier_max in self.FICO_TIERS:
            if tier_min <= fico <= tier_max:
                return tier_name
        
        # Should not reach here if FICO_TIERS is complete
        return "780+"
    
    def get_base_ltv(
        self, 
        fico_tier: str, 
        purpose: LoanPurpose,
        citizenship: CitizenshipType
    ) -> Decimal:
        """
        Look up base LTV from matrix.
        
        Args:
            fico_tier: FICO tier string
            purpose: Loan purpose
            citizenship: Borrower citizenship type
            
        Returns:
            Base LTV as decimal (e.g., 0.75 for 75%)
        """
        # Foreign Nationals use their own row
        if citizenship == CitizenshipType.FOREIGN_NATIONAL:
            matrix_key = "foreign_national"
        else:
            matrix_key = fico_tier
        
        if matrix_key not in self.BASE_LTV_MATRIX:
            raise ValueError(f"Invalid FICO tier: {matrix_key}")
        
        # Map purpose to matrix key
        if purpose == LoanPurpose.DELAYED_PURCHASE:
            purpose_key = "purchase"
        else:
            purpose_key = purpose.value
        
        return self.BASE_LTV_MATRIX[matrix_key][purpose_key]
    
    def get_pricing_max_ltv(
        self,
        fico_tier: str,
        citizenship: CitizenshipType,
        units: int
    ) -> Decimal:
        """
        Get maximum LTV with available pricing.
        
        Args:
            fico_tier: FICO tier string
            citizenship: Borrower citizenship type
            units: Number of property units
            
        Returns:
            Maximum LTV with available pricing
        """
        # 5-9 units have their own constraint
        if units >= 5:
            return self.PRICING_MAX_LTV["5-9_units"]
        
        # Foreign Nationals
        if citizenship == CitizenshipType.FOREIGN_NATIONAL:
            return self.PRICING_MAX_LTV["foreign_national"]
        
        return self.PRICING_MAX_LTV.get(fico_tier, Decimal("0.80"))
    
    def calculate_dscr(
        self,
        loan_amount: Decimal,
        interest_rate: Decimal,
        term_years: int,
        qualifying_rent: Decimal,
        monthly_taxes: Decimal,
        monthly_insurance: Decimal,
        monthly_hoa: Decimal,
        is_interest_only: bool = False
    ) -> Decimal:
        """
        Calculate DSCR for a given loan amount.
        
        Args:
            loan_amount: Loan principal amount
            interest_rate: Annual interest rate as decimal
            term_years: Loan term in years
            qualifying_rent: Monthly qualifying rent
            monthly_taxes: Monthly property taxes
            monthly_insurance: Monthly hazard insurance
            monthly_hoa: Monthly HOA dues
            is_interest_only: Whether loan is interest-only
            
        Returns:
            DSCR as decimal (e.g., 1.25 for 1.25x)
        """
        monthly_pi = self._calculate_monthly_pi(
            loan_amount, interest_rate, term_years, is_interest_only
        )
        monthly_pitia = monthly_pi + monthly_taxes + monthly_insurance + monthly_hoa
        
        if monthly_pitia == 0:
            return Decimal("999.99")  # Effectively infinite DSCR
        
        return (qualifying_rent / monthly_pitia).quantize(
            Decimal("0.01"), rounding=ROUND_DOWN
        )
    
    def _calculate_monthly_pi(
        self,
        loan_amount: Decimal,
        interest_rate: Decimal,
        term_years: int,
        is_interest_only: bool = False
    ) -> Decimal:
        """
        Calculate monthly principal and interest payment.
        
        Args:
            loan_amount: Loan principal amount
            interest_rate: Annual interest rate as decimal
            term_years: Loan term in years
            is_interest_only: Whether loan is interest-only
            
        Returns:
            Monthly P&I payment
        """
        if loan_amount <= 0:
            return Decimal("0")
            
        if is_interest_only:
            # Interest-only payment
            return (loan_amount * interest_rate / 12).quantize(
                Decimal("0.01"), rounding=ROUND_HALF_UP
            )
        
        # Fully amortizing payment
        monthly_rate = interest_rate / 12
        num_payments = term_years * 12
        
        if monthly_rate == 0:
            return (loan_amount / num_payments).quantize(
                Decimal("0.01"), rounding=ROUND_HALF_UP
            )
        
        # Standard amortization formula
        monthly_rate_float = float(monthly_rate)
        num_payments_int = int(num_payments)
        
        payment_factor = (
            monthly_rate_float * (1 + monthly_rate_float) ** num_payments_int
        ) / ((1 + monthly_rate_float) ** num_payments_int - 1)
        
        return (loan_amount * Decimal(str(payment_factor))).quantize(
            Decimal("0.01"), rounding=ROUND_HALF_UP
        )
    
    def apply_leverage_reductions(
        self,
        base_ltv: Decimal,
        borrower: Borrower,
        property: Property,
        loan_request: LoanRequest,
        dscr: Optional[Decimal] = None
    ) -> Tuple[Decimal, List[LeverageReduction]]:
        """
        Apply all applicable leverage reductions to base LTV.
        
        Args:
            base_ltv: Base LTV from matrix
            borrower: Borrower information
            property: Property information
            loan_request: Loan request parameters
            dscr: Calculated DSCR (for LTV increase eligibility)
            
        Returns:
            Tuple of (adjusted LTV, list of reductions applied)
        """
        reductions: List[LeverageReduction] = []
        total_reduction = Decimal("0")
        total_increase = Decimal("0")
        
        # Unleased refinance reduction
        is_refi = loan_request.purpose in [LoanPurpose.RATE_TERM_REFI, LoanPurpose.CASH_OUT_REFI]
        if is_refi and not property.is_leased:
            red = LeverageReduction(
                "Unleased Refinance", 
                self.REDUCTION_UNLEASED_REFI, 
                True
            )
            reductions.append(red)
            total_reduction += red.reduction
        
        # Non-warrantable condo reduction
        if property.property_type == PropertyType.CONDO_NON_WARRANTABLE:
            red = LeverageReduction(
                "Non-Warrantable Condo", 
                self.REDUCTION_NON_WARRANTABLE_CONDO, 
                True
            )
            reductions.append(red)
            total_reduction += red.reduction
        
        # 5-9 unit reduction
        if property.units >= 5:
            red = LeverageReduction(
                "5-9 Units", 
                self.REDUCTION_5_9_UNITS, 
                True
            )
            reductions.append(red)
            total_reduction += red.reduction
        
        # High-risk market reduction
        if property.market.lower() in HIGH_RISK_MARKETS:
            red = LeverageReduction(
                f"High-Risk Market ({property.market})", 
                self.REDUCTION_HIGH_RISK_MARKET, 
                True
            )
            reductions.append(red)
            total_reduction += red.reduction
        
        # STR reduction
        if property.is_str:
            red = LeverageReduction(
                "Short-Term Rental (STR)", 
                self.REDUCTION_STR, 
                True
            )
            reductions.append(red)
            total_reduction += red.reduction
        
        # Section 8 / Subsidized reduction
        if property.is_section8:
            red = LeverageReduction(
                "Section 8 / Subsidized Lease", 
                self.REDUCTION_SECTION8, 
                True
            )
            reductions.append(red)
            total_reduction += red.reduction
        
        # Luxury rental reduction (>$1M UPB single asset)
        if property.is_luxury:
            red = LeverageReduction(
                "Luxury Rental (>$1M UPB)", 
                self.REDUCTION_LUXURY, 
                True
            )
            reductions.append(red)
            total_reduction += red.reduction
        
        # LTV increases for strong DSCR
        if dscr is not None:
            fico_tier = self.get_fico_tier(borrower.fico_score)
            
            # 700-719 FICO with DSCR >= 1.20x gets +5%
            if fico_tier == "700-719" and dscr >= self.DSCR_THRESHOLD_700_719:
                inc = LeverageReduction(
                    f"700-719 FICO with DSCR ≥{self.DSCR_THRESHOLD_700_719}x", 
                    self.LTV_INCREASE, 
                    True
                )
                reductions.append(inc)
                total_increase += inc.reduction
            
            # Foreign National with DSCR >= 1.30x gets +5%
            if (borrower.citizenship == CitizenshipType.FOREIGN_NATIONAL and 
                dscr >= self.DSCR_THRESHOLD_FN):
                inc = LeverageReduction(
                    f"Foreign National with DSCR ≥{self.DSCR_THRESHOLD_FN}x", 
                    self.LTV_INCREASE, 
                    True
                )
                reductions.append(inc)
                total_increase += inc.reduction
        
        # Calculate adjusted LTV
        adjusted_ltv = base_ltv + total_reduction + total_increase
        
        # Apply floor (0%) and cap (80%)
        adjusted_ltv = max(Decimal("0"), min(adjusted_ltv, self.MAX_LTV_CAP))
        
        return adjusted_ltv, reductions
    
    def calculate_ltv_constrained_loan(
        self, 
        property_value: Decimal, 
        max_ltv: Decimal
    ) -> Decimal:
        """
        Calculate maximum loan based on LTV constraint.
        
        Args:
            property_value: Appraised property value
            max_ltv: Maximum LTV as decimal
            
        Returns:
            Maximum loan amount based on LTV
        """
        return (property_value * max_ltv).quantize(Decimal("1"), rounding=ROUND_DOWN)
    
    def calculate_dscr_constrained_loan(
        self,
        qualifying_rent: Decimal,
        min_dscr: Decimal,
        interest_rate: Decimal,
        term_years: int,
        monthly_taxes: Decimal,
        monthly_insurance: Decimal,
        monthly_hoa: Decimal,
        is_interest_only: bool = False
    ) -> Decimal:
        """
        Calculate maximum loan based on DSCR constraint.
        
        Uses algebraic approach to find the maximum loan amount where
        DSCR equals the minimum required DSCR.
        
        Args:
            qualifying_rent: Monthly qualifying rent
            min_dscr: Minimum required DSCR
            interest_rate: Annual interest rate as decimal
            term_years: Loan term in years
            monthly_taxes: Monthly property taxes
            monthly_insurance: Monthly hazard insurance
            monthly_hoa: Monthly HOA dues
            is_interest_only: Whether loan is interest-only
            
        Returns:
            Maximum loan amount based on DSCR constraint
        """
        # Calculate maximum allowable PITIA
        max_pitia = qualifying_rent / min_dscr
        
        # Calculate available amount for P&I
        available_for_pi = max_pitia - monthly_taxes - monthly_insurance - monthly_hoa
        
        if available_for_pi <= 0:
            return Decimal("0")
        
        if is_interest_only:
            # For I/O: Loan = Available P&I / (Rate / 12)
            monthly_rate = interest_rate / 12
            if monthly_rate == 0:
                return self.MAX_LOAN_AMOUNT
            max_loan = available_for_pi / monthly_rate
        else:
            # For amortizing: Solve for loan amount using payment formula
            monthly_rate = float(interest_rate / 12)
            num_payments = term_years * 12
            
            if monthly_rate == 0:
                max_loan = Decimal(str(float(available_for_pi) * num_payments))
            else:
                # Payment factor = r(1+r)^n / ((1+r)^n - 1)
                payment_factor = (
                    monthly_rate * (1 + monthly_rate) ** num_payments
                ) / ((1 + monthly_rate) ** num_payments - 1)
                
                max_loan = Decimal(str(float(available_for_pi) / payment_factor))
        
        return max_loan.quantize(Decimal("1"), rounding=ROUND_DOWN)
    
    def check_eligibility(
        self,
        borrower: Borrower,
        property: Property,
        loan_request: LoanRequest
    ) -> Tuple[bool, List[str]]:
        """
        Check loan eligibility before sizing.
        
        Args:
            borrower: Borrower information
            property: Property information
            loan_request: Loan request parameters
            
        Returns:
            Tuple of (is_eligible, list of ineligibility reasons)
        """
        reasons: List[str] = []
        
        # FICO minimum
        if borrower.fico_score < self.MIN_FICO:
            reasons.append(f"FICO score {borrower.fico_score} below minimum {self.MIN_FICO}")
        
        # Unit count
        if property.units > 9:
            reasons.append(f"Property has {property.units} units; maximum is 9")
        
        if property.units < 1:
            reasons.append(f"Property must have at least 1 unit")
        
        return (len(reasons) == 0, reasons)
    
    def size_loan(
        self,
        borrower: Borrower,
        property: Property,
        loan_request: LoanRequest
    ) -> DSCRSizingResult:
        """
        Calculate complete DSCR loan sizing.
        
        This is the main entry point for DSCR loan sizing. It calculates
        LTV-constrained, DSCR-constrained, and pricing-constrained maximum 
        loan amounts and returns the binding constraint.
        
        Args:
            borrower: Borrower information
            property: Property information
            loan_request: Loan request parameters
            
        Returns:
            Complete sizing result with all constraints and reductions
            
        Example:
            >>> sizer = DSCRSizer()
            >>> result = sizer.size_loan(borrower, property, loan_request)
            >>> if result.is_eligible:
            ...     print(f"Max loan: ${result.max_loan_amount:,.0f}")
            ...     print(f"Binding constraint: {result.binding_constraint.value}")
        """
        # Check eligibility first
        is_eligible, ineligibility_reasons = self.check_eligibility(
            borrower, property, loan_request
        )
        
        # Get FICO tier
        try:
            fico_tier = self.get_fico_tier(borrower.fico_score)
        except ValueError as e:
            return DSCRSizingResult(
                max_loan_amount=Decimal("0"),
                binding_constraint=BindingConstraint.LTV,
                ltv_constrained_loan=Decimal("0"),
                dscr_constrained_loan=Decimal("0"),
                pricing_constrained_loan=Decimal("0"),
                resulting_ltv=Decimal("0"),
                resulting_dscr=Decimal("0"),
                base_ltv=Decimal("0"),
                adjusted_ltv=Decimal("0"),
                pricing_max_ltv=Decimal("0"),
                fico_tier="N/A",
                min_dscr=self.MIN_DSCR,
                leverage_reductions=[],
                monthly_payment=Decimal("0"),
                monthly_pitia=Decimal("0"),
                is_eligible=False,
                ineligibility_reasons=[str(e)]
            )
        
        # Get base LTV
        base_ltv = self.get_base_ltv(fico_tier, loan_request.purpose, borrower.citizenship)
        
        # Get pricing-constrained max LTV
        pricing_max_ltv = self.get_pricing_max_ltv(
            fico_tier, borrower.citizenship, property.units
        )
        
        # Calculate DSCR-constrained loan first (needed for LTV adjustments)
        dscr_constrained_loan = self.calculate_dscr_constrained_loan(
            qualifying_rent=property.qualifying_rent,
            min_dscr=self.MIN_DSCR,
            interest_rate=loan_request.interest_rate,
            term_years=loan_request.term_years,
            monthly_taxes=property.monthly_taxes,
            monthly_insurance=property.monthly_insurance,
            monthly_hoa=property.monthly_hoa,
            is_interest_only=loan_request.is_interest_only
        )
        
        # Calculate DSCR at DSCR-constrained loan for adjustment purposes
        dscr_at_constraint = self.calculate_dscr(
            loan_amount=dscr_constrained_loan,
            interest_rate=loan_request.interest_rate,
            term_years=loan_request.term_years,
            qualifying_rent=property.qualifying_rent,
            monthly_taxes=property.monthly_taxes,
            monthly_insurance=property.monthly_insurance,
            monthly_hoa=property.monthly_hoa,
            is_interest_only=loan_request.is_interest_only
        )
        
        # Apply leverage reductions (using DSCR for increase eligibility)
        adjusted_ltv, leverage_reductions = self.apply_leverage_reductions(
            base_ltv=base_ltv,
            borrower=borrower,
            property=property,
            loan_request=loan_request,
            dscr=dscr_at_constraint
        )
        
        # Apply pricing constraint to adjusted LTV
        final_max_ltv = min(adjusted_ltv, pricing_max_ltv)
        
        # Calculate LTV-constrained loan
        ltv_constrained_loan = self.calculate_ltv_constrained_loan(
            property.value, adjusted_ltv
        )
        
        # Calculate pricing-constrained loan
        pricing_constrained_loan = self.calculate_ltv_constrained_loan(
            property.value, pricing_max_ltv
        )
        
        # Determine binding constraint and max loan
        constraints = [
            (ltv_constrained_loan, BindingConstraint.LTV),
            (dscr_constrained_loan, BindingConstraint.DSCR),
            (pricing_constrained_loan, BindingConstraint.PRICING),
        ]
        
        # Find minimum
        min_loan = min(c[0] for c in constraints)
        binding_constraints = [c[1] for c in constraints if c[0] == min_loan]
        
        if len(binding_constraints) > 1:
            binding_constraint = BindingConstraint.BOTH
        else:
            binding_constraint = binding_constraints[0]
        
        max_loan = min_loan
        
        # Apply loan amount limits
        if max_loan > self.MAX_LOAN_AMOUNT:
            max_loan = self.MAX_LOAN_AMOUNT
        
        if max_loan < self.MIN_LOAN_AMOUNT and max_loan > 0:
            is_eligible = False
            ineligibility_reasons.append(
                f"Maximum loan ${max_loan:,.0f} below minimum ${self.MIN_LOAN_AMOUNT:,.0f}"
            )
        
        # Calculate final metrics at max loan
        if property.value > 0:
            resulting_ltv = (max_loan / property.value).quantize(
                Decimal("0.0001"), rounding=ROUND_DOWN
            )
        else:
            resulting_ltv = Decimal("0")
        
        resulting_dscr = self.calculate_dscr(
            loan_amount=max_loan,
            interest_rate=loan_request.interest_rate,
            term_years=loan_request.term_years,
            qualifying_rent=property.qualifying_rent,
            monthly_taxes=property.monthly_taxes,
            monthly_insurance=property.monthly_insurance,
            monthly_hoa=property.monthly_hoa,
            is_interest_only=loan_request.is_interest_only
        )
        
        # Check DSCR eligibility
        if resulting_dscr < self.MIN_DSCR and max_loan > 0:
            is_eligible = False
            ineligibility_reasons.append(
                f"DSCR {resulting_dscr:.2f}x below minimum {self.MIN_DSCR:.2f}x"
            )
        
        monthly_payment = self._calculate_monthly_pi(
            max_loan,
            loan_request.interest_rate,
            loan_request.term_years,
            loan_request.is_interest_only
        )
        
        monthly_pitia = (
            monthly_payment + 
            property.monthly_taxes + 
            property.monthly_insurance + 
            property.monthly_hoa
        )
        
        return DSCRSizingResult(
            max_loan_amount=max_loan,
            binding_constraint=binding_constraint,
            ltv_constrained_loan=ltv_constrained_loan,
            dscr_constrained_loan=dscr_constrained_loan,
            pricing_constrained_loan=pricing_constrained_loan,
            resulting_ltv=resulting_ltv,
            resulting_dscr=resulting_dscr,
            base_ltv=base_ltv,
            adjusted_ltv=adjusted_ltv,
            pricing_max_ltv=pricing_max_ltv,
            fico_tier=fico_tier,
            min_dscr=self.MIN_DSCR,
            leverage_reductions=leverage_reductions,
            monthly_payment=monthly_payment,
            monthly_pitia=monthly_pitia,
            is_eligible=is_eligible,
            ineligibility_reasons=ineligibility_reasons
        )


class DSCRScenarioAnalyzer:
    """
    Analyze multiple DSCR loan scenarios for comparison.
    
    Provides tools for comparing different loan structures, rate scenarios,
    and property assumptions to help borrowers make informed decisions.
    """
    
    def __init__(self):
        self.sizer = DSCRSizer()
    
    def compare_amortization_options(
        self,
        borrower: Borrower,
        property: Property,
        base_request: LoanRequest
    ) -> Dict[str, DSCRSizingResult]:
        """
        Compare amortizing vs interest-only loan options.
        
        Args:
            borrower: Borrower information
            property: Property information
            base_request: Base loan request (will be modified for comparison)
            
        Returns:
            Dictionary of scenario name to sizing result
        """
        scenarios = {}
        
        # 30-year amortizing
        request_amort = LoanRequest(
            purpose=base_request.purpose,
            interest_rate=base_request.interest_rate,
            term_years=30,
            is_interest_only=False
        )
        scenarios["30-Year Amortizing"] = self.sizer.size_loan(
            borrower, property, request_amort
        )
        
        # 30-year with 10-year I/O
        request_io = LoanRequest(
            purpose=base_request.purpose,
            interest_rate=base_request.interest_rate,
            term_years=30,
            is_interest_only=True,
            io_period_years=10
        )
        scenarios["30-Year with 10-Year I/O"] = self.sizer.size_loan(
            borrower, property, request_io
        )
        
        return scenarios
    
    def rate_sensitivity_analysis(
        self,
        borrower: Borrower,
        property: Property,
        base_request: LoanRequest,
        rate_range: List[Decimal]
    ) -> Dict[str, DSCRSizingResult]:
        """
        Analyze how different interest rates affect sizing.
        
        Args:
            borrower: Borrower information
            property: Property information
            base_request: Base loan request
            rate_range: List of interest rates to analyze
            
        Returns:
            Dictionary of rate string to sizing result
        """
        scenarios = {}
        
        for rate in rate_range:
            request = LoanRequest(
                purpose=base_request.purpose,
                interest_rate=rate,
                term_years=base_request.term_years,
                is_interest_only=base_request.is_interest_only,
                io_period_years=base_request.io_period_years
            )
            scenarios[f"{float(rate) * 100:.2f}%"] = self.sizer.size_loan(
                borrower, property, request
            )
        
        return scenarios


# Convenience function for quick sizing
def size_dscr_loan(
    fico: int,
    property_value: float,
    qualifying_rent: float,
    monthly_taxes: float,
    monthly_insurance: float,
    interest_rate: float,
    purpose: str = "purchase",
    units: int = 1,
    citizenship: str = "us_citizen",
    monthly_hoa: float = 0,
    term_years: int = 30,
    is_interest_only: bool = False,
    market: str = "",
    is_str: bool = False,
    is_section8: bool = False,
    is_leased: bool = True
) -> Dict:
    """
    Convenience function for quick DSCR loan sizing.
    
    Args:
        fico: Borrower FICO score
        property_value: Property value
        qualifying_rent: Monthly qualifying rent
        monthly_taxes: Monthly property taxes
        monthly_insurance: Monthly insurance
        interest_rate: Annual interest rate (e.g., 0.075 for 7.5%)
        purpose: Loan purpose ("purchase", "rate_term_refi", "cash_out_refi")
        units: Number of units
        citizenship: Citizenship type ("us_citizen", "permanent_resident", "foreign_national")
        monthly_hoa: Monthly HOA dues
        term_years: Loan term in years
        is_interest_only: Whether loan is interest-only
        market: Property market/city
        is_str: Whether property is short-term rental
        is_section8: Whether property has Section 8 tenants
        is_leased: Whether property is leased
        
    Returns:
        Dictionary with sizing results
        
    Example:
        >>> result = size_dscr_loan(
        ...     fico=720,
        ...     property_value=500000,
        ...     qualifying_rent=3500,
        ...     monthly_taxes=400,
        ...     monthly_insurance=150,
        ...     interest_rate=0.075
        ... )
        >>> print(f"Max loan: ${result['max_loan']:,.0f}")
    """
    sizer = DSCRSizer()
    
    # Map string inputs to enums
    purpose_map = {
        "purchase": LoanPurpose.PURCHASE,
        "rate_term_refi": LoanPurpose.RATE_TERM_REFI,
        "cash_out_refi": LoanPurpose.CASH_OUT_REFI,
        "delayed_purchase": LoanPurpose.DELAYED_PURCHASE
    }
    
    citizenship_map = {
        "us_citizen": CitizenshipType.US_CITIZEN,
        "permanent_resident": CitizenshipType.PERMANENT_RESIDENT,
        "foreign_national": CitizenshipType.FOREIGN_NATIONAL
    }
    
    # Determine property type from units
    if units == 1:
        property_type = PropertyType.SFR
    elif units <= 4:
        property_type = PropertyType.MULTI_2_4
    else:
        property_type = PropertyType.MULTI_5_9
    
    borrower = Borrower(
        fico_score=fico,
        citizenship=citizenship_map.get(citizenship, CitizenshipType.US_CITIZEN)
    )
    
    prop = Property(
        value=Decimal(str(property_value)),
        property_type=property_type,
        units=units,
        qualifying_rent=Decimal(str(qualifying_rent)),
        monthly_taxes=Decimal(str(monthly_taxes)),
        monthly_insurance=Decimal(str(monthly_insurance)),
        monthly_hoa=Decimal(str(monthly_hoa)),
        market=market,
        is_str=is_str,
        is_section8=is_section8,
        is_leased=is_leased
    )
    
    loan_request = LoanRequest(
        purpose=purpose_map.get(purpose, LoanPurpose.PURCHASE),
        interest_rate=Decimal(str(interest_rate)),
        term_years=term_years,
        is_interest_only=is_interest_only
    )
    
    result = sizer.size_loan(borrower, prop, loan_request)
    
    return {
        "max_loan": float(result.max_loan_amount),
        "binding_constraint": result.binding_constraint.value,
        "ltv_constrained_loan": float(result.ltv_constrained_loan),
        "dscr_constrained_loan": float(result.dscr_constrained_loan),
        "pricing_constrained_loan": float(result.pricing_constrained_loan),
        "resulting_ltv": float(result.resulting_ltv),
        "resulting_dscr": float(result.resulting_dscr),
        "base_ltv": float(result.base_ltv),
        "adjusted_ltv": float(result.adjusted_ltv),
        "pricing_max_ltv": float(result.pricing_max_ltv),
        "min_dscr": float(result.min_dscr),
        "fico_tier": result.fico_tier,
        "monthly_payment": float(result.monthly_payment),
        "monthly_pitia": float(result.monthly_pitia),
        "is_eligible": result.is_eligible,
        "ineligibility_reasons": result.ineligibility_reasons,
        "leverage_reductions": [
            {
                "condition": red.condition, 
                "reduction": float(red.reduction), 
                "applied": red.applied
            }
            for red in result.leverage_reductions
        ]
    }
```

---

## 10.10 Quick Reference

### DSCR Sizing Decision Tree

```
START
  │
  ├─► Is FICO ≥ 660?
  │     NO ──► INELIGIBLE
  │     YES ──┐
  │           ▼
  ├─► Is Foreign National?
  │     YES ──► Use FN LTV matrix (70%/70%/65%)
  │     │       Check DSCR ≥1.30x for +5% LTV
  │     NO ──┐
  │          ▼
  ├─► Is 5-9 Units?
  │     YES ──► Apply -5% LTV reduction
  │     │       Max LTV capped at 75% (pricing)
  │     NO ──┐
  │          ▼
  ├─► Look up Base LTV (FICO tier × Purpose)
  │          │
  │          ▼
  ├─► Apply all leverage reductions
  │     • Unleased Refi: -10%
  │     • Non-Warrantable Condo: -10%
  │     • High-Risk Market: -5%
  │     • STR: -5%
  │     • Section 8: -5%
  │     • Luxury (>$1M): -10%
  │          │
  │          ▼
  ├─► Apply pricing-based LTV cap
  │     • 680-699 FICO: Max 75%
  │     • 660-679 FICO: Max 70%
  │     • Foreign National: Max 70%
  │     • 5-9 Units: Max 75%
  │          │
  │          ▼
  ├─► Calculate LTV-Constrained Loan = Value × Final Max LTV
  │          │
  │          ▼
  ├─► Calculate DSCR-Constrained Loan (where DSCR = 1.00x)
  │          │
  │          ▼
  └─► Maximum Loan = MIN(LTV-Constrained, DSCR-Constrained, Pricing-Constrained)
             │
             ▼
          RESULT
```

### Key Thresholds Summary

| Parameter | Threshold | Impact |
|-----------|-----------|--------|
| Minimum FICO | 660 | Below = ineligible |
| Minimum DSCR | 1.00x | Below = ineligible (no sub-1.00 DSCR) |
| DSCR for pricing bonus | ≥1.15x | +0.50% price improvement |
| DSCR for 700-719 LTV boost | ≥1.20x | +5% LTV |
| DSCR for FN LTV boost | ≥1.30x | +5% LTV |
| Maximum LTV cap | 80% | Hard ceiling |
| 680-699 FICO pricing max | 75% | N/A at 80% |
| 660-679 FICO pricing max | 70% | N/A at 75%+ |
| FN pricing max | 70% | N/A at 75%+ |
| 5-9 Unit pricing max | 75% | N/A at 80% |

### Leverage Reduction Summary

| Condition | Reduction | Source |
|-----------|-----------|--------|
| Unleased Refinance | -10% | Eastview Guidelines |
| Non-Warrantable Condo | -10% | Eastview Guidelines |
| 5-9 Units | -5% | Eastview Guidelines |
| High-Risk Market (Chicago/Detroit/Baltimore/Flint) | -5% | Eastview Guidelines |
| STR/Airbnb/VRBO | -5% | Archwest Guidelines |
| Section 8/Subsidized | -5% | Archwest Guidelines |
| Luxury Rental (>$1M UPB) | -10% | Archwest Guidelines |

### Common Scenario Examples

| Scenario | Base LTV | Reductions | Final Max LTV |
|----------|----------|------------|---------------|
| 750 FICO, Purchase, SFR | 80% | None | 80% |
| 720 FICO, Cash-Out, Condo | 80% | None | 80% |
| 680 FICO, Purchase, SFR | 75% | None | 75% (pricing cap) |
| 660 FICO, R&T Refi, SFR | 70% | None | 70% (pricing cap) |
| 740 FICO, Refi, Unleased | 80% | -10% | 70% |
| 760 FICO, Purchase, 6-Unit | 80% | -5% | 75% (pricing cap) |
| FN, Purchase, STR | 70% | -5% | 65% |
| 720 FICO, Refi, Detroit | 80% | -5% | 75% |

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01-01 | USDV Underwriting | Initial release |
| 2.0 | 2025-01-01 | USDV Underwriting | Updated with verified investor guideline data from Eastview v7.2, EV DSCR S Matrix 12/29/25, Archwest v1.8, Churchill guidelines |

---

## Source Documents

This section synthesizes requirements from the following investor guidelines:

- **Eastview DSCR Guidelines v7.2** (November 2025)
- **EV DSCR S Pricing Rate Sheet** (Effective 12/29/2025)
- **Archwest DSCR Guidelines v1.8** (July 2025)
- **Churchill DSCR Guidelines** (August 2023)

---

*This section is part of the USDV Underwriting Manual and integrates with INSPIRE Phase 3-4 (Deal Sizing & Quote Generation). For DSCR calculation methodology, see Section 7. For pricing and rate determination, see Section 11.*
