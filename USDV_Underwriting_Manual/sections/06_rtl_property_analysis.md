---
section: 6
title: RTL Property Analysis
version: 1.0
last_updated: 2025-12-30
model_used: sonnet
guideline_sources:
  - Archwest RTL Guidelines (PRIMARY)
  - Eastview RTL Guidelines v4.1
  - EV GUC Guidelines v1.0
  - RTL Program Guidelines 07.09.2025
changelog:
  - 2025-12-30: Initial creation
---

# Section 6: RTL Property Analysis

## 6.1 Overview

RTL (Residential Transition Loan) property analysis encompasses the evaluation of properties for Fix & Flip, Ground-Up Construction, and Bridge loan products. This section establishes standards for assessing property condition, validating scope of work, analyzing after-repair value (ARV), reviewing construction plans, and evaluating exit strategies.

**INSPIRE Integration Points:**
- Phase 1-2: RTL property data collection during application
- Phase 5-6: Feasibility study and construction plan review
- Phase 7: RTL-specific property analysis and flag generation

---

## 6.2 Fix & Flip Property Analysis

### 6.2.1 As-Is Condition Assessment

The as-is condition assessment establishes the property's current state and determines eligibility for Fix & Flip financing.

**Condition Rating Scale:**

| Rating | Description | Typical Characteristics | RTL Eligibility |
|--------|-------------|------------------------|-----------------|
| **C1** | New Construction | Built within last year, never occupied | Eligible (Bridge only) |
| **C2** | Recently Renovated | Fully updated within 5 years, excellent condition | Eligible |
| **C3** | Well Maintained | Good condition, minor cosmetic updates needed | Eligible |
| **C4** | Adequately Maintained | Average condition, moderate updates needed | Eligible |
| **C5** | Poorly Maintained | Deferred maintenance, substantial renovation needed | Eligible (standard RTL) |
| **C6** | Uninhabitable | Severe damage, health/safety hazards | Limited eligibility |

**As-Is Condition Evaluation Criteria:**

**Structural Elements:**
- Foundation (cracks, settling, water intrusion)
- Framing (load-bearing walls, roof structure)
- Roof (age, condition, remaining life)
- Windows and doors (functionality, weatherproofing)

**Systems:**
- Electrical (panel capacity, wiring condition, code compliance)
- Plumbing (supply lines, drain lines, fixtures)
- HVAC (age, condition, functionality)
- Water heater (age, capacity, condition)

**Interior:**
- Flooring (condition, type, coverage)
- Walls and ceilings (drywall condition, finishes)
- Kitchen (cabinets, countertops, appliances)
- Bathrooms (fixtures, tile, vanities)

**Exterior:**
- Siding/exterior finish (condition, weatherproofing)
- Landscaping (curb appeal, drainage)
- Driveway and walkways (condition, safety)
- Fencing (if applicable)

**Health and Safety Issues:**
- Mold or water damage
- Structural hazards
- Code violations
- Environmental concerns (lead paint, asbestos)

### 6.2.2 Scope of Work Evaluation

The scope of work defines all planned renovations and must be comprehensive, realistic, and adequately budgeted.

**Required Scope of Work Components:**

1. **Detailed Line-Item Budget**
   - Labor costs by trade
   - Material costs by category
   - Permit fees
   - Contingency (minimum 5% of rehab budget)
   - Soft costs (design, engineering, etc.)

2. **Timeline**
   - Start date
   - Completion date (must be within loan term)
   - Milestone schedule
   - Draw schedule alignment

3. **Contractor Information**
   - General contractor name and license
   - Insurance certificates
   - References or past projects
   - W-9 for payment processing

4. **Renovation Categories**

| Category | Typical Items | Budget Considerations |
|----------|--------------|----------------------|
| **Structural** | Foundation, framing, roof | High priority, safety-critical |
| **Systems** | Electrical, plumbing, HVAC | Code compliance required |
| **Interior** | Drywall, flooring, paint, kitchen, baths | Value-add focus |
| **Exterior** | Siding, windows, doors, landscaping | Curb appeal impact |
| **Permits** | Building permits, inspection fees | Required for major work |

**Scope of Work Red Flags:**

- Budget significantly below market rates for work described
- Timeline unrealistic for scope (e.g., gut rehab in 30 days)
- No contingency budget included
- Vague descriptions ("miscellaneous repairs")
- Missing critical systems (e.g., no HVAC budget for property without HVAC)
- Contractor unlicensed or uninsured
- Scope doesn't support claimed ARV

**Scope of Work Validation:**

```
Step 1: Review line-item budget for completeness
Step 2: Verify timeline is realistic (typical: 60-120 days for standard rehab)
Step 3: Confirm contractor qualifications
Step 4: Cross-reference scope with as-is condition
Step 5: Validate budget aligns with comparable renovated properties
Step 6: Ensure scope supports ARV valuation
```

### 6.2.3 After-Repair Value (ARV) Analysis

ARV is the estimated market value of the property after completion of all planned renovations.

**ARV Determination Methods:**

**Method 1: Appraisal Subject-to-Completion**
- Full appraisal with ARV opinion
- Appraiser reviews scope of work
- Provides as-is value and ARV
- Most reliable method

**Method 2: Comparable Sales Analysis**
- Analyze recent sales of renovated properties
- Adjust for differences in size, location, features
- Validate against scope of work
- Requires strong comparable data

**ARV Comparable Selection Criteria:**

| Criteria | Standard | Preferred |
|----------|----------|-----------|
| **Proximity** | Within 1 mile | Within 0.5 mile |
| **Sale Date** | Within 6 months | Within 3 months |
| **Property Type** | Same type (SFR, townhome, etc.) | Exact match |
| **Square Footage** | Within 20% | Within 10% |
| **Condition** | Renovated/updated | Recently renovated |
| **Bedroom/Bath Count** | Within 1 bed/bath | Exact match |

**ARV Adjustment Guidelines:**

```
Square Footage Adjustment:
- Typical: $50-$150 per sq ft difference (market-dependent)
- Higher in strong markets, lower in weak markets

Bedroom/Bath Adjustment:
- Additional bedroom: $10,000-$25,000
- Additional bathroom: $15,000-$30,000
- Half bath: $5,000-$10,000

Garage Adjustment:
- 1-car garage: $10,000-$20,000
- 2-car garage: $20,000-$40,000

Lot Size Adjustment:
- Typically $5,000-$15,000 per 1,000 sq ft difference

Condition Adjustment:
- Superior condition: +5-10%
- Inferior condition: -5-10%
```

**ARV Validation Checklist:**

- [ ] Minimum 3 comparable sales (6 preferred)
- [ ] All comps sold within 6 months
- [ ] All comps within 1 mile of subject
- [ ] Comps reflect similar renovation quality
- [ ] Adjustments documented and reasonable
- [ ] ARV supported by appraisal (if available)
- [ ] ARV aligns with scope of work quality
- [ ] ARV realistic for neighborhood

**ARV Red Flags:**

- ARV significantly exceeds neighborhood values (over-improvement)
- Limited comparable sales data
- Comps are distressed sales or foreclosures
- Large adjustments required (>20% per comp)
- ARV not supported by scope of work
- Appraiser ARV differs significantly from borrower estimate (>10%)

### 6.2.4 Heavy Rehab Definition and Impact

Heavy rehab projects require enhanced scrutiny and result in leverage reductions.

**Heavy Rehab Definition:**

A project is classified as "Heavy Rehab" if BOTH conditions are met:

1. **Rehab Budget > $50,000** AND
2. **Rehab Budget > 100% of Acquisition Cost**

Where:
- Acquisition Cost = Purchase Price (for purchases) or As-Is Value (for refinances)

**Heavy Rehab Examples:**

```
Example 1: Heavy Rehab (Purchase)
Purchase Price: $150,000
Rehab Budget: $175,000
Rehab Budget > $50,000? YES
Rehab Budget > 100% of Purchase? YES ($175K > $150K)
Classification: HEAVY REHAB

Example 2: Not Heavy Rehab (Purchase)
Purchase Price: $200,000
Rehab Budget: $125,000
Rehab Budget > $50,000? YES
Rehab Budget > 100% of Purchase? NO ($125K < $200K)
Classification: STANDARD REHAB

Example 3: Heavy Rehab (Refinance)
As-Is Value: $180,000
Rehab Budget: $200,000
Rehab Budget > $50,000? YES
Rehab Budget > 100% of As-Is? YES ($200K > $180K)
Classification: HEAVY REHAB

Example 4: Not Heavy Rehab (Small Budget)
Purchase Price: $100,000
Rehab Budget: $45,000
Rehab Budget > $50,000? NO
Classification: STANDARD REHAB (even though budget > 100% of purchase)
```

**Heavy Rehab Leverage Impact:**

| Borrower Class | Standard Leverage Reduction | Heavy Rehab Reduction |
|----------------|----------------------------|----------------------|
| **A+ / A / B** | None | -5% (all leverage metrics) |
| **C** | None | -10% (all leverage metrics) |

**Example Leverage Reduction:**

```
Borrower: Class A
Product: Fix & Flip Purchase
Standard Leverage: 85% As-Is LTV, 85% LTC, 70% LTARV

Heavy Rehab Project:
Adjusted Leverage: 80% As-Is LTV, 80% LTC, 65% LTARV
(5% reduction applied to all metrics)
```

**Heavy Rehab Enhanced Requirements:**

- Detailed scope of work with line-item budget
- Licensed and insured general contractor required
- Feasibility study or construction plan
- Progress inspection schedule (typically 3-4 inspections)
- Draw schedule with milestone-based releases
- Extended timeline approval (if needed)
- Enhanced contractor qualification review

---

## 6.3 Ground-Up Construction Analysis

### 6.3.1 Land Valuation

For ground-up construction projects, the land must be valued separately from the completed project.

**Land Valuation Methods:**

**Method 1: Recent Purchase**
- If land purchased within 6 months: Use purchase price
- Requires HUD-1 settlement statement
- Most straightforward method

**Method 2: Appraisal**
- Full appraisal of vacant land
- Comparable land sales analysis
- Highest and best use consideration
- Required if land held > 6 months

**Method 3: Lot Value from Builder Sales**
- Comparable new construction sales
- Extract land value from total sale price
- Requires strong comparable data

**Land Value Considerations:**

| Factor | Impact on Value | Notes |
|--------|----------------|-------|
| **Utilities Available** | +20-40% | Water, sewer, electric, gas |
| **Zoning** | Critical | Must allow intended use |
| **Topography** | ±10-30% | Flat preferred, steep slopes reduce value |
| **Access** | Critical | Road frontage, easements |
| **Size** | Varies | Must support intended structure |
| **Location** | High | Neighborhood, schools, amenities |

**Land Eligibility Requirements:**

- Clear title (no liens or encumbrances)
- Proper zoning for intended use
- Utilities available or feasible
- Access to public road
- No environmental issues (wetlands, contamination)
- Buildable lot (not landlocked, proper setbacks)

### 6.3.2 Plans and Specifications Review

Construction plans must be complete, professional, and approved by local authorities.

**Required Plan Components:**

1. **Architectural Plans**
   - Site plan showing property boundaries and structure placement
   - Floor plans for all levels
   - Elevations (all four sides)
   - Foundation plan
   - Roof plan
   - Cross-sections

2. **Structural Plans**
   - Foundation design
   - Framing plan
   - Load calculations
   - Beam and header sizing

3. **Mechanical Plans**
   - HVAC layout and sizing
   - Plumbing layout
   - Electrical layout and panel sizing

4. **Specifications**
   - Materials specifications
   - Finish schedules
   - Appliance and fixture specifications
   - Energy efficiency features

**Plan Review Criteria:**

- Plans prepared by licensed architect or designer
- Plans stamped by engineer (if required by jurisdiction)
- Plans consistent with construction budget
- Square footage matches loan application
- Bedroom/bathroom count matches application
- Finishes appropriate for market
- Design appropriate for neighborhood

### 6.3.3 Construction Budget Validation

The construction budget must be comprehensive, realistic, and support the projected value.

**Construction Budget Categories:**

| Category | Typical % of Total | Notes |
|----------|-------------------|-------|
| **Site Work** | 5-10% | Clearing, grading, utilities |
| **Foundation** | 8-12% | Footings, stem walls, slab |
| **Framing** | 15-20% | Lumber, labor, trusses |
| **Exterior** | 12-18% | Siding, roofing, windows, doors |
| **Mechanical** | 12-15% | HVAC, plumbing, electrical |
| **Interior** | 20-25% | Drywall, flooring, cabinets, trim |
| **Finishes** | 8-12% | Paint, tile, countertops, fixtures |
| **Soft Costs** | 5-8% | Permits, engineering, inspections |
| **Contingency** | 5-10% | Unexpected costs |

**Budget Validation Methods:**

**Method 1: Cost Per Square Foot Analysis**
```
Total Construction Budget / Gross Living Area = Cost per Sq Ft

Typical Ranges (varies by market and quality):
- Entry Level: $100-$150 per sq ft
- Mid-Range: $150-$200 per sq ft
- High-End: $200-$300+ per sq ft

Example:
Construction Budget: $400,000
Gross Living Area: 2,500 sq ft
Cost per Sq Ft: $160
Assessment: Mid-range construction, reasonable for suburban market
```

**Method 2: Comparable Construction Costs**
- Analyze recent construction projects in area
- Adjust for size, quality, and features
- Validate budget is in line with market

**Method 3: Contractor Bid Review**
- Review detailed contractor bid
- Compare to independent cost estimates
- Verify all categories included

**Budget Red Flags:**

- Cost per sq ft significantly below market norms
- Missing budget categories (e.g., no contingency)
- Vague line items ("miscellaneous")
- Budget doesn't support finish quality claimed
- Soft costs not included
- Contingency < 5%

### 6.3.4 Permit Status and Timeline

Building permits must be obtained or obtainable, and timeline must be realistic.

**Permit Status Requirements:**

| Status | Eligibility | Requirements |
|--------|-------------|--------------|
| **Permits Issued** | Eligible | Provide permit copies |
| **Permits Submitted** | Eligible | Provide submission proof, approval timeline |
| **Permits Not Yet Submitted** | Conditional | Plans must be complete, submit within 30 days |
| **Permits Denied** | Not Eligible | Must resolve denial issues |

**Required Permits:**

- Building permit (primary)
- Electrical permit
- Plumbing permit
- Mechanical permit
- Grading permit (if applicable)
- Septic permit (if applicable)

**Timeline Validation:**

**Typical Construction Timeline by Size:**

| Home Size | Typical Timeline | Loan Term |
|-----------|-----------------|-----------|
| < 1,500 sq ft | 6-9 months | 12 months |
| 1,500-2,500 sq ft | 8-12 months | 12-18 months |
| 2,500-4,000 sq ft | 10-14 months | 18 months |
| > 4,000 sq ft | 12-18 months | 18-24 months |

**Timeline Factors:**

- Weather (seasonal delays)
- Material availability
- Labor availability
- Permit inspection schedule
- Complexity of design
- Site conditions

**Timeline Red Flags:**

- Timeline significantly shorter than typical for size/complexity
- No buffer for delays
- Doesn't account for permit approval time
- Doesn't align with draw schedule
- Exceeds maximum loan term

### 6.3.5 General Contractor Qualification

The general contractor must be qualified, licensed, and financially stable.

**Required Contractor Documentation:**

1. **Licensing and Insurance**
   - Valid general contractor license (state-specific)
   - General liability insurance ($1M+ coverage)
   - Workers' compensation insurance
   - Builder's risk insurance (or will obtain)

2. **Experience and References**
   - Minimum 3 years construction experience
   - Minimum 5 completed projects
   - References from recent projects
   - Photos of completed work

3. **Financial Stability**
   - W-9 for tax reporting
   - Business bank account information
   - No recent bankruptcies
   - No significant liens or judgments

4. **Contract**
   - Written construction contract
   - Scope of work detailed
   - Payment schedule defined
   - Timeline specified
   - Warranty provisions

**Contractor Red Flags:**

- Unlicensed or license expired
- Insufficient insurance coverage
- No verifiable experience
- Recent business failure
- Poor references or no references
- Unwilling to provide documentation

---

## 6.4 Bridge Loan Property Analysis

### 6.4.1 Stabilized Property Standards

Bridge loans are for properties that are already stabilized with NO planned renovation budget. Any transaction that includes a rehab component is classified as Fix & Flip, not Bridge.

**Stabilized Property Definition:**

A property is considered stabilized if:
- Property is in C2-C4 condition (good to excellent)
- No major systems need replacement
- Property is habitable and marketable
- No renovation budget required

**Bridge Loan Property Requirements:**

| Requirement | Standard | Notes |
|-------------|----------|-------|
| **Condition** | C2-C4 | Well-maintained to excellent |
| **Systems** | Functional | All major systems operational |
| **Habitability** | Habitable | Can be occupied immediately |
| **Renovation Budget** | $0 (no rehab escrow) | Any rehab budget = Fix & Flip product |
| **Occupancy** | Vacant or occupied | Both acceptable |

**Important Distinction:**
- **Bridge Loan**: No rehab escrow, no renovation budget. Property is stabilized as-is.
- **Fix & Flip**: Any transaction with a rehab budget or escrow, regardless of amount.

**Bridge vs. Fix & Flip Determination:**

```
Decision Tree:

Renovation Budget = $0 (no rehab escrow)?
├─ YES: Consider Bridge Loan
│  └─ Property Condition C2-C4?
│     ├─ YES: Bridge Loan Appropriate
│     └─ NO: Not eligible for Bridge
└─ NO: Fix & Flip Required (any rehab budget)
```

### 6.4.2 Bridge Loan Clarifications

**Important:** Bridge loans have NO rehab escrow or renovation budget. If any renovation work is planned, the transaction must be structured as Fix & Flip, regardless of the scope or amount.

**What Qualifies as Bridge:**

- Property purchased or refinanced as-is
- No planned renovations
- No rehab budget or escrow
- Property is rent-ready or sale-ready in current condition
- Certificate of Occupancy already in place (or obtainable without work)

**What Requires Fix & Flip Product:**

Any transaction with planned renovation work, including:
- Any rehab budget, regardless of amount
- Any rehab escrow account
- Interior renovations (paint, flooring, etc.)
- Kitchen or bathroom updates
- System replacements (HVAC, roof, etc.)
- Structural repairs
- Deferred maintenance corrections
- Cosmetic improvements

**Bridge Loan Use Cases:**

1. **Acquisition Bridge**: Investor purchasing stabilized property for rental or quick resale
2. **Refinance Bridge**: Refinancing existing property that requires no work
3. **Portfolio Bridge**: Short-term financing for stabilized rental portfolio
4. **Exit Bridge**: Temporary financing before permanent DSCR financing

### 6.4.3 Bridge Loan Exit Strategies

Bridge loans require a clear exit strategy within the loan term.

**Acceptable Exit Strategies:**

**Exit 1: Sale**
- Property listed with licensed agent
- Realistic pricing based on comparable sales
- Timeline aligns with loan term
- Market conditions support sale

**Exit 2: Refinance to DSCR**
- Property will be rented
- Projected rent supports DSCR requirements
- Borrower meets DSCR eligibility
- Property meets DSCR property requirements

**Exit 3: Refinance to Conventional**
- Borrower will occupy or rent
- Borrower qualifies for conventional financing
- Property meets conventional standards
- Seasoning requirements met (if applicable)

**Exit 4: Cash Payoff**
- Borrower has demonstrated liquidity
- Sale of other asset
- Business proceeds
- Other documented source

**Exit Strategy Documentation:**

- Written exit strategy plan
- Supporting financial analysis
- Timeline with milestones
- Contingency plan (Plan B)

---

## 6.5 Feasibility Study Review

### 6.5.1 Feasibility Study Requirements

For projects with rehab budgets > $100,000 or all ground-up construction, a professional feasibility study is required.

**Feasibility Study Components:**

1. **Property Analysis**
   - As-is condition assessment
   - Property measurements and photos
   - Neighborhood analysis
   - Comparable sales analysis

2. **Scope of Work**
   - Detailed renovation plan
   - Line-item budget by category
   - Material specifications
   - Timeline with milestones

3. **After-Repair Value**
   - Comparable sales analysis
   - Adjustment methodology
   - ARV opinion with support
   - Market analysis

4. **Financial Analysis**
   - Total project cost
   - Projected profit
   - Return on investment
   - Sensitivity analysis

5. **Risk Assessment**
   - Market risks
   - Construction risks
   - Timeline risks
   - Mitigation strategies

**Feasibility Study Provider Qualifications:**

- Licensed contractor, OR
- Licensed appraiser, OR
- Real estate consultant with construction experience
- Minimum 5 years experience
- Errors & omissions insurance
- Independent third party (not borrower or contractor)

### 6.5.2 Budget Alignment Tolerance

The feasibility study budget must align with the borrower's budget and contractor bid.

**Acceptable Variance:**

| Variance | Status | Action Required |
|----------|--------|-----------------|
| **< 5%** | Excellent | No action |
| **5-10%** | Acceptable | Document variance |
| **10-15%** | Acceptable with review | Explanation required |
| **> 15%** | Not acceptable | Reconcile or obtain new estimate |

**Variance Calculation:**

```
Variance % = |Feasibility Budget - Borrower Budget| / Feasibility Budget × 100

Example 1: Acceptable Variance
Feasibility Budget: $150,000
Borrower Budget: $145,000
Variance: |$150K - $145K| / $150K = 3.3% → ACCEPTABLE

Example 2: High Variance
Feasibility Budget: $200,000
Borrower Budget: $165,000
Variance: |$200K - $165K| / $200K = 17.5% → NOT ACCEPTABLE
```

**Variance Resolution:**

- If feasibility budget higher: Increase loan amount or reduce scope
- If borrower budget higher: Justify additional costs or reduce budget
- Obtain third opinion if significant disagreement
- Document final budget and rationale

### 6.5.3 Timeline Reasonableness

The proposed timeline must be realistic for the scope of work.

**Timeline Benchmarks:**

**Fix & Flip Projects:**

| Scope | Typical Timeline | Maximum Loan Term |
|-------|-----------------|-------------------|
| **Light Rehab** (< $50K) | 30-60 days | 12 months |
| **Moderate Rehab** ($50K-$100K) | 60-90 days | 12 months |
| **Heavy Rehab** ($100K-$200K) | 90-150 days | 18 months |
| **Extensive Rehab** (> $200K) | 150-240 days | 24 months |

**Ground-Up Construction:**

| Size | Typical Timeline | Maximum Loan Term |
|------|-----------------|-------------------|
| < 2,000 sq ft | 6-9 months | 12 months |
| 2,000-3,000 sq ft | 8-12 months | 18 months |
| 3,000-4,000 sq ft | 10-14 months | 18 months |
| > 4,000 sq ft | 12-18 months | 24 months |

**Timeline Red Flags:**

- Timeline < 50% of typical for scope
- No contingency time built in
- Doesn't account for permit delays
- Doesn't account for weather delays
- Doesn't align with contractor availability
- Exceeds maximum loan term

### 6.5.4 Contingency Requirements

All budgets must include contingency for unexpected costs.

**Minimum Contingency:**

| Project Type | Minimum Contingency | Preferred |
|--------------|-------------------|-----------|
| **Light Rehab** | 5% of rehab budget | 10% |
| **Moderate Rehab** | 5% of rehab budget | 10% |
| **Heavy Rehab** | 10% of rehab budget | 15% |
| **Ground-Up Construction** | 10% of construction budget | 15% |

**Contingency Calculation:**

```
Minimum Contingency = Rehab Budget × Contingency %

Example:
Rehab Budget: $150,000
Project Type: Heavy Rehab
Minimum Contingency: $150,000 × 10% = $15,000
```

**Contingency Usage:**

- Held in reserve until needed
- Released only for legitimate cost overruns
- Requires documentation of additional work
- Cannot be used to increase loan amount retroactively

---

## 6.6 Exit Strategy Validation

### 6.6.1 Exit Strategy Requirements

All RTL loans require a documented exit strategy demonstrating how the loan will be repaid.

**Exit Strategy Components:**

1. **Primary Exit Plan**
   - Detailed description of exit method
   - Timeline to execution
   - Financial analysis supporting feasibility
   - Market conditions assessment

2. **Supporting Documentation**
   - Comparable sales or rent data
   - Pre-qualification letter (if refinancing)
   - Listing agreement (if selling)
   - Financial statements (if cash payoff)

3. **Contingency Plan**
   - Alternative exit if primary plan fails
   - Timeline for contingency
   - Financial impact analysis

### 6.6.2 Exit Strategy by Type

**Exit Strategy 1: Sale (Most Common)**

**Requirements:**
- Realistic ARV based on comparable sales
- Market absorption time < 6 months
- Pricing strategy defined
- Real estate agent identified (preferred)

**Validation:**
```
Sale Feasibility Check:

1. ARV Validation
   - Minimum 3 comparable sales
   - Sales within 6 months
   - Adjustments < 20% per comp

2. Market Absorption
   - Days on market for comps < 90 days
   - Inventory levels reasonable
   - No declining market indicators

3. Profit Analysis
   - Gross Profit = ARV - Total Cost
   - Total Cost = Purchase + Rehab + Holding + Closing
   - Minimum Gross Profit: 15% of ARV (preferred 20%+)

Example:
ARV: $450,000
Total Cost: $360,000
Gross Profit: $90,000 (20% of ARV) → ACCEPTABLE
```

**Exit Strategy 2: Refinance to DSCR**

**Requirements:**
- Property will be rented
- Market rent supports minimum DSCR
- Borrower meets DSCR eligibility (FICO 680+)
- Property meets DSCR property standards

**Validation:**
```
DSCR Refinance Feasibility:

1. Rent Analysis
   - Market rent from comparable rentals
   - Minimum 3 comparable rentals
   - Rentals within 1 mile, leased within 6 months

2. DSCR Calculation
   - Qualifying Rent = 100% Market Rent (if unleased)
   - Monthly PITIA = P&I + Taxes/12 + Insurance/12 + HOA
   - DSCR = Qualifying Rent / Monthly PITIA
   - Minimum DSCR: 1.00x (FICO 700+) or 1.20x (FICO 680-699)

3. LTV Analysis
   - Maximum DSCR LTV: 75-80% (based on FICO)
   - Projected Loan Amount = ARV × Max LTV
   - Must be sufficient to pay off RTL loan

Example:
ARV: $450,000
Market Rent: $2,500/month
Projected DSCR Loan: $360,000 (80% LTV)
Monthly PITIA: $2,300
DSCR: $2,500 / $2,300 = 1.09x → ACCEPTABLE
DSCR Loan Amount > RTL Payoff? YES → FEASIBLE
```

**Exit Strategy 3: Refinance to Conventional**

**Requirements:**
- Borrower qualifies for conventional financing
- Property meets conventional standards
- Seasoning requirements met (typically 6-12 months)
- Sufficient equity for conventional LTV limits

**Validation:**
- Pre-qualification letter from conventional lender
- Credit score meets conventional minimums (typically 620+)
- Debt-to-income ratio acceptable
- Occupancy plans (owner-occupied or investment)

**Exit Strategy 4: Cash Payoff**

**Requirements:**
- Documented source of funds
- Liquidity verification
- Timeline for fund availability

**Acceptable Sources:**
- Sale of other property (under contract)
- Business sale or distribution
- Investment liquidation
- Inheritance or gift
- Other documented source

**Validation:**
- Bank statements showing liquidity
- Purchase agreement (if property sale)
- Business sale agreement (if business)
- Other documentation as applicable

### 6.6.3 Exit Strategy Red Flags

- No documented exit strategy
- Exit strategy not feasible based on market conditions
- Timeline exceeds loan term
- No contingency plan
- Over-improvement (ARV exceeds neighborhood norms by >20%)
- Insufficient profit margin (< 10% of ARV)
- Market declining or oversupplied
- Borrower has history of failed exits

---

## 6.7 Python Implementation

### 6.7.1 RTL Property Analysis Module

```python
"""
RTL Property Analysis Module
Analyzes properties for Fix & Flip, Ground-Up Construction, and Bridge loans.
"""

from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List, Optional, Dict, Tuple


class PropertyCondition(Enum):
    """Property condition ratings"""
    C1 = "C1"  # New construction
    C2 = "C2"  # Recently renovated
    C3 = "C3"  # Well maintained
    C4 = "C4"  # Adequately maintained
    C5 = "C5"  # Poorly maintained
    C6 = "C6"  # Uninhabitable


class RTLProductType(Enum):
    """RTL product types"""
    FIX_FLIP = "FIX_FLIP"
    GROUND_UP_CONSTRUCTION = "GUC"
    BRIDGE = "BRIDGE"


class ExitStrategy(Enum):
    """Exit strategy types"""
    SALE = "SALE"
    REFINANCE_DSCR = "REFINANCE_DSCR"
    REFINANCE_CONVENTIONAL = "REFINANCE_CONVENTIONAL"
    CASH_PAYOFF = "CASH_PAYOFF"


@dataclass
class PropertyInfo:
    """Basic property information"""
    address: str
    property_type: str
    square_footage: int
    bedrooms: int
    bathrooms: float
    year_built: int
    lot_size: float
    condition: PropertyCondition


@dataclass
class ComparableSale:
    """Comparable sale for ARV analysis"""
    address: str
    sale_date: date
    sale_price: float
    square_footage: int
    bedrooms: int
    bathrooms: float
    distance_miles: float
    condition: str
    adjustments: Dict[str, float]
    adjusted_price: float


@dataclass
class ScopeOfWork:
    """Renovation scope of work"""
    budget_items: Dict[str, float]  # Category: Amount
    total_budget: float
    contingency: float
    timeline_days: int
    contractor_name: str
    contractor_licensed: bool
    contractor_insured: bool


@dataclass
class HeavyRehabAnalysis:
    """Heavy rehab determination"""
    is_heavy_rehab: bool
    rehab_budget: float
    acquisition_cost: float
    budget_threshold_met: bool  # > $50K
    ratio_threshold_met: bool  # > 100% of acquisition
    leverage_reduction: float  # 0.05 or 0.10
    explanation: str


@dataclass
class ARVAnalysis:
    """After-repair value analysis"""
    arv: float
    comparable_sales: List[ComparableSale]
    arv_per_sqft: float
    confidence_level: str  # HIGH, MEDIUM, LOW
    supporting_factors: List[str]
    concerns: List[str]


class RTLPropertyAnalyzer:
    """
    Analyze properties for RTL loan products.
    """
    
    # Heavy rehab thresholds
    HEAVY_REHAB_BUDGET_THRESHOLD = 50000.0
    HEAVY_REHAB_RATIO_THRESHOLD = 1.0  # 100%
    
    # Leverage reductions for heavy rehab
    HEAVY_REHAB_REDUCTION_AB = 0.05  # 5% for Class A/B
    HEAVY_REHAB_REDUCTION_C = 0.10  # 10% for Class C
    
    # Bridge loan thresholds
    BRIDGE_MAX_REHAB_BUDGET = 0.0  # Bridge loans have NO rehab budget
    
    # Contingency minimums
    MIN_CONTINGENCY_LIGHT = 0.05  # 5%
    MIN_CONTINGENCY_HEAVY = 0.10  # 10%
    MIN_CONTINGENCY_GUC = 0.10  # 10%
    
    def is_heavy_rehab(
        self,
        rehab_budget: float,
        acquisition_cost: float,
        is_purchase: bool
    ) -> HeavyRehabAnalysis:
        """
        Determine if project qualifies as heavy rehab.
        
        Heavy Rehab Definition:
        - Rehab budget > $50,000 AND
        - Rehab budget > 100% of acquisition cost
        
        Args:
            rehab_budget: Total renovation budget
            acquisition_cost: Purchase price (purchase) or as-is value (refi)
            is_purchase: True if purchase transaction
            
        Returns:
            HeavyRehabAnalysis with determination and details
        """
        # Check budget threshold
        budget_threshold_met = rehab_budget > self.HEAVY_REHAB_BUDGET_THRESHOLD
        
        # Check ratio threshold
        ratio = rehab_budget / acquisition_cost if acquisition_cost > 0 else 0
        ratio_threshold_met = ratio > self.HEAVY_REHAB_RATIO_THRESHOLD
        
        # Both must be true for heavy rehab
        is_heavy = budget_threshold_met and ratio_threshold_met
        
        # Determine leverage reduction (will be applied based on borrower class)
        leverage_reduction = 0.0  # Will be 0.05 or 0.10 based on class
        
        # Build explanation
        if is_heavy:
            explanation = (
                f"HEAVY REHAB: Budget ${rehab_budget:,.0f} exceeds ${self.HEAVY_REHAB_BUDGET_THRESHOLD:,.0f} "
                f"AND exceeds {self.HEAVY_REHAB_RATIO_THRESHOLD:.0%} of acquisition cost "
                f"(${acquisition_cost:,.0f}). Ratio: {ratio:.1%}"
            )
        elif budget_threshold_met and not ratio_threshold_met:
            explanation = (
                f"STANDARD REHAB: Budget ${rehab_budget:,.0f} exceeds ${self.HEAVY_REHAB_BUDGET_THRESHOLD:,.0f} "
                f"but does not exceed {self.HEAVY_REHAB_RATIO_THRESHOLD:.0%} of acquisition cost. "
                f"Ratio: {ratio:.1%}"
            )
        elif ratio_threshold_met and not budget_threshold_met:
            explanation = (
                f"STANDARD REHAB: Budget ${rehab_budget:,.0f} is below ${self.HEAVY_REHAB_BUDGET_THRESHOLD:,.0f} "
                f"threshold (even though ratio is {ratio:.1%})"
            )
        else:
            explanation = (
                f"STANDARD REHAB: Budget ${rehab_budget:,.0f} below ${self.HEAVY_REHAB_BUDGET_THRESHOLD:,.0f} "
                f"and ratio {ratio:.1%} below {self.HEAVY_REHAB_RATIO_THRESHOLD:.0%}"
            )
        
        return HeavyRehabAnalysis(
            is_heavy_rehab=is_heavy,
            rehab_budget=rehab_budget,
            acquisition_cost=acquisition_cost,
            budget_threshold_met=budget_threshold_met,
            ratio_threshold_met=ratio_threshold_met,
            leverage_reduction=leverage_reduction,
            explanation=explanation
        )
    
    def validate_bridge_eligibility(
        self,
        property_condition: PropertyCondition,
        rehab_budget: float
    ) -> Tuple[bool, str]:
        """
        Validate if property is eligible for bridge loan.
        
        Bridge loans require:
        - Property condition C2-C4
        - NO rehab budget (must be $0)
        
        Args:
            property_condition: Property condition rating
            rehab_budget: Planned renovation budget
            
        Returns:
            Tuple of (is_eligible, message)
        """
        # Check condition
        acceptable_conditions = [
            PropertyCondition.C2,
            PropertyCondition.C3,
            PropertyCondition.C4
        ]
        
        condition_ok = property_condition in acceptable_conditions
        budget_ok = rehab_budget == self.BRIDGE_MAX_REHAB_BUDGET  # Must be exactly $0
        
        if condition_ok and budget_ok:
            return True, (
                f"Bridge loan eligible: Condition {property_condition.value} "
                f"and no rehab budget (stabilized property)"
            )
        elif not condition_ok and budget_ok:
            return False, (
                f"Bridge loan not eligible: Condition {property_condition.value} "
                f"requires C2-C4. Property not stabilized."
            )
        elif condition_ok and not budget_ok:
            return False, (
                f"Bridge loan not eligible: Rehab budget ${rehab_budget:,.0f} present. "
                f"Any rehab budget requires Fix & Flip product."
            )
        else:
            return False, (
                f"Bridge loan not eligible: Condition {property_condition.value} "
                f"and rehab budget ${rehab_budget:,.0f}. "
                f"Use Fix & Flip product."
            )
    
    def validate_contingency(
        self,
        rehab_budget: float,
        contingency: float,
        is_heavy_rehab: bool,
        is_guc: bool
    ) -> Tuple[bool, str]:
        """
        Validate contingency is sufficient.
        
        Args:
            rehab_budget: Total rehab/construction budget
            contingency: Contingency amount
            is_heavy_rehab: True if heavy rehab project
            is_guc: True if ground-up construction
            
        Returns:
            Tuple of (is_sufficient, message)
        """
        # Determine minimum contingency percentage
        if is_guc:
            min_pct = self.MIN_CONTINGENCY_GUC
            project_type = "Ground-Up Construction"
        elif is_heavy_rehab:
            min_pct = self.MIN_CONTINGENCY_HEAVY
            project_type = "Heavy Rehab"
        else:
            min_pct = self.MIN_CONTINGENCY_LIGHT
            project_type = "Standard Rehab"
        
        min_contingency = rehab_budget * min_pct
        contingency_pct = contingency / rehab_budget if rehab_budget > 0 else 0
        
        if contingency >= min_contingency:
            return True, (
                f"Contingency ${contingency:,.0f} ({contingency_pct:.1%}) "
                f"meets minimum {min_pct:.0%} for {project_type}"
            )
        else:
            return False, (
                f"Contingency ${contingency:,.0f} ({contingency_pct:.1%}) "
                f"below minimum ${min_contingency:,.0f} ({min_pct:.0%}) "
                f"for {project_type}"
            )
    
    def analyze_arv_comparables(
        self,
        subject_property: PropertyInfo,
        comparable_sales: List[ComparableSale],
        proposed_arv: float
    ) -> ARVAnalysis:
        """
        Analyze ARV based on comparable sales.
        
        Args:
            subject_property: Subject property information
            comparable_sales: List of comparable sales
            proposed_arv: Proposed ARV from borrower/appraiser
            
        Returns:
            ARVAnalysis with validation and confidence level
        """
        if not comparable_sales:
            return ARVAnalysis(
                arv=proposed_arv,
                comparable_sales=[],
                arv_per_sqft=proposed_arv / subject_property.square_footage,
                confidence_level="LOW",
                supporting_factors=[],
                concerns=["No comparable sales provided"]
            )
        
        # Calculate ARV per sq ft
        arv_per_sqft = proposed_arv / subject_property.square_footage
        
        # Analyze comparables
        supporting_factors = []
        concerns = []
        
        # Check number of comps
        if len(comparable_sales) >= 6:
            supporting_factors.append(f"{len(comparable_sales)} comparable sales (excellent)")
        elif len(comparable_sales) >= 3:
            supporting_factors.append(f"{len(comparable_sales)} comparable sales (adequate)")
        else:
            concerns.append(f"Only {len(comparable_sales)} comparable sales (minimum 3 preferred)")
        
        # Check recency
        recent_comps = [c for c in comparable_sales 
                       if (date.today() - c.sale_date).days <= 180]
        if len(recent_comps) == len(comparable_sales):
            supporting_factors.append("All comps within 6 months")
        elif len(recent_comps) >= len(comparable_sales) * 0.5:
            supporting_factors.append(f"{len(recent_comps)} of {len(comparable_sales)} comps within 6 months")
        else:
            concerns.append("Multiple comps older than 6 months")
        
        # Check proximity
        close_comps = [c for c in comparable_sales if c.distance_miles <= 1.0]
        if len(close_comps) == len(comparable_sales):
            supporting_factors.append("All comps within 1 mile")
        elif len(close_comps) >= len(comparable_sales) * 0.5:
            supporting_factors.append(f"{len(close_comps)} of {len(comparable_sales)} comps within 1 mile")
        else:
            concerns.append("Multiple comps beyond 1 mile")
        
        # Calculate average adjusted price per sq ft
        comp_prices_per_sqft = [
            c.adjusted_price / c.square_footage 
            for c in comparable_sales
        ]
        avg_comp_price_per_sqft = sum(comp_prices_per_sqft) / len(comp_prices_per_sqft)
        
        # Compare ARV to comp average
        variance_pct = abs(arv_per_sqft - avg_comp_price_per_sqft) / avg_comp_price_per_sqft
        
        if variance_pct <= 0.05:
            supporting_factors.append(
                f"ARV ${arv_per_sqft:.0f}/sqft within 5% of comp average ${avg_comp_price_per_sqft:.0f}/sqft"
            )
        elif variance_pct <= 0.10:
            supporting_factors.append(
                f"ARV ${arv_per_sqft:.0f}/sqft within 10% of comp average ${avg_comp_price_per_sqft:.0f}/sqft"
            )
        else:
            concerns.append(
                f"ARV ${arv_per_sqft:.0f}/sqft differs {variance_pct:.1%} from comp average ${avg_comp_price_per_sqft:.0f}/sqft"
            )
        
        # Determine confidence level
        if len(concerns) == 0 and len(supporting_factors) >= 3:
            confidence_level = "HIGH"
        elif len(concerns) <= 1:
            confidence_level = "MEDIUM"
        else:
            confidence_level = "LOW"
        
        return ARVAnalysis(
            arv=proposed_arv,
            comparable_sales=comparable_sales,
            arv_per_sqft=arv_per_sqft,
            confidence_level=confidence_level,
            supporting_factors=supporting_factors,
            concerns=concerns
        )
    
    def validate_scope_of_work(
        self,
        scope: ScopeOfWork,
        is_heavy_rehab: bool
    ) -> Tuple[bool, List[str]]:
        """
        Validate scope of work is complete and reasonable.
        
        Args:
            scope: Scope of work details
            is_heavy_rehab: True if heavy rehab project
            
        Returns:
            Tuple of (is_valid, list of issues)
        """
        issues = []
        
        # Check contractor licensing
        if not scope.contractor_licensed:
            issues.append("Contractor must be licensed")
        
        # Check contractor insurance
        if not scope.contractor_insured:
            issues.append("Contractor must be insured")
        
        # Check contingency
        contingency_valid, contingency_msg = self.validate_contingency(
            scope.total_budget,
            scope.contingency,
            is_heavy_rehab,
            False
        )
        if not contingency_valid:
            issues.append(contingency_msg)
        
        # Check budget completeness
        required_categories = ["Labor", "Materials"]
        for category in required_categories:
            if category not in scope.budget_items:
                issues.append(f"Missing budget category: {category}")
        
        # Check timeline reasonableness
        if scope.total_budget < 50000 and scope.timeline_days > 90:
            issues.append(f"Timeline {scope.timeline_days} days seems long for ${scope.total_budget:,.0f} budget")
        elif scope.total_budget >= 50000 and scope.total_budget < 100000 and scope.timeline_days < 45:
            issues.append(f"Timeline {scope.timeline_days} days seems short for ${scope.total_budget:,.0f} budget")
        elif scope.total_budget >= 100000 and scope.timeline_days < 60:
            issues.append(f"Timeline {scope.timeline_days} days seems short for ${scope.total_budget:,.0f} budget")
        
        is_valid = len(issues) == 0
        return is_valid, issues
    
    def validate_exit_strategy_sale(
        self,
        arv: float,
        total_cost: float,
        market_days_on_market: int
    ) -> Tuple[bool, str]:
        """
        Validate sale exit strategy feasibility.
        
        Args:
            arv: After-repair value
            total_cost: Total project cost (purchase + rehab + holding + closing)
            market_days_on_market: Average days on market for comparable sales
            
        Returns:
            Tuple of (is_feasible, message)
        """
        # Calculate profit
        gross_profit = arv - total_cost
        profit_margin = gross_profit / arv if arv > 0 else 0
        
        # Check profit margin
        if profit_margin < 0:
            return False, f"Negative profit: ARV ${arv:,.0f} < Total Cost ${total_cost:,.0f}"
        elif profit_margin < 0.10:
            return False, (
                f"Insufficient profit margin {profit_margin:.1%} "
                f"(minimum 10% preferred, 15%+ recommended)"
            )
        elif profit_margin < 0.15:
            return True, (
                f"Marginal profit margin {profit_margin:.1%} "
                f"(15%+ recommended). Gross profit: ${gross_profit:,.0f}"
            )
        else:
            return True, (
                f"Acceptable profit margin {profit_margin:.1%}. "
                f"Gross profit: ${gross_profit:,.0f}"
            )


# Example usage
if __name__ == "__main__":
    analyzer = RTLPropertyAnalyzer()
    
    # Example 1: Heavy rehab determination
    heavy_rehab = analyzer.is_heavy_rehab(
        rehab_budget=175000,
        acquisition_cost=150000,
        is_purchase=True
    )
    print(f"Heavy Rehab: {heavy_rehab.is_heavy_rehab}")
    print(heavy_rehab.explanation)
    print()
    
    # Example 2: Bridge eligibility
    bridge_eligible, bridge_msg = analyzer.validate_bridge_eligibility(
        property_condition=PropertyCondition.C3,
        rehab_budget=0  # Bridge requires $0 rehab budget
    )
    print(f"Bridge Eligible: {bridge_eligible}")
    print(bridge_msg)
    print()
    
    # Example 3: Exit strategy validation
    exit_feasible, exit_msg = analyzer.validate_exit_strategy_sale(
        arv=450000,
        total_cost=360000,
        market_days_on_market=45
    )
    print(f"Exit Feasible: {exit_feasible}")
    print(exit_msg)
```

---

## 6.8 Cross-References

**Related Sections:**
- **Section 5**: Property Eligibility Standards - General property eligibility requirements
- **Section 7**: DSCR Property & Income Analysis - For DSCR refinance exit strategies
- **Section 8**: Appraisal & Valuation Review - ARV and as-is value validation
- **Section 9**: RTL Loan Sizing & Leverage - How property analysis impacts loan sizing
- **Section 14**: Third-Party Report Analysis - Feasibility study and appraisal analysis

---

*End of Section 6*

