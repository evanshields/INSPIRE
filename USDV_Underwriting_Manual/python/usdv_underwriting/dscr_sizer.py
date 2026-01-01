"""
DSCR Loan Sizing Module
USDV Capital Underwriting Library

This module provides DSCR loan sizing functionality including
LTV constraints, leverage reductions, and dual-constraint analysis.

Manual Reference: Section 10 - DSCR Loan Sizing & Leverage
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Tuple
from decimal import Decimal, ROUND_HALF_UP
from enum import Enum

from .common import (
    LoanPurpose, PropertyType, RentalType, CitizenshipStatus, FICOTier,
    MIN_LOAN_AMOUNT, MAX_LOAN_AMOUNT, MIN_DSCR_STANDARD
)
from .dscr_calculator import DSCRCalculator, DSCRResult


# =============================================================================
# ENUMS
# =============================================================================

class BindingConstraint(Enum):
    """Which constraint limits the loan."""
    LTV = "ltv"
    DSCR = "dscr"
    BOTH = "both"
    NONE = "none"


# =============================================================================
# DATA CLASSES
# =============================================================================

@dataclass
class LeverageReduction:
    """Individual leverage reduction."""
    reason: str
    reduction: float  # As decimal (e.g., 0.10 for 10%)
    applied: bool = True


@dataclass
class DSCRSizingResult:
    """Complete DSCR loan sizing result."""
    # Loan parameters
    loan_purpose: LoanPurpose
    property_type: PropertyType

    # Borrower
    fico: int
    fico_tier: FICOTier
    is_foreign_national: bool

    # Property values
    property_value: float

    # LTV analysis
    base_ltv: float
    reductions: List[LeverageReduction]
    total_reduction: float
    max_ltv: float
    ltv_constrained_loan: float

    # DSCR analysis
    dscr_result: Optional[DSCRResult]
    dscr_constrained_loan: float

    # Final sizing
    max_loan_amount: float
    binding_constraint: BindingConstraint
    actual_ltv: float
    actual_dscr: float

    # Eligibility
    is_eligible: bool
    ineligibility_reasons: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)


# =============================================================================
# DSCR SIZER
# =============================================================================

class DSCRSizer:
    """
    Calculate DSCR loan sizing with all constraints.

    Implements the dual-constraint methodology per USDV Guidelines
    Section 10, considering both LTV and DSCR limits.
    """

    # Base LTV matrix by FICO tier and purpose
    # Format: {fico_tier: {purpose: base_ltv}}
    BASE_LTV_MATRIX: Dict[str, Dict[LoanPurpose, float]] = {
        "780+": {
            LoanPurpose.PURCHASE: 0.80,
            LoanPurpose.RATE_TERM_REFINANCE: 0.80,
            LoanPurpose.CASH_OUT_REFINANCE: 0.80,
        },
        "760-779": {
            LoanPurpose.PURCHASE: 0.80,
            LoanPurpose.RATE_TERM_REFINANCE: 0.80,
            LoanPurpose.CASH_OUT_REFINANCE: 0.80,
        },
        "740-759": {
            LoanPurpose.PURCHASE: 0.80,
            LoanPurpose.RATE_TERM_REFINANCE: 0.80,
            LoanPurpose.CASH_OUT_REFINANCE: 0.80,
        },
        "720-739": {
            LoanPurpose.PURCHASE: 0.80,
            LoanPurpose.RATE_TERM_REFINANCE: 0.80,
            LoanPurpose.CASH_OUT_REFINANCE: 0.80,
        },
        "700-719": {
            LoanPurpose.PURCHASE: 0.80,
            LoanPurpose.RATE_TERM_REFINANCE: 0.80,
            LoanPurpose.CASH_OUT_REFINANCE: 0.75,
        },
        "680-699": {
            LoanPurpose.PURCHASE: 0.75,
            LoanPurpose.RATE_TERM_REFINANCE: 0.75,
            LoanPurpose.CASH_OUT_REFINANCE: 0.70,
        },
        "660-679": {
            LoanPurpose.PURCHASE: 0.70,
            LoanPurpose.RATE_TERM_REFINANCE: 0.70,
            LoanPurpose.CASH_OUT_REFINANCE: 0.65,
        },
        "FN": {
            LoanPurpose.PURCHASE: 0.70,
            LoanPurpose.RATE_TERM_REFINANCE: 0.70,
            LoanPurpose.CASH_OUT_REFINANCE: 0.65,
        },
    }

    # Leverage reduction values
    REDUCTION_UNLEASED_REFI = 0.10
    REDUCTION_NON_WARRANTABLE_CONDO = 0.10
    REDUCTION_5_9_UNITS = 0.05
    REDUCTION_HIGH_RISK_MARKET = 0.05
    REDUCTION_STR = 0.05
    REDUCTION_SECTION_8 = 0.05
    REDUCTION_LUXURY = 0.10

    # LTV increase opportunities
    INCREASE_700_719_HIGH_DSCR = 0.05  # DSCR >= 1.20x
    INCREASE_FN_HIGH_DSCR = 0.05  # DSCR >= 1.30x

    # Thresholds
    MIN_FICO = 660
    LUXURY_THRESHOLD = 1_000_000
    HIGH_RISK_MARKETS = ["Chicago", "Detroit", "Baltimore", "Flint"]

    def __init__(self):
        """Initialize the DSCR Sizer."""
        self.dscr_calculator = DSCRCalculator()

    def get_fico_tier(self, fico: int, is_foreign_national: bool = False) -> str:
        """
        Determine FICO tier from score.

        Args:
            fico: Credit score
            is_foreign_national: FN status

        Returns:
            FICO tier string
        """
        if is_foreign_national:
            return "FN"

        if fico >= 780:
            return "780+"
        elif fico >= 760:
            return "760-779"
        elif fico >= 740:
            return "740-759"
        elif fico >= 720:
            return "720-739"
        elif fico >= 700:
            return "700-719"
        elif fico >= 680:
            return "680-699"
        else:
            return "660-679"

    def get_fico_tier_enum(self, fico: int, is_foreign_national: bool = False) -> FICOTier:
        """Get FICO tier as enum."""
        if is_foreign_national:
            return FICOTier.FOREIGN_NATIONAL

        if fico >= 780:
            return FICOTier.TIER_1
        elif fico >= 760:
            return FICOTier.TIER_2
        elif fico >= 740:
            return FICOTier.TIER_3
        elif fico >= 720:
            return FICOTier.TIER_4
        elif fico >= 700:
            return FICOTier.TIER_5
        elif fico >= 680:
            return FICOTier.TIER_6
        else:
            return FICOTier.TIER_7

    def get_base_ltv(
        self,
        fico: int,
        purpose: LoanPurpose,
        is_foreign_national: bool = False
    ) -> float:
        """
        Get base LTV for FICO and purpose.

        Args:
            fico: Credit score
            purpose: Loan purpose
            is_foreign_national: FN status

        Returns:
            Base LTV as decimal
        """
        tier = self.get_fico_tier(fico, is_foreign_national)
        tier_matrix = self.BASE_LTV_MATRIX.get(tier, {})
        return tier_matrix.get(purpose, 0.70)

    def calculate_leverage_reductions(
        self,
        # Property conditions
        is_leased: bool,
        is_refinance: bool,
        property_type: PropertyType,
        units: int,
        rental_type: RentalType,
        market: str,
        loan_amount: float,
        dscr: float,
        # Borrower
        fico: int,
        is_foreign_national: bool
    ) -> Tuple[float, List[LeverageReduction]]:
        """
        Calculate all applicable leverage reductions.

        Args:
            is_leased: Property lease status
            is_refinance: Whether refinance
            property_type: Property type
            units: Number of units
            rental_type: Rental type
            market: Property market/city
            loan_amount: Estimated loan amount
            dscr: Calculated DSCR
            fico: Credit score
            is_foreign_national: FN status

        Returns:
            Tuple of (total_reduction, list of reductions)
        """
        reductions = []
        total_reduction = 0.0

        # Unleased refinance reduction
        if is_refinance and not is_leased:
            red = LeverageReduction(
                "Unleased Refinance",
                self.REDUCTION_UNLEASED_REFI,
                True
            )
            reductions.append(red)
            total_reduction += self.REDUCTION_UNLEASED_REFI

        # Non-warrantable condo
        if property_type == PropertyType.CONDO_NON_WARRANTABLE:
            red = LeverageReduction(
                "Non-Warrantable Condo",
                self.REDUCTION_NON_WARRANTABLE_CONDO,
                True
            )
            reductions.append(red)
            total_reduction += self.REDUCTION_NON_WARRANTABLE_CONDO

        # 5-9 units
        if 5 <= units <= 9:
            red = LeverageReduction(
                "5-9 Unit Property",
                self.REDUCTION_5_9_UNITS,
                True
            )
            reductions.append(red)
            total_reduction += self.REDUCTION_5_9_UNITS

        # High-risk market
        if market in self.HIGH_RISK_MARKETS:
            red = LeverageReduction(
                f"High-Risk Market ({market})",
                self.REDUCTION_HIGH_RISK_MARKET,
                True
            )
            reductions.append(red)
            total_reduction += self.REDUCTION_HIGH_RISK_MARKET

        # Short-term rental
        if rental_type == RentalType.SHORT_TERM:
            red = LeverageReduction(
                "Short-Term Rental",
                self.REDUCTION_STR,
                True
            )
            reductions.append(red)
            total_reduction += self.REDUCTION_STR

        # Section 8
        if rental_type == RentalType.SECTION_8:
            red = LeverageReduction(
                "Section 8 / Subsidized",
                self.REDUCTION_SECTION_8,
                True
            )
            reductions.append(red)
            total_reduction += self.REDUCTION_SECTION_8

        # Luxury rental
        if loan_amount > self.LUXURY_THRESHOLD:
            red = LeverageReduction(
                f"Luxury (>{self.LUXURY_THRESHOLD/1000:.0f}K UPB)",
                self.REDUCTION_LUXURY,
                True
            )
            reductions.append(red)
            total_reduction += self.REDUCTION_LUXURY

        return (total_reduction, reductions)

    def calculate_leverage_increases(
        self,
        fico: int,
        is_foreign_national: bool,
        dscr: float
    ) -> Tuple[float, List[LeverageReduction]]:
        """
        Calculate applicable leverage increases.

        Args:
            fico: Credit score
            is_foreign_national: FN status
            dscr: Calculated DSCR

        Returns:
            Tuple of (total_increase, list of increases)
        """
        increases = []
        total_increase = 0.0

        # 700-719 with high DSCR
        if 700 <= fico <= 719 and not is_foreign_national and dscr >= 1.20:
            inc = LeverageReduction(
                "700-719 FICO + DSCR >= 1.20x",
                self.INCREASE_700_719_HIGH_DSCR,
                True
            )
            increases.append(inc)
            total_increase += self.INCREASE_700_719_HIGH_DSCR

        # FN with high DSCR
        if is_foreign_national and dscr >= 1.30:
            inc = LeverageReduction(
                "Foreign National + DSCR >= 1.30x",
                self.INCREASE_FN_HIGH_DSCR,
                True
            )
            increases.append(inc)
            total_increase += self.INCREASE_FN_HIGH_DSCR

        return (total_increase, increases)

    def size_loan(
        self,
        # Property
        property_value: float,
        property_type: PropertyType,
        units: int = 1,
        is_leased: bool = True,
        rental_type: RentalType = RentalType.LONG_TERM,
        market: str = "",
        # Income
        market_rent: float = 0.0,
        in_place_rent: Optional[float] = None,
        str_trailing_income: Optional[float] = None,
        # Expenses
        annual_taxes: float = 0.0,
        annual_insurance: float = 0.0,
        monthly_hoa: float = 0.0,
        annual_flood: float = 0.0,
        # Loan terms
        purpose: LoanPurpose = LoanPurpose.PURCHASE,
        interest_rate: float = 0.075,
        loan_term_months: int = 360,
        is_interest_only: bool = False,
        # Borrower
        fico: int = 720,
        is_foreign_national: bool = False
    ) -> DSCRSizingResult:
        """
        Complete DSCR loan sizing analysis.

        Uses dual-constraint methodology: MIN(LTV-constrained, DSCR-constrained)

        Args:
            property_value: Appraised as-is value
            property_type: Property type
            units: Number of units
            is_leased: Whether property is leased
            rental_type: Type of rental
            market: City/market name
            market_rent: Appraised market rent
            in_place_rent: Current lease rent
            str_trailing_income: STR trailing income
            annual_taxes: Annual property taxes
            annual_insurance: Annual insurance
            monthly_hoa: Monthly HOA
            annual_flood: Annual flood insurance
            purpose: Loan purpose
            interest_rate: Annual interest rate
            loan_term_months: Loan term
            is_interest_only: Interest-only flag
            fico: Credit score
            is_foreign_national: FN status

        Returns:
            Complete DSCRSizingResult
        """
        ineligibility_reasons = []
        notes = []

        # Check minimum FICO
        if fico < self.MIN_FICO:
            ineligibility_reasons.append(f"FICO {fico} below minimum {self.MIN_FICO}")

        # Determine if refinance
        is_refinance = purpose in [
            LoanPurpose.RATE_TERM_REFINANCE,
            LoanPurpose.CASH_OUT_REFINANCE
        ]

        # Get FICO tier
        fico_tier = self.get_fico_tier_enum(fico, is_foreign_national)

        # Step 1: Get base LTV
        base_ltv = self.get_base_ltv(fico, purpose, is_foreign_national)

        # Step 2: Calculate preliminary DSCR for increase eligibility
        # Use estimated max loan for preliminary DSCR
        estimated_loan = property_value * base_ltv

        preliminary_dscr = self.dscr_calculator.analyze_dscr(
            market_rent=market_rent,
            in_place_rent=in_place_rent,
            is_leased=is_leased,
            rental_type=rental_type,
            str_trailing_income=str_trailing_income,
            loan_amount=estimated_loan,
            interest_rate=interest_rate,
            loan_term_months=loan_term_months,
            is_interest_only=is_interest_only,
            annual_taxes=annual_taxes,
            annual_insurance=annual_insurance,
            monthly_hoa=monthly_hoa,
            annual_flood=annual_flood,
            loan_purpose=purpose,
            fico=fico,
            is_foreign_national=is_foreign_national
        )

        # Step 3: Calculate leverage adjustments
        total_reduction, reductions = self.calculate_leverage_reductions(
            is_leased=is_leased,
            is_refinance=is_refinance,
            property_type=property_type,
            units=units,
            rental_type=rental_type,
            market=market,
            loan_amount=estimated_loan,
            dscr=preliminary_dscr.dscr,
            fico=fico,
            is_foreign_national=is_foreign_national
        )

        total_increase, increases = self.calculate_leverage_increases(
            fico=fico,
            is_foreign_national=is_foreign_national,
            dscr=preliminary_dscr.dscr
        )

        # Net adjustment
        net_adjustment = total_increase - total_reduction
        all_adjustments = reductions + increases

        # Step 4: Calculate max LTV
        max_ltv = max(0.0, min(1.0, base_ltv + net_adjustment))

        # Step 5: LTV-constrained loan
        ltv_constrained = property_value * max_ltv

        # Step 6: DSCR-constrained loan (iterative)
        # Find max loan where DSCR >= minimum
        min_dscr = self.dscr_calculator.get_minimum_dscr(
            fico=fico,
            is_foreign_national=is_foreign_national,
            rental_type=rental_type
        )

        # Binary search for DSCR-constrained max
        dscr_constrained = self._find_dscr_constrained_loan(
            target_dscr=min_dscr,
            market_rent=market_rent,
            in_place_rent=in_place_rent,
            is_leased=is_leased,
            is_refinance=is_refinance,
            rental_type=rental_type,
            str_trailing_income=str_trailing_income,
            interest_rate=interest_rate,
            loan_term_months=loan_term_months,
            is_interest_only=is_interest_only,
            annual_taxes=annual_taxes,
            annual_insurance=annual_insurance,
            monthly_hoa=monthly_hoa,
            annual_flood=annual_flood,
            max_loan=ltv_constrained * 1.5,  # Search up to 150% of LTV max
            fico=fico,
            is_foreign_national=is_foreign_national,
            purpose=purpose
        )

        # Step 7: Determine binding constraint
        if ltv_constrained <= 0 and dscr_constrained <= 0:
            binding = BindingConstraint.NONE
            max_loan = 0.0
        elif abs(ltv_constrained - dscr_constrained) < 100:
            binding = BindingConstraint.BOTH
            max_loan = min(ltv_constrained, dscr_constrained)
        elif ltv_constrained < dscr_constrained:
            binding = BindingConstraint.LTV
            max_loan = ltv_constrained
            notes.append(f"LTV-constrained: DSCR headroom of ${dscr_constrained - ltv_constrained:,.0f}")
        else:
            binding = BindingConstraint.DSCR
            max_loan = dscr_constrained
            notes.append(f"DSCR-constrained: LTV headroom of ${ltv_constrained - dscr_constrained:,.0f}")

        # Apply loan amount limits
        max_loan = min(max_loan, MAX_LOAN_AMOUNT)
        max_loan = max(max_loan, 0)

        if max_loan > 0 and max_loan < MIN_LOAN_AMOUNT:
            ineligibility_reasons.append(f"Max loan ${max_loan:,.0f} below minimum ${MIN_LOAN_AMOUNT:,.0f}")

        # Step 8: Final DSCR at max loan
        final_dscr = self.dscr_calculator.analyze_dscr(
            market_rent=market_rent,
            in_place_rent=in_place_rent,
            is_leased=is_leased,
            rental_type=rental_type,
            str_trailing_income=str_trailing_income,
            loan_amount=max_loan,
            interest_rate=interest_rate,
            loan_term_months=loan_term_months,
            is_interest_only=is_interest_only,
            annual_taxes=annual_taxes,
            annual_insurance=annual_insurance,
            monthly_hoa=monthly_hoa,
            annual_flood=annual_flood,
            loan_purpose=purpose,
            fico=fico,
            is_foreign_national=is_foreign_national
        )

        # Calculate actual LTV
        actual_ltv = max_loan / property_value if property_value > 0 else 0.0

        # Eligibility determination
        is_eligible = len(ineligibility_reasons) == 0 and final_dscr.meets_minimum

        if not final_dscr.meets_minimum:
            ineligibility_reasons.append(
                f"DSCR {final_dscr.dscr:.2f}x below minimum {final_dscr.min_dscr_required:.2f}x"
            )

        return DSCRSizingResult(
            loan_purpose=purpose,
            property_type=property_type,
            fico=fico,
            fico_tier=fico_tier,
            is_foreign_national=is_foreign_national,
            property_value=property_value,
            base_ltv=base_ltv,
            reductions=all_adjustments,
            total_reduction=total_reduction - total_increase,
            max_ltv=max_ltv,
            ltv_constrained_loan=round(ltv_constrained, 2),
            dscr_result=final_dscr,
            dscr_constrained_loan=round(dscr_constrained, 2),
            max_loan_amount=round(max_loan, 2),
            binding_constraint=binding,
            actual_ltv=round(actual_ltv, 4),
            actual_dscr=final_dscr.dscr,
            is_eligible=is_eligible,
            ineligibility_reasons=ineligibility_reasons,
            notes=notes + final_dscr.notes
        )

    def _find_dscr_constrained_loan(
        self,
        target_dscr: float,
        market_rent: float,
        in_place_rent: Optional[float],
        is_leased: bool,
        is_refinance: bool,
        rental_type: RentalType,
        str_trailing_income: Optional[float],
        interest_rate: float,
        loan_term_months: int,
        is_interest_only: bool,
        annual_taxes: float,
        annual_insurance: float,
        monthly_hoa: float,
        annual_flood: float,
        max_loan: float,
        fico: int,
        is_foreign_national: bool,
        purpose: LoanPurpose
    ) -> float:
        """
        Binary search to find DSCR-constrained max loan.

        Finds the maximum loan amount where DSCR >= target_dscr.
        """
        low = 0.0
        high = max_loan
        tolerance = 100  # $100 tolerance

        # Check if even max loan meets DSCR
        dscr_at_max = self.dscr_calculator.analyze_dscr(
            market_rent=market_rent,
            in_place_rent=in_place_rent,
            is_leased=is_leased,
            rental_type=rental_type,
            str_trailing_income=str_trailing_income,
            loan_amount=high,
            interest_rate=interest_rate,
            loan_term_months=loan_term_months,
            is_interest_only=is_interest_only,
            annual_taxes=annual_taxes,
            annual_insurance=annual_insurance,
            monthly_hoa=monthly_hoa,
            annual_flood=annual_flood,
            loan_purpose=purpose,
            fico=fico,
            is_foreign_national=is_foreign_national
        )

        if dscr_at_max.dscr >= target_dscr:
            return high

        # Binary search
        while high - low > tolerance:
            mid = (low + high) / 2

            dscr_result = self.dscr_calculator.analyze_dscr(
                market_rent=market_rent,
                in_place_rent=in_place_rent,
                is_leased=is_leased,
                rental_type=rental_type,
                str_trailing_income=str_trailing_income,
                loan_amount=mid,
                interest_rate=interest_rate,
                loan_term_months=loan_term_months,
                is_interest_only=is_interest_only,
                annual_taxes=annual_taxes,
                annual_insurance=annual_insurance,
                monthly_hoa=monthly_hoa,
                annual_flood=annual_flood,
                loan_purpose=purpose,
                fico=fico,
                is_foreign_national=is_foreign_national
            )

            if dscr_result.dscr >= target_dscr:
                low = mid
            else:
                high = mid

        return low


# =============================================================================
# CONVENIENCE FUNCTION
# =============================================================================

def size_dscr_loan(
    property_value: float,
    market_rent: float,
    fico: int,
    purpose: str = "purchase",
    interest_rate: float = 0.075,
    annual_taxes: float = 0.0,
    annual_insurance: float = 0.0,
    is_leased: bool = True,
    is_foreign_national: bool = False
) -> Dict:
    """
    Quick DSCR loan sizing.

    Args:
        property_value: Property value
        market_rent: Monthly market rent
        fico: Credit score
        purpose: "purchase", "rate_term", or "cash_out"
        interest_rate: Annual rate
        annual_taxes: Annual taxes
        annual_insurance: Annual insurance
        is_leased: Lease status
        is_foreign_national: FN status

    Returns:
        Dict with max_loan, max_ltv, dscr, is_eligible
    """
    purpose_map = {
        "purchase": LoanPurpose.PURCHASE,
        "rate_term": LoanPurpose.RATE_TERM_REFINANCE,
        "cash_out": LoanPurpose.CASH_OUT_REFINANCE
    }

    sizer = DSCRSizer()
    result = sizer.size_loan(
        property_value=property_value,
        property_type=PropertyType.SFR,
        is_leased=is_leased,
        market_rent=market_rent,
        in_place_rent=market_rent if is_leased else None,
        annual_taxes=annual_taxes,
        annual_insurance=annual_insurance,
        purpose=purpose_map.get(purpose, LoanPurpose.PURCHASE),
        interest_rate=interest_rate,
        fico=fico,
        is_foreign_national=is_foreign_national
    )

    return {
        "max_loan": result.max_loan_amount,
        "max_ltv": result.max_ltv,
        "actual_ltv": result.actual_ltv,
        "dscr": result.actual_dscr,
        "min_dscr": result.dscr_result.min_dscr_required if result.dscr_result else 1.0,
        "binding_constraint": result.binding_constraint.value,
        "is_eligible": result.is_eligible,
        "reasons": result.ineligibility_reasons
    }
