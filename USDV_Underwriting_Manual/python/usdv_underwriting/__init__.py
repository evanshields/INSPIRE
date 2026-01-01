"""
USDV Capital Underwriting Library
=================================

Production-ready Python library for USDV Capital's single-family
business purpose lending operations. Supports both RTL (Rehab/Transitional)
and DSCR (Debt Service Coverage Ratio) loan products.

Modules:
--------
- common: Shared enums and data classes
- rtl_sizer: RTL loan sizing (Fix & Flip, Bridge, GUC)
- dscr_calculator: DSCR calculations and property income analysis
- dscr_sizer: DSCR loan sizing with LTV constraints
- property_eligibility: Property eligibility checks

Quick Start:
------------
    # RTL Loan Sizing
    from usdv_underwriting import RTLSizer, LoanProduct, LoanPurpose

    sizer = RTLSizer()
    result = sizer.size_loan(
        fico=720,
        deals_36mo=5,
        is_foreign_national=False,
        as_is_value=300000,
        arv=400000,
        units=1,
        product=LoanProduct.FIX_AND_FLIP,
        purpose=LoanPurpose.PURCHASE,
        purchase_price=290000,
        closing_costs=5000,
        assignment_fee=0,
        rehab_budget=50000,
        completed_rehab=0
    )
    print(f"Max Loan: ${result.total_loan_amount:,.0f}")
    print(f"Classification: {result.borrower_classification.classification.value}")

    # DSCR Loan Sizing
    from usdv_underwriting import DSCRSizer, DSCRCalculator

    sizer = DSCRSizer()
    result = sizer.size_loan(
        property_value=400000,
        market_rent=2500,
        fico=720,
        purpose=LoanPurpose.PURCHASE,
        interest_rate=0.075,
        annual_taxes=4800,
        annual_insurance=1800
    )
    print(f"Max Loan: ${result.max_loan_amount:,.0f}")
    print(f"DSCR: {result.actual_dscr:.2f}x")
    print(f"Binding Constraint: {result.binding_constraint.value}")

    # Quick DSCR Check
    from usdv_underwriting import quick_dscr_check

    dscr, meets_min, status = quick_dscr_check(
        monthly_rent=2500,
        monthly_pitia=2000,
        fico=720
    )
    print(status)  # "DSCR 1.25x meets 1.00x minimum"

    # Property Eligibility
    from usdv_underwriting import check_property_eligible

    result = check_property_eligible(
        property_type="sfr",
        state="TX",
        square_footage=1500
    )
    print(f"Eligible: {result['is_eligible']}")

Version: 2.0.0
Manual Reference: USDV Underwriting Manual v1.0
"""

__version__ = "2.0.0"
__author__ = "USDV Capital"

# =============================================================================
# COMMON EXPORTS
# =============================================================================
from .common import (
    # Loan enums
    LoanProduct,
    LoanPurpose,
    LoanType,
    # Property enums
    PropertyType,
    RentalType,
    LeaseStatus,
    ConditionRating,
    # Borrower enums
    BorrowerClass,
    CitizenshipStatus,
    FICOTier,
    # Data classes
    ValidationResult,
    EligibilityResult,
    # Constants
    MIN_LOAN_AMOUNT,
    MAX_LOAN_AMOUNT,
    MIN_FICO_RTL,
    MIN_FICO_DSCR,
    MIN_DSCR_STANDARD,
    MIN_DSCR_LOW_FICO,
    INELIGIBLE_STATES,
)

# =============================================================================
# RTL SIZER EXPORTS
# =============================================================================
from .rtl_sizer import (
    RTLSizer,
    BorrowerClassifier,
    BorrowerClassification,
    LeverageLimits,
    CostBasis,
    SizingConstraint,
    RTLSizingResult,
    quick_classification,
    quick_max_ltv,
)

# =============================================================================
# DSCR CALCULATOR EXPORTS
# =============================================================================
from .dscr_calculator import (
    DSCRCalculator,
    NCFCalculator,
    UnitRent,
    PropertyExpenses,
    QualifyingRentResult,
    PITIAResult,
    DSCRResult,
    NCFResult,
    quick_dscr_check,
    calculate_max_loan_from_dscr,
)

# =============================================================================
# DSCR SIZER EXPORTS
# =============================================================================
from .dscr_sizer import (
    DSCRSizer,
    DSCRSizingResult,
    LeverageReduction,
    BindingConstraint,
    size_dscr_loan,
)

# =============================================================================
# PROPERTY ELIGIBILITY EXPORTS
# =============================================================================
from .property_eligibility import (
    PropertyEligibilityChecker,
    PropertyEligibilityResult,
    CondoWarrantabilityResult,
    check_property_eligible,
    check_condo_warrantable,
)

# =============================================================================
# ALL EXPORTS
# =============================================================================
__all__ = [
    # Version
    "__version__",

    # Common - Enums
    "LoanProduct",
    "LoanPurpose",
    "LoanType",
    "PropertyType",
    "RentalType",
    "LeaseStatus",
    "ConditionRating",
    "BorrowerClass",
    "CitizenshipStatus",
    "FICOTier",
    "BindingConstraint",

    # Common - Data Classes
    "ValidationResult",
    "EligibilityResult",

    # Common - Constants
    "MIN_LOAN_AMOUNT",
    "MAX_LOAN_AMOUNT",
    "MIN_FICO_RTL",
    "MIN_FICO_DSCR",
    "MIN_DSCR_STANDARD",
    "MIN_DSCR_LOW_FICO",
    "INELIGIBLE_STATES",

    # RTL Sizer
    "RTLSizer",
    "BorrowerClassifier",
    "BorrowerClassification",
    "LeverageLimits",
    "CostBasis",
    "SizingConstraint",
    "RTLSizingResult",
    "quick_classification",
    "quick_max_ltv",

    # DSCR Calculator
    "DSCRCalculator",
    "NCFCalculator",
    "UnitRent",
    "PropertyExpenses",
    "QualifyingRentResult",
    "PITIAResult",
    "DSCRResult",
    "NCFResult",
    "quick_dscr_check",
    "calculate_max_loan_from_dscr",

    # DSCR Sizer
    "DSCRSizer",
    "DSCRSizingResult",
    "LeverageReduction",
    "size_dscr_loan",

    # Property Eligibility
    "PropertyEligibilityChecker",
    "PropertyEligibilityResult",
    "CondoWarrantabilityResult",
    "check_property_eligible",
    "check_condo_warrantable",
]
