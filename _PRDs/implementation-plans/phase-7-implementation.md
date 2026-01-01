# Phase 7 Implementation Plan: AI Analysis & Credit Memo

**Document Version:** 1.0  
**PRD Reference:** INSPIRE Phase 7 PRD  
**Last Updated:** December 2024  
**Status:** Implementation Ready

---

## 1. Executive Summary

### 1.1 Phase Overview

Phase 7 implements AI-powered document analysis and automated credit memo generation:
- **Real-Time Analysis** - Documents analyzed against underwriting guidelines as they arrive
- **Red/Green Flag System** - Visual indicators for guideline compliance and exceptions
- **Automated Credit Memo** - AI-generated underwriting summary with findings
- **Exception Management** - Identification, categorization, and tracking of exceptions

### 1.2 Success Metrics (from PRD)

| Metric | Target |
|--------|--------|
| Document analysis automation rate | >95% |
| Flag accuracy | >95% |
| Credit memo auto-generation rate | >90% |
| Time from docs complete to credit memo | <30 minutes |
| Exception identification accuracy | >90% |
| Manual underwriting review reduction | 40% |

### 1.3 Key Dependencies

| Dependency | Status | Notes |
|------------|--------|-------|
| Phase 5-6 Complete | Required | Documents must be in data room |
| LLM API (Claude/GPT) | Required | Document analysis |
| Underwriting Guidelines | Required | Investor-specific rules |
| Deal Sizer (Phase 3) | Required | Leverage/pricing validation |
| Document OCR | Required | Text extraction |

---

## 2. Page/Screen Inventory

### 2.1 Complete Page List

| Page ID | Page Name | Route | User Role | Entry Point |
|---------|-----------|-------|-----------|-------------|
| P7-01 | Analysis Dashboard | `/deals/:id/analysis` | Internal | Deal detail |
| P7-02 | Document Analysis Detail | `/deals/:id/analysis/:docId` | Internal | Analysis dashboard |
| P7-03 | Flag Manager | `/deals/:id/flags` | Internal | Deal detail, Dashboard |
| P7-04 | Exception Request | `/deals/:id/exceptions` | Internal | Flag manager |
| P7-05 | Credit Memo | `/deals/:id/credit-memo` | Internal | Deal detail |
| P7-06 | Credit Memo Editor | `/deals/:id/credit-memo/edit` | Internal | Credit memo |

### 2.2 Analysis Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PHASE 7 ANALYSIS FLOW                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Document Received → OCR/Extract → AI Analysis → Generate Flags →            │
│  Update Deal Summary → Aggregate Flags → Generate Credit Memo →              │
│  Identify Exceptions → Present for Review                                    │
│                                                                              │
│  CONTINUOUS UPDATES:                                                         │
│  As each document arrives, analysis runs automatically.                      │
│  Credit memo updates in real-time with new findings.                         │
│  Flags aggregate across all documents.                                       │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Per-Page Specifications

---

### 3.1 P7-01: Analysis Dashboard

#### 3.1.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Central view of all AI analysis findings for a deal |
| **User Roles** | Underwriter, Loan Officer |
| **Entry Points** | Deal detail tabs, Pipeline card |
| **PRD Reference** | Phase 7 PRD, Section 3 |

#### 3.1.2 Information Architecture

**Primary Data:** AnalysisSummary, Flag[], DocumentAnalysis[]

**Content Hierarchy:**
1. Deal header with overall risk score
2. Flag summary (Red/Yellow/Green counts)
3. Key findings cards
4. Document analysis list
5. Exception summary

#### 3.1.3 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `card` | Summary cards, finding cards |
| `badge` | Flag severity badges |
| `table` | Document analysis list |
| `progress` | Analysis completion |
| `alert` | Critical findings |
| `tabs` | By category (Borrower, Property, etc.) |
| `accordion` | Expandable findings |
| `tooltip` | Guideline references |

**React Custom Components:**

```typescript
// components/analysis/AnalysisDashboard.tsx
interface AnalysisDashboardProps {
  dealId: string;
  summary: AnalysisSummary;
  flags: Flag[];
  documentAnalyses: DocumentAnalysis[];
  onViewDocument: (docId: string) => void;
  onViewFlag: (flagId: string) => void;
  onGenerateMemo: () => void;
}

// Main analysis dashboard
// Composition: Uses ShadCN Card, Badge, Table, Tabs
```

```typescript
// components/analysis/FlagSummaryCard.tsx
interface FlagSummaryCardProps {
  redCount: number;
  yellowCount: number;
  greenCount: number;
  totalChecks: number;
  onClick: (severity: FlagSeverity) => void;
}

// Flag count summary with visual indicators
// Composition: Uses ShadCN Card, Badge
```

```typescript
// components/analysis/RiskScoreGauge.tsx
interface RiskScoreGaugeProps {
  score: number; // 0-100
  label: string;
  breakdown: {
    category: string;
    score: number;
    weight: number;
  }[];
}

// Visual risk score indicator
// Composition: Uses custom SVG gauge
```

```typescript
// components/analysis/KeyFindingsCard.tsx
interface KeyFindingsCardProps {
  findings: {
    id: string;
    category: string;
    title: string;
    severity: FlagSeverity;
    summary: string;
    guidelineRef: string;
  }[];
  maxVisible?: number;
  onViewAll: () => void;
}

// Critical findings summary
// Composition: Uses ShadCN Card, Badge, Accordion
```

```typescript
// components/analysis/DocumentAnalysisList.tsx
interface DocumentAnalysisListProps {
  analyses: DocumentAnalysis[];
  onView: (docId: string) => void;
  onReanalyze: (docId: string) => void;
}

// List of analyzed documents with status
// Composition: Uses ShadCN Table, Badge, Button
```

#### 3.1.4 Data Requirements

```typescript
interface AnalysisSummary {
  dealId: string;
  
  // Overall scores
  riskScore: number; // 0-100, lower is better
  confidenceScore: number; // 0-100
  
  // Flag counts
  redFlags: number;
  yellowFlags: number;
  greenFlags: number;
  totalChecks: number;
  
  // Category scores
  categoryScores: {
    borrower: number;
    property: number;
    valuation: number;
    title: number;
    insurance: number;
    financial: number;
  };
  
  // Analysis status
  documentsAnalyzed: number;
  documentsTotal: number;
  lastAnalyzedAt: Date;
  
  // Key findings
  criticalFindings: string[];
  exceptionsIdentified: number;
  
  // Credit memo status
  creditMemoStatus: 'pending' | 'generating' | 'ready' | 'approved';
  creditMemoId?: string;
}

interface DocumentAnalysis {
  id: string;
  dealId: string;
  documentId: string;
  documentType: string;
  documentName: string;
  
  // Analysis status
  status: 'pending' | 'analyzing' | 'complete' | 'error';
  analyzedAt?: Date;
  
  // Results
  flags: Flag[];
  extractedData: Record<string, any>;
  summary: string;
  
  // Confidence
  confidence: number;
  needsManualReview: boolean;
  
  // Error info
  error?: string;
}

interface Flag {
  id: string;
  dealId: string;
  documentId?: string;
  
  // Classification
  category: FlagCategory;
  severity: FlagSeverity;
  
  // Content
  title: string;
  description: string;
  
  // Guideline reference
  guidelineRef: string;
  guidelineText: string;
  investorId?: string;
  
  // Actual vs expected
  actualValue?: string | number;
  expectedValue?: string | number;
  threshold?: string | number;
  
  // Exception handling
  isException: boolean;
  exceptionStatus?: ExceptionStatus;
  exceptionId?: string;
  
  // Resolution
  resolvedAt?: Date;
  resolvedBy?: string;
  resolution?: string;
  
  createdAt: Date;
  updatedAt: Date;
}

type FlagCategory = 
  | 'credit'
  | 'background'
  | 'entity'
  | 'experience'
  | 'property'
  | 'valuation'
  | 'title'
  | 'insurance'
  | 'financial'
  | 'leverage'
  | 'pricing';

type FlagSeverity = 'red' | 'yellow' | 'green';

type ExceptionStatus = 
  | 'pending'
  | 'approved'
  | 'denied'
  | 'escalated';
```

#### 3.1.5 Mock Data

```json
{
  "dealId": "deal_abc123",
  "summary": {
    "riskScore": 35,
    "confidenceScore": 92,
    "redFlags": 2,
    "yellowFlags": 5,
    "greenFlags": 28,
    "totalChecks": 35,
    "categoryScores": {
      "borrower": 85,
      "property": 90,
      "valuation": 75,
      "title": 95,
      "insurance": 100,
      "financial": 80
    },
    "documentsAnalyzed": 12,
    "documentsTotal": 14,
    "lastAnalyzedAt": "2024-12-15T14:30:00Z",
    "criticalFindings": [
      "FICO score 680 below minimum 700 for investor",
      "ARV variance 8% exceeds 5% threshold"
    ],
    "exceptionsIdentified": 2,
    "creditMemoStatus": "ready",
    "creditMemoId": "memo_001"
  },
  "flags": [
    {
      "id": "flag_001",
      "category": "credit",
      "severity": "red",
      "title": "FICO Below Minimum",
      "description": "Middle FICO score 680 is below investor minimum of 700",
      "guidelineRef": "Archwest DSCR 3.1.2",
      "guidelineText": "Minimum FICO score of 700 required",
      "actualValue": 680,
      "expectedValue": 700,
      "isException": true,
      "exceptionStatus": "pending",
      "exceptionId": "exc_001"
    },
    {
      "id": "flag_002",
      "category": "valuation",
      "severity": "red",
      "title": "ARV Variance High",
      "description": "Appraisal ARV differs from feasibility by 8%",
      "guidelineRef": "Archwest RTL 5.2.1",
      "guidelineText": "ARV variance must be within 5%",
      "actualValue": "8%",
      "threshold": "5%",
      "isException": true,
      "exceptionStatus": "pending",
      "exceptionId": "exc_002"
    },
    {
      "id": "flag_003",
      "category": "experience",
      "severity": "yellow",
      "title": "Limited Track Record",
      "description": "Borrower has completed 3 projects in past 36 months",
      "guidelineRef": "Archwest RTL 2.3.1",
      "guidelineText": "5+ projects preferred for Tier 1 pricing",
      "actualValue": 3,
      "expectedValue": 5,
      "isException": false
    },
    {
      "id": "flag_004",
      "category": "title",
      "severity": "green",
      "title": "Clear Title",
      "description": "No liens or encumbrances found",
      "guidelineRef": "Standard",
      "isException": false
    }
  ],
  "documentAnalyses": [
    {
      "id": "analysis_001",
      "documentId": "doc_credit_001",
      "documentType": "credit_report",
      "documentName": "Tri-Merge Credit Report",
      "status": "complete",
      "analyzedAt": "2024-12-10T10:15:00Z",
      "flags": ["flag_001"],
      "summary": "Credit report shows middle FICO of 680. No derogatory items in past 24 months. DTI not applicable for DSCR loan.",
      "confidence": 95
    },
    {
      "id": "analysis_002",
      "documentId": "doc_appraisal_001",
      "documentType": "appraisal",
      "documentName": "Full Appraisal Report",
      "status": "complete",
      "analyzedAt": "2024-12-15T14:00:00Z",
      "flags": ["flag_002"],
      "summary": "As-is value $425,000, ARV $585,000. Subject property is 3BR/2BA SFR. Comparable selection adequate. ARV shows 8% variance from feasibility study.",
      "confidence": 88
    }
  ]
}
```

---

### 3.2 P7-03: Flag Manager

#### 3.2.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | View, filter, and manage all flags for a deal |
| **User Roles** | Underwriter, Loan Officer |
| **Entry Points** | Analysis dashboard, Deal detail |
| **PRD Reference** | Phase 7 PRD, Section 4 |

#### 3.2.2 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `card` | Flag cards |
| `badge` | Severity badges |
| `table` | Flag list view |
| `button` | Request Exception, Resolve |
| `select` | Filter by category, severity |
| `dialog` | Exception request modal |
| `tabs` | By status (Active, Resolved, Exceptions) |
| `tooltip` | Guideline details |

**React Custom Components:**

```typescript
// components/flags/FlagManager.tsx
interface FlagManagerProps {
  dealId: string;
  flags: Flag[];
  onRequestException: (flagId: string) => void;
  onResolve: (flagId: string, resolution: string) => void;
  onViewDocument: (docId: string) => void;
}

// Main flag management view
// Composition: Uses ShadCN Table, Tabs, Select
```

```typescript
// components/flags/FlagCard.tsx
interface FlagCardProps {
  flag: Flag;
  onRequestException: () => void;
  onResolve: () => void;
  onViewDocument: () => void;
  expanded?: boolean;
}

// Individual flag card with details
// Composition: Uses ShadCN Card, Badge, Button
```

```typescript
// components/flags/FlagSeverityBadge.tsx
interface FlagSeverityBadgeProps {
  severity: FlagSeverity;
  size?: 'sm' | 'md' | 'lg';
}

// Color-coded severity badge
// Composition: Uses ShadCN Badge
```

```typescript
// components/flags/FlagFilters.tsx
interface FlagFiltersProps {
  categories: FlagCategory[];
  selectedCategories: FlagCategory[];
  selectedSeverities: FlagSeverity[];
  showResolved: boolean;
  onChange: (filters: FlagFilters) => void;
}

// Filter controls for flag list
// Composition: Uses ShadCN Select, Checkbox
```

```typescript
// components/flags/ExceptionRequestDialog.tsx
interface ExceptionRequestDialogProps {
  flag: Flag;
  open: boolean;
  onSubmit: (request: ExceptionRequest) => void;
  onCancel: () => void;
}

// Modal for requesting exception
// Composition: Uses ShadCN Dialog, Form, Textarea
```

#### 3.2.3 Flag Display Rules

```typescript
const FLAG_DISPLAY_CONFIG: Record<FlagSeverity, FlagDisplayConfig> = {
  red: {
    color: 'destructive',
    bgColor: 'bg-red-50',
    borderColor: 'border-red-200',
    icon: 'XCircle',
    label: 'Red Flag',
    description: 'Critical issue requiring exception or resolution',
    actions: ['request_exception', 'resolve'],
  },
  yellow: {
    color: 'warning',
    bgColor: 'bg-yellow-50',
    borderColor: 'border-yellow-200',
    icon: 'AlertTriangle',
    label: 'Yellow Flag',
    description: 'Caution - review recommended',
    actions: ['acknowledge', 'resolve'],
  },
  green: {
    color: 'success',
    bgColor: 'bg-green-50',
    borderColor: 'border-green-200',
    icon: 'CheckCircle',
    label: 'Pass',
    description: 'Meets guideline requirements',
    actions: [],
  },
};
```

---

### 3.3 P7-04: Exception Request

#### 3.3.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Request and track exceptions for red flags |
| **User Roles** | Loan Officer, Processor |
| **Entry Points** | Flag manager, Analysis dashboard |
| **PRD Reference** | Phase 7 PRD, Section 5 |

#### 3.3.2 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `card` | Exception cards |
| `badge` | Status badges |
| `form` | Exception request form |
| `textarea` | Justification, compensating factors |
| `select` | Exception type |
| `button` | Submit, Approve, Deny |
| `table` | Exception history |

**React Custom Components:**

```typescript
// components/exceptions/ExceptionRequestForm.tsx
interface ExceptionRequestFormProps {
  flag: Flag;
  onSubmit: (request: ExceptionRequest) => void;
  onCancel: () => void;
}

// Exception request form
// Composition: Uses ShadCN Form, Select, Textarea
```

```typescript
// components/exceptions/ExceptionCard.tsx
interface ExceptionCardProps {
  exception: Exception;
  onApprove?: () => void;
  onDeny?: () => void;
  onEscalate?: () => void;
}

// Exception status card
// Composition: Uses ShadCN Card, Badge, Button
```

```typescript
// components/exceptions/CompensatingFactorsInput.tsx
interface CompensatingFactorsInputProps {
  factors: CompensatingFactor[];
  onChange: (factors: CompensatingFactor[]) => void;
}

// Multi-select for compensating factors
// Composition: Uses ShadCN Checkbox, Input
```

#### 3.3.3 Data Requirements

```typescript
interface Exception {
  id: string;
  dealId: string;
  flagId: string;
  
  // Request details
  exceptionType: ExceptionType;
  justification: string;
  compensatingFactors: CompensatingFactor[];
  
  // Status
  status: ExceptionStatus;
  
  // Approval chain
  requestedBy: string;
  requestedAt: Date;
  reviewedBy?: string;
  reviewedAt?: Date;
  approvedBy?: string;
  approvedAt?: Date;
  
  // Decision
  decision?: 'approved' | 'denied';
  decisionNotes?: string;
  conditions?: string[];
  
  // Investor approval (if required)
  requiresInvestorApproval: boolean;
  investorApprovalStatus?: 'pending' | 'approved' | 'denied';
  investorApprovalDate?: Date;
  investorNotes?: string;
}

type ExceptionType = 
  | 'credit_fico'
  | 'credit_events'
  | 'experience'
  | 'property_type'
  | 'ltv_ltc'
  | 'dscr'
  | 'valuation'
  | 'title'
  | 'other';

interface CompensatingFactor {
  type: string;
  description: string;
  value?: string | number;
}

const COMMON_COMPENSATING_FACTORS: CompensatingFactor[] = [
  { type: 'cash_reserves', description: 'Strong cash reserves' },
  { type: 'experience', description: 'Extensive track record' },
  { type: 'low_ltv', description: 'Conservative LTV' },
  { type: 'strong_dscr', description: 'High DSCR' },
  { type: 'cross_collateral', description: 'Cross-collateralized' },
  { type: 'personal_guarantee', description: 'Personal guarantee' },
  { type: 'additional_collateral', description: 'Additional collateral' },
  { type: 'rate_buydown', description: 'Rate buydown/pricing adjustment' },
  { type: 'repeat_borrower', description: 'Repeat borrower with good history' },
];
```

#### 3.3.4 Mock Data

```json
{
  "id": "exc_001",
  "dealId": "deal_abc123",
  "flagId": "flag_001",
  "exceptionType": "credit_fico",
  "justification": "Borrower's FICO dropped due to high utilization during recent acquisition. Has since paid down and score is recovering. Strong track record with 8 successful projects.",
  "compensatingFactors": [
    {
      "type": "experience",
      "description": "8 completed projects in past 36 months"
    },
    {
      "type": "cash_reserves",
      "description": "$450,000 verified liquid reserves"
    },
    {
      "type": "low_ltv",
      "description": "LTV of 65% vs max 75%"
    }
  ],
  "status": "pending",
  "requestedBy": "user_lo_001",
  "requestedAt": "2024-12-15T15:00:00Z",
  "requiresInvestorApproval": true,
  "investorApprovalStatus": "pending"
}
```

---

### 3.4 P7-05: Credit Memo

#### 3.4.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | AI-generated credit memo with all underwriting findings |
| **User Roles** | Underwriter, Loan Officer |
| **Entry Points** | Deal detail, Analysis dashboard |
| **PRD Reference** | Phase 7 PRD, Section 6 |

#### 3.4.2 Credit Memo Structure (from PRD)

```typescript
interface CreditMemo {
  id: string;
  dealId: string;
  version: number;
  
  // Status
  status: 'draft' | 'review' | 'approved' | 'submitted';
  
  // Generation info
  generatedAt: Date;
  generatedBy: 'ai' | 'manual';
  lastEditedAt?: Date;
  lastEditedBy?: string;
  
  // Sections (from PRD Section 6.2)
  sections: {
    executiveSummary: ExecutiveSummary;
    dealOverview: DealOverview;
    borrowerAnalysis: BorrowerAnalysis;
    propertyAnalysis: PropertyAnalysis;
    valuationAnalysis: ValuationAnalysis;
    financialAnalysis: FinancialAnalysis;
    riskAssessment: RiskAssessment;
    recommendation: Recommendation;
  };
  
  // Flags summary
  flagsSummary: {
    red: Flag[];
    yellow: Flag[];
    green: number;
  };
  
  // Exceptions
  exceptions: Exception[];
  
  // Approval
  approvedBy?: string;
  approvedAt?: Date;
  approvalNotes?: string;
}

interface ExecutiveSummary {
  loanAmount: number;
  loanType: string;
  purpose: string;
  propertyAddress: string;
  borrowerName: string;
  keyMetrics: {
    ltv?: number;
    ltc?: number;
    dscr?: number;
    fico: number;
    experience: number;
  };
  recommendation: 'approve' | 'approve_with_conditions' | 'decline';
  conditions?: string[];
  keyStrengths: string[];
  keyRisks: string[];
}

interface BorrowerAnalysis {
  entityInfo: {
    name: string;
    type: string;
    state: string;
    formation: string;
  };
  guarantors: {
    name: string;
    ownership: number;
    fico: number;
    netWorth?: number;
    liquidity?: number;
  }[];
  experience: {
    totalProjects: number;
    projectsLast36Months: number;
    similarProjects: number;
    defaultHistory: boolean;
  };
  creditAnalysis: {
    middleFico: number;
    derogatory: string[];
    bankruptcies: string[];
    foreclosures: string[];
  };
  backgroundAnalysis: {
    criminal: boolean;
    litigation: boolean;
    judgments: boolean;
    ofac: boolean;
  };
}

interface PropertyAnalysis {
  address: string;
  propertyType: string;
  units?: number;
  squareFeet: number;
  yearBuilt: number;
  condition: string;
  marketAnalysis: string;
  comparables?: string;
}

interface ValuationAnalysis {
  asIsValue: number;
  arv?: number;
  appraisalDate: Date;
  appraiser: string;
  appraisalType: string;
  comparableAnalysis: string;
  valueConclusion: string;
  feasibilityComparison?: {
    feasibilityARV: number;
    appraisalARV: number;
    variance: number;
    explanation: string;
  };
}

interface FinancialAnalysis {
  // RTL
  acquisitionCost?: number;
  rehabBudget?: number;
  totalCost?: number;
  ltc?: number;
  arv?: number;
  ltv?: number;
  
  // DSCR
  grossRent?: number;
  expenses?: number;
  noi?: number;
  dscr?: number;
  
  // Reserves
  cashReserves: number;
  reserveRequirement: number;
  reservesMet: boolean;
}

interface RiskAssessment {
  overallRisk: 'low' | 'moderate' | 'high';
  riskScore: number;
  
  riskFactors: {
    category: string;
    risk: 'low' | 'moderate' | 'high';
    description: string;
    mitigant?: string;
  }[];
  
  strengths: string[];
  weaknesses: string[];
  mitigants: string[];
}

interface Recommendation {
  decision: 'approve' | 'approve_with_conditions' | 'decline';
  conditions?: string[];
  pricing: {
    rate: number;
    originationFee: number;
    term: number;
  };
  specialConditions?: string[];
  underwriterNotes?: string;
}
```

#### 3.4.3 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `card` | Section cards |
| `badge` | Risk badges, status |
| `table` | Data tables |
| `separator` | Section dividers |
| `button` | Edit, Approve, Export |
| `tabs` | Memo sections |
| `alert` | Exceptions, warnings |

**React Custom Components:**

```typescript
// components/credit-memo/CreditMemoViewer.tsx
interface CreditMemoViewerProps {
  memo: CreditMemo;
  onEdit: () => void;
  onApprove: () => void;
  onExport: (format: 'pdf' | 'docx') => void;
  onRegenerate: () => void;
}

// Credit memo viewer
// Composition: Uses ShadCN Card, Tabs, Table
```

```typescript
// components/credit-memo/ExecutiveSummarySection.tsx
interface ExecutiveSummarySectionProps {
  summary: ExecutiveSummary;
  flags: Flag[];
}

// Executive summary section
// Composition: Uses ShadCN Card, Badge, Table
```

```typescript
// components/credit-memo/BorrowerAnalysisSection.tsx
interface BorrowerAnalysisSectionProps {
  analysis: BorrowerAnalysis;
  flags: Flag[];
}

// Borrower analysis section
// Composition: Uses ShadCN Card, Table, Badge
```

```typescript
// components/credit-memo/RiskAssessmentSection.tsx
interface RiskAssessmentSectionProps {
  assessment: RiskAssessment;
}

// Risk assessment visualization
// Composition: Uses ShadCN Card, Progress, Badge
```

```typescript
// components/credit-memo/RecommendationSection.tsx
interface RecommendationSectionProps {
  recommendation: Recommendation;
  exceptions: Exception[];
}

// Recommendation with conditions
// Composition: Uses ShadCN Card, Alert, Badge
```

```typescript
// components/credit-memo/CreditMemoExport.tsx
interface CreditMemoExportProps {
  memo: CreditMemo;
  format: 'pdf' | 'docx';
}

// Export functionality
```

#### 3.4.4 Mock Credit Memo

```json
{
  "id": "memo_001",
  "dealId": "deal_abc123",
  "version": 1,
  "status": "review",
  "generatedAt": "2024-12-15T16:00:00Z",
  "generatedBy": "ai",
  "sections": {
    "executiveSummary": {
      "loanAmount": 382500,
      "loanType": "Fix & Flip",
      "purpose": "Purchase + Rehab",
      "propertyAddress": "123 Main Street, Austin, TX 78701",
      "borrowerName": "ABC Investments LLC",
      "keyMetrics": {
        "ltc": 75,
        "ltv": 65,
        "fico": 680,
        "experience": 8
      },
      "recommendation": "approve_with_conditions",
      "conditions": [
        "FICO exception approved with 10bps rate adjustment",
        "Verify rehab budget with contractor bids"
      ],
      "keyStrengths": [
        "Experienced borrower with 8 completed projects",
        "Strong cash reserves ($450K liquid)",
        "Conservative LTV at 65%",
        "Repeat borrower with clean payment history"
      ],
      "keyRisks": [
        "FICO 680 below 700 minimum",
        "ARV variance of 8% between appraisal and feasibility"
      ]
    },
    "borrowerAnalysis": {
      "entityInfo": {
        "name": "ABC Investments LLC",
        "type": "LLC",
        "state": "Texas",
        "formation": "2018"
      },
      "guarantors": [
        {
          "name": "John Smith",
          "ownership": 100,
          "fico": 680,
          "netWorth": 1250000,
          "liquidity": 450000
        }
      ],
      "experience": {
        "totalProjects": 12,
        "projectsLast36Months": 8,
        "similarProjects": 6,
        "defaultHistory": false
      },
      "creditAnalysis": {
        "middleFico": 680,
        "derogatory": [],
        "bankruptcies": [],
        "foreclosures": []
      },
      "backgroundAnalysis": {
        "criminal": false,
        "litigation": false,
        "judgments": false,
        "ofac": false
      }
    },
    "propertyAnalysis": {
      "address": "123 Main Street, Austin, TX 78701",
      "propertyType": "SFR",
      "squareFeet": 1850,
      "yearBuilt": 1985,
      "condition": "Fair - needs cosmetic rehab",
      "marketAnalysis": "Austin market remains strong with 5% YoY appreciation. Subject neighborhood has seen 8% appreciation. Strong rental demand."
    },
    "valuationAnalysis": {
      "asIsValue": 425000,
      "arv": 585000,
      "appraisalDate": "2024-12-15",
      "appraiser": "ABC Appraisals",
      "appraisalType": "Full Interior",
      "comparableAnalysis": "Three comparable sales within 0.5 miles, all within 6 months. Adjustments reasonable.",
      "valueConclusion": "ARV supported by comparables. 8% variance from feasibility study due to different comp selection.",
      "feasibilityComparison": {
        "feasibilityARV": 540000,
        "appraisalARV": 585000,
        "variance": 8,
        "explanation": "Appraisal used more recent sales showing market appreciation"
      }
    },
    "financialAnalysis": {
      "acquisitionCost": 400000,
      "rehabBudget": 110000,
      "totalCost": 510000,
      "ltc": 75,
      "arv": 585000,
      "ltv": 65,
      "cashReserves": 450000,
      "reserveRequirement": 38250,
      "reservesMet": true
    },
    "riskAssessment": {
      "overallRisk": "moderate",
      "riskScore": 35,
      "riskFactors": [
        {
          "category": "Credit",
          "risk": "moderate",
          "description": "FICO 680 below 700 minimum",
          "mitigant": "Strong experience and reserves"
        },
        {
          "category": "Valuation",
          "risk": "moderate",
          "description": "8% ARV variance",
          "mitigant": "Conservative LTV provides cushion"
        },
        {
          "category": "Experience",
          "risk": "low",
          "description": "8 projects completed",
          "mitigant": "N/A"
        },
        {
          "category": "Market",
          "risk": "low",
          "description": "Strong Austin market",
          "mitigant": "N/A"
        }
      ],
      "strengths": [
        "Experienced operator with proven track record",
        "Strong liquidity position",
        "Conservative leverage",
        "Strong market fundamentals"
      ],
      "weaknesses": [
        "Below-minimum FICO score",
        "ARV variance requires monitoring"
      ],
      "mitigants": [
        "10bps rate adjustment for FICO exception",
        "Conservative LTV provides valuation cushion",
        "Draw inspection to verify rehab progress"
      ]
    },
    "recommendation": {
      "decision": "approve_with_conditions",
      "conditions": [
        "FICO exception approved with 10bps rate adjustment",
        "Verify contractor bids for rehab budget",
        "Standard draw inspection schedule"
      ],
      "pricing": {
        "rate": 11.5,
        "originationFee": 2.0,
        "term": 12
      },
      "underwriterNotes": "Strong borrower profile mitigates FICO concern. ARV variance within acceptable range given conservative LTV."
    }
  },
  "flagsSummary": {
    "red": [
      {
        "id": "flag_001",
        "title": "FICO Below Minimum",
        "severity": "red"
      },
      {
        "id": "flag_002",
        "title": "ARV Variance High",
        "severity": "red"
      }
    ],
    "yellow": [
      {
        "id": "flag_003",
        "title": "Limited Track Record",
        "severity": "yellow"
      }
    ],
    "green": 28
  },
  "exceptions": [
    {
      "id": "exc_001",
      "flagId": "flag_001",
      "status": "approved",
      "decision": "approved",
      "conditions": ["10bps rate adjustment"]
    }
  ]
}
```

---

## 4. AI Analysis Pipeline

### 4.1 Document Analysis Rules

```typescript
const DOCUMENT_ANALYSIS_RULES: Record<string, DocumentAnalysisRule[]> = {
  credit_report: [
    {
      id: 'fico_minimum',
      name: 'FICO Minimum Check',
      check: (data, guidelines) => {
        const middleFico = data.creditScores.middle;
        const minimum = guidelines.fico.minimum;
        return {
          pass: middleFico >= minimum,
          severity: middleFico >= minimum ? 'green' : 'red',
          actualValue: middleFico,
          expectedValue: minimum,
          message: `Middle FICO ${middleFico} ${middleFico >= minimum ? 'meets' : 'below'} minimum ${minimum}`,
        };
      },
    },
    {
      id: 'bankruptcy_check',
      name: 'Bankruptcy History',
      check: (data, guidelines) => {
        const bankruptcies = data.bankruptcies || [];
        const seasoning = guidelines.bankruptcy.seasoning;
        const recentBankruptcy = bankruptcies.find(b => 
          monthsSince(b.dischargeDate) < seasoning
        );
        return {
          pass: !recentBankruptcy,
          severity: recentBankruptcy ? 'red' : 'green',
          message: recentBankruptcy 
            ? `Bankruptcy discharged ${monthsSince(recentBankruptcy.dischargeDate)} months ago, requires ${seasoning} months seasoning`
            : 'No recent bankruptcies',
        };
      },
    },
    {
      id: 'foreclosure_check',
      name: 'Foreclosure History',
      check: (data, guidelines) => {
        const foreclosures = data.foreclosures || [];
        const seasoning = guidelines.foreclosure.seasoning;
        const recentForeclosure = foreclosures.find(f =>
          monthsSince(f.date) < seasoning
        );
        return {
          pass: !recentForeclosure,
          severity: recentForeclosure ? 'red' : 'green',
          message: recentForeclosure
            ? `Foreclosure ${monthsSince(recentForeclosure.date)} months ago, requires ${seasoning} months seasoning`
            : 'No recent foreclosures',
        };
      },
    },
  ],
  
  background_check: [
    {
      id: 'criminal_check',
      name: 'Criminal History',
      check: (data) => {
        const hasCriminal = data.criminalRecords?.length > 0;
        return {
          pass: !hasCriminal,
          severity: hasCriminal ? 'red' : 'green',
          message: hasCriminal ? 'Criminal records found' : 'No criminal records',
        };
      },
    },
    {
      id: 'ofac_check',
      name: 'OFAC Check',
      check: (data) => {
        const hasOFAC = data.ofacHit;
        return {
          pass: !hasOFAC,
          severity: hasOFAC ? 'red' : 'green',
          message: hasOFAC ? 'OFAC hit found' : 'Clear OFAC check',
        };
      },
    },
    {
      id: 'litigation_check',
      name: 'Litigation Check',
      check: (data) => {
        const activeLitigation = data.litigation?.filter(l => l.status === 'active');
        return {
          pass: activeLitigation?.length === 0,
          severity: activeLitigation?.length > 0 ? 'yellow' : 'green',
          message: activeLitigation?.length > 0 
            ? `${activeLitigation.length} active litigation matters`
            : 'No active litigation',
        };
      },
    },
  ],
  
  appraisal: [
    {
      id: 'value_reasonableness',
      name: 'Value Reasonableness',
      check: (data, guidelines, dealData) => {
        const appraisalValue = data.asIsValue;
        const purchasePrice = dealData.purchasePrice;
        const ratio = appraisalValue / purchasePrice;
        return {
          pass: ratio >= 0.9 && ratio <= 1.2,
          severity: ratio < 0.9 || ratio > 1.2 ? 'yellow' : 'green',
          actualValue: `${(ratio * 100).toFixed(0)}%`,
          message: `Appraisal ${ratio >= 1 ? 'above' : 'below'} purchase price by ${Math.abs((ratio - 1) * 100).toFixed(0)}%`,
        };
      },
    },
    {
      id: 'arv_variance',
      name: 'ARV Variance Check',
      check: (data, guidelines, dealData) => {
        if (!dealData.feasibilityARV) return { pass: true, severity: 'green', message: 'No feasibility to compare' };
        const variance = Math.abs(data.arv - dealData.feasibilityARV) / dealData.feasibilityARV;
        const threshold = guidelines.arv.varianceThreshold || 0.05;
        return {
          pass: variance <= threshold,
          severity: variance > threshold ? 'red' : 'green',
          actualValue: `${(variance * 100).toFixed(1)}%`,
          threshold: `${(threshold * 100).toFixed(0)}%`,
          message: `ARV variance ${(variance * 100).toFixed(1)}% ${variance <= threshold ? 'within' : 'exceeds'} ${(threshold * 100).toFixed(0)}% threshold`,
        };
      },
    },
    {
      id: 'comparable_age',
      name: 'Comparable Age Check',
      check: (data, guidelines) => {
        const maxAge = guidelines.appraisal?.comparableAge || 6;
        const oldComps = data.comparables?.filter(c => monthsSince(c.saleDate) > maxAge);
        return {
          pass: oldComps?.length === 0,
          severity: oldComps?.length > 0 ? 'yellow' : 'green',
          message: oldComps?.length > 0
            ? `${oldComps.length} comparables older than ${maxAge} months`
            : 'All comparables within acceptable age',
        };
      },
    },
  ],
  
  title_commitment: [
    {
      id: 'liens_check',
      name: 'Liens Check',
      check: (data) => {
        const liens = data.liens?.filter(l => l.type !== 'mortgage');
        return {
          pass: liens?.length === 0,
          severity: liens?.length > 0 ? 'red' : 'green',
          message: liens?.length > 0
            ? `${liens.length} liens found: ${liens.map(l => l.type).join(', ')}`
            : 'No adverse liens',
        };
      },
    },
    {
      id: 'judgments_check',
      name: 'Judgments Check',
      check: (data) => {
        const judgments = data.judgments || [];
        return {
          pass: judgments.length === 0,
          severity: judgments.length > 0 ? 'red' : 'green',
          message: judgments.length > 0
            ? `${judgments.length} judgments found`
            : 'No judgments',
        };
      },
    },
    {
      id: 'vesting_check',
      name: 'Vesting Check',
      check: (data, guidelines, dealData) => {
        const titleVesting = data.vesting;
        const borrowerEntity = dealData.borrowerEntity;
        const match = titleVesting.toLowerCase().includes(borrowerEntity.toLowerCase());
        return {
          pass: match,
          severity: match ? 'green' : 'yellow',
          message: match
            ? 'Title vesting matches borrower entity'
            : 'Title vesting does not match borrower - verify assignment',
        };
      },
    },
  ],
  
  insurance_certificate: [
    {
      id: 'coverage_amount',
      name: 'Coverage Amount Check',
      check: (data, guidelines, dealData) => {
        const coverage = data.coverageAmount;
        const required = Math.max(dealData.loanAmount, dealData.replacementCost);
        return {
          pass: coverage >= required,
          severity: coverage >= required ? 'green' : 'red',
          actualValue: coverage,
          expectedValue: required,
          message: `Coverage $${coverage.toLocaleString()} ${coverage >= required ? 'meets' : 'below'} required $${required.toLocaleString()}`,
        };
      },
    },
    {
      id: 'mortgagee_clause',
      name: 'Mortgagee Clause Check',
      check: (data) => {
        const hasMortgagee = data.mortgageeClause?.includes('USDV Capital');
        return {
          pass: hasMortgagee,
          severity: hasMortgagee ? 'green' : 'red',
          message: hasMortgagee
            ? 'Correct mortgagee clause'
            : 'Missing or incorrect mortgagee clause',
        };
      },
    },
    {
      id: 'policy_expiration',
      name: 'Policy Expiration Check',
      check: (data, guidelines, dealData) => {
        const expiration = new Date(data.expirationDate);
        const loanMaturity = new Date(dealData.maturityDate);
        const coversLoan = expiration >= loanMaturity;
        return {
          pass: coversLoan,
          severity: coversLoan ? 'green' : 'yellow',
          message: coversLoan
            ? 'Policy covers loan term'
            : 'Policy expires before loan maturity',
        };
      },
    },
  ],
  
  lease: [
    {
      id: 'lease_term',
      name: 'Lease Term Check',
      check: (data, guidelines) => {
        const remainingMonths = monthsUntil(data.expirationDate);
        const minimum = guidelines.lease?.minimumRemaining || 6;
        return {
          pass: remainingMonths >= minimum,
          severity: remainingMonths >= minimum ? 'green' : 'yellow',
          actualValue: remainingMonths,
          expectedValue: minimum,
          message: `${remainingMonths} months remaining ${remainingMonths >= minimum ? 'meets' : 'below'} ${minimum} month minimum`,
        };
      },
    },
    {
      id: 'rent_verification',
      name: 'Rent Verification',
      check: (data, guidelines, dealData) => {
        const leaseRent = data.monthlyRent;
        const applicationRent = dealData.statedRent;
        const match = Math.abs(leaseRent - applicationRent) / applicationRent < 0.05;
        return {
          pass: match,
          severity: match ? 'green' : 'yellow',
          actualValue: leaseRent,
          expectedValue: applicationRent,
          message: match
            ? 'Lease rent matches application'
            : `Lease rent $${leaseRent} differs from stated $${applicationRent}`,
        };
      },
    },
  ],
  
  bank_statement: [
    {
      id: 'reserves_verification',
      name: 'Reserves Verification',
      check: (data, guidelines, dealData) => {
        const balance = data.endingBalance;
        const required = dealData.reserveRequirement;
        return {
          pass: balance >= required,
          severity: balance >= required ? 'green' : 'red',
          actualValue: balance,
          expectedValue: required,
          message: `Available balance $${balance.toLocaleString()} ${balance >= required ? 'meets' : 'below'} required $${required.toLocaleString()}`,
        };
      },
    },
    {
      id: 'large_deposits',
      name: 'Large Deposit Check',
      check: (data, guidelines) => {
        const threshold = guidelines.bankStatement?.largeDepositThreshold || 10000;
        const largeDeposits = data.deposits?.filter(d => d.amount > threshold);
        return {
          pass: true, // Always passes but flags for review
          severity: largeDeposits?.length > 0 ? 'yellow' : 'green',
          message: largeDeposits?.length > 0
            ? `${largeDeposits.length} deposits over $${threshold.toLocaleString()} - source verification recommended`
            : 'No large deposits requiring verification',
        };
      },
    },
  ],
};
```

### 4.2 Analysis Service

```typescript
interface AnalysisService {
  // Analyze single document
  analyzeDocument(
    document: Document,
    dealContext: DealContext,
    guidelines: InvestorGuidelines
  ): Promise<DocumentAnalysis>;
  
  // Analyze all documents for deal
  analyzeAllDocuments(dealId: string): Promise<AnalysisSummary>;
  
  // Generate flags from analysis
  generateFlags(analysis: DocumentAnalysis): Flag[];
  
  // Generate credit memo
  generateCreditMemo(dealId: string): Promise<CreditMemo>;
  
  // Identify exceptions
  identifyExceptions(flags: Flag[], guidelines: InvestorGuidelines): Exception[];
}

async function analyzeDocument(
  document: Document,
  dealContext: DealContext,
  guidelines: InvestorGuidelines
): Promise<DocumentAnalysis> {
  // 1. Extract text/data from document
  const extractedData = await extractDocumentData(document);
  
  // 2. Get applicable rules
  const rules = DOCUMENT_ANALYSIS_RULES[document.type] || [];
  
  // 3. Run each rule
  const results = rules.map(rule => ({
    ruleId: rule.id,
    ruleName: rule.name,
    ...rule.check(extractedData, guidelines, dealContext),
  }));
  
  // 4. Generate flags from results
  const flags = results
    .filter(r => r.severity !== 'green' || r.noteworthy)
    .map(r => createFlag(r, document, dealContext));
  
  // 5. Generate summary using LLM
  const summary = await generateDocumentSummary(document, extractedData, results);
  
  return {
    id: generateId(),
    dealId: dealContext.dealId,
    documentId: document.id,
    documentType: document.type,
    documentName: document.name,
    status: 'complete',
    analyzedAt: new Date(),
    flags,
    extractedData,
    summary,
    confidence: calculateConfidence(results),
    needsManualReview: flags.some(f => f.severity === 'red'),
  };
}
```

### 4.3 Credit Memo Generation Prompt

```typescript
const CREDIT_MEMO_PROMPT = `
Generate a professional credit memo for this real estate loan.

DEAL INFORMATION:
{dealData}

BORROWER ANALYSIS:
{borrowerData}

PROPERTY ANALYSIS:
{propertyData}

VALUATION ANALYSIS:
{valuationData}

ALL FLAGS:
{flags}

EXCEPTIONS:
{exceptions}

INVESTOR GUIDELINES:
{guidelinesReference}

Generate a comprehensive credit memo following this structure:

1. EXECUTIVE SUMMARY
- Loan amount, type, purpose
- Key metrics (LTV/LTC, DSCR if applicable, FICO, experience)
- Recommendation (Approve / Approve with Conditions / Decline)
- Key strengths (3-5 bullet points)
- Key risks (2-4 bullet points)

2. BORROWER ANALYSIS
- Entity information
- Guarantor profile(s)
- Experience summary
- Credit analysis findings
- Background check findings

3. PROPERTY ANALYSIS
- Property description
- Market analysis
- Condition assessment

4. VALUATION ANALYSIS
- As-is value and ARV (if applicable)
- Comparable analysis
- Feasibility comparison (if applicable)
- Value conclusion

5. FINANCIAL ANALYSIS
- Acquisition cost breakdown
- Rehab budget (if applicable)
- LTV/LTC calculations
- DSCR calculation (if applicable)
- Reserve verification

6. RISK ASSESSMENT
- Overall risk rating (Low/Moderate/High)
- Risk factors by category
- Mitigating factors

7. RECOMMENDATION
- Final recommendation
- Conditions (if any)
- Pricing summary
- Special conditions

Be specific, cite actual values, and reference flags/exceptions where relevant.
Write in professional underwriting language.
`;
```

---

## 5. API Contract (Mock)

### 5.1 Analysis Endpoints

```typescript
// GET /api/deals/:id/analysis
// Get analysis summary
interface GetAnalysisResponse {
  summary: AnalysisSummary;
  documentAnalyses: DocumentAnalysis[];
}

// POST /api/deals/:id/analysis/run
// Trigger full analysis
interface RunAnalysisResponse {
  jobId: string;
  status: 'queued' | 'running';
  estimatedCompletion: Date;
}

// GET /api/deals/:id/analysis/status
// Check analysis status
interface AnalysisStatusResponse {
  status: 'pending' | 'running' | 'complete' | 'error';
  progress: {
    documentsAnalyzed: number;
    documentsTotal: number;
  };
  currentDocument?: string;
}

// POST /api/documents/:id/analyze
// Analyze single document
interface AnalyzeDocumentResponse {
  analysis: DocumentAnalysis;
}
```

### 5.2 Flag Endpoints

```typescript
// GET /api/deals/:id/flags
// Get all flags
interface GetFlagsResponse {
  flags: Flag[];
  summary: {
    red: number;
    yellow: number;
    green: number;
  };
}

// POST /api/flags/:id/resolve
// Resolve a flag
interface ResolveFlagRequest {
  resolution: string;
}

interface ResolveFlagResponse {
  flag: Flag;
}

// POST /api/flags/:id/exception
// Request exception
interface RequestExceptionRequest {
  exceptionType: ExceptionType;
  justification: string;
  compensatingFactors: CompensatingFactor[];
}

interface RequestExceptionResponse {
  exception: Exception;
}
```

### 5.3 Exception Endpoints

```typescript
// GET /api/deals/:id/exceptions
// Get all exceptions
interface GetExceptionsResponse {
  exceptions: Exception[];
}

// POST /api/exceptions/:id/approve
// Approve exception
interface ApproveExceptionRequest {
  notes?: string;
  conditions?: string[];
}

interface ApproveExceptionResponse {
  exception: Exception;
}

// POST /api/exceptions/:id/deny
// Deny exception
interface DenyExceptionRequest {
  reason: string;
}

interface DenyExceptionResponse {
  exception: Exception;
}

// POST /api/exceptions/:id/escalate
// Escalate to investor
interface EscalateExceptionResponse {
  exception: Exception;
  escalationId: string;
}
```

### 5.4 Credit Memo Endpoints

```typescript
// GET /api/deals/:id/credit-memo
// Get credit memo
interface GetCreditMemoResponse {
  memo: CreditMemo;
}

// POST /api/deals/:id/credit-memo/generate
// Generate credit memo
interface GenerateCreditMemoResponse {
  jobId: string;
  status: 'queued' | 'generating';
}

// PUT /api/credit-memos/:id
// Update credit memo
interface UpdateCreditMemoRequest {
  sections: Partial<CreditMemo['sections']>;
}

interface UpdateCreditMemoResponse {
  memo: CreditMemo;
}

// POST /api/credit-memos/:id/approve
// Approve credit memo
interface ApproveCreditMemoRequest {
  notes?: string;
}

interface ApproveCreditMemoResponse {
  memo: CreditMemo;
}

// GET /api/credit-memos/:id/export
// Export credit memo
interface ExportCreditMemoRequest {
  format: 'pdf' | 'docx';
}

// Returns file download
```

---

## 6. Background Jobs

| Job | Frequency | Purpose |
|-----|-----------|---------|
| `analyze-new-documents` | On document upload | Trigger analysis for new docs |
| `regenerate-credit-memo` | On analysis complete | Update credit memo |
| `check-exception-status` | Every 4 hours | Check investor responses |
| `flag-aging-report` | Daily | Report on unresolved flags |

---

## 7. Open Questions & Assumptions

### 7.1 Open Questions

| # | Question | Impact | Owner |
|---|----------|--------|-------|
| 1 | Which LLM model for analysis (Claude/GPT)? | Accuracy, cost | Engineering |
| 2 | Exception approval workflow - who approves? | Business logic | Product |
| 3 | Credit memo template customization by investor? | Flexibility | Product |
| 4 | Flag severity thresholds - configurable? | Business rules | Product |

### 7.2 Assumptions Made

| # | Assumption | Rationale |
|---|------------|-----------|
| 1 | Claude 3.5 Sonnet for document analysis | Best accuracy for financial docs |
| 2 | Flags auto-generated, exceptions manual | PRD implies this flow |
| 3 | Credit memo is editable after generation | Standard workflow |
| 4 | Exception approval is internal first, then investor | Two-stage approval |

---

## 8. Implementation Checklist

### 8.1 Analysis Pipeline

- [ ] Document text extraction (OCR)
- [ ] Analysis rules engine
- [ ] Credit report analysis
- [ ] Background check analysis
- [ ] Appraisal analysis
- [ ] Title analysis
- [ ] Insurance analysis
- [ ] Lease analysis
- [ ] Bank statement analysis
- [ ] Entity document analysis
- [ ] Analysis summary aggregation
- [ ] Real-time analysis on upload

### 8.2 Flag System

- [ ] Flag generation from analysis
- [ ] Flag display components
- [ ] Flag filtering and sorting
- [ ] Flag resolution workflow
- [ ] Flag severity configuration
- [ ] Flag-to-exception linking

### 8.3 Exception Management

- [ ] Exception request form
- [ ] Compensating factors selection
- [ ] Exception approval workflow
- [ ] Investor escalation
- [ ] Exception tracking
- [ ] Exception history

### 8.4 Credit Memo

- [ ] Credit memo generation (LLM)
- [ ] Credit memo viewer
- [ ] Credit memo editor
- [ ] Section-by-section editing
- [ ] Credit memo approval
- [ ] PDF export
- [ ] DOCX export
- [ ] Version history

### 8.5 Testing

- [ ] Unit tests: Analysis rules
- [ ] Unit tests: Flag generation
- [ ] Integration tests: Full analysis pipeline
- [ ] Integration tests: Credit memo generation
- [ ] E2E tests: Document to memo flow
- [ ] Accuracy tests: Compare AI vs manual analysis

---

## 9. UW Manual Integration

This section maps Phase 7 implementation components to the USDV Underwriting Manual sections. **Phase 7 is the most manual-intensive phase** - the AI analysis logic must precisely match the manual's flag rules, and the credit memo structure follows Section 15 exactly.

### 9.1 Manual Section Cross-References

| Implementation Component | UW Manual Section | Usage |
|--------------------------|-------------------|-------|
| **Credit Report Analysis** | | |
| FICO score extraction | Section 4.1: FICO Requirements | Score calculation rules |
| Qualifying score determination | Section 14.2.2: Score Calculation | Median/lower rules |
| Trade line analysis | Section 4.2: Trade Line Requirements | Minimum requirements |
| Mortgage history analysis | Section 4.3: Mortgage History | Late payment rules |
| Derogatory analysis | Section 4.4: Derogatory Events | BK, FC, SS, judgments |
| Credit flag generation | Section 14.2.4: Credit Report Flags | Green/Yellow/Red criteria |
| **Background Check Analysis** | | |
| Criminal history review | Section 4.5.1: Criminal History | Disqualifying events |
| Civil litigation review | Section 4.5.2: Civil Litigation | Active litigation rules |
| OFAC screening | Section 4.5.3: OFAC Check | Sanctions check |
| Lien/judgment analysis | Section 4.5.4: Liens & Judgments | Threshold amounts |
| Background flag generation | Section 14.3: Background Flags | Flag criteria |
| **Appraisal Analysis** | | |
| Value extraction | Section 8.2: Value Types | As-Is, ARV parsing |
| Report currency check | Section 8.3: Currency | 120-day rule |
| Appraiser validation | Section 8.4: Appraiser Requirements | License verification |
| Condition assessment | Section 8.5: Condition Ratings | C-rating validation |
| Comp analysis | Section 8.6: Comparable Analysis | Comp quality rules |
| Value variance handling | Section 8.7: Variance | Resizing triggers |
| Appraisal flag generation | Section 14.4: Appraisal Flags | Flag criteria |
| **Title Analysis** | | |
| Schedule B-I review | Section 14.4.2: Schedule B-I | Requirements check |
| Schedule B-II review | Section 14.4.3: Schedule B-II | Exception analysis |
| Lien identification | Section 14.4.4: Liens | Payoff requirements |
| Easement/encroachment | Section 14.4.5: Easements | Acceptable exceptions |
| Title flag generation | Section 14.4.6: Title Flags | Flag criteria |
| **Insurance Analysis** | | |
| Coverage validation | Section 14.5.1: Coverage | Minimum amounts |
| Mortgagee clause check | Section 14.5.2: Mortgagee | Correct clause |
| Policy currency | Section 14.5.3: Currency | Effective dates |
| Flood determination | Section 14.5.4: Flood | Zone requirements |
| Insurance flag generation | Section 14.5.5: Insurance Flags | Flag criteria |
| **Exception Management** | | |
| Exception type identification | Section 12.1: Exception Types | Category assignment |
| Compensating factors | Section 12.2: Compensating Factors | Mitigant identification |
| Approval authority | Section 12.3: Approval Authority | Routing rules |
| Exception documentation | Section 12.4: Documentation | Required justification |
| **Credit Memo** | | |
| Memo structure | Section 15.2: Memo Structure | 6-page format |
| Executive summary | Section 15.3: Executive Summary | Deal snapshot |
| Borrower analysis | Section 15.4: Borrower Analysis | Credit/experience narrative |
| Property analysis | Section 15.5: Property Analysis | Property/market narrative |
| Deal economics | Section 15.6: Deal Economics | Sources & uses, metrics |
| Third-party summary | Section 15.7: Third-Party Summary | Report findings |
| Risk assessment | Section 15.8: Risk Assessment | Rating framework |
| Recommendation | Section 15.9: Recommendation | Approve/Decline logic |
| **Risk Rating** | | |
| Risk score calculation | Section 15.8.2: Risk Score | Weighted calculation |
| Low risk criteria | Section 15.8.3: Risk Levels | Green threshold |
| Moderate risk criteria | Section 15.8.3: Risk Levels | Yellow threshold |
| Elevated risk criteria | Section 15.8.3: Risk Levels | Orange threshold |
| High risk criteria | Section 15.8.3: Risk Levels | Red threshold |

### 9.2 Flag Generation Rules from Manual

**Critical:** These flag rules come directly from Section 14 and must be implemented exactly.

**Credit Report Flags (Section 14.2.4):**

| Check | Green | Yellow | Red | Critical |
|-------|-------|--------|-----|----------|
| FICO Score | ≥ 720 | 680-719 | 660-679 | < 660 |
| Mortgage Lates (24 mo) | 0 | 1x30 day | 2x30 or 1x60 | 90+ days |
| Bankruptcy | > 4 years | 2-4 years | < 2 years | Active |
| Foreclosure | > 4 years | 2-4 years | < 2 years | Active |
| Open Collections | None | < $5,000 | $5,000-$25,000 | > $25,000 |
| Tax Liens | None | Paid > 12 mo | Payment plan | Unpaid |

**Background Check Flags (Section 14.3.4):**

| Check | Green | Yellow | Red | Critical |
|-------|-------|--------|-----|----------|
| Criminal History | None | Misdemeanor > 7 yr | Misdemeanor < 7 yr | Felony |
| Active Litigation | None | < $50K | $50K-$250K | > $250K |
| OFAC | Clear | - | - | Hit |
| Judgments | None | < $10K paid | $10K-$50K | > $50K unpaid |

**Appraisal Flags (Section 14.4.6):**

| Check | Green | Yellow | Red | Critical |
|-------|-------|--------|-----|----------|
| Currency | < 90 days | 90-120 days | > 120 days | > 180 days |
| Value vs Purchase | ≥ 100% | 95-100% | 90-95% | < 90% |
| ARV Variance | < 5% | 5-10% | 10-15% | > 15% |
| Condition Rating | C1-C3 | C4 | C5 | C6 |

### 9.3 Credit Memo Structure from Manual

Section 15.2 defines the exact credit memo structure:

```
CREDIT MEMO STRUCTURE (6 pages)
═══════════════════════════════

Page 1: EXECUTIVE SUMMARY (½ page)
├── Deal Snapshot (property, loan type, amount)
├── Key Metrics (LTV, DSCR, FICO, experience)
├── Recommendation (Approve/Conditions/Decline)
├── Key Strengths (3-5 bullets)
└── Key Risks (2-4 bullets)

Page 1-2: BORROWER ANALYSIS (1 page)
├── Entity Information
├── Guarantor Profile(s)
├── Experience Summary
├── Credit Analysis
└── Background Analysis

Page 2-3: PROPERTY ANALYSIS (1 page)
├── Property Description
├── Location & Market
├── Condition Assessment
└── Business Plan (RTL) / Rental Analysis (DSCR)

Page 3-4: DEAL ECONOMICS (1 page)
├── Sources & Uses
├── Leverage Metrics
├── Exit Strategy
└── Reserve Analysis

Page 4-5: THIRD-PARTY REPORTS (1 page)
├── Appraisal Summary
├── Title Summary
├── Insurance Summary
└── Other Reports

Page 5-6: RISK ASSESSMENT (1 page)
├── Risk Score & Rating
├── Risk Factors by Category
├── Mitigating Factors
└── Conditions & Exceptions

Page 6: RECOMMENDATION
├── Final Recommendation
├── Conditions (if any)
├── Pricing Summary
└── Underwriter Signature
```

### 9.4 Risk Rating Framework from Manual

Section 15.8 defines the risk rating calculation:

```typescript
// Risk Rating Calculation (Section 15.8.2)
interface RiskRating {
  score: number;        // 0-100
  rating: 'low' | 'moderate' | 'elevated' | 'high';
}

const RISK_WEIGHTS = {
  borrower: 0.30,       // Credit, experience, liquidity
  property: 0.25,       // Location, condition, type
  valuation: 0.20,      // Appraisal quality, variance
  deal_structure: 0.15, // Leverage, reserves
  third_party: 0.10,    // Title, insurance, other
};

const RISK_THRESHOLDS = {
  low: { max: 25, color: 'green' },
  moderate: { max: 50, color: 'yellow' },
  elevated: { max: 75, color: 'orange' },
  high: { max: 100, color: 'red' },
};
```

### 9.5 Exception Types from Manual

Section 12.1 defines exception categories:

| Exception Type | Description | Typical Compensating Factors |
|----------------|-------------|------------------------------|
| `credit_fico` | FICO below minimum | Strong experience, reserves, low LTV |
| `credit_events` | Recent BK/FC/SS | Time since event, explanation |
| `experience` | Insufficient track record | Partner with experience, reserves |
| `property_type` | Non-standard property | Strong location, conservative LTV |
| `ltv_ltc` | Exceeds leverage limits | Additional collateral, guarantees |
| `dscr` | Below minimum DSCR | Strong borrower, reserves |
| `valuation` | Appraisal concerns | Additional valuation, conservative LTV |
| `title` | Title exceptions | Title insurance, indemnification |
| `other` | Other guideline deviation | Case-by-case |

### 9.6 Python Library Integration

| Analysis Need | Python Class | Method |
|---------------|--------------|--------|
| Credit analysis | `CreditAnalyzer` | `analyze_credit_report()` |
| Background analysis | `BackgroundAnalyzer` | `analyze_background_check()` |
| Appraisal analysis | `AppraisalAnalyzer` | `analyze_appraisal()` |
| Title analysis | `TitleAnalyzer` | `analyze_title_commitment()` |
| Flag generation | `FlagGenerator` | `generate_flags()` |
| Risk rating | `RiskRatingCalculator` | `calculate_risk_score()` |
| Credit memo generation | `CreditMemoGenerator` | `generate_memo()` |
| Exception management | `ExceptionManager` | `create_exception()`, `get_compensating_factors()` |

### 9.7 AI Analysis Prompts

Include manual context in AI prompts:

```typescript
const ANALYSIS_SYSTEM_PROMPT = `
You are analyzing documents for a real estate loan underwriting system.

Reference the following standards from the USDV Underwriting Manual:
- Section 4: Credit & Background Evaluation
- Section 8: Appraisal & Valuation Review
- Section 14: Third-Party Report Analysis

Flag Severity Definitions:
- GREEN: Meets or exceeds all requirements
- YELLOW: Minor deviation, acceptable with documentation
- RED: Significant deviation, requires exception
- CRITICAL: Disqualifying, cannot proceed

Always cite the specific manual section when generating flags.
`;
```

---

*End of Phase 7 Implementation Plan*

