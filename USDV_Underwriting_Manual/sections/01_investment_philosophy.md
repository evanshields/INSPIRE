---
section: 1
title: Investment Philosophy & Loan Products
version: 1.1
last_updated: 2025-12-30
model_used: haiku
guideline_sources:
  - Archwest RTL Guidelines v6.0
  - Eastview RTL Guidelines v4.1
  - Archwest DSCR Guidelines v1.8
  - Eastview DSCR Guidelines v7.2
  - EV GUC Guidelines v1.0
changelog:
  - 2025-12-30: Updated with investor-validated parameters; added Bridge Plus product; corrected GUC terms and max loan amounts; updated Python code
  - 2025-12-30: Initial creation
---

# Section 1: Investment Philosophy & Loan Products

## 1.1 USDV Capital Mission & Lending Philosophy

### 1.1.1 Core Lending Focus

USDV Capital specializes in single-family residential business purpose lending for experienced real estate investors. Our lending philosophy centers on:

- **Business Purpose Only**: All loans are structured exclusively for investment and business purposes. Owner-occupied properties are not eligible under any circumstance.
- **Experienced Borrower Focus**: We partner with knowledgeable real estate professionals who understand value-add investing, rental property acquisition, and development.
- **Flexible Structuring**: Our loan products accommodate multiple transaction types including acquisitions with renovation, new construction, stabilized rental properties, and bridge financing scenarios.
- **Risk-Based Pricing**: Pricing reflects borrower strength (credit, experience, liquidity) and property characteristics (type, condition, market).

### 1.1.2 Business Purpose Certification

All borrowers must execute a Borrower Certification of Business Purpose stating that:

- The loan proceeds will be used exclusively for business/investment purposes
- The property will not be occupied as a primary residence
- The borrower understands all loan terms and conditions
- All information provided is accurate and complete

**Failure to comply with business purpose requirements results in automatic loan decline.**

---

## 1.2 Supported Loan Products

### 1.2.1 Fix & Flip (RTL - Renovation Transitional Loan)

**Product Overview:**
The Fix & Flip loan provides acquisition and renovation financing for single-family and small multifamily properties with a clear exit strategy through refinance or sale.

**Intended Use:**
- Acquire property below market value due to condition or distress
- Renovate/rehabilitate to achieve market-ready condition
- Exit through sale to owner-occupant buyer or refinance to permanent loan

**Typical Transaction Flow:**
```
Purchase (60-90 days) → Renovation (3-6 months) → Exit (sale or refi)
```

**Borrower Profile:**
- Active real estate investors with renovation experience
- Strong credit and liquidity
- Market knowledge in target area

**Key Characteristics:**
- Short-term financing (12-24 months)
- Interest-only payments during construction phase
- Rehab budget holdback for quality assurance
- Value-add focus (purchase discount + renovation value)

---

### 1.2.2 Ground-Up Construction (GUC)

**Product Overview:**
The GUC loan finances construction of a new single-family residence on owned or to-be-purchased land. This product is exclusively for infill vertical development on entitled land.

**Intended Use:**
- Land acquisition or use of existing land (must be entitled)
- New construction to market-ready condition
- Exit through sale to owner-occupant or conversion to permanent rental

**Typical Transaction Flow:**
```
Land Acquisition (0-30 days) → Construction (4-12 months) → Exit (sale or refi)
```

**Borrower Profile:**
- Experienced builders or investor-developers with demonstrated construction experience
- Strong relationships with general contractors
- Market understanding in target development area
- Minimum 3 deals in last 36 months OR 2 deals + Licensed GC + 2x liquidity + 720 FICO

**Key Characteristics:**
- Construction-phase financing with draw schedules
- Interest-only payments during construction
- Construction budget tracking with lender approval
- Permit and architectural plan requirements
- Entitled land requirement (not suitable for raw land development)

---

### 1.2.3 Bridge Loan

**Product Overview:**
The Bridge loan provides short-term financing for stabilized or near-stabilized properties, ideal for time-gap scenarios or transitional situations.

**Intended Use:**
- Acquire stabilized rental property and stabilize further (value-add bridge)
- Temporary financing pending refinance to permanent loan
- Portfolio acquisition bridge pending individual property financing
- Hold property during market transition

**Typical Transaction Flow:**
```
Purchase → Hold/Stabilize/Improve (12-24 months) → Refinance or Sale
```

**Borrower Profile:**
- Active investors or operators with investment experience
- Property stabilization expertise
- Access to rental income or exit capital

**Key Characteristics:**
- Medium-term financing (12-24 months standard)
- Interest-only payments
- Based on stabilized property fundamentals
- Flexible exit scenarios

---

### 1.2.4 Bridge Plus (Extended Bridge)

**Product Overview:**
Bridge Plus is an extended bridge product for stabilized properties with documented rental income, structured as permanent-like rental financing with interest-only terms. This product bridges the gap between traditional bridge loans and DSCR permanent financing.

**Intended Use:**
- Stabilized rental properties with documented income stream
- Extended hold periods (25-36 months) before permanent refinance
- Portfolio consolidation with rental income focus
- Transition strategy to DSCR permanent financing

**Typical Transaction Flow:**
```
Purchase (Stabilized) → Hold (25-36 months, rental income) → Refinance to DSCR or Sale
```

**Borrower Profile:**
- Rental property operators with documented management experience
- Demonstrated rental income from property or similar properties
- Strong operational infrastructure

**Key Characteristics:**
- Extended terms (25-36 months)
- Interest-only payments
- DSCR-based qualification (minimum 1.00x for leased, 1.10x for vacant)
- Rental income documentation required
- Exit strategy: refinance to DSCR or sale

**Note:** Bridge Plus is available through EastView as an RTL product. Availability may vary by investor partner.

---

### 1.2.5 DSCR (Debt Service Coverage Ratio) Permanent Loan

**Product Overview:**
The DSCR loan is permanent financing for stabilized rental properties, underwritten on the property's ability to generate sufficient rental income to cover debt service.

**Intended Use:**
- Acquire stabilized single-family or small multifamily rental property
- Refinance existing rental property
- Portfolio lending for multiple properties

**Typical Scenarios:**
- Single-family rentals (1-unit)
- Multi-unit rentals (2-4 units, 5-9 units)
- Mixed residential portfolios
- Section 8 / Subsidized housing
- Short-term rentals (Airbnb, VRBO)

**Borrower Profile:**
- Rental property investors
- Portfolio operators
- Income-producing property owners
- No minimum experience required

**Key Characteristics:**
- Long-term permanent financing (30-year terms standard)
- Income-based underwriting (DSCR calculation)
- Fixed-rate or ARM products
- Amortizing or interest-only structures
- Rental income documentation required

---

## 1.3 Loan Product Parameter Comparison

### 1.3.1 Core Product Parameters (Investor-Validated)

| Parameter | Fix & Flip | GUC | Bridge | Bridge Plus | DSCR |
|-----------|-----------|-----|--------|-------------|------|
| **Minimum Loan Amount** | $100,000 | $150,000 | $100,000 | $100,000 | $100,000 |
| **Maximum Loan Amount** | $3,000,000 | $1,500,000* | $3,000,000 | $3,000,000 | $3,000,000 |
| **Loan Term Range** | 12-24 months | 12-24 months | 12-24 months | 25-36 months | 360 months (30 years) |
| **Minimum FICO Score** | 660 | 660 | 660 | 660 | 680 |
| **Minimum Experience** | 1 deal (36mo) | 3 deals (36mo)** | 1 deal (36mo) | 1 deal (36mo) | None required |
| **Primary Structure** | Interest-Only | Interest-Only | Interest-Only | Interest-Only | Amortizing (30yr) or I/O |
| **Rate Type** | Fixed | Fixed | Fixed | Fixed | Fixed 30yr, 5/1 ARM, 7/1 ARM |
| **Maximum LTV** | 85-90% (by class) | 70-75% | 75-82.5% | 72.5-77.5% | 65-80% (by FICO/purpose) |
| **Primary Exit Strategy** | Sale or Refi | Sale or Refi | Refinance or Sale | Refinance to DSCR or Sale | Ongoing rental income |
| **Prepayment Penalty** | Step-down preferred | Step-down preferred | Step-down available | Step-down available | Available on select products |

**Notes:**  
*GUC: Maximum is $1.5M standard; up to $2M on exception basis with strong compensating factors  
**GUC: 3 deals in last 36 months standard; OR 2 deals + Licensed General Contractor license + 2x post-closing liquidity + 720 FICO minimum

### 1.3.2 Eligible Property Types by Product

| Property Type | Fix & Flip | GUC | Bridge | Bridge Plus | DSCR |
|---------------|-----------|-----|--------|-------------|------|
| Single-Family Residence (SFR) | ✓ Primary | ✓ Primary | ✓ Primary | ✓ Primary | ✓ Primary |
| Townhome | ✓ | ✗ | ✓ | ✓ | ✓ |
| Planned Unit Development (PUD) | ✓ | ✗ | ✓ | ✓ | ✓ |
| Condominium (Warrantable) | ✓ | ✗ | Limited | Limited | ✓ |
| Condominium (Non-Warrantable) | Case-by-case | ✗ | Case-by-case | Case-by-case | Limited |
| 2-4 Unit Property | Limited | ✗ | Limited | Limited | ✓ |
| 5-9 Unit Small Multifamily | ✗ | ✗ | ✗ | ✗ | ✓ Enhanced |
| Manufactured/Mobile Home | ✗ | ✗ | ✗ | ✗ | ✗ |
| Agricultural Property | ✗ | ✗ | ✗ | ✗ | ✗ |

### 1.3.3 Eligible Loan Purposes by Product

| Loan Purpose | Fix & Flip | GUC | Bridge | Bridge Plus | DSCR |
|--------------|-----------|-----|--------|-------------|------|
| **Purchase** | ✓ | ✓ | ✓ | ✓ | ✓ |
| **Rate & Term Refinance*** | ✓ | ✗ | ✓ | ✓ | ✓ |
| **Cash-Out Refinance** | Limited (Class A/B) | ✗ | Limited (Class A+/A) | Limited | ✓ |

***Rate & Term Definition**: Net cash back to borrower cannot exceed 2% of loan amount or $2,000 (whichever is less). Amounts exceeding this threshold are classified as Cash-Out Refinance.

---

## 1.4 Product-Specific Underwriting Approaches

### 1.4.1 RTL Products (Fix & Flip, GUC, Bridge, Bridge Plus)

**Underwriting Focus:**
- Borrower experience and track record (critical)
- Property condition and scope of work (for renovation products)
- After-repair value support and market analysis
- Exit strategy feasibility and timeline
- Loan amount based on multiple leverage metrics (As-Is LTV, LTC, LTARV)

**Decision Drivers:**
1. Borrower classification (A+, A, B, C) from credit + experience
2. Property value and renovation economics
3. Market conditions and comparable sales data
4. Exit strategy validation

See Sections 2, 6, and 9 for detailed RTL underwriting methodology.

### 1.4.2 DSCR (Permanent Loan)

**Underwriting Focus:**
- Property's rental income capacity
- Debt service coverage ratio (DSCR) calculation
- Loan amount based on LTV and DSCR constraints (binding constraint determines max loan)
- Rental income documentation and lease review
- Long-term value preservation

**Decision Drivers:**
1. Qualifying rent determination (leased vs unleased, property type)
2. DSCR calculation and comparison to minimums
3. Property LTV constraint
4. Borrower FICO tier for base LTV selection

See Sections 2, 7, and 10 for detailed DSCR underwriting methodology.

---

## 1.5 Excluded Products & Lending Restrictions

### 1.5.1 Not Offered

The following loan products and scenarios are **explicitly not offered**:

- **BRRRR Strategy Loans**: Buy, Renovate, Rent, Refinance, Repeat - not supported as standalone program
- **Owner-Occupied Properties**: All properties must be business purpose investments
- **Commercial Properties**: Office, retail, hospitality (commercial lending is separate program)
- **Agricultural/Farm Properties**: Not eligible
- **Short-Term Rentals (Vacation Rentals)**: Except as documented rental income in DSCR loans
- **Speculative/Vacant Land**: Land must have clear development plan (GUC) or stabilization strategy
- **Undeveloped/Unentitled Land**: GUC requires entitled land

### 1.5.2 Geographic Restrictions

- All properties must be located in the United States (50 states + DC)
- Rural areas limited by property type and DSCR applicability (see Section 5.4.2)
- Properties in designated declining markets subject to enhanced underwriting
- Military housing and base properties: Case-by-case review
- States excluded: North Dakota, South Dakota, Alaska, Hawaii

### 1.5.3 Borrower Restrictions

- No OFAC/Sanctions list matches
- No recent fraud convictions
- Minimum credit score: 660 (RTL), 680 (DSCR)
- No active bankruptcy
- Cannot be debarred from federal programs

See Section 2 for complete borrower eligibility requirements.

---

## 1.6 Key Loan Characteristics Across Products

### 1.6.1 Interest-Only Structure (RTL Products)

**Fix & Flip, GUC, Bridge, and Bridge Plus loans** are typically structured as interest-only during the construction or holding phase:

- Borrower pays interest monthly only
- No principal reduction during I/O period
- Reduces monthly payment burden during active renovation/stabilization
- Standard approach for short-term financing

**Example:**
```
$250,000 loan at 8.5% annual rate, I/O for 12 months:
Monthly I/O Payment = $250,000 × 8.5% / 12 = $1,770.83
(Compare to amortizing: ~$2,429/month on 20-year)
```

### 1.6.2 Fixed Rate vs. ARM (DSCR)

**DSCR products** offer multiple rate structures:

| Rate Type | Structure | Typical Use |
|-----------|-----------|------------|
| **Fixed 30** | Fixed rate for entire 30-year term | Owner-operators wanting payment certainty |
| **5/1 ARM** | Fixed 5 years, then adjusts annually | Shorter hold periods, value-add scenarios |
| **7/1 ARM** | Fixed 7 years, then adjusts annually | Medium-term hold strategies |

**Note:** All RTL products are fixed-rate during the loan term.

### 1.6.3 Prepayment Penalties

**Purpose:** Protect lender yield in lower-rate environment

**Available Structures:**
- 7-year step-down (7% penalty years 1-3, stepping down to 1% in year 7)
- 5-year step-down (5% penalty years 1-2, stepping down to 1% in year 5)
- 3-year step-down (3% penalty declining)
- Interest-rate-dependent penalties

**Flexibility:** Borrowers can often buy down or eliminate penalties for additional basis points in rate.

---

## 1.7 Python Code: Loan Product Definitions & Validation

```python
from enum import Enum
from dataclasses import dataclass
from typing import Optional, List
from decimal import Decimal


class LoanType(Enum):
    """Enumeration of supported loan types."""
    FIX_FLIP = "fix_flip"
    GROUND_UP_CONSTRUCTION = "guc"
    BRIDGE = "bridge"
    BRIDGE_PLUS = "bridge_plus"
    DSCR = "dscr"


class LoanPurpose(Enum):
    """Loan purpose/transaction type."""
    PURCHASE = "purchase"
    RATE_TERM_REFI = "rate_and_term_refinance"
    CASH_OUT_REFI = "cash_out_refinance"


class PropertyType(Enum):
    """Eligible property types."""
    SFR = "single_family"
    TOWNHOME = "townhome"
    PUD = "pud"
    CONDO_WARRANTABLE = "condo_warrantable"
    CONDO_NON_WARRANTABLE = "condo_non_warrantable"
    TWO_FOUR_UNIT = "two_four_unit"
    FIVE_NINE_UNIT = "five_nine_unit"


class RateType(Enum):
    """Rate structure types."""
    FIXED = "fixed"
    FIXED_30 = "fixed_30"
    ARM_5_1 = "arm_5_1"
    ARM_7_1 = "arm_7_1"
    INTEREST_ONLY = "interest_only"


@dataclass
class LoanProductParameters:
    """
    Core parameters for each loan product.
    
    Attributes:
        loan_type: Type of loan (Fix & Flip, GUC, Bridge, Bridge Plus, DSCR)
        min_loan_amount: Minimum loan amount in dollars
        max_loan_amount: Maximum loan amount in dollars
        min_term_months: Minimum loan term in months
        max_term_months: Maximum loan term in months
        min_fico: Minimum required FICO score
        default_rate_type: Standard rate structure
        eligible_purposes: List of eligible loan purposes
        eligible_property_types: List of eligible property types
        requires_experience: Whether borrower must have prior deals
    """
    
    loan_type: LoanType
    min_loan_amount: Decimal
    max_loan_amount: Decimal
    min_term_months: int
    max_term_months: int
    min_fico: int
    default_rate_type: RateType
    eligible_purposes: List[LoanPurpose]
    eligible_property_types: List[PropertyType]
    requires_experience: bool


# Product Definition Database - Investor-Validated
PRODUCT_DEFINITIONS = {
    LoanType.FIX_FLIP: LoanProductParameters(
        loan_type=LoanType.FIX_FLIP,
        min_loan_amount=Decimal("100000"),
        max_loan_amount=Decimal("3000000"),
        min_term_months=12,
        max_term_months=24,
        min_fico=660,
        default_rate_type=RateType.INTEREST_ONLY,
        eligible_purposes=[
            LoanPurpose.PURCHASE,
            LoanPurpose.RATE_TERM_REFI,
            LoanPurpose.CASH_OUT_REFI
        ],
        eligible_property_types=[
            PropertyType.SFR,
            PropertyType.TOWNHOME,
            PropertyType.PUD,
            PropertyType.CONDO_WARRANTABLE,
        ],
        requires_experience=True
    ),
    
    LoanType.GROUND_UP_CONSTRUCTION: LoanProductParameters(
        loan_type=LoanType.GROUND_UP_CONSTRUCTION,
        min_loan_amount=Decimal("150000"),
        max_loan_amount=Decimal("1500000"),
        min_term_months=12,
        max_term_months=24,  # Corrected from 18 to 24
        min_fico=660,
        default_rate_type=RateType.INTEREST_ONLY,
        eligible_purposes=[LoanPurpose.PURCHASE],
        eligible_property_types=[PropertyType.SFR],
        requires_experience=True
    ),
    
    LoanType.BRIDGE: LoanProductParameters(
        loan_type=LoanType.BRIDGE,
        min_loan_amount=Decimal("100000"),
        max_loan_amount=Decimal("3000000"),
        min_term_months=12,
        max_term_months=24,  # Corrected from 36 to 24
        min_fico=660,
        default_rate_type=RateType.INTEREST_ONLY,
        eligible_purposes=[
            LoanPurpose.PURCHASE,
            LoanPurpose.RATE_TERM_REFI,
            LoanPurpose.CASH_OUT_REFI
        ],
        eligible_property_types=[
            PropertyType.SFR,
            PropertyType.TOWNHOME,
            PropertyType.PUD,
            PropertyType.CONDO_WARRANTABLE,
        ],
        requires_experience=True
    ),
    
    LoanType.BRIDGE_PLUS: LoanProductParameters(
        loan_type=LoanType.BRIDGE_PLUS,
        min_loan_amount=Decimal("100000"),
        max_loan_amount=Decimal("3000000"),
        min_term_months=25,
        max_term_months=36,
        min_fico=660,
        default_rate_type=RateType.INTEREST_ONLY,
        eligible_purposes=[
            LoanPurpose.PURCHASE,
            LoanPurpose.RATE_TERM_REFI,
            LoanPurpose.CASH_OUT_REFI
        ],
        eligible_property_types=[
            PropertyType.SFR,
            PropertyType.TOWNHOME,
            PropertyType.PUD,
            PropertyType.CONDO_WARRANTABLE,
        ],
        requires_experience=True
    ),
    
    LoanType.DSCR: LoanProductParameters(
        loan_type=LoanType.DSCR,
        min_loan_amount=Decimal("100000"),
        max_loan_amount=Decimal("3000000"),
        min_term_months=360,  # 30 years permanent
        max_term_months=360,
        min_fico=680,
        default_rate_type=RateType.FIXED_30,
        eligible_purposes=[
            LoanPurpose.PURCHASE,
            LoanPurpose.RATE_TERM_REFI,
            LoanPurpose.CASH_OUT_REFI
        ],
        eligible_property_types=[
            PropertyType.SFR,
            PropertyType.TOWNHOME,
            PropertyType.PUD,
            PropertyType.CONDO_WARRANTABLE,
            PropertyType.TWO_FOUR_UNIT,
            PropertyType.FIVE_NINE_UNIT,
        ],
        requires_experience=False
    ),
}


@dataclass
class LoanValidationResult:
    """Result of loan product validation."""
    is_valid: bool
    errors: List[str]
    warnings: List[str]


class LoanProductValidator:
    """
    Validates loan requests against product parameters and business rules.
    
    This class ensures that loan requests conform to USDV guidelines for
    minimum/maximum amounts, acceptable terms, eligible properties, and
    borrower requirements.
    """
    
    def __init__(self):
        """Initialize validator with product definitions."""
        self.products = PRODUCT_DEFINITIONS
    
    def validate_loan_amount(
        self,
        loan_type: LoanType,
        loan_amount: Decimal
    ) -> tuple[bool, List[str]]:
        """
        Validate loan amount is within product limits.
        
        Args:
            loan_type: Type of loan requested
            loan_amount: Requested loan amount
        
        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []
        params = self.products.get(loan_type)
        
        if not params:
            errors.append(f"Unknown loan type: {loan_type}")
            return False, errors
        
        if loan_amount < params.min_loan_amount:
            errors.append(
                f"Loan amount ${loan_amount:,.0f} is below minimum "
                f"${params.min_loan_amount:,.0f} for {loan_type.value}"
            )
        
        if loan_amount > params.max_loan_amount:
            errors.append(
                f"Loan amount ${loan_amount:,.0f} exceeds maximum "
                f"${params.max_loan_amount:,.0f} for {loan_type.value}"
            )
        
        return len(errors) == 0, errors
    
    def validate_loan_term(
        self,
        loan_type: LoanType,
        term_months: int
    ) -> tuple[bool, List[str]]:
        """
        Validate loan term is within product limits.
        
        Args:
            loan_type: Type of loan requested
            term_months: Requested term in months
        
        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []
        params = self.products.get(loan_type)
        
        if not params:
            errors.append(f"Unknown loan type: {loan_type}")
            return False, errors
        
        if term_months < params.min_term_months:
            errors.append(
                f"Term {term_months} months is below minimum "
                f"{params.min_term_months} for {loan_type.value}"
            )
        
        if term_months > params.max_term_months:
            errors.append(
                f"Term {term_months} months exceeds maximum "
                f"{params.max_term_months} for {loan_type.value}"
            )
        
        return len(errors) == 0, errors
    
    def validate_fico(
        self,
        loan_type: LoanType,
        fico_score: int
    ) -> tuple[bool, List[str]]:
        """
        Validate borrower FICO meets minimum requirement.
        
        Args:
            loan_type: Type of loan requested
            fico_score: Borrower FICO score
        
        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []
        params = self.products.get(loan_type)
        
        if not params:
            errors.append(f"Unknown loan type: {loan_type}")
            return False, errors
        
        if fico_score < params.min_fico:
            errors.append(
                f"FICO {fico_score} is below minimum {params.min_fico} "
                f"for {loan_type.value}"
            )
        
        return len(errors) == 0, errors
    
    def validate_property_type(
        self,
        loan_type: LoanType,
        property_type: PropertyType
    ) -> tuple[bool, List[str]]:
        """
        Validate property type is eligible for loan product.
        
        Args:
            loan_type: Type of loan requested
            property_type: Property type being financed
        
        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []
        params = self.products.get(loan_type)
        
        if not params:
            errors.append(f"Unknown loan type: {loan_type}")
            return False, errors
        
        if property_type not in params.eligible_property_types:
            eligible_types = ", ".join(
                [pt.value for pt in params.eligible_property_types]
            )
            errors.append(
                f"Property type {property_type.value} is not eligible for "
                f"{loan_type.value}. Eligible types: {eligible_types}"
            )
        
        return len(errors) == 0, errors
    
    def validate_loan_purpose(
        self,
        loan_type: LoanType,
        loan_purpose: LoanPurpose
    ) -> tuple[bool, List[str]]:
        """
        Validate loan purpose is eligible for loan product.
        
        Args:
            loan_type: Type of loan requested
            loan_purpose: Purpose of the loan (purchase, refi, etc.)
        
        Returns:
            Tuple of (is_valid, error_messages)
        """
        errors = []
        params = self.products.get(loan_type)
        
        if not params:
            errors.append(f"Unknown loan type: {loan_type}")
            return False, errors
        
        if loan_purpose not in params.eligible_purposes:
            eligible_purposes = ", ".join(
                [lp.value for lp in params.eligible_purposes]
            )
            errors.append(
                f"Loan purpose {loan_purpose.value} is not eligible for "
                f"{loan_type.value}. Eligible purposes: {eligible_purposes}"
            )
        
        return len(errors) == 0, errors
    
    def validate_complete_loan_request(
        self,
        loan_type: LoanType,
        loan_amount: Decimal,
        term_months: int,
        fico_score: int,
        property_type: PropertyType,
        loan_purpose: LoanPurpose,
        borrower_experience: int = 0
    ) -> LoanValidationResult:
        """
        Validate complete loan request against all product requirements.
        
        Args:
            loan_type: Type of loan requested
            loan_amount: Requested loan amount in dollars
            term_months: Requested term in months
            fico_score: Borrower FICO score
            property_type: Property type being financed
            loan_purpose: Loan purpose (purchase, refi, etc.)
            borrower_experience: Number of completed deals (optional)
        
        Returns:
            LoanValidationResult with validation status and messages
        """
        all_errors = []
        all_warnings = []
        
        # Validate each component
        is_amount_valid, amount_errors = self.validate_loan_amount(
            loan_type, loan_amount
        )
        all_errors.extend(amount_errors)
        
        is_term_valid, term_errors = self.validate_loan_term(
            loan_type, term_months
        )
        all_errors.extend(term_errors)
        
        is_fico_valid, fico_errors = self.validate_fico(
            loan_type, fico_score
        )
        all_errors.extend(fico_errors)
        
        is_property_valid, property_errors = self.validate_property_type(
            loan_type, property_type
        )
        all_errors.extend(property_errors)
        
        is_purpose_valid, purpose_errors = self.validate_loan_purpose(
            loan_type, loan_purpose
        )
        all_errors.extend(purpose_errors)
        
        # Check experience requirement if applicable
        params = self.products.get(loan_type)
        if params and params.requires_experience and borrower_experience == 0:
            all_warnings.append(
                f"{loan_type.value} typically requires prior real estate "
                f"investment experience. This borrower has no documented deals."
            )
        
        is_valid = len(all_errors) == 0
        
        return LoanValidationResult(
            is_valid=is_valid,
            errors=all_errors,
            warnings=all_warnings
        )
    
    def get_product_summary(
        self, loan_type: LoanType
    ) -> Optional[LoanProductParameters]:
        """
        Retrieve product parameter summary.
        
        Args:
            loan_type: Type of loan to retrieve parameters for
        
        Returns:
            LoanProductParameters or None if loan type not found
        """
        return self.products.get(loan_type)


# Example Usage
if __name__ == "__main__":
    validator = LoanProductValidator()
    
    # Example 1: Valid Fix & Flip Request
    result1 = validator.validate_complete_loan_request(
        loan_type=LoanType.FIX_FLIP,
        loan_amount=Decimal("250000"),
        term_months=18,
        fico_score=720,
        property_type=PropertyType.SFR,
        loan_purpose=LoanPurpose.PURCHASE,
        borrower_experience=3
    )
    
    print("Fix & Flip Validation:", result1.is_valid)
    if result1.errors:
        print("Errors:", result1.errors)
    if result1.warnings:
        print("Warnings:", result1.warnings)
    
    # Example 2: Invalid DSCR Request (FICO too low)
    result2 = validator.validate_complete_loan_request(
        loan_type=LoanType.DSCR,
        loan_amount=Decimal("400000"),
        term_months=360,
        fico_score=670,  # Below minimum of 680
        property_type=PropertyType.SFR,
        loan_purpose=LoanPurpose.PURCHASE
    )
    
    print("\nDSCR Validation:", result2.is_valid)
    if result2.errors:
        print("Errors:", result2.errors)
    
    # Example 3: Valid GUC with corrected parameters
    result3 = validator.validate_complete_loan_request(
        loan_type=LoanType.GROUND_UP_CONSTRUCTION,
        loan_amount=Decimal("1200000"),
        term_months=20,
        fico_score=700,
        property_type=PropertyType.SFR,
        loan_purpose=LoanPurpose.PURCHASE,
        borrower_experience=3
    )
    
    print("\nGUC Validation (corrected):", result3.is_valid)
    if result3.errors:
        print("Errors:", result3.errors)
    
    # Example 4: Valid Bridge Plus Request
    result4 = validator.validate_complete_loan_request(
        loan_type=LoanType.BRIDGE_PLUS,
        loan_amount=Decimal("500000"),
        term_months=30,
        fico_score=700,
        property_type=PropertyType.SFR,
        loan_purpose=LoanPurpose.PURCHASE,
        borrower_experience=2
    )
    
    print("\nBridge Plus Validation:", result4.is_valid)
    if result4.errors:
        print("Errors:", result4.errors)
```

---

*End of Section 1*
