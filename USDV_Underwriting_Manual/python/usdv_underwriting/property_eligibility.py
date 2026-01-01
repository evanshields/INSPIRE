"""
Property Eligibility Module
USDV Capital Underwriting Library

This module provides property eligibility checks for both
RTL and DSCR loan products.

Manual Reference: Section 5 - Property Eligibility Standards
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict
from enum import Enum

from .common import (
    PropertyType, LoanProduct, ConditionRating,
    MIN_SQ_FT_SFR, MIN_SQ_FT_CONDO, MIN_SQ_FT_MULTI,
    MAX_ACREAGE, INELIGIBLE_STATES
)


# =============================================================================
# DATA CLASSES
# =============================================================================

@dataclass
class PropertyEligibilityResult:
    """Result of property eligibility check."""
    is_eligible: bool
    property_type: PropertyType
    loan_products_eligible: List[LoanProduct]
    loan_products_ineligible: List[LoanProduct]
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)


@dataclass
class CondoWarrantabilityResult:
    """Result of condo warrantability check."""
    is_warrantable: bool
    failures: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)


# =============================================================================
# PROPERTY ELIGIBILITY CHECKER
# =============================================================================

class PropertyEligibilityChecker:
    """
    Check property eligibility for USDV loan products.

    Implements eligibility rules per Section 5 of the manual.
    """

    # Ineligible property types
    INELIGIBLE_TYPES = [
        PropertyType.MANUFACTURED,
    ]

    # Minimum square footage requirements (EastView standard)
    MIN_SQ_FT = {
        PropertyType.SFR: 600,
        PropertyType.TOWNHOME: 600,
        PropertyType.PUD: 600,
        PropertyType.CONDO_WARRANTABLE: 500,
        PropertyType.CONDO_NON_WARRANTABLE: 500,
        PropertyType.TWO_TO_FOUR_UNIT: 500,
        PropertyType.FIVE_TO_NINE_UNIT: 500,
    }

    # Ineligible states
    INELIGIBLE_STATES = ["ND", "SD", "AK", "HI"]

    # Maximum acreage
    MAX_ACREAGE = 5.0

    # Product eligibility by property type
    PRODUCT_ELIGIBILITY = {
        PropertyType.SFR: [
            LoanProduct.FIX_AND_FLIP,
            LoanProduct.BRIDGE,
            LoanProduct.BRIDGE_PLUS,
            LoanProduct.GROUND_UP_CONSTRUCTION,
            LoanProduct.DSCR,
            LoanProduct.DSCR_5_9,
        ],
        PropertyType.TOWNHOME: [
            LoanProduct.FIX_AND_FLIP,
            LoanProduct.BRIDGE,
            LoanProduct.BRIDGE_PLUS,
            LoanProduct.DSCR,
        ],
        PropertyType.PUD: [
            LoanProduct.FIX_AND_FLIP,
            LoanProduct.BRIDGE,
            LoanProduct.BRIDGE_PLUS,
            LoanProduct.GROUND_UP_CONSTRUCTION,
            LoanProduct.DSCR,
        ],
        PropertyType.CONDO_WARRANTABLE: [
            LoanProduct.FIX_AND_FLIP,
            LoanProduct.BRIDGE,
            LoanProduct.BRIDGE_PLUS,
            LoanProduct.DSCR,
        ],
        PropertyType.CONDO_NON_WARRANTABLE: [
            LoanProduct.FIX_AND_FLIP,
            LoanProduct.BRIDGE,
            # Note: Bridge Plus and DSCR require case-by-case
        ],
        PropertyType.TWO_TO_FOUR_UNIT: [
            LoanProduct.FIX_AND_FLIP,
            LoanProduct.BRIDGE,
            LoanProduct.BRIDGE_PLUS,
            LoanProduct.DSCR,
        ],
        PropertyType.FIVE_TO_NINE_UNIT: [
            LoanProduct.DSCR_5_9,
            LoanProduct.FIX_AND_FLIP,  # With restrictions
        ],
    }

    # Condition rating eligibility
    INELIGIBLE_CONDITIONS = [
        ConditionRating.C6,  # Not eligible without exception
    ]

    RESTRICTED_CONDITIONS = [
        ConditionRating.C5,  # May require exception
    ]

    def check_property_type(
        self,
        property_type: PropertyType
    ) -> tuple[bool, List[str]]:
        """
        Check if property type is eligible.

        Args:
            property_type: Property type

        Returns:
            Tuple of (is_eligible, errors)
        """
        errors = []

        if property_type in self.INELIGIBLE_TYPES:
            errors.append(f"Property type '{property_type.value}' is not eligible")
            return (False, errors)

        return (True, errors)

    def check_square_footage(
        self,
        property_type: PropertyType,
        square_footage: float,
        units: int = 1
    ) -> tuple[bool, List[str]]:
        """
        Check minimum square footage requirements.

        Args:
            property_type: Property type
            square_footage: Total or per-unit square footage
            units: Number of units (for multi-unit)

        Returns:
            Tuple of (is_eligible, errors)
        """
        errors = []
        min_sf = self.MIN_SQ_FT.get(property_type, 600)

        if units > 1:
            # For multi-unit, check per-unit average
            avg_sf = square_footage / units
            if avg_sf < min_sf:
                errors.append(
                    f"Average unit size {avg_sf:.0f} sq ft is below minimum "
                    f"{min_sf} sq ft per unit."
                )
                return (False, errors)
        else:
            if square_footage < min_sf:
                errors.append(
                    f"Property {square_footage} sq ft is below minimum "
                    f"{min_sf} sq ft for {property_type.value}."
                )
                return (False, errors)

        return (True, errors)

    def check_state(self, state: str) -> tuple[bool, List[str]]:
        """
        Check if state is eligible.

        Args:
            state: State abbreviation

        Returns:
            Tuple of (is_eligible, errors)
        """
        errors = []
        state_upper = state.upper()

        if state_upper in self.INELIGIBLE_STATES:
            errors.append(f"State '{state_upper}' is not eligible for financing")
            return (False, errors)

        return (True, errors)

    def check_acreage(self, acreage: float) -> tuple[bool, List[str], List[str]]:
        """
        Check acreage requirements.

        Args:
            acreage: Property acreage

        Returns:
            Tuple of (is_eligible, errors, warnings)
        """
        errors = []
        warnings = []

        if acreage > self.MAX_ACREAGE:
            errors.append(
                f"Property acreage {acreage:.2f} exceeds maximum {self.MAX_ACREAGE} acres"
            )
            return (False, errors, warnings)

        if acreage > 2.0:
            warnings.append(
                f"Property acreage {acreage:.2f} is elevated; may require additional review"
            )

        return (True, errors, warnings)

    def check_rural_status(self, is_rural: bool) -> tuple[bool, List[str]]:
        """
        Check rural property status.

        Args:
            is_rural: Whether property is classified as rural

        Returns:
            Tuple of (is_eligible, errors)
        """
        errors = []

        if is_rural:
            errors.append("Rural properties are not eligible for financing")
            return (False, errors)

        return (True, errors)

    def check_condition(
        self,
        condition: ConditionRating
    ) -> tuple[bool, List[str], List[str]]:
        """
        Check property condition rating.

        Args:
            condition: UAD condition rating (C1-C6)

        Returns:
            Tuple of (is_eligible, errors, warnings)
        """
        errors = []
        warnings = []

        if condition in self.INELIGIBLE_CONDITIONS:
            errors.append(
                f"Condition rating {condition.value} is not eligible without exception"
            )
            return (False, errors, warnings)

        if condition in self.RESTRICTED_CONDITIONS:
            warnings.append(
                f"Condition rating {condition.value} may require exception approval"
            )

        return (True, errors, warnings)

    def check_condo_warrantability(
        self,
        project_complete: bool = True,
        developer_control: bool = False,
        single_entity_ownership_pct: float = 0.0,
        commercial_space_pct: float = 0.0,
        rental_pct: float = 0.0,
        hoa_delinquency_pct: float = 0.0,
        pending_litigation: bool = False,
        allows_str: bool = False
    ) -> CondoWarrantabilityResult:
        """
        Check condo warrantability per Fannie Mae standards.

        Args:
            project_complete: Whether project is fully complete
            developer_control: Whether developer still controls HOA
            single_entity_ownership_pct: % owned by single entity
            commercial_space_pct: % of building as commercial
            rental_pct: % of units as rentals
            hoa_delinquency_pct: % of units delinquent on HOA
            pending_litigation: Whether there's pending litigation
            allows_str: Whether HOA permits short-term rentals

        Returns:
            CondoWarrantabilityResult
        """
        failures = []
        notes = []

        # Project completion
        if not project_complete:
            failures.append("Project is not yet complete")

        # Developer control
        if developer_control:
            failures.append("Developer has not turned over control to HOA")

        # Single entity ownership (>10%)
        if single_entity_ownership_pct > 10.0:
            failures.append(
                f"Single entity owns {single_entity_ownership_pct:.1f}% of units (max 10%)"
            )

        # Commercial space (>25%)
        if commercial_space_pct > 25.0:
            failures.append(
                f"Commercial space is {commercial_space_pct:.1f}% of building (max 25%)"
            )

        # Rental percentage (>50%)
        if rental_pct > 50.0:
            failures.append(
                f"Rental units are {rental_pct:.1f}% of project (max 50%)"
            )

        # HOA delinquency (>15%)
        if hoa_delinquency_pct > 15.0:
            failures.append(
                f"HOA delinquency is {hoa_delinquency_pct:.1f}% (max 15%)"
            )

        # Pending litigation
        if pending_litigation:
            failures.append("Pending litigation associated with HOA")

        # Short-term rentals
        if allows_str:
            notes.append("HOA permits short-term rentals")

        is_warrantable = len(failures) == 0

        return CondoWarrantabilityResult(
            is_warrantable=is_warrantable,
            failures=failures,
            notes=notes
        )

    def get_eligible_products(
        self,
        property_type: PropertyType,
        is_warrantable_condo: bool = True,
        units: int = 1
    ) -> List[LoanProduct]:
        """
        Get list of eligible loan products for property.

        Args:
            property_type: Property type
            is_warrantable_condo: Whether condo is warrantable
            units: Number of units

        Returns:
            List of eligible loan products
        """
        # Handle condo warrantability
        if property_type == PropertyType.CONDO_NON_WARRANTABLE:
            return self.PRODUCT_ELIGIBILITY.get(property_type, [])

        if property_type == PropertyType.CONDO_WARRANTABLE and not is_warrantable_condo:
            # Non-warrantable condo
            return self.PRODUCT_ELIGIBILITY.get(PropertyType.CONDO_NON_WARRANTABLE, [])

        # Handle 5-9 units
        if units >= 5:
            return self.PRODUCT_ELIGIBILITY.get(PropertyType.FIVE_TO_NINE_UNIT, [])

        return self.PRODUCT_ELIGIBILITY.get(property_type, [])

    def check_eligibility(
        self,
        property_type: PropertyType,
        state: str,
        square_footage: float,
        units: int = 1,
        acreage: float = 0.25,
        is_rural: bool = False,
        condition: Optional[ConditionRating] = None,
        is_warrantable_condo: bool = True
    ) -> PropertyEligibilityResult:
        """
        Complete property eligibility check.

        Args:
            property_type: Property type
            state: State abbreviation
            square_footage: Square footage (total or per unit)
            units: Number of units
            acreage: Property acreage
            is_rural: Whether classified as rural
            condition: UAD condition rating
            is_warrantable_condo: Whether condo is warrantable

        Returns:
            Complete PropertyEligibilityResult
        """
        errors = []
        warnings = []
        notes = []

        # Property type check
        type_ok, type_errors = self.check_property_type(property_type)
        errors.extend(type_errors)

        # State check
        state_ok, state_errors = self.check_state(state)
        errors.extend(state_errors)

        # Square footage check
        sqft_ok, sqft_errors = self.check_square_footage(
            property_type, square_footage, units
        )
        errors.extend(sqft_errors)

        # Acreage check
        acre_ok, acre_errors, acre_warnings = self.check_acreage(acreage)
        errors.extend(acre_errors)
        warnings.extend(acre_warnings)

        # Rural check
        rural_ok, rural_errors = self.check_rural_status(is_rural)
        errors.extend(rural_errors)

        # Condition check
        if condition:
            cond_ok, cond_errors, cond_warnings = self.check_condition(condition)
            errors.extend(cond_errors)
            warnings.extend(cond_warnings)

        # Determine eligibility
        is_eligible = len(errors) == 0

        # Get eligible products
        eligible_products = self.get_eligible_products(
            property_type, is_warrantable_condo, units
        )

        # Determine ineligible products
        all_products = [
            LoanProduct.FIX_AND_FLIP,
            LoanProduct.BRIDGE,
            LoanProduct.BRIDGE_PLUS,
            LoanProduct.GROUND_UP_CONSTRUCTION,
            LoanProduct.DSCR,
            LoanProduct.DSCR_5_9,
        ]
        ineligible_products = [p for p in all_products if p not in eligible_products]

        # Add notes
        if property_type in [PropertyType.CONDO_WARRANTABLE, PropertyType.CONDO_NON_WARRANTABLE]:
            if is_warrantable_condo:
                notes.append("Condo is warrantable - full product availability")
            else:
                notes.append("Condo is non-warrantable - restricted products")

        if units >= 5:
            notes.append(f"5-9 unit property ({units} units) - commercial underwriting applies")

        return PropertyEligibilityResult(
            is_eligible=is_eligible,
            property_type=property_type,
            loan_products_eligible=eligible_products,
            loan_products_ineligible=ineligible_products,
            errors=errors,
            warnings=warnings,
            notes=notes
        )


# =============================================================================
# CONVENIENCE FUNCTIONS
# =============================================================================

def check_property_eligible(
    property_type: str,
    state: str,
    square_footage: float,
    units: int = 1
) -> Dict:
    """
    Quick property eligibility check.

    Args:
        property_type: Property type string (sfr, townhome, condo, etc.)
        state: State abbreviation
        square_footage: Square footage
        units: Number of units

    Returns:
        Dict with is_eligible, errors, eligible_products
    """
    type_map = {
        "sfr": PropertyType.SFR,
        "townhome": PropertyType.TOWNHOME,
        "pud": PropertyType.PUD,
        "condo": PropertyType.CONDO_WARRANTABLE,
        "condo_nw": PropertyType.CONDO_NON_WARRANTABLE,
        "2-4": PropertyType.TWO_TO_FOUR_UNIT,
        "5-9": PropertyType.FIVE_TO_NINE_UNIT,
    }

    prop_type = type_map.get(property_type.lower(), PropertyType.SFR)

    checker = PropertyEligibilityChecker()
    result = checker.check_eligibility(
        property_type=prop_type,
        state=state,
        square_footage=square_footage,
        units=units
    )

    return {
        "is_eligible": result.is_eligible,
        "errors": result.errors,
        "warnings": result.warnings,
        "eligible_products": [p.value for p in result.loan_products_eligible]
    }


def check_condo_warrantable(
    project_complete: bool = True,
    developer_control: bool = False,
    single_entity_pct: float = 0.0,
    commercial_pct: float = 0.0,
    rental_pct: float = 0.0,
    hoa_delinquency_pct: float = 0.0,
    pending_litigation: bool = False
) -> Dict:
    """
    Quick condo warrantability check.

    Returns:
        Dict with is_warrantable and failures
    """
    checker = PropertyEligibilityChecker()
    result = checker.check_condo_warrantability(
        project_complete=project_complete,
        developer_control=developer_control,
        single_entity_ownership_pct=single_entity_pct,
        commercial_space_pct=commercial_pct,
        rental_pct=rental_pct,
        hoa_delinquency_pct=hoa_delinquency_pct,
        pending_litigation=pending_litigation
    )

    return {
        "is_warrantable": result.is_warrantable,
        "failures": result.failures,
        "notes": result.notes
    }
