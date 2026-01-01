"""
USDV Underwriting Library - Usage Examples
==========================================

This file demonstrates how to use the unified underwriting library
for both RTL and DSCR loan products.

Run with: python examples.py
"""

from usdv_underwriting import (
    # RTL
    RTLSizer, BorrowerClassifier, LoanProduct, LoanPurpose,
    quick_classification, quick_max_ltv,
    # DSCR
    DSCRCalculator, DSCRSizer, RentalType,
    quick_dscr_check, size_dscr_loan, calculate_max_loan_from_dscr,
    # Property
    PropertyEligibilityChecker, PropertyType,
    check_property_eligible, check_condo_warrantable,
    # Common
    ConditionRating,
)


def example_rtl_classification():
    """Example: Borrower classification for RTL loans."""
    print("\n" + "="*60)
    print("EXAMPLE 1: RTL Borrower Classification")
    print("="*60)

    classifier = BorrowerClassifier()

    # Example 1: Experienced investor with good credit
    result = classifier.classify_borrower(
        fico=725,
        deals_36mo=12,
        is_foreign_national=False
    )

    print(f"\nBorrower 1: FICO 725, 12 deals in 36 months")
    print(f"  Credit Decision Score: {result.credit_decision_score} points")
    print(f"  Experience Score: {result.experience_score} points")
    print(f"  Total Score: {result.total_score} points")
    print(f"  Classification: {result.classification.value}")

    # Example 2: Less experienced investor
    result2 = classifier.classify_borrower(
        fico=695,
        deals_36mo=2,
        is_foreign_national=False
    )

    print(f"\nBorrower 2: FICO 695, 2 deals in 36 months")
    print(f"  Classification: {result2.classification.value}")

    # Quick classification
    quick = quick_classification(720, 5)
    print(f"\nQuick lookup (FICO 720, 5 deals): {quick}")


def example_rtl_sizing():
    """Example: RTL loan sizing."""
    print("\n" + "="*60)
    print("EXAMPLE 2: RTL Loan Sizing (Fix & Flip Purchase)")
    print("="*60)

    sizer = RTLSizer()

    result = sizer.size_loan(
        # Borrower
        fico=720,
        deals_36mo=8,
        is_foreign_national=False,
        # Property
        as_is_value=350000,
        arv=450000,
        units=1,
        # Deal
        product=LoanProduct.FIX_AND_FLIP,
        purpose=LoanPurpose.PURCHASE,
        purchase_price=340000,
        closing_costs=8000,
        assignment_fee=0,
        rehab_budget=60000,
        completed_rehab=0,
        # Market
        hpa_decline=0.0,
        zhvi_multiplier=1.2
    )

    print(f"\nProperty: As-Is $350,000, ARV $450,000")
    print(f"Purchase Price: $340,000, Rehab Budget: $60,000")
    print(f"\nResults:")
    print(f"  Borrower Classification: {result.borrower_classification.classification.value}")
    print(f"  Max As-Is LTV: {result.leverage_limits.max_as_is_ltv:.1%}")
    print(f"  Max LTC: {result.leverage_limits.max_ltc:.1%}")
    print(f"  Max LTARV: {result.leverage_limits.max_ltarv:.1%}")
    print(f"\n  Initial Loan Amount: ${result.initial_loan_amount:,.0f}")
    print(f"  Rehab Holdback: ${result.rehab_holdback:,.0f}")
    print(f"  Total Loan Amount: ${result.total_loan_amount:,.0f}")
    print(f"\n  Actual As-Is LTV: {result.actual_as_is_ltv:.1%}")
    print(f"  Actual LTARV: {result.actual_ltarv:.1%}")
    print(f"  Binding Constraint: {result.binding_constraint}")
    print(f"  Eligible: {result.is_eligible}")


def example_dscr_calculation():
    """Example: DSCR calculation."""
    print("\n" + "="*60)
    print("EXAMPLE 3: DSCR Calculation")
    print("="*60)

    calc = DSCRCalculator()

    # Calculate DSCR for a leased property
    result = calc.analyze_dscr(
        # Property income
        market_rent=2500,
        in_place_rent=2400,
        is_leased=True,
        rental_type=RentalType.LONG_TERM,
        # Loan terms
        loan_amount=320000,
        interest_rate=0.0725,
        loan_term_months=360,
        is_interest_only=False,
        # Expenses
        annual_taxes=4800,
        annual_insurance=1800,
        monthly_hoa=150,
        # Loan details
        loan_purpose=LoanPurpose.PURCHASE,
        # Borrower
        fico=720,
        is_foreign_national=False
    )

    print(f"\nProperty: Leased at $2,400/mo, Market rent $2,500/mo")
    print(f"Loan: $320,000 at 7.25%, 30-year amortizing")
    print(f"\nResults:")
    print(f"  Qualifying Rent: ${result.qualifying_rent:,.0f}")
    print(f"  Method: {result.rent_breakdown.calculation_method}")
    print(f"\n  Monthly PITIA: ${result.monthly_pitia:,.0f}")
    print(f"    - P&I: ${result.pitia_breakdown.principal + result.pitia_breakdown.interest:,.0f}")
    print(f"    - Taxes: ${result.pitia_breakdown.taxes:,.0f}")
    print(f"    - Insurance: ${result.pitia_breakdown.insurance:,.0f}")
    print(f"    - HOA: ${result.pitia_breakdown.association:,.0f}")
    print(f"\n  DSCR: {result.dscr:.3f}x")
    print(f"  Minimum Required: {result.min_dscr_required:.2f}x")
    print(f"  Meets Minimum: {result.meets_minimum}")

    # Quick DSCR check
    dscr, meets, status = quick_dscr_check(2400, 2000, fico=720)
    print(f"\nQuick Check: {status}")


def example_dscr_sizing():
    """Example: DSCR loan sizing with dual constraints."""
    print("\n" + "="*60)
    print("EXAMPLE 4: DSCR Loan Sizing (Dual Constraint)")
    print("="*60)

    sizer = DSCRSizer()

    result = sizer.size_loan(
        # Property
        property_value=400000,
        property_type=PropertyType.SFR,
        units=1,
        is_leased=True,
        rental_type=RentalType.LONG_TERM,
        market="Houston",
        # Income
        market_rent=2500,
        in_place_rent=2400,
        # Expenses
        annual_taxes=5000,
        annual_insurance=2000,
        monthly_hoa=0,
        # Loan terms
        purpose=LoanPurpose.PURCHASE,
        interest_rate=0.075,
        loan_term_months=360,
        is_interest_only=False,
        # Borrower
        fico=720,
        is_foreign_national=False
    )

    print(f"\nProperty: $400,000 SFR, leased at $2,400/mo")
    print(f"Borrower: FICO 720, Purchase")
    print(f"\nResults:")
    print(f"  FICO Tier: {result.fico_tier.value}")
    print(f"  Base LTV: {result.base_ltv:.0%}")
    print(f"  Max LTV (after adjustments): {result.max_ltv:.0%}")
    print(f"\n  LTV-Constrained Max: ${result.ltv_constrained_loan:,.0f}")
    print(f"  DSCR-Constrained Max: ${result.dscr_constrained_loan:,.0f}")
    print(f"\n  Max Loan Amount: ${result.max_loan_amount:,.0f}")
    print(f"  Binding Constraint: {result.binding_constraint.value}")
    print(f"  Actual LTV: {result.actual_ltv:.1%}")
    print(f"  Actual DSCR: {result.actual_dscr:.2f}x")
    print(f"  Eligible: {result.is_eligible}")

    if result.notes:
        print(f"\nNotes:")
        for note in result.notes:
            print(f"  - {note}")

    # Quick sizing
    quick = size_dscr_loan(
        property_value=400000,
        market_rent=2500,
        fico=720,
        annual_taxes=5000,
        annual_insurance=2000
    )
    print(f"\nQuick Sizing: Max ${quick['max_loan']:,.0f} at {quick['actual_ltv']:.1%} LTV")


def example_vacant_refinance():
    """Example: Vacant refinance with LTV reduction."""
    print("\n" + "="*60)
    print("EXAMPLE 5: Vacant Refinance (10% LTV Reduction)")
    print("="*60)

    sizer = DSCRSizer()

    result = sizer.size_loan(
        # Property
        property_value=350000,
        property_type=PropertyType.SFR,
        units=1,
        is_leased=False,  # VACANT
        rental_type=RentalType.LONG_TERM,
        # Income
        market_rent=2200,
        in_place_rent=None,  # No lease
        # Expenses
        annual_taxes=4200,
        annual_insurance=1500,
        # Loan terms
        purpose=LoanPurpose.CASH_OUT_REFINANCE,  # Refinance
        interest_rate=0.075,
        # Borrower
        fico=690,
        is_foreign_national=False
    )

    print(f"\nProperty: $350,000 SFR, VACANT, Cash-Out Refi")
    print(f"Market Rent: $2,200/mo")
    print(f"Borrower: FICO 690")
    print(f"\nResults:")
    print(f"  Base LTV: {result.base_ltv:.0%}")

    for red in result.reductions:
        if red.applied:
            print(f"  Reduction: {red.reason} (-{red.reduction:.0%})")

    print(f"  Max LTV: {result.max_ltv:.0%}")
    print(f"\n  Max Loan: ${result.max_loan_amount:,.0f}")
    print(f"  DSCR: {result.actual_dscr:.2f}x")
    print(f"  Eligible: {result.is_eligible}")


def example_property_eligibility():
    """Example: Property eligibility checks."""
    print("\n" + "="*60)
    print("EXAMPLE 6: Property Eligibility Checks")
    print("="*60)

    checker = PropertyEligibilityChecker()

    # Example 1: Standard SFR
    result = checker.check_eligibility(
        property_type=PropertyType.SFR,
        state="TX",
        square_footage=1800,
        units=1,
        acreage=0.25,
        is_rural=False,
        condition=ConditionRating.C3
    )

    print(f"\nProperty 1: 1,800 sq ft SFR in TX, C3 condition")
    print(f"  Eligible: {result.is_eligible}")
    print(f"  Products: {[p.value for p in result.loan_products_eligible]}")

    # Example 2: Property in ineligible state
    result2 = checker.check_eligibility(
        property_type=PropertyType.SFR,
        state="AK",
        square_footage=1500,
        units=1
    )

    print(f"\nProperty 2: SFR in Alaska")
    print(f"  Eligible: {result2.is_eligible}")
    print(f"  Errors: {result2.errors}")

    # Example 3: Small condo
    result3 = checker.check_eligibility(
        property_type=PropertyType.CONDO_WARRANTABLE,
        state="FL",
        square_footage=450,  # Below minimum
        units=1
    )

    print(f"\nProperty 3: 450 sq ft condo in FL")
    print(f"  Eligible: {result3.is_eligible}")
    print(f"  Errors: {result3.errors}")

    # Quick check
    quick = check_property_eligible("sfr", "CA", 1200)
    print(f"\nQuick Check (SFR, CA, 1200 sqft): {quick['is_eligible']}")


def example_condo_warrantability():
    """Example: Condo warrantability check."""
    print("\n" + "="*60)
    print("EXAMPLE 7: Condo Warrantability Check")
    print("="*60)

    checker = PropertyEligibilityChecker()

    # Warrantable condo
    result = checker.check_condo_warrantability(
        project_complete=True,
        developer_control=False,
        single_entity_ownership_pct=5.0,
        commercial_space_pct=10.0,
        rental_pct=40.0,
        hoa_delinquency_pct=8.0,
        pending_litigation=False
    )

    print(f"\nCondo 1: Standard warrantable project")
    print(f"  Warrantable: {result.is_warrantable}")

    # Non-warrantable condo
    result2 = checker.check_condo_warrantability(
        project_complete=True,
        developer_control=True,  # Developer still controls
        single_entity_ownership_pct=15.0,  # >10%
        commercial_space_pct=10.0,
        rental_pct=60.0,  # >50%
        hoa_delinquency_pct=8.0,
        pending_litigation=False
    )

    print(f"\nCondo 2: Non-warrantable project")
    print(f"  Warrantable: {result2.is_warrantable}")
    print(f"  Failures:")
    for failure in result2.failures:
        print(f"    - {failure}")

    # Quick check
    quick = check_condo_warrantable(
        project_complete=True,
        single_entity_pct=5.0,
        rental_pct=30.0
    )
    print(f"\nQuick Check: Warrantable = {quick['is_warrantable']}")


def example_max_loan_from_dscr():
    """Example: Calculate max loan to achieve target DSCR."""
    print("\n" + "="*60)
    print("EXAMPLE 8: Max Loan from Target DSCR")
    print("="*60)

    max_loan = calculate_max_loan_from_dscr(
        qualifying_rent=2500,
        target_dscr=1.00,
        interest_rate=0.075,
        annual_taxes=5000,
        annual_insurance=2000,
        monthly_hoa=100,
        loan_term_months=360,
        is_interest_only=False
    )

    print(f"\nInputs:")
    print(f"  Qualifying Rent: $2,500/mo")
    print(f"  Target DSCR: 1.00x")
    print(f"  Rate: 7.5%, 30-year amortizing")
    print(f"  T&I: $7,000/year, HOA: $100/mo")
    print(f"\nMax Loan for 1.00x DSCR: ${max_loan:,.0f}")

    # What about 1.20x target?
    max_loan_120 = calculate_max_loan_from_dscr(
        qualifying_rent=2500,
        target_dscr=1.20,
        interest_rate=0.075,
        annual_taxes=5000,
        annual_insurance=2000,
        monthly_hoa=100
    )
    print(f"Max Loan for 1.20x DSCR: ${max_loan_120:,.0f}")


if __name__ == "__main__":
    print("\n" + "="*60)
    print("USDV UNDERWRITING LIBRARY - EXAMPLES")
    print("="*60)

    example_rtl_classification()
    example_rtl_sizing()
    example_dscr_calculation()
    example_dscr_sizing()
    example_vacant_refinance()
    example_property_eligibility()
    example_condo_warrantability()
    example_max_loan_from_dscr()

    print("\n" + "="*60)
    print("ALL EXAMPLES COMPLETE")
    print("="*60 + "\n")
