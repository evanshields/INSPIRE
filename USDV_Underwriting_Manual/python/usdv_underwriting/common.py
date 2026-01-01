"""
Common Enums and Data Classes
USDV Capital Underwriting Library

Shared types used across RTL and DSCR modules.

Manual Reference: All Sections
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List
from decimal import Decimal


# =============================================================================
# LOAN ENUMS
# =============================================================================

class LoanProduct(Enum):
    """All loan product types."""
    # RTL Products
    FIX_AND_FLIP = "fix_and_flip"
    BRIDGE = "bridge"
    BRIDGE_PLUS = "bridge_plus"
    GROUND_UP_CONSTRUCTION = "guc"
    # DSCR Products
    DSCR = "dscr"
    DSCR_5_9 = "dscr_5_9"


class LoanPurpose(Enum):
    """Loan purpose classification."""
    PURCHASE = "purchase"
    RATE_TERM_REFINANCE = "rate_term_refinance"
    CASH_OUT_REFINANCE = "cash_out_refinance"
    DELAYED_PURCHASE = "delayed_purchase"


class LoanType(Enum):
    """High-level loan type."""
    RTL = "rtl"
    DSCR = "dscr"


# =============================================================================
# PROPERTY ENUMS
# =============================================================================

class PropertyType(Enum):
    """Property type classification."""
    SFR = "sfr"
    TOWNHOME = "townhome"
    PUD = "pud"
    CONDO_WARRANTABLE = "condo_warrantable"
    CONDO_NON_WARRANTABLE = "condo_non_warrantable"
    TWO_TO_FOUR_UNIT = "2_4_unit"
    FIVE_TO_NINE_UNIT = "5_9_unit"
    MANUFACTURED = "manufactured"


class RentalType(Enum):
    """Rental property classification."""
    LONG_TERM = "long_term"
    SHORT_TERM = "str"
    SECTION_8 = "section_8"
    VACATION = "vacation"


class LeaseStatus(Enum):
    """Property lease status."""
    LEASED = "leased"
    UNLEASED = "unleased"
    MONTH_TO_MONTH = "month_to_month"


class ConditionRating(Enum):
    """Property condition per UAD standards."""
    C1 = "C1"  # New construction
    C2 = "C2"  # Recently built, no deferred maintenance
    C3 = "C3"  # Well maintained, limited depreciation
    C4 = "C4"  # Adequately maintained, some deferred maintenance
    C5 = "C5"  # Obvious deferred maintenance
    C6 = "C6"  # Substantial damage or deferred maintenance


# =============================================================================
# BORROWER ENUMS
# =============================================================================

class BorrowerClass(Enum):
    """RTL borrower classification tiers."""
    A_PLUS = "A+"
    A = "A"
    B = "B"
    C = "C"


class CitizenshipStatus(Enum):
    """Borrower citizenship status."""
    US_CITIZEN = "us_citizen"
    PERMANENT_RESIDENT = "permanent_resident"
    NON_PERMANENT_RESIDENT = "non_permanent_resident"
    FOREIGN_NATIONAL = "foreign_national"


class FICOTier(Enum):
    """DSCR FICO tiers for leverage determination."""
    TIER_1 = "780+"
    TIER_2 = "760-779"
    TIER_3 = "740-759"
    TIER_4 = "720-739"
    TIER_5 = "700-719"
    TIER_6 = "680-699"
    TIER_7 = "660-679"
    FOREIGN_NATIONAL = "FN"


# =============================================================================
# SHARED DATA CLASSES
# =============================================================================

@dataclass
class ValidationResult:
    """Result of any validation check."""
    is_valid: bool
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)


@dataclass
class EligibilityResult:
    """Result of eligibility determination."""
    is_eligible: bool
    reasons: List[str] = field(default_factory=list)
    exceptions_required: List[str] = field(default_factory=list)
    compensating_factors: List[str] = field(default_factory=list)


# =============================================================================
# CONSTANTS
# =============================================================================

# Loan amount limits
MIN_LOAN_AMOUNT = 100_000
MAX_LOAN_AMOUNT = 3_000_000
MAX_LOAN_AMOUNT_EXCEPTION = 4_500_000

# FICO limits
MIN_FICO_RTL = 660
MIN_FICO_DSCR = 660
STANDARD_MIN_FICO_DSCR = 680

# Property limits
MIN_SQ_FT_SFR = 600
MIN_SQ_FT_CONDO = 500
MIN_SQ_FT_MULTI = 500
MAX_ACREAGE = 5

# DSCR limits
MIN_DSCR_STANDARD = 1.00
MIN_DSCR_LOW_FICO = 1.20
MIN_DSCR_FOREIGN_NATIONAL = 1.20

# Document currency (days)
APPRAISAL_CURRENCY_DAYS = 120
CREDIT_CURRENCY_DAYS = 120
BANK_STATEMENT_CURRENCY_DAYS = 90

# Ineligible states
INELIGIBLE_STATES = ["ND", "SD", "AK", "HI"]

# High risk markets
HIGH_RISK_MARKETS = ["Chicago", "Detroit", "Baltimore", "Flint"]
