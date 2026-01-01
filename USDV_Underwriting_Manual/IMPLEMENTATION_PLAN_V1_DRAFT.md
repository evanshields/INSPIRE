# USDV Capital Underwriting Manual
## Implementation Plan

**Project:** USDV Capital Single-Family Business Purpose Loan Underwriting Manual
**For Use With:** INSPIRE Loan Origination System
**Created:** December 2025
**Status:** Implementation Plan - Awaiting Approval

---

## Executive Summary

This implementation plan outlines the creation of a comprehensive underwriting manual for USDV Capital's single-family business purpose lending operations. The manual will serve as the authoritative reference for underwriting RTL loans (Fix & Flip, Ground-Up Construction, Bridge) and DSCR permanent loans, incorporating guidelines from three primary investors: **ArchWest**, **EastView**, and **Churchill**.

The manual will follow a similar structure and depth to the Shieldstone Multifamily Value-Add Underwriting Manual, including:
- Comprehensive underwriting guidelines and methodologies
- Production-ready Python calculation library
- Full glossary of 200+ terms
- Integration points with the INSPIRE platform (Phase 7: AI Analysis & Credit Memo)

---

## Table of Contents

1. [Manual Structure Overview](#1-manual-structure-overview)
2. [Chapter-by-Chapter Implementation](#2-chapter-by-chapter-implementation)
3. [Python Library Architecture](#3-python-library-architecture)
4. [Model Selection by Section](#4-model-selection-by-section)
5. [Glossary Structure](#5-glossary-structure)
6. [Implementation Timeline](#6-implementation-timeline)
7. [Dependencies & Prerequisites](#7-dependencies--prerequisites)
8. [Quality Assurance](#8-quality-assurance)

---

## 1. Manual Structure Overview

### 1.1 Proposed Manual Outline

The USDV Underwriting Manual will be organized into **16 Sections** across **4 Parts**:

```
PART I: FOUNDATIONS (Sections 1-4)
├── Section 1: Investment Philosophy & Loan Products
├── Section 2: Borrower Eligibility & Qualification
├── Section 3: Entity & Guarantor Analysis
└── Section 4: Credit & Background Evaluation

PART II: PROPERTY & VALUATION (Sections 5-8)
├── Section 5: Property Eligibility Standards
├── Section 6: RTL Property Analysis (Fix & Flip, GUC, Bridge)
├── Section 7: DSCR Property & Income Analysis
└── Section 8: Appraisal & Valuation Review

PART III: LOAN STRUCTURING (Sections 9-12)
├── Section 9: RTL Loan Sizing & Leverage
├── Section 10: DSCR Loan Sizing & Leverage
├── Section 11: Pricing & Rate Calculations
└── Section 12: Exception Management

PART IV: OPERATIONS & REFERENCE (Sections 13-16)
├── Section 13: Document Requirements & Diligence
├── Section 14: Third-Party Report Analysis
├── Section 15: Credit Memo & Risk Assessment
└── Section 16: Comprehensive Glossary
```

### 1.2 Cross-Reference to Investor Guidelines

| Manual Section | ArchWest Ref | EastView Ref | Churchill Ref |
|----------------|--------------|--------------|---------------|
| Borrower Eligibility | DSCR v1.8, RTL | RTL v4.1, DSCR v7.2 | DSCR 8.8.23, RTL 06.23 |
| Property Standards | Both guidelines | Both guidelines | Both guidelines |
| Leverage Limits | Both guidelines | Both + GUC v1.0 | Both guidelines |
| Pricing/LLPAs | DSCR matrix | DSCR S Matrix 12.29.25 | DSCR guidelines |
| Documentation | Both guidelines | Both guidelines | Required Doc List |

### 1.3 Integration with INSPIRE

The manual will directly support INSPIRE's Phase 7 (AI Analysis & Credit Memo) by providing:
- Structured rule definitions for automated document analysis
- Flag generation criteria (Green/Yellow/Red)
- Credit memo narrative templates
- Exception request frameworks

---

## 2. Chapter-by-Chapter Implementation

### PART I: FOUNDATIONS

---

#### Section 1: Investment Philosophy & Loan Products

**Purpose:** Establish USDV's lending philosophy and define all supported loan products with their key parameters.

**Contents:**
- 1.1 USDV Capital Mission & Risk Philosophy
- 1.2 Loan Product Overview
  - 1.2.1 Fix & Flip (RTL)
  - 1.2.2 Ground-Up Construction (GUC)
  - 1.2.3 Bridge Loans
  - 1.2.4 DSCR Permanent Loans
- 1.3 Investor Partner Profiles (ArchWest, EastView, Churchill)
- 1.4 Loan Parameter Summary Tables
- 1.5 BRRRR Exclusion Policy
- 1.6 Python: LoanProduct class definitions

**Key Data Points to Extract from Guidelines:**

| Parameter | RTL | GUC | Bridge | DSCR |
|-----------|-----|-----|--------|------|
| Min Loan | $100K | $100K | $100K | $100K |
| Max Loan | $3M | $3M | $3M | $3M |
| Term | 12-24mo | 12-18mo | 12-36mo | 30yr |
| Structure | I/O | I/O | I/O | I/O or Amort |
| Min FICO | 660 | 660 | 660 | 680 |
| Min Experience | 1 deal | Varies | 1 deal | None |

**Model Recommendation:** `Sonnet` - Requires synthesis of multiple investor guidelines into unified framework. Moderate complexity.

**Estimated Output:** ~15 pages + Python code

---

#### Section 2: Borrower Eligibility & Qualification

**Purpose:** Define borrower qualification standards including experience, citizenship, and prohibited borrower characteristics.

**Contents:**
- 2.1 Borrower Classification Framework
  - 2.1.1 RTL Classification (A+, A, B, C)
  - 2.1.2 DSCR Tier Assignment
- 2.2 Experience Requirements
  - 2.2.1 Verified Experience Definition
  - 2.2.2 Experience Documentation
  - 2.2.3 First-Time Investor Programs
- 2.3 Citizenship & Residency
  - 2.3.1 US Citizens & Permanent Residents
  - 2.3.2 Foreign National Programs
  - 2.3.3 ITIN Borrowers
- 2.4 Prohibited Borrowers & OFAC Screening
- 2.5 Python: BorrowerClassifier class

**Borrower Classification Logic (from PRD Phase 3-4):**

```python
# Credit Decision Score
FICO >= 700: 3 points
FICO 680-699: 1 point
FICO < 680 or FN: 0 points

# Experience Score (36 months)
10+ deals: 7 points
3-9 deals: 5 points
0-2 deals: 1 point

# Classification
>= 7 points: A+
5-6 points: A
2-4 points: B
< 2 points: C
```

**Model Recommendation:** `Sonnet` - Core classification logic requires accuracy. Multiple investor variations to reconcile.

**Estimated Output:** ~20 pages + Python code

---

#### Section 3: Entity & Guarantor Analysis

**Purpose:** Define requirements for borrowing entities, ownership structures, and guarantor qualifications.

**Contents:**
- 3.1 Eligible Entity Types
  - 3.1.1 LLCs, LPs, Corporations
  - 3.1.2 Trust Structures
  - 3.1.3 Ineligible Entities
- 3.2 Ownership Structure Analysis
  - 3.2.1 Ownership Percentage Requirements
  - 3.2.2 Nested Entity Structures
  - 3.2.3 Multiple Guarantors
- 3.3 Guarantor Requirements
  - 3.3.1 Key Principal Identification
  - 3.3.2 Guarantor Minimum Qualifications
  - 3.3.3 Carve-Out Guarantees
- 3.4 State Registration & Good Standing
- 3.5 Python: EntityAnalyzer class

**Model Recommendation:** `Sonnet` - Complex ownership analysis logic needed.

**Estimated Output:** ~18 pages + Python code

---

#### Section 4: Credit & Background Evaluation

**Purpose:** Define credit report analysis standards and background check evaluation criteria.

**Contents:**
- 4.1 Credit Report Requirements
  - 4.1.1 Tri-Merge Report Standards
  - 4.1.2 FICO Score Tiers
  - 4.1.3 Trade Line Requirements
- 4.2 Mortgage History Analysis
  - 4.2.1 Housing Payment History
  - 4.2.2 Late Payment Thresholds
- 4.3 Derogatory Credit Events
  - 4.3.1 Bankruptcy (Chapter 7, 13)
  - 4.3.2 Foreclosure
  - 4.3.3 Short Sale / DIL
  - 4.3.4 Judgments & Liens
  - 4.3.5 Collections
- 4.4 Background Check Evaluation
  - 4.4.1 Criminal History Review
  - 4.4.2 Civil Litigation
  - 4.4.3 OFAC/AML Screening
- 4.5 Credit Exception Framework
- 4.6 Python: CreditAnalyzer, BackgroundChecker classes

**Credit Analysis Thresholds (from Investor Guidelines):**

| Factor | RTL Standard | DSCR Standard | Flag Type |
|--------|--------------|---------------|-----------|
| Min FICO | 660 | 680 | Red if below |
| BK Ch 7 Seasoning | 4 years | 4 years | Red if within |
| Foreclosure Seasoning | 4 years | 4 years | Red if within |
| Housing Lates (12mo) | 0x30 | 1x30 max | Red/Yellow |
| Trade Lines | 3 total | 3 total | Red if below |
| Active Judgments | None >$10K | None >$10K | Red if found |

**Model Recommendation:** `Opus` - Critical section with regulatory implications. Requires precise extraction from multiple guidelines.

**Estimated Output:** ~25 pages + Python code

---

### PART II: PROPERTY & VALUATION

---

#### Section 5: Property Eligibility Standards

**Purpose:** Define eligible property types, locations, and condition requirements.

**Contents:**
- 5.1 Eligible Property Types
  - 5.1.1 Single Family Residences
  - 5.1.2 Condominiums (Warrantable/Non-Warrantable)
  - 5.1.3 Townhomes
  - 5.1.4 2-4 Unit Properties
  - 5.1.5 5-9 Unit Properties (Small Multifamily)
- 5.2 Ineligible Property Types
- 5.3 Geographic Eligibility
  - 5.3.1 State Restrictions
  - 5.3.2 Rural Property Limitations
  - 5.3.3 Declining Markets
- 5.4 Property Condition Standards
  - 5.4.1 Condition Ratings (C1-C6)
  - 5.4.2 Minimum Habitability Standards
- 5.5 Size & Value Requirements
  - 5.5.1 Minimum Square Footage
  - 5.5.2 Loan Amount Limits by Property Type
- 5.6 Acreage & Land Limitations
- 5.7 Python: PropertyEligibilityChecker class

**Property Type Matrix:**

| Property Type | RTL Eligible | DSCR Eligible | Max LTV Impact | Notes |
|---------------|--------------|---------------|----------------|-------|
| SFR | Yes | Yes | Standard | Primary focus |
| Condo (Warr) | Yes | Yes | -5% LTV | HOA review |
| Condo (Non-Warr) | Limited | Limited | -10% LTV | Case-by-case |
| Townhome | Yes | Yes | Standard | - |
| 2-4 Unit | Yes | Yes | -5% LTV | Unit count based |
| 5-9 Unit | Yes (some) | Yes (some) | -10% LTV | Enhanced DD |
| Manufactured | No | No | N/A | Excluded |
| Mixed-Use | No | No | N/A | Excluded |

**Model Recommendation:** `Sonnet` - Moderate complexity, requires consolidation of eligibility matrices.

**Estimated Output:** ~22 pages + Python code

---

#### Section 6: RTL Property Analysis

**Purpose:** Define property evaluation standards specific to RTL loans (Fix & Flip, Ground-Up Construction, Bridge).

**Contents:**
- 6.1 Fix & Flip Property Analysis
  - 6.1.1 As-Is Condition Assessment
  - 6.1.2 Scope of Work Evaluation
  - 6.1.3 ARV Analysis & Support
  - 6.1.4 Heavy Rehab Definition & Standards
- 6.2 Ground-Up Construction Analysis
  - 6.2.1 Land Valuation
  - 6.2.2 Plans & Specifications Review
  - 6.2.3 Construction Budget Validation
  - 6.2.4 Permit Status & Timeline
- 6.3 Bridge Loan Property Analysis
  - 6.3.1 Stabilized Property Standards
  - 6.3.2 Value-Add Bridge Scenarios
- 6.4 Feasibility Study Review
  - 6.4.1 Budget Alignment Analysis
  - 6.4.2 Timeline Reasonableness
  - 6.4.3 Contingency Requirements
- 6.5 Exit Strategy Validation
- 6.6 Python: RTLPropertyAnalyzer class

**Heavy Rehab Definition (from Guidelines):**
- Rehab budget > $50,000 AND
- Rehab budget > 100% of purchase price (or as-is value for refi)
- Results in -5% leverage reduction (Class A/B) or -10% (Class C)

**Model Recommendation:** `Sonnet` - Technical property analysis with clear criteria.

**Estimated Output:** ~24 pages + Python code

---

#### Section 7: DSCR Property & Income Analysis

**Purpose:** Define property and income analysis standards for DSCR permanent loans.

**Contents:**
- 7.1 DSCR Calculation Methodology
  - 7.1.1 Formula & Components
  - 7.1.2 PITIA Calculation
  - 7.1.3 Qualifying Rent Determination
- 7.2 Rental Income Analysis
  - 7.2.1 Leased Properties (In-Place Rent)
  - 7.2.2 Unleased Properties (Market Rent)
  - 7.2.3 Short-Term Rental / Vacation Rental
  - 7.2.4 Section 8 / Subsidized Housing
- 7.3 Lease Review Standards
  - 7.3.1 Arm's Length Requirements
  - 7.3.2 Lease Term Limitations
  - 7.3.3 Rent Verification Methods
- 7.4 Market Rent Validation
  - 7.4.1 Comp Analysis Standards
  - 7.4.2 Rent Roll Review
- 7.5 DSCR Thresholds by Scenario
- 7.6 Python: DSCRCalculator class

**DSCR Calculation Framework:**

```python
class DSCRCalculator:
    """
    DSCR = Qualifying Monthly Rent / Monthly PITIA

    Monthly PITIA Components:
    - Principal & Interest (P&I) - Based on loan terms
    - Taxes (T) - Annual property taxes / 12
    - Insurance (I) - Annual insurance / 12
    - Association (A) - Monthly HOA fees

    Qualifying Rent Rules:
    - Leased (Purchase): MIN(In-place rent, 100% Market rent)
    - Leased (Refi): MIN(In-place rent, 100% Market rent)
    - Unleased (Purchase): 100% Market rent
    - Unleased (Refi): 90% Market rent + 5% LTV reduction
    - Vacation Rental: MIN(125% Market rent, 12mo avg income)
    """
```

**Minimum DSCR Requirements:**

| Scenario | Min DSCR | Notes |
|----------|----------|-------|
| FICO >= 700 | 1.00x | Standard |
| FICO < 700 | 1.20x | Credit adjustment |
| 5-9 Unit | 1.20x NCF | Net Cash Flow basis |
| Foreign National | 1.20x | Enhanced requirement |

**Model Recommendation:** `Opus` - Complex financial calculations with multiple scenarios. Critical for accuracy.

**Estimated Output:** ~28 pages + Python code

---

#### Section 8: Appraisal & Valuation Review

**Purpose:** Define appraisal review standards and valuation analysis methodology.

**Contents:**
- 8.1 Appraisal Requirements by Loan Type
  - 8.1.1 Full Appraisal Standards
  - 8.1.2 Interior BPO Scenarios
  - 8.1.3 Desktop Analysis (CDA)
- 8.2 Appraisal Review Checklist
  - 8.2.1 Report Currency Requirements
  - 8.2.2 Appraiser Licensing Validation
  - 8.2.3 Property Condition Assessment
- 8.3 Value Analysis
  - 8.3.1 As-Is Value Evaluation
  - 8.3.2 After-Repair Value (ARV) Support
  - 8.3.3 Comparable Sales Analysis
- 8.4 Value Variance Handling
  - 8.4.1 Acceptable Variance Thresholds
  - 8.4.2 Resizing Triggers
  - 8.4.3 Reconsideration of Value Process
- 8.5 Python: AppraisalAnalyzer class

**Appraisal Review Flags:**

| Check | Pass Criteria | Flag if Fail |
|-------|---------------|--------------|
| Report Date | Within 120 days | Red |
| Appraiser License | State certified | Red |
| Condition Rating | C1-C4 | Red if C5-C6 |
| Property Type | Matches eligible | Red |
| Square Footage | SFR >= 600sf | Red |
| Rural Designation | Not rural | Red |
| Photos | Interior + Exterior | Yellow |
| Comps | 6mo, same neighborhood | Yellow |
| Value Variance | Within 10% of app | Yellow |

**Model Recommendation:** `Sonnet` - Technical but well-defined criteria.

**Estimated Output:** ~20 pages + Python code

---

### PART III: LOAN STRUCTURING

---

#### Section 9: RTL Loan Sizing & Leverage

**Purpose:** Define RTL loan sizing methodology, leverage limits, and leverage reduction rules.

**Contents:**
- 9.1 RTL Leverage Framework
  - 9.1.1 As-Is LTV
  - 9.1.2 Loan-to-Cost (LTC)
  - 9.1.3 Loan-to-ARV (LTARV)
- 9.2 Leverage Limits by Product & Classification
  - 9.2.1 Fix & Flip (Purchase)
  - 9.2.2 Fix & Flip (Rate & Term Refi)
  - 9.2.3 Fix & Flip (Cash-Out Refi)
  - 9.2.4 Bridge (Purchase/Refi)
  - 9.2.5 Ground-Up Construction
- 9.3 Leverage Reductions
  - 9.3.1 HPA Decline Markets
  - 9.3.2 ZHVI Multiplier Impact
  - 9.3.3 High Loan Amount Adjustments
  - 9.3.4 Heavy Rehab Impact
  - 9.3.5 Small Multifamily Adjustments
- 9.4 Loan Amount Calculation
  - 9.4.1 Initial Loan Calculation
  - 9.4.2 Rehab Holdback Calculation
  - 9.4.3 Cost Basis Determination
- 9.5 Python: RTLSizer class

**RTL Leverage Matrix (Fix & Flip Purchase):**

| Classification | Max As-Is LTV | Max LTC | Max LTARV |
|----------------|---------------|---------|-----------|
| A+ | 90.0% | 90.0% | 75.0% |
| A | 85.0% | 85.0% | 70.0% |
| B | 82.5% | 82.5% | 65.0% |
| C | 75.0% | 75.0% | 60.0% |

**Leverage Reduction Matrix:**

| Condition | Reduction |
|-----------|-----------|
| HPA Decline 0-10% | -5% |
| ZHVI Multiplier 200-300% | -5% |
| Loan Amount $2M-$3M | -5% |
| Heavy Rehab (Class A/B) | -5% |
| Heavy Rehab (Class C) | -10% |
| Small Multifamily 5-9 (RTL) | -5% |
| Small Multifamily 5-9 (GUC) | -10% |

**Model Recommendation:** `Opus` - Critical financial calculations. Direct impact on loan economics.

**Estimated Output:** ~30 pages + Python code

---

#### Section 10: DSCR Loan Sizing & Leverage

**Purpose:** Define DSCR loan sizing methodology, LTV limits by scenario, and adjustment factors.

**Contents:**
- 10.1 DSCR Leverage Framework
  - 10.1.1 LTV-Based Sizing
  - 10.1.2 DSCR-Constrained Sizing
  - 10.1.3 Binding Constraint Analysis
- 10.2 Base LTV by FICO & Purpose
  - 10.2.1 Purchase LTV Matrix
  - 10.2.2 Rate & Term Refi Matrix
  - 10.2.3 Cash-Out Refi Matrix
- 10.3 LTV Adjustments
  - 10.3.1 DSCR-Based Adjustments
  - 10.3.2 Property Type Adjustments
  - 10.3.3 Occupancy Adjustments
  - 10.3.4 Loan Size Adjustments
- 10.4 Foreign National Sizing
- 10.5 5-9 Unit Sizing
- 10.6 Python: DSCRSizer class

**DSCR Base LTV Matrix:**

| FICO | Purchase | R&T Refi | Cash-Out |
|------|----------|----------|----------|
| 720+ | 80% | 80% | 75% |
| 700-719 | 75% | 75% | 70% |
| 680-699 | 75% | 75% | 70% |
| 5+ Units | 75% | 70% | 70% |
| Foreign Nat | 65% | 65% | 60% |

**LTV Adjustment Matrix:**

| Condition | Adjustment |
|-----------|------------|
| DSCR 1.00-1.10 | -0% to -0.375% (by LTV) |
| DSCR >= 1.15 | +0.50% |
| DSCR >= 1.20 (700-719 FICO) | +5% LTV |
| DSCR >= 1.30 (FN) | +5% LTV |
| STR/Airbnb | -5% LTV |
| Section 8 | -5% LTV |
| Vacant Refi | -5% LTV |
| Luxury (>$1M) | -10% LTV |

**Model Recommendation:** `Opus` - Complex matrices with multiple interdependencies. Must be accurate.

**Estimated Output:** ~28 pages + Python code

---

#### Section 11: Pricing & Rate Calculations

**Purpose:** Define interest rate determination, LLPA calculations, and YSP/origination fee structure.

**Contents:**
- 11.1 RTL Pricing
  - 11.1.1 Base Rate Determination
  - 11.1.2 Rate Adjustments by Classification
  - 11.1.3 Points Structure
- 11.2 DSCR Pricing Framework
  - 11.2.1 Base Rate by Spread (5YR Treasury)
  - 11.2.2 Product Types (Fixed 30, 5/1 ARM, 7/1 ARM)
  - 11.2.3 Rate Type Selection
- 11.3 LLPA (Loan Level Price Adjustments)
  - 11.3.1 FICO-Based LLPAs
  - 11.3.2 LTV-Based LLPAs
  - 11.3.3 Property Type LLPAs
  - 11.3.4 DSCR-Based LLPAs
  - 11.3.5 Loan Size LLPAs
  - 11.3.6 Cash-Out LLPAs
  - 11.3.7 Interest-Only LLPAs
- 11.4 Prepayment Penalty Structures
  - 11.4.1 Step-Down Structures
  - 11.4.2 Level Prepay
  - 11.4.3 Minimum Interest
  - 11.4.4 Prepay LLPAs
- 11.5 USDV Economics
  - 11.5.1 Origination Points
  - 11.5.2 Yield Spread Premium (YSP)
- 11.6 Rate Lock Procedures
- 11.7 Python: PricingEngine class

**DSCR LLPA Matrix (Sample - FICO by LTV):**

| FICO | 50% | 55% | 60% | 65% | 70% | 75% | 80% |
|------|-----|-----|-----|-----|-----|-----|-----|
| 780+ | +1.00% | +0.875% | +0.75% | +0.625% | +0.50% | +0.375% | +0.125% |
| 760-779 | +0.875% | +0.75% | +0.625% | +0.50% | +0.375% | +0.25% | 0.00% |
| 740-759 | +0.75% | +0.625% | +0.50% | +0.375% | +0.25% | +0.125% | -0.125% |
| 720-739 | +0.675% | +0.50% | +0.375% | +0.25% | +0.125% | 0.00% | -0.25% |
| 700-719 | +0.50% | +0.375% | +0.25% | +0.125% | 0.00% | -0.25% | -0.50% |
| 680-699 | +0.375% | +0.25% | +0.125% | -0.25% | -0.75% | -1.00% | N/A |

**Prepayment Penalty LLPAs:**

| Structure | Adjustment |
|-----------|------------|
| 7 Year (84mo) Min Interest | +2.00% |
| 7 Year Step-down (7/6/5/4/3/2/1) | +1.75% |
| 5 Year (60mo) Min Interest | +0.75% |
| 5 Year Step-down (5/4/3/2/1) | +0.50% |
| 3 Year Step-down (3/2/1) | 0.00% |
| 2 Year Step-down (2/1) | -1.00% |
| 1 Year (1%) | -2.00% |
| No Prepay | -4.00% |

**Model Recommendation:** `Opus` - Most complex section. LLPA calculations require precision.

**Estimated Output:** ~35 pages + Python code

---

#### Section 12: Exception Management

**Purpose:** Define the exception request process, approval authority, and compensating factor framework.

**Contents:**
- 12.1 Exception Categories
  - 12.1.1 Credit Exceptions
  - 12.1.2 LTV Exceptions
  - 12.1.3 Property Exceptions
  - 12.1.4 Experience Exceptions
  - 12.1.5 Documentation Exceptions
- 12.2 Exception Request Process
  - 12.2.1 Auto-Detection by INSPIRE
  - 12.2.2 Request Template
  - 12.2.3 Required Supporting Documentation
- 12.3 Compensating Factors Framework
  - 12.3.1 Strong Liquidity (>150% required)
  - 12.3.2 High Experience (>10 deals)
  - 12.3.3 Low Leverage (<70% LTV)
  - 12.3.4 Strong DSCR (>1.30x)
  - 12.3.5 Prior Relationship
- 12.4 Approval Authority Matrix
- 12.5 Exception Tracking & Reporting
- 12.6 Python: ExceptionManager class

**Exception Request Template:**
```
EXCEPTION REQUEST

Deal: [Address]
Loan Type: [Type]
Investor: [Investor]

EXCEPTION REQUESTED:
[Type]: [Current Value] → Requesting: [Requested Value]

GUIDELINE REFERENCE:
Per [Investor] Guidelines, requirement is [X].
Subject deal shows [Y].

MITIGATING FACTORS:
• [Factor 1 with data]
• [Factor 2 with data]

COMPENSATING STRENGTHS:
• [Strength 1]
• [Strength 2]

RECOMMENDATION:
USDV recommends approval based on above factors.
```

**Model Recommendation:** `Sonnet` - Process-oriented content with templates.

**Estimated Output:** ~18 pages + Python code

---

### PART IV: OPERATIONS & REFERENCE

---

#### Section 13: Document Requirements & Diligence

**Purpose:** Define complete document requirements by loan type and client type.

**Contents:**
- 13.1 Document Matrix Overview
- 13.2 Borrower Documents
  - 13.2.1 Entity Formation Documents
  - 13.2.2 Personal Identification
  - 13.2.3 Financial Documents
- 13.3 Property Documents
  - 13.3.1 RTL Property Documents
  - 13.3.2 DSCR Property Documents
- 13.4 Third-Party Reports
- 13.5 Closing Documents
- 13.6 Document Currency Requirements
- 13.7 Existing Client Streamlining
- 13.8 Python: DiligenceChecker class

**Document Currency Standards:**

| Document Type | Max Age | Notes |
|---------------|---------|-------|
| Credit Report | 120 days | From pull date |
| Background Check | 120 days | From pull date |
| Appraisal | 120 days | From note date |
| Bank Statements | 90 days | From statement date |
| Good Standing | 90 days | From issue date |
| Title Commitment | 90 days | Standard |
| Insurance | Active at close | Min 6mo forward |

**Model Recommendation:** `Sonnet` - Reference content with clear structure.

**Estimated Output:** ~22 pages + Python code

---

#### Section 14: Third-Party Report Analysis

**Purpose:** Define analysis standards for all third-party reports with automated flag generation rules.

**Contents:**
- 14.1 Credit Report Analysis
  - 14.1.1 Score Extraction
  - 14.1.2 Trade Line Analysis
  - 14.1.3 Derogatory Analysis
  - 14.1.4 Flag Generation Rules
- 14.2 Background Check Analysis
  - 14.2.1 Criminal History Review
  - 14.2.2 Civil Litigation Review
  - 14.2.3 OFAC/Sanctions Screening
- 14.3 Appraisal Analysis
  - 14.3.1 Value Extraction
  - 14.3.2 Comparable Validation
  - 14.3.3 Condition Assessment
- 14.4 Title Report Analysis
  - 14.4.1 Schedule B-I Requirements
  - 14.4.2 Schedule B-II Exceptions
  - 14.4.3 Lien Analysis
- 14.5 Insurance Certificate Analysis
  - 14.5.1 Coverage Validation
  - 14.5.2 Mortgagee Clause Verification
- 14.6 Feasibility Study Analysis (RTL)
- 14.7 Python: ReportAnalyzer classes

**Analysis Flag Rules (Credit Report):**

| Check | Rule | Flag |
|-------|------|------|
| FICO Score | >= 680 (DSCR), >= 660 (RTL) | Red if below |
| Trade Lines Total | >= 3 | Red if below |
| Active Trade Lines | >= 1 | Red if below |
| 24mo History | >= 1 trade line | Red if none |
| Housing Lates (12mo) | <= 1x30 | Red if exceeded |
| Bankruptcy | None in 3-4 years | Red if found |
| Foreclosure | None in 3-4 years | Red if found |
| Active Judgments | None > $10K | Red if found |
| Report Age | <= 120 days | Red if expired |

**Model Recommendation:** `Opus` - Critical for INSPIRE Phase 7 integration. Must be precise.

**Estimated Output:** ~30 pages + Python code

---

#### Section 15: Credit Memo & Risk Assessment

**Purpose:** Define credit memo structure, content standards, and overall risk assessment framework.

**Contents:**
- 15.1 Credit Memo Structure
  - 15.1.1 Executive Summary
  - 15.1.2 Borrower Analysis Section
  - 15.1.3 Property Analysis Section
  - 15.1.4 Deal Economics Section
  - 15.1.5 Third-Party Summary
  - 15.1.6 Risk Assessment Section
  - 15.1.7 Conditions & Exceptions
- 15.2 Risk Rating Framework
  - 15.2.1 Low Risk Criteria
  - 15.2.2 Moderate Risk Criteria
  - 15.2.3 Elevated Risk Criteria
  - 15.2.4 High Risk Criteria
- 15.3 Recommendation Framework
  - 15.3.1 Approve
  - 15.3.2 Approve with Conditions
  - 15.3.3 Decline
- 15.4 Flag Aggregation & Interpretation
- 15.5 Python: CreditMemoGenerator class

**Risk Rating Matrix:**

| Rating | Criteria |
|--------|----------|
| Low | All green flags; no yellow; FICO > 720; LTV < 70%; experienced borrower |
| Moderate | Some yellow flags; FICO 680-720; LTV 70-75%; adequate experience |
| Elevated | Multiple yellow flags; FICO 660-680; LTV > 75%; limited experience |
| High | Red flags present; exceptions required; significant concerns |

**Model Recommendation:** `Sonnet` - Synthesis and narrative generation.

**Estimated Output:** ~25 pages + Python code

---

#### Section 16: Comprehensive Glossary

**Purpose:** Provide complete glossary of all terms used in underwriting with definitions, formulas, and cross-references.

**Contents:**
- 16.1 Alphabetical Term Reference (200+ terms)
- 16.2 Acronym Reference
- 16.3 Formula Reference
- 16.4 Cross-Reference Index

**Sample Glossary Entries:**

```
ARV (After-Repair Value)
─────────────────────────
Definition: The estimated market value of a property after
completion of all planned renovations and improvements.

Formula: ARV = As-Is Value + Value Created by Improvements

Related Terms: As-Is Value, LTARV, Scope of Work

Usage: "The subject property has an ARV of $485,000 based
on comparable renovated properties in the neighborhood."

Investor Notes:
- EastView: ARV must be supported by 3+ comps within 6 months
- ArchWest: ARV variance >10% triggers resizing
- Churchill: Full appraisal required for ARV >$750K
───────────────────────────────────────────────────────────

DSCR (Debt Service Coverage Ratio)
─────────────────────────────────────
Definition: A measure of a property's ability to cover its
debt obligations from rental income.

Formula: DSCR = Qualifying Monthly Rent / Monthly PITIA

Components:
- Qualifying Rent: Varies by lease status and loan type
- PITIA: Principal + Interest + Taxes + Insurance + Association

Minimum Requirements:
- FICO >= 700: 1.00x
- FICO < 700: 1.20x
- 5-9 Units: 1.20x (NCF basis)
- Foreign National: 1.20x

Related Terms: PITIA, NOI, Cash Flow, Qualifying Rent
───────────────────────────────────────────────────────────
```

**Model Recommendation:** `Haiku` - Reference content compilation. Can be done efficiently.

**Estimated Output:** ~50 pages

---

## 3. Python Library Architecture

### 3.1 Module Structure

```
usdv_underwriting/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── enums.py              # All enumerations (LoanType, BorrowerClass, etc.)
│   ├── models.py             # Data classes (Borrower, Property, Loan, etc.)
│   └── constants.py          # All constants and thresholds
├── borrower/
│   ├── __init__.py
│   ├── classifier.py         # BorrowerClassifier class
│   ├── credit_analyzer.py    # CreditAnalyzer class
│   └── background_checker.py # BackgroundChecker class
├── property/
│   ├── __init__.py
│   ├── eligibility.py        # PropertyEligibilityChecker class
│   ├── rtl_analyzer.py       # RTLPropertyAnalyzer class
│   └── dscr_analyzer.py      # DSCRPropertyAnalyzer class
├── sizing/
│   ├── __init__.py
│   ├── rtl_sizer.py          # RTLSizer class
│   └── dscr_sizer.py         # DSCRSizer class
├── pricing/
│   ├── __init__.py
│   ├── rtl_pricing.py        # RTL pricing calculations
│   ├── dscr_pricing.py       # DSCR pricing with LLPAs
│   └── rate_lock.py          # Rate lock management
├── analysis/
│   ├── __init__.py
│   ├── appraisal.py          # AppraisalAnalyzer class
│   ├── title.py              # TitleAnalyzer class
│   ├── insurance.py          # InsuranceAnalyzer class
│   └── reports.py            # General report analysis
├── diligence/
│   ├── __init__.py
│   ├── checklist.py          # DiligenceChecker class
│   └── flags.py              # Flag generation system
├── memo/
│   ├── __init__.py
│   ├── generator.py          # CreditMemoGenerator class
│   └── risk_rating.py        # Risk assessment
├── exceptions/
│   ├── __init__.py
│   └── manager.py            # ExceptionManager class
└── utils/
    ├── __init__.py
    ├── calculations.py       # Shared calculation utilities
    └── validators.py         # Input validation
```

### 3.2 Key Classes Overview

```python
# Core Data Models
@dataclass
class Borrower:
    name: str
    ssn: str  # Encrypted
    fico: int
    experience_36mo: int
    citizenship: CitizenshipType
    # ... additional fields

@dataclass
class Property:
    address: str
    property_type: PropertyType
    units: int
    square_footage: int
    as_is_value: float
    arv: Optional[float]
    # ... additional fields

@dataclass
class Loan:
    loan_type: LoanType
    purpose: LoanPurpose
    amount: float
    investor: Investor
    # ... additional fields

# Sizing Classes
class RTLSizer:
    """Calculate RTL loan sizing with all leverage constraints."""

    def calculate_borrower_classification(self, borrower: Borrower) -> BorrowerClass:
        """Determine A+/A/B/C classification."""

    def calculate_max_leverage(self, classification: BorrowerClass,
                               loan_type: LoanType, purpose: LoanPurpose) -> LeverageLimits:
        """Get leverage limits by classification and product."""

    def apply_leverage_reductions(self, limits: LeverageLimits,
                                  property: Property) -> LeverageLimits:
        """Apply all leverage reduction factors."""

    def size_loan(self, borrower: Borrower, property: Property,
                  loan_request: LoanRequest) -> SizingResult:
        """Full loan sizing with all constraints."""

class DSCRSizer:
    """Calculate DSCR loan sizing with all constraints."""

    def calculate_dscr(self, property: Property, loan: Loan) -> float:
        """Calculate DSCR from property income and loan terms."""

    def get_ltv_limits(self, borrower: Borrower, purpose: LoanPurpose) -> LTVLimits:
        """Get LTV limits by FICO and purpose."""

    def apply_ltv_adjustments(self, limits: LTVLimits,
                              property: Property, loan: Loan) -> LTVLimits:
        """Apply all LTV adjustments."""

    def size_loan(self, borrower: Borrower, property: Property,
                  loan_request: LoanRequest) -> SizingResult:
        """Full DSCR loan sizing."""

# Pricing Classes
class DSCRPricingEngine:
    """Calculate DSCR loan pricing with all LLPAs."""

    def get_base_rate(self, spread: float, product: DSCRProduct) -> float:
        """Get base rate from spread and product type."""

    def calculate_fico_llpa(self, fico: int, ltv: float) -> float:
        """Calculate FICO-based LLPA."""

    def calculate_all_llpas(self, loan: Loan, borrower: Borrower,
                            property: Property) -> LLPABreakdown:
        """Calculate all applicable LLPAs."""

    def calculate_final_price(self, loan: Loan, borrower: Borrower,
                              property: Property) -> PricingResult:
        """Full pricing calculation with all adjustments."""

# Analysis Classes
class CreditAnalyzer:
    """Analyze credit reports and generate flags."""

    def extract_scores(self, report: CreditReport) -> CreditScores:
        """Extract all credit scores."""

    def analyze_trade_lines(self, report: CreditReport) -> TradeLineAnalysis:
        """Analyze trade line requirements."""

    def analyze_derogatories(self, report: CreditReport) -> DerogatoryAnalysis:
        """Analyze bankruptcy, foreclosure, judgments, etc."""

    def generate_flags(self, report: CreditReport,
                       loan_type: LoanType) -> List[AnalysisFlag]:
        """Generate all analysis flags."""

# Credit Memo Generation
class CreditMemoGenerator:
    """Generate credit memorandum from deal data."""

    def generate_executive_summary(self, deal: Deal) -> ExecutiveSummary:
        """Generate executive summary section."""

    def generate_borrower_analysis(self, deal: Deal) -> BorrowerAnalysis:
        """Generate borrower analysis section."""

    def generate_risk_assessment(self, deal: Deal,
                                 flags: List[AnalysisFlag]) -> RiskAssessment:
        """Generate risk assessment with rating."""

    def generate_full_memo(self, deal: Deal) -> CreditMemo:
        """Generate complete credit memorandum."""
```

### 3.3 Usage Examples

```python
from usdv_underwriting import (
    Borrower, Property, LoanRequest,
    RTLSizer, DSCRSizer, DSCRPricingEngine,
    CreditAnalyzer, CreditMemoGenerator
)

# Example 1: RTL Loan Sizing
borrower = Borrower(
    name="John Smith",
    fico=720,
    experience_36mo=5,
    citizenship=CitizenshipType.US_CITIZEN
)

property = Property(
    property_type=PropertyType.SFR,
    as_is_value=300000,
    arv=450000,
    purchase_price=280000,
    rehab_budget=80000
)

loan_request = LoanRequest(
    loan_type=LoanType.FIX_FLIP,
    purpose=LoanPurpose.PURCHASE,
    investor=Investor.EASTVIEW
)

sizer = RTLSizer()
result = sizer.size_loan(borrower, property, loan_request)

print(f"Borrower Classification: {result.classification}")
print(f"Max As-Is LTV: {result.max_as_is_ltv:.1%}")
print(f"Max LTC: {result.max_ltc:.1%}")
print(f"Max LTARV: {result.max_ltarv:.1%}")
print(f"Initial Loan: ${result.initial_loan:,.0f}")
print(f"Rehab Holdback: ${result.rehab_holdback:,.0f}")
print(f"Total Loan: ${result.total_loan:,.0f}")

# Example 2: DSCR Loan Pricing
pricing_engine = DSCRPricingEngine()
pricing = pricing_engine.calculate_final_price(loan, borrower, property)

print(f"Base Rate: {pricing.base_rate:.3%}")
print(f"Total LLPA: {pricing.total_llpa:.3%}")
print(f"Final Price: {pricing.final_price:.3%}")
print(f"Final Rate: {pricing.final_rate:.3%}")
```

---

## 4. Model Selection by Section

### 4.1 Model Recommendation Summary

| Section | Model | Rationale | Est. Tokens |
|---------|-------|-----------|-------------|
| 1. Investment Philosophy | Sonnet | Synthesis required | 15K |
| 2. Borrower Eligibility | Sonnet | Core logic, moderate complexity | 20K |
| 3. Entity Analysis | Sonnet | Complex structures | 18K |
| 4. Credit & Background | **Opus** | Regulatory precision required | 25K |
| 5. Property Eligibility | Sonnet | Matrix consolidation | 22K |
| 6. RTL Property Analysis | Sonnet | Technical but defined | 24K |
| 7. DSCR Income Analysis | **Opus** | Complex calculations | 28K |
| 8. Appraisal Review | Sonnet | Well-defined criteria | 20K |
| 9. RTL Sizing | **Opus** | Critical calculations | 30K |
| 10. DSCR Sizing | **Opus** | Complex matrices | 28K |
| 11. Pricing & LLPAs | **Opus** | Most complex section | 35K |
| 12. Exception Management | Sonnet | Process content | 18K |
| 13. Document Requirements | Sonnet | Reference content | 22K |
| 14. Report Analysis | **Opus** | INSPIRE integration | 30K |
| 15. Credit Memo | Sonnet | Narrative generation | 25K |
| 16. Glossary | Haiku | Reference compilation | 15K |

### 4.2 Model Usage Summary

| Model | Sections | Rationale |
|-------|----------|-----------|
| **Opus** | 4, 7, 9, 10, 11, 14 | Critical calculations, regulatory content, INSPIRE integration |
| **Sonnet** | 1, 2, 3, 5, 6, 8, 12, 13, 15 | Moderate complexity, synthesis, process documentation |
| **Haiku** | 16 | Reference content, glossary compilation |

### 4.3 Estimated Token Budget

| Model | Sections | Est. Input | Est. Output | Total |
|-------|----------|------------|-------------|-------|
| Opus | 6 sections | ~150K | ~180K | ~330K |
| Sonnet | 9 sections | ~200K | ~200K | ~400K |
| Haiku | 1 section | ~20K | ~15K | ~35K |
| **Total** | 16 sections | ~370K | ~395K | ~765K |

---

## 5. Glossary Structure

### 5.1 Proposed Terms (200+ Entries)

**A (18 terms)**
- Acquisition Fee, Amortization, Appraisal, ARM (Adjustable Rate Mortgage), ARV (After-Repair Value), As-Is Value, Assignment Fee, Asset Management Fee, ATIMA...

**B (15 terms)**
- Background Check, Bankruptcy, Base Rate, BPO (Broker Price Opinion), Bridge Loan, Builder's Risk Insurance, Business Purpose Loan, Buydown...

**C (22 terms)**
- Cap Rate, Cash-Out Refinance, CDA (Collateral Desktop Analysis), Certificate of Good Standing, Closing Costs, Collateral, Collections, Compensating Factors, Condition Rating, Construction Budget, Cost Basis, Credit Exception, Credit Memo, Credit Score...

**D (18 terms)**
- Debt Service, Deed of Trust, Default, Deferred Maintenance, Depreciation, Disbursement, DSCR (Debt Service Coverage Ratio), Draw Schedule, Due Diligence...

**E (14 terms)**
- Easement, EIN, Encumbrance, Entity, Equity, Escrow, Exception Request, Exit Strategy, Experience Requirement, Extension Fee...

**F (16 terms)**
- Feasibility Study, FICO Score, First Lien, Fix & Flip, Flood Certification, Forbearance, Foreclosure, Foreign National, Full Appraisal, Funding...

**G-H (12 terms)**
- Good Standing, Gross Rent, Ground-Up Construction, Guarantor, Hard Money, Heavy Rehab, HO6 Insurance, Holdback, HOA...

**I-J (15 terms)**
- I/O (Interest Only), Impound, Insurance, Interest Rate, Interest Reserve, Investor, ISAOA, ITIN, Judgment, Junior Lien...

**K-L (18 terms)**
- Key Principal, Land Value, Late Fee, Lease, Lender, Lien, Liquidity, LLPA, Loan Amount, Loan-to-ARV, Loan-to-Cost, Loan-to-Value, Lock Period...

**M-N (14 terms)**
- Market Rent, Maturity Date, Mechanic's Lien, Modification, Mortgage, Mortgagee Clause, NCF (Net Cash Flow), NOI, Note Rate...

**O-P (20 terms)**
- OFAC, Operating Agreement, Origination Fee, Ownership Percentage, Payoff, PITIA, Points, Portfolio, Prepayment Penalty, Principal, Property Type, Purchase Price...

**Q-R (14 terms)**
- Qualifying Rent, Rate Lock, Rate Sheet, Recourse, Refinance, Rehab Budget, Rent Roll, Replacement Cost, Reserve Requirements, ROI, RTL...

**S-T (18 terms)**
- Scope of Work, Section 8, Security Deposit, Servicing, Short Sale, Short-Term Rental, Single Source, Sponsor, Spread, Step-Down Prepay, Tax Certificate, Term Sheet, Title Commitment, Trade Lines...

**U-Z (12 terms)**
- UCC Filing, Underwriting, UPB, Vacancy, Variance, Vesting, W-9, Waiver, Warrant, YSP, ZHVI, Zoning...

### 5.2 Glossary Entry Format

```markdown
## TERM NAME (Acronym if applicable)

**Definition:**
Clear, concise definition of the term in the context of single-family
business purpose lending.

**Formula:** (if applicable)
Mathematical formula with variable definitions.

**Example:**
Practical example showing how the term is used.

**Investor-Specific Notes:**
- ArchWest: [Any specific requirements or variations]
- EastView: [Any specific requirements or variations]
- Churchill: [Any specific requirements or variations]

**Related Terms:**
[List of related glossary terms with cross-references]

**INSPIRE Integration:**
[How this term is used within the INSPIRE platform, if applicable]
```

---

## 6. Implementation Timeline

### 6.1 Phase 1: Foundation (Sections 1-4)
**Tasks:**
1. Extract and consolidate investor guidelines
2. Create Section 1: Investment Philosophy
3. Create Section 2: Borrower Eligibility
4. Create Section 3: Entity Analysis
5. Create Section 4: Credit & Background
6. Develop core Python models and enums

**Deliverables:**
- Sections 1-4 complete (~78 pages)
- Python: core/, borrower/ modules

---

### 6.2 Phase 2: Property & Valuation (Sections 5-8)
**Tasks:**
1. Create Section 5: Property Eligibility
2. Create Section 6: RTL Property Analysis
3. Create Section 7: DSCR Income Analysis
4. Create Section 8: Appraisal Review
5. Develop property Python modules

**Deliverables:**
- Sections 5-8 complete (~94 pages)
- Python: property/, analysis/ modules

---

### 6.3 Phase 3: Loan Structuring (Sections 9-12)
**Tasks:**
1. Create Section 9: RTL Sizing
2. Create Section 10: DSCR Sizing
3. Create Section 11: Pricing & LLPAs
4. Create Section 12: Exception Management
5. Develop sizing and pricing Python modules

**Deliverables:**
- Sections 9-12 complete (~111 pages)
- Python: sizing/, pricing/, exceptions/ modules

---

### 6.4 Phase 4: Operations & Reference (Sections 13-16)
**Tasks:**
1. Create Section 13: Document Requirements
2. Create Section 14: Report Analysis
3. Create Section 15: Credit Memo
4. Create Section 16: Glossary
5. Develop memo and diligence Python modules
6. Final integration and testing

**Deliverables:**
- Sections 13-16 complete (~127 pages)
- Python: memo/, diligence/ modules
- Complete glossary (200+ terms)

---

### 6.5 Phase 5: Integration & QA
**Tasks:**
1. Cross-reference all sections
2. Validate Python calculations against investor sizers
3. Test INSPIRE integration points
4. Review by USDV stakeholders
5. Final revisions and formatting

**Deliverables:**
- Complete manual (~410+ pages)
- Validated Python library
- Integration documentation

---

## 7. Dependencies & Prerequisites

### 7.1 Required Documents

| Document | Status | Location |
|----------|--------|----------|
| ArchWest DSCR Guidelines v1.8 | Available | /Investor Underwriting Guidelines/ |
| ArchWest RTL Guidelines | Available | /Investor Underwriting Guidelines/ |
| ArchWest GUC Sizer | Available | /Investor Underwriting Guidelines/ |
| EastView DSCR Guidelines v7.2 | Available | /Investor Underwriting Guidelines/ |
| EastView RTL Guidelines v4.1 | Available | /Investor Underwriting Guidelines/ |
| EastView GUC Guidelines v1.0 | Available | /Investor Underwriting Guidelines/ |
| EastView DSCR S Matrix | Available | /Investor Underwriting Guidelines/ |
| EastView DSCR S Sizer | Available | /Investor Underwriting Guidelines/ |
| Churchill DSCR Guidelines | Available | /Investor Underwriting Guidelines/ |
| Churchill RTL Guidelines | Available | /Investor Underwriting Guidelines/ |
| Churchill Doc List | Available | /Investor Underwriting Guidelines/ |

### 7.2 Access Requirements

- Read access to all investor guideline PDFs
- Ability to extract data from Excel sizers (ArchWest GUC, EastView DSCR)
- INSPIRE PRD files for integration alignment

### 7.3 Stakeholder Input Needed

| Item | From | Purpose |
|------|------|---------|
| USDV Internal Policies | USDV Team | House rules beyond investor guidelines |
| Exception Approval Matrix | USDV Leadership | Authority levels for exceptions |
| Credit Memo Template Approval | USDV Underwriting | Format and content validation |
| YSP/Points Structure | USDV Finance | USDV economics confirmation |

---

## 8. Quality Assurance

### 8.1 Validation Checkpoints

**Guideline Accuracy:**
- Cross-reference every threshold, matrix, and calculation against source investor guidelines
- Document any discrepancies or interpretation decisions
- Flag areas where investor guidelines conflict

**Python Validation:**
- Test all calculations against investor Excel sizers
- Unit tests for each calculation class
- Integration tests for complete sizing scenarios
- Edge case testing (min/max values, boundary conditions)

**INSPIRE Integration:**
- Verify flag rules match Phase 7 PRD specifications
- Validate credit memo structure against PRD template
- Ensure exception request format compatibility

### 8.2 Review Process

1. **Technical Review:** Verify calculations and formulas
2. **Legal/Compliance Review:** Confirm regulatory accuracy
3. **Underwriter Review:** Validate practical application
4. **System Integration Review:** Confirm INSPIRE compatibility

### 8.3 Success Criteria

| Criteria | Target |
|----------|--------|
| Calculation accuracy vs. investor sizers | >99% |
| Guideline coverage | 100% of investor requirements |
| Python test coverage | >90% |
| Glossary completeness | 200+ terms |
| INSPIRE integration points documented | 100% |

---

## Appendix A: File Output Structure

```
USDV_Underwriting_Manual/
├── USDV_UNDERWRITING_MANUAL_COMPLETE.md    # Full compiled manual
├── sections/
│   ├── 01_investment_philosophy.md
│   ├── 02_borrower_eligibility.md
│   ├── 03_entity_analysis.md
│   ├── 04_credit_background.md
│   ├── 05_property_eligibility.md
│   ├── 06_rtl_property_analysis.md
│   ├── 07_dscr_income_analysis.md
│   ├── 08_appraisal_review.md
│   ├── 09_rtl_sizing.md
│   ├── 10_dscr_sizing.md
│   ├── 11_pricing_llpas.md
│   ├── 12_exception_management.md
│   ├── 13_document_requirements.md
│   ├── 14_report_analysis.md
│   ├── 15_credit_memo.md
│   └── 16_glossary.md
├── python/
│   └── usdv_underwriting/
│       ├── [full library structure]
│       └── tests/
└── reference/
    ├── investor_matrices.md
    ├── llpa_tables.md
    └── quick_reference.md
```

---

## Appendix B: Questions for Clarification

Before proceeding with implementation, the following clarifications would be helpful:

1. **USDV-Specific Policies:**
   - Are there any USDV internal policies that override or supplement investor guidelines?
   - What are USDV's default origination points and YSP structures?

2. **Investor Prioritization:**
   - When investor guidelines conflict, which investor's guidelines take precedence?
   - Is there a primary investor for each loan type?

3. **Exception Authority:**
   - What is the approval matrix for exceptions (USDV internal vs. investor required)?
   - Are there any exceptions USDV will not pursue regardless of investor approval?

4. **Credit Memo Format:**
   - Should the credit memo follow the ~6-page structure from Phase 7 PRD exactly?
   - Are there additional sections needed for USDV's internal use?

5. **Python Library Deployment:**
   - Will the Python library be integrated directly into INSPIRE's backend?
   - Should the library be designed for standalone use as well?

---

*End of Implementation Plan*

**Next Steps:**
1. Review and approve this implementation plan
2. Clarify questions in Appendix B
3. Begin Phase 1 implementation

**Awaiting your approval to proceed.**
