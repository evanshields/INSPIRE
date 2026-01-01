# Open Questions: USDV Underwriting Manual

## Status Overview

This document tracks questions requiring clarification from investor guidelines or USDV stakeholders. Questions are categorized by **Status** (Resolved, Partially Resolved, Open) and **Priority** (High, Medium, Low).

---

## RESOLVED QUESTIONS ✅

### Q1.1: GUC Minimum Experience Requirement
**Status**: ✅ **RESOLVED**  
**Answer**: 
- Standard: 3 completed deals in last 36 months  
- Alternative: 2 deals + Licensed General Contractor + 2x post-closing liquidity + 720 FICO minimum

**Sources**:
- ArchWest RTL Guidelines v6.0 (Ground-Up Construction section, page 9)
- EastView GUC Guidelines v1.0 (Borrower Classification section)

**Implementation**: Section 1.3.1 parameter table updated; Python code in Section 1 reflects both pathways

---

### Q1.2: DSCR R&T Cash-Back Threshold
**Status**: ✅ **RESOLVED**  
**Answer**: 
- **Definition**: Cash-out occurs when net proceeds to borrower **exceed 2% of loan amount OR $2,000 (whichever is less)**
- Below this threshold = Rate & Term Refinance
- Above this threshold = Cash-Out Refinance
- This is the threshold across all four investor guidelines

**Sources**:
- ArchWest DSCR Guidelines v1.8 (page 5)
- EastView DSCR Guidelines v7.2 (page 5)
- ArchWest RTL Guidelines v6.0 (Cash Out Refinance section, page 8)
- EastView RTL Guidelines v4.1 (Definitions section, page 7)

**Implementation**: Section 1.3.3 loan purposes table and Section 1.6 clarified

---

### Q1.3: Bridge Plus Investor Availability
**Status**: ✅ **RESOLVED**  
**Answer**:
- **Product**: Bridge Plus (25-36 month RTL product with DSCR qualification) is offered by **EastView RTL only**
- **ArchWest**: Does NOT offer Bridge Plus (maximum 24-month Bridge)
- **Availability**: EastView RTL Guidelines v4.1 defines Bridge Plus explicitly
- **USDV Position**: Adopt Bridge Plus as product #4 in RTL lineup (available through EastView)

**Sources**:
- EastView RTL Guidelines v4.1 (Loan Programs and Qualifications section, page 5)
- ArchWest RTL Guidelines v6.0 (No Bridge Plus mentioned; max terms 12-24 months)

**Implementation**: Section 1.2.4 new subsection created; Section 1.3 tables updated; Python code includes Bridge Plus

---

### Q3.2: Revocable Trust Guarantor Requirements
**Status**: ✅ **RESOLVED**  
**Answer**:
- **Requirement**: BOTH trustee AND grantor/owner of trust must execute personal guaranties
- If trustee is an entity (LLC, corporation): 20%+ owners of trustee also must guarantee
- Grantor guarantee required even if not serving as trustee

**Source**:
- ArchWest DSCR Guidelines v1.8 (Recourse section, page 5): "Revocable trust requires trustee and owner of the trust"

**Implementation**: Section 3.2.5 Revocable Trust subsection explicitly states dual guarantor requirement

---

### Q3.3b: Series LLC Eligibility (DSCR)
**Status**: ✅ **RESOLVED**  
**Answer**:
- **Series LLCs**: **EXPLICITLY INELIGIBLE for DSCR products**
- **RTL Products**: Series LLC eligibility is case-by-case (not explicitly prohibited but requires review)
- **Reason**: ArchWest DSCR explicitly states: "Series LLCs are ineligible borrowing entities" (page 3)

**Source**:
- ArchWest DSCR Guidelines v1.8 (Borrower section, page 3)
- EastView DSCR/RTL: No mention of Series LLC (implicitly not addressed)

**Implementation**: Section 3.2.1 Ineligible Entity Types marks Series LLC with DSCR ineligibility; Python code enforces restriction in DSCR validation

---

### Q5.3: Rural Property Definition Standard
**Status**: ✅ **RESOLVED**  
**Answer**:
- **Primary Standard**: **CFPB Rural and Underserved Designation website**
- Properties designated "Yes" = Rural = Ineligible
- **Exception**: Properties within 50-minute commute to secondary market with 250,000+ MSA population may be approved by SVP of Credit
- **Secondary Confirmation**: Appraisal rural designation (confirms but doesn't override CFPB)

**Sources**:
- ArchWest DSCR Guidelines v1.8 (Eligible Markets section, page 7)
- EastView RTL/GUC Guidelines: "Rural areas (as defined in the appraisal)" 

**Implementation**: Section 5.3.2 Rural Property Restrictions fully detailed with CFPB reference and exception process

---

### Q5.4: Declining Market HPA Measurement Level
**Status**: ✅ **RESOLVED**  
**Answer**:
- **Primary Level**: **ZIP code level** (most granular, most current)
- **Data Source**: Zillow ZHVI (Home Value Index) + Home Price Appreciation (HPA) calculation
- **Time Period**: Last 12 months typically; longer for trend confirmation
- **Leverage Impact**:
  - HPA 0% to -10% decline: -5% LTV reduction
  - HPA >-10% decline: -10% LTV reduction
  - ZHVI multiplier 200-300%: -5% LTV reduction
  - ZHVI multiplier >300%: -10% LTV reduction

**Sources**:
- EastView RTL Guidelines v4.1 (Area Conformity Assessment section, page 10)
- EastView DSCR Guidelines v7.2 (Leverage Matrices section, pages 4, 83-84)
- ArchWest DSCR Guidelines v1.8 (Eligible Markets section, page 7)

**Implementation**: Section 5.3.3 Declining Markets section fully detailed with metrics, sources, and reduction triggers

---

### Q5.5: Short-Term Rental (STR) Income Documentation
**Status**: ✅ **RESOLVED**  
**Answer**:
- **Minimum History**: **12-month trailing income history required**
- **Documentation Required**:
  - Annual income statement verifying collected rents (12-month period)
  - Proof of online listing (Airbnb, VRBO, etc.)
  - Property management agreement (if not self-managed)
- **Qualifying Rent Calculation**:
  - Lesser of: 125% of market rent OR actual 12-month average income
  - For unleased STR: 90% of market rent (RTL) or 100% (DSCR)

**Sources**:
- EastView DSCR Guidelines v7.2 (DSCR calculation section, pages 10-11)
- EastView RTL Guidelines v4.1 (Bridge Plus DSCR section, page 20)
- ArchWest DSCR Guidelines v1.8 (Airbnb/VRBO section, page 9)

**Implementation**: Reference in Section 7 (DSCR Property & Income Analysis); aligns with Bridge Plus and DSCR STR requirements

---

## PARTIALLY RESOLVED QUESTIONS ⚠️

### Q3.1: Affiliate Company Guaranties
**Status**: ⚠️ **PARTIALLY RESOLVED**  
**Finding**: 
- Guidelines require all 20%+ direct or indirect owners to guarantee
- Guidelines do NOT explicitly address whether indirect control (through affiliated entities) requires guaranty beyond 20%+ indirect ownership threshold
- ArchWest/EastView both use "20% or greater direct or indirect ownership" as threshold

**Answer for USDV**:
- Apply 20%+ direct/indirect ownership rule consistently
- Individuals controlling entity through affiliated business structures must guarantee if their aggregate indirect ownership ≥20%
- Requires organizational chart showing all layered relationships

**Remaining Question for USDV**:
- What is USDV's policy on guaranties from individuals who control borrowing entity via common management/control but <20% ownership? (Recommend: Case-by-case, exception-based)

**Implementation**: Section 3.3.2 Nested Entity Structures covers; recommend adding affiliate control policy in USDV procedures

---

### Q3.3: Limited Partnership Guarantor Requirements
**Status**: ⚠️ **PARTIALLY RESOLVED**  
**Finding**:
- Both investors require General Partner(s) to guarantee
- Both investors require 20%+ ownership individual/entity to guarantee
- ArchWest allows "warm body waiver" if entity has >250% net worth + >100% liquidity (requires SVP approval)
- EastView allows "51% on exception basis"

**Remaining Gaps**:
- Are ALL General Partners required to guarantee, or only those meeting 20%+ threshold?
- Can Limited Partners ever be required to guarantee?

**Answer for USDV**:
- All General Partner entities must be identified; 20%+ owners of GP entities must guarantee
- Limited Partners do not guarantee (they are passive investors)
- General Partner entity itself can guarantee if it meets net worth/liquidity thresholds
- Default: Require GP individual guaranties; allow exception with strong financials

**Implementation**: Section 3.2.2 Limited Partnership subsection updated

---

## OPEN QUESTIONS (USDV DECISION REQUIRED) ❓

### Q-Op1: Exception Approval Authority Matrix
**Status**: ❓ **REQUIRES USDV DECISION**  
**Recommendation from Implementation Plan V2**:
- Tier 1 (Processor/Sr. UW): Minor items (documentation, verifications)
- Tier 2 (UW Manager): Experience/FICO/LTV variances (<10%)
- Tier 3 (Investor): Major credit derogatory, property exceptions
- Tier 4 (Not Approvable): OFAC, fraud, active bankruptcy

**Questions for USDV**:
1. Does USDV adoption of this matrix align with investor approval requirements?
2. Are there product-specific differences (RTL vs DSCR)?
3. What is USDV's escalation process for exceptions that touch multiple categories?

**Impact**: Section 12 (Exception Management) framework depends on this decision

---

### Q-Op2: Series LLC RTL Eligibility
**Status**: ❓ **REQUIRES USDV DECISION**  
**Finding**:
- Series LLCs explicitly ineligible for DSCR (ArchWest DSCR Guidelines)
- RTL guidelines from ArchWest/EastView do not explicitly mention Series LLC
- ArchWest RTL lists as eligible: "Limited Liability Companies" (no series exclusion)
- EastView RTL lists as eligible: "LLC" (no series exclusion)

**Question for USDV**:
- Are Series LLCs eligible for RTL products (Fix & Flip, GUC, Bridge, Bridge Plus)?
- If eligible, are there special requirements due to series structure complexity?
- Or should USDV universally exclude Series LLC for consistency?

**Recommendation**: 
- If allowing for RTL: Require detailed organizational chart showing series separation
- If prohibiting universally: Simplify policy and coding

**Impact**: Section 3 and Python implementation in EntityAnalyzer

---

### Q-Op3: Condo Reserve Funding Minimum Threshold
**Status**: ❓ **REQUIRES USDV DECISION**  
**Finding**:
- EastView DSCR doesn't specify reserve % requirement
- ArchWest DSCR doesn't specify reserve % requirement
- Fannie Mae standard: 25% funding acceptable; 10-year reserve study as alternative
- Original Section 5 draft said "typically 10%" (no investor specification found)

**Question for USDV**:
1. What is USDV's minimum reserve funding standard?
   - 10% (minimal)?
   - 20% (moderate)?
   - 25% (Fannie Mae standard)?
   - Flexible with reserve study?
2. Does USDV require reserve study or just funding analysis?

**Impact**: Section 5.6.2 HOA Review Requirements and condo eligibility

---

### Q-Op4: GUC Alternative Experience Pathway Acceptance
**Status**: ❓ **REQUIRES USDV DECISION**  
**Finding**:
- ArchWest GUC allows: "2 deals in last 36 months if borrower is licensed General Contractor, has 2x liquidity and at least 720 FICO"
- This is an alternative to the standard 3-deal requirement

**Question for USDV**:
1. Should USDV accept this alternative pathway for GUC borrowers?
2. Are USDV's liquidity and FICO requirements aligned with ArchWest's definitions?

**Impact**: Section 2 (Borrower Eligibility) when written; GUC experience rules

---

### Q-Op5: Cash-Out Refinance Definition for Bridge Products
**Status**: ❓ **PARTIALLY REQUIRES CLARIFICATION**  
**Finding**:
- DSCR: 2% or $2,000 threshold established
- RTL Bridge: ArchWest allows Cash-Out on limited basis for Classes A+/A only
- EastView RTL: Cash-Out available for A+/A classes

**Question for USDV**:
1. Does USDV apply same 2% / $2,000 threshold to RTL Bridge cash-outs?
2. Or does RTL have different cash-out restrictions by borrower class?

**Impact**: Section 9 (RTL Sizing) when written

---

### Q-Op6: Non-Warrantable Condo Approval Authority
**Status**: ❓ **REQUIRES USDV DECISION**  
**Recommendation**:
- Minor non-warrantable issues (reserve funding improving, litigation resolving): Senior Underwriter approval
- Major issues (multiple problems, weak compensating factors): Underwriting Manager or Investor approval

**Question for USDV**:
1. What is USDV's approval authority for non-warrantable condos?
2. Can USDV approve internally, or must investor approve?
3. What is threshold for escalating to investor?

**Impact**: Section 5.6.3 project approval process and Section 12 exception management

---

## Summary Table: Open Questions Status

| Question ID | Category | Status | Priority | Resolution Needed |
|------------|----------|--------|----------|-------------------|
| Q1.1 | Product Definition | ✅ Resolved | High | None - implemented |
| Q1.2 | Product Definition | ✅ Resolved | High | None - implemented |
| Q1.3 | Product Definition | ✅ Resolved | Medium | None - implemented |
| Q3.1 | Entity/Guarantor | ⚠️ Partial | Medium | USDV affiliate control policy |
| Q3.2 | Entity/Guarantor | ✅ Resolved | Medium | None - implemented |
| Q3.3 | Entity/Guarantor | ⚠️ Partial | Medium | USDV LP guarantor policy |
| Q5.3 | Property Eligibility | ✅ Resolved | High | None - implemented |
| Q5.4 | Property Eligibility | ✅ Resolved | High | None - implemented |
| Q5.5 | Property Eligibility | ✅ Resolved | Medium | None - implemented |
| Q-Op1 | Operations | ❓ Open | High | USDV approval authority |
| Q-Op2 | Operations | ❓ Open | Medium | USDV Series LLC policy |
| Q-Op3 | Operations | ❓ Open | Medium | USDV condo reserve policy |
| Q-Op4 | Operations | ❓ Open | Low | USDV GUC pathway acceptance |
| Q-Op5 | Operations | ❓ Open | Low | USDV cash-out refinance policy |
| Q-Op6 | Operations | ❓ Open | High | USDV exception authority |

---

## Next Steps

### For USDV Stakeholders:
1. **Review and Approve Resolved Questions** (Sections 1.1-1.3, 3.2, 5.3-5.5)
   - These are now reflected in updated Sections 1, 3, and 5
   - Verify alignment with USDV operational needs
   
2. **Clarify Partially Resolved Questions** (Q3.1, Q3.3)
   - Provide guidance on affiliate guarantor policy
   - Provide guidance on LP guarantor requirements
   - These will inform Section 2 (Borrower Eligibility) when written

3. **Make USDV Policy Decisions** (Q-Op1 through Q-Op6)
   - Exception approval authority and thresholds
   - Series LLC eligibility for RTL
   - Condo reserve funding minimum
   - GUC alternative experience pathway
   - Cash-out refinance definitions
   - Non-warrantable condo approval process

4. **Update Sections 2, 9, and 10 (When Written)**
   - Sections 2 (Borrower Eligibility), 9 (RTL Sizing), and 10 (DSCR Sizing) depend on these USDV decisions
   - Once above decisions made, these sections can be finalized with confidence

---

*Last Updated: December 30, 2025*  
*Document Status: Preliminary - Awaiting USDV Decision on Q-Op1 through Q-Op6*
