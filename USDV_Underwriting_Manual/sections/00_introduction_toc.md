---
section: 0
title: Introduction & Table of Contents
version: 1.0
last_updated: 2025-12-30
---

# USDV Capital Underwriting Manual

## Introduction

This manual provides comprehensive underwriting guidelines for USDV Capital's single-family business purpose lending operations. It covers two primary product families:

- **RTL (Rehab/Transitional Loans)**: Fix & Flip, Ground-Up Construction (GUC), and Bridge financing
- **DSCR (Debt Service Coverage Ratio)**: Permanent rental property financing

### Purpose & Scope

This manual serves as the authoritative reference for:

1. **Loan Officers & Originators**: Structuring deals that meet program requirements
2. **Underwriters**: Evaluating borrower, property, and deal risk
3. **INSPIRE Integration**: Providing calculation logic and decision rules for the loan origination system
4. **AI Analysis (Phase 7)**: Supplying criteria for automated document review and flag generation

### How to Use This Manual

| If You Need To... | Reference Section(s) |
|-------------------|---------------------|
| Determine product eligibility | Section 1 |
| Qualify a borrower | Sections 2, 3, 4 |
| Evaluate a property | Sections 5, 6 (RTL), 7 (DSCR), 8 |
| Size and structure a loan | Section 9 (RTL), Section 10 (DSCR) |
| Price a loan | Section 11 |
| Request an exception | Section 12 |
| Check document requirements | Section 13 |
| Review third-party reports | Section 14 |
| Write a credit memo | Section 15 |
| Look up a term | Section 16 |
| Configure AI/LLM rules | Section 17 |

### Key Thresholds Quick Reference

| Parameter | RTL | DSCR |
|-----------|-----|------|
| Minimum FICO | 660 | 680 |
| Minimum Loan Amount | $100,000 | $100,000 |
| Maximum Loan Amount | $3,000,000 | $3,000,000 |
| Maximum LTV | 90% (As-Is) | 80% (Purchase) |
| Document Currency | 120 days | 120 days |

---

## Table of Contents

### Part I: Foundations (Sections 1-4)

| Section | Title | Description |
|---------|-------|-------------|
| [1](01_investment_philosophy.md) | **Investment Philosophy & Loan Products** | Mission, product definitions, eligible loan purposes, term structures |
| [2](02_borrower_eligibility.md) | **Borrower Eligibility & Classification** | Borrower types, citizenship requirements, experience scoring, RTL classification (A+/A/B/C) |
| [3](03_entity_guarantor_analysis.md) | **Entity & Guarantor Analysis** | Entity types, ownership structure, guarantor requirements, vesting |
| [4](04_credit_background.md) | **Credit & Background Evaluation** | FICO requirements, derogatory events, background checks, mortgage history |

### Part II: Property & Valuation (Sections 5-8)

| Section | Title | Description |
|---------|-------|-------------|
| [5](05_property_eligibility.md) | **Property Eligibility Standards** | Property types, location restrictions, condition ratings, ineligible properties |
| [6](06_rtl_property_analysis.md) | **RTL Property Analysis** | Rehab scope, ARV methodology, exit strategy, construction analysis |
| [7](07_dscr_property_income.md) | **DSCR Property & Income Analysis** | Qualifying rent, lease analysis, DSCR calculation, 5-9 unit NCF |
| [8](08_appraisal_valuation.md) | **Appraisal & Valuation Review** | Appraisal types, value reconciliation, comp analysis, condition ratings |

### Part III: Loan Structuring (Sections 9-12)

| Section | Title | Description |
|---------|-------|-------------|
| [9](09_rtl_sizing_leverage.md) | **RTL Loan Sizing & Leverage** | LTV/LTC/LTARV matrices, borrower classification impact, leverage reductions, rehab holdback |
| [10](10_dscr_sizing_leverage.md) | **DSCR Loan Sizing & Leverage** | LTV matrices by FICO/purpose, DSCR constraints, LTV adjustments |
| [11](11_pricing_calculations.md) | **Pricing & Rate Calculations** | RTL pricing, DSCR LLPAs, rate locks, origination fees, YSP |
| [12](12_exception_management.md) | **Exception Management** | Exception types, approval authority, compensating factors, documentation |

### Part IV: Operations & Reference (Sections 13-16)

| Section | Title | Description |
|---------|-------|-------------|
| [13](13_document_requirements.md) | **Document Requirements & Diligence** | Master checklists by loan type, document currency, naming conventions |
| [14](14_third_party_reports.md) | **Third-Party Report Analysis** | Credit, appraisal, title, insurance review; flag generation rules |
| [15](15_credit_memo_risk_assessment.md) | **Credit Memo & Risk Assessment** | Memo structure, risk rating framework, recommendation logic |
| [16](16_glossary.md) | **Comprehensive Glossary** | Definitions of all terms used throughout the manual |

### Part V: AI/LLM Integration (Section 17)

| Section | Title | Description |
|---------|-------|-------------|
| [17](17_llm_integration_guide.md) | **LLM Integration Guide** | Structured rules for INSPIRE AI systems; decision logic, flag criteria, validation schemas |

---

## Document Conventions

### Formatting

- **Bold**: Key terms, important thresholds, required items
- `Code blocks`: Python implementation, calculations, formulas
- Tables: Matrices, thresholds, eligibility criteria
- > Blockquotes: Important notes and warnings

### Cross-References

Sections reference each other using the format "See Section X.Y" where X is the section number and Y is the subsection.

### Python Code

Each section containing calculations includes production-ready Python code with:
- Type hints
- Docstrings
- Clear class/function structure
- Integration with INSPIRE system architecture

The consolidated Python library is located at:
```
USDV_Underwriting_Manual/python/usdv_underwriting/
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.1 | 2025-12-30 | Added Section 17 (LLM Integration Guide) for INSPIRE AI systems |
| 1.0 | 2025-12-30 | Initial release - all 16 sections complete |

---

## Support

For questions about this manual or INSPIRE integration:
- **Technical**: Reference the PRD_MANUAL_MAPPING.md for INSPIRE phase mappings
- **Guideline Clarification**: See OPEN_QUESTIONS.md for known ambiguities under review

---

*USDV Capital - Single Family Business Purpose Lending*
