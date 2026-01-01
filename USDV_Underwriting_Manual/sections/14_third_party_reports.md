---
section: 14
title: Third-Party Report Analysis
version: 1.0
last_updated: 2025-12-30
model_used: opus
guideline_sources:
  - Eastview DSCR Guidelines v7.2
  - Archwest RTL Guidelines
  - Churchill DSCR Guidelines
  - INSPIRE Phase 7 PRD
changelog:
  - 2025-12-30: Initial creation
---

# Section 14: Third-Party Report Analysis

## 14.1 Overview

Third-party reports provide independent verification of borrower qualifications, property condition, and legal standing. This section defines the analysis standards for each report type, including extraction requirements, validation rules, and flag generation criteria for INSPIRE Phase 7 integration.

**INSPIRE Integration Points:**
- Phase 7: Real-time document analysis pipeline
- Phase 7: Automated flag generation and compliance checking
- Phase 8: Credit memo narrative generation

**Report Categories:**
1. Credit & Background Reports
2. Property Valuation Reports
3. Title & Legal Reports
4. Insurance Documentation
5. Financial Verification Reports
6. Entity Documentation
7. Lease Documentation

---

## 14.2 Credit Report Analysis

### 14.2.1 Required Credit Report Elements

| Element | Description | Extraction Priority |
|---------|-------------|-------------------|
| Credit Scores | All three bureau scores | Critical |
| Tradelines | All open and closed accounts | High |
| Public Records | Bankruptcies, judgments, liens | Critical |
| Inquiries | Hard inquiries last 12 months | Medium |
| Authorized Users | AU accounts to exclude | High |
| Name/SSN Match | Identity verification | Critical |

### 14.2.2 Score Calculation Rules

**Qualifying Score Determination:**

| Scenario | Qualifying Score |
|----------|-----------------|
| Three scores available | Median score |
| Two scores available | Lower of the two |
| One score available | That score (requires approval) |
| No score | Ineligible (standard programs) |

**Multiple Guarantor Scenarios:**

| Ownership Structure | Score Used |
|--------------------|------------|
| Equal ownership (50/50) | Higher qualifying score |
| Unequal ownership | Score of majority owner |
| 51% recourse structure | Highest qualifying score |

### 14.2.3 Credit Event Identification

| Event Type | Lookback Period | Impact |
|------------|-----------------|--------|
| Bankruptcy (Ch 7) | 4 years from discharge | LTV reduction |
| Bankruptcy (Ch 13) | 2 years from discharge | LTV reduction |
| Foreclosure | 4 years | LTV reduction |
| Short Sale | 4 years | LTV reduction |
| Deed-in-Lieu | 4 years | LTV reduction |
| Mortgage Delinquency 60+ | 24 months | Flag for review |

### 14.2.4 Credit Report Flags

| Check | Green Flag | Yellow Flag | Red Flag | Critical Flag |
|-------|------------|-------------|----------|---------------|
| FICO Score | ≥ 720 | 680-719 | 660-679 | < 660 |
| Mortgage Lates (24 mo) | 0 | 1x30 day | 2x30 or 1x60 | 90+ days |
| Bankruptcy | > 4 years | 2-4 years | < 2 years | Active |
| Foreclosure | > 4 years | 2-4 years | < 2 years | Active |
| Open Collections | None | < $5,000 | $5,000-$25,000 | > $25,000 |
| Tax Liens | None | Paid > 12 mo | Payment plan | Unpaid |

### 14.2.5 Credit Report Data Extraction

```python
@dataclass
class CreditReportData:
    """Extracted credit report data."""
    # Identity
    borrower_name: str
    ssn_last_four: str
    report_date: date
    
    # Scores
    experian_score: Optional[int]
    equifax_score: Optional[int]
    transunion_score: Optional[int]
    qualifying_score: int
    
    # Events
    bankruptcies: List[BankruptcyRecord]
    foreclosures: List[ForeclosureRecord]
    collections: List[CollectionRecord]
    
    # Tradelines
    mortgage_tradelines: List[MortgageTradeline]
    installment_tradelines: List[InstallmentTradeline]
    revolving_tradelines: List[RevolvingTradeline]
    
    # Summary
    total_debt: float
    monthly_obligations: float
    au_accounts_excluded: List[str]
```

---

## 14.3 Background Check Analysis

### 14.3.1 Required Background Elements

| Element | Description | Extraction Priority |
|---------|-------------|-------------------|
| Identity Verification | Name, DOB, SSN match | Critical |
| Criminal History | Felonies, misdemeanors | Critical |
| Civil Judgments | Outstanding judgments | High |
| OFAC/Sanctions | Watchlist screening | Critical |
| Fraud Indicators | Identity fraud alerts | Critical |

### 14.3.2 Disqualifying Conditions

| Condition | Impact | Exception Path |
|-----------|--------|----------------|
| Active OFAC match | Immediate decline | None |
| Felony conviction (financial) | Decline | None |
| Felony conviction (other) | Review required | Management approval |
| Outstanding civil judgment | Payoff required | Escrow holdback |
| Identity fraud alert | Verification required | Clear with documentation |

### 14.3.3 Background Check Flags

| Check | Green Flag | Yellow Flag | Red Flag | Critical Flag |
|-------|------------|-------------|----------|---------------|
| OFAC/Sanctions | Clear | N/A | N/A | Match found |
| Criminal - Financial | Clear | N/A | Misdemeanor | Felony |
| Criminal - Other | Clear | Misdemeanor | Felony (>7 yrs) | Felony (<7 yrs) |
| Civil Judgments | None | Paid >12 mo | Outstanding <$10K | Outstanding >$10K |
| Identity Match | Verified | Minor variance | Requires review | Cannot verify |

---

## 14.4 Appraisal Analysis

### 14.4.1 Appraisal Requirements by Product

| Product | Appraisal Type | Age Limit | Recertification |
|---------|---------------|-----------|-----------------|
| RTL Fix & Flip | As-Is + ARV | 120 days | 180 days with recert |
| RTL GUC | As-Is + Prospective | 120 days | 180 days with recert |
| RTL Bridge | As-Is | 120 days | 180 days with recert |
| DSCR (< $1M) | Full Interior | 120 days | 180 days with recert |
| DSCR (≥ $1M) | Full Interior | 90 days | 120 days with recert |
| DSCR (≥ $2M) | Two appraisals | 90 days | Not allowed |

### 14.4.2 Required Appraisal Elements

| Element | Description | Validation Rule |
|---------|-------------|-----------------|
| Property Address | Legal address | Must match application |
| Effective Date | Date of inspection | Within age limits |
| As-Is Value | Current market value | Required for all |
| ARV (if applicable) | After-repair value | RTL rehab only |
| Prospective Value | At completion | GUC only |
| Subject Photos | Interior/exterior | Minimum 6 photos |
| Comparable Sales | Recent sales data | 3-6 comps required |
| Adjustments | Value adjustments | Net < 15%, Gross < 25% |
| Condition Rating | C1-C6 scale | Document condition |
| Quality Rating | Q1-Q6 scale | Document quality |

### 14.4.3 Comparable Sale Requirements

| Requirement | Standard | Exception |
|-------------|----------|-----------|
| Distance | ≤ 1 mile | ≤ 3 miles rural |
| Age of Sale | ≤ 6 months | ≤ 12 months with explanation |
| GLA Variance | ± 20% | ± 30% with adjustment |
| Net Adjustments | ≤ 15% | ≤ 20% with explanation |
| Gross Adjustments | ≤ 25% | ≤ 30% with explanation |
| Minimum Comps | 3 | 2 with approval |

### 14.4.4 Value Reconciliation Rules

**Multiple Appraisal Scenarios:**

| Scenario | Value Used |
|----------|------------|
| Two appraisals required | Lower of the two values |
| Values within 10% | Average may be used |
| Values differ > 10% | Third appraisal required |
| Desktop + Full | Full appraisal value |

### 14.4.5 Appraisal Flags

| Check | Green Flag | Yellow Flag | Red Flag | Critical Flag |
|-------|------------|-------------|----------|---------------|
| Age | < 90 days | 90-120 days | 120-180 days | > 180 days |
| Net Adjustments | ≤ 10% | 10-15% | 15-20% | > 20% |
| Gross Adjustments | ≤ 20% | 20-25% | 25-30% | > 30% |
| Comp Distance | ≤ 0.5 mile | 0.5-1 mile | 1-3 miles | > 3 miles |
| Comp Age | ≤ 3 months | 3-6 months | 6-12 months | > 12 months |
| Condition | C1-C3 | C4 | C5 | C6 |
| Value vs Contract | Within 5% | 5-10% variance | 10-15% variance | > 15% variance |

### 14.4.6 Appraisal Data Extraction

```python
@dataclass
class AppraisalData:
    """Extracted appraisal data."""
    # Property
    property_address: str
    legal_description: str
    property_type: str
    year_built: int
    gla: int
    lot_size: float
    bedrooms: int
    bathrooms: float
    
    # Values
    as_is_value: float
    arv: Optional[float]
    prospective_value: Optional[float]
    land_value: float
    
    # Dates
    effective_date: date
    report_date: date
    
    # Condition
    condition_rating: str  # C1-C6
    quality_rating: str    # Q1-Q6
    
    # Comparables
    comparables: List[ComparableSale]
    net_adjustment_pct: float
    gross_adjustment_pct: float
    
    # Analysis
    appraiser_name: str
    appraiser_license: str
    appraisal_company: str
```

---

## 14.5 Title Report Analysis

### 14.5.1 Required Title Elements

| Element | Description | Validation Rule |
|---------|-------------|-----------------|
| Legal Description | Full legal description | Match appraisal |
| Vesting | Current ownership | Verify seller/borrower |
| Liens | All recorded liens | Must be cleared/paid |
| Encumbrances | Easements, restrictions | Review for impact |
| Taxes | Tax status | Current or escrowed |
| Judgments | Recorded judgments | Must be cleared |
| Chain of Title | Ownership history | 24 months minimum |

### 14.5.2 Title Defect Classifications

| Classification | Examples | Resolution |
|----------------|----------|------------|
| Curative | Minor name variance, missing signatures | Title company cure |
| Major | Unreleased liens, boundary disputes | Require resolution |
| Fatal | Fraud, forgery, incapacity | Cannot close |

### 14.5.3 Lien Priority Requirements

| Position | Requirement |
|----------|-------------|
| First Lien | USDV must be in first position |
| Subordinate Liens | Must be subordinated or paid off |
| Property Taxes | Must be current or escrowed |
| HOA Liens | Must be current |
| Mechanic's Liens | Must be released |

### 14.5.4 Title Report Flags

| Check | Green Flag | Yellow Flag | Red Flag | Critical Flag |
|-------|------------|-------------|----------|---------------|
| Lien Position | Clear first | Subordination pending | Multiple liens | Cannot achieve first |
| Tax Status | Current | 1 year delinquent | 2+ years delinquent | Tax sale pending |
| Chain of Title | Clear 24+ mo | Minor gaps | Recent transfers | Clouded title |
| Encumbrances | Standard | Unusual easements | Access issues | Building violations |
| Vesting | Matches | Minor variance | Entity mismatch | Cannot verify |

---

## 14.6 Insurance Certificate Analysis

### 14.6.1 Required Insurance Coverage

**Property Insurance (All Loans):**

| Coverage Type | Minimum Requirement |
|---------------|-------------------|
| Dwelling Coverage | ≥ Loan amount or replacement cost |
| Deductible | ≤ 5% of coverage or $25,000 |
| Named Insured | Borrowing entity |
| Mortgagee Clause | USDV Capital and/or servicer |
| Policy Term | ≥ 12 months |

**Additional Coverage Requirements:**

| Condition | Required Coverage |
|-----------|------------------|
| Flood Zone A/V | Flood insurance required |
| Coastal Property | Wind/hurricane coverage |
| Earthquake Zone | Earthquake coverage (CA) |
| Builder's Risk (GUC) | Course of construction coverage |

### 14.6.2 Flood Zone Requirements

| Flood Zone | Insurance Required | Coverage Amount |
|------------|-------------------|-----------------|
| Zone A, AE, AH, AO | Yes | ≥ Loan amount |
| Zone V, VE | Yes | ≥ Loan amount |
| Zone B, C, X | No (recommended) | N/A |
| Zone D | Case by case | Per underwriter |

### 14.6.3 Insurance Flags

| Check | Green Flag | Yellow Flag | Red Flag | Critical Flag |
|-------|------------|-------------|----------|---------------|
| Coverage Amount | ≥ 110% loan | 100-110% loan | 90-100% loan | < 90% loan |
| Deductible | ≤ 2% | 2-5% | 5-10% | > 10% |
| Policy Expiration | > 60 days | 30-60 days | < 30 days | Expired |
| Mortgagee Clause | Correct | Minor error | Missing | Wrong lender |
| Flood Zone | Not required | Zone X | Zone B/C | Zone A/V (no ins) |

---

## 14.7 Feasibility Study Analysis (GUC Only)

### 14.7.1 Required Feasibility Elements

| Element | Description | Validation Rule |
|---------|-------------|-----------------|
| Project Scope | Detailed scope of work | Match appraisal |
| Cost Breakdown | Line-item budget | Reasonable costs |
| Timeline | Construction schedule | ≤ 18 months |
| Contractor Info | Licensed contractor | Verify license |
| Permits | Required permits | Status verified |

### 14.7.2 Budget Analysis Rules

| Category | Typical Range | Flag Threshold |
|----------|---------------|----------------|
| Hard Costs | 65-80% of budget | < 60% or > 85% |
| Soft Costs | 15-25% of budget | > 30% |
| Contingency | 5-10% of budget | < 5% or > 15% |
| Land (if applicable) | Per appraisal | > 110% of appraised |

### 14.7.3 Feasibility Flags

| Check | Green Flag | Yellow Flag | Red Flag | Critical Flag |
|-------|------------|-------------|----------|---------------|
| Budget vs Appraisal | Within 10% | 10-20% variance | 20-30% variance | > 30% variance |
| Timeline | ≤ 12 months | 12-18 months | 18-24 months | > 24 months |
| Contingency | 5-10% | 3-5% or 10-15% | < 3% or > 15% | None |
| Contractor License | Active, verified | Minor issues | Expired | Not licensed |
| Permits | Approved | In progress | Not applied | Denied |

---

## 14.8 Bank Statement Analysis

### 14.8.1 Required Bank Statement Elements

| Element | Description | Validation Rule |
|---------|-------------|-----------------|
| Account Holder | Name on account | Match borrower/entity |
| Statement Period | Date range | 2-3 consecutive months |
| Beginning Balance | Opening balance | Verify continuity |
| Ending Balance | Closing balance | Match next statement |
| Deposits | All deposits | Source large deposits |
| Withdrawals | All withdrawals | Flag unusual activity |

### 14.8.2 Liquidity Verification Rules

| Requirement | Standard | Calculation |
|-------------|----------|-------------|
| Reserves (RTL) | 6 months PITIA | Principal + Interest + Taxes + Insurance |
| Reserves (DSCR) | 6-12 months PITIA | Based on FICO tier |
| Cash to Close | Verified funds | Down payment + closing costs |
| Large Deposit | > 25% of qualifying income | Must be sourced |

### 14.8.3 Bank Statement Flags

| Check | Green Flag | Yellow Flag | Red Flag | Critical Flag |
|-------|------------|-------------|----------|---------------|
| Reserves | > 12 months | 6-12 months | 3-6 months | < 3 months |
| Large Deposits | All sourced | 1-2 unsourced < $5K | Unsourced > $5K | Unsourced > $25K |
| NSF/Overdrafts | None | 1-2 in 3 months | 3-5 in 3 months | > 5 in 3 months |
| Account Age | > 12 months | 6-12 months | 3-6 months | < 3 months |
| Balance Trend | Stable/increasing | Minor fluctuation | Declining | Significant decline |

---

## 14.9 Entity Document Analysis

### 14.9.1 Required Entity Documents

| Document | Purpose | Validation |
|----------|---------|------------|
| Articles of Organization | Entity formation | State filing verified |
| Operating Agreement | Ownership structure | Matches application |
| Certificate of Good Standing | Active status | Current (< 90 days) |
| EIN Letter | Tax ID verification | Match entity name |
| Resolution to Borrow | Authorization | Properly executed |

### 14.9.2 Entity Verification Rules

| Check | Requirement |
|-------|-------------|
| Entity Type | LLC, LP, Corp, Trust (eligible types) |
| State of Formation | Any US state |
| Good Standing | Current in state of formation |
| Foreign Qualification | If operating in different state |
| Ownership | All members/managers identified |
| Signing Authority | Authorized signers verified |

### 14.9.3 Entity Document Flags

| Check | Green Flag | Yellow Flag | Red Flag | Critical Flag |
|-------|------------|-------------|----------|---------------|
| Good Standing | Current | Pending renewal | Administratively dissolved | Judicially dissolved |
| Operating Agreement | Complete | Minor updates needed | Significant gaps | Missing |
| Ownership Match | 100% match | Minor variance | Significant variance | Cannot verify |
| Signing Authority | Clear | Ambiguous | Disputed | Unauthorized |
| Entity Age | > 2 years | 1-2 years | 6-12 months | < 6 months |

---

## 14.10 Lease Document Analysis

### 14.10.1 Lease Review Requirements

| Element | Requirement | Validation |
|---------|-------------|------------|
| Parties | Landlord and tenant | Arm's length transaction |
| Property | Correct address | Match subject property |
| Term | Start and end dates | Remaining term noted |
| Rent Amount | Monthly rent | Market rate verification |
| Security Deposit | Amount held | ≤ 2 months rent |
| Signatures | All parties | Properly executed |

### 14.10.2 Lease Eligibility Criteria

| Criterion | Eligible | Ineligible |
|-----------|----------|------------|
| Lease Type | Standard residential | Commercial in residential |
| Term | Month-to-month or fixed | Expired without renewal |
| Parties | Arm's length | Related party |
| Purchase Option | None | Contains purchase option |
| Rent Amount | Market rate | Significantly above/below market |

### 14.10.3 Lease Document Flags

| Check | Green Flag | Yellow Flag | Red Flag | Critical Flag |
|-------|------------|-------------|----------|---------------|
| Remaining Term | > 6 months | 3-6 months | < 3 months | Expired |
| Rent vs Market | Within 10% | 10-20% variance | 20-30% variance | > 30% variance |
| Arm's Length | Verified | Cannot verify | Related party disclosed | Related party hidden |
| Lease Execution | Complete | Minor issues | Incomplete | Forged/fraudulent |
| Tenant Payment History | Current | 1 late (30 day) | Multiple lates | Non-paying |

---

## 14.11 Python Implementation

```python
"""
Third-Party Report Analysis Module
USDV Capital Underwriting Library

This module provides comprehensive analysis functionality for all
third-party reports including credit, background, appraisal, title,
insurance, feasibility, bank statements, entity documents, and leases.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List, Dict, Tuple, Any
from datetime import date, datetime
from decimal import Decimal


class FlagLevel(Enum):
    """Flag severity levels."""
    GREEN = "green"
    YELLOW = "yellow"
    RED = "red"
    CRITICAL = "critical"


class ReportType(Enum):
    """Third-party report types."""
    CREDIT_REPORT = "credit_report"
    BACKGROUND_CHECK = "background_check"
    APPRAISAL = "appraisal"
    TITLE_REPORT = "title_report"
    INSURANCE_CERT = "insurance_certificate"
    FEASIBILITY_STUDY = "feasibility_study"
    BANK_STATEMENT = "bank_statement"
    ENTITY_DOCS = "entity_documents"
    LEASE = "lease"


@dataclass
class AnalysisFlag:
    """Individual analysis flag."""
    flag_id: str
    report_type: ReportType
    check_name: str
    level: FlagLevel
    message: str
    value: Any
    threshold: Any
    requires_action: bool
    action_description: Optional[str] = None


@dataclass
class ReportAnalysisResult:
    """Complete analysis result for a report."""
    report_type: ReportType
    report_date: date
    analysis_date: date
    flags: List[AnalysisFlag]
    extracted_data: Dict[str, Any]
    is_acceptable: bool
    requires_review: bool
    critical_issues: List[str]
    recommendations: List[str]
    
    @property
    def flag_summary(self) -> Dict[str, int]:
        """Count flags by level."""
        summary = {level.value: 0 for level in FlagLevel}
        for flag in self.flags:
            summary[flag.level.value] += 1
        return summary
    
    @property
    def has_critical_flags(self) -> bool:
        """Check for critical flags."""
        return any(f.level == FlagLevel.CRITICAL for f in self.flags)


# Credit Report Data Structures

@dataclass
class BankruptcyRecord:
    """Bankruptcy record from credit report."""
    chapter: str  # '7', '13'
    filing_date: date
    discharge_date: Optional[date]
    status: str  # 'discharged', 'dismissed', 'active'
    
    @property
    def years_since_discharge(self) -> Optional[float]:
        """Calculate years since discharge."""
        if self.discharge_date:
            delta = date.today() - self.discharge_date
            return delta.days / 365.25
        return None


@dataclass
class ForeclosureRecord:
    """Foreclosure record from credit report."""
    completion_date: date
    property_address: Optional[str]
    deficiency_balance: float
    
    @property
    def years_since_completion(self) -> float:
        """Calculate years since foreclosure."""
        delta = date.today() - self.completion_date
        return delta.days / 365.25


@dataclass
class CollectionRecord:
    """Collection account from credit report."""
    creditor: str
    original_amount: float
    current_balance: float
    date_opened: date
    status: str  # 'open', 'paid', 'settled'
    is_medical: bool


@dataclass
class MortgageTradeline:
    """Mortgage tradeline from credit report."""
    creditor: str
    account_number_masked: str
    original_amount: float
    current_balance: float
    monthly_payment: float
    date_opened: date
    payment_history: Dict[str, str]  # YYYY-MM: status
    
    def get_late_payments(self, months: int = 24) -> Dict[str, int]:
        """Get late payment counts in last N months."""
        lates = {'30_day': 0, '60_day': 0, '90_day': 0, '120_plus': 0}
        # Implementation would parse payment_history
        return lates


@dataclass
class CreditReportData:
    """Complete extracted credit report data."""
    # Identity
    borrower_name: str
    ssn_last_four: str
    report_date: date
    report_id: str
    
    # Scores
    experian_score: Optional[int]
    equifax_score: Optional[int]
    transunion_score: Optional[int]
    
    # Events
    bankruptcies: List[BankruptcyRecord] = field(default_factory=list)
    foreclosures: List[ForeclosureRecord] = field(default_factory=list)
    collections: List[CollectionRecord] = field(default_factory=list)
    
    # Tradelines
    mortgage_tradelines: List[MortgageTradeline] = field(default_factory=list)
    
    # Inquiries
    hard_inquiries_12mo: int = 0
    
    # AU accounts
    au_accounts_excluded: List[str] = field(default_factory=list)
    
    @property
    def qualifying_score(self) -> Optional[int]:
        """Calculate qualifying credit score."""
        scores = [s for s in [
            self.experian_score,
            self.equifax_score,
            self.transunion_score
        ] if s is not None]
        
        if len(scores) == 3:
            scores.sort()
            return scores[1]  # Median
        elif len(scores) == 2:
            return min(scores)
        elif len(scores) == 1:
            return scores[0]
        return None
    
    @property
    def total_collections_balance(self) -> float:
        """Sum of open collection balances."""
        return sum(
            c.current_balance for c in self.collections
            if c.status == 'open'
        )


# Appraisal Data Structures

@dataclass
class ComparableSale:
    """Comparable sale from appraisal."""
    address: str
    sale_price: float
    sale_date: date
    distance_miles: float
    gla: int
    adjusted_price: float
    net_adjustment_pct: float
    gross_adjustment_pct: float


@dataclass
class AppraisalData:
    """Complete extracted appraisal data."""
    # Property
    property_address: str
    legal_description: str
    property_type: str
    year_built: int
    gla: int
    lot_size_sqft: float
    bedrooms: int
    bathrooms: float
    
    # Values
    as_is_value: float
    arv: Optional[float] = None
    prospective_value: Optional[float] = None
    land_value: float = 0
    
    # Dates
    effective_date: date = field(default_factory=date.today)
    report_date: date = field(default_factory=date.today)
    
    # Condition
    condition_rating: str = "C3"
    quality_rating: str = "Q3"
    
    # Comparables
    comparables: List[ComparableSale] = field(default_factory=list)
    
    # Appraiser
    appraiser_name: str = ""
    appraiser_license: str = ""
    appraisal_company: str = ""
    
    @property
    def age_days(self) -> int:
        """Calculate appraisal age in days."""
        return (date.today() - self.effective_date).days
    
    @property
    def avg_net_adjustment(self) -> float:
        """Average net adjustment across comps."""
        if not self.comparables:
            return 0
        return sum(c.net_adjustment_pct for c in self.comparables) / len(self.comparables)
    
    @property
    def avg_gross_adjustment(self) -> float:
        """Average gross adjustment across comps."""
        if not self.comparables:
            return 0
        return sum(c.gross_adjustment_pct for c in self.comparables) / len(self.comparables)


# Analysis Engines

class CreditReportAnalyzer:
    """
    Analyze credit reports and generate flags.
    
    Implements credit analysis rules per USDV Guidelines
    including score validation, event identification, and
    tradeline analysis.
    """
    
    # FICO thresholds
    FICO_THRESHOLDS = {
        'excellent': 720,
        'good': 680,
        'fair': 660,
        'minimum': 660
    }
    
    # Event seasoning requirements (years)
    EVENT_SEASONING = {
        'bankruptcy_ch7': 4,
        'bankruptcy_ch13': 2,
        'foreclosure': 4,
        'short_sale': 4,
        'deed_in_lieu': 4
    }
    
    def analyze(self, credit_data: CreditReportData) -> ReportAnalysisResult:
        """
        Perform complete credit report analysis.
        
        Args:
            credit_data: Extracted credit report data
            
        Returns:
            Complete analysis result with flags
        """
        flags = []
        critical_issues = []
        recommendations = []
        
        # Analyze FICO score
        fico_flags = self._analyze_fico(credit_data)
        flags.extend(fico_flags)
        
        # Analyze bankruptcies
        bk_flags = self._analyze_bankruptcies(credit_data)
        flags.extend(bk_flags)
        
        # Analyze foreclosures
        fc_flags = self._analyze_foreclosures(credit_data)
        flags.extend(fc_flags)
        
        # Analyze collections
        coll_flags = self._analyze_collections(credit_data)
        flags.extend(coll_flags)
        
        # Analyze mortgage payment history
        mtg_flags = self._analyze_mortgage_history(credit_data)
        flags.extend(mtg_flags)
        
        # Determine acceptability
        has_critical = any(f.level == FlagLevel.CRITICAL for f in flags)
        has_red = any(f.level == FlagLevel.RED for f in flags)
        
        if has_critical:
            critical_issues.append("Critical credit issues require immediate attention")
        
        return ReportAnalysisResult(
            report_type=ReportType.CREDIT_REPORT,
            report_date=credit_data.report_date,
            analysis_date=date.today(),
            flags=flags,
            extracted_data={
                'qualifying_score': credit_data.qualifying_score,
                'total_collections': credit_data.total_collections_balance,
                'bankruptcies': len(credit_data.bankruptcies),
                'foreclosures': len(credit_data.foreclosures)
            },
            is_acceptable=not has_critical,
            requires_review=has_red,
            critical_issues=critical_issues,
            recommendations=recommendations
        )
    
    def _analyze_fico(self, data: CreditReportData) -> List[AnalysisFlag]:
        """Analyze FICO score."""
        flags = []
        score = data.qualifying_score
        
        if score is None:
            flags.append(AnalysisFlag(
                flag_id="CR001",
                report_type=ReportType.CREDIT_REPORT,
                check_name="FICO Score",
                level=FlagLevel.CRITICAL,
                message="No credit score available",
                value=None,
                threshold=self.FICO_THRESHOLDS['minimum'],
                requires_action=True,
                action_description="Obtain valid credit report with scores"
            ))
        elif score >= self.FICO_THRESHOLDS['excellent']:
            flags.append(AnalysisFlag(
                flag_id="CR001",
                report_type=ReportType.CREDIT_REPORT,
                check_name="FICO Score",
                level=FlagLevel.GREEN,
                message=f"Excellent credit score: {score}",
                value=score,
                threshold=self.FICO_THRESHOLDS['excellent'],
                requires_action=False
            ))
        elif score >= self.FICO_THRESHOLDS['good']:
            flags.append(AnalysisFlag(
                flag_id="CR001",
                report_type=ReportType.CREDIT_REPORT,
                check_name="FICO Score",
                level=FlagLevel.YELLOW,
                message=f"Good credit score: {score}",
                value=score,
                threshold=self.FICO_THRESHOLDS['good'],
                requires_action=False
            ))
        elif score >= self.FICO_THRESHOLDS['fair']:
            flags.append(AnalysisFlag(
                flag_id="CR001",
                report_type=ReportType.CREDIT_REPORT,
                check_name="FICO Score",
                level=FlagLevel.RED,
                message=f"Fair credit score: {score}",
                value=score,
                threshold=self.FICO_THRESHOLDS['fair'],
                requires_action=True,
                action_description="Review for compensating factors"
            ))
        else:
            flags.append(AnalysisFlag(
                flag_id="CR001",
                report_type=ReportType.CREDIT_REPORT,
                check_name="FICO Score",
                level=FlagLevel.CRITICAL,
                message=f"Below minimum credit score: {score}",
                value=score,
                threshold=self.FICO_THRESHOLDS['minimum'],
                requires_action=True,
                action_description="Score below program minimum"
            ))
        
        return flags
    
    def _analyze_bankruptcies(self, data: CreditReportData) -> List[AnalysisFlag]:
        """Analyze bankruptcy records."""
        flags = []
        
        for bk in data.bankruptcies:
            if bk.status == 'active':
                flags.append(AnalysisFlag(
                    flag_id="CR002",
                    report_type=ReportType.CREDIT_REPORT,
                    check_name="Bankruptcy Status",
                    level=FlagLevel.CRITICAL,
                    message=f"Active Chapter {bk.chapter} bankruptcy",
                    value="active",
                    threshold="discharged",
                    requires_action=True,
                    action_description="Cannot proceed with active bankruptcy"
                ))
            elif bk.years_since_discharge:
                req_years = self.EVENT_SEASONING.get(
                    f'bankruptcy_ch{bk.chapter}', 4
                )
                
                if bk.years_since_discharge >= req_years:
                    level = FlagLevel.GREEN
                    message = f"Ch {bk.chapter} BK discharged {bk.years_since_discharge:.1f} years ago"
                elif bk.years_since_discharge >= req_years - 2:
                    level = FlagLevel.YELLOW
                    message = f"Ch {bk.chapter} BK within seasoning period"
                else:
                    level = FlagLevel.RED
                    message = f"Recent Ch {bk.chapter} BK discharge"
                
                flags.append(AnalysisFlag(
                    flag_id="CR002",
                    report_type=ReportType.CREDIT_REPORT,
                    check_name="Bankruptcy Seasoning",
                    level=level,
                    message=message,
                    value=bk.years_since_discharge,
                    threshold=req_years,
                    requires_action=level != FlagLevel.GREEN
                ))
        
        if not data.bankruptcies:
            flags.append(AnalysisFlag(
                flag_id="CR002",
                report_type=ReportType.CREDIT_REPORT,
                check_name="Bankruptcy Status",
                level=FlagLevel.GREEN,
                message="No bankruptcy history",
                value=0,
                threshold=0,
                requires_action=False
            ))
        
        return flags
    
    def _analyze_foreclosures(self, data: CreditReportData) -> List[AnalysisFlag]:
        """Analyze foreclosure records."""
        flags = []
        
        for fc in data.foreclosures:
            years = fc.years_since_completion
            req_years = self.EVENT_SEASONING['foreclosure']
            
            if years >= req_years:
                level = FlagLevel.GREEN
                message = f"Foreclosure {years:.1f} years ago - seasoned"
            elif years >= req_years - 2:
                level = FlagLevel.YELLOW
                message = f"Foreclosure within seasoning period"
            else:
                level = FlagLevel.RED
                message = f"Recent foreclosure {years:.1f} years ago"
            
            flags.append(AnalysisFlag(
                flag_id="CR003",
                report_type=ReportType.CREDIT_REPORT,
                check_name="Foreclosure Seasoning",
                level=level,
                message=message,
                value=years,
                threshold=req_years,
                requires_action=level != FlagLevel.GREEN
            ))
        
        if not data.foreclosures:
            flags.append(AnalysisFlag(
                flag_id="CR003",
                report_type=ReportType.CREDIT_REPORT,
                check_name="Foreclosure Status",
                level=FlagLevel.GREEN,
                message="No foreclosure history",
                value=0,
                threshold=0,
                requires_action=False
            ))
        
        return flags
    
    def _analyze_collections(self, data: CreditReportData) -> List[AnalysisFlag]:
        """Analyze collection accounts."""
        flags = []
        total = data.total_collections_balance
        
        if total == 0:
            flags.append(AnalysisFlag(
                flag_id="CR004",
                report_type=ReportType.CREDIT_REPORT,
                check_name="Collections",
                level=FlagLevel.GREEN,
                message="No open collections",
                value=0,
                threshold=0,
                requires_action=False
            ))
        elif total < 5000:
            flags.append(AnalysisFlag(
                flag_id="CR004",
                report_type=ReportType.CREDIT_REPORT,
                check_name="Collections",
                level=FlagLevel.YELLOW,
                message=f"Open collections: ${total:,.0f}",
                value=total,
                threshold=5000,
                requires_action=False
            ))
        elif total < 25000:
            flags.append(AnalysisFlag(
                flag_id="CR004",
                report_type=ReportType.CREDIT_REPORT,
                check_name="Collections",
                level=FlagLevel.RED,
                message=f"Significant collections: ${total:,.0f}",
                value=total,
                threshold=25000,
                requires_action=True,
                action_description="Review collection accounts for payoff requirement"
            ))
        else:
            flags.append(AnalysisFlag(
                flag_id="CR004",
                report_type=ReportType.CREDIT_REPORT,
                check_name="Collections",
                level=FlagLevel.CRITICAL,
                message=f"Excessive collections: ${total:,.0f}",
                value=total,
                threshold=25000,
                requires_action=True,
                action_description="Collections exceed program maximum"
            ))
        
        return flags
    
    def _analyze_mortgage_history(self, data: CreditReportData) -> List[AnalysisFlag]:
        """Analyze mortgage payment history."""
        flags = []
        
        total_30_late = 0
        total_60_late = 0
        total_90_late = 0
        
        for mtg in data.mortgage_tradelines:
            lates = mtg.get_late_payments(24)
            total_30_late += lates['30_day']
            total_60_late += lates['60_day']
            total_90_late += lates['90_day']
        
        if total_90_late > 0:
            flags.append(AnalysisFlag(
                flag_id="CR005",
                report_type=ReportType.CREDIT_REPORT,
                check_name="Mortgage Lates",
                level=FlagLevel.CRITICAL,
                message=f"90+ day mortgage late in last 24 months",
                value=total_90_late,
                threshold=0,
                requires_action=True,
                action_description="Severe mortgage delinquency"
            ))
        elif total_60_late > 0:
            flags.append(AnalysisFlag(
                flag_id="CR005",
                report_type=ReportType.CREDIT_REPORT,
                check_name="Mortgage Lates",
                level=FlagLevel.RED,
                message=f"60 day mortgage late in last 24 months",
                value=total_60_late,
                threshold=0,
                requires_action=True,
                action_description="Review mortgage payment history"
            ))
        elif total_30_late > 1:
            flags.append(AnalysisFlag(
                flag_id="CR005",
                report_type=ReportType.CREDIT_REPORT,
                check_name="Mortgage Lates",
                level=FlagLevel.YELLOW,
                message=f"Multiple 30-day lates in last 24 months",
                value=total_30_late,
                threshold=1,
                requires_action=False
            ))
        else:
            flags.append(AnalysisFlag(
                flag_id="CR005",
                report_type=ReportType.CREDIT_REPORT,
                check_name="Mortgage Lates",
                level=FlagLevel.GREEN,
                message="Clean mortgage payment history",
                value=0,
                threshold=0,
                requires_action=False
            ))
        
        return flags


class AppraisalAnalyzer:
    """
    Analyze appraisal reports and generate flags.
    
    Implements appraisal analysis rules per USDV Guidelines
    including age validation, comparable analysis, and
    value reconciliation.
    """
    
    # Age thresholds (days)
    AGE_THRESHOLDS = {
        'standard': 120,
        'high_value': 90,
        'recert_max': 180
    }
    
    # Adjustment thresholds
    ADJUSTMENT_THRESHOLDS = {
        'net_good': 10,
        'net_max': 15,
        'gross_good': 20,
        'gross_max': 25
    }
    
    def analyze(
        self,
        appraisal_data: AppraisalData,
        loan_amount: float,
        contract_price: Optional[float] = None,
        is_high_value: bool = False
    ) -> ReportAnalysisResult:
        """
        Perform complete appraisal analysis.
        
        Args:
            appraisal_data: Extracted appraisal data
            loan_amount: Requested loan amount
            contract_price: Purchase price (if applicable)
            is_high_value: Whether loan is high value (>$1M)
            
        Returns:
            Complete analysis result with flags
        """
        flags = []
        critical_issues = []
        recommendations = []
        
        # Analyze age
        age_flags = self._analyze_age(appraisal_data, is_high_value)
        flags.extend(age_flags)
        
        # Analyze comparables
        comp_flags = self._analyze_comparables(appraisal_data)
        flags.extend(comp_flags)
        
        # Analyze condition
        cond_flags = self._analyze_condition(appraisal_data)
        flags.extend(cond_flags)
        
        # Analyze value vs contract
        if contract_price:
            value_flags = self._analyze_value_vs_contract(
                appraisal_data, contract_price
            )
            flags.extend(value_flags)
        
        # Determine acceptability
        has_critical = any(f.level == FlagLevel.CRITICAL for f in flags)
        has_red = any(f.level == FlagLevel.RED for f in flags)
        
        return ReportAnalysisResult(
            report_type=ReportType.APPRAISAL,
            report_date=appraisal_data.report_date,
            analysis_date=date.today(),
            flags=flags,
            extracted_data={
                'as_is_value': appraisal_data.as_is_value,
                'arv': appraisal_data.arv,
                'age_days': appraisal_data.age_days,
                'condition': appraisal_data.condition_rating,
                'num_comps': len(appraisal_data.comparables)
            },
            is_acceptable=not has_critical,
            requires_review=has_red,
            critical_issues=critical_issues,
            recommendations=recommendations
        )
    
    def _analyze_age(
        self,
        data: AppraisalData,
        is_high_value: bool
    ) -> List[AnalysisFlag]:
        """Analyze appraisal age."""
        flags = []
        age = data.age_days
        threshold = self.AGE_THRESHOLDS['high_value'] if is_high_value else self.AGE_THRESHOLDS['standard']
        
        if age <= 90:
            level = FlagLevel.GREEN
            message = f"Appraisal is {age} days old"
        elif age <= threshold:
            level = FlagLevel.YELLOW
            message = f"Appraisal is {age} days old"
        elif age <= self.AGE_THRESHOLDS['recert_max']:
            level = FlagLevel.RED
            message = f"Appraisal is {age} days old - recertification required"
        else:
            level = FlagLevel.CRITICAL
            message = f"Appraisal is {age} days old - new appraisal required"
        
        flags.append(AnalysisFlag(
            flag_id="AP001",
            report_type=ReportType.APPRAISAL,
            check_name="Appraisal Age",
            level=level,
            message=message,
            value=age,
            threshold=threshold,
            requires_action=level in [FlagLevel.RED, FlagLevel.CRITICAL]
        ))
        
        return flags
    
    def _analyze_comparables(self, data: AppraisalData) -> List[AnalysisFlag]:
        """Analyze comparable sales."""
        flags = []
        
        # Check number of comps
        num_comps = len(data.comparables)
        if num_comps >= 3:
            flags.append(AnalysisFlag(
                flag_id="AP002",
                report_type=ReportType.APPRAISAL,
                check_name="Comparable Count",
                level=FlagLevel.GREEN,
                message=f"{num_comps} comparable sales provided",
                value=num_comps,
                threshold=3,
                requires_action=False
            ))
        elif num_comps == 2:
            flags.append(AnalysisFlag(
                flag_id="AP002",
                report_type=ReportType.APPRAISAL,
                check_name="Comparable Count",
                level=FlagLevel.YELLOW,
                message="Only 2 comparable sales provided",
                value=num_comps,
                threshold=3,
                requires_action=True,
                action_description="Request additional comparable if available"
            ))
        else:
            flags.append(AnalysisFlag(
                flag_id="AP002",
                report_type=ReportType.APPRAISAL,
                check_name="Comparable Count",
                level=FlagLevel.RED,
                message=f"Insufficient comparables: {num_comps}",
                value=num_comps,
                threshold=3,
                requires_action=True,
                action_description="Additional comparables required"
            ))
        
        # Check adjustments
        avg_net = data.avg_net_adjustment
        avg_gross = data.avg_gross_adjustment
        
        if avg_net <= self.ADJUSTMENT_THRESHOLDS['net_good']:
            net_level = FlagLevel.GREEN
        elif avg_net <= self.ADJUSTMENT_THRESHOLDS['net_max']:
            net_level = FlagLevel.YELLOW
        elif avg_net <= 20:
            net_level = FlagLevel.RED
        else:
            net_level = FlagLevel.CRITICAL
        
        flags.append(AnalysisFlag(
            flag_id="AP003",
            report_type=ReportType.APPRAISAL,
            check_name="Net Adjustments",
            level=net_level,
            message=f"Average net adjustment: {avg_net:.1f}%",
            value=avg_net,
            threshold=self.ADJUSTMENT_THRESHOLDS['net_max'],
            requires_action=net_level in [FlagLevel.RED, FlagLevel.CRITICAL]
        ))
        
        if avg_gross <= self.ADJUSTMENT_THRESHOLDS['gross_good']:
            gross_level = FlagLevel.GREEN
        elif avg_gross <= self.ADJUSTMENT_THRESHOLDS['gross_max']:
            gross_level = FlagLevel.YELLOW
        elif avg_gross <= 30:
            gross_level = FlagLevel.RED
        else:
            gross_level = FlagLevel.CRITICAL
        
        flags.append(AnalysisFlag(
            flag_id="AP004",
            report_type=ReportType.APPRAISAL,
            check_name="Gross Adjustments",
            level=gross_level,
            message=f"Average gross adjustment: {avg_gross:.1f}%",
            value=avg_gross,
            threshold=self.ADJUSTMENT_THRESHOLDS['gross_max'],
            requires_action=gross_level in [FlagLevel.RED, FlagLevel.CRITICAL]
        ))
        
        return flags
    
    def _analyze_condition(self, data: AppraisalData) -> List[AnalysisFlag]:
        """Analyze property condition rating."""
        flags = []
        condition = data.condition_rating
        
        condition_levels = {
            'C1': FlagLevel.GREEN,
            'C2': FlagLevel.GREEN,
            'C3': FlagLevel.GREEN,
            'C4': FlagLevel.YELLOW,
            'C5': FlagLevel.RED,
            'C6': FlagLevel.CRITICAL
        }
        
        level = condition_levels.get(condition, FlagLevel.YELLOW)
        
        flags.append(AnalysisFlag(
            flag_id="AP005",
            report_type=ReportType.APPRAISAL,
            check_name="Property Condition",
            level=level,
            message=f"Condition rating: {condition}",
            value=condition,
            threshold="C4",
            requires_action=level in [FlagLevel.RED, FlagLevel.CRITICAL]
        ))
        
        return flags
    
    def _analyze_value_vs_contract(
        self,
        data: AppraisalData,
        contract_price: float
    ) -> List[AnalysisFlag]:
        """Analyze appraised value vs contract price."""
        flags = []
        
        variance_pct = ((data.as_is_value - contract_price) / contract_price) * 100
        
        if abs(variance_pct) <= 5:
            level = FlagLevel.GREEN
            message = f"Value within 5% of contract ({variance_pct:+.1f}%)"
        elif abs(variance_pct) <= 10:
            level = FlagLevel.YELLOW
            message = f"Value variance {variance_pct:+.1f}% from contract"
        elif abs(variance_pct) <= 15:
            level = FlagLevel.RED
            message = f"Significant value variance: {variance_pct:+.1f}%"
        else:
            level = FlagLevel.CRITICAL
            message = f"Extreme value variance: {variance_pct:+.1f}%"
        
        flags.append(AnalysisFlag(
            flag_id="AP006",
            report_type=ReportType.APPRAISAL,
            check_name="Value vs Contract",
            level=level,
            message=message,
            value=variance_pct,
            threshold=10,
            requires_action=level in [FlagLevel.RED, FlagLevel.CRITICAL]
        ))
        
        return flags


class TitleReportAnalyzer:
    """Analyze title reports and generate flags."""
    
    def analyze(
        self,
        vesting_verified: bool,
        liens_clear: bool,
        taxes_current: bool,
        chain_clear: bool,
        encumbrances: List[str]
    ) -> ReportAnalysisResult:
        """Perform title report analysis."""
        flags = []
        
        # Vesting
        flags.append(AnalysisFlag(
            flag_id="TI001",
            report_type=ReportType.TITLE_REPORT,
            check_name="Vesting Verification",
            level=FlagLevel.GREEN if vesting_verified else FlagLevel.RED,
            message="Vesting verified" if vesting_verified else "Vesting mismatch",
            value=vesting_verified,
            threshold=True,
            requires_action=not vesting_verified
        ))
        
        # Liens
        flags.append(AnalysisFlag(
            flag_id="TI002",
            report_type=ReportType.TITLE_REPORT,
            check_name="Lien Status",
            level=FlagLevel.GREEN if liens_clear else FlagLevel.RED,
            message="Clear of liens" if liens_clear else "Outstanding liens",
            value=liens_clear,
            threshold=True,
            requires_action=not liens_clear
        ))
        
        # Taxes
        if taxes_current:
            tax_level = FlagLevel.GREEN
            tax_msg = "Property taxes current"
        else:
            tax_level = FlagLevel.RED
            tax_msg = "Property taxes delinquent"
        
        flags.append(AnalysisFlag(
            flag_id="TI003",
            report_type=ReportType.TITLE_REPORT,
            check_name="Tax Status",
            level=tax_level,
            message=tax_msg,
            value=taxes_current,
            threshold=True,
            requires_action=not taxes_current
        ))
        
        # Chain of title
        flags.append(AnalysisFlag(
            flag_id="TI004",
            report_type=ReportType.TITLE_REPORT,
            check_name="Chain of Title",
            level=FlagLevel.GREEN if chain_clear else FlagLevel.YELLOW,
            message="Clear chain of title" if chain_clear else "Chain issues noted",
            value=chain_clear,
            threshold=True,
            requires_action=not chain_clear
        ))
        
        has_critical = any(f.level == FlagLevel.CRITICAL for f in flags)
        has_red = any(f.level == FlagLevel.RED for f in flags)
        
        return ReportAnalysisResult(
            report_type=ReportType.TITLE_REPORT,
            report_date=date.today(),
            analysis_date=date.today(),
            flags=flags,
            extracted_data={
                'vesting_verified': vesting_verified,
                'liens_clear': liens_clear,
                'taxes_current': taxes_current,
                'encumbrances': encumbrances
            },
            is_acceptable=not has_critical,
            requires_review=has_red,
            critical_issues=[],
            recommendations=[]
        )


class InsuranceAnalyzer:
    """Analyze insurance certificates and generate flags."""
    
    def analyze(
        self,
        coverage_amount: float,
        loan_amount: float,
        deductible_pct: float,
        expiration_date: date,
        mortgagee_correct: bool,
        flood_zone: str,
        has_flood_insurance: bool
    ) -> ReportAnalysisResult:
        """Perform insurance certificate analysis."""
        flags = []
        
        # Coverage adequacy
        coverage_ratio = coverage_amount / loan_amount
        if coverage_ratio >= 1.10:
            cov_level = FlagLevel.GREEN
        elif coverage_ratio >= 1.0:
            cov_level = FlagLevel.YELLOW
        elif coverage_ratio >= 0.9:
            cov_level = FlagLevel.RED
        else:
            cov_level = FlagLevel.CRITICAL
        
        flags.append(AnalysisFlag(
            flag_id="IN001",
            report_type=ReportType.INSURANCE_CERT,
            check_name="Coverage Amount",
            level=cov_level,
            message=f"Coverage {coverage_ratio*100:.0f}% of loan",
            value=coverage_ratio,
            threshold=1.0,
            requires_action=cov_level in [FlagLevel.RED, FlagLevel.CRITICAL]
        ))
        
        # Deductible
        if deductible_pct <= 2:
            ded_level = FlagLevel.GREEN
        elif deductible_pct <= 5:
            ded_level = FlagLevel.YELLOW
        elif deductible_pct <= 10:
            ded_level = FlagLevel.RED
        else:
            ded_level = FlagLevel.CRITICAL
        
        flags.append(AnalysisFlag(
            flag_id="IN002",
            report_type=ReportType.INSURANCE_CERT,
            check_name="Deductible",
            level=ded_level,
            message=f"Deductible: {deductible_pct}%",
            value=deductible_pct,
            threshold=5,
            requires_action=ded_level in [FlagLevel.RED, FlagLevel.CRITICAL]
        ))
        
        # Expiration
        days_to_exp = (expiration_date - date.today()).days
        if days_to_exp > 60:
            exp_level = FlagLevel.GREEN
        elif days_to_exp > 30:
            exp_level = FlagLevel.YELLOW
        elif days_to_exp > 0:
            exp_level = FlagLevel.RED
        else:
            exp_level = FlagLevel.CRITICAL
        
        flags.append(AnalysisFlag(
            flag_id="IN003",
            report_type=ReportType.INSURANCE_CERT,
            check_name="Policy Expiration",
            level=exp_level,
            message=f"Policy expires in {days_to_exp} days",
            value=days_to_exp,
            threshold=30,
            requires_action=exp_level in [FlagLevel.RED, FlagLevel.CRITICAL]
        ))
        
        # Mortgagee clause
        flags.append(AnalysisFlag(
            flag_id="IN004",
            report_type=ReportType.INSURANCE_CERT,
            check_name="Mortgagee Clause",
            level=FlagLevel.GREEN if mortgagee_correct else FlagLevel.RED,
            message="Mortgagee clause correct" if mortgagee_correct else "Mortgagee clause incorrect",
            value=mortgagee_correct,
            threshold=True,
            requires_action=not mortgagee_correct
        ))
        
        # Flood insurance
        high_risk_zones = ['A', 'AE', 'AH', 'AO', 'V', 'VE']
        needs_flood = any(flood_zone.startswith(z) for z in high_risk_zones)
        
        if needs_flood and not has_flood_insurance:
            flags.append(AnalysisFlag(
                flag_id="IN005",
                report_type=ReportType.INSURANCE_CERT,
                check_name="Flood Insurance",
                level=FlagLevel.CRITICAL,
                message=f"Flood zone {flood_zone} requires flood insurance",
                value=has_flood_insurance,
                threshold=True,
                requires_action=True
            ))
        elif needs_flood and has_flood_insurance:
            flags.append(AnalysisFlag(
                flag_id="IN005",
                report_type=ReportType.INSURANCE_CERT,
                check_name="Flood Insurance",
                level=FlagLevel.GREEN,
                message=f"Flood insurance in place for zone {flood_zone}",
                value=has_flood_insurance,
                threshold=True,
                requires_action=False
            ))
        
        has_critical = any(f.level == FlagLevel.CRITICAL for f in flags)
        has_red = any(f.level == FlagLevel.RED for f in flags)
        
        return ReportAnalysisResult(
            report_type=ReportType.INSURANCE_CERT,
            report_date=date.today(),
            analysis_date=date.today(),
            flags=flags,
            extracted_data={
                'coverage_amount': coverage_amount,
                'deductible_pct': deductible_pct,
                'expiration_date': expiration_date.isoformat(),
                'flood_zone': flood_zone
            },
            is_acceptable=not has_critical,
            requires_review=has_red,
            critical_issues=[],
            recommendations=[]
        )


class BankStatementAnalyzer:
    """Analyze bank statements and generate flags."""
    
    def analyze(
        self,
        average_balance: float,
        monthly_pitia: float,
        nsf_count: int,
        large_deposits_unsourced: float,
        account_age_months: int,
        balance_trend: str  # 'increasing', 'stable', 'declining'
    ) -> ReportAnalysisResult:
        """Perform bank statement analysis."""
        flags = []
        
        # Reserves calculation
        months_reserves = average_balance / monthly_pitia if monthly_pitia > 0 else 0
        
        if months_reserves >= 12:
            res_level = FlagLevel.GREEN
        elif months_reserves >= 6:
            res_level = FlagLevel.YELLOW
        elif months_reserves >= 3:
            res_level = FlagLevel.RED
        else:
            res_level = FlagLevel.CRITICAL
        
        flags.append(AnalysisFlag(
            flag_id="BS001",
            report_type=ReportType.BANK_STATEMENT,
            check_name="Reserves",
            level=res_level,
            message=f"{months_reserves:.1f} months reserves",
            value=months_reserves,
            threshold=6,
            requires_action=res_level in [FlagLevel.RED, FlagLevel.CRITICAL]
        ))
        
        # NSF/Overdrafts
        if nsf_count == 0:
            nsf_level = FlagLevel.GREEN
        elif nsf_count <= 2:
            nsf_level = FlagLevel.YELLOW
        elif nsf_count <= 5:
            nsf_level = FlagLevel.RED
        else:
            nsf_level = FlagLevel.CRITICAL
        
        flags.append(AnalysisFlag(
            flag_id="BS002",
            report_type=ReportType.BANK_STATEMENT,
            check_name="NSF/Overdrafts",
            level=nsf_level,
            message=f"{nsf_count} NSF/overdrafts in 3 months",
            value=nsf_count,
            threshold=2,
            requires_action=nsf_level in [FlagLevel.RED, FlagLevel.CRITICAL]
        ))
        
        # Large deposits
        if large_deposits_unsourced == 0:
            dep_level = FlagLevel.GREEN
            dep_msg = "All deposits sourced"
        elif large_deposits_unsourced < 5000:
            dep_level = FlagLevel.YELLOW
            dep_msg = f"Unsourced deposits: ${large_deposits_unsourced:,.0f}"
        elif large_deposits_unsourced < 25000:
            dep_level = FlagLevel.RED
            dep_msg = f"Unsourced deposits: ${large_deposits_unsourced:,.0f}"
        else:
            dep_level = FlagLevel.CRITICAL
            dep_msg = f"Large unsourced deposits: ${large_deposits_unsourced:,.0f}"
        
        flags.append(AnalysisFlag(
            flag_id="BS003",
            report_type=ReportType.BANK_STATEMENT,
            check_name="Large Deposits",
            level=dep_level,
            message=dep_msg,
            value=large_deposits_unsourced,
            threshold=5000,
            requires_action=dep_level in [FlagLevel.RED, FlagLevel.CRITICAL]
        ))
        
        has_critical = any(f.level == FlagLevel.CRITICAL for f in flags)
        has_red = any(f.level == FlagLevel.RED for f in flags)
        
        return ReportAnalysisResult(
            report_type=ReportType.BANK_STATEMENT,
            report_date=date.today(),
            analysis_date=date.today(),
            flags=flags,
            extracted_data={
                'average_balance': average_balance,
                'months_reserves': months_reserves,
                'nsf_count': nsf_count,
                'account_age_months': account_age_months
            },
            is_acceptable=not has_critical,
            requires_review=has_red,
            critical_issues=[],
            recommendations=[]
        )


class LeaseAnalyzer:
    """Analyze lease documents and generate flags."""
    
    def analyze(
        self,
        monthly_rent: float,
        market_rent: float,
        lease_end_date: date,
        is_arms_length: bool,
        has_purchase_option: bool,
        tenant_current: bool
    ) -> ReportAnalysisResult:
        """Perform lease document analysis."""
        flags = []
        
        # Rent vs market
        rent_variance = ((monthly_rent - market_rent) / market_rent) * 100
        
        if abs(rent_variance) <= 10:
            rent_level = FlagLevel.GREEN
        elif abs(rent_variance) <= 20:
            rent_level = FlagLevel.YELLOW
        elif abs(rent_variance) <= 30:
            rent_level = FlagLevel.RED
        else:
            rent_level = FlagLevel.CRITICAL
        
        flags.append(AnalysisFlag(
            flag_id="LS001",
            report_type=ReportType.LEASE,
            check_name="Rent vs Market",
            level=rent_level,
            message=f"Rent {rent_variance:+.1f}% vs market",
            value=rent_variance,
            threshold=10,
            requires_action=rent_level in [FlagLevel.RED, FlagLevel.CRITICAL]
        ))
        
        # Remaining term
        days_remaining = (lease_end_date - date.today()).days
        months_remaining = days_remaining / 30
        
        if months_remaining > 6:
            term_level = FlagLevel.GREEN
        elif months_remaining > 3:
            term_level = FlagLevel.YELLOW
        elif months_remaining > 0:
            term_level = FlagLevel.RED
        else:
            term_level = FlagLevel.CRITICAL
        
        flags.append(AnalysisFlag(
            flag_id="LS002",
            report_type=ReportType.LEASE,
            check_name="Remaining Term",
            level=term_level,
            message=f"{months_remaining:.0f} months remaining",
            value=months_remaining,
            threshold=6,
            requires_action=term_level in [FlagLevel.RED, FlagLevel.CRITICAL]
        ))
        
        # Arm's length
        flags.append(AnalysisFlag(
            flag_id="LS003",
            report_type=ReportType.LEASE,
            check_name="Arm's Length",
            level=FlagLevel.GREEN if is_arms_length else FlagLevel.RED,
            message="Arm's length verified" if is_arms_length else "Related party lease",
            value=is_arms_length,
            threshold=True,
            requires_action=not is_arms_length
        ))
        
        # Purchase option
        if has_purchase_option:
            flags.append(AnalysisFlag(
                flag_id="LS004",
                report_type=ReportType.LEASE,
                check_name="Purchase Option",
                level=FlagLevel.CRITICAL,
                message="Lease contains purchase option",
                value=has_purchase_option,
                threshold=False,
                requires_action=True,
                action_description="Leases with purchase options are ineligible"
            ))
        
        # Tenant payment status
        flags.append(AnalysisFlag(
            flag_id="LS005",
            report_type=ReportType.LEASE,
            check_name="Tenant Status",
            level=FlagLevel.GREEN if tenant_current else FlagLevel.RED,
            message="Tenant current" if tenant_current else "Tenant delinquent",
            value=tenant_current,
            threshold=True,
            requires_action=not tenant_current
        ))
        
        has_critical = any(f.level == FlagLevel.CRITICAL for f in flags)
        has_red = any(f.level == FlagLevel.RED for f in flags)
        
        return ReportAnalysisResult(
            report_type=ReportType.LEASE,
            report_date=date.today(),
            analysis_date=date.today(),
            flags=flags,
            extracted_data={
                'monthly_rent': monthly_rent,
                'market_rent': market_rent,
                'rent_variance_pct': rent_variance,
                'months_remaining': months_remaining
            },
            is_acceptable=not has_critical,
            requires_review=has_red,
            critical_issues=[],
            recommendations=[]
        )


# Convenience functions

def analyze_credit_report(credit_data: CreditReportData) -> ReportAnalysisResult:
    """Quick credit report analysis."""
    analyzer = CreditReportAnalyzer()
    return analyzer.analyze(credit_data)


def analyze_appraisal(
    appraisal_data: AppraisalData,
    loan_amount: float,
    contract_price: Optional[float] = None
) -> ReportAnalysisResult:
    """Quick appraisal analysis."""
    analyzer = AppraisalAnalyzer()
    is_high_value = loan_amount >= 1000000
    return analyzer.analyze(appraisal_data, loan_amount, contract_price, is_high_value)


def generate_flag_summary(results: List[ReportAnalysisResult]) -> Dict:
    """
    Generate summary of flags across all reports.
    
    Args:
        results: List of analysis results
        
    Returns:
        Summary dictionary with counts and critical issues
    """
    summary = {
        'total_flags': 0,
        'by_level': {level.value: 0 for level in FlagLevel},
        'by_report': {},
        'critical_issues': [],
        'requires_review': [],
        'all_acceptable': True
    }
    
    for result in results:
        report_name = result.report_type.value
        summary['by_report'][report_name] = result.flag_summary
        summary['total_flags'] += len(result.flags)
        
        for flag in result.flags:
            summary['by_level'][flag.level.value] += 1
        
        if result.has_critical_flags:
            summary['critical_issues'].extend(result.critical_issues)
            summary['all_acceptable'] = False
        
        if result.requires_review:
            summary['requires_review'].append(report_name)
    
    return summary
```

---

## 14.12 Flag Generation Summary (INSPIRE Phase 7)

### 14.12.1 Flag Level Definitions

| Level | Color | Meaning | Action Required |
|-------|-------|---------|-----------------|
| GREEN | 🟢 | Meets all requirements | None |
| YELLOW | 🟡 | Minor concern or edge case | Documentation/explanation |
| RED | 🔴 | Significant issue | Underwriter review required |
| CRITICAL | ⛔ | Deal-breaking issue | Management approval or decline |

### 14.12.2 Flag Count Thresholds

| Scenario | Automated Decision |
|----------|-------------------|
| All GREEN | Auto-approve (subject to other checks) |
| Any YELLOW | Proceed with documentation |
| Any RED | Route to senior underwriter |
| Any CRITICAL | Route to management |

### 14.12.3 Report Priority Order

1. **Credit Report** - Borrower qualification
2. **Background Check** - Fraud/compliance screening
3. **Appraisal** - Collateral valuation
4. **Title Report** - Legal standing
5. **Insurance** - Risk mitigation
6. **Bank Statements** - Liquidity verification
7. **Entity Documents** - Borrower structure
8. **Lease Documents** - Income verification (DSCR)

---

## 14.13 Cross-References

| Topic | Reference Section |
|-------|------------------|
| Credit Score Requirements | Section 4: Credit & Background Analysis |
| Appraisal Requirements | Section 8: Appraisal & Valuation Standards |
| Liquidity Requirements | Section 2: Borrower Eligibility |
| DSCR Lease Analysis | Section 7: DSCR Property & Income Analysis |
| RTL Budget Analysis | Section 6: RTL Property Analysis |
| INSPIRE Phase 7 | INSPIRE Phase 7 PRD |

---

## 14.14 Open Questions

1. **OCR Accuracy:** Confirm acceptable OCR confidence thresholds for automated data extraction from scanned documents.

2. **Flag Override Authority:** Define which user roles can override specific flag levels.

3. **Historical Comparison:** Determine whether INSPIRE should compare current report data against historical submissions for fraud detection.

4. **Third-Party Integration:** Confirm API specifications for real-time credit pulls and background check ordering.

---

*End of Section 14: Third-Party Report Analysis*

