# Section Prompts Master Document
## USDV Capital Underwriting Manual

**Purpose:** This document contains detailed prompts for generating each section of the underwriting manual. Each prompt is designed to be self-contained and can be used in parallel Claude sessions.

**Critical Rules for ALL Sections:**
1. NEVER mention investor names (ArchWest, EastView, Churchill) in the output
2. Use "USDV Guidelines" or "Program Guidelines" instead
3. All content must be investor-agnostic - unified standards only
4. Include Python code with every section where calculations exist
5. Reference source files but synthesize into unified rules

---

# PROMPT: Section 1 - Investment Philosophy & Loan Products

## Model: Haiku

## Objective
Create Section 1 of the USDV Underwriting Manual covering the investment philosophy and all supported loan products. This section provides the foundational context for all subsequent sections.

## Required Source Files
```
C:\Users\evana\inspire\Investor Underwriting Guidelines\Archwest RTL Guidelines.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\Eastview_RTL_Guidelines_v4_1.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\Eastview DSCR Guidelines_v7.2.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\1. Archwest DSCR Guidelines_7.9.25_V1.8.pdf
C:\Users\evana\inspire\_PRDs\inspire-master-prd.md
```

## INSPIRE Integration Points
- Phase 1-2: Loan product selection during Quick App and Full Application
- Phase 3-4: Product-specific sizing logic selection

## Content Requirements

### 1.1 USDV Capital Mission
- Single-family business purpose lending focus
- RTL (renovation transitional loans) and DSCR (permanent financing)
- NOT owner-occupied - business purpose only

### 1.2 Loan Product Definitions

**RTL Products:**
- Fix & Flip: Short-term financing for acquisition + renovation + resale
- Ground-Up Construction (GUC): Financing for new construction
- Bridge: Short-term financing for stabilized or near-stabilized properties

**DSCR Products:**
- DSCR Permanent: Long-term rental property financing based on property cash flow

### 1.3 Loan Parameter Summary Tables

Create comprehensive tables with:
| Parameter | Fix & Flip | GUC | Bridge | DSCR |
- Minimum loan amount
- Maximum loan amount
- Loan term range
- Interest structure (I/O vs Amortizing)
- Rate type (Fixed vs ARM options)
- Minimum FICO
- Minimum experience
- Eligible property types
- Eligible loan purposes

### 1.4 Business Purpose Requirement
- All loans must be for business/investment purposes
- Owner-occupied properties are NOT eligible
- Borrower certification requirements

### 1.5 Python Code

```python
# Create LoanProduct enum and LoanParameters dataclass
# Create function to validate loan request against product parameters
```

## Output Format
- Markdown with clear headers
- Tables for parameter comparisons
- Python code blocks with docstrings
- ~12 pages

## Key Rules
- Do NOT mention BRRRR strategy (excluded product)
- Do NOT reference specific investors
- Focus on unified USDV product offerings

---

# PROMPT: Section 2 - Borrower Eligibility & Classification

## Model: Sonnet

## Objective
Create Section 2 covering all borrower eligibility requirements and the borrower classification system (A+/A/B/C for RTL).

## Required Source Files
```
C:\Users\evana\inspire\Investor Underwriting Guidelines\Archwest RTL Guidelines.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\Eastview_RTL_Guidelines_v4_1.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\Eastview DSCR Guidelines_v7.2.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\1. Archwest DSCR Guidelines_7.9.25_V1.8.pdf
C:\Users\evana\inspire\_PRDs\inspire-phase-3-4-prd.md (Section 3.4.1 Borrower Classification)
```

## INSPIRE Integration Points
- Phase 1-2: Borrower data collection and validation
- Phase 3-4: Classification calculation for sizing

## Content Requirements

### 2.1 Borrower Classification Framework (RTL)

Extract and synthesize the classification logic:

**Credit Decision Score:**
| FICO Range | Score |
|------------|-------|
| >= 700 | 3 |
| 680-699 | 1 |
| < 680 or Foreign National | 0 |

**Verified Experience Score:**
| Experience (36 months) | Score |
|------------------------|-------|
| 10+ deals | 7 |
| 3-9 deals | 5 |
| 0-2 deals | 1 |

**Classification:**
| Total Score | Class |
|-------------|-------|
| >= 7 | A+ |
| 5-6 | A |
| 2-4 | B |
| < 2 | C |

### 2.2 Experience Requirements
- What counts as verified experience
- Documentation requirements (HUD, settlement statements)
- Deals in last 36 months vs lifetime
- First-time investor eligibility

### 2.3 Citizenship & Residency
- US Citizens: Standard requirements
- Permanent Residents: Green card requirements
- Foreign Nationals: Additional requirements, LTV impacts
- ITIN Borrowers: Eligibility rules

### 2.4 Minimum Requirements by Product
| Requirement | RTL | DSCR |
- FICO minimum
- Experience minimum
- Liquidity requirements
- Net worth requirements

### 2.5 Prohibited Borrowers
- OFAC/sanctions list
- Recent fraud convictions
- Active bankruptcy
- Debarred from federal programs

### 2.6 Python Code

```python
class BorrowerClassifier:
    """Calculate borrower classification for RTL loans."""

    def calculate_credit_score_points(self, fico: int, is_foreign_national: bool) -> int:
        pass

    def calculate_experience_points(self, deals_36mo: int) -> int:
        pass

    def get_classification(self, fico: int, deals_36mo: int, is_foreign_national: bool) -> str:
        pass

class BorrowerEligibilityChecker:
    """Validate borrower meets minimum requirements."""
    pass
```

## Output Format
- ~18 pages
- Clear tables for classification logic
- Decision trees for eligibility
- Comprehensive Python implementation

---

# PROMPT: Section 3 - Entity & Guarantor Analysis

## Model: Haiku

## Objective
Create Section 3 covering entity eligibility, ownership structure requirements, and guarantor qualifications.

## Required Source Files
```
C:\Users\evana\inspire\Investor Underwriting Guidelines\Archwest RTL Guidelines.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\Eastview DSCR Guidelines_v7.2.pdf
C:\Users\evana\inspire\_PRDs\inspire-master-prd.md (Section 9.2 Entity Model)
```

## INSPIRE Integration Points
- Phase 1-2: Entity data collection
- Phase 5-6: Entity document checklist

## Content Requirements

### 3.1 Eligible Entity Types
- LLCs (single-member and multi-member)
- Limited Partnerships (LP)
- Corporations (S-Corp, C-Corp)
- Trusts (revocable, irrevocable, land trusts)
- Series LLCs

### 3.2 Ineligible Entity Types
- Sole proprietorships (for certain products)
- General partnerships
- Non-profit organizations
- Government entities

### 3.3 Ownership Structure Requirements
- Minimum ownership percentage for guarantors
- Nested entity structures (entity owns entity)
- Multiple entity scenarios
- Ownership verification documentation

### 3.4 Guarantor Requirements
- Key Principal identification
- Minimum guarantor qualifications
- Multiple guarantor scenarios
- Carve-out guarantee provisions

### 3.5 State Registration
- Property state registration requirements
- Good standing requirements
- Timeline for foreign entity registration

### 3.6 Required Entity Documents
- Articles of Organization/Incorporation
- Operating Agreement/Bylaws
- Certificate of Good Standing (currency requirement)
- EIN Letter / W-9

### 3.7 Python Code

```python
class EntityAnalyzer:
    """Analyze entity structure and guarantor requirements."""

    def validate_entity_type(self, entity_type: str, loan_type: str) -> bool:
        pass

    def analyze_ownership_structure(self, owners: List[Owner]) -> OwnershipAnalysis:
        pass

    def identify_key_principals(self, owners: List[Owner]) -> List[Owner]:
        pass
```

## Output Format
- ~15 pages
- Entity type eligibility matrix
- Ownership structure diagrams
- Document checklist

---

# PROMPT: Section 4 - Credit & Background Evaluation

## Model: Sonnet

## Objective
Create Section 4 covering credit report analysis standards and background check evaluation. This section is critical for INSPIRE Phase 7 AI analysis.

## Required Source Files
```
C:\Users\evana\inspire\Investor Underwriting Guidelines\Archwest RTL Guidelines.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\Eastview_RTL_Guidelines_v4_1.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\Eastview DSCR Guidelines_v7.2.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\1. Archwest DSCR Guidelines_7.9.25_V1.8.pdf
C:\Users\evana\inspire\_PRDs\inspire-phase-7-prd.md (Section 4.3.1 Credit Report Analysis)
```

## INSPIRE Integration Points
- Phase 3-4: FICO for classification and pricing
- Phase 7: Automated credit report analysis and flag generation

## Content Requirements

### 4.1 Credit Report Requirements
- Tri-merge report (Equifax, Experian, TransUnion)
- Report currency (120-day max)
- Middle score determination

### 4.2 FICO Score Tiers
| Product | Minimum FICO | Pricing Impact |
| RTL | 660 | Classification-based |
| DSCR | 680 | LLPA matrix |

### 4.3 Trade Line Requirements
- Minimum total trade lines: 3
- Minimum active trade lines: 1
- Minimum 24-month history: 1 trade line
- Authorized user considerations

### 4.4 Mortgage History Analysis
| Scenario | RTL Standard | DSCR Standard |
- 0x30 in 12 months
- 1x30 in 12 months
- 2x30 in 12 months
- 60+ day lates
- 90+ day lates

### 4.5 Derogatory Credit Events

**Bankruptcy:**
| Chapter | Seasoning Required | Documentation |
| Chapter 7 | 4 years from discharge | Discharge papers |
| Chapter 13 | 2 years from discharge, 4 years from filing | Court documents |

**Foreclosure:**
- Seasoning: 4 years
- Documentation requirements

**Short Sale / DIL:**
- Seasoning requirements
- Documentation

**Judgments:**
- Unpaid > $10K: Not eligible
- Paid judgments: Acceptable
- Payment plan requirements (6 months)

**Liens:**
- Tax liens: Resolution required
- UCC filings: Review for conflicts

**Collections:**
- Threshold amounts
- Payment plan eligibility

### 4.6 Background Check Evaluation

**Criminal History:**
- Financial fraud: Not eligible
- Felony convictions: Review required
- Misdemeanors: Generally acceptable

**Civil Litigation:**
- Active litigation: Not eligible (with property)
- Historical litigation: Case-by-case

**OFAC/AML Screening:**
- Mandatory for all borrowers
- Match = immediate decline

### 4.7 Flag Generation Rules

Create explicit flag rules for INSPIRE:

| Check | Pass (Green) | Warning (Yellow) | Fail (Red) |
|-------|--------------|------------------|------------|
| FICO | >= threshold | N/A | < threshold |
| Trade lines | >= 3 | 2 | < 2 |
| Housing lates | 0x30 | 1x30 | > 1x30 |
| Bankruptcy | > 4 years | N/A | <= 4 years |
| Active judgments | $0 | < $10K | >= $10K |

### 4.8 Python Code

```python
class CreditAnalyzer:
    """Analyze credit reports and generate flags."""

    def extract_scores(self, report: dict) -> CreditScores:
        pass

    def analyze_trade_lines(self, report: dict) -> TradeLineAnalysis:
        pass

    def analyze_mortgage_history(self, report: dict) -> MortgageHistoryAnalysis:
        pass

    def analyze_derogatories(self, report: dict) -> DerogatoryAnalysis:
        pass

    def generate_flags(self, report: dict, loan_type: str) -> List[AnalysisFlag]:
        pass

class BackgroundChecker:
    """Analyze background check results."""

    def check_criminal_history(self, report: dict) -> CriminalAnalysis:
        pass

    def check_civil_litigation(self, report: dict) -> LitigationAnalysis:
        pass

    def check_ofac(self, report: dict) -> OFACResult:
        pass
```

## Output Format
- ~22 pages
- Comprehensive tables for thresholds
- Explicit flag generation rules (for INSPIRE Phase 7)
- Complete Python implementation

---

# PROMPT: Section 5 - Property Eligibility Standards

## Model: Haiku

## Objective
Create Section 5 covering all property eligibility criteria including property types, locations, conditions, and size requirements.

## Required Source Files
```
C:\Users\evana\inspire\Investor Underwriting Guidelines\Archwest RTL Guidelines.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\Eastview_RTL_Guidelines_v4_1.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\Eastview DSCR Guidelines_v7.2.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\EV GUC Guidelines_v1.0.pdf
```

## INSPIRE Integration Points
- Phase 1-2: Property pre-qualification
- Phase 7: Property eligibility validation

## Content Requirements

### 5.1 Eligible Property Types

**Primary Eligible:**
- Single Family Residence (SFR)
- Townhome
- Planned Unit Development (PUD)

**Conditional Eligible:**
- Condominium (Warrantable)
- Condominium (Non-Warrantable) - case by case
- 2-4 Unit Properties
- 5-9 Unit Small Multifamily

### 5.2 Ineligible Property Types
- Manufactured/mobile homes
- Modular homes (on temporary foundation)
- Mixed-use properties
- Commercial properties
- Agricultural/farms
- Houseboats
- Co-ops
- Condotels

### 5.3 Geographic Eligibility
- Eligible states list
- Restricted/ineligible states
- Rural property limitations
- Declining market considerations

### 5.4 Property Condition Standards
| Rating | Description | Eligibility |
| C1 | New construction | Eligible |
| C2 | Recently renovated | Eligible |
| C3 | Well maintained | Eligible |
| C4 | Adequately maintained | Eligible |
| C5 | Poorly maintained | Limited - RTL only |
| C6 | Substantial renovation needed | Not eligible |

### 5.5 Size & Value Requirements
| Property Type | Min Sq Ft | Max Loan | Notes |
| SFR | 600 | $3M | |
| Condo | 500 | $3M | Per unit |
| 2-4 Unit | 400/unit | $3M | |

### 5.6 Acreage Limitations
- Maximum acreage by property type
- Land value limitations
- Agricultural exclusions

### 5.7 Condominium Requirements
- Warrantable vs non-warrantable criteria
- HOA review requirements
- Project approval process

### 5.8 Python Code

```python
class PropertyEligibilityChecker:
    """Check property eligibility against guidelines."""

    def check_property_type(self, property_type: str, loan_type: str) -> EligibilityResult:
        pass

    def check_location(self, state: str, is_rural: bool) -> EligibilityResult:
        pass

    def check_condition(self, condition_rating: str, loan_type: str) -> EligibilityResult:
        pass

    def check_size(self, sq_ft: int, property_type: str) -> EligibilityResult:
        pass

    def full_eligibility_check(self, property: Property, loan_type: str) -> PropertyEligibilityResult:
        pass
```

## Output Format
- ~18 pages
- Eligibility matrices by property type
- State eligibility map/list
- Condition rating criteria

---

# PROMPT: Section 6 - RTL Property Analysis

## Model: Sonnet

## Objective
Create Section 6 covering property analysis specific to RTL loans (Fix & Flip, GUC, Bridge).

## Required Source Files
```
C:\Users\evana\inspire\Investor Underwriting Guidelines\Archwest RTL Guidelines.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\Eastview_RTL_Guidelines_v4_1.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\EV GUC Guidelines_v1.0.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\RTL Program Guidelines (07.09.2025) - CLEAN 1.pdf
```

## INSPIRE Integration Points
- Phase 1-2: RTL property data collection
- Phase 5-6: Feasibility study review
- Phase 7: RTL-specific property analysis

## Content Requirements

### 6.1 Fix & Flip Property Analysis
- As-Is condition assessment criteria
- Scope of work evaluation standards
- ARV analysis and support requirements
- Comp selection criteria

### 6.2 Heavy Rehab Definition
**Definition:**
- Rehab budget > $50,000 AND
- Rehab budget > 100% of purchase price (purchase) OR
- Rehab budget > 100% of as-is value (refinance)

**Impact:**
- Leverage reduction: -5% (Class A/B), -10% (Class C)
- Enhanced documentation requirements

### 6.3 Ground-Up Construction Analysis
- Land valuation standards
- Plans & specifications review criteria
- Construction budget validation
- Permit status requirements
- Timeline reasonableness assessment

### 6.4 Bridge Loan Property Analysis
- Stabilized property standards
- Value-add bridge scenarios
- Occupancy requirements

### 6.5 Feasibility Study Review
- Budget alignment tolerance (±10%)
- Timeline reasonableness criteria
- Contingency requirements (5% minimum)
- GC qualification review

### 6.6 Exit Strategy Validation
| Exit Strategy | Requirements | Timeline |
| Sale | ARV support, market analysis | Within term |
| Refinance (DSCR) | Rent support, DSCR pro forma | Before maturity |
| Refinance (Conventional) | Stabilization evidence | Before maturity |

### 6.7 Python Code

```python
class RTLPropertyAnalyzer:
    """Analyze properties for RTL loans."""

    def is_heavy_rehab(self, rehab_budget: float, purchase_price: float, as_is_value: float, is_purchase: bool) -> bool:
        pass

    def analyze_scope_of_work(self, scope: dict, property: Property) -> ScopeAnalysis:
        pass

    def validate_arv(self, arv: float, comps: List[Comp]) -> ARVValidation:
        pass

    def validate_exit_strategy(self, exit_strategy: str, property: Property, loan: Loan) -> ExitValidation:
        pass
```

## Output Format
- ~20 pages
- Heavy rehab decision tree
- Feasibility review checklist
- Exit strategy validation matrix

---

# PROMPT: Section 7 - DSCR Property & Income Analysis

## Model: Opus

## Objective
Create Section 7 covering DSCR calculation methodology and rental income analysis. This is a critical calculation section.

## Required Source Files
```
C:\Users\evana\inspire\Investor Underwriting Guidelines\Eastview DSCR Guidelines_v7.2.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\1. Archwest DSCR Guidelines_7.9.25_V1.8.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\EV DSCR S Matrix_12.29.25.pdf
C:\Users\evana\inspire\_PRDs\inspire-phase-3-4-prd.md (Section 3.5 DSCR Sizer Logic)
```

## INSPIRE Integration Points
- Phase 3-4: DSCR calculation for sizing
- Phase 7: DSCR validation from appraisal/rent data

## Content Requirements

### 7.1 DSCR Calculation Formula

```
DSCR = Qualifying Monthly Rent / Monthly PITIA

Monthly PITIA Components:
- P&I: Principal & Interest based on loan terms
- T: Annual Property Taxes / 12
- I: Annual Insurance / 12
- A: Monthly HOA/Association Fees
```

### 7.2 Qualifying Rent Determination

| Scenario | Qualifying Rent Formula |
|----------|------------------------|
| Leased (Purchase) | MIN(In-place rent, 100% Market rent) |
| Leased (Refinance) | MIN(In-place rent, 100% Market rent) |
| Unleased (Purchase) | 100% Market rent |
| Unleased (Refinance) | 90% Market rent (+ 5% LTV reduction) |
| Short-Term Rental | MIN(125% Market rent, 12-month average income) |
| Section 8 | Contract rent (with verification) |

### 7.3 Minimum DSCR Requirements

| Scenario | Minimum DSCR |
|----------|--------------|
| FICO >= 700 | 1.00x |
| FICO < 700 | 1.20x |
| 5-9 Units | 1.20x (NCF basis) |
| Foreign National | 1.20x |

### 7.4 Lease Review Standards
- Arm's length requirement (no related party)
- Maximum lease term (3 years)
- No purchase options
- Rent verification methods

### 7.5 Market Rent Validation
- Comparable rent analysis
- Rent-to-value ratios
- Market rent report requirements

### 7.6 Short-Term Rental (STR) Analysis
- Income documentation (12-month history)
- Platform verification (Airbnb, VRBO)
- Seasonal adjustment
- LTV impact (-5%)

### 7.7 Section 8 / Subsidized Housing
- Contract rent verification
- HAP contract review
- LTV impact (-5%)

### 7.8 5-9 Unit Analysis
- Net Cash Flow (NCF) DSCR basis
- Operating expense analysis
- Rent roll requirements

### 7.9 Python Code

```python
class DSCRCalculator:
    """Calculate DSCR for loan sizing and validation."""

    def calculate_monthly_pi(self, loan_amount: float, rate: float, term_months: int, io_months: int = 0) -> float:
        """Calculate monthly P&I payment."""
        pass

    def calculate_monthly_pitia(self, loan_amount: float, rate: float, term_months: int,
                                 annual_taxes: float, annual_insurance: float, monthly_hoa: float,
                                 io_months: int = 0) -> float:
        """Calculate full monthly PITIA."""
        pass

    def determine_qualifying_rent(self, in_place_rent: float, market_rent: float,
                                   is_leased: bool, is_purchase: bool, is_str: bool = False,
                                   str_avg_income: float = 0) -> QualifyingRent:
        """Determine qualifying rent based on scenario."""
        pass

    def calculate_dscr(self, qualifying_rent: float, monthly_pitia: float) -> float:
        """Calculate DSCR ratio."""
        pass

    def get_minimum_dscr(self, fico: int, units: int, is_foreign_national: bool) -> float:
        """Get minimum DSCR requirement for scenario."""
        pass

    def full_dscr_analysis(self, property: Property, loan: Loan, borrower: Borrower) -> DSCRAnalysis:
        """Complete DSCR analysis with all components."""
        pass
```

## Output Format
- ~25 pages
- DSCR calculation examples
- Qualifying rent decision tree
- Comprehensive Python with examples

---

# PROMPT: Section 8 - Appraisal & Valuation Review

## Model: Sonnet

## Objective
Create Section 8 covering appraisal review standards and valuation analysis methodology.

## Required Source Files
```
C:\Users\evana\inspire\Investor Underwriting Guidelines\Archwest RTL Guidelines.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\Eastview DSCR Guidelines_v7.2.pdf
C:\Users\evana\inspire\_PRDs\inspire-phase-7-prd.md (Section 4.3.3 Appraisal Analysis)
```

## INSPIRE Integration Points
- Phase 5-6: Appraisal ordering and receipt
- Phase 7: Automated appraisal analysis and flag generation

## Content Requirements

### 8.1 Appraisal Types by Loan
| Loan Type | Primary | Alternative |
| Fix & Flip | Full Interior | Interior BPO |
| GUC | Full | N/A |
| Bridge | Full Interior | Interior BPO |
| DSCR | Full Interior | CDA (limited scenarios) |

### 8.2 Appraisal Review Checklist
- Report date (120-day currency)
- Appraiser licensing (state certified)
- Property identification match
- Subject photos (interior + exterior)
- Condition rating (C1-C4 acceptable)
- Property type match

### 8.3 Value Analysis
**As-Is Value:**
- Reconciliation review
- Comparable selection criteria
- Adjustment reasonableness

**After-Repair Value (ARV):**
- Comparable selection (renovated properties)
- Adjustment methodology
- Market support analysis

### 8.4 Comparable Analysis Standards
- Proximity requirements
- Age of sale (6 months preferred)
- Property similarity criteria
- Adjustment limits

### 8.5 Value Variance Handling
| Variance | Action |
| <= 5% | No action |
| 5-10% | Review and document |
| > 10% | Resize loan or obtain ROV |

### 8.6 Reconsideration of Value (ROV)
- When to request
- Required documentation
- Timeline expectations

### 8.7 Flag Generation Rules (for INSPIRE)

| Check | Green | Yellow | Red |
|-------|-------|--------|-----|
| Report currency | <= 90 days | 91-120 days | > 120 days |
| Appraiser license | Valid certified | Valid licensed | Invalid/expired |
| Condition | C1-C3 | C4 | C5-C6 |
| Value variance | <= 5% | 5-10% | > 10% |
| Photos | All present | Some missing | Critical missing |

### 8.8 Python Code

```python
class AppraisalAnalyzer:
    """Analyze appraisals and generate flags."""

    def check_currency(self, appraisal_date: date, note_date: date) -> CurrencyResult:
        pass

    def validate_appraiser(self, license_number: str, state: str) -> LicenseValidation:
        pass

    def analyze_value_variance(self, appraised_value: float, expected_value: float) -> VarianceAnalysis:
        pass

    def analyze_comparables(self, comps: List[Comparable]) -> CompAnalysis:
        pass

    def generate_flags(self, appraisal: Appraisal, loan: Loan) -> List[AnalysisFlag]:
        pass
```

## Output Format
- ~18 pages
- Appraisal review checklist
- Flag generation rules table
- Value variance decision tree

---

# PROMPT: Section 9 - RTL Loan Sizing & Leverage

## Model: Opus

## Objective
Create Section 9 covering RTL loan sizing methodology with all leverage constraints and reduction factors. This is a critical calculation section.

## Required Source Files
```
C:\Users\evana\inspire\Investor Underwriting Guidelines\Archwest RTL Guidelines.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\Eastview_RTL_Guidelines_v4_1.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\EV GUC Guidelines_v1.0.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\RTL Program Guidelines (07.09.2025) - CLEAN 1.pdf
C:\Users\evana\inspire\_PRDs\inspire-phase-3-4-prd.md (Section 3.4 RTL Sizer Logic)
```

## INSPIRE Integration Points
- Phase 3-4: RTL loan sizing engine

## Content Requirements

### 9.1 Leverage Metrics Definitions

**As-Is LTV:**
```
As-Is LTV = Loan Amount / As-Is Value
```

**Loan-to-Cost (LTC):**
```
LTC = Total Loan Amount / Total Cost Basis

Cost Basis (Purchase) = Purchase Price + Closing Costs + Assignment Fees
Cost Basis (Refinance) = Original Purchase + Completed Rehab
```

**Loan-to-ARV (LTARV):**
```
LTARV = Total Loan Amount / After-Repair Value
```

### 9.2 Leverage Limits by Product & Classification

**Fix & Flip (Purchase):**
| Class | Max As-Is LTV | Max LTC | Max LTARV |
|-------|---------------|---------|-----------|
| A+ | 90.0% | 90.0% | 75.0% |
| A | 85.0% | 85.0% | 70.0% |
| B | 82.5% | 82.5% | 65.0% |
| C | 75.0% | 75.0% | 60.0% |

**Fix & Flip (Rate & Term Refinance):**
| Class | Max As-Is LTV | Max LTC | Max LTARV |
|-------|---------------|---------|-----------|
| A+ | 75.0% | N/A | 65.0% |
| A | 72.5% | N/A | 65.0% |
| B | 70.0% | N/A | 60.0% |
| C | 60.0% | N/A | 55.0% |

**Fix & Flip (Cash-Out Refinance):**
| Class | Max As-Is LTV | Max LTC | Max LTARV |
|-------|---------------|---------|-----------|
| A+ | 70.0% | N/A | 65.0% |
| A | 67.5% | N/A | 65.0% |
| B | 65.0% | N/A | 60.0% |
| C | N/A | N/A | N/A |

**Bridge (Purchase):**
[Similar table structure]

**Ground-Up Construction:**
| Metric | Limit |
|--------|-------|
| Max LT As-Is (Land) | 70.0% |
| Max LTC | 85.0% |
| Max LTARV | 67.5% |

### 9.3 Leverage Reductions

| Condition | Reduction | Cumulative |
|-----------|-----------|------------|
| HPA Decline 0-10% | -5% | Yes |
| ZHVI Multiplier 200-300% | -5% | Yes |
| Loan Amount $2M-$3M | -5% | Yes |
| Heavy Rehab (Class A/B) | -5% | Yes |
| Heavy Rehab (Class C) | -10% | Yes |
| Small Multifamily 5-9 (RTL) | -5% | Yes |
| Small Multifamily 5-9 (GUC) | -10% | Yes |

### 9.4 Loan Amount Calculation

```
Initial Loan = MIN(
    As-Is Value × Max As-Is LTV,
    Cost Basis × Max LTC,
    ARV × Max LTARV
)

Rehab Holdback = MIN(
    Rehab Budget,
    60% × Total Loan Amount  // Max rehab percentage
)

Total Loan Amount = Initial Loan + Rehab Holdback
```

### 9.5 Cost Basis Calculation
- Purchase: HUD closing costs (excl. origination) + assignment fees (max 5% or $40K)
- Refinance: Original purchase + verified completed rehab

### 9.6 Product Parameters
| Parameter | Fix & Flip | Bridge | Bridge Plus | GUC |
| Min Loan | $100K | $100K | $100K | $100K |
| Max Loan | $3M | $3M | $3M | $3M |
| Term | 12-24mo | 12-24mo | 25-36mo | 12-18mo |
| Structure | I/O | I/O | I/O | I/O |

### 9.7 Python Code

```python
class RTLSizer:
    """Calculate RTL loan sizing with all constraints."""

    # Leverage matrices
    FF_PURCHASE_LEVERAGE = {
        'A+': {'as_is_ltv': 0.90, 'ltc': 0.90, 'ltarv': 0.75},
        'A': {'as_is_ltv': 0.85, 'ltc': 0.85, 'ltarv': 0.70},
        'B': {'as_is_ltv': 0.825, 'ltc': 0.825, 'ltarv': 0.65},
        'C': {'as_is_ltv': 0.75, 'ltc': 0.75, 'ltarv': 0.60},
    }

    def get_leverage_limits(self, classification: str, product: str, purpose: str) -> LeverageLimits:
        pass

    def apply_leverage_reductions(self, limits: LeverageLimits,
                                   hpa_decline: float, zhvi_multiplier: float,
                                   loan_amount: float, is_heavy_rehab: bool,
                                   classification: str, units: int) -> LeverageLimits:
        pass

    def calculate_cost_basis(self, purchase_price: float, closing_costs: float,
                             assignment_fee: float, is_purchase: bool,
                             completed_rehab: float = 0) -> float:
        pass

    def calculate_initial_loan(self, as_is_value: float, cost_basis: float,
                                arv: float, limits: LeverageLimits) -> InitialLoanResult:
        pass

    def calculate_rehab_holdback(self, rehab_budget: float, initial_loan: float) -> float:
        pass

    def size_loan(self, borrower: Borrower, property: Property,
                  loan_request: LoanRequest) -> RTLSizingResult:
        pass
```

## Output Format
- ~28 pages
- Complete leverage matrices
- Calculation examples for each scenario
- Comprehensive Python implementation

---

# PROMPT: Section 10 - DSCR Loan Sizing & Leverage

## Model: Opus

## Objective
Create Section 10 covering DSCR loan sizing methodology with LTV matrices and adjustment factors.

## Required Source Files
```
C:\Users\evana\inspire\Investor Underwriting Guidelines\Eastview DSCR Guidelines_v7.2.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\1. Archwest DSCR Guidelines_7.9.25_V1.8.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\EV DSCR S Matrix_12.29.25.pdf
C:\Users\evana\inspire\_PRDs\inspire-phase-3-4-prd.md (Section 3.5 DSCR Sizer Logic)
```

## INSPIRE Integration Points
- Phase 3-4: DSCR loan sizing engine

## Content Requirements

### 10.1 DSCR Sizing Approach
- LTV-constrained sizing
- DSCR-constrained sizing
- Binding constraint determination

### 10.2 Base LTV by FICO & Purpose

| FICO | Purchase | R&T Refi | Cash-Out |
|------|----------|----------|----------|
| 720+ | 80% | 80% | 75% |
| 700-719 | 75% | 75% | 70% |
| 680-699 | 75% | 75% | 70% |
| 5+ Units | 75% | 70% | 70% |
| Foreign National | 65% | 65% | 60% |

### 10.3 LTV Adjustments

| Condition | Adjustment |
|-----------|------------|
| DSCR >= 1.20 (700-719 FICO) | +5% LTV |
| DSCR >= 1.30 (FN) | +5% LTV |
| STR/Airbnb/VRBO | -5% LTV |
| Section 8/Subsidized | -5% LTV |
| Vacant Refinance | -5% LTV |
| Luxury (>$1M UPB) | -10% LTV |
| Condo | -5% LTV |
| 2-4 Unit | -5% LTV |
| 5-9 Unit | -10% LTV |

### 10.4 DSCR-Constrained Maximum
```
When DSCR < minimum requirement:
Max Loan = Qualifying Rent × 12 / (Min DSCR × Annual PITIA Rate)
```

### 10.5 Foreign National Sizing
- Base LTV: 65% (all purposes)
- Enhanced DSCR: 1.20x minimum
- DSCR >= 1.30x: +5% LTV

### 10.6 5-9 Unit Sizing
- Base LTV: 75% purchase, 70% R&T
- DSCR calculated on NCF basis
- Enhanced documentation

### 10.7 Product Parameters
| Parameter | Value |
| Min Loan | $100,000 |
| Max Loan | $3,000,000 |
| Term | 30 years |
| Rate Types | Fixed 30, 5/1 ARM, 7/1 ARM |
| Amortization | 30-year or 10-year I/O + 20-year amort |

### 10.8 Python Code

```python
class DSCRSizer:
    """Calculate DSCR loan sizing with all constraints."""

    BASE_LTV_MATRIX = {
        # FICO tier: {purpose: ltv}
        '720+': {'purchase': 0.80, 'rt_refi': 0.80, 'cashout': 0.75},
        '700-719': {'purchase': 0.75, 'rt_refi': 0.75, 'cashout': 0.70},
        '680-699': {'purchase': 0.75, 'rt_refi': 0.75, 'cashout': 0.70},
        '5+_units': {'purchase': 0.75, 'rt_refi': 0.70, 'cashout': 0.70},
        'foreign_national': {'purchase': 0.65, 'rt_refi': 0.65, 'cashout': 0.60},
    }

    def get_fico_tier(self, fico: int, units: int, is_fn: bool) -> str:
        pass

    def get_base_ltv(self, fico_tier: str, purpose: str) -> float:
        pass

    def apply_ltv_adjustments(self, base_ltv: float, dscr: float, fico: int,
                               is_str: bool, is_section8: bool, is_vacant: bool,
                               loan_amount: float, property_type: str, units: int) -> float:
        pass

    def calculate_ltv_constrained_loan(self, property_value: float, max_ltv: float) -> float:
        pass

    def calculate_dscr_constrained_loan(self, qualifying_rent: float, min_dscr: float,
                                         rate: float, term: int, taxes: float,
                                         insurance: float, hoa: float) -> float:
        pass

    def size_loan(self, borrower: Borrower, property: Property,
                  loan_request: LoanRequest) -> DSCRSizingResult:
        pass
```

## Output Format
- ~26 pages
- Complete LTV matrices
- Adjustment calculation examples
- Comprehensive Python implementation

---

# PROMPT: Section 11 - Pricing & Rate Calculations

## Model: Opus

## Objective
Create Section 11 covering interest rate determination and LLPA calculations. This is the most complex section with extensive matrices.

## Required Source Files
```
C:\Users\evana\inspire\Investor Underwriting Guidelines\Eastview DSCR Guidelines_v7.2.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\EV DSCR S Matrix_12.29.25.pdf
C:\Users\evana\inspire\Investor Underwriting Guidelines\EV DSCR S Sizer_12.29.25.xlsx
C:\Users\evana\inspire\_PRDs\inspire-phase-3-4-prd.md (Section 3.5.4 DSCR Pricing)
```

## INSPIRE Integration Points
- Phase 3-4: Quote generation, pricing calculations
- Phase 4: Rate lock

## Content Requirements

### 11.1 RTL Pricing
- Base rate determination
- Rate adjustments by classification
- Points structure
- YSP calculation

### 11.2 DSCR Pricing Framework
- Base rate by Treasury spread
- Product types (Fixed 30, 5/1 ARM, 7/1 ARM)
- Price-to-rate conversion

### 11.3 FICO LLPAs (Full Matrix)

| FICO | 50% LTV | 55% | 60% | 65% | 70% | 75% | 80% |
|------|---------|-----|-----|-----|-----|-----|-----|
| 780+ | +1.000% | +0.875% | +0.750% | +0.625% | +0.500% | +0.375% | +0.125% |
| 760-779 | +0.875% | +0.750% | +0.625% | +0.500% | +0.375% | +0.250% | 0.000% |
| 740-759 | +0.750% | +0.625% | +0.500% | +0.375% | +0.250% | +0.125% | -0.125% |
| 720-739 | +0.675% | +0.500% | +0.375% | +0.250% | +0.125% | 0.000% | -0.250% |
| 700-719 | +0.500% | +0.375% | +0.250% | +0.125% | 0.000% | -0.250% | -0.500% |
| 680-699 | +0.375% | +0.250% | +0.125% | -0.250% | -0.750% | -1.000% | N/A |

### 11.4 Additional LLPAs
- DSCR-based LLPAs
- Loan size LLPAs
- Property type LLPAs
- Cash-out LLPAs
- Interest-only LLPAs

### 11.5 Prepayment Penalty LLPAs

| Structure | Adjustment |
|-----------|------------|
| 7 Year Min Interest | +2.000% |
| 7 Year Step-down | +1.750% |
| 5 Year Min Interest | +0.750% |
| 5 Year Step-down | +0.500% |
| 3 Year Step-down | 0.000% |
| 2 Year Step-down | -1.000% |
| 1 Year | -2.000% |
| No Prepay | -4.000% |

### 11.6 USDV Economics
- Origination points calculation
- YSP determination
- All-in pricing

### 11.7 Rate Lock Procedures
- Lock periods (30, 45, 60, 90 days)
- Extension costs (15 bps per 15 days)
- Lock expiration handling

### 11.8 Python Code

```python
class DSCRPricingEngine:
    """Calculate DSCR loan pricing with all LLPAs."""

    FICO_LLPA_MATRIX = {
        # Nested dict: FICO tier -> LTV tier -> LLPA
    }

    PREPAY_LLPAS = {
        '7yr_min_interest': 0.0200,
        '7yr_stepdown': 0.0175,
        # etc.
    }

    def get_fico_llpa(self, fico: int, ltv: float) -> float:
        pass

    def get_dscr_llpa(self, dscr: float, ltv: float) -> float:
        pass

    def get_loan_size_llpa(self, loan_amount: float, ltv: float) -> float:
        pass

    def get_property_type_llpa(self, property_type: str, units: int, ltv: float) -> float:
        pass

    def get_cashout_llpa(self, is_cashout: bool, ltv: float) -> float:
        pass

    def get_io_llpa(self, is_io: bool, ltv: float) -> float:
        pass

    def get_prepay_llpa(self, prepay_structure: str) -> float:
        pass

    def calculate_total_llpa(self, loan: Loan, borrower: Borrower, property: Property) -> LLPABreakdown:
        pass

    def calculate_final_price(self, base_price: float, total_llpa: float) -> float:
        pass

    def price_to_rate(self, price: float, base_rate: float) -> float:
        pass

class RTLPricingEngine:
    """Calculate RTL loan pricing."""
    pass

class RateLockManager:
    """Manage rate locks."""
    pass
```

## Output Format
- ~32 pages
- Complete LLPA matrices (all variations)
- Pricing calculation examples
- Comprehensive Python implementation

---

# PROMPT: Section 12 - Exception Management

## Model: Haiku

## Objective
Create Section 12 covering the exception request process, approval authority, and compensating factor framework.

## Required Source Files
```
C:\Users\evana\inspire\_PRDs\inspire-phase-7-prd.md (Section 6 Exception Management)
C:\Users\evana\inspire\USDV_Underwriting_Manual\IMPLEMENTATION_PLAN_V2.md (Exception Approval Matrix)
```

## INSPIRE Integration Points
- Phase 7: Auto-detection of exceptions, request generation

## Content Requirements

### 12.1 Exception Categories
- Credit exceptions
- LTV/leverage exceptions
- Property exceptions
- Experience exceptions
- Documentation exceptions
- Timing exceptions

### 12.2 Approval Authority Tiers

**Tier 1: Internal (Processor/Sr. UW)**
- Documentation timing (1-15 days)
- Minor credit variance (5-10 points)
- Entity registration timing

**Tier 2: Management (UW Manager)**
- Experience shortfall (1-2 deals)
- LTV variance (1-2%)
- Property condition (C5 with plan)

**Tier 3: Investor Required**
- Major credit exceptions (>20 points)
- Major LTV exceptions (>2%)
- Derogatory credit events
- Non-standard property types

**Tier 4: Not Approvable**
- OFAC match
- Recent fraud conviction
- FICO below 620
- Active bankruptcy

### 12.3 Exception Request Process
- Auto-detection by INSPIRE
- Draft generation
- Supporting documentation
- Routing workflow
- Response tracking

### 12.4 Compensating Factors Framework
- Strong liquidity (>150% required)
- High experience (>10 deals)
- Low leverage (<70% LTV)
- Strong DSCR (>1.30x)
- Prior relationship

### 12.5 Exception Request Template
[Include full template from PRD]

### 12.6 Python Code

```python
class ExceptionManager:
    """Manage exception identification and requests."""

    def identify_exceptions(self, loan: Loan, borrower: Borrower,
                           property: Property, flags: List[AnalysisFlag]) -> List[Exception]:
        pass

    def determine_approval_tier(self, exception: Exception) -> ApprovalTier:
        pass

    def identify_compensating_factors(self, loan: Loan, borrower: Borrower,
                                       property: Property) -> List[CompensatingFactor]:
        pass

    def generate_exception_request(self, exception: Exception,
                                    compensating_factors: List[CompensatingFactor]) -> ExceptionRequest:
        pass
```

## Output Format
- ~15 pages
- Exception type matrix
- Approval authority flowchart
- Request template

---

# PROMPT: Section 13 - Document Requirements & Diligence

## Model: Haiku

## Objective
Create Section 13 covering complete document requirements by loan type and client type.

## Required Source Files
```
C:\Users\evana\inspire\Investor Underwriting Guidelines\Churchill DSCR - Required Document List.docx
C:\Users\evana\inspire\_PRDs\inspire-phase-5-6-prd.md (Section 4 Diligence)
```

## INSPIRE Integration Points
- Phase 5-6: Diligence checklist generation, document tracking

## Content Requirements

### 13.1 Document Matrix Overview
- By loan type (RTL vs DSCR)
- By client type (New, Existing, RE CFO)
- By loan purpose (Purchase, R&T, Cash-Out)

### 13.2 Borrower Documents
[Full list with requirements]

### 13.3 Property Documents
- RTL specific
- DSCR specific

### 13.4 Third-Party Reports
[Full list]

### 13.5 Closing Documents
[Full list]

### 13.6 Document Currency Requirements
| Document | Max Age |
| Credit Report | 120 days |
| Bank Statements | 90 days |
| Good Standing | 90 days |
| Appraisal | 120 days |

### 13.7 Existing Client Streamlining
- On-file documents
- Verification requirements

### 13.8 Python Code

```python
class DiligenceChecker:
    """Generate and track diligence checklists."""

    def generate_checklist(self, loan_type: str, client_type: str,
                           loan_purpose: str) -> DiligenceChecklist:
        pass

    def check_document_currency(self, doc_type: str, doc_date: date) -> CurrencyResult:
        pass

    def get_checklist_completion(self, deal: Deal) -> CompletionStatus:
        pass
```

## Output Format
- ~20 pages
- Complete document checklists
- Currency requirements table
- Client type variations

---

# PROMPT: Section 14 - Third-Party Report Analysis

## Model: Opus

## Objective
Create Section 14 covering analysis standards for all third-party reports with explicit flag generation rules. This section directly supports INSPIRE Phase 7.

## Required Source Files
```
C:\Users\evana\inspire\_PRDs\inspire-phase-7-prd.md (All Section 4)
C:\Users\evana\inspire\Investor Underwriting Guidelines\[All guidelines for thresholds]
```

## INSPIRE Integration Points
- Phase 7: All automated analysis and flag generation

## Content Requirements

### 14.1 Credit Report Analysis
[Detailed rules with flag criteria]

### 14.2 Background Check Analysis
[Detailed rules with flag criteria]

### 14.3 Appraisal Analysis
[Detailed rules with flag criteria]

### 14.4 Title Report Analysis
- Schedule B-I review
- Schedule B-II exceptions
- Lien analysis
- Flag criteria

### 14.5 Insurance Certificate Analysis
- Coverage validation
- Mortgagee clause verification
- Flag criteria

### 14.6 Feasibility Study Analysis (RTL)
- Budget alignment
- Timeline validation
- Flag criteria

### 14.7 Bank Statement Analysis
- Currency check
- Liquidity verification
- Large deposit review
- Flag criteria

### 14.8 Lease Analysis (DSCR)
- Arm's length verification
- Rent validation
- Flag criteria

### 14.9 Complete Flag Rules Table
[Master table of all flags by document type]

### 14.10 Python Code

```python
class ReportAnalyzer:
    """Base class for report analysis."""
    pass

class CreditReportAnalyzer(ReportAnalyzer):
    pass

class BackgroundCheckAnalyzer(ReportAnalyzer):
    pass

class AppraisalAnalyzer(ReportAnalyzer):
    pass

class TitleAnalyzer(ReportAnalyzer):
    pass

class InsuranceAnalyzer(ReportAnalyzer):
    pass

class FeasibilityAnalyzer(ReportAnalyzer):
    pass

class BankStatementAnalyzer(ReportAnalyzer):
    pass

class LeaseAnalyzer(ReportAnalyzer):
    pass

class FlagGenerator:
    """Generate flags from all analyses."""

    def generate_all_flags(self, deal: Deal) -> List[AnalysisFlag]:
        pass
```

## Output Format
- ~28 pages
- Complete flag rules for each report type
- Master flag table
- Comprehensive Python implementation

---

# PROMPT: Section 15 - Credit Memo & Risk Assessment

## Model: Sonnet

## Objective
Create Section 15 covering credit memo structure (matching Phase 7 PRD exactly) and risk rating framework.

## Required Source Files
```
C:\Users\evana\inspire\_PRDs\inspire-phase-7-prd.md (Section 7 Credit Memo)
```

## INSPIRE Integration Points
- Phase 7: Credit memo generation

## Content Requirements

### 15.1 Credit Memo Structure (~6 pages)
Must match Phase 7 PRD exactly:
1. Executive Summary (½ page)
2. Borrower Analysis (1 page)
3. Property Analysis (1 page)
4. Deal Economics (1 page)
5. Third-Party Report Summary (1 page)
6. Risk Assessment (1 page)
7. Conditions & Exceptions (½ page)

### 15.2 Section Content Guidelines
[Detailed content for each section]

### 15.3 Risk Rating Framework

| Rating | Criteria |
|--------|----------|
| Low | All green flags; FICO >720; LTV <70% |
| Moderate | Some yellow flags; FICO 680-720; LTV 70-75% |
| Elevated | Multiple yellow flags; FICO 660-680; LTV >75% |
| High | Red flags present; exceptions required |

### 15.4 Recommendation Framework
- Approve
- Approve with Conditions
- Decline

### 15.5 Flag Integration
- Flag aggregation
- Risk rating calculation

### 15.6 Python Code

```python
class CreditMemoGenerator:
    """Generate credit memorandum."""

    def generate_executive_summary(self, deal: Deal) -> str:
        pass

    def generate_borrower_analysis(self, deal: Deal, borrower: Borrower) -> str:
        pass

    def generate_property_analysis(self, deal: Deal, property: Property) -> str:
        pass

    def generate_deal_economics(self, deal: Deal) -> str:
        pass

    def generate_third_party_summary(self, deal: Deal, reports: List[Report]) -> str:
        pass

    def generate_risk_assessment(self, flags: List[AnalysisFlag]) -> str:
        pass

    def generate_conditions_exceptions(self, deal: Deal) -> str:
        pass

    def generate_full_memo(self, deal: Deal) -> CreditMemo:
        pass

class RiskRatingCalculator:
    """Calculate overall risk rating."""

    def calculate_rating(self, flags: List[AnalysisFlag],
                         borrower: Borrower, loan: Loan) -> RiskRating:
        pass

    def determine_recommendation(self, rating: RiskRating,
                                  exceptions: List[Exception]) -> Recommendation:
        pass
```

## Output Format
- ~22 pages
- Credit memo template
- Risk rating criteria
- Python implementation

---

# PROMPT: Section 16 - Comprehensive Glossary

## Model: Haiku

## Objective
Create Section 16 containing the comprehensive glossary of 200+ terms used throughout the manual.

## Required Source Files
```
All previous sections of the manual (for term extraction)
C:\Users\evana\inspire\_PRDs\inspire-master-prd.md (for INSPIRE-specific terms)
```

## INSPIRE Integration Points
- All phases: Term definitions, tooltips, AI context

## Content Requirements

### 16.1 Glossary Format

```markdown
## TERM NAME (Acronym)

**Definition:**
Clear, concise definition.

**Formula:** (if applicable)
Mathematical formula with variables defined.

**Example:**
Practical usage example.

**Related Terms:**
Cross-references to other glossary entries.

**Manual References:**
Section numbers where this term is used.
```

### 16.2 Required Terms (A-Z)

**A:** Acquisition, Amortization, Appraisal, ARM, ARV, As-Is Value, Assignment Fee...
**B:** Background Check, Bankruptcy, Base Rate, BPO, Bridge Loan, Builder's Risk...
**C:** Cap Rate, Cash-Out, CDA, Classification, Closing Costs, Collateral, Collections...
[Continue through Z]

### 16.3 Acronym Reference Table
| Acronym | Full Term | Section |
| ARV | After-Repair Value | 6, 9 |
| DSCR | Debt Service Coverage Ratio | 7, 10 |
[etc.]

### 16.4 Formula Reference
All formulas used in the manual compiled in one location.

## Output Format
- ~45 pages
- Alphabetical organization
- Cross-references
- Formula compilation

---

*End of Section Prompts Master Document*
