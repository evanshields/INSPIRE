# Phase 5-6 Implementation Plan: Third-Party Reports & Diligence Chase

**Document Version:** 1.0  
**PRD Reference:** INSPIRE Phase 5-6 PRD  
**Last Updated:** December 2024  
**Status:** Implementation Ready

---

## 1. Executive Summary

### 1.1 Phase Overview

Phase 5-6 automates document collection and third-party report ordering:
- **Phase 5: Third-Party Reports** - Automated ordering and ingestion of appraisals, title, credit, background, insurance, feasibility, flood
- **Phase 6: Diligence Chase** - Smart diligence lists, AI document classification, frictionless upload

### 1.2 Success Metrics (from PRD)

| Metric | Target |
|--------|--------|
| Third-party reports auto-ordered | >90% |
| Report ingestion automation rate | >95% |
| Document auto-classification accuracy | >95% |
| Time from deposit to reports ordered | <1 hour |
| Manual document filing | <5% of documents |
| Diligence request to complete package | <5 business days |

### 1.3 Key Dependencies

| Dependency | Status | Notes |
|------------|--------|-------|
| Phase 4 Complete | Required | Term sheet + deposit triggers Phase 5 |
| Single Source API | Required | Appraisal, title, flood, feasibility |
| CRS API | Required | Credit, background checks |
| Google Drive API | Required | Document storage |
| Gmail/IMAP | Required | Email ingestion |
| LLM API (Claude/GPT) | Required | Document classification |

---

## 2. Page/Screen Inventory

### 2.1 Complete Page List

| Page ID | Page Name | Route | User Role | Entry Point |
|---------|-----------|-------|-----------|-------------|
| P5-01 | Third-Party Reports Dashboard | `/deals/:id/reports` | Internal | Deal detail |
| P5-02 | Report Order Form | `/deals/:id/reports/order` | Internal | Reports dashboard |
| P5-03 | Report Detail View | `/deals/:id/reports/:reportId` | Internal | Reports dashboard |
| P6-01 | Diligence Checklist | `/deals/:id/diligence` | Internal | Deal detail |
| P6-02 | Document Upload (Borrower) | `/upload/:dealId/:token` | Public | Email link |
| P6-03 | Document Review Queue | `/deals/:id/documents/review` | Internal | Deal detail |
| P6-04 | Data Room Browser | `/deals/:id/data-room` | Internal | Deal detail |

### 2.2 Navigation Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PHASE 5-6 FLOWS                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  PHASE 5: THIRD-PARTY REPORTS                                                │
│  ────────────────────────────                                                │
│  Deposit Paid → Auto-Order Reports → Track Status → Receive via Webhook →   │
│  AI Analysis → File to Data Room → Update Checklist                          │
│                                                                              │
│  PHASE 6: DILIGENCE CHASE                                                    │
│  ────────────────────────                                                    │
│  Term Sheet Signed → Generate Checklist → Send Request Email →               │
│  Borrower Uploads (Drag-Drop/Email/WhatsApp) → AI Classify → File →          │
│  Send Reminders → Track Completion                                           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Per-Page Specifications

---

### 3.1 P5-01: Third-Party Reports Dashboard

#### 3.1.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Track and manage third-party report ordering and receipt |
| **User Roles** | Processor, Loan Officer, Underwriter |
| **Entry Points** | Deal detail tabs, Pipeline card |
| **PRD Reference** | Phase 5-6 PRD, Section 3.1-3.9 |

#### 3.1.2 Information Architecture

**Primary Data:** ThirdPartyReport[]

**Content Hierarchy:**
1. Deal header
2. Report status summary (ordered, received, pending)
3. Report cards by type
4. Order actions
5. Manual order fallback

#### 3.1.3 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `card` | Report cards |
| `badge` | Status badges (ordered, received, etc.) |
| `button` | Order, Track, View, Resend |
| `table` | Report list view |
| `progress` | Overall completion progress |
| `alert` | API failures, warnings |
| `tabs` | By status (All, Pending, Received) |
| `tooltip` | Status explanations |

**React Custom Components:**

```typescript
// components/reports/ThirdPartyReportsDashboard.tsx
interface ThirdPartyReportsDashboardProps {
  dealId: string;
  reports: ThirdPartyReport[];
  onOrderReport: (reportType: ReportType) => void;
  onOrderAll: () => void;
  onRefresh: () => void;
}

// Main reports dashboard
// Composition: Uses ShadCN Card, Badge, Button, Table
```

```typescript
// components/reports/ReportCard.tsx
interface ReportCardProps {
  report: ThirdPartyReport;
  onTrack: () => void;
  onView: () => void;
  onReorder: () => void;
}

// Individual report status card
// Composition: Uses ShadCN Card, Badge, Button
```

```typescript
// components/reports/ReportStatusBadge.tsx
interface ReportStatusBadgeProps {
  status: ReportStatus;
  estimatedCompletion?: Date;
}

// Status badge with color coding
// Composition: Uses ShadCN Badge
```

```typescript
// components/reports/ReportOrderButton.tsx
interface ReportOrderButtonProps {
  reportType: ReportType;
  dealId: string;
  disabled?: boolean;
  onOrder: () => void;
  onManualOrder: () => void;
}

// Order button with fallback to manual
// Composition: Uses ShadCN Button, DropdownMenu
```

#### 3.1.4 Data Requirements

```typescript
interface ThirdPartyReport {
  id: string;
  dealId: string;
  reportType: ReportType;
  provider: Provider;
  
  // Order tracking
  orderedAt?: Date;
  externalOrderId?: string;
  status: ReportStatus;
  
  // Assignment (appraisal)
  assignedVendor?: string;
  scheduledDate?: Date;
  estimatedCompletion?: Date;
  
  // Receipt
  receivedAt?: Date;
  documentId?: string;
  documentUrl?: string;
  
  // Cost tracking
  cost?: number;
  invoiceId?: string;
  
  // AI Analysis (Phase 7)
  aiAnalyzedAt?: Date;
  aiFlags?: AnalysisFlag[];
  
  // Errors
  lastError?: string;
  errorAt?: Date;
  
  createdAt: Date;
  updatedAt: Date;
}

type ReportType = 
  | 'credit'
  | 'background_individual'
  | 'background_entity'
  | 'appraisal'
  | 'title'
  | 'flood'
  | 'feasibility'
  | 'collateral_desktop'
  | 'insurance';

type ReportStatus = 
  | 'pending_order'
  | 'ordered'
  | 'assigned'
  | 'scheduled'
  | 'in_progress'
  | 'received'
  | 'reviewed'
  | 'approved'
  | 'revision_needed'
  | 'cancelled';

type Provider = 
  | 'single_source'
  | 'crs'
  | 'exactus'
  | 'marketwise'
  | 'trinity'
  | 'first_choice'
  | 'manual';
```

#### 3.1.5 Report Type Configuration

```typescript
const REPORT_CONFIG: Record<ReportType, ReportConfig> = {
  credit: {
    displayName: 'Credit Report (Tri-Merge)',
    provider: 'crs',
    method: 'api',
    loanTypes: ['all'],
    triggerEvent: 'ssn_captured',
    cost: 'paid',
    autoOrder: true,
  },
  background_individual: {
    displayName: 'Background Check (Individual)',
    provider: 'crs',
    method: 'api',
    loanTypes: ['all'],
    triggerEvent: 'ssn_captured',
    cost: 'paid',
    autoOrder: true,
  },
  background_entity: {
    displayName: 'Background Check (Entity)',
    provider: 'crs',
    method: 'api',
    loanTypes: ['all'],
    triggerEvent: 'ein_captured',
    cost: 'paid',
    autoOrder: true,
  },
  appraisal: {
    displayName: 'Appraisal',
    provider: 'single_source',
    method: 'api',
    loanTypes: ['all'],
    triggerEvent: 'deposit_received',
    cost: 'paid',
    autoOrder: true,
  },
  title: {
    displayName: 'Title Report',
    provider: 'single_source',
    method: 'api',
    loanTypes: ['all'],
    triggerEvent: 'term_sheet_signed',
    cost: 'free',
    autoOrder: true,
  },
  flood: {
    displayName: 'Flood Determination',
    provider: 'single_source',
    method: 'api',
    loanTypes: ['all'],
    triggerEvent: 'deposit_received',
    cost: 'paid',
    autoOrder: true,
  },
  feasibility: {
    displayName: 'Feasibility Study',
    provider: 'single_source',
    method: 'api',
    loanTypes: ['fix_flip', 'ground_up', 'bridge'],
    triggerEvent: 'deposit_received',
    cost: 'paid',
    autoOrder: true,
  },
  collateral_desktop: {
    displayName: 'Collateral Desktop Analysis',
    provider: 'single_source',
    method: 'api',
    loanTypes: ['dscr'],
    triggerEvent: 'deposit_received',
    cost: 'paid',
    autoOrder: true,
  },
  insurance: {
    displayName: 'Insurance Quote',
    provider: 'first_choice',
    method: 'email',
    loanTypes: ['all'],
    triggerEvent: 'term_sheet_signed',
    cost: 'free',
    autoOrder: true,
  },
};
```

#### 3.1.6 Mock Data

```json
{
  "dealId": "deal_abc123",
  "reports": [
    {
      "id": "report_001",
      "reportType": "credit",
      "provider": "crs",
      "status": "received",
      "orderedAt": "2024-12-08T10:00:00Z",
      "receivedAt": "2024-12-08T10:05:00Z",
      "documentId": "doc_credit_001",
      "documentUrl": "/documents/doc_credit_001"
    },
    {
      "id": "report_002",
      "reportType": "background_individual",
      "provider": "crs",
      "status": "received",
      "orderedAt": "2024-12-08T10:00:00Z",
      "receivedAt": "2024-12-08T10:10:00Z",
      "documentId": "doc_bg_001"
    },
    {
      "id": "report_003",
      "reportType": "appraisal",
      "provider": "single_source",
      "status": "scheduled",
      "orderedAt": "2024-12-10T14:00:00Z",
      "externalOrderId": "SS-2024-12345",
      "assignedVendor": "ABC Appraisals",
      "scheduledDate": "2024-12-15T10:00:00Z",
      "estimatedCompletion": "2024-12-17T17:00:00Z"
    },
    {
      "id": "report_004",
      "reportType": "title",
      "provider": "single_source",
      "status": "received",
      "orderedAt": "2024-12-08T14:00:00Z",
      "receivedAt": "2024-12-09T16:00:00Z",
      "documentId": "doc_title_001"
    },
    {
      "id": "report_005",
      "reportType": "flood",
      "provider": "single_source",
      "status": "received",
      "orderedAt": "2024-12-10T14:00:00Z",
      "receivedAt": "2024-12-10T14:30:00Z",
      "documentId": "doc_flood_001"
    },
    {
      "id": "report_006",
      "reportType": "feasibility",
      "provider": "single_source",
      "status": "in_progress",
      "orderedAt": "2024-12-10T14:00:00Z",
      "externalOrderId": "SS-2024-12346",
      "estimatedCompletion": "2024-12-14T17:00:00Z"
    },
    {
      "id": "report_007",
      "reportType": "insurance",
      "provider": "first_choice",
      "status": "ordered",
      "orderedAt": "2024-12-08T14:00:00Z"
    }
  ],
  "summary": {
    "total": 7,
    "received": 4,
    "inProgress": 2,
    "pending": 1
  }
}
```

---

### 3.2 P6-01: Diligence Checklist

#### 3.2.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Track document collection progress and manage diligence requests |
| **User Roles** | Processor, Loan Officer |
| **Entry Points** | Deal detail tabs, Closing dashboard |
| **PRD Reference** | Phase 5-6 PRD, Section 4.1-4.11 |

#### 3.2.2 Information Architecture

**Primary Data:** DiligenceItem[]

**Content Hierarchy:**
1. Progress summary (X/Y complete, percentage)
2. Category sections (Borrower, Property, Third-Party, Closing)
3. Individual items with status
4. Actions (Send Reminder, Request Doc, Mark Complete)

#### 3.2.3 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `card` | Category cards |
| `checkbox` | Item completion |
| `badge` | Status badges |
| `button` | Send Reminder, Request, Upload |
| `progress` | Category and overall progress |
| `accordion` | Collapsible categories |
| `alert` | Expiring documents, missing items |
| `tooltip` | Item details |
| `dialog` | Request document modal |

**React Custom Components:**

```typescript
// components/diligence/DiligenceChecklist.tsx
interface DiligenceChecklistProps {
  dealId: string;
  items: DiligenceItem[];
  clientType: 'new' | 'existing' | 're_cfo';
  loanType: string;
  onSendReminder: () => void;
  onRequestDocument: (itemId: string) => void;
  onMarkComplete: (itemId: string) => void;
  onWaive: (itemId: string, reason: string) => void;
}

// Main diligence checklist
// Composition: Uses ShadCN Accordion, Card, Checkbox, Badge
```

```typescript
// components/diligence/DiligenceCategoryCard.tsx
interface DiligenceCategoryCardProps {
  category: DiligenceCategory;
  items: DiligenceItem[];
  progress: { complete: number; total: number };
  expanded?: boolean;
  onToggle: () => void;
}

// Category section with items
// Composition: Uses ShadCN Card, Accordion, Progress
```

```typescript
// components/diligence/DiligenceItemRow.tsx
interface DiligenceItemRowProps {
  item: DiligenceItem;
  onView: () => void;
  onRequest: () => void;
  onReject: () => void;
  onWaive: () => void;
}

// Individual checklist item
// Composition: Uses ShadCN Checkbox, Badge, Button
```

```typescript
// components/diligence/DiligenceProgressBar.tsx
interface DiligenceProgressBarProps {
  categories: {
    name: string;
    complete: number;
    total: number;
  }[];
  overallProgress: number;
}

// Visual progress indicator
// Composition: Uses ShadCN Progress
```

```typescript
// components/diligence/DocumentExpirationAlert.tsx
interface DocumentExpirationAlertProps {
  expiringDocuments: {
    documentType: string;
    expirationDate: Date;
    daysUntilExpiry: number;
  }[];
}

// Alert for expiring documents
// Composition: Uses ShadCN Alert, Badge
```

#### 3.2.4 Data Requirements

```typescript
interface DiligenceItem {
  id: string;
  dealId: string;
  
  // Item definition
  category: DiligenceCategory;
  documentType: string;
  displayName: string;
  
  // Requirements
  isRequired: boolean;
  requiredFor: string[]; // Loan types
  source: DiligenceSource;
  
  // Status
  status: DiligenceStatus;
  
  // Linked document
  documentId?: string;
  document?: Document;
  
  // For existing clients
  onFileFrom?: string; // Reference to prior deal
  onFileDate?: Date;
  
  // Expiration
  expirationDate?: Date;
  expirationAlertSent?: boolean;
  
  // Rejection
  rejectedAt?: Date;
  rejectionReason?: string;
  rejectionNotes?: string;
  
  // Waiver
  waivedAt?: Date;
  waivedBy?: string;
  waiverReason?: string;
  
  createdAt: Date;
  updatedAt: Date;
}

type DiligenceCategory = 
  | 'borrower'
  | 'property'
  | 'third_party'
  | 'closing'
  | 'internal';

type DiligenceSource = 
  | 'borrower'
  | 'third_party'
  | 'title'
  | 'internal'
  | 'application';

type DiligenceStatus = 
  | 'required'
  | 'on_file'
  | 'requested'
  | 'received'
  | 'rejected'
  | 'waived';
```

#### 3.2.5 Diligence Checklist Template

```typescript
const DILIGENCE_TEMPLATE: DiligenceItemTemplate[] = [
  // BORROWER DOCUMENTS
  {
    category: 'borrower',
    documentType: 'articles_of_organization',
    displayName: 'Articles of Organization/Incorporation',
    requiredFor: ['all'],
    source: 'borrower',
    newClientRequired: true,
    existingClientOnFile: true,
    reCFOClientOnFile: true,
  },
  {
    category: 'borrower',
    documentType: 'operating_agreement',
    displayName: 'Operating Agreement / Bylaws',
    requiredFor: ['all'],
    source: 'borrower',
    newClientRequired: true,
    existingClientOnFile: true,
    reCFOClientOnFile: true,
  },
  {
    category: 'borrower',
    documentType: 'certificate_good_standing',
    displayName: 'Certificate of Good Standing',
    requiredFor: ['all'],
    source: 'borrower',
    newClientRequired: true,
    existingClientOnFile: false, // Must verify current
    reCFOClientOnFile: true,
    expirationDays: 90,
  },
  {
    category: 'borrower',
    documentType: 'ein_letter',
    displayName: 'EIN Letter (SS4) or W-9',
    requiredFor: ['all'],
    source: 'borrower',
    newClientRequired: true,
    existingClientOnFile: true,
    reCFOClientOnFile: true,
  },
  {
    category: 'borrower',
    documentType: 'bank_statements',
    displayName: 'Last 2 months Bank Statements',
    requiredFor: ['all'],
    source: 'borrower',
    newClientRequired: true,
    existingClientRequired: true,
    reCFOClientOnFile: true,
    expirationDays: 90,
  },
  {
    category: 'borrower',
    documentType: 'drivers_license',
    displayName: 'Driver\'s License (all guarantors)',
    requiredFor: ['all'],
    source: 'borrower',
    newClientRequired: true,
    existingClientOnFile: true,
    reCFOClientOnFile: true,
    perGuarantor: true,
  },
  
  // PROPERTY DOCUMENTS - RTL
  {
    category: 'property',
    documentType: 'purchase_contract',
    displayName: 'Purchase Contract / PSA',
    requiredFor: ['fix_flip', 'ground_up', 'bridge'],
    source: 'borrower',
    loanPurpose: ['purchase'],
  },
  {
    category: 'property',
    documentType: 'plans_specifications',
    displayName: 'Plans & Specifications',
    requiredFor: ['ground_up'],
    source: 'borrower',
  },
  {
    category: 'property',
    documentType: 'scope_of_work',
    displayName: 'Construction Budget / Scope of Work',
    requiredFor: ['fix_flip', 'ground_up'],
    source: 'borrower',
  },
  {
    category: 'property',
    documentType: 'permits',
    displayName: 'Permits (if on file)',
    requiredFor: ['fix_flip', 'ground_up'],
    source: 'borrower',
    isOptional: true,
  },
  
  // PROPERTY DOCUMENTS - DSCR
  {
    category: 'property',
    documentType: 'lease_agreement',
    displayName: 'Lease Agreement(s)',
    requiredFor: ['dscr'],
    source: 'borrower',
  },
  {
    category: 'property',
    documentType: 'rent_payment_proof',
    displayName: 'Proof of Rent Payment',
    requiredFor: ['dscr'],
    source: 'borrower',
  },
  {
    category: 'property',
    documentType: 'security_deposit_proof',
    displayName: 'Security Deposit Proof',
    requiredFor: ['dscr'],
    source: 'borrower',
  },
  
  // THIRD-PARTY REPORTS
  {
    category: 'third_party',
    documentType: 'credit_report',
    displayName: 'Credit Report',
    requiredFor: ['all'],
    source: 'third_party',
    expirationDays: 120,
    autoOrdered: true,
  },
  {
    category: 'third_party',
    documentType: 'background_check',
    displayName: 'Background Check',
    requiredFor: ['all'],
    source: 'third_party',
    autoOrdered: true,
  },
  {
    category: 'third_party',
    documentType: 'appraisal',
    displayName: 'Appraisal',
    requiredFor: ['all'],
    source: 'third_party',
    expirationDays: 120,
    autoOrdered: true,
  },
  {
    category: 'third_party',
    documentType: 'title_commitment',
    displayName: 'Title Commitment',
    requiredFor: ['all'],
    source: 'third_party',
    autoOrdered: true,
  },
  {
    category: 'third_party',
    documentType: 'flood_cert',
    displayName: 'Flood Determination',
    requiredFor: ['all'],
    source: 'third_party',
    autoOrdered: true,
  },
  {
    category: 'third_party',
    documentType: 'feasibility',
    displayName: 'Feasibility Study',
    requiredFor: ['fix_flip', 'ground_up'],
    source: 'third_party',
    autoOrdered: true,
  },
  {
    category: 'third_party',
    documentType: 'insurance_certificate',
    displayName: 'Insurance Certificate',
    requiredFor: ['all'],
    source: 'third_party',
    autoOrdered: true,
  },
  
  // CLOSING DOCUMENTS
  {
    category: 'closing',
    documentType: 'preliminary_hud',
    displayName: 'Preliminary HUD / Settlement Statement',
    requiredFor: ['all'],
    source: 'title',
  },
  {
    category: 'closing',
    documentType: 'closing_protection_letter',
    displayName: 'Closing Protection Letter',
    requiredFor: ['all'],
    source: 'title',
  },
  {
    category: 'closing',
    documentType: 'escrow_instructions',
    displayName: 'Escrow & Closing Instructions',
    requiredFor: ['all'],
    source: 'title',
  },
];
```

#### 3.2.6 Mock Data

```json
{
  "dealId": "deal_abc123",
  "clientType": "existing",
  "loanType": "fix_flip",
  "progress": {
    "overall": 78,
    "byCategory": {
      "borrower": { "complete": 6, "total": 8 },
      "property": { "complete": 5, "total": 6 },
      "third_party": { "complete": 5, "total": 6 },
      "closing": { "complete": 2, "total": 4 }
    }
  },
  "items": [
    {
      "id": "item_001",
      "category": "borrower",
      "documentType": "articles_of_organization",
      "displayName": "Articles of Organization",
      "status": "on_file",
      "onFileFrom": "deal_xyz789",
      "onFileDate": "2024-06-15T00:00:00Z"
    },
    {
      "id": "item_002",
      "category": "borrower",
      "documentType": "certificate_good_standing",
      "displayName": "Certificate of Good Standing",
      "status": "received",
      "documentId": "doc_cgs_001",
      "expirationDate": "2025-03-10T00:00:00Z"
    },
    {
      "id": "item_003",
      "category": "borrower",
      "documentType": "bank_statements",
      "displayName": "Bank Statements (2 months)",
      "status": "received",
      "documentId": "doc_bank_001"
    },
    {
      "id": "item_004",
      "category": "borrower",
      "documentType": "drivers_license",
      "displayName": "Driver's License - Jane Smith",
      "status": "required"
    },
    {
      "id": "item_005",
      "category": "property",
      "documentType": "purchase_contract",
      "displayName": "Purchase Contract",
      "status": "received",
      "documentId": "doc_psa_001"
    },
    {
      "id": "item_006",
      "category": "third_party",
      "documentType": "appraisal",
      "displayName": "Appraisal",
      "status": "requested",
      "linkedReportId": "report_003"
    }
  ],
  "expiringDocuments": [
    {
      "documentType": "certificate_good_standing",
      "expirationDate": "2025-03-10T00:00:00Z",
      "daysUntilExpiry": 90
    }
  ]
}
```

---

### 3.3 P6-02: Document Upload (Borrower-Facing)

#### 3.3.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Frictionless document upload for borrowers |
| **User Roles** | Borrower (public, authenticated via token) |
| **Entry Points** | Email link, SMS link |
| **PRD Reference** | Phase 5-6 PRD, Section 4.5.1 |

#### 3.3.2 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `card` | Upload area, recent uploads |
| `button` | Browse Files |
| `progress` | Upload progress |
| `badge` | Processing status |
| `alert` | Success/error messages |

**React Custom Components:**

```typescript
// components/upload/BorrowerUploadPage.tsx
interface BorrowerUploadPageProps {
  dealId: string;
  token: string;
}

// Public upload page
// Composition: Uses ShadCN Card, custom drag-drop
```

```typescript
// components/upload/DragDropUploader.tsx
interface DragDropUploaderProps {
  onUpload: (files: File[]) => Promise<void>;
  acceptedTypes?: string[];
  maxFileSize?: number; // bytes
  maxFiles?: number;
}

// Drag and drop file uploader
// Composition: Uses ShadCN Card, Progress
```

```typescript
// components/upload/UploadProgressList.tsx
interface UploadProgressListProps {
  uploads: {
    filename: string;
    progress: number;
    status: 'uploading' | 'processing' | 'complete' | 'error';
    classifiedAs?: string;
    error?: string;
  }[];
}

// List of uploads with progress
// Composition: Uses ShadCN Progress, Badge
```

```typescript
// components/upload/RecentUploadsCard.tsx
interface RecentUploadsCardProps {
  uploads: {
    filename: string;
    uploadedAt: Date;
    classifiedAs: string;
    status: string;
  }[];
}

// Recently uploaded files
// Composition: Uses ShadCN Card, Table
```

#### 3.3.3 Responsive Design

| Breakpoint | Layout |
|------------|--------|
| Desktop | Large drop zone, side panel for recent uploads |
| Tablet | Stacked layout, medium drop zone |
| Mobile | Full-width drop zone, tap to upload, camera capture |

---

### 3.4 P6-03: Document Review Queue

#### 3.4.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Review AI-classified documents, approve/reject/reclassify |
| **User Roles** | Processor |
| **Entry Points** | Deal detail, notification link |
| **PRD Reference** | Phase 5-6 PRD, Section 4.6 |

#### 3.4.2 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `card` | Document cards |
| `badge` | Confidence score, classification |
| `button` | Approve, Reject, Reclassify |
| `select` | Reclassification dropdown |
| `dialog` | Rejection reason modal |
| `table` | Queue list view |

**React Custom Components:**

```typescript
// components/documents/DocumentReviewQueue.tsx
interface DocumentReviewQueueProps {
  dealId: string;
  documents: DocumentForReview[];
  onApprove: (docId: string) => void;
  onReject: (docId: string, reason: string, notes: string) => void;
  onReclassify: (docId: string, newType: string) => void;
}

// Document review queue
// Composition: Uses ShadCN Table, Card, Badge
```

```typescript
// components/documents/DocumentReviewCard.tsx
interface DocumentReviewCardProps {
  document: DocumentForReview;
  onApprove: () => void;
  onReject: () => void;
  onReclassify: (newType: string) => void;
  onPreview: () => void;
}

// Individual document review card
// Composition: Uses ShadCN Card, Badge, Button, Select
```

```typescript
// components/documents/AIClassificationBadge.tsx
interface AIClassificationBadgeProps {
  classification: string;
  confidence: number;
  suggestedFilename: string;
}

// AI classification display with confidence
// Composition: Uses ShadCN Badge, Tooltip
```

```typescript
// components/documents/DocumentRejectionDialog.tsx
interface DocumentRejectionDialogProps {
  document: DocumentForReview;
  open: boolean;
  onReject: (reason: string, notes: string) => void;
  onCancel: () => void;
}

// Rejection modal with reason selection
// Composition: Uses ShadCN Dialog, Select, Textarea
```

#### 3.4.3 Data Requirements

```typescript
interface DocumentForReview {
  id: string;
  dealId: string;
  
  // File info
  filename: string;
  originalFilename: string;
  fileUrl: string;
  fileSize: number;
  mimeType: string;
  
  // Upload info
  uploadedAt: Date;
  uploadMethod: 'drag_drop' | 'email' | 'whatsapp' | 'api' | 'direct';
  uploadedBy?: string;
  sourceEmail?: string;
  
  // AI Classification
  aiClassification: string;
  aiConfidence: number;
  aiSuggestedFilename: string;
  aiExtractedData?: Record<string, any>;
  
  // Review status
  reviewStatus: 'pending' | 'approved' | 'rejected';
  needsManualClassification: boolean;
  
  // Preview
  previewUrl?: string;
  thumbnailUrl?: string;
}
```

---

## 4. AI Document Classification

### 4.1 Classification Categories

```typescript
const DOCUMENT_CATEGORIES = {
  borrower_entity: {
    displayName: 'Borrower Entity Documents',
    types: [
      'articles_of_organization',
      'operating_agreement',
      'certificate_good_standing',
      'ein_letter',
      'w9',
    ],
  },
  borrower_identity: {
    displayName: 'Borrower Identity Documents',
    types: [
      'drivers_license',
      'passport',
      'green_card',
    ],
  },
  borrower_financial: {
    displayName: 'Borrower Financial Documents',
    types: [
      'bank_statement',
      'personal_financial_statement',
      'sreo',
      'tax_return',
    ],
  },
  property_acquisition: {
    displayName: 'Property Acquisition Documents',
    types: [
      'purchase_contract',
      'psa',
      'assignment',
    ],
  },
  property_construction: {
    displayName: 'Property Construction Documents',
    types: [
      'plans',
      'specifications',
      'scope_of_work',
      'budget',
      'permits',
    ],
  },
  property_rental: {
    displayName: 'Property Rental Documents',
    types: [
      'lease',
      'rent_roll',
      'rent_receipt',
      'security_deposit_proof',
    ],
  },
  third_party_valuation: {
    displayName: 'Third-Party Valuation',
    types: [
      'appraisal',
      'bpo',
      'cda',
      'feasibility',
    ],
  },
  third_party_title: {
    displayName: 'Third-Party Title',
    types: [
      'title_commitment',
      'title_policy',
      'payoff_letter',
    ],
  },
  third_party_other: {
    displayName: 'Third-Party Other',
    types: [
      'flood_cert',
      'insurance_certificate',
      'tax_cert',
    ],
  },
  closing: {
    displayName: 'Closing Documents',
    types: [
      'hud',
      'closing_instructions',
      'cpl',
      'note',
      'deed_of_trust',
    ],
  },
  unknown: {
    displayName: 'Unknown',
    types: ['unknown'],
  },
};
```

### 4.2 Classification Prompt

```typescript
const CLASSIFICATION_PROMPT = `
Analyze this document and classify it for a real estate loan file.

Document filename: {filename}
First 2000 characters of extracted text:
{extractedText}

Deal context:
- Loan Type: {loanType}
- Property Address: {propertyAddress}
- Borrower Name: {borrowerName}
- Entity Name: {entityName}

Classify into one of these categories:
- borrower_entity: Corporate formation documents (Articles, Operating Agreement, Good Standing, EIN, W-9)
- borrower_identity: ID documents (Driver's License, Passport, Green Card)
- borrower_financial: Financial documents (Bank Statements, PFS, Tax Returns)
- property_acquisition: Purchase documents (Contract, PSA, Assignment)
- property_construction: Construction documents (Plans, Specs, Scope of Work, Budget, Permits)
- property_rental: Rental documents (Lease, Rent Roll, Rent Receipts)
- third_party_valuation: Valuation reports (Appraisal, BPO, CDA, Feasibility)
- third_party_title: Title documents (Title Commitment, Policy, Payoff)
- third_party_other: Other third-party (Flood, Insurance, Tax Cert)
- closing: Closing documents (HUD, Note, Deed of Trust)
- unknown: Cannot determine

Respond with JSON:
{
  "category": "...",
  "documentType": "specific type within category",
  "confidence": 0.0-1.0,
  "suggestedFilename": "standardized filename",
  "extractedData": {
    // Any key data points extracted (dates, names, amounts, etc.)
  },
  "reasoning": "Brief explanation of classification"
}
`;
```

### 4.3 Classification Service

```typescript
interface ClassificationResult {
  category: string;
  documentType: string;
  confidence: number;
  suggestedFilename: string;
  extractedData: Record<string, any>;
  reasoning: string;
}

async function classifyDocument(
  file: File,
  dealContext: DealContext
): Promise<ClassificationResult> {
  // 1. Extract text from document
  const extractedText = await extractText(file);
  
  // 2. Build prompt
  const prompt = CLASSIFICATION_PROMPT
    .replace('{filename}', file.name)
    .replace('{extractedText}', extractedText.substring(0, 2000))
    .replace('{loanType}', dealContext.loanType)
    .replace('{propertyAddress}', dealContext.propertyAddress)
    .replace('{borrowerName}', dealContext.borrowerName)
    .replace('{entityName}', dealContext.entityName);
  
  // 3. Call LLM
  const response = await llm.complete({
    model: 'claude-3-5-sonnet',
    temperature: 0.1,
    maxTokens: 1000,
    messages: [{ role: 'user', content: prompt }],
  });
  
  // 4. Parse response
  const result = JSON.parse(response.content);
  
  // 5. Handle low confidence
  if (result.confidence < 0.8) {
    await flagForManualReview(file, result);
  }
  
  return result;
}
```

---

## 5. API Integrations

### 5.1 Single Source API

```typescript
// Order Request
interface SingleSourceOrderRequest {
  orderId: string;
  dealId: string;
  reportType: 'appraisal' | 'title' | 'flood' | 'feasibility' | 'cda';
  
  property: {
    address: string;
    city: string;
    state: string;
    zip: string;
    propertyType: string;
    units?: number;
  };
  
  borrower: {
    name: string;
    email: string;
    phone: string;
  };
  
  entity: {
    name: string;
    type: string;
  };
  
  loan: {
    type: string;
    amount: number;
    purpose: string;
  };
  
  // Appraisal specific
  appraisalType?: 'interior_bpo' | 'full_appraisal';
  rushOrder?: boolean;
  
  // Feasibility specific
  scopeOfWork?: string;
  rehabBudget?: number;
  
  // Property access contact
  propertyContact: {
    name: string;
    phone: string;
    email: string;
  };
  
  callbackUrl: string;
}

// Order Response
interface SingleSourceOrderResponse {
  singleSourceOrderId: string;
  status: 'received' | 'assigned' | 'scheduled' | 'in_progress' | 'completed' | 'cancelled';
  estimatedCompletion?: Date;
  assignedVendor?: string;
  trackingUrl?: string;
}

// Webhook Payload
interface SingleSourceWebhook {
  orderId: string;
  singleSourceOrderId: string;
  status: 'completed' | 'cancelled' | 'revision_needed';
  reportUrl?: string;
  completedAt?: Date;
  notes?: string;
}
```

### 5.2 CRS API (Credit & Background)

```typescript
// Credit Request
interface CRSCreditRequest {
  requestId: string;
  dealId: string;
  
  applicant: {
    firstName: string;
    lastName: string;
    ssn: string; // Encrypted
    dateOfBirth: string;
    currentAddress: {
      street: string;
      city: string;
      state: string;
      zip: string;
    };
    previousAddress?: {
      street: string;
      city: string;
      state: string;
      zip: string;
    };
  };
  
  reportType: 'tri_merge';
  callbackUrl: string;
}

// Credit Response
interface CRSCreditResponse {
  crsReportId: string;
  status: 'pending' | 'completed' | 'error';
  
  creditScores?: {
    equifax: number;
    experian: number;
    transunion: number;
    middle: number;
  };
  
  reportPdfUrl?: string;
}

// Background Request
interface CRSBackgroundRequest {
  requestId: string;
  dealId: string;
  
  subjectType: 'individual' | 'entity';
  
  individual?: {
    firstName: string;
    lastName: string;
    ssn: string;
    dateOfBirth: string;
    address: Address;
  };
  
  entity?: {
    name: string;
    ein: string;
    state: string;
    type: string;
  };
  
  searches: (
    | 'criminal'
    | 'civil_litigation'
    | 'bankruptcy'
    | 'liens_judgments'
    | 'ofac'
    | 'foreclosure'
  )[];
  
  callbackUrl: string;
}

// Background Response
interface CRSBackgroundResponse {
  crsReportId: string;
  status: 'pending' | 'completed' | 'error';
  
  flags?: {
    hasCriminal: boolean;
    hasLitigation: boolean;
    hasBankruptcy: boolean;
    hasLiensJudgments: boolean;
    hasOFACHit: boolean;
    hasForeclosure: boolean;
  };
  
  reportPdfUrl?: string;
}
```

---

## 6. Email Ingestion

### 6.1 Email Parsing Service

```typescript
interface IncomingEmail {
  from: string;
  to: string;
  cc?: string[];
  subject: string;
  body: string;
  htmlBody?: string;
  attachments: EmailAttachment[];
  receivedAt: Date;
  messageId: string;
  inReplyTo?: string;
  references?: string[];
}

interface EmailAttachment {
  filename: string;
  contentType: string;
  size: number;
  content: Buffer;
}

interface ParsedEmailResult {
  dealId: string | null;
  reportType: ReportType | null;
  documents: {
    file: EmailAttachment;
    classification: ClassificationResult;
  }[];
  confidence: number;
  matchMethod: 'thread' | 'subject' | 'body' | 'sender' | 'attachment';
}

async function parseIncomingEmail(email: IncomingEmail): Promise<ParsedEmailResult> {
  // 1. Try to match by thread (in-reply-to)
  if (email.inReplyTo) {
    const threadMatch = await matchByThread(email.inReplyTo);
    if (threadMatch) {
      return { ...threadMatch, matchMethod: 'thread' };
    }
  }
  
  // 2. Try to match by subject (Deal ID, address)
  const subjectMatch = await matchBySubject(email.subject);
  if (subjectMatch) {
    return { ...subjectMatch, matchMethod: 'subject' };
  }
  
  // 3. Try to match by body content
  const bodyMatch = await matchByBody(email.body);
  if (bodyMatch) {
    return { ...bodyMatch, matchMethod: 'body' };
  }
  
  // 4. Try to match by sender email
  const senderMatch = await matchBySender(email.from);
  if (senderMatch) {
    return { ...senderMatch, matchMethod: 'sender' };
  }
  
  // 5. Classify attachments and try to match
  const attachmentMatch = await matchByAttachmentContent(email.attachments);
  if (attachmentMatch) {
    return { ...attachmentMatch, matchMethod: 'attachment' };
  }
  
  // 6. No match - flag for manual review
  return {
    dealId: null,
    reportType: null,
    documents: await classifyAllAttachments(email.attachments),
    confidence: 0,
    matchMethod: 'none',
  };
}
```

### 6.2 Report Email Identification

```typescript
const REPORT_EMAIL_PATTERNS: Record<string, ReportEmailPattern> = {
  single_source_appraisal: {
    fromPatterns: ['@singlesource.com', '@appraisalreport.com'],
    subjectPatterns: ['appraisal report', 'appraisal complete'],
    reportType: 'appraisal',
  },
  single_source_title: {
    fromPatterns: ['@singlesource.com', '@titlereport.com'],
    subjectPatterns: ['title commitment', 'title report'],
    reportType: 'title',
  },
  crs_credit: {
    fromPatterns: ['@crsreports.com'],
    subjectPatterns: ['credit report', 'tri-merge'],
    reportType: 'credit',
  },
  crs_background: {
    fromPatterns: ['@crsreports.com'],
    subjectPatterns: ['background check', 'background report'],
    reportType: 'background',
  },
  first_choice_insurance: {
    fromPatterns: ['@firstchoiceinsurance.com'],
    subjectPatterns: ['insurance quote', 'insurance certificate'],
    reportType: 'insurance',
  },
};

function identifyReportType(from: string, subject: string): ReportType | null {
  for (const [key, pattern] of Object.entries(REPORT_EMAIL_PATTERNS)) {
    const fromMatch = pattern.fromPatterns.some(p => from.toLowerCase().includes(p));
    const subjectMatch = pattern.subjectPatterns.some(p => 
      subject.toLowerCase().includes(p)
    );
    
    if (fromMatch || subjectMatch) {
      return pattern.reportType;
    }
  }
  
  return null;
}
```

---

## 7. API Contract (Mock)

### 7.1 Report Endpoints

```typescript
// POST /api/deals/:id/reports/order
// Order specific report
interface OrderReportRequest {
  reportType: ReportType;
  rushOrder?: boolean;
}

interface OrderReportResponse {
  report: ThirdPartyReport;
}

// POST /api/deals/:id/reports/order-all
// Order all pending reports
interface OrderAllReportsResponse {
  reports: ThirdPartyReport[];
  errors: { reportType: string; error: string }[];
}

// GET /api/deals/:id/reports
// Get all reports for deal
interface GetReportsResponse {
  reports: ThirdPartyReport[];
  summary: {
    total: number;
    received: number;
    inProgress: number;
    pending: number;
  };
}

// POST /api/reports/:reportId/reorder
// Reorder failed report
interface ReorderReportResponse {
  report: ThirdPartyReport;
}

// Webhooks
// POST /api/webhooks/single-source
// POST /api/webhooks/crs
```

### 7.2 Diligence Endpoints

```typescript
// GET /api/deals/:id/diligence-checklist
// Get customized checklist
interface GetChecklistResponse {
  items: DiligenceItem[];
  progress: {
    overall: number;
    byCategory: Record<string, { complete: number; total: number }>;
  };
  expiringDocuments: ExpiringDocument[];
}

// POST /api/deals/:id/diligence/send-request
// Send diligence request email
interface SendRequestResponse {
  success: boolean;
  emailId: string;
  uploadLink: string;
}

// POST /api/deals/:id/diligence/send-reminder
// Send reminder email
interface SendReminderRequest {
  itemIds?: string[]; // Specific items, or all outstanding
}

interface SendReminderResponse {
  success: boolean;
  emailId: string;
}
```

### 7.3 Document Endpoints

```typescript
// POST /api/upload/:dealId/:token
// Public upload endpoint
interface UploadResponse {
  documents: {
    id: string;
    filename: string;
    classification: ClassificationResult;
    status: string;
  }[];
}

// GET /api/upload/:dealId/:token/status
// Check upload link validity
interface UploadLinkStatusResponse {
  valid: boolean;
  dealId: string;
  propertyAddress: string;
  expiresAt?: Date;
}

// GET /api/deals/:id/documents
// Get all documents for deal
interface GetDocumentsResponse {
  documents: Document[];
  byCategory: Record<string, Document[]>;
}

// POST /api/documents/:id/classify
// Manually classify document
interface ClassifyRequest {
  category: string;
  documentType: string;
}

interface ClassifyResponse {
  document: Document;
}

// POST /api/documents/:id/reject
// Reject document
interface RejectRequest {
  reason: string;
  notes?: string;
}

interface RejectResponse {
  document: Document;
  emailSent: boolean;
}

// GET /api/documents/:id/versions
// Get version history
interface GetVersionsResponse {
  versions: DocumentVersion[];
}
```

### 7.4 Email Ingestion Endpoint

```typescript
// POST /api/email/ingest
// Webhook for incoming email processing
interface EmailIngestWebhook {
  messageId: string;
  from: string;
  to: string;
  subject: string;
  body: string;
  attachments: {
    filename: string;
    contentType: string;
    url: string; // Temporary download URL
  }[];
  receivedAt: string;
}

interface EmailIngestResponse {
  processed: boolean;
  dealId?: string;
  documentsCreated: number;
  flaggedForReview: boolean;
}
```

---

## 8. Background Jobs

| Job | Frequency | Purpose |
|-----|-----------|---------|
| `check-report-status` | Every 15 min | Poll Single Source/CRS for updates |
| `process-incoming-email` | Every 5 min | Parse underwriting@usdvcapital.com |
| `check-document-expiration` | Daily | Flag expiring documents |
| `send-diligence-reminders` | Daily | Send automated reminders |
| `sync-google-drive` | Every 10 min | Ensure Drive sync |
| `cleanup-upload-links` | Daily | Expire old upload links |

---

## 9. Open Questions & Assumptions

### 9.1 Open Questions

| # | Question | Impact | Owner |
|---|----------|--------|-------|
| 1 | What is the Single Source API endpoint URL? | Integration | IT |
| 2 | What is the CRS API endpoint URL? | Integration | IT |
| 3 | What email address monitors for incoming reports? | Email ingestion | IT |
| 4 | What is the standard deposit amount for third-party reports? | Payment flow | Product |

### 9.2 Assumptions Made

| # | Assumption | Rationale |
|---|------------|-----------|
| 1 | Single Source and CRS have webhook capabilities | PRD mentions webhooks |
| 2 | Google Drive is primary document storage | PRD specification |
| 3 | Email parsing uses IMAP or webhook | Standard approach |
| 4 | OCR is available for document text extraction | Required for AI classification |

---

## 10. Implementation Checklist

### 10.1 Phase 5 (Third-Party Reports)

- [ ] Single Source API integration (appraisal)
- [ ] Single Source API integration (title)
- [ ] Single Source API integration (flood)
- [ ] Single Source API integration (feasibility)
- [ ] Single Source API integration (CDA)
- [ ] CRS API integration (credit)
- [ ] CRS API integration (background)
- [ ] Insurance quote email generation
- [ ] Report status tracking
- [ ] Webhook handlers
- [ ] Report dashboard UI
- [ ] Manual order fallback
- [ ] API failure handling

### 10.2 Phase 6 (Diligence Chase)

- [ ] Diligence checklist generation logic
- [ ] Checklist customization by client type
- [ ] Checklist customization by loan type
- [ ] Diligence request email template
- [ ] Reminder email automation
- [ ] Borrower upload page (public)
- [ ] Drag-and-drop uploader
- [ ] Email ingestion service
- [ ] AI document classification
- [ ] Document review queue
- [ ] Document rejection flow
- [ ] Document versioning
- [ ] Expiration tracking
- [ ] Google Drive integration
- [ ] Data room folder structure

### 10.3 Testing

- [ ] Integration tests: Single Source API
- [ ] Integration tests: CRS API
- [ ] Integration tests: Email ingestion
- [ ] Integration tests: Google Drive
- [ ] Unit tests: Document classification
- [ ] E2E tests: Report ordering flow
- [ ] E2E tests: Document upload flow
- [ ] E2E tests: Email to document flow
- [ ] Load tests: Concurrent uploads

---

## 11. UW Manual Integration

This section maps Phase 5-6 implementation components to the USDV Underwriting Manual sections. The manual provides the authoritative document requirements and third-party report standards.

### 11.1 Manual Section Cross-References

| Implementation Component | UW Manual Section | Usage |
|--------------------------|-------------------|-------|
| **Third-Party Report Requirements** | | |
| Report types by loan type | Section 13: Document Requirements | Which reports required for RTL vs DSCR |
| Appraisal requirements | Section 8: Appraisal & Valuation | Full vs BPO vs CDA criteria |
| Credit report standards | Section 4: Credit & Background | Tri-merge requirements |
| Background check scope | Section 4.5: Background Checks | Search types (criminal, civil, OFAC) |
| Title requirements | Section 14.4: Title Analysis | Commitment standards, exceptions |
| Insurance requirements | Section 14.5: Insurance Analysis | Coverage amounts, mortgagee clause |
| Flood determination | Section 14.5.4: Flood Insurance | Zone requirements |
| **Diligence Checklist** | | |
| Master document checklist | Section 13.2: Document Checklist | Complete list by loan type |
| Borrower documents | Section 13.3: Borrower Documents | Entity, ID, financial docs |
| Property documents | Section 13.4: Property Documents | PSA, leases, SOW |
| Third-party documents | Section 13.5: Third-Party Documents | Reports, insurance, title |
| Closing documents | Section 13.6: Closing Documents | HUD, CPL, wire instructions |
| New vs existing client | Section 13.7: On-File Documents | What can be reused |
| Document currency | Section 13.8: Currency Requirements | Freshness rules (120 days) |
| **Document Classification** | | |
| Document categories | Section 13.2: Document Checklist | Classification taxonomy |
| Naming conventions | Section 13.9: Naming Conventions | Standard file naming |
| AI classification rules | Section 14: Third-Party Reports | Document type identification |

### 11.2 Document Checklist from Manual

Reference Section 13.2 for the complete checklist. Key categories:

**Borrower Documents (Section 13.3):**
| Document | RTL | DSCR | New Client | Existing Client |
|----------|-----|------|------------|-----------------|
| Articles of Organization | ✓ | ✓ | Required | On-File |
| Operating Agreement | ✓ | ✓ | Required | On-File |
| Certificate of Good Standing | ✓ | ✓ | Required | Required (current) |
| EIN Letter / W-9 | ✓ | ✓ | Required | On-File |
| Bank Statements (2 mo) | ✓ | ✓ | Required | Required |
| Driver's License | ✓ | ✓ | Required | On-File |
| Personal Financial Statement | ✓ | ✓ | Required | On-File |

**Property Documents (Section 13.4):**
| Document | RTL | DSCR | Condition |
|----------|-----|------|-----------|
| Purchase Contract | ✓ | ✓ | Purchase only |
| Scope of Work | ✓ | - | Fix & Flip, GUC |
| Plans & Specs | GUC | - | Ground-Up only |
| Permits | ✓ | - | If available |
| Lease Agreements | - | ✓ | DSCR only |
| Rent Payment Proof | - | ✓ | DSCR only |

**Third-Party Documents (Section 13.5):**
| Document | RTL | DSCR | Auto-Ordered |
|----------|-----|------|--------------|
| Credit Report | ✓ | ✓ | Yes |
| Background Check | ✓ | ✓ | Yes |
| Appraisal | ✓ | ✓ | Yes |
| Title Commitment | ✓ | ✓ | Yes |
| Flood Determination | ✓ | ✓ | Yes |
| Feasibility Study | ✓ | - | Yes (RTL) |
| Insurance Certificate | ✓ | ✓ | Yes |

### 11.3 Document Currency Rules

From Section 13.8:

| Document Type | Currency Requirement | Alert Threshold |
|---------------|---------------------|-----------------|
| Bank Statements | 90 days | 14 days before |
| Credit Report | 120 days | 14 days before |
| Appraisal | 120 days | 14 days before |
| Good Standing | 90 days | 14 days before |
| PFS | 120 days | 14 days before |
| Title Commitment | 30 days at closing | 7 days before |
| Insurance | Must cover loan term | 30 days before |

### 11.4 AI Classification Categories

Map AI classification to manual document taxonomy (Section 13.2):

```typescript
const MANUAL_CLASSIFICATION_MAP = {
  // Borrower Entity (Section 13.3.1)
  'articles_of_organization': 'borrower_entity',
  'operating_agreement': 'borrower_entity',
  'certificate_good_standing': 'borrower_entity',
  'ein_letter': 'borrower_entity',
  'w9': 'borrower_entity',
  
  // Borrower Identity (Section 13.3.2)
  'drivers_license': 'borrower_identity',
  'passport': 'borrower_identity',
  'green_card': 'borrower_identity',
  
  // Borrower Financial (Section 13.3.3)
  'bank_statement': 'borrower_financial',
  'pfs': 'borrower_financial',
  'sreo': 'borrower_financial',
  
  // Property (Section 13.4)
  'purchase_contract': 'property_acquisition',
  'scope_of_work': 'property_construction',
  'lease': 'property_rental',
  
  // Third-Party (Section 13.5)
  'appraisal': 'third_party_valuation',
  'title_commitment': 'third_party_title',
  'insurance_certificate': 'third_party_insurance',
  'flood_cert': 'third_party_flood',
};
```

### 11.5 Report Analysis Standards

When reports are received, validate against manual standards:

**Appraisal (Section 8):**
- Report type matches loan requirements (Full, BPO, CDA)
- Currency within 120 days
- Appraiser license valid
- Comp selection appropriate
- Value reconciliation reasonable

**Title (Section 14.4):**
- Schedule B-I requirements satisfied
- Schedule B-II exceptions acceptable
- No unacceptable liens
- Vesting matches borrower entity

**Insurance (Section 14.5):**
- Coverage ≥ loan amount or replacement cost
- Correct mortgagee clause
- Policy effective through loan term
- Flood insurance if in flood zone

### 11.6 Python Library Integration

| Validation Need | Python Class | Method |
|-----------------|--------------|--------|
| Document checklist generation | `DiligenceChecker` | `generate_checklist()` |
| Currency validation | `DiligenceChecker` | `check_document_currency()` |
| Expiration alerts | `DiligenceChecker` | `get_expiring_documents()` |

---

*End of Phase 5-6 Implementation Plan*

