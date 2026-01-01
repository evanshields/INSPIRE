---
section: 5
title: Property Eligibility Standards
version: 1.1
last_updated: 2025-12-30
model_used: haiku
guideline_sources:
  - Archwest RTL Guidelines v6.0
  - Eastview RTL Guidelines v4.1
  - Eastview DSCR Guidelines v7.2
  - EV GUC Guidelines v1.0
changelog:
  - 2025-12-30: Updated minimum SFR/Townhome square footage from 700 to 600 per EastView guidelines
  - 2025-12-30: Updated with investor-validated criteria; corrected non-warrantable condo eligibility by product; clarified acreage and rural property definitions; updated Python code
  - 2025-12-30: Initial creation
---

# Section 5: Property Eligibility Standards

## 5.1 Overview

Property eligibility is a foundational underwriting decision that determines whether a property can be financed under USDV guidelines. Ineligible properties result in automatic loan decline. This section defines property type eligibility, geographic restrictions, condition standards, and size/value requirements across all loan products.

**INSPIRE Integration Points:**
- Phase 1-2: Property pre-qualification during application intake
- Phase 7: Property eligibility validation during AI analysis

---

## 5.2 Eligible Property Types

### 5.2.1 Primary Eligible Property Types

These property types are eligible across **all loan products** (with noted product-specific limitations):

#### Single-Family Residence (SFR)

**Definition:**
A residential structure designed for occupancy by a single household with separate entrance, kitchen, and bathroom.

**Eligibility Criteria:**
- ✓ Detached single-family home
- ✓ Minimum **600 square feet** (Gross Living Area)
- ✓ Standard foundation (concrete, pier & beam, slab)
- ✓ All loan products eligible (FF, GUC, Bridge, Bridge Plus, DSCR)

**Financing Available:**
- RTL: Full leverage range (see Section 9)
- DSCR: Full leverage range (see Section 10)
- No special SFR restrictions across products

#### Townhome

**Definition:**
An attached residential structure with individual unit ownership, separate entrance, kitchen, bathroom, and typically shared walls (but not common ownership of land or building).

**Eligibility Criteria:**
- ✓ Individual unit ownership (not condominium)
- ✓ Minimum **600 square feet** per unit (Gross Living Area)
- ✓ Direct land ownership (not ground lease)
- ✓ Primary eligible for Fix & Flip, Bridge, Bridge Plus, DSCR
- ✗ NOT eligible for GUC (typically cannot be newly constructed as townhome in GUC structure)

**Key Distinction from Condos:**
- Townhomes have individual ownership of land
- Condominiums have shared ownership of common areas
- Townhomes are generally preferred over condos (lower risk)

#### Planned Unit Development (PUD)

**Definition:**
A residential development where individual unit owners hold title to their unit and land, with ownership of common areas (roads, amenities, green space) held collectively.

**Eligibility Criteria:**
- ✓ Individual unit ownership documented
- ✓ Ownership certificate for unit and proportionate share of common areas
- ✓ HOA governance with documented reserves
- ✓ Primary eligible for all products (Fix & Flip, GUC, Bridge, Bridge Plus, DSCR)

**HOA Review:**
- Standard HOA document review required (CC&Rs, budget, litigation)
- Warrantable PUD status preferred but not required
- Non-warrantable PUDs may be allowed with case-by-case review

---

### 5.2.2 Conditionally Eligible Property Types

These property types are eligible but require additional scrutiny and may have product-specific restrictions:

#### Condominium (Warrantable)

**Definition:**
A condominium project that meets warrantability standards per Fannie Mae guidelines or investor-specific criteria.

**Warrantability Criteria (Fannie Mae Standard):**
- ✓ Project completed and stabilized
- ✓ Developer has conveyed control to owners (homeowners association)
- ✓ Single entity does not own >10% of units
- ✓ Commercial space <25% of building square footage
- ✓ No more than 15% of units delinquent on HOA fees
- ✓ No pending litigation involving HOA
- ✓ HOA permits rentals (no restrictive lease limitations)

**Eligibility by Product:**
- ✓ Fix & Flip, Bridge, Bridge Plus: Fully eligible
- ✓ DSCR: Fully eligible
- ✗ GUC: NOT eligible (cannot be newly constructed as condo)

**HOA Review Required:**
- CC&Rs, bylaws, and meeting minutes (last 2 years)
- Current budget and financial statements
- Master insurance policy and coverage details
- Reserve study (if available)
- Litigation search

#### Condominium (Non-Warrantable)

**Definition:**
A condominium project that does NOT meet warrantability standards (typically due to project status, ownership concentration, rental restrictions, or HOA issues).

**Non-Warrantability Triggers:**
- ✗ Project not yet completed
- ✗ Developer still controls HOA
- ✗ Single entity owns >10% of units
- ✗ HOA restricts short-term rentals
- ✗ >50% of units are rental-occupied
- ✗ Pending HOA litigation
- ✗ Commercial space >25% of building
- ✗ >15% of units in arrears on HOA dues

**Eligibility by Product:**
- **RTL (Fix & Flip, Bridge, Bridge Plus)**: **Conditional** - Case-by-case review; requires strong compensating factors and documented approval
- **DSCR**: **Eligible with -10% LTV reduction** - Non-warrantable status accepted but with leverage reduction

**Case-by-Case Factors (RTL Only):**
- HOA reserve funding trajectory improving
- Litigation status and resolution timeline
- Ownership concentration declining
- Rental restrictions policy likelihood

#### 2-4 Unit Property

**Definition:**
Residential property containing 2, 3, or 4 dwelling units in one structure or complex.

**Eligibility by Product:**
- ✓ Fix & Flip: Limited (case-by-case); requires strong exit strategy
- ✓ GUC: Limited (must meet builder requirements; minimum experience)
- ✓ Bridge: Limited (requires income documentation or clear stabilization path)
- ✓ Bridge Plus: Limited (requires rental income documentation and DSCR qualification)
- ✓ DSCR: Fully eligible with income analysis

**Minimum Unit Square Footage:**
- ✓ Minimum **500 square feet per unit** (Gross Living Area)
- Each unit must be self-contained (separate entrance, kitchen, bathroom)

**Key Considerations:**
- Income analysis required if rental-based
- Investor experience with multifamily strongly preferred
- HOA requirements (if applicable) same as single-family condos

#### 5-9 Unit Small Multifamily

**Definition:**
Residential property with 5 to 9 dwelling units (within USDV definition of "small multifamily").

**Eligibility by Product:**
- ✗ Fix & Flip: NOT eligible (exceeds single/dual focus)
- ✗ GUC: NOT eligible (exceeds USDV scope)
- ✗ Bridge: NOT eligible
- ✗ Bridge Plus: NOT eligible
- ✓ DSCR: **Fully eligible** with enhanced underwriting

**DSCR-Specific Requirements for 5-9 Unit:**
- Full NCF (Net Cash Flow) DSCR analysis required
- Detailed operating expense analysis required
- Minimum 1.20x DSCR for borrowers with FICO <720
- Minimum 1.20x DSCR for 5-9 units (per ArchWest DSCR)
- Minimum **500 square feet per unit**
- Enhanced appraisal (commercial-grade narrative appraisal)
- Property management documentation required

**Market Restrictions:**
- Subject to same geographic restrictions as other properties
- Market decline/ZHVI factors apply same as SFR

---

### 5.2.3 Property Type Eligibility Matrix (By Product)

| Property Type | Fix & Flip | GUC | Bridge | Bridge Plus | DSCR |
|---------------|-----------|-----|--------|-------------|------|
| **SFR** | ✓ Primary | ✓ Primary | ✓ Primary | ✓ Primary | ✓ Primary |
| **Townhome** | ✓ | ✗ | ✓ | ✓ | ✓ |
| **PUD** | ✓ | Limited* | ✓ | ✓ | ✓ |
| **Condo (Warrantable)** | ✓ | ✗ | ✓ | ✓ | ✓ |
| **Condo (Non-Warrantable)** | Case-by-case | ✗ | Case-by-case | Case-by-case | -10% LTV |
| **2-4 Unit** | Limited | Limited* | Limited | Limited | ✓ |
| **5-9 Unit** | ✗ | ✗ | ✗ | ✗ | ✓ Enhanced |
| **Manufactured/Mobile** | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Commercial** | ✗ | ✗ | ✗ | ✗ | ✗ |

*PUD and 2-4 Unit for GUC require strong compensating factors and documentation

---

### 5.2.4 Universally Ineligible Property Types

The following property types are **explicitly NOT eligible** for any USDV loan product:

- **Manufactured/Mobile Homes**: Non-standard foundation; depreciation risk; title/registration issues
- **Modular Homes (Temporary Foundation)**: Must be permanently affixed to qualify; temporary foundation ineligible
- **Mixed-Use Properties**: Residential + commercial (e.g., apt building with retail storefront)
- **Commercial Properties**: Office, retail, hotel, industrial properties
- **Agricultural/Farm Properties**: Properties with active agricultural use or agricultural zoning
- **Houseboats**: Non-real property collateral
- **Co-Operatives**: Complex ownership structure; non-standard title
- **Condotels**: Hotel-operated condominium units (commercial use)
- **Properties >10 Acres**: Exceed residential investment property scope
- **Properties with Environmental Hazards**: Lava zones (Hawaii), underground oil tanks, contaminated sites
- **Rent-Controlled Properties**: Subject to government regulation; impacts exit/refinance
- **Daily Tenancy Properties**: Hotels, boarding houses, dormitories
- **Single-Room-Occupancy (SRO)**: Rented by room/bed (not full-unit)
- **Student Housing (by-the-bed)**: Rented by room to students
- **Undeveloped Land**: Except GUC projects with clear development plan
- **Unreinforced Brick Buildings**: Structural integrity concerns

---

## 5.3 Geographic Eligibility

### 5.3.1 Eligible States List

USDV Capital lends in all U.S. states except those explicitly listed as ineligible.

**Ineligible States:**
- ✗ North Dakota (ND)
- ✗ South Dakota (SD)
- ✗ Alaska (AK)
- ✗ Hawaii (HI)

**Note**: All other 46 states + Washington D.C. are eligible for lending (subject to property-level restrictions detailed below).

### 5.3.2 Rural Property Restrictions

**Definition:**
Properties in designated rural areas are ineligible due to limited liquidity and market volatility.

**Primary Determination Method:**
- Use **CFPB Rural and Underserved Designation website** as primary source
- Property must NOT be designated as "rural" by CFPB to be eligible
- Property appraisal designation of "rural" is secondary confirmation

**Exception - Urban Commute Clause:**
- A property may be approved despite CFPB "rural" designation IF:
  - Property is within 50-minute commute to secondary market with minimum **250,000 MSA population**
  - Must be documented with maps/commute time verification
  - Requires SVP of Credit approval as exception
  - Used for borderline/fringe rural areas

**Impact on Underwriting:**
- Rural properties fail property eligibility checklist automatically
- Exception requires documented rationale and approval trail
- When approved, may trigger additional margin/pricing adjustments

### 5.3.3 Declining Market Considerations

**Definition:**
Markets with negative Home Price Appreciation (HPA) and/or inflated valuation multiples relative to historical norms.

**Market Metrics Used:**
- **Home Price Appreciation (HPA)**: Year-over-year % change in median home values (ZIP code level)
- **ZHVI Multiplier**: Zillow Home Value Index compared to historical range

**Data Source:**
- **Primary**: Zillow ZHVI data at ZIP code level (most granular, most current)
- **Secondary**: Case-Shiller index or similar at county/MSA level if Zillow data unavailable
- **Measurement Period**: Last 12 months typically; longer periods for trend confirmation

**Leverage Reduction Triggers:**
- **HPA between 0% and -10% decline**: -5% LTV reduction
- **HPA greater than -10% decline**: -10% LTV reduction
- **ZHVI Multiplier 200-300% of historical norm**: -5% LTV reduction
- **ZHVI Multiplier >300% of historical norm**: -10% LTV reduction

**Appraisal Requirements:**
- Declining market designation typically noted in appraisal
- Enhanced comparable sales analysis required
- Market analysis section of appraisal critical

---

## 5.4 Property Condition Standards

### 5.4.1 Condition Rating System (C1-C6)

USDV uses the **Uniform Appraisal Dataset (UAD) Condition Rating System** established by Fannie Mae. This is industry standard and used by all major lenders.

| Rating | Description | RTL Eligible | DSCR Eligible | Notes |
|--------|-------------|:------------:|:-------------:|-------|
| **C1** | New construction, never occupied | ✓ | ✓ | Perfect/like-new condition |
| **C2** | Recently renovated, like-new condition | ✓ | ✓ | Recently completed cosmetic/mechanical updates |
| **C3** | Well-maintained, minimal deferred maintenance | ✓ | ✓ | Standard acceptable condition |
| **C4** | Adequately maintained, minor deferred maintenance, fully functional | ✓ | ✓ | Some age/wear but functional systems |
| **C5** | Poorly maintained, significant deferred maintenance, requires repairs | **Conditional*** | ✗ | RTL only; rehab-focused; DSCR not permitted |
| **C6** | Substantial renovation needed, uninhabitable, structural issues | ✗ | ✗ | Ineligible for all products |

***C5 RTL Eligibility**: Permitted only if:
- Detailed rehabilitation budget provided
- Budget addresses all deferred maintenance items
- Post-rehab condition projected to reach minimum C3
- Strong exit strategy documented

### 5.4.2 Minimum Habitability Standards (All Products)

All properties must meet minimum habitability standards at loan closing (or post-rehabilitation for RTL):

**Structural Integrity:**
- Sound foundation (no active settling, subsidence, or structural movement)
- Roof in reasonable condition (not actively leaking)
- Walls and framing structurally sound
- No condemned or unsafe structures

**Mechanical Systems:**
- Functional plumbing (hot/cold water, working drains, functional toilets/sinks)
- Operational electrical system (safe panel, adequate capacity, no exposed hazards)
- Heating system functional (or climate-appropriate alternative)
- No hazardous materials or code violations noted

**Safety Requirements:**
- Accessible public street access (not private road or limited access)
- Safe egress/exit paths
- No significant hazards noted in appraisal

**Appraisal Notation:**
- C5 appraisals require specific notation of repair items and estimated costs
- C4 appraisals note any deferred maintenance items for lender awareness
- C3 and better appraisals confirm fully market-ready condition

---

## 5.5 Size & Value Requirements

### 5.5.1 Minimum Square Footage by Property Type

| Property Type | Minimum GLA | Notes |
|---------------|-------------|-------|
| **SFR** | 600 sq ft | Gross Living Area; standard residential |
| **Townhome** | 600 sq ft | Per unit; minimum 600 per dwelling |
| **Condo** | 500 sq ft | Per unit; typically smaller than SFR/townhome |
| **2-4 Unit** | 500 sq ft | Per unit minimum; average can be lower |
| **5-9 Unit** | 500 sq ft | Per unit minimum; commercial appraisal standards |

**Definition - Gross Living Area (GLA):**
- Space enclosed and climate-controlled
- Includes bedrooms, kitchens, baths, living areas, hallways
- Excludes unfinished basements, garages, carports, decks, patios

**Enforcement:**
- Appraisal must document GLA by unit/structure
- Properties below minimums are ineligible
- Measurement disputes resolved by MAT (appraisal review/recert)

### 5.5.2 Maximum Loan Amount

The maximum loan amount for any single property is **$3,000,000**, regardless of property type, market, or loan product.

**Application:**
- Applies to initial funding plus any rehab holdbacks (total loan amount)
- Loans in excess of $3M require exception approval from investor
- GUC has lower max of $1.5M (standard); $2M (exception)

**Cross-Collateralization:**
- Portfolio loans (multiple properties) may aggregate, but individual property limit still applies
- Cross-collateralization allowed within USDV guidelines for RTL
- Each property individually appraised and valued

### 5.5.3 Acreage Limitations

**Standard Guideline:**
- Properties with **less than 5 acres** of land are standard
- Properties with **5 acres or more** are conditional/exception-based
- Properties with **10+ acres** are **ineligible**

**Exception Process (5-9.99 Acres):**
- Case-by-case review required
- Land value must be reasonable relative to improved value
- Excess land must not be intended for agricultural use
- Exception approval from underwriting manager minimum
- Larger land holdings (7-10 acres) require senior underwriter + investor consultation

**Acreage Exclusions:**
- Vacant or undeveloped acres trigger higher leverage reductions
- Excess land beyond primary residence footprint impacts appraisal methodology
- Development potential must be clearly addressed

**Special Cases:**
- **GUC Projects**: Entitled land acceptable even if larger acreage (provided proper zoning/entitlements)
- **Residential Compounds**: Multi-unit development on same parcel may be allowed if properly zoned
- **Rural Properties**: Acreage limitations compound with rural property ineligibility

---

## 5.6 Condominium Requirements (Enhanced)

### 5.6.1 Warrantable vs. Non-Warrantable Assessment

**Warrantability Determination:**
Using Fannie Mae Form 1076 (Condominium Questionnaire) and supporting documents, assess:

1. **Project Status**: Is project completed and stabilized?
2. **Developer Control**: Has developer conveyed control to owners?
3. **Owner Concentration**: Does single entity own >10% of units?
4. **Commercial Restrictions**: Is commercial space <25% of building?
5. **HOA Delinquency**: Are <15% of units delinquent on HOA fees?
6. **Litigation**: Is there pending HOA litigation?
7. **Rental Restrictions**: Does HOA permit rentals?

**Warrantable = YES to all 7 criteria**  
**Non-Warrantable = NO to any 1 or more criteria**

### 5.6.2 HOA Document Review (Required for All Condos)

**Mandatory Documents:**
- **CC&Rs (Covenants, Conditions & Restrictions)**: Master deed controlling development
- **Bylaws**: HOA governance and operational rules
- **Current Budget**: Annual operating budget with line-item detail
- **Financial Statements**: Balance sheet and income statement (last 2 years)
- **Master Insurance Policy**: Proof of hazard, liability, and flood (if applicable) coverage
- **Reserve Study**: Professional assessment of reserve funding (if available; many projects have)
- **HOA Minutes**: Last 2-3 years of meeting minutes (showing litigation, special assessments)
- **Management Contract**: Current HOA management company/agreement

**Key Review Points:**
- Reserve funding level: Ideally 25%+ of annual budget (USDV flexible standard)
- Special assessments: Any pending or recent special assessments to owners
- Litigation: Active HOA disputes or litigation that could impact value
- Rental restrictions: Any prohibition on rental use (critical for DSCR properties)
- Delinquency rates: Percentage of units with unpaid HOA dues (>15% = non-warrantable)

### 5.6.3 Project Approval Process (Non-Warrantable Condos - RTL Only)

**Step 1: Initial Screening**
- Identify non-warrantable status from questionnaire
- Document reason(s) for non-warrantable designation
- Assess severity (minor vs. major issue)

**Step 2: Compensating Factors**
Identify and document compensating factors such as:
- HOA litigation in final resolution stage
- Reserve funding plan improving over next 12-24 months
- Single owner concentration declining (e.g., developer selling down)
- Strong local market fundamentals supporting value/exit
- Borrower's strong credit/experience/liquidity

**Step 3: Approval Authority**
- **Minor non-warrantable issues**: Senior Underwriter approval
- **Major non-warrantable issues**: Underwriting Manager approval
- **Multiple major issues or weak compensating factors**: Escalate to investor for approval

---

## 5.7 Property Valuation & Appraisal Standards

### 5.7.1 Appraisal Requirements by Loan Amount

| Loan Amount | Appraisal Type | Frequency | Notes |
|-------------|----------------|-----------|-------|
| <$750,000 | Hybrid or Full Interior | No recertification needed | Interior inspection + desktop analysis acceptable |
| $750,000-$1.5M | Full Interior Appraisal | Recertification if >120 days | Licensed/certified appraiser required |
| >$1.5M | Full Interior Appraisal | Recertification if >120 days | May require two appraisals for >$2M |

**Appraisal Age:**
- Appraisal must be dated no more than **120 days prior** to loan note date
- If older than 120 days: Recertification of value by same appraiser OR new appraisal required
- Recertification must confirm values within acceptable variance

### 5.7.2 ARV (After-Repair Value) Appraisals for RTL

**Required for Fix & Flip and GUC:**
- Appraisal must provide both **As-Is Value** and **After-Repair Value (ARV)**
- ARV assumes completion of all planned renovations
- ARV assumes property in C3 minimum condition post-rehab
- ARV cap: Typically not to exceed 110-115% of historical home values in area

**ARV Validation:**
- Must be supported by comparable sales of similar properties in area
- Recent sales (within 6 months) of similar properties post-renovation
- Appraisal must address market conditions and demand for finished product
- Conservative estimate preferred over optimistic projections

---

## 5.8 Python Implementation: Property Eligibility Checker

```python
from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Tuple
from decimal import Decimal


class LoanType(Enum):
    """Loan product types."""
    FIX_FLIP = "fix_flip"
    GROUND_UP_CONSTRUCTION = "guc"
    BRIDGE = "bridge"
    BRIDGE_PLUS = "bridge_plus"
    DSCR = "dscr"


class PropertyType(Enum):
    """Eligible property types."""
    SFR = "sfr"
    TOWNHOME = "townhome"
    PUD = "pud"
    CONDO_WARRANTABLE = "condo_warrantable"
    CONDO_NON_WARRANTABLE = "condo_non_warrantable"
    TWO_TO_FOUR_UNIT = "two_to_four_unit"
    FIVE_TO_NINE_UNIT = "five_to_nine_unit"
    MANUFACTURED = "manufactured_home"


class ConditionRating(Enum):
    """UAD Condition Ratings per Fannie Mae."""
    C1 = "c1_new_construction"
    C2 = "c2_recently_renovated"
    C3 = "c3_well_maintained"
    C4 = "c4_adequately_maintained"
    C5 = "c5_poorly_maintained"
    C6 = "c6_substantial_renovation_needed"


@dataclass
class Property:
    """Represents a property for eligibility assessment."""
    property_type: PropertyType
    state: str  # Two-letter abbreviation (e.g., 'TX', 'CA')
    is_rural: bool  # From CFPB Rural Designation
    condition_rating: ConditionRating
    square_footage: int  # Gross Living Area
    units: int = 1
    acreage: float = 0.0
    is_warrantable_condo: Optional[bool] = None
    has_hoa_rental_restrictions: bool = False
    is_in_declining_market: bool = False
    hpa_percentage: Optional[float] = None  # Year-over-year HPA %
    zhvi_multiplier: Optional[float] = None  # ZHVI multiplier relative to historical
    loan_amount: Decimal = Decimal("0")


@dataclass
class PropertyEligibilityResult:
    """Result of property eligibility assessment."""
    is_eligible: bool
    issues: List[str]  # Fatal eligibility issues
    warnings: List[str]  # Warnings/exceptions
    ltv_impact: float = 0.0  # Cumulative LTV reduction (e.g., -0.10 = -10%)


class PropertyEligibilityChecker:
    """
    Validates property eligibility against USDV guidelines.
    Assesses property type, location, condition, size, and market factors.
    """
    
    # Eligible property types by loan product
    ELIGIBLE_TYPES_BY_PRODUCT = {
        LoanType.FIX_FLIP: [
            PropertyType.SFR, PropertyType.TOWNHOME, PropertyType.PUD,
            PropertyType.CONDO_WARRANTABLE, PropertyType.CONDO_NON_WARRANTABLE,
            PropertyType.TWO_TO_FOUR_UNIT,
        ],
        LoanType.GROUND_UP_CONSTRUCTION: [
            PropertyType.SFR, PropertyType.TOWNHOME, PropertyType.PUD,
            PropertyType.TWO_TO_FOUR_UNIT,  # Limited
        ],
        LoanType.BRIDGE: [
            PropertyType.SFR, PropertyType.TOWNHOME, PropertyType.PUD,
            PropertyType.CONDO_WARRANTABLE, PropertyType.CONDO_NON_WARRANTABLE,
            PropertyType.TWO_TO_FOUR_UNIT,
        ],
        LoanType.BRIDGE_PLUS: [
            PropertyType.SFR, PropertyType.TOWNHOME, PropertyType.PUD,
            PropertyType.CONDO_WARRANTABLE, PropertyType.CONDO_NON_WARRANTABLE,
            PropertyType.TWO_TO_FOUR_UNIT,
        ],
        LoanType.DSCR: [
            PropertyType.SFR, PropertyType.TOWNHOME, PropertyType.PUD,
            PropertyType.CONDO_WARRANTABLE, PropertyType.CONDO_NON_WARRANTABLE,
            PropertyType.TWO_TO_FOUR_UNIT, PropertyType.FIVE_TO_NINE_UNIT,
        ],
    }
    
    # Universally ineligible types
    INELIGIBLE_TYPES = [
        PropertyType.MANUFACTURED,
    ]
    
    # Minimum square footage requirements (EastView standard)
    MIN_SQ_FT = {
        PropertyType.SFR: 600,
        PropertyType.TOWNHOME: 600,
        PropertyType.PUD: 600,
        PropertyType.CONDO_WARRANTABLE: 500,
        PropertyType.CONDO_NON_WARRANTABLE: 500,
        PropertyType.TWO_TO_FOUR_UNIT: 500,
        PropertyType.FIVE_TO_NINE_UNIT: 500,
    }
    
    # Ineligible states
    INELIGIBLE_STATES = ["ND", "SD", "AK", "HI"]
    
    # Leverage/size limits
    MAX_LOAN_AMOUNT = Decimal("3000000")
    MAX_ACREAGE = 5.0
    MAX_ACREAGE_HARD_LIMIT = 10.0
    
    def validate_property_type(
        self,
        property_type: PropertyType,
        loan_type: LoanType
    ) -> Tuple[bool, List[str]]:
        """Validate property type is eligible for loan product."""
        errors = []
        
        if property_type in self.INELIGIBLE_TYPES:
            errors.append(
                f"Property type '{property_type.value}' is universally ineligible."
            )
            return False, errors
        
        eligible_types = self.ELIGIBLE_TYPES_BY_PRODUCT.get(loan_type, [])
        if property_type not in eligible_types:
            errors.append(
                f"Property type '{property_type.value}' is not eligible for "
                f"{loan_type.value} loans."
            )
            return False, errors
        
        return True, errors
    
    def validate_location(
        self,
        state: str,
        is_rural: bool
    ) -> Tuple[bool, List[str], float]:
        """
        Validate geographic eligibility.
        
        Returns:
            Tuple of (is_eligible, errors, ltv_impact)
        """
        errors = []
        ltv_impact = 0.0
        
        if state.upper() not in self.INELIGIBLE_STATES:
            pass  # Valid state
        else:
            errors.append(f"Properties in {state} are not eligible.")
        
        if is_rural:
            errors.append("Rural properties are not eligible.")
        
        return len(errors) == 0, errors, ltv_impact
    
    def validate_condition(
        self,
        condition: ConditionRating,
        loan_type: LoanType
    ) -> Tuple[bool, List[str]]:
        """Validate property condition rating."""
        errors = []
        
        if condition == ConditionRating.C6:
            errors.append(
                f"Property condition C6 (Substantial Renovation) is not eligible."
            )
            return False, errors
        
        if loan_type == LoanType.DSCR:
            if condition in [ConditionRating.C5, ConditionRating.C6]:
                errors.append(
                    f"DSCR Permanent requires C1-C4 condition. "
                    f"Current: {condition.value}"
                )
                return False, errors
        
        elif loan_type in [LoanType.FIX_FLIP, LoanType.GUC, LoanType.BRIDGE, LoanType.BRIDGE_PLUS]:
            if condition == ConditionRating.C5:
                # Conditional - OK but needs documentation
                pass
        
        return True, errors
    
    def validate_size_and_value(
        self,
        property_type: PropertyType,
        square_footage: int,
        units: int,
        acreage: float,
        loan_amount: Decimal
    ) -> Tuple[bool, List[str], float]:
        """
        Validate property size and loan amount.
        
        Returns:
            Tuple of (is_eligible, errors, ltv_impact)
        """
        errors = []
        ltv_impact = 0.0
        
        # Square footage check
        min_sf = self.MIN_SQ_FT.get(property_type)
        if min_sf:
            if property_type in [PropertyType.SFR, PropertyType.TOWNHOME, PropertyType.PUD]:
                if square_footage < min_sf:
                    errors.append(
                        f"Property {square_footage} sq ft is below minimum "
                        f"{min_sf} sq ft for {property_type.value}."
                    )
            else:  # Multi-unit: check per-unit
                avg_sf = square_footage / units
                if avg_sf < min_sf:
                    errors.append(
                        f"Average unit size {avg_sf:.0f} sq ft is below minimum "
                        f"{min_sf} sq ft per unit."
                    )
        
        # Acreage check
        if acreage >= self.MAX_ACREAGE_HARD_LIMIT:
            errors.append(
                f"Property acreage {acreage} exceeds maximum {self.MAX_ACREAGE_HARD_LIMIT} acres."
            )
        elif acreage >= self.MAX_ACREAGE:
            # Conditional - needs exception
            ltv_impact -= 0.05  # Example reduction for borderline acreage
        
        # Loan amount check
        if loan_amount > self.MAX_LOAN_AMOUNT:
            errors.append(
                f"Loan amount ${loan_amount:,.0f} exceeds maximum ${self.MAX_LOAN_AMOUNT:,.0f}."
            )
        
        return len(errors) == 0, errors, ltv_impact
    
    def validate_condo_requirements(
        self,
        property_type: PropertyType,
        is_warrantable: Optional[bool],
        loan_type: LoanType
    ) -> Tuple[bool, List[str], float]:
        """
        Validate condominium-specific requirements.
        
        Returns:
            Tuple of (is_eligible, errors, ltv_impact)
        """
        errors = []
        ltv_impact = 0.0
        
        if property_type not in [
            PropertyType.CONDO_WARRANTABLE, PropertyType.CONDO_NON_WARRANTABLE
        ]:
            return True, errors, ltv_impact
        
        if property_type == PropertyType.CONDO_NON_WARRANTABLE:
            if loan_type == LoanType.DSCR:
                # Non-warrantable DSCR: -10% LTV reduction
                ltv_impact -= 0.10
            elif loan_type in [LoanType.FIX_FLIP, LoanType.BRIDGE, LoanType.BRIDGE_PLUS, LoanType.GUC]:
                # RTL products: case-by-case
                # Return as eligible but flag warning
                pass
        
        return True, errors, ltv_impact
    
    def validate_market_conditions(
        self,
        is_declining: bool,
        hpa_pct: Optional[float],
        zhvi_mult: Optional[float]
    ) -> Tuple[bool, List[str], float]:
        """
        Validate market conditions and calculate leverage adjustments.
        
        Returns:
            Tuple of (is_eligible, warnings, ltv_impact)
        """
        warnings = []
        ltv_impact = 0.0
        
        if is_declining:
            warnings.append("Property located in declining market.")
            
            # HPA-based adjustment
            if hpa_pct is not None:
                if -10.0 <= hpa_pct < 0:
                    ltv_impact -= 0.05
                elif hpa_pct < -10.0:
                    ltv_impact -= 0.10
            
            # ZHVI-based adjustment
            if zhvi_mult is not None:
                if 2.0 < zhvi_mult <= 3.0:
                    ltv_impact -= 0.05
                elif zhvi_mult > 3.0:
                    ltv_impact -= 0.10
        
        return True, warnings, ltv_impact
    
    def full_eligibility_check(
        self,
        property_obj: Property,
        loan_type: LoanType
    ) -> PropertyEligibilityResult:
        """
        Perform comprehensive property eligibility assessment.
        
        Returns:
            PropertyEligibilityResult with all findings and LTV impact
        """
        all_issues = []
        all_warnings = []
        total_ltv_impact = 0.0
        
        # 1. Property Type Check
        is_valid, errors = self.validate_property_type(
            property_obj.property_type, loan_type
        )
        all_issues.extend(errors)
        
        # 2. Location Check
        is_valid, errors, ltv = self.validate_location(
            property_obj.state, property_obj.is_rural
        )
        all_issues.extend(errors)
        total_ltv_impact += ltv
        
        # 3. Condition Check
        is_valid, errors = self.validate_condition(
            property_obj.condition_rating, loan_type
        )
        all_issues.extend(errors)
        
        # 4. Size & Value Check
        is_valid, errors, ltv = self.validate_size_and_value(
            property_obj.property_type,
            property_obj.square_footage,
            property_obj.units,
            property_obj.acreage,
            property_obj.loan_amount
        )
        all_issues.extend(errors)
        total_ltv_impact += ltv
        
        # 5. Condo Requirements
        is_valid, errors, ltv = self.validate_condo_requirements(
            property_obj.property_type,
            property_obj.is_warrantable_condo,
            loan_type
        )
        all_issues.extend(errors)
        total_ltv_impact += ltv
        
        # 6. Market Conditions
        is_valid, warnings, ltv = self.validate_market_conditions(
            property_obj.is_in_declining_market,
            property_obj.hpa_percentage,
            property_obj.zhvi_multiplier
        )
        all_warnings.extend(warnings)
        total_ltv_impact += ltv
        
        overall_eligible = len(all_issues) == 0
        
        return PropertyEligibilityResult(
            is_eligible=overall_eligible,
            issues=all_issues,
            warnings=all_warnings,
            ltv_impact=total_ltv_impact
        )


# Example Usage
if __name__ == "__main__":
    checker = PropertyEligibilityChecker()
    
    # Example 1: Eligible SFR for Fix & Flip
    prop1 = Property(
        property_type=PropertyType.SFR,
        state="TX",
        is_rural=False,
        condition_rating=ConditionRating.C3,
        square_footage=1500,
        acreage=0.2,
        loan_amount=Decimal("250000")
    )
    
    result1 = checker.full_eligibility_check(prop1, LoanType.FIX_FLIP)
    print(f"Eligible SFR: {result1.is_eligible}, LTV Impact: {result1.ltv_impact:.0%}")
    
    # Example 2: Ineligible rural property
    prop2 = Property(
        property_type=PropertyType.SFR,
        state="GA",
        is_rural=True,
        condition_rating=ConditionRating.C4,
        square_footage=1800,
        acreage=0.5,
        loan_amount=Decimal("300000")
    )
    
    result2 = checker.full_eligibility_check(prop2, LoanType.DSCR)
    print(f"Rural Property: {result2.is_eligible}, Issues: {len(result2.issues)}")
    
    # Example 3: Non-warrantable condo for DSCR (with LTV reduction)
    prop3 = Property(
        property_type=PropertyType.CONDO_NON_WARRANTABLE,
        state="CA",
        is_rural=False,
        condition_rating=ConditionRating.C3,
        square_footage=800,
        units=1,
        acreage=0.05,
        is_warrantable_condo=False,
        loan_amount=Decimal("400000")
    )
    
    result3 = checker.full_eligibility_check(prop3, LoanType.DSCR)
    print(f"Non-Warrantable Condo (DSCR): {result3.is_eligible}, LTV Impact: {result3.ltv_impact:.0%}")
```

---

*End of Section 5*
