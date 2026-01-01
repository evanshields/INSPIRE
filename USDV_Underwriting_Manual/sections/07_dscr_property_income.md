---
section: 7
title: DSCR Property & Income Analysis
version: 1.0
last_updated: 2025-12-30
model_used: opus
guideline_sources:
  - Eastview DSCR Guidelines v7.2
  - Archwest DSCR Guidelines v1.8
  - EV DSCR S Matrix 12.29.25
changelog:
  - 2025-12-30: Initial creation
---

# Section 7: DSCR Property & Income Analysis

## 7.1 Overview

Debt Service Coverage Ratio (DSCR) loans are permanent financing products designed for stabilized rental properties. Unlike traditional income documentation loans, DSCR loans qualify based on the property's ability to generate sufficient rental income to cover debt service obligations. This section details the methodology for calculating DSCR, determining qualifying rent, and analyzing rental income across various property and lease scenarios.

**INSPIRE Integration Points:**
- Phase 3-4: DSCR calculation for loan sizing and quote generation
- Phase 7: DSCR validation from appraisal and rent data during AI analysis

---

## 7.2 DSCR Calculation Formula

### 7.2.1 Standard DSCR Formula (1-4 Unit Properties)

The Debt Service Coverage Ratio measures the relationship between a property's rental income and its debt service obligations:

```
DSCR = Qualifying Monthly Rent / Monthly PITIA
```

**Where:**
- **Qualifying Monthly Rent** = Rental income used for underwriting (see Section 7.3)
- **Monthly PITIA** = Principal + Interest + Taxes + Insurance + Association Fees

### 7.2.2 NCF DSCR Formula (5-9 Unit Properties)

For small multifamily properties (5-9 units), DSCR is calculated on a Net Cash Flow (NCF) basis:

```
NCF DSCR = Net Cash Flow / Monthly Debt Service

Net Cash Flow = Gross Rent Income - Operating Expenses - Capital Expenditures
```

**Operating Expenses Include:**
- Property management (typically 8-10% of gross rent)
- Marketing & leasing costs
- Repairs & maintenance
- Insurance
- HOA/Association fees
- Property taxes
- Turnover costs
- Utilities (if landlord-paid)
- Other property-specific expenses

**Capital Expenditure Reserves:**
| Property Type | Annual Reserve Per Unit |
|--------------|------------------------|
| Multi-unit (2+ units) | $300/unit |
| Newly constructed SFR | $400 |
| Existing SFR | $600 |

**Repairs & Maintenance Minimums:**
| Property Type | Annual Amount Per Unit |
|--------------|------------------------|
| Multi-unit (2+ units) | $500/unit |
| Newly constructed SFR | $500 |
| Existing SFR | $700 |

---

## 7.3 Qualifying Rent Determination

Qualifying rent is the rental income figure used in the DSCR calculation. The methodology varies based on lease status, loan purpose, and property type.

### 7.3.1 Standard Qualifying Rent Rules

| Scenario | Qualifying Rent Formula | Notes |
|----------|------------------------|-------|
| **Leased (Purchase)** | MIN(In-place rent, 105% Market rent) | Lease must be arm's length |
| **Leased (Refinance)** | MIN(In-place rent, 105% Market rent) | Requires lease verification |
| **Unleased (Purchase)** | 100% Market rent | No lease required |
| **Unleased (Refinance)** | 100% Market rent | 10% LTV reduction applies (see Section 10) |
| **Short-Term Rental** | MIN(125% Market rent, 12-month avg income) | See Section 7.7 |
| **Section 8** | Contract rent (verified) | See Section 7.8 |

### 7.3.2 Multi-Unit Property Calculations

For 2-4 unit properties, calculate qualifying rent for each unit individually:

```
Total Qualifying Rent = Sum of (Qualifying Rent per Unit)
```

**Example - 3-Unit Property:**
| Unit | In-Place Rent | Market Rent | 105% Market | Qualifying Rent |
|------|---------------|-------------|-------------|-----------------|
| Unit 1 (Leased) | $1,200 | $1,100 | $1,155 | $1,155 |
| Unit 2 (Leased) | $1,050 | $1,100 | $1,155 | $1,050 |
| Unit 3 (Vacant) | N/A | $1,100 | N/A | $1,100 |
| **Total** | | | | **$3,305** |

### 7.3.3 Leased Property Definition

A property qualifies as "leased" based on the following criteria:

| Property Type | Units Required to be Leased |
|--------------|----------------------------|
| SFR/Townhome/Condo/PUD | 1 |
| 2 Unit | 1 |
| 3 Unit | 2 |
| 4 Unit | 2 |
| 5 Unit | 3 |
| 6 Unit | 3 |
| 7 Unit | 4 |
| 8 Unit | 4 |
| 9 Unit | 5 |

**For cross-collateralized portfolios:** The majority of properties must be leased to avoid the "vacant refinance" leverage reduction.

### 7.3.4 Market Rent Sources

Market rent is determined from the following sources in order of precedence:

1. **Appraisal Form 1007 / Market Rent Addendum** - Primary source
2. **RentRange Report** - Required for STR/Vacation rentals; optional for ambiguous situations
3. **Comparable Rent Analysis** - May be used to support or challenge appraisal rent

**10% Variance Rule:**
If a RentRange report is ordered and the variance between RentRange and appraisal market rent exceeds 10%, the lesser value is used for underwriting.

---

## 7.4 Monthly PITIA Components

### 7.4.1 Component Definitions

| Component | Definition | Source |
|-----------|-----------|--------|
| **Principal (P)** | Monthly principal payment based on loan amount, rate, and term | Calculated (see 7.4.2) |
| **Interest (I)** | Monthly interest payment based on loan amount and rate | Calculated (see 7.4.2) |
| **Taxes (T)** | Annual property taxes divided by 12 | Title report or appraisal |
| **Insurance (I)** | Annual insurance premium divided by 12 | Insurance quote/binder |
| **Association (A)** | Monthly HOA/association fees | HOA letter/statement |

### 7.4.2 Payment Calculation Methods

**Interest-Only Payment:**
```
Monthly Interest = (Loan Amount × Annual Interest Rate) / 12
```

**Amortizing Payment (P&I):**
```
Monthly P&I = Loan Amount × [r(1+r)^n] / [(1+r)^n - 1]

Where:
r = Monthly interest rate (Annual Rate / 12)
n = Number of payments (Term in months)
```

**Example - $400,000 Loan at 7.5% for 30 years:**
```
r = 0.075 / 12 = 0.00625
n = 360 months

Monthly P&I = $400,000 × [0.00625(1.00625)^360] / [(1.00625)^360 - 1]
Monthly P&I = $2,797.19
```

### 7.4.3 DSCR Calculation for Interest-Only vs. Amortizing

| Loan Structure | DSCR Calculation Basis |
|----------------|----------------------|
| Interest-Only (I/O) | Use interest-only payment for P&I |
| Fully Amortizing | Use fully amortizing P&I payment |
| Hybrid (I/O then Amortizing) | Use fully amortizing P&I payment |

**Important:** All I/O loans use accelerated amortization for DSCR calculation purposes. The DSCR is calculated using the fully amortizing payment to ensure the property can support the eventual amortizing payment.

### 7.4.4 Complete PITIA Example

**Property:** Single Family Residence
**Loan Amount:** $400,000
**Interest Rate:** 7.50%
**Term:** 30 years (10-year I/O)
**Annual Taxes:** $6,000
**Annual Insurance:** $2,400
**Monthly HOA:** $150

| Component | Monthly Amount |
|-----------|---------------|
| P&I (Amortizing) | $2,797.19 |
| Taxes | $500.00 |
| Insurance | $200.00 |
| Association | $150.00 |
| **Total PITIA** | **$3,647.19** |

**If Qualifying Rent = $4,000:**
```
DSCR = $4,000 / $3,647.19 = 1.097x
```

---

## 7.5 Minimum DSCR Requirements

### 7.5.1 Standard Minimum DSCR by FICO

| FICO Score | Minimum DSCR |
|------------|-------------|
| ≥ 700 | 1.00x |
| 680-699 | 1.00x |
| 660-679 | 1.00x |
| < 700 (with exception) | 1.20x |

**Note:** While the minimum program DSCR is 1.00x, borrowers with FICO scores below 700 may be subject to enhanced minimum DSCR requirements of 1.20x based on credit profile.

### 7.5.2 Special Scenario Minimum DSCR

| Scenario | Minimum DSCR | Notes |
|----------|-------------|-------|
| **5-9 Unit Properties** | 1.20x NCF | Uses Net Cash Flow calculation |
| **Foreign National** | 1.20x | Regardless of other factors |
| **DSCR < 1.00x** | Not eligible | Exception requires approval |
| **Multi-Collateral > $2M** | 1.20x NCF | Portfolio-level calculation |
| **Multi-Collateral > 10 properties** | 1.20x NCF | Portfolio-level calculation |

### 7.5.3 DSCR and Leverage Relationship

| DSCR Range | Pricing Impact | LTV Impact |
|------------|---------------|-----------|
| ≥ 1.30x (Foreign National) | Standard | +5% LTV allowed |
| ≥ 1.20x (700-719 FICO) | Standard | +5% LTV allowed |
| ≥ 1.15x | LLPA credit | N/A |
| 1.10x - 1.149x | Standard | N/A |
| 1.00x - 1.099x | LLPA hit | Limited LTV tiers |
| < 1.00x | Not eligible | N/A |

---

## 7.6 Lease Review Standards

### 7.6.1 Eligible Lease Characteristics

All leases must meet the following criteria:

| Requirement | Standard | Notes |
|-------------|----------|-------|
| **Arm's Length** | Required | No related party transactions |
| **Maximum Term** | 3 years | Longer leases not permitted |
| **Purchase Option** | Not permitted | No tenant purchase rights |
| **Currency** | USD only | Leases must be in U.S. dollars |
| **Use** | Residential only | No commercial tenants |
| **Structure** | Whole unit only | No room rentals (SRO) |
| **Sublease** | Not permitted | No subleases allowed |
| **Sale-Leaseback** | Not permitted | No cash-for-deeds |

### 7.6.2 Lease Verification Requirements

**For Existing Leases:**
1. Copy of current, fully executed lease agreement
2. Two (2) most recent consecutive rental payments verified via:
   - Check deposit records
   - Bank statement showing deposits
   - Certified tenant rental payment form
   - Property management ledger with payment history
   - Third-party payment processor verification

**For New Leases:**
- Proof of receipt of security deposit OR first month's rent
- Fully executed lease agreement

### 7.6.3 Month-to-Month Leases

Month-to-month arrangements are permitted under these conditions:

| Condition | Requirement |
|-----------|-------------|
| **Rolled from Initial Lease** | Initial lease term was minimum 12 months |
| **No Prior Lease** | Evidence of 3+ months verified rental payments |
| **Tenant Occupancy** | Tenant has resided in property for minimum 6 months |

### 7.6.4 Ineligible Lease Structures

The following lease types are **NOT** eligible:

- Single Room Occupancy (SRO)
- Individual room leases
- Boarder arrangements
- Subleases
- Commercial leases
- Corporate housing/leases to entities
- Leases with purchase options
- Leases exceeding 3 years
- Non-arm's length leases (related parties)

---

## 7.7 Short-Term Rental (STR) Analysis

### 7.7.1 STR Definition and Eligibility

Short-term rentals include properties marketed on platforms such as Airbnb, VRBO, or similar vacation rental services.

**Eligibility Requirements:**
- Verification of active online listing
- Property management agreement (if not self-managed)
- Annual income statement with trailing 12-month rental history

### 7.7.2 STR Qualifying Rent Calculation

```
STR Qualifying Rent = MIN(125% × Market Rent, Average Monthly STR Income)

Average Monthly STR Income = Total Trailing 12-Month STR Revenue / 12
```

**Example:**
- Market Rent: $2,000/month
- 125% of Market Rent: $2,500/month
- Trailing 12-Month STR Revenue: $36,000
- Average Monthly STR Income: $3,000/month
- **Qualifying Rent: MIN($2,500, $3,000) = $2,500**

### 7.7.3 STR Documentation Requirements

| Document | Requirement |
|----------|-------------|
| **Online Listing** | Screenshot/URL verification |
| **Income Statement** | 12-month trailing income summary |
| **RentRange Report** | Required for all STR properties |
| **Platform Verification** | Airbnb/VRBO account confirmation |
| **Property Management** | Agreement required if 3rd party managed |

### 7.7.4 STR Leverage and Pricing Impact

| Impact Type | Adjustment |
|-------------|-----------|
| **LTV Reduction** | -5% (Max 70% LTV) |
| **DSCR Calculation** | Capped at 100% market rent for pricing |
| **Production Limit** | No more than 10% of lender production |

### 7.7.5 STR Income Verification (AirDNA)

For all STR refinances and purchases, income patterns must be verified using the AirDNA Rentalizer tool:

**Required Information:**
- Property-specific annual revenue
- Nightly rent rates
- Occupancy percentage for trailing 12 months
- For new purchases: all available months since purchase

---

## 7.8 Section 8 / Subsidized Housing

### 7.8.1 Eligibility

Section 8, Section 42 (LIHTC), and Housing Choice Voucher (HCV) program properties are eligible with additional review requirements.

### 7.8.2 Qualifying Rent for Subsidized Properties

| Component | Treatment |
|-----------|----------|
| **Contract Rent** | Use full contract rent from HAP contract |
| **Tenant Portion** | Include in total qualifying rent |
| **Subsidy Portion** | Include in total qualifying rent |

**Verification Required:**
- Current Housing Assistance Payment (HAP) contract
- Verification of subsidy amount and term
- Landlord payment history from housing authority

### 7.8.3 Subsidized Housing Leverage Impact

| Adjustment | Amount |
|-----------|--------|
| LTV Reduction | -5% |
| DSCR Requirement | Standard minimums apply |

---

## 7.9 5-9 Unit Small Multifamily Analysis

### 7.9.1 Enhanced Underwriting Requirements

Properties with 5-9 units require more comprehensive analysis:

| Requirement | Standard |
|-------------|----------|
| **DSCR Basis** | Net Cash Flow (NCF) |
| **Minimum DSCR** | 1.20x NCF |
| **Minimum FICO** | 720 |
| **Maximum LTV (Purchase)** | 75% |
| **Maximum LTV (Refinance)** | 70% |
| **Appraisal Type** | Full MAI/Narrative |
| **Minimum Occupancy** | 80% |

### 7.9.2 NCF DSCR Calculation Example

**Property:** 6-Unit Apartment Building
**Gross Monthly Rent:** $9,000
**Annual Gross Rent:** $108,000

**Operating Expenses (Annual):**
| Expense | Amount |
|---------|--------|
| Property Management (8%) | $8,640 |
| Repairs & Maintenance ($500 × 6) | $3,000 |
| Insurance | $4,800 |
| Property Taxes | $12,000 |
| Utilities (Owner-Paid) | $3,600 |
| Turnover/Vacancy (5%) | $5,400 |
| Other Expenses | $2,400 |
| **Total Operating Expenses** | **$39,840** |

**Capital Expenditures ($300 × 6):** $1,800

**Net Operating Income:** $108,000 - $39,840 = $68,160
**Net Cash Flow:** $68,160 - $1,800 = $66,360
**Monthly NCF:** $66,360 / 12 = $5,530

**Debt Service (Loan: $600,000 @ 7.5%, 30-year amort):**
Monthly P&I: $4,195.79

**NCF DSCR:** $5,530 / $4,195.79 = **1.318x** ✓

### 7.9.3 5-9 Unit Rent Roll Requirements

| Requirement | Standard |
|-------------|----------|
| **Format** | Current rent roll with all units |
| **Lease Status** | Each unit's lease status and term |
| **Rent Amounts** | Current rent and market rent per unit |
| **Vacancy** | Duration and reason for vacant units |
| **Delinquency** | Any past-due tenant balances |

---

## 7.10 Market Rent Validation

### 7.10.1 Appraisal Market Rent Requirements

Market rent must be supported by the appraisal using Form 1007 / Market Rent Addendum with:

- Minimum 3 comparable rentals
- Comparables within same market area
- Similar property type and unit count
- Rent comparisons within 6 months preferred

### 7.10.2 Rent-to-Value Analysis

As a reasonableness check, evaluate the rent-to-value ratio:

```
Monthly Rent-to-Value = Monthly Rent / Property Value × 100

Annual Gross Rent Multiplier (GRM) = Property Value / Annual Rent
```

**Typical Ranges:**
| Market Type | Monthly Rent/Value | GRM Range |
|-------------|-------------------|-----------|
| High Growth | 0.4% - 0.6% | 14-20 |
| Stable | 0.6% - 0.9% | 9-14 |
| Cash Flow | 0.9% - 1.2% | 7-11 |

### 7.10.3 Market Rent Variance Handling

| Variance | Action |
|----------|--------|
| ≤ 10% | Use appraisal market rent |
| > 10% | Use lesser of appraisal and secondary source |
| > 20% | Additional documentation required |

---

## 7.11 DSCR Calculation Examples

### 7.11.1 Example 1: Standard Leased Purchase

**Scenario:** SFR purchase, leased property, strong FICO

| Input | Value |
|-------|-------|
| Property Value | $400,000 |
| Loan Amount | $320,000 (80% LTV) |
| Interest Rate | 7.25% |
| Term | 30 years |
| In-Place Rent | $2,600/month |
| Market Rent | $2,500/month |
| Annual Taxes | $4,800 |
| Annual Insurance | $1,800 |
| HOA | $0 |
| FICO | 740 |

**Qualifying Rent:** MIN($2,600, $2,500 × 105%) = MIN($2,600, $2,625) = **$2,600**

**Monthly PITIA:**
- P&I: $2,182.78
- Taxes: $400.00
- Insurance: $150.00
- HOA: $0
- **Total: $2,732.78**

**DSCR:** $2,600 / $2,732.78 = **0.951x** ❌ (Below 1.00x minimum)

**Solution:** Reduce loan amount to achieve 1.00x DSCR or decline.

### 7.11.2 Example 2: Vacant Refinance

**Scenario:** SFR refinance, vacant property, moderate FICO

| Input | Value |
|-------|-------|
| Property Value | $350,000 |
| Base Max LTV | 75% (680-699 FICO) |
| Adjusted Max LTV | 65% (10% vacant reduction) |
| Loan Amount | $227,500 |
| Interest Rate | 7.50% |
| Market Rent | $2,200/month |
| Annual Taxes | $4,200 |
| Annual Insurance | $1,500 |
| FICO | 690 |

**Qualifying Rent:** $2,200 × 100% = **$2,200** (Full market rent, no haircut)

**Monthly PITIA:**
- P&I: $1,590.82
- Taxes: $350.00
- Insurance: $125.00
- **Total: $2,065.82**

**DSCR:** $2,200 / $2,065.82 = **1.065x** ✓ (Meets 1.00x minimum)

**Note:** Vacant refinances receive a 10% LTV reduction per EastView guidelines, but use 100% of market rent for DSCR calculation.

### 7.11.3 Example 3: Short-Term Rental

**Scenario:** STR purchase with Airbnb income history

| Input | Value |
|-------|-------|
| Property Value | $500,000 |
| Max LTV | 70% (STR reduction) |
| Loan Amount | $350,000 |
| Interest Rate | 7.375% |
| Market Rent | $2,800/month |
| Trailing 12-Month STR Income | $48,000 |
| Average Monthly STR | $4,000 |
| Annual Taxes | $6,000 |
| Annual Insurance | $2,400 |
| FICO | 760 |

**Qualifying Rent:** MIN($2,800 × 125%, $4,000) = MIN($3,500, $4,000) = **$3,500**

**Monthly PITIA:**
- P&I: $2,418.17
- Taxes: $500.00
- Insurance: $200.00
- **Total: $3,118.17**

**DSCR:** $3,500 / $3,118.17 = **1.122x** ✓

### 7.11.4 Example 4: Foreign National

**Scenario:** Foreign National purchase

| Input | Value |
|-------|-------|
| Property Value | $425,000 |
| Max LTV | 65% (FN Base) |
| Loan Amount | $276,250 |
| Interest Rate | 7.625% |
| In-Place Rent | $2,400/month |
| Market Rent | $2,350/month |
| Annual Taxes | $5,100 |
| Annual Insurance | $1,700 |
| FICO | N/A (Foreign National) |
| Minimum DSCR | 1.20x |

**Qualifying Rent:** MIN($2,400, $2,350 × 105%) = MIN($2,400, $2,467.50) = **$2,400**

**Monthly PITIA:**
- P&I: $1,969.54
- Taxes: $425.00
- Insurance: $141.67
- **Total: $2,536.21**

**DSCR:** $2,400 / $2,536.21 = **0.946x** ❌ (Below 1.20x FN minimum)

**Solution:** If DSCR ≥ 1.30x, FN would qualify for +5% LTV. Current scenario requires loan reduction.

---

## 7.12 Python Implementation

```python
"""
DSCR Property & Income Analysis Module
USDV Capital Underwriting Library

This module provides comprehensive DSCR calculation functionality
including qualifying rent determination, PITIA calculation, and
minimum DSCR validation for all property and borrower scenarios.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List, Tuple
from decimal import Decimal, ROUND_HALF_UP
import math


class LeaseStatus(Enum):
    """Lease status classification."""
    LEASED = "leased"
    UNLEASED = "unleased"
    MONTH_TO_MONTH = "month_to_month"


class LoanPurpose(Enum):
    """Loan purpose classification."""
    PURCHASE = "purchase"
    RATE_TERM_REFINANCE = "rate_term_refinance"
    CASH_OUT_REFINANCE = "cash_out_refinance"


class PropertyType(Enum):
    """Property type classification for DSCR."""
    SFR = "sfr"
    TOWNHOME = "townhome"
    CONDO = "condo"
    PUD = "pud"
    TWO_UNIT = "2_unit"
    THREE_UNIT = "3_unit"
    FOUR_UNIT = "4_unit"
    SMALL_MULTIFAMILY = "5_9_unit"  # 5-9 units


class RentalType(Enum):
    """Rental arrangement type."""
    LONG_TERM = "long_term"
    SHORT_TERM = "short_term"  # Airbnb, VRBO, etc.
    SECTION_8 = "section_8"
    SUBSIDIZED = "subsidized"


@dataclass
class UnitRent:
    """Rental information for a single unit."""
    unit_number: int
    in_place_rent: float
    market_rent: float
    is_leased: bool
    lease_start_date: Optional[str] = None
    lease_end_date: Optional[str] = None
    is_section_8: bool = False
    contract_rent: Optional[float] = None  # For Section 8


@dataclass
class PropertyExpenses:
    """Property operating expenses for NCF calculation."""
    property_management: float = 0.0
    repairs_maintenance: float = 0.0
    insurance: float = 0.0
    property_taxes: float = 0.0
    hoa_fees: float = 0.0
    utilities: float = 0.0
    turnover_costs: float = 0.0
    marketing_leasing: float = 0.0
    other_expenses: float = 0.0
    capital_expenditures: float = 0.0

    @property
    def total_operating_expenses(self) -> float:
        """Calculate total annual operating expenses."""
        return (
            self.property_management +
            self.repairs_maintenance +
            self.insurance +
            self.property_taxes +
            self.hoa_fees +
            self.utilities +
            self.turnover_costs +
            self.marketing_leasing +
            self.other_expenses
        )

    @property
    def total_expenses_with_capex(self) -> float:
        """Calculate total expenses including capital expenditures."""
        return self.total_operating_expenses + self.capital_expenditures


@dataclass
class QualifyingRentResult:
    """Result of qualifying rent calculation."""
    qualifying_rent: float
    calculation_method: str
    in_place_rent: Optional[float]
    market_rent: float
    market_rent_cap: float  # 105% or 100% depending on scenario
    haircut_applied: Optional[float] = None  # For vacant refi
    notes: List[str] = field(default_factory=list)


@dataclass
class PITIAResult:
    """Monthly PITIA calculation result."""
    principal_interest: float
    taxes: float
    insurance: float
    association: float
    total_pitia: float
    is_interest_only: bool
    amortizing_payment: float  # For I/O loans, shows what amort would be


@dataclass
class DSCRResult:
    """Complete DSCR analysis result."""
    dscr: float
    qualifying_rent: float
    monthly_pitia: float
    minimum_required_dscr: float
    meets_minimum: bool
    loan_amount: float
    interest_rate: float
    property_value: float
    ltv: float
    calculation_basis: str  # "PITIA" or "NCF"
    qualifying_rent_details: QualifyingRentResult
    pitia_details: PITIAResult
    notes: List[str] = field(default_factory=list)
    max_loan_at_min_dscr: Optional[float] = None


class DSCRCalculator:
    """
    Calculate DSCR for loan sizing and validation.

    This class implements the full DSCR calculation methodology
    per USDV Capital underwriting guidelines.
    """

    # Market rent caps by scenario
    MARKET_RENT_CAP_LEASED = 1.05  # 105% for leased properties
    MARKET_RENT_CAP_UNLEASED = 1.00  # 100% for unleased
    MARKET_RENT_CAP_STR = 1.25  # 125% for short-term rentals

    # Vacant refinance adjustments (EastView standard)
    VACANT_REFI_RENT_FACTOR = 1.00  # 100% of market rent (no haircut)
    VACANT_REFI_LTV_REDUCTION = 0.10  # 10% LTV reduction

    # Minimum DSCR requirements
    MIN_DSCR_STANDARD = 1.00
    MIN_DSCR_LOW_FICO = 1.20  # FICO < 700 with elevated risk
    MIN_DSCR_FOREIGN_NATIONAL = 1.20
    MIN_DSCR_MULTIFAMILY = 1.20  # 5-9 units NCF basis

    # NCF calculation constants
    CAPEX_PER_UNIT_MULTIUNIT = 300
    CAPEX_NEW_CONSTRUCTION_SFR = 400
    CAPEX_EXISTING_SFR = 600
    REPAIRS_PER_UNIT_MULTIUNIT = 500
    REPAIRS_NEW_CONSTRUCTION_SFR = 500
    REPAIRS_EXISTING_SFR = 700

    def calculate_monthly_pi(
        self,
        loan_amount: float,
        annual_rate: float,
        term_months: int,
        io_months: int = 0
    ) -> Tuple[float, float]:
        """
        Calculate monthly P&I payment.

        Args:
            loan_amount: Total loan amount
            annual_rate: Annual interest rate (as decimal, e.g., 0.075 for 7.5%)
            term_months: Total loan term in months
            io_months: Interest-only period in months (0 for fully amortizing)

        Returns:
            Tuple of (interest_only_payment, amortizing_payment)
        """
        if loan_amount <= 0 or annual_rate <= 0:
            return (0.0, 0.0)

        monthly_rate = annual_rate / 12

        # Interest-only payment
        io_payment = loan_amount * monthly_rate

        # Amortizing payment
        if monthly_rate > 0:
            amort_payment = loan_amount * (
                (monthly_rate * (1 + monthly_rate) ** term_months) /
                ((1 + monthly_rate) ** term_months - 1)
            )
        else:
            amort_payment = loan_amount / term_months

        return (round(io_payment, 2), round(amort_payment, 2))

    def calculate_monthly_pitia(
        self,
        loan_amount: float,
        annual_rate: float,
        term_months: int,
        annual_taxes: float,
        annual_insurance: float,
        monthly_hoa: float = 0.0,
        io_months: int = 0,
        use_amortizing_for_dscr: bool = True
    ) -> PITIAResult:
        """
        Calculate full monthly PITIA.

        Args:
            loan_amount: Total loan amount
            annual_rate: Annual interest rate (as decimal)
            term_months: Total loan term in months
            annual_taxes: Annual property taxes
            annual_insurance: Annual insurance premium
            monthly_hoa: Monthly HOA/association fees
            io_months: Interest-only period in months
            use_amortizing_for_dscr: If True, use amortizing P&I for DSCR calc

        Returns:
            PITIAResult with all components
        """
        io_payment, amort_payment = self.calculate_monthly_pi(
            loan_amount, annual_rate, term_months, io_months
        )

        monthly_taxes = annual_taxes / 12
        monthly_insurance = annual_insurance / 12

        # For DSCR calculation, typically use amortizing payment
        # even during I/O period
        pi_for_dscr = amort_payment if use_amortizing_for_dscr else io_payment

        total_pitia = pi_for_dscr + monthly_taxes + monthly_insurance + monthly_hoa

        return PITIAResult(
            principal_interest=round(pi_for_dscr, 2),
            taxes=round(monthly_taxes, 2),
            insurance=round(monthly_insurance, 2),
            association=round(monthly_hoa, 2),
            total_pitia=round(total_pitia, 2),
            is_interest_only=(io_months > 0),
            amortizing_payment=round(amort_payment, 2)
        )

    def determine_qualifying_rent(
        self,
        in_place_rent: Optional[float],
        market_rent: float,
        is_leased: bool,
        loan_purpose: LoanPurpose,
        rental_type: RentalType = RentalType.LONG_TERM,
        str_avg_income: float = 0.0,
        contract_rent: Optional[float] = None  # For Section 8
    ) -> QualifyingRentResult:
        """
        Determine qualifying rent based on scenario.

        Args:
            in_place_rent: Current lease rent (None if vacant)
            market_rent: Appraised market rent
            is_leased: Whether property has active lease
            loan_purpose: Purchase, R&T Refi, or Cash-Out Refi
            rental_type: Long-term, STR, Section 8, etc.
            str_avg_income: Average monthly STR income (for STR properties)
            contract_rent: Section 8 contract rent

        Returns:
            QualifyingRentResult with calculation details
        """
        notes = []
        haircut = None

        # Section 8 handling
        if rental_type == RentalType.SECTION_8 and contract_rent:
            return QualifyingRentResult(
                qualifying_rent=contract_rent,
                calculation_method="Section 8 Contract Rent",
                in_place_rent=in_place_rent,
                market_rent=market_rent,
                market_rent_cap=1.00,
                notes=["Section 8 contract rent verified from HAP contract"]
            )

        # Short-Term Rental handling
        if rental_type == RentalType.SHORT_TERM:
            str_cap = market_rent * self.MARKET_RENT_CAP_STR
            qualifying = min(str_cap, str_avg_income) if str_avg_income > 0 else str_cap
            notes.append(f"STR qualifying rent capped at MIN(125% market, avg income)")
            return QualifyingRentResult(
                qualifying_rent=round(qualifying, 2),
                calculation_method="Short-Term Rental",
                in_place_rent=in_place_rent,
                market_rent=market_rent,
                market_rent_cap=self.MARKET_RENT_CAP_STR,
                notes=notes
            )

        # Standard long-term rental scenarios
        is_refinance = loan_purpose in [
            LoanPurpose.RATE_TERM_REFINANCE,
            LoanPurpose.CASH_OUT_REFINANCE
        ]

        if is_leased and in_place_rent:
            # Leased property: MIN(in-place, 105% market)
            market_cap = market_rent * self.MARKET_RENT_CAP_LEASED
            qualifying = min(in_place_rent, market_cap)
            method = f"Leased: MIN(in-place ${in_place_rent:,.0f}, 105% market ${market_cap:,.0f})"
            cap_used = self.MARKET_RENT_CAP_LEASED

        elif not is_leased and is_refinance:
            # Vacant refinance: 100% of market rent, 10% LTV reduction (EastView standard)
            qualifying = market_rent * self.VACANT_REFI_RENT_FACTOR
            haircut = None  # No rent haircut under EastView standard
            method = "Vacant Refinance: 100% of market rent"
            cap_used = self.MARKET_RENT_CAP_UNLEASED
            notes.append("10% LTV reduction applies for vacant refinance (see Section 10)")

        else:
            # Unleased purchase: 100% of market rent
            qualifying = market_rent * self.MARKET_RENT_CAP_UNLEASED
            method = "Unleased Purchase: 100% of market rent"
            cap_used = self.MARKET_RENT_CAP_UNLEASED

        return QualifyingRentResult(
            qualifying_rent=round(qualifying, 2),
            calculation_method=method,
            in_place_rent=in_place_rent,
            market_rent=market_rent,
            market_rent_cap=cap_used,
            haircut_applied=haircut,
            notes=notes
        )

    def calculate_qualifying_rent_multiunit(
        self,
        units: List[UnitRent],
        loan_purpose: LoanPurpose
    ) -> Tuple[float, List[QualifyingRentResult]]:
        """
        Calculate total qualifying rent for multi-unit properties.

        Args:
            units: List of UnitRent objects for each unit
            loan_purpose: Loan purpose

        Returns:
            Tuple of (total_qualifying_rent, list of per-unit results)
        """
        total_rent = 0.0
        unit_results = []

        for unit in units:
            rental_type = RentalType.SECTION_8 if unit.is_section_8 else RentalType.LONG_TERM

            result = self.determine_qualifying_rent(
                in_place_rent=unit.in_place_rent if unit.is_leased else None,
                market_rent=unit.market_rent,
                is_leased=unit.is_leased,
                loan_purpose=loan_purpose,
                rental_type=rental_type,
                contract_rent=unit.contract_rent
            )

            total_rent += result.qualifying_rent
            unit_results.append(result)

        return (round(total_rent, 2), unit_results)

    def get_minimum_dscr(
        self,
        fico: Optional[int],
        units: int,
        is_foreign_national: bool,
        is_elevated_risk: bool = False
    ) -> float:
        """
        Get minimum DSCR requirement for scenario.

        Args:
            fico: Credit score (None for Foreign National)
            units: Number of units in property
            is_foreign_national: Whether borrower is foreign national
            is_elevated_risk: Whether loan has elevated risk factors

        Returns:
            Minimum required DSCR
        """
        # Foreign nationals always require 1.20x
        if is_foreign_national:
            return self.MIN_DSCR_FOREIGN_NATIONAL

        # 5-9 unit properties require 1.20x NCF
        if units >= 5:
            return self.MIN_DSCR_MULTIFAMILY

        # Low FICO with elevated risk
        if fico and fico < 700 and is_elevated_risk:
            return self.MIN_DSCR_LOW_FICO

        # Standard minimum
        return self.MIN_DSCR_STANDARD

    def calculate_dscr(
        self,
        qualifying_rent: float,
        monthly_pitia: float
    ) -> float:
        """
        Calculate DSCR ratio.

        Args:
            qualifying_rent: Monthly qualifying rent
            monthly_pitia: Monthly PITIA payment

        Returns:
            DSCR ratio rounded to 3 decimal places
        """
        if monthly_pitia <= 0:
            return 0.0

        dscr = qualifying_rent / monthly_pitia
        return round(dscr, 3)

    def calculate_ncf_dscr(
        self,
        gross_annual_rent: float,
        expenses: PropertyExpenses,
        annual_debt_service: float
    ) -> float:
        """
        Calculate NCF DSCR for 5-9 unit properties.

        Args:
            gross_annual_rent: Total annual gross rent
            expenses: PropertyExpenses object with all expenses
            annual_debt_service: Annual debt service (P&I × 12)

        Returns:
            NCF DSCR ratio
        """
        if annual_debt_service <= 0:
            return 0.0

        net_cash_flow = gross_annual_rent - expenses.total_expenses_with_capex
        ncf_dscr = net_cash_flow / annual_debt_service

        return round(ncf_dscr, 3)

    def calculate_max_loan_for_dscr(
        self,
        target_dscr: float,
        qualifying_rent: float,
        annual_rate: float,
        term_months: int,
        annual_taxes: float,
        annual_insurance: float,
        monthly_hoa: float = 0.0
    ) -> float:
        """
        Calculate maximum loan amount to achieve target DSCR.

        This iteratively solves for the loan amount that produces
        the target DSCR given fixed property expenses.

        Args:
            target_dscr: Target DSCR (e.g., 1.00)
            qualifying_rent: Monthly qualifying rent
            annual_rate: Annual interest rate (as decimal)
            term_months: Loan term in months
            annual_taxes: Annual property taxes
            annual_insurance: Annual insurance premium
            monthly_hoa: Monthly HOA fees

        Returns:
            Maximum loan amount
        """
        # Fixed monthly costs (T+I+A)
        fixed_costs = (annual_taxes + annual_insurance) / 12 + monthly_hoa

        # Maximum allowable P&I to hit target DSCR
        max_pi = (qualifying_rent / target_dscr) - fixed_costs

        if max_pi <= 0:
            return 0.0

        # Solve for loan amount from P&I payment
        monthly_rate = annual_rate / 12

        if monthly_rate > 0:
            # P&I = L * [r(1+r)^n] / [(1+r)^n - 1]
            # Solving for L:
            # L = P&I * [(1+r)^n - 1] / [r(1+r)^n]
            factor = (1 + monthly_rate) ** term_months
            loan_amount = max_pi * (factor - 1) / (monthly_rate * factor)
        else:
            loan_amount = max_pi * term_months

        return round(loan_amount, 2)

    def full_dscr_analysis(
        self,
        loan_amount: float,
        property_value: float,
        annual_rate: float,
        term_months: int,
        annual_taxes: float,
        annual_insurance: float,
        monthly_hoa: float,
        in_place_rent: Optional[float],
        market_rent: float,
        is_leased: bool,
        loan_purpose: LoanPurpose,
        fico: Optional[int],
        units: int = 1,
        is_foreign_national: bool = False,
        rental_type: RentalType = RentalType.LONG_TERM,
        str_avg_income: float = 0.0,
        io_months: int = 0
    ) -> DSCRResult:
        """
        Complete DSCR analysis with all components.

        Args:
            loan_amount: Proposed loan amount
            property_value: Property value
            annual_rate: Annual interest rate (as decimal)
            term_months: Loan term in months
            annual_taxes: Annual property taxes
            annual_insurance: Annual insurance premium
            monthly_hoa: Monthly HOA fees
            in_place_rent: Current lease rent
            market_rent: Appraised market rent
            is_leased: Whether property has active lease
            loan_purpose: Purchase, R&T Refi, or Cash-Out Refi
            fico: Credit score
            units: Number of units
            is_foreign_national: Foreign national borrower flag
            rental_type: Type of rental arrangement
            str_avg_income: Average STR income (for STR properties)
            io_months: Interest-only period

        Returns:
            Complete DSCRResult with all analysis details
        """
        notes = []

        # Calculate qualifying rent
        qualifying_rent_result = self.determine_qualifying_rent(
            in_place_rent=in_place_rent,
            market_rent=market_rent,
            is_leased=is_leased,
            loan_purpose=loan_purpose,
            rental_type=rental_type,
            str_avg_income=str_avg_income
        )

        # Calculate PITIA
        pitia_result = self.calculate_monthly_pitia(
            loan_amount=loan_amount,
            annual_rate=annual_rate,
            term_months=term_months,
            annual_taxes=annual_taxes,
            annual_insurance=annual_insurance,
            monthly_hoa=monthly_hoa,
            io_months=io_months,
            use_amortizing_for_dscr=True
        )

        # Calculate DSCR
        dscr = self.calculate_dscr(
            qualifying_rent=qualifying_rent_result.qualifying_rent,
            monthly_pitia=pitia_result.total_pitia
        )

        # Get minimum required DSCR
        min_dscr = self.get_minimum_dscr(
            fico=fico,
            units=units,
            is_foreign_national=is_foreign_national
        )

        # Check if meets minimum
        meets_minimum = dscr >= min_dscr

        # Calculate LTV
        ltv = loan_amount / property_value if property_value > 0 else 0

        # Add relevant notes
        if is_foreign_national:
            notes.append("Foreign National: 1.20x minimum DSCR required")

        if rental_type == RentalType.SHORT_TERM:
            notes.append("STR property: 5% LTV reduction applies")

        if not is_leased and loan_purpose in [
            LoanPurpose.RATE_TERM_REFINANCE,
            LoanPurpose.CASH_OUT_REFINANCE
        ]:
            notes.append("Vacant refinance: 10% LTV reduction applies")

        if not meets_minimum:
            notes.append(f"DSCR {dscr:.3f}x below minimum {min_dscr:.2f}x")

            # Calculate max loan at minimum DSCR
            max_loan = self.calculate_max_loan_for_dscr(
                target_dscr=min_dscr,
                qualifying_rent=qualifying_rent_result.qualifying_rent,
                annual_rate=annual_rate,
                term_months=term_months,
                annual_taxes=annual_taxes,
                annual_insurance=annual_insurance,
                monthly_hoa=monthly_hoa
            )
            notes.append(f"Max loan at {min_dscr:.2f}x DSCR: ${max_loan:,.0f}")
        else:
            max_loan = None

        return DSCRResult(
            dscr=dscr,
            qualifying_rent=qualifying_rent_result.qualifying_rent,
            monthly_pitia=pitia_result.total_pitia,
            minimum_required_dscr=min_dscr,
            meets_minimum=meets_minimum,
            loan_amount=loan_amount,
            interest_rate=annual_rate,
            property_value=property_value,
            ltv=round(ltv, 4),
            calculation_basis="PITIA" if units < 5 else "NCF",
            qualifying_rent_details=qualifying_rent_result,
            pitia_details=pitia_result,
            notes=notes,
            max_loan_at_min_dscr=max_loan
        )


class NCFCalculator:
    """
    Net Cash Flow calculator for 5-9 unit properties.

    Implements the NCF DSCR methodology with standardized
    expense assumptions per underwriting guidelines.
    """

    # Default expense assumptions
    PROPERTY_MANAGEMENT_RATE = 0.08  # 8% of gross rent
    VACANCY_RATE = 0.05  # 5% vacancy/turnover

    def calculate_standard_expenses(
        self,
        gross_annual_rent: float,
        units: int,
        annual_taxes: float,
        annual_insurance: float,
        annual_hoa: float = 0.0,
        is_new_construction: bool = False,
        annual_utilities: float = 0.0
    ) -> PropertyExpenses:
        """
        Calculate standardized expenses for NCF DSCR.

        Args:
            gross_annual_rent: Annual gross rental income
            units: Number of units
            annual_taxes: Annual property taxes
            annual_insurance: Annual insurance
            annual_hoa: Annual HOA fees
            is_new_construction: Whether property is new construction
            annual_utilities: Annual owner-paid utilities

        Returns:
            PropertyExpenses object with all calculated expenses
        """
        # Property management at 8%
        property_management = gross_annual_rent * self.PROPERTY_MANAGEMENT_RATE

        # Repairs & maintenance based on unit count
        if units > 1:
            repairs = DSCRCalculator.REPAIRS_PER_UNIT_MULTIUNIT * units
        elif is_new_construction:
            repairs = DSCRCalculator.REPAIRS_NEW_CONSTRUCTION_SFR
        else:
            repairs = DSCRCalculator.REPAIRS_EXISTING_SFR

        # Capital expenditures based on unit count
        if units > 1:
            capex = DSCRCalculator.CAPEX_PER_UNIT_MULTIUNIT * units
        elif is_new_construction:
            capex = DSCRCalculator.CAPEX_NEW_CONSTRUCTION_SFR
        else:
            capex = DSCRCalculator.CAPEX_EXISTING_SFR

        # Turnover/vacancy allowance
        turnover = gross_annual_rent * self.VACANCY_RATE

        return PropertyExpenses(
            property_management=property_management,
            repairs_maintenance=repairs,
            insurance=annual_insurance,
            property_taxes=annual_taxes,
            hoa_fees=annual_hoa,
            utilities=annual_utilities,
            turnover_costs=turnover,
            capital_expenditures=capex
        )

    def calculate_ncf(
        self,
        gross_annual_rent: float,
        expenses: PropertyExpenses
    ) -> Tuple[float, float, float]:
        """
        Calculate Net Cash Flow.

        Args:
            gross_annual_rent: Annual gross rental income
            expenses: PropertyExpenses object

        Returns:
            Tuple of (NOI, NCF, monthly_NCF)
        """
        noi = gross_annual_rent - expenses.total_operating_expenses
        ncf = noi - expenses.capital_expenditures
        monthly_ncf = ncf / 12

        return (round(noi, 2), round(ncf, 2), round(monthly_ncf, 2))


# Convenience functions for common scenarios

def quick_dscr_check(
    monthly_rent: float,
    loan_amount: float,
    rate: float,
    annual_taxes: float,
    annual_insurance: float,
    monthly_hoa: float = 0.0,
    term_years: int = 30
) -> Tuple[float, bool]:
    """
    Quick DSCR check for initial screening.

    Args:
        monthly_rent: Monthly qualifying rent
        loan_amount: Loan amount
        rate: Annual interest rate (as decimal)
        annual_taxes: Annual property taxes
        annual_insurance: Annual insurance
        monthly_hoa: Monthly HOA
        term_years: Loan term in years

    Returns:
        Tuple of (DSCR, meets_1.00x_minimum)
    """
    calc = DSCRCalculator()

    pitia = calc.calculate_monthly_pitia(
        loan_amount=loan_amount,
        annual_rate=rate,
        term_months=term_years * 12,
        annual_taxes=annual_taxes,
        annual_insurance=annual_insurance,
        monthly_hoa=monthly_hoa
    )

    dscr = calc.calculate_dscr(monthly_rent, pitia.total_pitia)

    return (dscr, dscr >= 1.00)


def calculate_max_loan_amount(
    monthly_rent: float,
    rate: float,
    annual_taxes: float,
    annual_insurance: float,
    monthly_hoa: float = 0.0,
    target_dscr: float = 1.00,
    term_years: int = 30
) -> float:
    """
    Calculate maximum loan amount for target DSCR.

    Args:
        monthly_rent: Monthly qualifying rent
        rate: Annual interest rate (as decimal)
        annual_taxes: Annual property taxes
        annual_insurance: Annual insurance
        monthly_hoa: Monthly HOA
        target_dscr: Target DSCR (default 1.00)
        term_years: Loan term in years

    Returns:
        Maximum loan amount
    """
    calc = DSCRCalculator()

    return calc.calculate_max_loan_for_dscr(
        target_dscr=target_dscr,
        qualifying_rent=monthly_rent,
        annual_rate=rate,
        term_months=term_years * 12,
        annual_taxes=annual_taxes,
        annual_insurance=annual_insurance,
        monthly_hoa=monthly_hoa
    )
```

---

## 7.13 Flag Generation Rules (INSPIRE Phase 7)

The following flags are generated during automated DSCR analysis:

### 7.13.1 DSCR Flags

| Check | Pass (Green) | Warning (Yellow) | Fail (Red) |
|-------|-------------|------------------|-----------|
| DSCR vs Minimum | ≥ minimum + 0.10 | ≥ minimum | < minimum |
| DSCR Level | ≥ 1.20x | 1.00x - 1.19x | < 1.00x |
| Rent vs Market | ≤ 105% market | 105-115% market | > 115% market |
| NCF DSCR (5-9) | ≥ 1.30x | 1.20x - 1.29x | < 1.20x |

### 7.13.2 Lease Verification Flags

| Check | Pass (Green) | Warning (Yellow) | Fail (Red) |
|-------|-------------|------------------|-----------|
| Lease Term | ≤ 3 years | N/A | > 3 years |
| Arm's Length | Verified | Unable to verify | Related party |
| Payment History | 2+ months verified | 1 month verified | No verification |
| Purchase Option | None | N/A | Option exists |

### 7.13.3 Rent Variance Flags

| Check | Pass (Green) | Warning (Yellow) | Fail (Red) |
|-------|-------------|------------------|-----------|
| Appraisal vs RentRange | ≤ 5% variance | 5-10% variance | > 10% variance |
| In-Place vs Market | ≤ 110% market | 110-120% market | > 120% market |
| STR Income vs Cap | Below 125% cap | At 125% cap | Exceeds cap |

---

## 7.14 Cross-References

| Topic | Reference Section |
|-------|------------------|
| FICO Score Requirements | Section 4: Credit & Background Evaluation |
| Property Eligibility | Section 5: Property Eligibility Standards |
| LTV Matrices | Section 10: DSCR Loan Sizing & Leverage |
| Pricing Adjustments | Section 11: Pricing & Rate Calculations |
| Appraisal Review | Section 8: Appraisal & Valuation Review |
| Document Requirements | Section 13: Document Requirements |

---

## 7.15 Open Questions

1. **RentRange Variance Threshold:** Guidelines show 10% variance rule - confirm this applies equally to value and rent comparisons.

2. **STR Production Limit:** Some guidelines reference "no more than 10% of production" for STR - determine if this is a hard cap or guideline.

3. **NCF Expense Assumptions:** Confirm standardized expense percentages for property management and vacancy factors across all scenarios.

---

*End of Section 7: DSCR Property & Income Analysis*
