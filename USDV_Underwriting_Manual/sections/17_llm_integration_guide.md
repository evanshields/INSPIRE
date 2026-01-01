---
section: 17
title: LLM Integration Guide
version: 1.0
last_updated: 2025-12-30
model_used: opus
purpose: Structured rules for AI/LLM systems in INSPIRE
changelog:
  - 2025-12-30: Initial creation
---

# Section 17: LLM Integration Guide

## 17.1 Purpose & Scope

This section provides **structured, machine-parseable rules** for LLM systems operating within INSPIRE. While other sections of this manual are written for human underwriters, this section is optimized for consistent AI decision-making.

**Use Cases:**
- Document analysis and red/green flag generation
- Automated exception identification
- Credit memo generation
- Data validation and completeness checks
- Eligibility pre-screening

**Key Principle:** Rules in this section use explicit IF/THEN logic with exact thresholds. When in doubt, the LLM should flag for human review rather than make assumptions.

---

## 17.2 Loan Eligibility Decision Rules

### 17.2.1 Hard Stops (Automatic Decline)

These conditions result in immediate ineligibility with no exception path:

```yaml
HARD_STOPS:
  - condition: "state IN ['ND', 'SD', 'AK', 'HI']"
    flag: RED
    message: "Property located in ineligible state: {state}"
    action: DECLINE

  - condition: "property_type == 'manufactured'"
    flag: RED
    message: "Manufactured homes are not eligible"
    action: DECLINE

  - condition: "fico < 660"
    flag: RED
    message: "FICO {fico} below absolute minimum 660"
    action: DECLINE

  - condition: "loan_amount < 100000"
    flag: RED
    message: "Loan amount ${loan_amount} below minimum $100,000"
    action: DECLINE

  - condition: "loan_amount > 3000000 AND no_exception_approved"
    flag: RED
    message: "Loan amount ${loan_amount} exceeds maximum $3,000,000"
    action: DECLINE_OR_EXCEPTION

  - condition: "is_rural == true"
    flag: RED
    message: "Rural properties are not eligible"
    action: DECLINE

  - condition: "hpa_decline < -0.10"
    flag: RED
    message: "HPA decline {hpa_decline}% exceeds -10% threshold"
    action: DECLINE

  - condition: "zhvi_multiplier > 3.0"
    flag: RED
    message: "ZHVI multiplier {zhvi_multiplier}x exceeds 300%"
    action: DECLINE
```

### 17.2.2 RTL Eligibility Rules

```yaml
RTL_ELIGIBILITY:
  products: [FIX_AND_FLIP, BRIDGE, BRIDGE_PLUS, GUC]

  borrower_rules:
    - rule: "FICO minimum"
      condition: "fico >= 660"
      flag_if_false: RED
      message: "RTL requires minimum FICO 660"

    - rule: "Experience for first-time"
      condition: "deals_36mo >= 1 OR (fico >= 700 AND liquidity_months >= 12)"
      flag_if_false: YELLOW
      message: "First-time investor requires FICO 700+ and 12mo reserves"

    - rule: "Guarantor requirement"
      condition: "guarantor_ownership_pct >= 51"
      flag_if_false: RED
      message: "Guarantor must own at least 51% of entity"

  classification_rules:
    credit_decision_score:
      - condition: "fico >= 700"
        points: 3
      - condition: "fico >= 680 AND fico < 700"
        points: 1
      - condition: "fico < 680 OR is_foreign_national"
        points: 0

    experience_score:
      - condition: "deals_36mo >= 10"
        points: 7
      - condition: "deals_36mo >= 3 AND deals_36mo < 10"
        points: 5
      - condition: "deals_36mo < 3"
        points: 1

    classification:
      - condition: "total_score >= 7"
        class: "A+"
      - condition: "total_score >= 5 AND total_score < 7"
        class: "A"
      - condition: "total_score >= 2 AND total_score < 5"
        class: "B"
      - condition: "total_score < 2"
        class: "C"
```

### 17.2.3 DSCR Eligibility Rules

```yaml
DSCR_ELIGIBILITY:
  products: [DSCR, DSCR_5_9]

  borrower_rules:
    - rule: "FICO minimum"
      condition: "fico >= 660"
      flag_if_false: RED
      message: "DSCR requires minimum FICO 660"

    - rule: "Standard FICO"
      condition: "fico >= 680"
      flag_if_false: YELLOW
      message: "FICO 660-679 eligible but with reduced leverage (70% max)"

  fico_tier_mapping:
    - range: "780+"
      tier: 1
      base_ltv_purchase: 0.80
      base_ltv_rt_refi: 0.80
      base_ltv_cashout: 0.80

    - range: "760-779"
      tier: 2
      base_ltv_purchase: 0.80
      base_ltv_rt_refi: 0.80
      base_ltv_cashout: 0.80

    - range: "740-759"
      tier: 3
      base_ltv_purchase: 0.80
      base_ltv_rt_refi: 0.80
      base_ltv_cashout: 0.80

    - range: "720-739"
      tier: 4
      base_ltv_purchase: 0.80
      base_ltv_rt_refi: 0.80
      base_ltv_cashout: 0.80

    - range: "700-719"
      tier: 5
      base_ltv_purchase: 0.80
      base_ltv_rt_refi: 0.80
      base_ltv_cashout: 0.75

    - range: "680-699"
      tier: 6
      base_ltv_purchase: 0.75
      base_ltv_rt_refi: 0.75
      base_ltv_cashout: 0.70

    - range: "660-679"
      tier: 7
      base_ltv_purchase: 0.70
      base_ltv_rt_refi: 0.70
      base_ltv_cashout: 0.65

    - range: "FN"
      tier: "FN"
      base_ltv_purchase: 0.70
      base_ltv_rt_refi: 0.70
      base_ltv_cashout: 0.65

  dscr_minimums:
    - condition: "is_foreign_national == true"
      min_dscr: 1.20

    - condition: "fico < 700"
      min_dscr: 1.20
      note: "Exception-based; may be waived with compensating factors"

    - condition: "default"
      min_dscr: 1.00
```

---

## 17.3 Leverage Adjustment Rules

### 17.3.1 RTL Leverage Reductions

```yaml
RTL_LEVERAGE_REDUCTIONS:
  - condition: "is_heavy_rehab AND classification IN ['A+', 'A', 'B']"
    reduction: 0.05
    applies_to: [as_is_ltv, ltc, ltarv]
    message: "Heavy rehab reduction (Class A/B): -5%"

  - condition: "is_heavy_rehab AND classification == 'C'"
    reduction: 0.10
    applies_to: [as_is_ltv, ltc, ltarv]
    message: "Heavy rehab reduction (Class C): -10%"

  - condition: "hpa_decline >= -0.10 AND hpa_decline < 0"
    reduction: 0.05
    applies_to: [as_is_ltv, ltc, ltarv]
    message: "HPA decline {hpa_decline}%: -5%"

  - condition: "zhvi_multiplier >= 2.0 AND zhvi_multiplier <= 3.0"
    reduction: 0.05
    applies_to: [as_is_ltv, ltc, ltarv]
    message: "ZHVI multiplier {zhvi_multiplier}x: -5%"

  - condition: "loan_amount >= 2000000 AND loan_amount <= 3000000"
    reduction: 0.05
    applies_to: [as_is_ltv, ltc, ltarv]
    message: "High loan amount: -5%"

  - condition: "units >= 5 AND units <= 9 AND product != 'GUC'"
    reduction: 0.05
    applies_to: [as_is_ltv, ltc, ltarv]
    message: "5-9 unit RTL: -5%"

  - condition: "units >= 5 AND units <= 9 AND product == 'GUC'"
    reduction: 0.10
    applies_to: [as_is_ltv, ltc, ltarv]
    message: "5-9 unit GUC: -10%"

HEAVY_REHAB_DEFINITION:
  condition: "rehab_budget > 50000 AND rehab_budget > comparison_value"
  comparison_value_purchase: "purchase_price"
  comparison_value_refinance: "as_is_value"
```

### 17.3.2 DSCR Leverage Reductions

```yaml
DSCR_LEVERAGE_REDUCTIONS:
  - condition: "is_refinance AND NOT is_leased"
    reduction: 0.10
    message: "Unleased refinance: -10%"

  - condition: "property_type == 'condo_non_warrantable'"
    reduction: 0.10
    message: "Non-warrantable condo: -10%"

  - condition: "units >= 5 AND units <= 9"
    reduction: 0.05
    message: "5-9 units: -5%"
    max_ltv_cap: 0.75

  - condition: "market IN ['Chicago', 'Detroit', 'Baltimore', 'Flint']"
    reduction: 0.05
    message: "High-risk market ({market}): -5%"

  - condition: "rental_type == 'STR'"
    reduction: 0.05
    message: "Short-term rental: -5%"

  - condition: "rental_type == 'Section8'"
    reduction: 0.05
    message: "Section 8/subsidized: -5%"

  - condition: "loan_amount > 1000000"
    reduction: 0.10
    message: "Luxury rental (>$1M): -10%"
    additional_requirement: "dscr >= 1.20 AND lease_term >= 12"

DSCR_LEVERAGE_INCREASES:
  - condition: "fico >= 700 AND fico <= 719 AND dscr >= 1.20"
    increase: 0.05
    message: "700-719 FICO with DSCR >= 1.20x: +5%"

  - condition: "is_foreign_national AND dscr >= 1.30"
    increase: 0.05
    message: "Foreign National with DSCR >= 1.30x: +5%"
```

---

## 17.4 Document Analysis Flag Criteria

### 17.4.1 Credit Report Flags

```yaml
CREDIT_REPORT_FLAGS:
  red_flags:
    - condition: "fico < 660"
      message: "FICO {fico} below minimum 660"

    - condition: "bankruptcy_years < 4"
      message: "Bankruptcy within 4 years (discharged {bankruptcy_date})"

    - condition: "foreclosure_years < 2"
      message: "Foreclosure within 2 years"

    - condition: "active_fraud_alert"
      message: "Active fraud alert on credit file"

    - condition: "judgment_amount > 15000 AND NOT remedied"
      message: "Unresolved judgment over $15,000"

  yellow_flags:
    - condition: "fico >= 660 AND fico < 680"
      message: "FICO {fico} below standard minimum 680"

    - condition: "bankruptcy_years >= 4 AND bankruptcy_years < 7"
      message: "Bankruptcy 4-7 years ago - monitor"

    - condition: "mortgage_late_12mo > 0"
      message: "Mortgage delinquency in last 12 months: {mortgage_late_12mo}x30"

    - condition: "collections_count > 3"
      message: "Multiple collections ({collections_count})"

    - condition: "inquiry_count_6mo > 10"
      message: "Excessive inquiries ({inquiry_count_6mo} in 6 months)"

  green_indicators:
    - condition: "fico >= 720"
      message: "Strong credit score: {fico}"

    - condition: "mortgage_history_clean AND years >= 2"
      message: "Clean mortgage history 24+ months"
```

### 17.4.2 Appraisal Report Flags

```yaml
APPRAISAL_FLAGS:
  red_flags:
    - condition: "age_days > 120"
      message: "Appraisal expired ({age_days} days old, max 120)"

    - condition: "condition_rating == 'C6'"
      message: "Condition C6 - substantial damage/deferred maintenance"

    - condition: "secondary_value_variance > 0.10 AND secondary_value < primary_value"
      message: "Secondary valuation {variance}% below appraisal"
      action: "Use lesser value"

    - condition: "is_rural == true"
      message: "Property classified as rural in appraisal"

    - condition: "square_footage < min_square_footage"
      message: "Square footage {sq_ft} below minimum {min_sq_ft}"

  yellow_flags:
    - condition: "condition_rating == 'C5'"
      message: "Condition C5 - obvious deferred maintenance"

    - condition: "age_days > 90 AND age_days <= 120"
      message: "Appraisal aging ({age_days} days) - verify before closing"

    - condition: "comp_distance_miles > 1"
      message: "Comparable sales beyond 1 mile"

    - condition: "comp_age_months > 6"
      message: "Comparable sales older than 6 months"

    - condition: "arv_variance > 0.15"
      message: "ARV variance from comps exceeds 15%"

  validation_rules:
    - check: "appraiser_license_valid"
      message: "Verify appraiser state certification"

    - check: "form_type_correct"
      sfr: ["1004", "1004C", "2055"]
      multifamily: ["1025"]
      condo: ["1073"]

    - check: "photos_complete"
      required: ["front", "rear", "street", "kitchen", "bathrooms", "all_bedrooms"]
```

### 17.4.3 Title Report Flags

```yaml
TITLE_FLAGS:
  red_flags:
    - condition: "existing_liens > 0"
      message: "Existing liens found: {lien_count}"
      action: "Require payoff or subordination"

    - condition: "property_ownership != borrowing_entity"
      message: "Title holder '{title_owner}' does not match borrower '{borrower}'"

    - condition: "active_litigation"
      message: "Property involved in active litigation"

    - condition: "zoning_violation AND NOT resolvable_at_closing"
      message: "Unresolved zoning violation"

    - condition: "tax_liens > 0"
      message: "Tax liens on property"

    - condition: "ownership_type != 'fee_simple'"
      message: "Property is not fee simple (leasehold not permitted)"

  yellow_flags:
    - condition: "easements_present"
      message: "Easements on property - review for impact"

    - condition: "hoa_delinquency > 0"
      message: "HOA dues in arrears: ${hoa_delinquency}"

    - condition: "special_assessments_pending"
      message: "Pending special assessments"

  validation_rules:
    - check: "alta_form_type"
      required: ["ALTA 2006", "ALTA Short Form"]

    - check: "coverage_amount"
      minimum: "loan_amount"
```

### 17.4.4 Insurance Certificate Flags

```yaml
INSURANCE_FLAGS:
  red_flags:
    - condition: "coverage_amount < loan_amount AND coverage_amount < replacement_cost"
      message: "Insufficient coverage: ${coverage} (need ${required})"

    - condition: "policy_expired OR effective_date > closing_date"
      message: "Policy not in effect at closing"

    - condition: "mortgagee_clause_missing"
      message: "Mortgagee clause not present or incorrect"

    - condition: "in_flood_zone AND no_flood_insurance"
      message: "Property in flood zone without flood coverage"

  yellow_flags:
    - condition: "expiration_days < 90 AND purpose == 'refinance'"
      message: "Policy expires in {expiration_days} days"

    - condition: "deductible > 10000"
      message: "High deductible: ${deductible}"

  validation_rules:
    - check: "coverage_minimum"
      value: "MIN(replacement_cost, loan_amount)"

    - check: "mortgagee_clause"
      required_text: "ISAOA/ATIMA"

    - check: "named_insured"
      must_match: "borrowing_entity"
```

### 17.4.5 Lease Agreement Flags

```yaml
LEASE_FLAGS:
  red_flags:
    - condition: "is_related_party"
      message: "Related party lease - not arm's length"

    - condition: "lease_term_years > 3"
      message: "Lease term exceeds 3 years"

    - condition: "has_purchase_option"
      message: "Lease contains purchase option"

    - condition: "is_commercial_tenant"
      message: "Commercial tenant not permitted"

    - condition: "is_single_room_occupancy"
      message: "SRO leases not permitted"

  yellow_flags:
    - condition: "rent_vs_market > 1.05"
      message: "In-place rent {in_place} exceeds 105% of market {market}"
      action: "Cap at 105% market for qualifying"

    - condition: "lease_remaining_months < 6"
      message: "Lease expires in {remaining} months"

    - condition: "is_month_to_month AND tenure_months < 6"
      message: "Month-to-month with less than 6 months tenure"

  validation_rules:
    - check: "arm_length_certification"
      required: true

    - check: "tenant_name_on_lease"
      required: true

    - check: "rent_amount_clear"
      required: true
```

---

## 17.5 Exception Identification Matrix

### 17.5.1 Exception Tier Classification

```yaml
EXCEPTION_TIERS:
  tier_1_internal:
    approval_authority: "Underwriter"
    description: "Minor deviations with strong compensating factors"
    examples:
      - "FICO 655-659 with 10+ deals experience"
      - "Document 5-10 days past currency"
      - "Minor title clouds resolvable at closing"
    auto_approve_conditions:
      - "compensating_factor_score >= 3"
      - "risk_rating <= 'moderate'"

  tier_2_manager:
    approval_authority: "Underwriting Manager"
    description: "Moderate deviations requiring senior review"
    examples:
      - "LTV 1-5% above guideline with DSCR > 1.25x"
      - "Bankruptcy 3-4 years (vs 4 year requirement)"
      - "First-time investor on larger deal"
    escalate_conditions:
      - "deviation_from_guideline > 5%"
      - "multiple_yellow_flags >= 3"

  tier_3_investor:
    approval_authority: "Investor"
    description: "Significant deviations requiring capital partner approval"
    examples:
      - "Loan amount $3M-$4.5M (above standard max)"
      - "Non-warrantable condo for DSCR"
      - "Property condition C5"
    escalate_conditions:
      - "loan_amount > 3000000"
      - "property_type_restricted"
      - "condition_rating == 'C5'"

  tier_4_not_approvable:
    approval_authority: "None"
    description: "Hard declines - no exception path"
    examples:
      - "FICO below 660"
      - "Ineligible state"
      - "Rural property"
      - "Manufactured home"
```

### 17.5.2 Compensating Factors Scoring

```yaml
COMPENSATING_FACTORS:
  strong_factors:
    - factor: "dscr >= 1.30"
      points: 2
      message: "Strong DSCR of {dscr}x"

    - factor: "ltv <= guideline_ltv - 0.10"
      points: 2
      message: "LTV 10%+ below maximum"

    - factor: "liquidity_months >= 12"
      points: 2
      message: "12+ months liquidity reserves"

    - factor: "deals_36mo >= 10"
      points: 2
      message: "Institutional-level experience (10+ deals)"

    - factor: "repeat_borrower AND prior_loans_performing"
      points: 2
      message: "Repeat borrower with clean payment history"

  moderate_factors:
    - factor: "fico >= 740"
      points: 1
      message: "Strong credit score {fico}"

    - factor: "dscr >= 1.15 AND dscr < 1.30"
      points: 1
      message: "Solid DSCR of {dscr}x"

    - factor: "deals_36mo >= 5"
      points: 1
      message: "Experienced investor (5+ deals)"

    - factor: "property_condition IN ['C1', 'C2']"
      points: 1
      message: "Excellent property condition"

  exception_approval_threshold:
    tier_1: 3  # 3+ points auto-approve
    tier_2: 5  # 5+ points recommend approve
```

---

## 17.6 Credit Memo Structure

### 17.6.1 Required Sections

```yaml
CREDIT_MEMO_STRUCTURE:
  header:
    required_fields:
      - deal_name
      - loan_number
      - date_prepared
      - prepared_by
      - loan_product
      - investor_target

  section_1_executive_summary:
    format: "2-3 sentence deal overview"
    include:
      - loan_amount
      - property_address
      - loan_purpose
      - key_strength
      - key_risk

  section_2_borrower_analysis:
    subsections:
      - borrower_background
      - credit_analysis
      - experience_summary
      - liquidity_verification
      - entity_structure
    flags_to_highlight:
      - credit_flags
      - background_flags

  section_3_property_analysis:
    subsections:
      - property_description
      - valuation_summary
      - condition_assessment
      - market_analysis
      - comparable_analysis
    flags_to_highlight:
      - appraisal_flags
      - title_flags

  section_4_deal_structure:
    subsections:
      - loan_terms
      - sizing_analysis
      - ltv_calculation
      - dscr_calculation  # DSCR only
      - cost_basis  # RTL only
      - rehab_analysis  # Fix & Flip only

  section_5_risk_assessment:
    required_elements:
      - strengths: "minimum 3"
      - risks: "minimum 2"
      - mitigants: "for each risk"

  section_6_exceptions:
    include_if: "exceptions_present"
    format:
      - exception_description
      - guideline_requirement
      - actual_value
      - compensating_factors
      - recommendation

  section_7_recommendation:
    options:
      - "APPROVE"
      - "APPROVE WITH CONDITIONS"
      - "DECLINE"
      - "ESCALATE TO [AUTHORITY]"
    required: "justification paragraph"
```

### 17.6.2 Flag Summary Format

```yaml
FLAG_SUMMARY_FORMAT:
  display_order:
    1: RED
    2: YELLOW
    3: GREEN

  red_flag_format:
    icon: "[RED]"
    template: "{category}: {message}"
    action_required: true

  yellow_flag_format:
    icon: "[YELLOW]"
    template: "{category}: {message}"
    action_required: false
    monitoring: true

  green_indicator_format:
    icon: "[GREEN]"
    template: "{category}: {message}"
    highlight_as_strength: true
```

---

## 17.7 Validation Schemas

### 17.7.1 Loan Request Validation

```yaml
LOAN_REQUEST_SCHEMA:
  borrower:
    fico:
      type: integer
      minimum: 300
      maximum: 850
      required: true

    is_foreign_national:
      type: boolean
      required: true

    deals_36mo:
      type: integer
      minimum: 0
      required_for: [RTL]

    citizenship:
      type: enum
      values: [US_CITIZEN, PERMANENT_RESIDENT, NON_PERMANENT_RESIDENT, FOREIGN_NATIONAL]
      required: true

  property:
    property_type:
      type: enum
      values: [SFR, TOWNHOME, PUD, CONDO_WARRANTABLE, CONDO_NON_WARRANTABLE, TWO_TO_FOUR_UNIT, FIVE_TO_NINE_UNIT]
      required: true

    state:
      type: string
      length: 2
      required: true
      validate: "NOT IN ['ND', 'SD', 'AK', 'HI']"

    square_footage:
      type: number
      minimum: 500
      required: true

    units:
      type: integer
      minimum: 1
      maximum: 9
      required: true

    as_is_value:
      type: number
      minimum: 0
      required: true

    arv:
      type: number
      minimum: 0
      required_for: [FIX_AND_FLIP, GUC]

  loan:
    loan_product:
      type: enum
      values: [FIX_AND_FLIP, BRIDGE, BRIDGE_PLUS, GUC, DSCR, DSCR_5_9]
      required: true

    loan_purpose:
      type: enum
      values: [PURCHASE, RATE_TERM_REFINANCE, CASH_OUT_REFINANCE, DELAYED_PURCHASE]
      required: true

    requested_amount:
      type: number
      minimum: 100000
      maximum: 4500000
      required: true
```

### 17.7.2 Document Completeness Validation

```yaml
DOCUMENT_CHECKLIST:
  rtl_purchase:
    required:
      - purchase_contract
      - appraisal
      - credit_report
      - background_check
      - entity_documents
      - insurance_certificate
      - title_commitment
      - bank_statements_2mo
      - track_record
      - photo_id

    conditional:
      - condition: "product == 'FIX_AND_FLIP'"
        documents: [rehab_budget, feasibility_study]
        feasibility_required_if: "rehab_budget > 150000 OR is_conversion"

      - condition: "is_condo"
        documents: [condo_questionnaire]

  dscr_purchase:
    required:
      - purchase_contract
      - appraisal_with_1007
      - credit_report
      - background_check
      - entity_documents
      - insurance_certificate
      - title_commitment
      - bank_statements_2mo
      - photo_id

    conditional:
      - condition: "is_leased"
        documents: [lease_agreement]

      - condition: "rental_type == 'STR'"
        documents: [str_income_statement, property_management_agreement, online_listing_proof]

      - condition: "is_condo"
        documents: [condo_questionnaire]

  currency_requirements:
    appraisal:
      max_age_days: 120
      from_date: "note_date"

    credit_report:
      max_age_days: 120
      from_date: "note_date"

    bank_statements:
      max_age_days: 90
      from_date: "application_date"

    good_standing:
      max_age_days: 90
      from_date: "closing_date"
```

---

## 17.8 Response Format Standards

### 17.8.1 Eligibility Check Response

```yaml
ELIGIBILITY_RESPONSE:
  format:
    is_eligible: boolean
    loan_product: string

    if_eligible:
      max_loan_amount: number
      max_ltv: number
      classification: string  # RTL only
      fico_tier: string  # DSCR only
      dscr: number  # DSCR only
      binding_constraint: enum [LTV, DSCR, BOTH]

    flags:
      red: array[{category, message, action}]
      yellow: array[{category, message}]
      green: array[{category, message}]

    exceptions_required: array[{exception_type, tier, description}]

    if_ineligible:
      decline_reasons: array[string]
      nearest_eligible_scenario: object  # Optional suggestion
```

### 17.8.2 Document Analysis Response

```yaml
DOCUMENT_ANALYSIS_RESPONSE:
  format:
    document_type: string
    document_date: date
    is_current: boolean
    days_until_expiry: number

    extracted_data:
      # Document-type specific fields

    flags:
      red: array[{field, value, threshold, message}]
      yellow: array[{field, value, threshold, message}]
      green: array[{field, value, message}]

    validation_errors: array[{field, error}]

    missing_information: array[string]

    confidence_score: number  # 0-1
    requires_human_review: boolean
    review_reason: string
```

---

## 17.9 Error Handling Guidelines

### 17.9.1 When to Flag for Human Review

```yaml
HUMAN_REVIEW_TRIGGERS:
  always_escalate:
    - "Confidence score < 0.80 on document extraction"
    - "Conflicting information between documents"
    - "Data validation errors that cannot be resolved"
    - "Edge cases not explicitly covered in rules"
    - "Multiple tier-2+ exceptions on single deal"

  never_auto_approve:
    - "Any red flag present"
    - "Loan amount > $2M without manager review"
    - "Foreign national borrowers"
    - "Non-warrantable condos"
    - "5-9 unit properties"

  request_clarification:
    - "Ambiguous document content"
    - "Missing required fields"
    - "Date discrepancies"
    - "Name mismatches (may be valid - verify)"
```

### 17.9.2 Confidence Scoring

```yaml
CONFIDENCE_SCORING:
  document_extraction:
    high: 0.90+  # Proceed with extracted data
    medium: 0.70-0.89  # Flag for verification
    low: <0.70  # Require human review

  eligibility_determination:
    definitive: "All rules clearly pass or fail"
    conditional: "Passes with exceptions identified"
    uncertain: "Edge cases require human judgment"

  response_behavior:
    high_confidence: "Provide recommendation"
    medium_confidence: "Provide analysis with caveats"
    low_confidence: "Flag for human review without recommendation"
```

---

## 17.10 Quick Reference Lookups

### 17.10.1 Property Eligibility Quick Check

```yaml
PROPERTY_ELIGIBILITY_QUICK:
  eligible_types:
    SFR: {min_sqft: 600, all_products: true}
    TOWNHOME: {min_sqft: 600, exclude: [GUC]}
    PUD: {min_sqft: 600, all_products: true}
    CONDO_W: {min_sqft: 500, exclude: [GUC]}
    CONDO_NW: {min_sqft: 500, products: [FIX_AND_FLIP, BRIDGE], requires_exception: [DSCR]}
    2_4_UNIT: {min_sqft_per_unit: 500, all_products: true}
    5_9_UNIT: {min_sqft_per_unit: 500, products: [DSCR_5_9, FIX_AND_FLIP]}

  ineligible_always:
    - MANUFACTURED
    - RAW_LAND
    - COMMERCIAL
    - MIXED_USE_MAJORITY_COMMERCIAL

  ineligible_states: [ND, SD, AK, HI]

  max_acreage: 5

  rural_eligible: false
```

### 17.10.2 DSCR Qualifying Rent Quick Reference

```yaml
QUALIFYING_RENT_QUICK:
  leased_purchase:
    formula: "MIN(in_place_rent, 105% * market_rent)"

  leased_refinance:
    formula: "MIN(in_place_rent, 105% * market_rent)"

  unleased_purchase:
    formula: "100% * market_rent"

  unleased_refinance:
    formula: "100% * market_rent"
    ltv_reduction: 0.10

  str:
    formula: "MIN(125% * market_rent, trailing_12mo_avg)"
    ltv_reduction: 0.05

  section_8:
    formula: "contract_rent"
    ltv_reduction: 0.05
```

---

## 17.11 Version Control

```yaml
RULES_VERSION:
  version: "1.0.0"
  effective_date: "2025-12-30"
  manual_reference: "USDV Underwriting Manual v1.0"

  change_log:
    - version: "1.0.0"
      date: "2025-12-30"
      changes:
        - "Initial LLM integration guide"
        - "Structured rules from Sections 1-16"
        - "EastView standards for DSCR"
        - "ArchWest standards for RTL"
```

---

*Section 17 - LLM Integration Guide*
*USDV Underwriting Manual v1.0*
*For INSPIRE AI System Use*
