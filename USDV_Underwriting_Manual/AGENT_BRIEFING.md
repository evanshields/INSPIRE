# Agent Briefing: USDV Underwriting Manual
## Read This First Before Writing Any Section

**Purpose:** This document provides full context for any agent writing sections of the USDV Underwriting Manual. Read this entire file before starting work.

---

## Project Overview

**What We're Building:**
A comprehensive underwriting manual for USDV Capital's single-family business purpose lending operations. The manual covers:
- **RTL Loans**: Fix & Flip, Ground-Up Construction (GUC), Bridge
- **DSCR Loans**: Permanent rental property financing

**How It Will Be Used:**
- Integrated with the INSPIRE loan origination system (not standalone)
- Each section referenced by specific INSPIRE app pages/features
- Python calculation library will be imported directly into INSPIRE backend
- AI analysis (INSPIRE Phase 7) will use this manual for document review and flag generation

---

## Critical Rules (MUST FOLLOW)

### 1. NEVER Mention Investor Names
**DO NOT** write "ArchWest", "EastView", or "Churchill" anywhere in your output.

**Instead use:**
- "USDV Guidelines"
- "Program Guidelines"
- "Guideline requirements"
- "Standard requirements"

**Why:** The manual must be investor-agnostic. We synthesize multiple investor guidelines into unified USDV standards.

### 2. Precedence Rules (For Your Reference Only)
When extracting and synthesizing guidelines:
- **DSCR products**: EastView guidelines take precedence
- **RTL products**: ArchWest guidelines take precedence

But DO NOT mention this in your output - just use these rules when guidelines conflict.

### 3. No Owner-Occupied Content
All loans are business purpose only. Owner-occupied is never eligible.

### 4. Include Python Code
Every section with calculations or logic MUST include production-ready Python code with:
- Type hints
- Docstrings
- Clear class/function structure

---

## Manual Structure

```
PART I: FOUNDATIONS (Sections 1-4)
├── Section 1: Investment Philosophy & Loan Products (Haiku)
├── Section 2: Borrower Eligibility & Classification (Sonnet)
├── Section 3: Entity & Guarantor Analysis (Haiku)
└── Section 4: Credit & Background Evaluation (Sonnet)

PART II: PROPERTY & VALUATION (Sections 5-8)
├── Section 5: Property Eligibility Standards (Haiku)
├── Section 6: RTL Property Analysis (Sonnet)
├── Section 7: DSCR Property & Income Analysis (Opus)
└── Section 8: Appraisal & Valuation Review (Sonnet)

PART III: LOAN STRUCTURING (Sections 9-12)
├── Section 9: RTL Loan Sizing & Leverage (Opus)
├── Section 10: DSCR Loan Sizing & Leverage (Opus)
├── Section 11: Pricing & Rate Calculations (Opus)
└── Section 12: Exception Management (Haiku)

PART IV: OPERATIONS & REFERENCE (Sections 13-16)
├── Section 13: Document Requirements & Diligence (Haiku)
├── Section 14: Third-Party Report Analysis (Opus)
├── Section 15: Credit Memo & Risk Assessment (Sonnet)
└── Section 16: Comprehensive Glossary (Haiku)
```

---

## Source Files Location

All investor guidelines are in:
```
C:\Users\evana\inspire\Investor Underwriting Guidelines\
```

**RTL Guidelines:**
- `Archwest RTL Guidelines.pdf` (PRIMARY for RTL)
- `Eastview_RTL_Guidelines_v4_1.pdf`
- `EV GUC Guidelines_v1.0.pdf`
- `RTL Program Guidelines (07.09.2025) - CLEAN 1.pdf`
- `Churchill RTL UPG - 06.2023_vf.pdf`

**DSCR Guidelines:**
- `Eastview DSCR Guidelines_v7.2.pdf` (PRIMARY for DSCR)
- `EV DSCR S Matrix_12.29.25.pdf`
- `EV DSCR S Sizer_12.29.25.xlsx`
- `1. Archwest DSCR Guidelines_7.9.25_V1.8.pdf`
- `Churchill DSCR Guidelines - 8.8.2023 5.pdf`
- `Churchill DSCR - Required Document List.docx`

**INSPIRE PRDs:**
```
C:\Users\evana\inspire\_PRDs\
```
- `inspire-master-prd.md`
- `inspire-phase-1-2-prd.md`
- `inspire-phase-3-4-prd.md`
- `inspire-phase-5-6-prd.md`
- `inspire-phase-7-prd.md`
- `inspire-phase-8-prd.md`

---

## Output Format Requirements

### File Header
Every section file MUST start with:
```markdown
---
section: [NUMBER]
title: [TITLE]
version: 1.0
last_updated: [DATE]
model_used: [haiku/sonnet/opus]
---

# Section [NUMBER]: [TITLE]
```

### Structure
- Use clear markdown headers (##, ###)
- Include tables for matrices and thresholds
- Include Python code in fenced code blocks
- Cross-reference other sections where relevant

### Save Location
Save your output to:
```
C:\Users\evana\inspire\USDV_Underwriting_Manual\sections\[XX]_[section_name].md
```

Example: `09_rtl_sizing_leverage.md`

---

## Your Task

1. **Read this briefing** (you're doing this now)
2. **Read the specific prompt** for your assigned section from:
   `C:\Users\evana\inspire\USDV_Underwriting_Manual\prompts\SECTION_PROMPTS_MASTER.md`
3. **Read the required source files** listed in your section's prompt
4. **Write the section** following all guidelines above
5. **Save the output** to the sections folder

---

## Key Reference Documents

If you need additional context:

| Document | Path | Purpose |
|----------|------|---------|
| Implementation Plan | `USDV_Underwriting_Manual/IMPLEMENTATION_PLAN_V2.md` | Full project plan |
| PRD Mapping | `USDV_Underwriting_Manual/PRD_MANUAL_MAPPING.md` | How manual integrates with INSPIRE |
| Section Prompts | `USDV_Underwriting_Manual/prompts/SECTION_PROMPTS_MASTER.md` | Detailed prompts for each section |
| Shieldstone Example | `Context/SHIELDSTONE_TECHNICAL_MANUAL_V2_FINAL.md` | Reference for style/depth (multifamily, different product) |

---

## Quick Reference: Key Thresholds

These appear across multiple sections - use consistently:

**FICO Minimums:**
- RTL: 660
- DSCR: 680

**Loan Amounts:**
- Minimum: $100,000
- Maximum: $3,000,000

**RTL Borrower Classification:**
| Score | Class |
|-------|-------|
| >= 7 | A+ |
| 5-6 | A |
| 2-4 | B |
| < 2 | C |

**DSCR Minimums:**
- FICO >= 700: 1.00x
- FICO < 700: 1.20x
- 5-9 Units: 1.20x (NCF)
- Foreign National: 1.20x

**Document Currency:**
- Credit/Background: 120 days
- Appraisal: 120 days
- Bank Statements: 90 days
- Good Standing: 90 days

---

## Contact/Questions

If you encounter conflicts or unclear requirements, note them in your output under a "## Open Questions" section at the end. These will be resolved during integration.

---

*Ready to begin? Find your section prompt in SECTION_PROMPTS_MASTER.md and start writing!*
