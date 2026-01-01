---
section: 3
title: Entity & Guarantor Analysis
version: 1.1
last_updated: 2025-12-30
model_used: haiku
guideline_sources:
  - Archwest RTL Guidelines v6.0
  - Eastview RTL Guidelines v4.1
  - Archwest DSCR Guidelines v1.8
  - Eastview DSCR Guidelines v7.2
changelog:
  - 2025-12-30: Updated with investor-validated requirements; clarified guarantor thresholds to 51% minimum; marked Series LLC ineligible for DSCR; updated Python code
  - 2025-12-30: Initial creation
---

# Section 3: Entity & Guarantor Analysis

## 3.1 Overview

This section addresses borrowing entity structure, ownership documentation, and guarantor requirements. All USDV loans are made to business entities (never to individuals as sole proprietorships). Understanding entity composition, ownership percentages, and guarantor strength is critical for credit analysis and legal enforceability.

**Key Principle:** All loans require **full recourse to at least 51% of entity ownership** via personal guarantees, with 100% recourse preferred.

**INSPIRE Integration Points:**
- Phase 1-2: Entity data collection during application
- Phase 5-6: Entity document checklist and good standing verification

---

## 3.2 Eligible Entity Types (By Product)

### 3.2.1 LLCs (Limited Liability Companies)

**Overview:**
LLCs are pass-through entities that combine liability protection with operational flexibility. They are the most common entity type for USDV borrowers (85%+ of loans).

**Eligible Structures:**
- **Single-Member LLC**: One owner, typically an individual
- **Multi-Member LLC**: Multiple owners, can be individuals, corporations, or other entities

**Requirements:**
- Valid Articles of Organization filed in state of formation
- Operating Agreement clearly identifying ownership percentages and management rights
- EIN letter or most recent tax return (verify entity name and tax ID)
- Certificate of Good Standing from state of formation and property state (if different)

**Guarantor Requirements:**
- Single-member LLCs: Individual member must guarantee
- Multi-member LLCs: All members with 20%+ ownership must be identified; at least 51% aggregate of ownership must guarantee
- Key principals (managing members) must guarantee regardless of ownership %

**Product Eligibility:**
- ✓ Fix & Flip, GUC, Bridge, Bridge Plus, DSCR

---

### 3.2.2 Limited Partnerships (LP)

**Overview:**
Limited Partnerships allow investors to raise capital from passive investors (Limited Partners) while maintaining control through General Partner(s).

**Eligible Structures:**
- General Partner (GP) must be an LLC or corporation
- Limited Partners (LP) contribute capital but have no management role
- Can have one or multiple GPs and/or LPs

**Requirements:**
- Certificate of Limited Partnership filed with state
- Limited Partnership Agreement identifying GP and LP roles/percentages
- Certificate of Good Standing
- Corporate documents for GP entity (if LLC/Corp)

**Guarantor Requirements:**
- All General Partners must guarantee (control entity)
- Limited Partners do NOT guarantee (passive investors)
- If GP is entity, owners of GP with 20%+ must also guarantee
- Minimum 51% of overall LP ownership must guarantee (typically GP achieves this)

**Product Eligibility:**
- ✓ Fix & Flip, GUC, Bridge, Bridge Plus, DSCR

---

### 3.2.3 S-Corporations

**Overview:**
S-Corp structure provides liability protection and may offer tax benefits. Less common for USDV but acceptable.

**Requirements:**
- Articles of Incorporation and bylaws filed with state
- IRS Form 2553 confirming S-Corp election status
- Shareholder Registry showing ownership percentages
- Corporate Resolution authorizing loan and guaranty
- Certificate of Good Standing

**Guarantor Requirements:**
- All shareholders with 20%+ ownership must guarantee
- Minimum 51% aggregate of shareholders must guarantee
- Key officers (President, CEO) must guarantee regardless of ownership %

**Product Eligibility:**
- ✓ Fix & Flip, GUC, Bridge, Bridge Plus, DSCR

---

### 3.2.4 C-Corporations

**Overview:**
C-Corp structure with full double taxation. Used occasionally for established businesses or acquisition vehicles.

**Requirements:**
- Articles of Incorporation and bylaws filed with state
- Shareholder Registry showing ownership percentages
- Corporate Resolution authorizing loan and guaranty
- Most recent K-1 or corporate tax return
- Certificate of Good Standing

**Guarantor Requirements:**
- All shareholders with 20%+ ownership must guarantee
- Minimum 51% aggregate of shareholders must guarantee
- All officers must guarantee

**Product Eligibility:**
- ✓ Fix & Flip, GUC, Bridge, Bridge Plus, DSCR

---

### 3.2.5 Trusts

**Overview:**
Trusts can be used as borrowing entities for certain scenarios. Different trust types have different guarantor requirements.

#### Revocable (Living) Trusts
**Definition:** Trust that can be modified or revoked by grantor during grantor's lifetime; becomes irrevocable at death.

**Requirements:**
- Full copy of Trust Agreement (with signature pages)
- Certification of Trust (may be used instead of full agreement for privacy)
- Trustee identification and acceptance
- Certificate of Good Standing (if trustee is entity)

**Guarantor Requirements:**
- **Both trustee AND grantor/owner must execute personal guaranties**
- If trustee is entity (LLC, corp), owners of trustee with 20%+ must also guarantee
- Grantor (settlor) must guarantee even if not trustee

**Product Eligibility:**
- ✓ Fix & Flip, GUC, Bridge, Bridge Plus, DSCR

#### Irrevocable Trusts
**Definition:** Trust that cannot be modified or revoked after creation; typically used for tax planning or asset protection.

**Requirements:**
- Full copy of Trust Agreement required
- Trustee identification and acceptance
- Certification of beneficiaries and their interests
- Certificate of Good Standing (if trustee is entity)

**Guarantor Requirements:**
- Trustee must guarantee (managing party)
- If trustee is entity, 20%+ owners of trustee must guarantee
- Beneficiaries may be required to guarantee depending on structure (case-by-case)
- Case-by-case approval required

**Product Eligibility:**
- ✓ Fix & Flip, GUC, Bridge, Bridge Plus, DSCR (case-by-case)

#### Land Trusts
**Definition:** Trust used to hold real property title, with beneficial ownership held separately (common in some states).

**Requirements:**
- Trust Agreement for land trust
- Identification of beneficial owner(s)
- Certificate of Good Standing in property state
- Title held in trustee name

**Guarantor Requirements:**
- Beneficial owner(s) must guarantee (they are the actual parties to the transaction)
- Trustee may guarantee as secondary guarantor
- All beneficial owners with 20%+ interest must guarantee

**Product Eligibility:**
- ✓ Fix & Flip, GUC, Bridge, Bridge Plus, DSCR (limited applicability)

---

### 3.2.6 Ineligible Entity Types

The following entity types are **NOT eligible** for any USDV Capital loan:

- **Sole Proprietorships**: No liability protection; individual name on loan
- **General Partnerships**: Unlimited liability for all partners
- **Series LLCs**: **EXPLICITLY INELIGIBLE for DSCR products** (per ArchWest DSCR Guidelines); RTL case-by-case review only
- **Non-Profit Organizations**: USDV lends only for profit-generating activities
- **Government Entities**: Federal, state, local agencies
- **Foreign Entities**: Non-U.S. based entities (though foreign nationals can own U.S. entities)

---

## 3.3 Ownership Structure Analysis

### 3.3.1 Guarantor Identification & Requirements

**Primary Rule: 51% Minimum Aggregate Guaranty**

All loans must have personal guaranties from individuals representing **at least 51% of entity ownership**. Additionally, any individual or family unit with **20% or greater direct or indirect ownership** must be identified for credit analysis and potential guaranty requirement.

**Ownership Tiers:**
- **20%-49% ownership**: Must be identified; may be included in 51% aggregate guaranty
- **50%+ ownership**: Must be identified; must guarantee individually or as part of aggregate
- **Key Principal (regardless of ownership %)**: Must guarantee (managing member, CEO, president, etc.)

**Aggregation Rules:**
- Guarantors can be aggregated to meet 51% minimum (e.g., 30% owner + 30% owner + 25% owner = 85% aggregate = sufficient)
- Must have documented commitment from each guarantor
- Each guarantor's capacity independently assessed (credit, liquidity, experience)

**100% Recourse (Preferred):**
- Ideal structure is 100% of owners execute personal guaranties
- Achievable in single-owner or equal multi-owner structures
- Recommended for all loans when feasible

**51% Recourse (Minimum Exception):**
- Allowed when strong compensating factors exist
- Requires documented exception approval
- Must show clear 51% ownership attribution
- Remaining owners still require documentation (even if not guaranteeing)

### 3.3.2 Nested Entity Structures

**Definition:** One entity (e.g., LLC) is owned, in whole or in part, by another entity rather than directly by individuals.

**Transparency Requirement:**
- All layers of ownership must be fully disclosed (up to ultimate beneficial individuals)
- Organizational charts required showing ownership at each level
- Formation documents for each entity in the chain required

**Analysis Process:**
1. Identify all entities in ownership chain
2. Trace to ultimate individual beneficial owners
3. Calculate indirect ownership percentages at each level
4. Apply 20% and 51% rules at ultimate individual level
5. Require guaranties from individuals meeting 20%+ indirect ownership

**Example:**
```
Property LLC (100%)
  ↓ owned by
Holding LLC (100%)
  ↓ owned 40% by
Individual A, 30% by Individual B, 30% by Individual C LLC
  ↓ Individual C LLC is 60% owned by
Individual D, 40% by Individual E

Guarantor Requirements:
- Individual A: Direct 40% → MUST GUARANTEE
- Individual B: Direct 30% → MUST GUARANTEE
- Individual D: Indirect 18% (30% × 60%) → below 20%, document only
- Individual E: Indirect 12% (30% × 40%) → below 20%, document only
- Need guarantee from minimum 51%: A+B = 70% ✓
```

### 3.3.3 Spousal Considerations

**Community Property States:**
- AZ, CA, ID, LA, NV, NM, TX, WA, WI (+ AL, KY with opt-in)
- If borrower is married and resides in community property state, spouse may need to sign or guarantee
- Community property status affects lien enforceability
- Recommend spousal signature on all loan documents for clarity

**Non-Community Property States:**
- Spouse signature generally not required unless also on deed or own property
- However, spousal guaranty may strengthen credit (if spouse has income/assets)

---

## 3.4 Guarantor Qualifications

### 3.4.1 Minimum Guarantor Credit Qualifications

All personal guarantors must meet the following minimum standards:

**Credit Score:**
- Minimum FICO: 660 (RTL products), 680 (DSCR products)
- Must have tri-merge credit report within 90 days of loan origination
- Using lower of two scores or median of three scores

**Credit History:**
- No active bankruptcies
- Maximum 2 x 30-day lates in past 24 months (1 x 30 x 12 delinquency standard)
- Foreclosures: 2+ years seasoning (RTL), 4+ years seasoning (DSCR)
- Judgments/Liens >$10K (RTL) or >$5K (DSCR): Must be paid, in payment plan, or satisfactorily resolved

**Background Check:**
- No financial fraud convictions
- No OFAC/Sanctions matches
- No active litigation (except standard civil matters)

### 3.4.2 Financial Capacity

**Liquidity:**
- Guarantors must demonstrate adequate post-closing liquidity to cover carrying costs, debt service, or unexpected needs
- Liquidity requirements vary by product and borrower classification (detailed in Section 2)
- Sources: Bank statements, investments, retirement accounts, lines of credit (documented within 2 months of closing)

**Net Worth:**
- Should be commensurate with loan amount
- Guideline: Net worth ≥ 25-50% of loan amount (risk-based assessment)
- Calculated from personal financial statement (PFS) provided at application

**Real Estate Experience:**
- Guarantor should have relevant real estate experience for product (see Section 2)
- For RTL products: Construction/renovation/investment experience required
- For DSCR: Rental property management experience preferred but not mandatory

### 3.4.3 Multiple Guarantor Scenarios

**Joint & Several Liability:**
- When multiple individuals guarantee, each is individually liable for entire debt
- Lender can pursue any or all guarantors for full repayment
- Aggregated qualifications may be used if individual guarantors are weaker

**Combined Analysis:**
- Use highest FICO of guarantors for loan qualification
- Combine liquidity from multiple guarantors to meet requirements
- Credit analysis considers guarantor group as whole (not individually)
- Each guarantor still must be identified and documented

### 3.4.4 "Warm Body" Waiver (Exception)

**ArchWest DSCR Guideline:** Guaranty can be waived if:
- Entity net worth >250% of total loan amount AND
- Entity liquidity >100% of total loan amount
- Requires SVP of Credit approval

**Use Case:**
- Established companies with strong balance sheets
- Minimal benefit of individual guarantee (entity strength is sufficient)
- Documentation must show clear 250%/100% thresholds

**USDV Standard:** Allow as exception with strong compensating factors; recommend requiring at least 51% ownership guaranty even with strong entity position.

### 3.4.5 Carve-Out (Bad Boy) Guarantee

**Definition:**
A carve-out guaranty (aka "bad boy" guarantee) makes guarantor personally liable for specific, intentional acts or inactions that harm the lender.

**Typical Carve-Outs:**
- Fraud or misrepresentation
- Misappropriation or misuse of funds
- Material breach of loan covenants (intentional)
- Voluntary bankruptcy (of guarantor or entity)
- Environmental violations or hazards

**USDV Standard:**
- Carve-out guaranties standard for all loans
- Provides lender recourse for borrower malfeasance
- Does not eliminate primary guaranty obligation
- Added layer of protection beyond standard guaranty

---

## 3.5 Entity Formation, Standing & Documentation

### 3.5.1 Formation Requirements

**U.S. Domicile:**
- All entities must be formed in a U.S. state or territory
- Foreign entities must be registered in the state where property is located
- Canadian/Caribbean entities acceptable only on case-by-case basis with legal review

**Good Standing:**
- Certificate of Good Standing from state of formation (must be dated within 90 days of closing)
- If property located in different state: Certificate of Good Standing from property state as well
- If obtained more than 90 days before closing: Secretary of State must confirm entity still in good standing at closing

**Registration:**
- Multi-state operations require registration as "foreign entity" in each state where business is conducted
- Property state registration mandatory if different from formation state
- Failure to register can create lien/liability exposure to lender

### 3.5.2 Required Entity Documentation

**All Entities:**
- Certificate of Formation/Articles of Organization/Incorporation (founding documents)
- Certificate of Good Standing (both states if applicable, dated <90 days)
- EIN Letter from IRS or most recent tax return (verify entity name, EIN, tax status)
- Current Operating Agreement / Bylaws / Partnership Agreement (governing documents)
- Organizational Chart (if nested/complex ownership)

**LLCs:**
- Operating Agreement with signature pages
- Member Registry or Schedule showing ownership percentages
- Certificate of Authority (if exists)
- Manager Certification or Unanimous Consent to Borrow

**Corporations:**
- Bylaws with current amendments
- Corporate Resolution authorizing loan and guaranty
- Board Meeting Minutes approving the transaction (or Unanimous Written Consent)
- Shareholder Registry or capitalization table
- Certification of Good Standing and Corporate Status

**Partnerships:**
- Partnership Agreement
- Certificate of Limited Partnership (for LPs)
- General Partner entity documents
- Partner Registry showing percentages

**Trusts:**
- Full Trust Agreement (or Certification of Trust if privacy preferred)
- Trustee acceptance/certification
- Trust registration (if applicable by state)
- Certificate of Good Standing (if trustee is entity)
- Affidavit of Trust (may be required at closing)

---

## 3.6 Python Implementation: Entity Analysis & Guarantor Validation

```python
from enum import Enum
from dataclasses import dataclass
from typing import List, Optional, Tuple
from decimal import Decimal


class EntityType(Enum):
    """Eligible borrowing entity types."""
    LLC = "llc"
    MULTI_MEMBER_LLC = "multi_member_llc"
    SERIES_LLC = "series_llc"
    LIMITED_PARTNERSHIP = "limited_partnership"
    S_CORPORATION = "s_corporation"
    C_CORPORATION = "c_corporation"
    REVOCABLE_TRUST = "revocable_trust"
    IRREVOCABLE_TRUST = "irrevocable_trust"
    LAND_TRUST = "land_trust"
    SOLE_PROPRIETORSHIP = "sole_proprietorship"
    GENERAL_PARTNERSHIP = "general_partnership"
    NON_PROFIT = "non_profit"


class LoanType(Enum):
    """Loan product types."""
    FIX_FLIP = "fix_flip"
    GROUND_UP_CONSTRUCTION = "guc"
    BRIDGE = "bridge"
    BRIDGE_PLUS = "bridge_plus"
    DSCR = "dscr"


@dataclass
class Owner:
    """Represents an owner within an entity structure."""
    name: str
    ownership_percentage: float  # 0.20 = 20%
    is_individual: bool
    entity_type: Optional[EntityType] = None  # If owner is another entity
    is_key_principal: bool = False  # Explicitly designated as key principal
    fico: Optional[int] = None  # For individual owners/guarantors
    experience_deals: Optional[int] = None  # For individual owners/guarantors
    
    def __hash__(self):
        return hash(self.name)
    
    def __eq__(self, other):
        return self.name == other.name


@dataclass
class OwnershipAnalysis:
    """Results of ownership structure analysis."""
    all_owners: List[Owner]
    guarantors_required: List[Owner]
    guarantor_aggregate_percentage: float  # e.g., 0.85 for 85%
    has_nested_entities: bool
    is_eligible: bool
    issues: List[str]
    warnings: List[str]


class EntityAnalyzer:
    """
    Analyzes entity structure and guarantor requirements.
    Validates against USDV guidelines and investor requirements.
    """
    
    # Entity eligibility by loan product
    ELIGIBLE_ENTITIES_BY_PRODUCT = {
        LoanType.FIX_FLIP: [
            EntityType.LLC, EntityType.MULTI_MEMBER_LLC,
            EntityType.LIMITED_PARTNERSHIP,
            EntityType.S_CORPORATION, EntityType.C_CORPORATION,
            EntityType.REVOCABLE_TRUST, EntityType.IRREVOCABLE_TRUST,
            EntityType.LAND_TRUST,
        ],
        LoanType.GROUND_UP_CONSTRUCTION: [
            EntityType.LLC, EntityType.MULTI_MEMBER_LLC,
            EntityType.LIMITED_PARTNERSHIP,
            EntityType.S_CORPORATION, EntityType.C_CORPORATION,
            EntityType.REVOCABLE_TRUST, EntityType.IRREVOCABLE_TRUST,
            EntityType.LAND_TRUST,
        ],
        LoanType.BRIDGE: [
            EntityType.LLC, EntityType.MULTI_MEMBER_LLC,
            EntityType.LIMITED_PARTNERSHIP,
            EntityType.S_CORPORATION, EntityType.C_CORPORATION,
            EntityType.REVOCABLE_TRUST, EntityType.IRREVOCABLE_TRUST,
            EntityType.LAND_TRUST,
        ],
        LoanType.BRIDGE_PLUS: [
            EntityType.LLC, EntityType.MULTI_MEMBER_LLC,
            EntityType.LIMITED_PARTNERSHIP,
            EntityType.S_CORPORATION, EntityType.C_CORPORATION,
            EntityType.REVOCABLE_TRUST, EntityType.IRREVOCABLE_TRUST,
            EntityType.LAND_TRUST,
        ],
        LoanType.DSCR: [
            EntityType.LLC, EntityType.MULTI_MEMBER_LLC,
            EntityType.LIMITED_PARTNERSHIP,
            EntityType.S_CORPORATION, EntityType.C_CORPORATION,
            EntityType.REVOCABLE_TRUST, EntityType.IRREVOCABLE_TRUST,
            EntityType.LAND_TRUST,
            # SERIES_LLC explicitly ineligible for DSCR
        ],
    }
    
    # Universally ineligible entities
    INELIGIBLE_ENTITIES = [
        EntityType.SOLE_PROPRIETORSHIP,
        EntityType.GENERAL_PARTNERSHIP,
        EntityType.NON_PROFIT,
    ]
    
    # Guarantor requirements
    MIN_GUARANTOR_OWNERSHIP_PERCENTAGE = 0.20  # 20%
    MIN_AGGREGATE_GUARANTOR_PERCENTAGE = 0.51  # 51%
    
    # DSCR-specific ineligibility
    DSCR_INELIGIBLE_ENTITIES = [EntityType.SERIES_LLC]
    
    def validate_entity_type(
        self, 
        entity_type: EntityType, 
        loan_type: LoanType
    ) -> Tuple[bool, List[str]]:
        """
        Validate if entity type is eligible for loan product.
        
        Args:
            entity_type: Type of borrowing entity
            loan_type: Type of loan requested
        
        Returns:
            Tuple of (is_eligible, error_messages)
        """
        errors = []
        
        # Check if universally ineligible
        if entity_type in self.INELIGIBLE_ENTITIES:
            errors.append(
                f"Entity type '{entity_type.value}' is not eligible for "
                f"any USDV Capital loans."
            )
            return False, errors
        
        # Check DSCR-specific ineligibility
        if loan_type == LoanType.DSCR and entity_type in self.DSCR_INELIGIBLE_ENTITIES:
            errors.append(
                f"Entity type '{entity_type.value}' is not eligible for "
                f"DSCR Permanent loans. (RTL products may allow case-by-case)"
            )
            return False, errors
        
        # Check if eligible for requested product
        eligible_types = self.ELIGIBLE_ENTITIES_BY_PRODUCT.get(loan_type, [])
        if entity_type not in eligible_types:
            eligible_names = ", ".join([et.value for et in eligible_types])
            errors.append(
                f"Entity type '{entity_type.value}' is not eligible for "
                f"{loan_type.value}. Eligible types: {eligible_names}"
            )
            return False, errors
        
        return True, errors
    
    def analyze_ownership_structure(
        self,
        owners: List[Owner],
        loan_type: LoanType
    ) -> OwnershipAnalysis:
        """
        Analyze ownership structure to determine guarantor requirements.
        
        Args:
            owners: List of all owners in entity
            loan_type: Type of loan being requested
        
        Returns:
            OwnershipAnalysis with findings and guarantor requirements
        """
        issues = []
        warnings = []
        guarantors_required = []
        has_nested_entities = False
        
        # Check for nested entities
        for owner in owners:
            if not owner.is_individual:
                has_nested_entities = True
        
        # Calculate total individual ownership
        total_individual_ownership = sum(
            [o.ownership_percentage for o in owners if o.is_individual]
        )
        
        # Identify key principals and 20%+ owners
        for owner in owners:
            if owner.is_individual:
                # Add if 20%+ OR key principal
                if owner.ownership_percentage >= self.MIN_GUARANTOR_OWNERSHIP_PERCENTAGE or owner.is_key_principal:
                    if owner not in guarantors_required:
                        guarantors_required.append(owner)
        
        # Calculate guarantor aggregate
        guarantor_aggregate = sum(
            [o.ownership_percentage for o in guarantors_required if o.is_individual]
        )
        
        # Validation checks
        if len(guarantors_required) == 0 and total_individual_ownership > 0:
            issues.append(
                "No identified guarantors. At least 51% of ownership "
                "must be identified for guaranty requirement."
            )
        
        if guarantor_aggregate < self.MIN_AGGREGATE_GUARANTOR_PERCENTAGE:
            issues.append(
                f"Identified guarantors represent only {guarantor_aggregate:.1%} "
                f"of ownership. Minimum {self.MIN_AGGREGATE_GUARANTOR_PERCENTAGE:.0%} aggregate required."
            )
        
        if total_individual_ownership < 1.0 and not has_nested_entities:
            issues.append(
                f"Total identified individual ownership is {total_individual_ownership:.1%}. "
                f"100% must be accounted for."
            )
        
        is_eligible = len(issues) == 0
        
        return OwnershipAnalysis(
            all_owners=owners,
            guarantors_required=list(set(guarantors_required)),
            guarantor_aggregate_percentage=guarantor_aggregate,
            has_nested_entities=has_nested_entities,
            is_eligible=is_eligible,
            issues=issues,
            warnings=warnings
        )
    
    def identify_key_principals(self, owners: List[Owner]) -> List[Owner]:
        """
        Identify all key principals from ownership list.
        
        Key principals include:
        - Any owner with 20%+ ownership
        - Any explicitly marked is_key_principal=True
        
        Args:
            owners: List of owners
        
        Returns:
            List of identified key principals
        """
        principals = []
        for owner in owners:
            if owner.is_individual and (
                owner.ownership_percentage >= self.MIN_GUARANTOR_OWNERSHIP_PERCENTAGE
                or owner.is_key_principal
            ):
                if owner not in principals:
                    principals.append(owner)
        
        return principals


# Example Usage
if __name__ == "__main__":
    analyzer = EntityAnalyzer()
    
    # Scenario 1: Multi-member LLC with clear guarantor requirement
    owners_1 = [
        Owner(name="Alice", ownership_percentage=0.50, is_individual=True),
        Owner(name="Bob", ownership_percentage=0.50, is_individual=True, is_key_principal=True),
    ]
    
    is_valid, errors = analyzer.validate_entity_type(
        EntityType.MULTI_MEMBER_LLC, LoanType.FIX_FLIP
    )
    print(f"Scenario 1 - Entity Type Valid: {is_valid}")
    
    analysis_1 = analyzer.analyze_ownership_structure(owners_1, LoanType.FIX_FLIP)
    print(f"Guarantors Required: {[o.name for o in analysis_1.guarantors_required]}")
    print(f"Aggregate Ownership: {analysis_1.guarantor_aggregate_percentage:.0%}")
    print(f"Eligible: {analysis_1.is_eligible}\n")
    
    # Scenario 2: Series LLC for DSCR (ineligible)
    is_valid_dscr, errors_dscr = analyzer.validate_entity_type(
        EntityType.SERIES_LLC, LoanType.DSCR
    )
    print(f"Scenario 2 - Series LLC for DSCR: {is_valid_dscr}")
    print(f"Errors: {errors_dscr}\n")
    
    # Scenario 3: Limited Partnership with GP guarantee
    owners_3 = [
        Owner(name="GP LLC", ownership_percentage=0.10, is_individual=False, 
              entity_type=EntityType.LLC),
        Owner(name="Charlie", ownership_percentage=0.04, is_individual=True),  # 40% of GP
        Owner(name="Limited Partner A", ownership_percentage=0.50, is_individual=True),  # LP only
        Owner(name="Limited Partner B", ownership_percentage=0.40, is_individual=True),  # LP only
    ]
    
    analysis_3 = analyzer.analyze_ownership_structure(owners_3, LoanType.BRIDGE)
    print(f"Scenario 3 - Limited Partnership")
    print(f"Guarantors: {[o.name for o in analysis_3.guarantors_required]}")
    print(f"Has Nested: {analysis_3.has_nested_entities}")
    print(f"Issues: {analysis_3.issues if analysis_3.issues else 'None'}")
```

---

*End of Section 3*
