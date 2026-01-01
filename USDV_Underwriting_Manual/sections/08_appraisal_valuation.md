---
section: 8
title: Appraisal & Valuation Review
version: 1.0
last_updated: 2025-12-30
model_used: sonnet
guideline_sources:
  - Archwest RTL Guidelines (PRIMARY for RTL)
  - Eastview DSCR Guidelines v7.2 (PRIMARY for DSCR)
  - Eastview RTL Guidelines v4.1
  - Archwest DSCR Guidelines v1.8
changelog:
  - 2025-12-30: Initial creation
---

# Section 8: Appraisal & Valuation Review

## 8.1 Overview

Appraisal and valuation review is critical to determining appropriate loan sizing and ensuring adequate collateral protection. This section establishes standards for appraisal requirements, review procedures, value analysis, and variance handling for both RTL and DSCR loan products.

**INSPIRE Integration Points:**
- Phase 5-6: Appraisal ordering and receipt
- Phase 7: Automated appraisal analysis and flag generation
- Phase 7: Value variance detection and resolution

---

## 8.2 Appraisal Types and Requirements

### 8.2.1 Appraisal Types by Loan Product

| Loan Type | Primary Appraisal Type | Alternative Options | Notes |
|-----------|----------------------|---------------------|-------|
| **Fix & Flip** | Full Interior Appraisal | Interior BPO (< $1M) | Must include ARV opinion |
| **Ground-Up Construction** | Full Appraisal | None | Must include land value and completed value |
| **Bridge** | Full Interior Appraisal | Interior BPO (< $1M) | As-is value only |
| **DSCR** | Full Interior Appraisal | CDA (limited scenarios) | Must include rent analysis |

### 8.2.2 Full Interior Appraisal

**Definition:**
A complete appraisal performed by a state-certified appraiser with interior and exterior inspection of the subject property.

**Required Components:**
- Property inspection (interior and exterior)
- Comparable sales analysis (minimum 3 comps)
- Subject property photos (interior and exterior)
- Neighborhood analysis
- Site description and analysis
- Improvements description
- Cost approach (if applicable)
- Sales comparison approach
- Income approach (for DSCR loans)
- Reconciliation of value

**Appraiser Requirements:**
- State-certified residential appraiser
- Licensed in property state
- Errors & omissions insurance
- Independent third party (no relationship to transaction)
- Minimum 3 years experience

### 8.2.3 Interior Broker Price Opinion (BPO)

**Definition:**
A property valuation performed by a licensed real estate broker or agent with interior inspection.

**Eligibility:**
- Loan amount < $1,000,000
- RTL products only (Fix & Flip, Bridge)
- Property condition C3 or better
- Not acceptable for DSCR loans

**Required Components:**
- Property inspection (interior and exterior)
- Comparable sales analysis (minimum 3 comps)
- Property photos (interior and exterior)
- Market analysis
- Condition assessment
- Value opinion (as-is and ARV if applicable)

**Agent Requirements:**
- Licensed real estate agent or broker
- Licensed in property state
- Minimum 3 years experience
- Independent third party

### 8.2.4 Collateral Desktop Analysis (CDA)

**Definition:**
A limited appraisal without interior inspection, using public records and exterior observation.

**Eligibility (DSCR Only):**
- Loan amount < $750,000
- Rate & term refinance only (no cash-out)
- LTV ≤ 70%
- Property condition C3 or better (based on exterior)
- No recent renovations
- Borrower FICO ≥ 720

**Required Components:**
- Exterior property inspection
- Public records review
- Comparable sales analysis
- Exterior photos
- Value opinion
- Rent analysis (for DSCR)

**Limitations:**
- Cannot be used for purchase transactions
- Cannot be used for cash-out refinances
- Cannot be used if property condition uncertain
- Cannot be used for properties > $750,000

---

## 8.3 General Appraisal Review Standards

### 8.3.1 Appraisal Currency Requirements

**Maximum Age:**
- 120 days from note date (closing date)
- No exceptions to 120-day rule

**Recency Validation:**
```
Report Date: Date appraisal was completed
Note Date: Loan closing date
Age = Note Date - Report Date

If Age > 120 days: New appraisal required
If Age 91-120 days: Acceptable but aging (flag for monitoring)
If Age ≤ 90 days: Current and acceptable
```

**Update Requirements:**
- If appraisal expires during processing, new appraisal required
- Updates or recertifications not acceptable
- Market conditions addendum may be required if significant market changes

### 8.3.2 Appraiser Licensing Validation

**Required Licensing:**

| Appraisal Type | Required License | Verification |
|----------------|-----------------|--------------|
| **Full Appraisal** | State Certified Residential Appraiser | State licensing board |
| **Full Appraisal (Complex)** | State Certified General Appraiser | State licensing board |
| **BPO** | Licensed Real Estate Agent/Broker | State real estate commission |
| **CDA** | State Certified Residential Appraiser | State licensing board |

**Verification Process:**
1. Verify appraiser name matches report
2. Verify license number provided
3. Check license status with state board
4. Confirm license is active and current
5. Verify license is valid in property state
6. Check for disciplinary actions

**Red Flags:**
- License expired or inactive
- License not valid in property state
- Appraiser has disciplinary actions
- License number not provided
- Appraiser name doesn't match license

### 8.3.3 Property Identification Verification

**Required Matches:**

| Element | Source | Must Match |
|---------|--------|------------|
| **Address** | Appraisal vs. Application | Exact match |
| **Legal Description** | Appraisal vs. Title | Exact match |
| **APN/Parcel Number** | Appraisal vs. Tax Records | Exact match |
| **Property Type** | Appraisal vs. Application | Consistent |
| **Unit Count** | Appraisal vs. Application | Exact match |

**Verification Process:**
```
Step 1: Compare appraisal address to loan application
Step 2: Verify legal description matches title report
Step 3: Confirm APN matches tax records
Step 4: Validate property type consistency
Step 5: Verify unit count (for multi-unit properties)
```

**Discrepancy Resolution:**
- Minor discrepancies (e.g., "Street" vs. "St."): Acceptable with notation
- Major discrepancies: Requires clarification or new appraisal
- Wrong property appraised: New appraisal required

### 8.3.4 Subject Property Photos

**Required Photos:**

**Exterior Photos:**
- Front view (street view)
- Rear view
- Left side view
- Right side view
- Street scene
- Garage/parking
- Any outbuildings

**Interior Photos:**
- Kitchen
- All bathrooms
- Living room
- Dining room
- All bedrooms
- Basement (if applicable)
- Attic (if accessible)
- Any unique features

**Photo Quality Standards:**
- Clear and in focus
- Adequate lighting
- Shows condition accurately
- Recent (taken during inspection)
- Color (not black and white)
- Properly oriented (not sideways)

**Photo Red Flags:**
- Photos missing or incomplete
- Photos unclear or poor quality
- Photos don't match property description
- Photos appear outdated
- Photos show different property
- No interior photos (for full appraisal)

### 8.3.5 Condition Rating Validation

**Condition Rating Scale:**

| Rating | Description | Acceptable for Lending |
|--------|-------------|----------------------|
| **C1** | New construction, never occupied | Yes (all products) |
| **C2** | Recently renovated, excellent condition | Yes (all products) |
| **C3** | Well maintained, good condition | Yes (all products) |
| **C4** | Adequately maintained, average condition | Yes (all products) |
| **C5** | Poorly maintained, deferred maintenance | RTL only |
| **C6** | Substantial renovation needed, uninhabitable | Limited eligibility |

**Condition Assessment Review:**
- Verify condition rating matches photo evidence
- Confirm condition rating matches property description
- Check for health/safety issues noted
- Review deferred maintenance items
- Validate condition supports value opinion

**Condition Red Flags:**
- Condition rating inconsistent with photos
- Health/safety hazards noted (mold, structural damage)
- Significant deferred maintenance
- Condition C5-C6 for DSCR loan
- Appraiser notes concerns about condition

---

## 8.4 RTL-Specific Appraisal Review

### 8.4.1 As-Is Value Analysis (RTL)

For RTL loans, the as-is value represents the property's current market value in its existing condition.

**As-Is Value Review Checklist:**

- [ ] Comparable sales are truly comparable (similar condition)
- [ ] Comps are distressed/as-is sales (not renovated)
- [ ] Comps sold within 6 months (12 months maximum)
- [ ] Comps within 1 mile of subject (closer preferred)
- [ ] Adjustments are reasonable and documented
- [ ] Value reconciliation is logical
- [ ] Value supported by multiple approaches (if applicable)

**As-Is Comparable Selection Criteria:**

| Criteria | Standard | Red Flag |
|----------|----------|----------|
| **Condition** | Similar to subject (C4-C5) | Renovated properties used |
| **Sale Date** | Within 6 months | > 12 months old |
| **Proximity** | Within 1 mile | > 2 miles |
| **Size** | Within 20% of subject | > 30% difference |
| **Adjustments** | < 20% per comp | > 30% per comp |

**As-Is Value Validation:**

```
Step 1: Review comparable sales grid
Step 2: Verify comps are similar condition to subject
Step 3: Check sale dates (recency)
Step 4: Validate proximity to subject
Step 5: Review adjustments for reasonableness
Step 6: Compare value to subject's condition
Step 7: Cross-check with tax assessed value (if available)
```

**As-Is Value Red Flags:**
- Comps are renovated properties (should be as-is condition)
- Large adjustments required (> 25% per comp)
- Wide value range among comps
- Value significantly above/below tax assessed value
- Appraiser notes limited comparable data
- Value seems high for condition

### 8.4.2 After-Repair Value (ARV) Analysis (RTL)

For Fix & Flip and Ground-Up Construction loans, ARV represents the estimated value after completion of renovations.

**ARV Review Checklist:**

- [ ] Scope of work reviewed by appraiser
- [ ] Comparable sales are renovated properties
- [ ] Comps reflect similar quality/finishes as planned
- [ ] Comps sold within 6 months
- [ ] Comps within 1 mile of subject
- [ ] ARV supported by market data
- [ ] ARV reasonable for neighborhood
- [ ] ARV aligns with scope of work budget

**ARV Comparable Selection Criteria:**

| Criteria | Standard | Red Flag |
|----------|----------|----------|
| **Condition** | Renovated/updated (C2-C3) | Distressed properties |
| **Sale Date** | Within 6 months | > 12 months old |
| **Proximity** | Within 1 mile | > 2 miles |
| **Quality** | Similar to planned finishes | Significantly different |
| **Size** | Within 10% of subject | > 20% difference |

**ARV Validation Process:**

```
Step 1: Review scope of work provided to appraiser
Step 2: Verify comps are renovated properties
Step 3: Compare comp finishes to planned finishes
Step 4: Check comp sale dates and proximity
Step 5: Review adjustments for reasonableness
Step 6: Validate ARV is achievable for neighborhood
Step 7: Compare ARV to highest sales in area
Step 8: Assess over-improvement risk
```

**ARV Per Square Foot Analysis:**

```
ARV per Sq Ft = ARV / Gross Living Area

Compare to:
- Comp average per sq ft
- Neighborhood high per sq ft
- Market average per sq ft

Example:
Subject ARV: $450,000
Subject GLA: 2,200 sq ft
ARV per Sq Ft: $205

Comp Average: $195/sq ft
Neighborhood High: $225/sq ft
Assessment: ARV reasonable, within market range
```

**Over-Improvement Risk Assessment:**

Over-improvement occurs when the ARV significantly exceeds neighborhood norms, limiting resale potential.

| ARV vs. Neighborhood | Risk Level | Action |
|---------------------|------------|--------|
| Within 10% of high | Low | Acceptable |
| 10-20% above high | Moderate | Document justification |
| > 20% above high | High | Reduce ARV or decline |

**ARV Red Flags:**
- ARV significantly exceeds neighborhood values (> 20%)
- Limited comparable sales at ARV level
- Comps are outliers or unique properties
- Scope of work doesn't support ARV
- Appraiser expresses concerns about achievability
- Market trending downward

### 8.4.3 Heavy Rehab Considerations (RTL)

For heavy rehab projects, additional scrutiny is required.

**Heavy Rehab Appraisal Requirements:**
- Detailed scope of work must be provided to appraiser
- Appraiser must review feasibility study (if available)
- ARV must be subject-to-completion of described work
- Appraiser should comment on reasonableness of scope
- Photos should document current condition thoroughly

**Heavy Rehab Review Focus:**
- Verify scope of work aligns with condition
- Confirm ARV reflects scope quality
- Validate budget supports ARV quality level
- Assess timeline reasonableness
- Review market absorption for ARV level

### 8.4.4 Ground-Up Construction Appraisal Review (RTL)

Ground-up construction appraisals require both land value and completed value opinions.

**Required Components:**
- Land value (as vacant land)
- Completed value (subject-to-completion)
- Construction plans review
- Cost approach analysis
- Market analysis for completed value

**Land Value Review:**

```
Land Value Validation:

1. Recent Purchase (if < 6 months):
   - Use purchase price
   - Verify with HUD-1
   - Confirm arm's length transaction

2. Comparable Land Sales:
   - Minimum 3 land sales
   - Similar size and location
   - Utilities available/not available
   - Zoning consistent

3. Extraction Method:
   - From recent new construction sales
   - Subtract improvement value
   - Results in land value
```

**Completed Value Review:**

```
Completed Value Validation:

1. Plans Review:
   - Verify appraiser reviewed plans
   - Confirm square footage matches plans
   - Validate bedroom/bath count

2. Comparable New Construction:
   - Recent new construction sales
   - Similar size and quality
   - Same neighborhood or comparable area
   - Similar finishes and features

3. Cost Approach:
   - Reproduction/replacement cost
   - Plus land value
   - Less depreciation
   - Should support sales comparison value
```

**Ground-Up Construction Red Flags:**
- Land value not supported
- Completed value not achievable for area
- Plans not reviewed by appraiser
- No new construction comparables
- Cost approach significantly different from sales approach
- Over-improvement for neighborhood

---

## 8.5 DSCR-Specific Appraisal Review

### 8.5.1 Market Value Analysis (DSCR)

For DSCR loans, market value represents the property's value in current condition.

**DSCR Value Review Checklist:**

- [ ] Comparable sales are similar condition (C2-C4)
- [ ] Comps are arms-length sales (not distressed)
- [ ] Comps sold within 6 months
- [ ] Comps within 1 mile of subject
- [ ] Property type matches (SFR, condo, multi-unit)
- [ ] Unit count matches (for multi-unit)
- [ ] Adjustments reasonable and documented
- [ ] Value supported by market data

**DSCR Comparable Selection Criteria:**

| Criteria | Standard | Red Flag |
|----------|----------|----------|
| **Condition** | Similar to subject (C2-C4) | Distressed or significantly different |
| **Sale Type** | Arms-length | Foreclosure, REO, short sale |
| **Sale Date** | Within 6 months | > 12 months old |
| **Proximity** | Within 1 mile | > 2 miles |
| **Property Type** | Exact match | Different type |
| **Unit Count** | Exact match (multi-unit) | Different unit count |

**DSCR Value Validation:**

```
Step 1: Review comparable sales grid
Step 2: Verify comps are arms-length transactions
Step 3: Check comp condition matches subject
Step 4: Validate sale dates and proximity
Step 5: Review adjustments for reasonableness
Step 6: Compare value to tax assessed value
Step 7: Cross-check with recent refinance appraisals (if available)
Step 8: Validate value supports requested loan amount
```

**DSCR Value Red Flags:**
- Comps include distressed sales
- Comps significantly different condition
- Large adjustments required (> 20% per comp)
- Value significantly different from recent appraisal
- Value not supported by market data
- Declining market indicators

### 8.5.2 Rental Income Analysis (DSCR)

DSCR appraisals must include rental income analysis to support DSCR calculations.

**Required Rental Analysis Components:**

1. **Market Rent Opinion**
   - Appraiser's opinion of market rent
   - Based on comparable rentals
   - Minimum 3 rental comps
   - Adjustments documented

2. **Comparable Rental Analysis**
   - Recent rentals (within 6 months)
   - Similar property type and size
   - Same neighborhood or comparable area
   - Similar condition and features

3. **Rent Reasonableness**
   - Rent-to-value ratio
   - Comparison to market norms
   - Validation of in-place rent (if leased)

**Rental Comparable Selection Criteria:**

| Criteria | Standard | Red Flag |
|----------|----------|----------|
| **Lease Date** | Within 6 months | > 12 months old |
| **Proximity** | Within 1 mile | > 2 miles |
| **Property Type** | Exact match | Different type |
| **Size** | Within 20% | > 30% difference |
| **Condition** | Similar | Significantly different |
| **Features** | Similar (bed/bath/garage) | Major differences |

**Market Rent Validation:**

```
Market Rent Analysis:

1. Review Rental Comps:
   - Minimum 3 comps required
   - Check lease dates (recency)
   - Verify proximity to subject
   - Compare features (bed/bath/garage/sqft)

2. Calculate Rent per Sq Ft:
   - Subject Market Rent / GLA = Rent per Sq Ft
   - Compare to comp average
   - Should be within 10% of comp average

3. Rent-to-Value Ratio:
   - Monthly Rent / Property Value = Rent Ratio
   - Typical range: 0.5% - 1.0%
   - Higher in lower-value markets
   - Lower in higher-value markets

Example:
Property Value: $400,000
Market Rent: $2,500/month
Rent-to-Value Ratio: $2,500 / $400,000 = 0.625%
Assessment: Reasonable ratio for market
```

**In-Place Rent Validation (Leased Properties):**

If property is currently leased, validate in-place rent:

```
In-Place Rent Review:

1. Obtain lease agreement
2. Verify monthly rent amount
3. Confirm lease term and expiration
4. Check for rent escalations
5. Compare to market rent
6. Validate arm's length lease

Qualifying Rent = MIN(In-place rent, 105% Market rent)

Example:
In-Place Rent: $2,600/month
Market Rent: $2,500/month
105% Market Rent: $2,625/month
Qualifying Rent: $2,600/month (lesser of two)
```

**Rental Analysis Red Flags:**
- Fewer than 3 rental comps
- Rental comps outdated (> 12 months)
- Market rent not supported by comps
- In-place rent significantly above market (> 10%)
- Rent-to-value ratio outside normal range
- Appraiser expresses concerns about rent achievability

### 8.5.3 Multi-Unit Property Considerations (DSCR)

For 2-9 unit properties, additional analysis is required.

**Multi-Unit Appraisal Requirements:**

1. **Unit-by-Unit Analysis**
   - Separate rent analysis for each unit
   - Unit mix (studio/1BR/2BR/3BR)
   - Condition of each unit
   - Occupancy status of each unit

2. **Income Approach**
   - Gross scheduled income
   - Vacancy & collection loss
   - Operating expenses
   - Net operating income (NOI)
   - Capitalization rate analysis

3. **Rent Roll Review (if applicable)**
   - Current lease status for each unit
   - Rent amounts and lease terms
   - Security deposits
   - Tenant payment history

**Multi-Unit Rent Analysis:**

```
Multi-Unit Rent Validation:

Property: 4-unit building

Unit 1 (2BR/1BA): Market Rent $1,200
Unit 2 (2BR/1BA): Market Rent $1,200
Unit 3 (1BR/1BA): Market Rent $950
Unit 4 (1BR/1BA): Market Rent $950

Total Market Rent: $4,300/month

Verify each unit rent with comparable rentals
Aggregate for total property rent
Use for DSCR calculation
```

**5-9 Unit Special Requirements:**

For 5-9 unit properties, enhanced analysis required:
- Net Cash Flow (NCF) DSCR calculation
- Operating expense analysis
- Operating expense ratio validation
- Rent roll required (if occupied)
- Income/expense statement (if available)
- Higher DSCR minimum (1.20x)

### 8.5.4 Short-Term Rental (STR) Properties (DSCR)

Short-term rental properties require special analysis.

**STR Appraisal Requirements:**

1. **Market Rent Analysis**
   - Traditional long-term market rent
   - Based on comparable long-term rentals
   - Used as baseline for DSCR

2. **STR Income Analysis**
   - 12-month STR income history
   - Platform data (Airbnb, VRBO)
   - Occupancy rates
   - Average daily rate (ADR)
   - Seasonal variations

3. **STR Feasibility**
   - Zoning allows STR
   - HOA allows STR (if applicable)
   - Licensing requirements met
   - Market demand for STR

**STR Qualifying Rent Calculation:**

```
STR Qualifying Rent = MIN(
    125% of Long-Term Market Rent,
    12-Month Average STR Income
)

Example:
Long-Term Market Rent: $2,000/month
125% of Market Rent: $2,500/month
12-Month Avg STR Income: $3,200/month
Qualifying Rent: $2,500/month (lesser of two)

Note: Additional -5% LTV adjustment for STR properties
```

**STR Red Flags:**
- No STR income history
- STR income not verified
- Zoning prohibits STR
- HOA prohibits STR
- Declining STR market indicators
- High seasonality without sufficient annual income

---

## 8.6 Comparable Sales Analysis

### 8.6.1 Comparable Selection Standards

**Proximity Requirements:**

| Priority | Distance | Notes |
|----------|----------|-------|
| **Preferred** | Within 0.5 mile | Same neighborhood |
| **Acceptable** | Within 1 mile | Similar neighborhood |
| **Conditional** | 1-2 miles | Must justify, similar characteristics |
| **Not Acceptable** | > 2 miles | Unless rural area with limited data |

**Recency Requirements:**

| Priority | Age | Notes |
|----------|-----|-------|
| **Preferred** | Within 3 months | Most current data |
| **Acceptable** | Within 6 months | Standard |
| **Conditional** | 6-12 months | Must adjust for market trends |
| **Not Acceptable** | > 12 months | Unless no recent sales available |

**Similarity Requirements:**

| Characteristic | Acceptable Variance | Red Flag |
|----------------|-------------------|----------|
| **Square Footage** | Within 20% | > 30% |
| **Bedrooms** | Within 1 | > 1 difference |
| **Bathrooms** | Within 1 | > 1 difference |
| **Age** | Within 20 years | > 40 years |
| **Condition** | Within 1 rating | > 2 ratings |
| **Lot Size** | Within 50% | > 100% |

### 8.6.2 Adjustment Analysis

**Typical Adjustment Ranges:**

| Adjustment Type | Typical Range | Notes |
|-----------------|---------------|-------|
| **Square Footage** | $50-$150/sq ft | Market-dependent |
| **Bedroom** | $10,000-$25,000 | Per bedroom |
| **Bathroom** | $15,000-$30,000 | Full bath |
| **Half Bath** | $5,000-$10,000 | Per half bath |
| **Garage** | $10,000-$40,000 | Based on size |
| **Pool** | $10,000-$30,000 | Market-dependent |
| **Condition** | 5-15% | Based on difference |
| **Location** | 5-20% | Neighborhood quality |

**Adjustment Reasonableness:**

```
Adjustment Analysis:

1. Calculate Total Adjustments per Comp:
   - Sum of all adjustments (absolute value)
   - Divide by comp sale price
   - Result = Adjustment Percentage

2. Acceptable Adjustment Ranges:
   - < 15% per comp: Excellent
   - 15-20% per comp: Acceptable
   - 20-25% per comp: Acceptable with review
   - > 25% per comp: Questionable comparability

3. Net Adjustment:
   - Sum of positive and negative adjustments
   - Should be relatively small
   - Large net adjustment indicates poor comp selection

Example:
Comp Sale Price: $400,000
Adjustments:
  + Size: +$15,000
  + Bedroom: +$20,000
  - Garage: -$10,000
  - Condition: -$20,000
Total Adjustments: $65,000
Adjustment %: $65,000 / $400,000 = 16.25% → ACCEPTABLE
Net Adjustment: +$5,000 (1.25%) → GOOD
```

**Adjustment Red Flags:**
- Total adjustments > 25% per comp
- Large net adjustments (> 15%)
- Inconsistent adjustments across comps
- Adjustments not supported or explained
- Adjustments outside typical ranges
- Adjustments contradict market data

### 8.6.3 Value Reconciliation Review

**Reconciliation Process:**

The appraiser must reconcile values from different approaches and comparables to arrive at final value opinion.

**Reconciliation Review Checklist:**

- [ ] Appraiser explains weight given to each approach
- [ ] Rationale for final value is clear
- [ ] Final value within range of adjusted comps
- [ ] Reconciliation considers all relevant factors
- [ ] Reconciliation is logical and well-supported

**Value Range Analysis:**

```
Value Range Validation:

1. Calculate Adjusted Value for Each Comp:
   - Comp Sale Price + Total Adjustments = Adjusted Value

2. Determine Value Range:
   - Low = Lowest adjusted comp value
   - High = Highest adjusted comp value
   - Range = High - Low

3. Validate Final Value:
   - Should be within comp range
   - Typically near middle of range
   - If outside range, requires explanation

Example:
Comp 1 Adjusted: $435,000
Comp 2 Adjusted: $450,000
Comp 3 Adjusted: $445,000
Range: $435,000 - $450,000
Final Value: $445,000 → Within range, ACCEPTABLE
```

**Reconciliation Red Flags:**
- Final value outside adjusted comp range
- No explanation for value selection
- Heavy weight on weakest comp
- Inconsistent with market data
- Appears to "hit the number" (match contract price)

---

## 8.7 Value Variance Handling

### 8.7.1 Acceptable Variance Thresholds

Value variance is the difference between the appraised value and another value indicator (contract price, borrower estimate, previous appraisal).

**Variance Thresholds:**

| Variance | Status | Action Required |
|----------|--------|-----------------|
| **≤ 5%** | Acceptable | No action |
| **5-10%** | Review Required | Document and explain |
| **10-15%** | Significant | Underwriter review, may resize |
| **> 15%** | Excessive | Resize loan or obtain ROV |

**Variance Calculation:**

```
Variance % = |Appraised Value - Comparison Value| / Comparison Value × 100

Example 1: Purchase Transaction
Contract Price: $400,000
Appraised Value: $385,000
Variance: |$385K - $400K| / $400K = 3.75% → ACCEPTABLE

Example 2: Refinance
Borrower Estimate: $500,000
Appraised Value: $450,000
Variance: |$450K - $500K| / $500K = 10% → SIGNIFICANT, REVIEW REQUIRED

Example 3: Previous Appraisal
Prior Appraisal (6 months ago): $425,000
Current Appraisal: $380,000
Variance: |$380K - $425K| / $425K = 10.6% → SIGNIFICANT, INVESTIGATE
```

### 8.7.2 Variance Investigation

When variance exceeds 5%, investigation is required.

**Investigation Steps:**

```
Step 1: Review Appraisal Quality
- Check comparable selection
- Review adjustments
- Validate appraiser qualifications
- Look for errors or omissions

Step 2: Compare to Market Data
- Research recent sales in area
- Check current listings
- Review market trends
- Validate value is reasonable

Step 3: Identify Variance Cause
- Market conditions changed
- Property condition different than expected
- Borrower estimate unrealistic
- Appraisal quality issues
- Contract price inflated

Step 4: Determine Action
- Accept appraisal and resize loan
- Request appraisal review/revision
- Order Reconsideration of Value (ROV)
- Order second appraisal
- Decline loan if value insufficient
```

**Common Variance Causes:**

| Cause | Typical Scenario | Resolution |
|-------|-----------------|------------|
| **Market Decline** | Values dropping in area | Accept lower value |
| **Borrower Overestimate** | Borrower not familiar with market | Accept appraisal |
| **Property Condition** | Condition worse than expected | Accept appraisal |
| **Contract Inflation** | Contract price above market | Resize to appraisal |
| **Appraisal Error** | Poor comp selection, errors | Request ROV |
| **Missing Information** | Appraiser unaware of improvements | Provide info, request ROV |

### 8.7.3 Reconsideration of Value (ROV)

A Reconsideration of Value is a formal request for the appraiser to review and potentially revise the appraisal.

**When to Request ROV:**

- Appraisal contains factual errors
- Comparable selection is poor
- Appraiser missed relevant information
- Recent comparable sales not considered
- Property improvements not considered
- Variance > 10% and appraisal quality questionable

**ROV Process:**

```
Step 1: Identify Issues
- Document specific errors or omissions
- Gather supporting evidence
- Identify better comparable sales

Step 2: Prepare ROV Request
- Written request to appraiser
- Specific issues identified
- Supporting documentation attached
- Additional comparable sales (if applicable)

Step 3: Appraiser Review
- Appraiser reviews request
- Appraiser investigates issues
- Appraiser responds with findings

Step 4: Appraiser Response
- Revised appraisal (if errors found)
- Explanation of original value (if no changes)
- Additional analysis or support
```

**ROV Documentation Requirements:**

1. **Factual Errors**
   - Incorrect square footage → Provide tax records, plans
   - Incorrect bedroom/bath count → Provide photos, MLS
   - Incorrect property features → Provide documentation

2. **Better Comparables**
   - More recent sales → Provide MLS data
   - Closer proximity → Provide addresses and data
   - More similar properties → Provide details

3. **Missing Information**
   - Recent renovations → Provide invoices, photos
   - Property improvements → Provide documentation
   - Market data → Provide sales data, market reports

**ROV Outcomes:**

| Outcome | Frequency | Next Steps |
|---------|-----------|------------|
| **Value Increased** | 20-30% | Accept revised appraisal |
| **Value Unchanged** | 50-60% | Accept original or order new appraisal |
| **Partial Increase** | 10-20% | Evaluate if sufficient |
| **Additional Issues Found** | 5-10% | May decrease value further |

**ROV Red Flags:**
- Appraiser defensive or uncooperative
- Appraiser doesn't address issues raised
- Revised appraisal still has errors
- Value change not supported by new analysis
- Multiple ROVs required (quality concern)

### 8.7.4 Second Appraisal

In some cases, a second appraisal may be warranted.

**When to Order Second Appraisal:**

- First appraisal quality is poor
- ROV unsuccessful and variance remains high
- Conflicting information in first appraisal
- Borrower disputes first appraisal with valid concerns
- Loan amount > $2,000,000 (may require two appraisals)

**Second Appraisal Process:**

```
Step 1: Order from Different Appraiser
- Use different appraisal company
- Ensure independence from first appraiser

Step 2: Provide Same Information
- Same scope of work
- Same property access
- Same market data

Step 3: Compare Results
- Review both appraisals
- Identify differences
- Determine which is more credible

Step 4: Value Determination
- If values within 5%: Use average or lower
- If values differ > 5%: Use lower value
- If one clearly superior: Use that value
```

**Second Appraisal Scenarios:**

```
Scenario 1: Values Close
Appraisal 1: $450,000
Appraisal 2: $445,000
Variance: 1.1%
Action: Use average ($447,500) or lower ($445,000)

Scenario 2: Values Different
Appraisal 1: $450,000
Appraisal 2: $420,000
Variance: 6.7%
Action: Review both for quality, use lower ($420,000) if both credible

Scenario 3: One Clearly Better
Appraisal 1: $450,000 (poor comps, high adjustments)
Appraisal 2: $425,000 (excellent comps, low adjustments)
Action: Use second appraisal ($425,000)
```

### 8.7.5 Secondary Valuation Requirements

In certain scenarios, a secondary valuation is required to support the primary appraisal value.

**When Secondary Valuation is Required:**

| Scenario | Requirement | Rationale |
|----------|-------------|-----------|
| Loan amount > $2,000,000 | Required (some investors) | Enhanced due diligence |
| Loan amount > $3,000,000 | Required (all investors) | Significant exposure |
| Suspected value variance > 10% | Required | Value validation |
| Limited comparable data | Required | Market uncertainty |
| Unique or complex property | Required | Special characteristics |
| Declining market conditions | May be required | Market volatility |

**Acceptable Secondary Valuation Types:**

1. **Second Full Appraisal** (most credible)
   - Different appraiser from different company
   - Full interior inspection
   - Complete comparable analysis

2. **Collateral Desktop Analysis (CDA)**
   - Exterior inspection only
   - Public records review
   - Limited comparable analysis

3. **Automated Valuation Model (AVM)**
   - Computer-generated valuation
   - Statistical modeling
   - No physical inspection

4. **Enhanced Desk Review (EDR)**
   - Third-party review of original appraisal
   - Additional market data
   - Value validation

5. **Exterior BPO**
   - Licensed agent/broker
   - Exterior inspection
   - Market analysis

**10% Variance Rule:**

The secondary valuation must be compared to the primary appraisal to determine underwriting value:

**If Variance ≤ 10%:**
- Use primary appraisal value
- Document both values in file
- No further action required

**If Variance > 10%:**
- Use lesser of the two values for underwriting
- Investigate reason for variance
- May require third valuation or ROV
- Consider resizing loan or declining

**Variance Calculation:**

```
Variance % = |Primary Value - Secondary Value| / Primary Value × 100

Example 1: Within 10%
Primary Appraisal: $500,000
Secondary Valuation (CDA): $480,000
Variance: |$500K - $480K| / $500K = 4.0%
Action: Use primary value $500,000 ✓

Example 2: Exceeds 10%
Primary Appraisal: $500,000
Secondary Valuation (CDA): $425,000
Variance: |$500K - $425K| / $500K = 15.0%
Action: Use lesser value $425,000, investigate variance

Example 3: Close to 10%
Primary Appraisal: $500,000
Secondary Valuation (EDR): $455,000
Variance: |$500K - $455K| / $500K = 9.0%
Action: Use primary value $500,000 ✓
```

**Secondary Valuation Process:**

```
Step 1: Determine if secondary valuation required
Step 2: Order appropriate valuation type
Step 3: Review both valuations for quality
Step 4: Calculate variance percentage
Step 5: Apply 10% variance rule
Step 6: Determine underwriting value
Step 7: Document decision in file
```

**Value Reconciliation with Secondary Valuation:**

| Primary Appraisal | Secondary Valuation | Variance | Underwriting Value | Action |
|-------------------|---------------------|----------|-------------------|---------|
| $400,000 | $395,000 | 1.3% | $400,000 | Use primary |
| $400,000 | $380,000 | 5.0% | $400,000 | Use primary |
| $400,000 | $360,000 | 10.0% | $400,000 | Use primary (at threshold) |
| $400,000 | $350,000 | 12.5% | $350,000 | Use lesser, investigate |
| $400,000 | $320,000 | 20.0% | $320,000 | Use lesser, may decline |

**Investigation Required When Variance > 10%:**

1. **Review Both Valuations:**
   - Check comparable selection in both
   - Review adjustments in both
   - Assess quality of analysis

2. **Market Research:**
   - Independent market data review
   - Recent sales verification
   - Current listing analysis

3. **Determine Cause:**
   - Different comparable selection
   - Market conditions changed
   - Property characteristics misunderstood
   - Quality issue in one valuation

4. **Resolution Options:**
   - Accept lower value and resize loan
   - Order third valuation (tie-breaker)
   - Request ROV on primary appraisal
   - Request revision of secondary valuation
   - Decline loan if values cannot be reconciled

**Three-Valuation Scenario:**

If two valuations differ by > 10%, a third valuation may be ordered:

```
Scenario: Large Variance
Primary Appraisal: $500,000
Secondary Valuation: $425,000
Variance: 15%

Order Third Valuation

Third Valuation: $475,000

Value Determination:
- Discard outlier ($425,000 or $500,000)
- Use average of closest two: ($500K + $475K) / 2 = $487,500
- Or use middle value: $475,000
- Underwriter discretion with documentation
```

---

## 8.8 Flag Generation Rules for INSPIRE Phase 7

### 8.8.1 Appraisal Review Flags

| Check | Pass (Green) | Warning (Yellow) | Fail (Red) |
|-------|--------------|------------------|------------|
| **Report Currency** | ≤ 90 days | 91-120 days | > 120 days |
| **Appraiser License** | Valid certified | Valid licensed | Invalid/expired |
| **Property Match** | Exact match | Minor discrepancy | Major discrepancy |
| **Condition Rating** | C1-C3 | C4 | C5-C6 (DSCR) |
| **Interior Photos** | All present | Some missing | Critical missing |
| **Exterior Photos** | All present | Some missing | Critical missing |
| **Comparable Count** | ≥ 6 comps | 3-5 comps | < 3 comps |
| **Comparable Recency** | All ≤ 6 months | Some > 6 months | All > 6 months |
| **Comparable Proximity** | All ≤ 1 mile | Some > 1 mile | All > 1 mile |
| **Adjustments** | < 15% per comp | 15-25% per comp | > 25% per comp |
| **Value Variance** | ≤ 5% | 5-10% | > 10% |

### 8.8.2 RTL-Specific Flags

| Check | Pass (Green) | Warning (Yellow) | Fail (Red) |
|-------|--------------|------------------|------------|
| **As-Is Comps** | Similar condition | Some renovated | All renovated |
| **ARV Provided** | Yes, supported | Yes, limited support | No or unsupported |
| **ARV Comps** | Renovated properties | Mixed condition | As-is properties |
| **Over-Improvement** | ≤ 10% above area | 10-20% above | > 20% above |
| **Scope Review** | Reviewed by appraiser | Not reviewed | Conflicts with value |

### 8.8.3 DSCR-Specific Flags

| Check | Pass (Green) | Warning (Yellow) | Fail (Red) |
|-------|--------------|------------------|------------|
| **Rental Analysis** | Complete with comps | Limited comps | Missing or inadequate |
| **Market Rent** | Supported | Limited support | Unsupported |
| **Rental Comps** | ≥ 3 comps | 1-2 comps | 0 comps |
| **Rent-to-Value** | 0.5-1.0% | 0.4-0.5% or 1.0-1.2% | < 0.4% or > 1.2% |
| **In-Place Rent** | ≤ 105% market | 105-115% market | > 115% market |
| **Multi-Unit Analysis** | Unit-by-unit | Aggregate only | Missing |

---

## 8.9 Python Implementation

### 8.9.1 Appraisal Analysis Module

```python
"""
Appraisal Analysis Module
Analyzes appraisals and generates flags for INSPIRE Phase 7.
"""

from dataclasses import dataclass
from datetime import date, timedelta
from enum import Enum
from typing import List, Optional, Dict, Tuple


class AppraisalType(Enum):
    """Types of appraisals"""
    FULL_INTERIOR = "FULL_INTERIOR"
    INTERIOR_BPO = "INTERIOR_BPO"
    CDA = "CDA"


class PropertyCondition(Enum):
    """Property condition ratings"""
    C1 = "C1"
    C2 = "C2"
    C3 = "C3"
    C4 = "C4"
    C5 = "C5"
    C6 = "C6"


class FlagType(Enum):
    """Flag types"""
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    RED = "RED"


@dataclass
class AnalysisFlag:
    """Analysis flag"""
    flag_type: FlagType
    check_name: str
    message: str
    value: any
    threshold: any = None


@dataclass
class ComparableSale:
    """Comparable sale information"""
    address: str
    sale_date: date
    sale_price: float
    square_footage: int
    distance_miles: float
    adjustments: Dict[str, float]
    adjusted_price: float
    
    @property
    def total_adjustments(self) -> float:
        """Calculate total absolute adjustments"""
        return sum(abs(v) for v in self.adjustments.values())
    
    @property
    def adjustment_percentage(self) -> float:
        """Calculate adjustment percentage"""
        return self.total_adjustments / self.sale_price if self.sale_price > 0 else 0
    
    @property
    def net_adjustment(self) -> float:
        """Calculate net adjustment"""
        return sum(self.adjustments.values())
    
    @property
    def age_days(self) -> int:
        """Calculate age of sale in days"""
        return (date.today() - self.sale_date).days


@dataclass
class RentalComparable:
    """Comparable rental information"""
    address: str
    lease_date: date
    monthly_rent: float
    square_footage: int
    bedrooms: int
    bathrooms: float
    distance_miles: float
    
    @property
    def rent_per_sqft(self) -> float:
        """Calculate rent per square foot"""
        return self.monthly_rent / self.square_footage if self.square_footage > 0 else 0
    
    @property
    def age_days(self) -> int:
        """Calculate age of lease in days"""
        return (date.today() - self.lease_date).days


@dataclass
class Appraisal:
    """Appraisal report information"""
    report_date: date
    appraisal_type: AppraisalType
    appraiser_name: str
    appraiser_license: str
    property_address: str
    square_footage: int
    condition: PropertyCondition
    as_is_value: Optional[float] = None
    arv: Optional[float] = None
    market_rent: Optional[float] = None
    comparable_sales: List[ComparableSale] = None
    rental_comparables: List[RentalComparable] = None
    has_interior_photos: bool = True
    has_exterior_photos: bool = True
    
    def __post_init__(self):
        if self.comparable_sales is None:
            self.comparable_sales = []
        if self.rental_comparables is None:
            self.rental_comparables = []
    
    @property
    def age_days(self) -> int:
        """Calculate appraisal age in days"""
        return (date.today() - self.report_date).days
    
    @property
    def value_per_sqft(self) -> float:
        """Calculate value per square foot"""
        value = self.arv if self.arv else self.as_is_value
        return value / self.square_footage if value and self.square_footage > 0 else 0
    
    @property
    def rent_to_value_ratio(self) -> Optional[float]:
        """Calculate rent-to-value ratio"""
        if self.market_rent and self.as_is_value:
            return self.market_rent / self.as_is_value
        return None


class AppraisalAnalyzer:
    """
    Analyze appraisals and generate flags for INSPIRE Phase 7.
    """
    
    # Currency thresholds
    CURRENCY_PREFERRED = 90  # days
    CURRENCY_MAXIMUM = 120  # days
    
    # Comparable thresholds
    MIN_COMPS = 3
    PREFERRED_COMPS = 6
    MAX_COMP_AGE_DAYS = 180  # 6 months
    MAX_COMP_DISTANCE = 1.0  # miles
    
    # Adjustment thresholds
    ADJUSTMENT_EXCELLENT = 0.15  # 15%
    ADJUSTMENT_ACCEPTABLE = 0.20  # 20%
    ADJUSTMENT_HIGH = 0.25  # 25%
    
    # Variance thresholds
    VARIANCE_ACCEPTABLE = 0.05  # 5%
    VARIANCE_REVIEW = 0.10  # 10%
    VARIANCE_SIGNIFICANT = 0.15  # 15%
    
    # Rent-to-value thresholds
    RENT_TO_VALUE_MIN = 0.004  # 0.4%
    RENT_TO_VALUE_LOW = 0.005  # 0.5%
    RENT_TO_VALUE_HIGH = 0.010  # 1.0%
    RENT_TO_VALUE_MAX = 0.012  # 1.2%
    
    def check_currency(self, appraisal: Appraisal, note_date: date) -> AnalysisFlag:
        """
        Check appraisal currency.
        
        Args:
            appraisal: Appraisal to check
            note_date: Loan closing date
            
        Returns:
            AnalysisFlag with currency status
        """
        age_days = (note_date - appraisal.report_date).days
        
        if age_days <= self.CURRENCY_PREFERRED:
            return AnalysisFlag(
                flag_type=FlagType.GREEN,
                check_name="Report Currency",
                message=f"Report is {age_days} days old (within {self.CURRENCY_PREFERRED} days)",
                value=age_days,
                threshold=self.CURRENCY_PREFERRED
            )
        elif age_days <= self.CURRENCY_MAXIMUM:
            return AnalysisFlag(
                flag_type=FlagType.YELLOW,
                check_name="Report Currency",
                message=f"Report is {age_days} days old (acceptable but aging)",
                value=age_days,
                threshold=self.CURRENCY_MAXIMUM
            )
        else:
            return AnalysisFlag(
                flag_type=FlagType.RED,
                check_name="Report Currency",
                message=f"Report is {age_days} days old (exceeds {self.CURRENCY_MAXIMUM}-day maximum)",
                value=age_days,
                threshold=self.CURRENCY_MAXIMUM
            )
    
    def check_condition(self, appraisal: Appraisal, loan_type: str) -> AnalysisFlag:
        """
        Check property condition rating.
        
        Args:
            appraisal: Appraisal with condition rating
            loan_type: 'RTL' or 'DSCR'
            
        Returns:
            AnalysisFlag with condition assessment
        """
        condition = appraisal.condition
        
        if condition in [PropertyCondition.C1, PropertyCondition.C2, PropertyCondition.C3]:
            return AnalysisFlag(
                flag_type=FlagType.GREEN,
                check_name="Property Condition",
                message=f"Condition {condition.value} (excellent to good)",
                value=condition.value
            )
        elif condition == PropertyCondition.C4:
            return AnalysisFlag(
                flag_type=FlagType.YELLOW,
                check_name="Property Condition",
                message=f"Condition {condition.value} (average, acceptable)",
                value=condition.value
            )
        else:  # C5 or C6
            if loan_type == 'RTL':
                return AnalysisFlag(
                    flag_type=FlagType.YELLOW,
                    check_name="Property Condition",
                    message=f"Condition {condition.value} (poor, RTL acceptable)",
                    value=condition.value
                )
            else:  # DSCR
                return AnalysisFlag(
                    flag_type=FlagType.RED,
                    check_name="Property Condition",
                    message=f"Condition {condition.value} (not acceptable for DSCR)",
                    value=condition.value
                )
    
    def check_photos(self, appraisal: Appraisal) -> List[AnalysisFlag]:
        """
        Check for required photos.
        
        Args:
            appraisal: Appraisal to check
            
        Returns:
            List of AnalysisFlags for photo checks
        """
        flags = []
        
        if appraisal.has_interior_photos and appraisal.has_exterior_photos:
            flags.append(AnalysisFlag(
                flag_type=FlagType.GREEN,
                check_name="Property Photos",
                message="Interior and exterior photos present",
                value="Complete"
            ))
        elif appraisal.has_interior_photos or appraisal.has_exterior_photos:
            missing = "exterior" if appraisal.has_interior_photos else "interior"
            flags.append(AnalysisFlag(
                flag_type=FlagType.YELLOW,
                check_name="Property Photos",
                message=f"Missing {missing} photos",
                value="Incomplete"
            ))
        else:
            flags.append(AnalysisFlag(
                flag_type=FlagType.RED,
                check_name="Property Photos",
                message="Missing interior and exterior photos",
                value="Missing"
            ))
        
        return flags
    
    def check_comparable_count(self, appraisal: Appraisal) -> AnalysisFlag:
        """
        Check number of comparable sales.
        
        Args:
            appraisal: Appraisal with comparable sales
            
        Returns:
            AnalysisFlag with comp count assessment
        """
        comp_count = len(appraisal.comparable_sales)
        
        if comp_count >= self.PREFERRED_COMPS:
            return AnalysisFlag(
                flag_type=FlagType.GREEN,
                check_name="Comparable Count",
                message=f"{comp_count} comparable sales (excellent)",
                value=comp_count,
                threshold=self.PREFERRED_COMPS
            )
        elif comp_count >= self.MIN_COMPS:
            return AnalysisFlag(
                flag_type=FlagType.YELLOW,
                check_name="Comparable Count",
                message=f"{comp_count} comparable sales (adequate)",
                value=comp_count,
                threshold=self.MIN_COMPS
            )
        else:
            return AnalysisFlag(
                flag_type=FlagType.RED,
                check_name="Comparable Count",
                message=f"{comp_count} comparable sales (below minimum of {self.MIN_COMPS})",
                value=comp_count,
                threshold=self.MIN_COMPS
            )
    
    def check_comparable_quality(self, appraisal: Appraisal) -> List[AnalysisFlag]:
        """
        Check quality of comparable sales.
        
        Args:
            appraisal: Appraisal with comparable sales
            
        Returns:
            List of AnalysisFlags for comp quality checks
        """
        flags = []
        
        if not appraisal.comparable_sales:
            return flags
        
        # Check recency
        recent_comps = [c for c in appraisal.comparable_sales if c.age_days <= self.MAX_COMP_AGE_DAYS]
        recency_pct = len(recent_comps) / len(appraisal.comparable_sales)
        
        if recency_pct == 1.0:
            flags.append(AnalysisFlag(
                flag_type=FlagType.GREEN,
                check_name="Comparable Recency",
                message=f"All {len(appraisal.comparable_sales)} comps within 6 months",
                value="All recent"
            ))
        elif recency_pct >= 0.5:
            flags.append(AnalysisFlag(
                flag_type=FlagType.YELLOW,
                check_name="Comparable Recency",
                message=f"{len(recent_comps)} of {len(appraisal.comparable_sales)} comps within 6 months",
                value=f"{recency_pct:.0%} recent"
            ))
        else:
            flags.append(AnalysisFlag(
                flag_type=FlagType.RED,
                check_name="Comparable Recency",
                message=f"Only {len(recent_comps)} of {len(appraisal.comparable_sales)} comps within 6 months",
                value=f"{recency_pct:.0%} recent"
            ))
        
        # Check proximity
        close_comps = [c for c in appraisal.comparable_sales if c.distance_miles <= self.MAX_COMP_DISTANCE]
        proximity_pct = len(close_comps) / len(appraisal.comparable_sales)
        
        if proximity_pct == 1.0:
            flags.append(AnalysisFlag(
                flag_type=FlagType.GREEN,
                check_name="Comparable Proximity",
                message=f"All {len(appraisal.comparable_sales)} comps within 1 mile",
                value="All close"
            ))
        elif proximity_pct >= 0.5:
            flags.append(AnalysisFlag(
                flag_type=FlagType.YELLOW,
                check_name="Comparable Proximity",
                message=f"{len(close_comps)} of {len(appraisal.comparable_sales)} comps within 1 mile",
                value=f"{proximity_pct:.0%} close"
            ))
        else:
            flags.append(AnalysisFlag(
                flag_type=FlagType.RED,
                check_name="Comparable Proximity",
                message=f"Only {len(close_comps)} of {len(appraisal.comparable_sales)} comps within 1 mile",
                value=f"{proximity_pct:.0%} close"
            ))
        
        # Check adjustments
        avg_adjustment_pct = sum(c.adjustment_percentage for c in appraisal.comparable_sales) / len(appraisal.comparable_sales)
        
        if avg_adjustment_pct <= self.ADJUSTMENT_EXCELLENT:
            flags.append(AnalysisFlag(
                flag_type=FlagType.GREEN,
                check_name="Comparable Adjustments",
                message=f"Average adjustments {avg_adjustment_pct:.1%} (excellent)",
                value=f"{avg_adjustment_pct:.1%}",
                threshold=f"{self.ADJUSTMENT_EXCELLENT:.0%}"
            ))
        elif avg_adjustment_pct <= self.ADJUSTMENT_ACCEPTABLE:
            flags.append(AnalysisFlag(
                flag_type=FlagType.YELLOW,
                check_name="Comparable Adjustments",
                message=f"Average adjustments {avg_adjustment_pct:.1%} (acceptable)",
                value=f"{avg_adjustment_pct:.1%}",
                threshold=f"{self.ADJUSTMENT_ACCEPTABLE:.0%}"
            ))
        else:
            flags.append(AnalysisFlag(
                flag_type=FlagType.RED,
                check_name="Comparable Adjustments",
                message=f"Average adjustments {avg_adjustment_pct:.1%} (high)",
                value=f"{avg_adjustment_pct:.1%}",
                threshold=f"{self.ADJUSTMENT_HIGH:.0%}"
            ))
        
        return flags
    
    def check_value_variance(
        self,
        appraised_value: float,
        comparison_value: float,
        comparison_type: str
    ) -> AnalysisFlag:
        """
        Check variance between appraised value and comparison value.
        
        Args:
            appraised_value: Value from appraisal
            comparison_value: Contract price, borrower estimate, or previous appraisal
            comparison_type: Description of comparison value
            
        Returns:
            AnalysisFlag with variance assessment
        """
        variance = abs(appraised_value - comparison_value) / comparison_value
        
        if variance <= self.VARIANCE_ACCEPTABLE:
            return AnalysisFlag(
                flag_type=FlagType.GREEN,
                check_name="Value Variance",
                message=f"Variance {variance:.1%} from {comparison_type} (acceptable)",
                value=f"{variance:.1%}",
                threshold=f"{self.VARIANCE_ACCEPTABLE:.0%}"
            )
        elif variance <= self.VARIANCE_REVIEW:
            return AnalysisFlag(
                flag_type=FlagType.YELLOW,
                check_name="Value Variance",
                message=f"Variance {variance:.1%} from {comparison_type} (review required)",
                value=f"{variance:.1%}",
                threshold=f"{self.VARIANCE_REVIEW:.0%}"
            )
        else:
            return AnalysisFlag(
                flag_type=FlagType.RED,
                check_name="Value Variance",
                message=f"Variance {variance:.1%} from {comparison_type} (significant)",
                value=f"{variance:.1%}",
                threshold=f"{self.VARIANCE_SIGNIFICANT:.0%}"
            )
    
    def check_rental_analysis(self, appraisal: Appraisal) -> List[AnalysisFlag]:
        """
        Check rental income analysis for DSCR loans.
        
        Args:
            appraisal: Appraisal with rental analysis
            
        Returns:
            List of AnalysisFlags for rental analysis
        """
        flags = []
        
        # Check if rental analysis present
        if not appraisal.market_rent:
            flags.append(AnalysisFlag(
                flag_type=FlagType.RED,
                check_name="Rental Analysis",
                message="No market rent opinion provided",
                value="Missing"
            ))
            return flags
        
        # Check rental comp count
        rental_comp_count = len(appraisal.rental_comparables)
        
        if rental_comp_count >= self.MIN_COMPS:
            flags.append(AnalysisFlag(
                flag_type=FlagType.GREEN,
                check_name="Rental Comparable Count",
                message=f"{rental_comp_count} rental comps (adequate)",
                value=rental_comp_count,
                threshold=self.MIN_COMPS
            ))
        elif rental_comp_count > 0:
            flags.append(AnalysisFlag(
                flag_type=FlagType.YELLOW,
                check_name="Rental Comparable Count",
                message=f"{rental_comp_count} rental comps (below minimum)",
                value=rental_comp_count,
                threshold=self.MIN_COMPS
            ))
        else:
            flags.append(AnalysisFlag(
                flag_type=FlagType.RED,
                check_name="Rental Comparable Count",
                message="No rental comparables provided",
                value=0,
                threshold=self.MIN_COMPS
            ))
        
        # Check rent-to-value ratio
        if appraisal.rent_to_value_ratio:
            rtv = appraisal.rent_to_value_ratio
            
            if self.RENT_TO_VALUE_LOW <= rtv <= self.RENT_TO_VALUE_HIGH:
                flags.append(AnalysisFlag(
                    flag_type=FlagType.GREEN,
                    check_name="Rent-to-Value Ratio",
                    message=f"Rent-to-value {rtv:.2%} (normal range)",
                    value=f"{rtv:.2%}",
                    threshold=f"{self.RENT_TO_VALUE_LOW:.1%}-{self.RENT_TO_VALUE_HIGH:.1%}"
                ))
            elif self.RENT_TO_VALUE_MIN <= rtv <= self.RENT_TO_VALUE_MAX:
                flags.append(AnalysisFlag(
                    flag_type=FlagType.YELLOW,
                    check_name="Rent-to-Value Ratio",
                    message=f"Rent-to-value {rtv:.2%} (outside normal range but acceptable)",
                    value=f"{rtv:.2%}",
                    threshold=f"{self.RENT_TO_VALUE_LOW:.1%}-{self.RENT_TO_VALUE_HIGH:.1%}"
                ))
            else:
                flags.append(AnalysisFlag(
                    flag_type=FlagType.RED,
                    check_name="Rent-to-Value Ratio",
                    message=f"Rent-to-value {rtv:.2%} (outside acceptable range)",
                    value=f"{rtv:.2%}",
                    threshold=f"{self.RENT_TO_VALUE_MIN:.1%}-{self.RENT_TO_VALUE_MAX:.1%}"
                ))
        
        return flags
    
    def generate_all_flags(
        self,
        appraisal: Appraisal,
        loan_type: str,
        note_date: date,
        comparison_value: Optional[float] = None,
        comparison_type: Optional[str] = None
    ) -> List[AnalysisFlag]:
        """
        Generate all appraisal analysis flags.
        
        Args:
            appraisal: Appraisal to analyze
            loan_type: 'RTL' or 'DSCR'
            note_date: Loan closing date
            comparison_value: Optional comparison value (contract price, etc.)
            comparison_type: Description of comparison value
            
        Returns:
            List of all AnalysisFlags
        """
        flags = []
        
        # Currency check
        flags.append(self.check_currency(appraisal, note_date))
        
        # Condition check
        flags.append(self.check_condition(appraisal, loan_type))
        
        # Photo checks
        flags.extend(self.check_photos(appraisal))
        
        # Comparable count
        flags.append(self.check_comparable_count(appraisal))
        
        # Comparable quality
        flags.extend(self.check_comparable_quality(appraisal))
        
        # Value variance (if comparison provided)
        if comparison_value and comparison_type:
            value = appraisal.arv if appraisal.arv else appraisal.as_is_value
            if value:
                flags.append(self.check_value_variance(value, comparison_value, comparison_type))
        
        # Rental analysis (DSCR only)
        if loan_type == 'DSCR':
            flags.extend(self.check_rental_analysis(appraisal))
        
        return flags


# Example usage
if __name__ == "__main__":
    # Example appraisal
    comps = [
        ComparableSale(
            address="123 Main St",
            sale_date=date(2024, 11, 1),
            sale_price=440000,
            square_footage=2200,
            distance_miles=0.5,
            adjustments={"size": 10000, "condition": -5000, "garage": 15000},
            adjusted_price=460000
        ),
        ComparableSale(
            address="456 Oak Ave",
            sale_date=date(2024, 10, 15),
            sale_price=455000,
            square_footage=2300,
            distance_miles=0.8,
            adjustments={"size": -5000, "lot": 5000},
            adjusted_price=455000
        ),
        ComparableSale(
            address="789 Elm St",
            sale_date=date(2024, 12, 1),
            sale_price=450000,
            square_footage=2250,
            distance_miles=0.3,
            adjustments={"condition": -10000, "garage": 15000},
            adjusted_price=455000
        )
    ]
    
    appraisal = Appraisal(
        report_date=date(2024, 12, 15),
        appraisal_type=AppraisalType.FULL_INTERIOR,
        appraiser_name="John Appraiser",
        appraiser_license="CA-12345",
        property_address="100 Test St",
        square_footage=2200,
        condition=PropertyCondition.C3,
        as_is_value=450000,
        comparable_sales=comps,
        has_interior_photos=True,
        has_exterior_photos=True
    )
    
    # Analyze appraisal
    analyzer = AppraisalAnalyzer()
    flags = analyzer.generate_all_flags(
        appraisal=appraisal,
        loan_type='RTL',
        note_date=date(2025, 1, 15),
        comparison_value=460000,
        comparison_type="contract price"
    )
    
    print("Appraisal Analysis Flags:")
    print("=" * 60)
    for flag in flags:
        print(f"[{flag.flag_type.value}] {flag.check_name}: {flag.message}")
```

---

## 8.10 Cross-References

**Related Sections:**
- **Section 5**: Property Eligibility Standards - Property type and condition requirements
- **Section 6**: RTL Property Analysis - ARV analysis and scope of work validation
- **Section 7**: DSCR Property & Income Analysis - Rental income validation
- **Section 9**: RTL Loan Sizing & Leverage - How appraisal values impact loan sizing
- **Section 10**: DSCR Loan Sizing & Leverage - Property value for LTV calculations
- **Section 14**: Third-Party Report Analysis - Complete appraisal analysis framework

---

*End of Section 8*

