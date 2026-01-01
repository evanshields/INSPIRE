"""
DSCR Calculator Module
USDV Capital Underwriting Library

This module provides DSCR (Debt Service Coverage Ratio) calculation
functionality for rental property income analysis.

Manual Reference: Section 7 - DSCR Property & Income Analysis
"""

from dataclasses import dataclass, field
from typing import Optional, List, Tuple
from decimal import Decimal, ROUND_HALF_UP

from .common import (
    LoanPurpose, PropertyType, RentalType, LeaseStatus,
    MIN_DSCR_STANDARD, MIN_DSCR_LOW_FICO, MIN_DSCR_FOREIGN_NATIONAL
)


# =============================================================================
# DATA CLASSES
# =============================================================================

@dataclass
class UnitRent:
    """Rent information for a single unit."""
    unit_number: int
    is_leased: bool
    in_place_rent: Optional[float] = None
    market_rent: float = 0.0
    qualifying_rent: float = 0.0
    calculation_method: str = ""


@dataclass
class PropertyExpenses:
    """Monthly property expense breakdown."""
    taxes: float  # Annual taxes / 12
    insurance: float  # Annual insurance / 12
    hoa: float = 0.0  # Monthly HOA/association fees
    flood_insurance: float = 0.0  # Additional flood if in flood zone

    @property
    def total_tia(self) -> float:
        """Total Taxes, Insurance, Association fees."""
        return self.taxes + self.insurance + self.hoa + self.flood_insurance


@dataclass
class QualifyingRentResult:
    """Result of qualifying rent calculation."""
    qualifying_rent: float
    calculation_method: str
    in_place_rent: Optional[float]
    market_rent: float
    market_rent_cap: float
    haircut_applied: Optional[float] = None
    notes: List[str] = field(default_factory=list)


@dataclass
class PITIAResult:
    """Monthly PITIA calculation result."""
    principal: float
    interest: float
    taxes: float
    insurance: float
    association: float
    total_pitia: float
    calculation_notes: List[str] = field(default_factory=list)


@dataclass
class DSCRResult:
    """Complete DSCR calculation result."""
    dscr: float
    qualifying_rent: float
    monthly_pitia: float
    rent_breakdown: QualifyingRentResult
    pitia_breakdown: PITIAResult
    min_dscr_required: float
    meets_minimum: bool
    is_eligible: bool
    notes: List[str] = field(default_factory=list)


# =============================================================================
# DSCR CALCULATOR
# =============================================================================

class DSCRCalculator:
    """
    Calculate DSCR for rental properties.

    Implements qualifying rent determination and DSCR calculation
    per USDV Guidelines Section 7.
    """

    # Rent caps
    MARKET_RENT_CAP_LEASED = 1.05  # 105% for leased properties
    MARKET_RENT_CAP_UNLEASED = 1.00  # 100% for unleased
    MARKET_RENT_CAP_STR = 1.25  # 125% for short-term rentals

    # Vacant refinance adjustments (EastView standard)
    VACANT_REFI_RENT_FACTOR = 1.00  # 100% of market rent (no haircut)
    VACANT_REFI_LTV_REDUCTION = 0.10  # 10% LTV reduction

    # Minimum DSCR requirements
    MIN_DSCR_STANDARD = 1.00
    MIN_DSCR_LOW_FICO = 1.20  # FICO < 700 with elevated risk
    MIN_DSCR_FOREIGN_NATIONAL = 1.20

    # Units required to be leased for "leased" classification
    UNITS_REQUIRED_LEASED = {
        1: 1,  # SFR/Townhome/Condo/PUD
        2: 1,
        3: 2,
        4: 2,
        5: 3,
        6: 3,
        7: 4,
        8: 4,
        9: 5,
    }

    def calculate_qualifying_rent(
        self,
        market_rent: float,
        in_place_rent: Optional[float],
        is_leased: bool,
        is_refinance: bool,
        rental_type: RentalType = RentalType.LONG_TERM,
        str_trailing_income: Optional[float] = None
    ) -> QualifyingRentResult:
        """
        Calculate qualifying rent per USDV guidelines.

        Args:
            market_rent: Appraised market rent (Form 1007)
            in_place_rent: Current lease rent (if leased)
            is_leased: Whether property is currently leased
            is_refinance: Whether this is a refinance transaction
            rental_type: Type of rental (long-term, STR, Section 8)
            str_trailing_income: 12-month average STR income (if STR)

        Returns:
            QualifyingRentResult with qualifying rent and methodology
        """
        notes = []
        haircut = None

        # Short-term rental handling
        if rental_type == RentalType.SHORT_TERM:
            market_cap = market_rent * self.MARKET_RENT_CAP_STR

            if str_trailing_income:
                qualifying = min(market_cap, str_trailing_income)
                method = f"STR: MIN(125% market ${market_cap:,.0f}, trailing ${str_trailing_income:,.0f})"
            else:
                qualifying = market_cap
                method = f"STR: 125% of market rent"
                notes.append("No trailing income provided - using 125% market rent")

            cap_used = self.MARKET_RENT_CAP_STR

        # Section 8 handling
        elif rental_type == RentalType.SECTION_8:
            if in_place_rent:
                qualifying = in_place_rent
                method = "Section 8: Contract rent"
            else:
                qualifying = market_rent
                method = "Section 8: Market rent (no contract provided)"
                notes.append("Section 8 contract rent preferred")
            cap_used = 1.00

        # Leased property
        elif is_leased and in_place_rent:
            market_cap = market_rent * self.MARKET_RENT_CAP_LEASED
            qualifying = min(in_place_rent, market_cap)
            method = f"Leased: MIN(in-place ${in_place_rent:,.0f}, 105% market ${market_cap:,.0f})"
            cap_used = self.MARKET_RENT_CAP_LEASED

        # Vacant refinance: 100% of market rent, 10% LTV reduction (EastView standard)
        elif not is_leased and is_refinance:
            qualifying = market_rent * self.VACANT_REFI_RENT_FACTOR
            haircut = None  # No rent haircut under EastView standard
            method = "Vacant Refinance: 100% of market rent"
            cap_used = self.MARKET_RENT_CAP_UNLEASED
            notes.append("10% LTV reduction applies for vacant refinance (see Section 10)")

        # Unleased purchase: 100% of market rent
        else:
            qualifying = market_rent * self.MARKET_RENT_CAP_UNLEASED
            method = "Unleased Purchase: 100% of market rent"
            cap_used = self.MARKET_RENT_CAP_UNLEASED

        return QualifyingRentResult(
            qualifying_rent=round(qualifying, 2),
            calculation_method=method,
            in_place_rent=in_place_rent,
            market_rent=market_rent,
            market_rent_cap=cap_used,
            haircut_applied=haircut,
            notes=notes
        )

    def calculate_multi_unit_rent(
        self,
        units: List[UnitRent],
        is_refinance: bool,
        rental_type: RentalType = RentalType.LONG_TERM
    ) -> Tuple[float, List[UnitRent]]:
        """
        Calculate total qualifying rent for multi-unit property.

        Args:
            units: List of UnitRent objects for each unit
            is_refinance: Whether this is a refinance
            rental_type: Rental type

        Returns:
            Tuple of (total_qualifying_rent, updated_units)
        """
        total = 0.0
        updated_units = []

        for unit in units:
            result = self.calculate_qualifying_rent(
                market_rent=unit.market_rent,
                in_place_rent=unit.in_place_rent,
                is_leased=unit.is_leased,
                is_refinance=is_refinance,
                rental_type=rental_type
            )

            updated_unit = UnitRent(
                unit_number=unit.unit_number,
                is_leased=unit.is_leased,
                in_place_rent=unit.in_place_rent,
                market_rent=unit.market_rent,
                qualifying_rent=result.qualifying_rent,
                calculation_method=result.calculation_method
            )
            updated_units.append(updated_unit)
            total += result.qualifying_rent

        return (round(total, 2), updated_units)

    def is_property_leased(
        self,
        total_units: int,
        leased_units: int
    ) -> bool:
        """
        Determine if property qualifies as "leased" for underwriting.

        Args:
            total_units: Total number of units in property
            leased_units: Number of units currently leased

        Returns:
            True if property qualifies as leased
        """
        required = self.UNITS_REQUIRED_LEASED.get(total_units, total_units // 2 + 1)
        return leased_units >= required

    def calculate_pitia(
        self,
        loan_amount: float,
        interest_rate: float,
        loan_term_months: int,
        annual_taxes: float,
        annual_insurance: float,
        monthly_hoa: float = 0.0,
        annual_flood: float = 0.0,
        is_interest_only: bool = False
    ) -> PITIAResult:
        """
        Calculate monthly PITIA (Principal, Interest, Taxes, Insurance, Association).

        Args:
            loan_amount: Total loan amount
            interest_rate: Annual interest rate (e.g., 0.075 for 7.5%)
            loan_term_months: Loan term in months (e.g., 360 for 30-year)
            annual_taxes: Annual property taxes
            annual_insurance: Annual insurance premium
            monthly_hoa: Monthly HOA/association fees
            annual_flood: Annual flood insurance (if applicable)
            is_interest_only: Whether loan is interest-only

        Returns:
            PITIAResult with component breakdown
        """
        notes = []

        # Calculate monthly interest
        monthly_rate = interest_rate / 12

        if is_interest_only:
            # Interest-only payment
            monthly_interest = loan_amount * monthly_rate
            monthly_principal = 0.0
            notes.append("Interest-only payment calculated")
        else:
            # Fully amortizing P&I
            if monthly_rate > 0 and loan_term_months > 0:
                # Standard amortization formula
                monthly_pi = loan_amount * (
                    monthly_rate * (1 + monthly_rate) ** loan_term_months
                ) / (
                    (1 + monthly_rate) ** loan_term_months - 1
                )
            else:
                monthly_pi = loan_amount / loan_term_months if loan_term_months > 0 else 0

            monthly_interest = loan_amount * monthly_rate
            monthly_principal = monthly_pi - monthly_interest

        # Monthly escrows
        monthly_taxes = annual_taxes / 12
        monthly_insurance = annual_insurance / 12
        monthly_flood = annual_flood / 12

        total_pitia = (
            monthly_principal +
            monthly_interest +
            monthly_taxes +
            monthly_insurance +
            monthly_hoa +
            monthly_flood
        )

        return PITIAResult(
            principal=round(monthly_principal, 2),
            interest=round(monthly_interest, 2),
            taxes=round(monthly_taxes, 2),
            insurance=round(monthly_insurance + monthly_flood, 2),
            association=round(monthly_hoa, 2),
            total_pitia=round(total_pitia, 2),
            calculation_notes=notes
        )

    def calculate_dscr(
        self,
        qualifying_rent: float,
        monthly_pitia: float
    ) -> float:
        """
        Calculate DSCR ratio.

        Args:
            qualifying_rent: Qualifying monthly rent
            monthly_pitia: Monthly PITIA payment

        Returns:
            DSCR ratio (e.g., 1.25)
        """
        if monthly_pitia <= 0:
            return 0.0

        return round(qualifying_rent / monthly_pitia, 3)

    def get_minimum_dscr(
        self,
        fico: int,
        is_foreign_national: bool = False,
        rental_type: RentalType = RentalType.LONG_TERM
    ) -> float:
        """
        Determine minimum required DSCR.

        Args:
            fico: Credit score
            is_foreign_national: Foreign national status
            rental_type: Type of rental

        Returns:
            Minimum required DSCR
        """
        if is_foreign_national:
            return self.MIN_DSCR_FOREIGN_NATIONAL

        if fico < 700:
            return self.MIN_DSCR_LOW_FICO

        return self.MIN_DSCR_STANDARD

    def analyze_dscr(
        self,
        # Property income
        market_rent: float,
        in_place_rent: Optional[float],
        is_leased: bool,
        rental_type: RentalType,
        str_trailing_income: Optional[float] = None,
        # Loan terms
        loan_amount: float = 0.0,
        interest_rate: float = 0.0,
        loan_term_months: int = 360,
        is_interest_only: bool = False,
        # Expenses
        annual_taxes: float = 0.0,
        annual_insurance: float = 0.0,
        monthly_hoa: float = 0.0,
        annual_flood: float = 0.0,
        # Loan details
        loan_purpose: LoanPurpose = LoanPurpose.PURCHASE,
        # Borrower
        fico: int = 720,
        is_foreign_national: bool = False
    ) -> DSCRResult:
        """
        Complete DSCR analysis.

        Args:
            market_rent: Appraised market rent
            in_place_rent: Current lease rent (if leased)
            is_leased: Whether property is leased
            rental_type: Type of rental
            str_trailing_income: STR trailing income (if applicable)
            loan_amount: Loan amount for PITIA calculation
            interest_rate: Annual interest rate
            loan_term_months: Loan term in months
            is_interest_only: Interest-only flag
            annual_taxes: Annual property taxes
            annual_insurance: Annual insurance
            monthly_hoa: Monthly HOA fees
            annual_flood: Annual flood insurance
            loan_purpose: Loan purpose
            fico: Credit score
            is_foreign_national: Foreign national status

        Returns:
            Complete DSCRResult with all details
        """
        notes = []

        # Determine if refinance
        is_refinance = loan_purpose in [
            LoanPurpose.RATE_TERM_REFINANCE,
            LoanPurpose.CASH_OUT_REFINANCE
        ]

        # Calculate qualifying rent
        rent_result = self.calculate_qualifying_rent(
            market_rent=market_rent,
            in_place_rent=in_place_rent,
            is_leased=is_leased,
            is_refinance=is_refinance,
            rental_type=rental_type,
            str_trailing_income=str_trailing_income
        )
        notes.extend(rent_result.notes)

        # Calculate PITIA
        pitia_result = self.calculate_pitia(
            loan_amount=loan_amount,
            interest_rate=interest_rate,
            loan_term_months=loan_term_months,
            annual_taxes=annual_taxes,
            annual_insurance=annual_insurance,
            monthly_hoa=monthly_hoa,
            annual_flood=annual_flood,
            is_interest_only=is_interest_only
        )
        notes.extend(pitia_result.calculation_notes)

        # Calculate DSCR
        dscr = self.calculate_dscr(
            qualifying_rent=rent_result.qualifying_rent,
            monthly_pitia=pitia_result.total_pitia
        )

        # Determine minimum required
        min_dscr = self.get_minimum_dscr(
            fico=fico,
            is_foreign_national=is_foreign_national,
            rental_type=rental_type
        )

        meets_minimum = dscr >= min_dscr

        # Add context notes
        if is_foreign_national:
            notes.append("Foreign National: 1.20x minimum DSCR required")

        if rental_type == RentalType.SHORT_TERM:
            notes.append("STR property: 5% LTV reduction applies")

        if not is_leased and is_refinance:
            notes.append("Vacant refinance: 10% LTV reduction applies")

        if not meets_minimum:
            notes.append(f"DSCR {dscr:.3f}x below minimum {min_dscr:.2f}x")

        return DSCRResult(
            dscr=dscr,
            qualifying_rent=rent_result.qualifying_rent,
            monthly_pitia=pitia_result.total_pitia,
            rent_breakdown=rent_result,
            pitia_breakdown=pitia_result,
            min_dscr_required=min_dscr,
            meets_minimum=meets_minimum,
            is_eligible=meets_minimum,
            notes=notes
        )


# =============================================================================
# NCF CALCULATOR (5-9 Units)
# =============================================================================

@dataclass
class NCFResult:
    """Net Cash Flow calculation result for 5-9 unit properties."""
    gross_rent: float
    effective_gross_income: float
    vacancy_loss: float
    operating_expenses: float
    net_operating_income: float
    capital_reserves: float
    net_cash_flow: float
    annual_debt_service: float
    ncf_dscr: float
    expense_ratio: float
    notes: List[str] = field(default_factory=list)


class NCFCalculator:
    """
    Calculate NCF-based DSCR for 5-9 unit properties.

    Implements Net Cash Flow methodology per Section 7.2.2.
    """

    # Operating expense minimums
    MIN_MANAGEMENT_RATE = 0.08  # 8% of gross rent
    MIN_REPAIRS_PER_UNIT_NEW = 500
    MIN_REPAIRS_PER_UNIT_EXISTING = 700
    MIN_CAPEX_PER_UNIT_MULTI = 300
    MIN_CAPEX_PER_UNIT_SFR_NEW = 400
    MIN_CAPEX_PER_UNIT_SFR_EXISTING = 600

    # Default vacancy
    DEFAULT_VACANCY_RATE = 0.05  # 5%

    def calculate_ncf_dscr(
        self,
        # Income
        gross_annual_rent: float,
        other_income: float = 0.0,
        vacancy_rate: float = 0.05,
        # Property
        units: int = 5,
        is_new_construction: bool = False,
        # Expenses
        management_expense: Optional[float] = None,
        repairs_expense: Optional[float] = None,
        insurance_expense: float = 0.0,
        taxes_expense: float = 0.0,
        utilities_expense: float = 0.0,
        hoa_expense: float = 0.0,
        other_expenses: float = 0.0,
        # Capital reserves
        capex_reserves: Optional[float] = None,
        # Debt service
        annual_debt_service: float = 0.0
    ) -> NCFResult:
        """
        Calculate NCF-based DSCR for multifamily properties.

        Args:
            gross_annual_rent: Total annual gross rent
            other_income: Other income (laundry, parking, etc.)
            vacancy_rate: Vacancy/collection loss rate
            units: Number of units
            is_new_construction: Whether newly constructed
            management_expense: Property management (min 8%)
            repairs_expense: Repairs & maintenance
            insurance_expense: Annual insurance
            taxes_expense: Annual property taxes
            utilities_expense: Landlord-paid utilities
            hoa_expense: Annual HOA fees
            other_expenses: Other operating expenses
            capex_reserves: Capital expenditure reserves
            annual_debt_service: Annual debt service

        Returns:
            NCFResult with complete breakdown
        """
        notes = []

        # Effective Gross Income
        vacancy_loss = gross_annual_rent * vacancy_rate
        effective_gross = gross_annual_rent + other_income - vacancy_loss

        # Management expense (minimum 8%)
        min_management = gross_annual_rent * self.MIN_MANAGEMENT_RATE
        if management_expense is None or management_expense < min_management:
            management_expense = min_management
            notes.append(f"Management set to minimum 8% = ${min_management:,.0f}")

        # Repairs & maintenance minimums
        if is_new_construction:
            min_repairs = units * self.MIN_REPAIRS_PER_UNIT_NEW
        else:
            min_repairs = units * self.MIN_REPAIRS_PER_UNIT_EXISTING

        if repairs_expense is None or repairs_expense < min_repairs:
            repairs_expense = min_repairs
            notes.append(f"Repairs set to minimum ${min_repairs:,.0f}/year")

        # Total operating expenses
        total_opex = (
            management_expense +
            repairs_expense +
            insurance_expense +
            taxes_expense +
            utilities_expense +
            hoa_expense +
            other_expenses
        )

        # Net Operating Income
        noi = effective_gross - total_opex

        # Capital reserves minimums
        if is_new_construction:
            min_capex = units * self.MIN_CAPEX_PER_UNIT_SFR_NEW
        else:
            min_capex = units * self.MIN_CAPEX_PER_UNIT_MULTI

        if capex_reserves is None or capex_reserves < min_capex:
            capex_reserves = min_capex
            notes.append(f"CapEx reserves set to minimum ${min_capex:,.0f}/year")

        # Net Cash Flow
        ncf = noi - capex_reserves

        # NCF DSCR
        if annual_debt_service > 0:
            ncf_dscr = ncf / annual_debt_service
        else:
            ncf_dscr = 0.0

        # Expense ratio
        expense_ratio = total_opex / gross_annual_rent if gross_annual_rent > 0 else 0

        return NCFResult(
            gross_rent=gross_annual_rent,
            effective_gross_income=round(effective_gross, 2),
            vacancy_loss=round(vacancy_loss, 2),
            operating_expenses=round(total_opex, 2),
            net_operating_income=round(noi, 2),
            capital_reserves=round(capex_reserves, 2),
            net_cash_flow=round(ncf, 2),
            annual_debt_service=annual_debt_service,
            ncf_dscr=round(ncf_dscr, 3),
            expense_ratio=round(expense_ratio, 3),
            notes=notes
        )


# =============================================================================
# CONVENIENCE FUNCTIONS
# =============================================================================

def quick_dscr_check(
    monthly_rent: float,
    monthly_pitia: float,
    fico: int = 720,
    is_foreign_national: bool = False
) -> Tuple[float, bool, str]:
    """
    Quick DSCR eligibility check.

    Args:
        monthly_rent: Monthly qualifying rent
        monthly_pitia: Monthly PITIA
        fico: Credit score
        is_foreign_national: FN status

    Returns:
        Tuple of (dscr, meets_minimum, status_message)
    """
    calc = DSCRCalculator()

    dscr = calc.calculate_dscr(monthly_rent, monthly_pitia)
    min_dscr = calc.get_minimum_dscr(fico, is_foreign_national)
    meets = dscr >= min_dscr

    if meets:
        status = f"DSCR {dscr:.2f}x meets {min_dscr:.2f}x minimum"
    else:
        status = f"DSCR {dscr:.2f}x below {min_dscr:.2f}x minimum"

    return (dscr, meets, status)


def calculate_max_loan_from_dscr(
    qualifying_rent: float,
    target_dscr: float,
    interest_rate: float,
    annual_taxes: float,
    annual_insurance: float,
    monthly_hoa: float = 0.0,
    loan_term_months: int = 360,
    is_interest_only: bool = False
) -> float:
    """
    Calculate maximum loan amount to achieve target DSCR.

    Args:
        qualifying_rent: Monthly qualifying rent
        target_dscr: Target DSCR (e.g., 1.00)
        interest_rate: Annual interest rate
        annual_taxes: Annual property taxes
        annual_insurance: Annual insurance
        monthly_hoa: Monthly HOA
        loan_term_months: Loan term in months
        is_interest_only: Interest-only flag

    Returns:
        Maximum loan amount
    """
    # Target PITIA = Rent / DSCR
    target_pitia = qualifying_rent / target_dscr

    # TIA component
    monthly_tia = (annual_taxes + annual_insurance) / 12 + monthly_hoa

    # Maximum P&I
    max_pi = target_pitia - monthly_tia

    if max_pi <= 0:
        return 0.0

    monthly_rate = interest_rate / 12

    if is_interest_only:
        # Interest-only: PI = Loan * rate/12
        max_loan = max_pi / monthly_rate if monthly_rate > 0 else 0
    else:
        # Amortizing: solve for loan amount
        if monthly_rate > 0 and loan_term_months > 0:
            factor = (
                (1 + monthly_rate) ** loan_term_months - 1
            ) / (
                monthly_rate * (1 + monthly_rate) ** loan_term_months
            )
            max_loan = max_pi * factor
        else:
            max_loan = max_pi * loan_term_months

    return round(max_loan, 2)
