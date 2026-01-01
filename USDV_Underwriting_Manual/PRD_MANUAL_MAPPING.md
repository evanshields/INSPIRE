# PRD to Manual Section Mapping
## INSPIRE App Integration Reference

**Purpose:** This document maps every INSPIRE PRD component that requires underwriting logic to the corresponding manual section(s). Use this reference when developing INSPIRE features to know which manual sections to consult.

---

## Quick Reference Matrix

| INSPIRE Phase | Manual Sections Referenced |
|---------------|---------------------------|
| Phase 1-2 (Intake/Application) | 1, 2, 3, 4, 5, 6, 7 |
| Phase 3-4 (Sizing/Quote) | 2, 7, 9, 10, 11 |
| Phase 5-6 (Reports/Diligence) | 8, 13, 14 |
| Phase 7 (AI Analysis/Credit Memo) | 4, 8, 12, 14, 15, 16 |
| Phase 8 (Pipeline/Closing) | 13 |

---

## Phase 1-2: Intake & Full Application

**PRD File:** `_PRDs/inspire-phase-1-2-prd.md`

### Quick App / Pre-Qualification

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Loan product eligibility check | **Section 1** | Determine if request fits RTL vs DSCR |
| Property type pre-check | **Section 5** | Validate property type is eligible |
| Property location check | **Section 5** | State/market eligibility |
| Borrower citizenship pre-check | **Section 2** | US Citizen, Perm Resident, FN, ITIN |
| Estimated experience validation | **Section 2** | Experience tier assessment |

### Full Application - Borrower Information

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Borrower data validation | **Section 2** | Required borrower fields |
| Credit authorization | **Section 4** | Credit pull requirements |
| Experience documentation | **Section 2** | Track record validation rules |
| Citizenship documentation | **Section 2** | Acceptable ID by citizenship type |
| Financial statement review | **Section 2** | PFS/liquidity requirements |

### Full Application - Entity Information

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Entity type validation | **Section 3** | Eligible entity types |
| Ownership structure | **Section 3** | Ownership percentage rules |
| Guarantor identification | **Section 3** | Key principal requirements |
| Entity documentation | **Section 3** | Required entity docs |
| Good standing requirements | **Section 3** | Currency requirements |

### Full Application - Property Information

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Property type validation | **Section 5** | Eligible property types |
| Property characteristics | **Section 5** | Size, units, acreage limits |
| RTL property specifics | **Section 6** | Rehab scope, ARV, exit strategy |
| DSCR property specifics | **Section 7** | Rent, lease status, income |
| Property condition assessment | **Section 5** | Condition rating criteria |

### Full Application - Loan Request

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Loan purpose validation | **Section 1** | Purchase, R&T Refi, Cash-Out |
| Loan amount limits | **Section 1, 9, 10** | Min/max by product |
| Term selection | **Section 1** | Available terms by product |
| Exit strategy validation | **Section 6** | RTL exit requirements |

---

## Phase 3-4: Deal Sizing & Quote Generation

**PRD File:** `_PRDs/inspire-phase-3-4-prd.md`

### Deal Sizing - RTL

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Borrower classification (A+/A/B/C) | **Section 2** | Classification calculation |
| Max As-Is LTV | **Section 9** | Leverage by classification |
| Max LTC | **Section 9** | Cost basis calculation |
| Max LTARV | **Section 9** | ARV-based constraint |
| Leverage reductions | **Section 9** | HPA, ZHVI, heavy rehab, etc. |
| Rehab holdback calculation | **Section 9** | Holdback sizing rules |
| Initial loan amount | **Section 9** | MIN of all constraints |

### Deal Sizing - DSCR

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| DSCR calculation | **Section 7** | Qualifying rent / PITIA |
| Qualifying rent determination | **Section 7** | By lease status |
| PITIA calculation | **Section 7** | All components |
| Base LTV by FICO/Purpose | **Section 10** | LTV matrix |
| LTV adjustments | **Section 10** | DSCR, property type, etc. |
| Minimum DSCR requirements | **Section 7** | By FICO tier |

### Quote Generation - RTL

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Interest rate determination | **Section 11** | RTL rate structure |
| Points calculation | **Section 11** | Origination points |
| YSP calculation | **Section 11** | Yield spread premium |
| Monthly payment calculation | **Section 9** | I/O payment |

### Quote Generation - DSCR

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Base rate by spread | **Section 11** | Treasury + spread |
| FICO LLPAs | **Section 11** | FICO × LTV matrix |
| Property type LLPAs | **Section 11** | Condo, 2-4 unit, etc. |
| DSCR LLPAs | **Section 11** | By DSCR tier |
| Loan size LLPAs | **Section 11** | UPB adjustments |
| Cash-out LLPAs | **Section 11** | Refi type adjustment |
| I/O LLPAs | **Section 11** | By LTV tier |
| Prepay LLPAs | **Section 11** | Step-down, level, min interest |
| Final rate calculation | **Section 11** | Base + all LLPAs |
| Origination/YSP | **Section 11** | USDV economics |

### Rate Lock

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Lock period options | **Section 11** | Lock durations |
| Extension fees | **Section 11** | Extension costs |
| Lock expiration handling | **Section 11** | Relock process |

---

## Phase 5-6: Third-Party Reports & Diligence

**PRD File:** `_PRDs/inspire-phase-5-6-prd.md`

### Third-Party Report Ordering

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Report type requirements | **Section 13, 14** | By loan type |
| Appraisal requirements | **Section 8** | Full vs BPO vs CDA |
| Credit report requirements | **Section 4** | Tri-merge standards |
| Background check scope | **Section 4** | Search types |
| Title requirements | **Section 14** | Commitment standards |
| Insurance requirements | **Section 14** | Coverage amounts |

### Diligence Checklist Generation

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Master document checklist | **Section 13** | By loan type |
| New vs existing client | **Section 13** | On-file docs |
| Currency requirements | **Section 13** | Document freshness |
| Expiration tracking | **Section 13** | Alert thresholds |

### Document Classification

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Document categories | **Section 13** | Classification taxonomy |
| AI classification rules | **Section 14** | Document type identification |
| Naming conventions | **Section 13** | Standard file naming |

---

## Phase 7: AI Analysis & Credit Memo

**PRD File:** `_PRDs/inspire-phase-7-prd.md`

### Credit Report Analysis

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| FICO score extraction | **Section 4, 14** | Score rules |
| Trade line analysis | **Section 4, 14** | Minimum requirements |
| Mortgage history analysis | **Section 4, 14** | Late payment rules |
| Derogatory analysis | **Section 4, 14** | BK, FC, SS, judgments |
| Flag generation rules | **Section 14** | Red/Yellow/Green criteria |

### Background Check Analysis

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Criminal history review | **Section 4, 14** | Disqualifying events |
| Civil litigation review | **Section 4, 14** | Active litigation rules |
| OFAC screening | **Section 4, 14** | Sanctions check |
| Lien/judgment analysis | **Section 4, 14** | Threshold amounts |

### Appraisal Analysis

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Value extraction | **Section 8, 14** | As-Is, ARV parsing |
| Report currency check | **Section 8, 14** | 120-day rule |
| Appraiser validation | **Section 8, 14** | License verification |
| Condition assessment | **Section 8, 14** | C-rating validation |
| Comp analysis | **Section 8, 14** | Comp quality rules |
| Value variance handling | **Section 8** | Resizing triggers |

### Title Analysis

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Schedule B-I review | **Section 14** | Requirements check |
| Schedule B-II review | **Section 14** | Exception analysis |
| Lien identification | **Section 14** | Payoff requirements |
| Easement/encroachment | **Section 14** | Acceptable exceptions |

### Insurance Analysis

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Coverage validation | **Section 14** | Minimum amounts |
| Mortgagee clause check | **Section 14** | Correct clause |
| Policy currency | **Section 14** | Effective dates |
| Flood determination | **Section 14** | Zone requirements |

### Flag System

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Green flag rules | **Section 14** | Pass criteria |
| Yellow flag rules | **Section 14** | Warning criteria |
| Red flag rules | **Section 14** | Failure criteria |
| Critical flag rules | **Section 14** | Immediate escalation |
| Flag aggregation | **Section 15** | Deal-level summary |

### Exception Management

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Exception type identification | **Section 12** | Category assignment |
| Auto-draft exception request | **Section 12** | Template generation |
| Compensating factors | **Section 12** | Mitigant identification |
| Approval authority | **Section 12** | Routing rules |

### Credit Memo Generation

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Executive summary | **Section 15** | Deal snapshot |
| Borrower analysis section | **Section 15** | Credit/experience narrative |
| Property analysis section | **Section 15** | Property/market narrative |
| Deal economics section | **Section 15** | Sources & uses, metrics |
| Third-party summary | **Section 15** | Report findings |
| Risk assessment | **Section 15** | Rating framework |
| Conditions & exceptions | **Section 15** | Outstanding items |

### Risk Rating

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Low risk criteria | **Section 15** | Green threshold |
| Moderate risk criteria | **Section 15** | Yellow threshold |
| Elevated risk criteria | **Section 15** | Orange threshold |
| High risk criteria | **Section 15** | Red threshold |
| Recommendation logic | **Section 15** | Approve/Decline rules |

---

## Phase 8: Pipeline & Closing

**PRD File:** `_PRDs/inspire-phase-8-prd.md`

### Closing Checklist

| PRD Component | Manual Section | Usage |
|---------------|----------------|-------|
| Required closing docs | **Section 13** | Closing doc list |
| Final verification checks | **Section 13** | Pre-close validation |
| Document expiration recheck | **Section 13** | Currency validation |

---

## Glossary Usage

**Section 16: Comprehensive Glossary** is referenced by ALL phases for:
- Term definitions in tooltips
- AI context for document analysis
- Consistent terminology across INSPIRE
- User education/help content

---

## Python Library Integration

Each INSPIRE module references specific Python classes:

| INSPIRE Module | Python Classes | Manual Section |
|----------------|----------------|----------------|
| Application Validation | `BorrowerClassifier`, `PropertyEligibilityChecker` | 2, 5 |
| RTL Sizing Engine | `RTLSizer` | 9 |
| DSCR Sizing Engine | `DSCRSizer`, `DSCRCalculator` | 7, 10 |
| Pricing Engine | `RTLPricingEngine`, `DSCRPricingEngine` | 11 |
| Document Analysis | `CreditAnalyzer`, `AppraisalAnalyzer`, `TitleAnalyzer` | 4, 8, 14 |
| Flag Generator | `FlagGenerator` | 14 |
| Credit Memo Generator | `CreditMemoGenerator`, `RiskRatingCalculator` | 15 |
| Exception Manager | `ExceptionManager` | 12 |
| Diligence Checker | `DiligenceChecker` | 13 |

---

## Implementation Notes

### When Building INSPIRE Features:

1. **Before coding any underwriting logic**, check this mapping to find the relevant manual section(s)

2. **Reference the manual section**, not investor guideline PDFs directly - the manual contains the synthesized, investor-agnostic rules

3. **Use the Python library** for all calculations - don't reimplement formulas

4. **Use Section 16 (Glossary)** for any term definitions needed in UI or AI prompts

5. **For flag generation**, reference Section 14's explicit flag rules - these are designed to match INSPIRE's Phase 7 requirements

---

*Document maintained as part of USDV Underwriting Manual project*
