# USDV Capital Underwriting Manual
## Implementation Plan v2.0

**Project:** USDV Capital Single-Family Business Purpose Loan Underwriting Manual
**For Use With:** INSPIRE Loan Origination System
**Created:** December 2025
**Status:** Implementation Plan - Approved with Modifications

---

## Key Design Principles

Based on feedback, the manual will follow these core principles:

1. **Investor-Agnostic Language**: The manual will NEVER reference specific investors (ArchWest, EastView, Churchill) by name. All guidelines will be synthesized into unified USDV standards.

2. **INSPIRE Integration**: Each section is designed to be referenced by specific INSPIRE app pages/tabs. The manual is NOT for standalone deal underwriting in a chat interface.

3. **Modular & Updatable**: Each section is a standalone markdown file that can be updated independently when investor guidelines change.

4. **Precedence Rules** (for internal synthesis only):
   - DSCR Products: EastView guidelines take precedence
   - RTL Products: ArchWest guidelines take precedence

5. **Parallel Writing**: Sections can be written simultaneously in parallel Claude Code sessions as they are largely independent.

---

## Directory Structure

```
C:\Users\evana\inspire\USDV_Underwriting_Manual\
├── IMPLEMENTATION_PLAN_V2.md           # This file
├── PRD_MANUAL_MAPPING.md               # Maps PRD sections to manual sections
├── USDV_UNDERWRITING_MANUAL_COMPLETE.md # Combined final manual
│
├── sections/                           # Individual section files
│   ├── 00_table_of_contents.md
│   ├── 01_investment_philosophy.md
│   ├── 02_borrower_eligibility.md
│   ├── 03_entity_guarantor_analysis.md
│   ├── 04_credit_background.md
│   ├── 05_property_eligibility.md
│   ├── 06_rtl_property_analysis.md
│   ├── 07_dscr_property_income.md
│   ├── 08_appraisal_valuation.md
│   ├── 09_rtl_sizing_leverage.md
│   ├── 10_dscr_sizing_leverage.md
│   ├── 11_pricing_calculations.md
│   ├── 12_exception_management.md
│   ├── 13_document_requirements.md
│   ├── 14_report_analysis.md
│   ├── 15_credit_memo.md
│   └── 16_glossary.md
│
├── prompts/                            # Detailed prompts for each section
│   ├── prompt_section_01.md
│   ├── prompt_section_02.md
│   ├── ... (one per section)
│   └── prompt_section_16.md
│
├── python/                             # Python calculation library
│   └── usdv_underwriting/
│       ├── __init__.py
│       ├── core/
│       ├── borrower/
│       ├── property/
│       ├── sizing/
│       ├── pricing/
│       ├── analysis/
│       ├── diligence/
│       ├── memo/
│       └── exceptions/
│
└── reference/                          # Quick reference materials
    ├── leverage_matrices.md
    ├── llpa_tables.md
    ├── document_checklists.md
    └── flag_rules.md
```

---

## Section Overview (Revised)

### Removed/Changed Items:
- **BRRRR Section**: Removed (not applicable to business purpose lending)
- **Owner-Occupied**: Already excluded by loan type definition
- **Investor Names**: Never mentioned in manual content

### 16 Sections:

| # | Section | Pages | Model | Parallel? |
|---|---------|-------|-------|-----------|
| 1 | Investment Philosophy & Loan Products | ~12 | Haiku | Yes |
| 2 | Borrower Eligibility & Classification | ~18 | Sonnet | Yes |
| 3 | Entity & Guarantor Analysis | ~15 | Haiku | Yes |
| 4 | Credit & Background Evaluation | ~22 | Sonnet | Yes |
| 5 | Property Eligibility Standards | ~18 | Haiku | Yes |
| 6 | RTL Property Analysis | ~20 | Sonnet | Yes |
| 7 | DSCR Property & Income Analysis | ~25 | Opus | Yes |
| 8 | Appraisal & Valuation Review | ~18 | Sonnet | Yes |
| 9 | RTL Loan Sizing & Leverage | ~28 | Opus | Yes |
| 10 | DSCR Loan Sizing & Leverage | ~26 | Opus | Yes |
| 11 | Pricing & Rate Calculations | ~32 | Opus | After 9,10 |
| 12 | Exception Management | ~15 | Haiku | Yes |
| 13 | Document Requirements & Diligence | ~20 | Haiku | Yes |
| 14 | Third-Party Report Analysis | ~28 | Opus | Yes |
| 15 | Credit Memo & Risk Assessment | ~22 | Sonnet | After 14 |
| 16 | Comprehensive Glossary | ~45 | Haiku | Last |

**Total: ~364 pages**

---

## Model Usage Optimization

### Haiku (6 sections) - Reference content, matrices, straightforward logic:
- Section 1: Investment Philosophy (product definitions, parameters)
- Section 3: Entity & Guarantor Analysis (clear eligibility rules)
- Section 5: Property Eligibility (eligibility matrices)
- Section 12: Exception Management (process documentation)
- Section 13: Document Requirements (checklists)
- Section 16: Glossary (term definitions)

### Sonnet (5 sections) - Moderate complexity, synthesis required:
- Section 2: Borrower Eligibility (classification logic)
- Section 4: Credit & Background (derogatory analysis)
- Section 6: RTL Property Analysis (technical criteria)
- Section 8: Appraisal Review (validation rules)
- Section 15: Credit Memo (narrative generation)

### Opus (5 sections) - Complex calculations, critical accuracy:
- Section 7: DSCR Property & Income (DSCR calculations)
- Section 9: RTL Sizing (leverage calculations)
- Section 10: DSCR Sizing (LTV matrices)
- Section 11: Pricing (LLPA engine)
- Section 14: Report Analysis (flag generation for INSPIRE)

---

## PRD-to-Manual Mapping

This mapping shows which manual sections support which INSPIRE PRD phases:

### Phase 1-2: Intake & Full Application
| PRD Component | Manual Section(s) |
|---------------|-------------------|
| Borrower data collection | 2, 3, 4 |
| Entity validation | 3 |
| Property pre-qualification | 5, 6, 7 |
| Experience verification | 2 |
| Loan product selection | 1 |

### Phase 3-4: Deal Sizing & Quote
| PRD Component | Manual Section(s) |
|---------------|-------------------|
| Borrower classification | 2 |
| RTL leverage calculation | 9 |
| DSCR leverage calculation | 10 |
| DSCR calculation | 7 |
| Rate/pricing calculation | 11 |
| Quote generation | 11 |

### Phase 5-6: Third-Party Reports & Diligence
| PRD Component | Manual Section(s) |
|---------------|-------------------|
| Document checklist generation | 13 |
| Report ordering criteria | 8, 14 |
| Document classification rules | 13, 14 |
| Expiration tracking | 13 |

### Phase 7: AI Analysis & Credit Memo
| PRD Component | Manual Section(s) |
|---------------|-------------------|
| Credit report analysis | 4, 14 |
| Background check analysis | 4, 14 |
| Appraisal analysis | 8, 14 |
| Title analysis | 14 |
| Insurance analysis | 14 |
| Flag generation (Green/Yellow/Red) | All sections with rules |
| Credit memo generation | 15 |
| Exception identification | 12 |
| Risk rating | 15 |

### Phase 8: Pipeline & Closing
| PRD Component | Manual Section(s) |
|---------------|-------------------|
| Closing checklist | 13 |
| Final verification | All |

---

## Exception Approval Matrix (Recommended)

Since you asked for my suggestion on the exception approval authority matrix:

### Tier 1: USDV Internal Approval
*Can be approved by USDV Senior Underwriter without investor submission*

| Exception Type | Criteria | Authority |
|----------------|----------|-----------|
| Documentation timing | Document 1-15 days past standard currency | Processor |
| Minor credit variance | FICO 5-10 points below threshold with strong compensating factors | Sr. Underwriter |
| Entity registration | Foreign entity registering in property state pre-close | Processor |

### Tier 2: USDV Management Approval
*Requires USDV management sign-off, may not require investor*

| Exception Type | Criteria | Authority |
|----------------|----------|-----------|
| Experience shortfall | 1-2 deals short with strong credit + liquidity | UW Manager |
| LTV variance | 1-2% over max with strong DSCR (>1.25x) | UW Manager |
| Property condition | C5 with detailed remediation plan | UW Manager |

### Tier 3: Investor Approval Required
*Must be submitted to investor for approval*

| Exception Type | Criteria | Authority |
|----------------|----------|-----------|
| Credit exception | FICO >20 points below threshold | Investor |
| LTV exception | >2% over guideline max | Investor |
| Derogatory credit | Recent BK/foreclosure within seasoning period | Investor |
| Property type | Non-standard property type | Investor |
| Experience exception | First-time investor or significant shortfall | Investor |
| DSCR exception | Below minimum DSCR threshold | Investor |

### Tier 4: Not Approvable
*USDV will not pursue regardless of compensating factors*

| Exception Type | Reason |
|----------------|--------|
| OFAC/sanctions match | Regulatory prohibition |
| Recent fraud conviction | Risk too high |
| FICO below 620 | Below all investor minimums |
| Active bankruptcy | Cannot close during BK |
| Condemned property | Uninhabitable |

---

## Parallel vs Sequential Writing

### Can Be Written in Parallel (Independent Sections):
These sections have no dependencies on each other and can be written simultaneously in different Claude Code tabs:

**Group A (Foundations):**
- Section 1: Investment Philosophy
- Section 2: Borrower Eligibility
- Section 3: Entity & Guarantor
- Section 4: Credit & Background

**Group B (Property):**
- Section 5: Property Eligibility
- Section 6: RTL Property Analysis
- Section 7: DSCR Property & Income
- Section 8: Appraisal Review

**Group C (Reference):**
- Section 12: Exception Management
- Section 13: Document Requirements

### Must Be Written Sequentially:
These sections depend on prior sections:

```
Section 9 (RTL Sizing) ──┐
                         ├──► Section 11 (Pricing) ──► Section 15 (Credit Memo)
Section 10 (DSCR Sizing) ┘

Section 14 (Report Analysis) ──► Section 15 (Credit Memo)

All Sections ──► Section 16 (Glossary)
```

### Recommended Approach:
1. **Wave 1** (Parallel): Sections 1, 2, 3, 4, 5, 6, 7, 8, 12, 13
2. **Wave 2** (Sequential): Sections 9, 10
3. **Wave 3** (Sequential): Section 11, 14
4. **Wave 4** (Sequential): Section 15
5. **Wave 5** (Final): Section 16 (Glossary)

---

## Update Mechanism Design

### Manual Update Process

When new investor guidelines are received:

1. **Identify Affected Sections**
   - Compare new guidelines to existing manual
   - List all sections requiring updates

2. **Update Individual Section Files**
   - Each section file is independent
   - Update only affected files
   - Maintain version history in file header

3. **Regenerate Combined Manual**
   - Run combination script
   - Updates `USDV_UNDERWRITING_MANUAL_COMPLETE.md`

4. **Update Python Library**
   - Modify affected calculation modules
   - Update constants and thresholds
   - Run test suite

### Section File Header Format:
```markdown
---
section: 9
title: RTL Loan Sizing & Leverage
version: 1.0
last_updated: 2025-12-30
guideline_sources:
  - RTL Program Guidelines (07.09.2025)
  - EV GUC Guidelines v1.0
changelog:
  - 2025-12-30: Initial creation
---
```

### Future INSPIRE Feature (for PRD consideration):
The idea of allowing users to upload investor guideline PDFs/Excel files and auto-update manual sections is excellent. This would be a Phase 9+ feature:

**Concept: "Guidelines Manager"**
- Upload new investor guideline document
- AI extracts changes/updates
- Highlights affected manual sections
- Generates draft updates for review
- User approves and publishes updates

*This should be added as a future roadmap item in the Master PRD.*

---

## Detailed Prompts Structure

Each section will have a dedicated prompt file in `/prompts/` with this structure:

```markdown
# Prompt: Section [X] - [Title]

## Objective
[Clear statement of what this section must accomplish]

## INSPIRE Integration Points
[Which PRD phases/pages reference this section]

## Required Source Files
[List of guideline files to reference with paths]

## Content Requirements
[Detailed list of what must be included]

## Python Code Requirements
[Classes and functions to include]

## Formatting Requirements
[Markdown structure, tables, code blocks]

## Key Rules
- NEVER mention investor names (ArchWest, EastView, Churchill)
- Use "USDV Guidelines" or "Program Guidelines" instead
- Focus on unified standards, not investor-specific variations

## Output Format
[Expected structure and length]
```

---

## Next Steps

1. **Create PRD Mapping Document** - Detailed mapping of PRD → Manual sections
2. **Create Section Prompts** - Detailed prompts for all 16 sections
3. **Begin Wave 1 Writing** - Parallel writing of 10 independent sections
4. **Wave 2-5** - Sequential sections as dependencies complete
5. **Combine & Review** - Generate complete manual
6. **Python Library** - Develop calculation modules
7. **Integration Testing** - Verify INSPIRE compatibility

---

## Approval Confirmation

Based on your feedback, this plan incorporates:

- [x] Dedicated folder structure (not in root directory)
- [x] Each section as standalone markdown file
- [x] Combined comprehensive document capability
- [x] Detailed prompts for each section
- [x] Reference to source files in prompts
- [x] BRRRR section removed
- [x] Investor-agnostic language (no investor names)
- [x] Haiku usage expanded (6 sections)
- [x] Parallel writing capability documented
- [x] PRD-to-Manual mapping
- [x] Exception approval matrix recommendation
- [x] Update mechanism design
- [x] Credit memo follows Phase 7 PRD exactly
- [x] Python library integrated with INSPIRE

**Ready to proceed with creating the detailed prompts and PRD mapping document?**
