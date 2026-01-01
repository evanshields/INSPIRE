# INSPIRE - Phase 5-6 Product Requirements Document

**Product Name:** INSPIRE  
**Company:** USDV Capital  
**Document Type:** Phase 5-6 PRD (Third-Party Reports + Diligence Chase)  
**Version:** 1.0  
**Last Updated:** November 2025

---

## 1. Overview

This PRD covers Phases 5 and 6 of INSPIRE's loan origination workflow:

- **Phase 5: Third-Party Reports** - Automated ordering and ingestion of external reports (appraisal, title, credit, background, insurance, feasibility, flood)
- **Phase 6: Diligence Chase** - Automated diligence request lists, intelligent data room, AI-powered document classification and filing

These phases transform manual report ordering and document collection into an automated, AI-driven workflow.

---

## 2. Goals & Success Metrics

### Goals

1. Automate third-party report ordering via API where available
2. Auto-ingest reports received via email into deal-specific data rooms
3. Generate smart diligence request lists based on client type and loan type
4. Enable frictionless document upload (drag-drop, no auth required)
5. AI-classify and auto-name all incoming documents
6. Reduce manual document handling to near-zero

### Success Metrics

| Metric | Target |
|--------|--------|
| Third-party reports auto-ordered | >90% |
| Report ingestion automation rate | >95% |
| Document auto-classification accuracy | >95% |
| Time from deposit to reports ordered | <1 hour |
| Manual document filing | <5% of documents |
| Diligence request to complete package | <5 business days |

---

## 3. Phase 5: Third-Party Reports

### 3.1 Overview

Once the borrower signs the term sheet and pays the third-party deposit (Phase 4), INSPIRE automatically orders all required third-party reports. Reports are tracked, received, and filed to the deal's data room.

### 3.2 Third-Party Report Types

| Report | Provider | Method | Loan Types | Cost | Trigger |
|--------|----------|--------|------------|------|---------|
| Credit Report (Tri-Merge) | CRS (primary) | API | All | Paid | Phase 3-4 (SSN captured) |
| Background Check (Guarantors) | CRS (primary) | API | All | Paid | Phase 3-4 |
| Background Check (Entities) | CRS (primary) | API | All | Paid | Phase 3-4 |
| Appraisal | Single Source (primary) | API | All | Paid | Deposit received |
| Title Report | Single Source | API | All | Free | Term sheet signed |
| Flood Determination | Single Source | API | All | Paid | Deposit received |
| Feasibility Study | Single Source (primary) | API | RTL only | Paid | Deposit received |
| Collateral Desktop Analysis | Single Source | API | DSCR only | Paid | Deposit received |
| Insurance Quote | First Choice | Email | All | Free | Term sheet signed |

**Backup Providers:**
| Report | Backup Provider | Method |
|--------|-----------------|--------|
| Credit / Background | Exactus | API |
| Appraisal | Marketwise | Portal |
| Feasibility | Trinity | Email |

### 3.3 Report Ordering Triggers

```
┌─────────────────────────────────────────────────────────────┐
│                 THIRD-PARTY REPORT TRIGGERS                  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  PHASE 3-4 (Early - No Cost to Borrower)                    │
│  ────────────────────────────────────────                   │
│  • Credit Report ──────────► On SSN capture                 │
│  • Background Checks ──────► On SSN/EIN capture             │
│                                                              │
│  TERM SHEET SIGNED (Free Reports)                           │
│  ────────────────────────────                               │
│  • Title Report ───────────► Immediate                      │
│  • Insurance Quote ────────► Immediate                      │
│                                                              │
│  DEPOSIT RECEIVED (Paid Reports)                            │
│  ────────────────────────────                               │
│  • Appraisal ──────────────► Immediate                      │
│  • Flood Determination ────► Immediate                      │
│  • Feasibility Study ──────► RTL only                       │
│  • Collateral Desktop ─────► DSCR only                      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 3.4 Single Source API Integration

#### 3.4.1 Available Endpoints

| Service | Endpoint | Data Required |
|---------|----------|---------------|
| Appraisal Order | `/appraisal/order` | Property address, contact info, loan type, rush flag |
| Title Order | `/title/order` | Property address, borrower name, entity name |
| Flood Cert | `/flood/order` | Property address |
| Feasibility | `/feasibility/order` | Property address, scope of work, budget |
| Collateral Desktop | `/cda/order` | Property address, loan amount, rent |

#### 3.4.2 Order Request Structure

```typescript
interface SingleSourceOrderRequest {
  orderId: string; // INSPIRE internal ID
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
  
  // CDA specific
  monthlyRent?: number;
  
  // Contact for property access
  propertyContact: {
    name: string;
    phone: string;
    email: string;
  };
  
  callbackUrl: string; // Webhook for status updates
}
```

#### 3.4.3 Order Response & Status Tracking

```typescript
interface SingleSourceOrderResponse {
  singleSourceOrderId: string;
  status: 'received' | 'assigned' | 'scheduled' | 'in_progress' | 'completed' | 'cancelled';
  estimatedCompletion?: Date;
  assignedVendor?: string;
  trackingUrl?: string;
}

// Webhook payload when report complete
interface SingleSourceWebhook {
  orderId: string;
  singleSourceOrderId: string;
  status: 'completed' | 'cancelled' | 'revision_needed';
  reportUrl?: string; // Download URL
  completedAt?: Date;
  notes?: string;
}
```

### 3.5 CRS API Integration (Credit & Background)

#### 3.5.1 Credit Report Order

```typescript
interface CRSCreditRequest {
  requestId: string;
  dealId: string;
  
  applicant: {
    firstName: string;
    lastName: string;
    ssn: string; // Encrypted in transit
    dateOfBirth: string;
    currentAddress: {
      street: string;
      city: string;
      state: string;
      zip: string;
    };
    previousAddress?: { /* same structure */ };
  };
  
  reportType: 'tri_merge'; // Equifax, Experian, TransUnion
  
  callbackUrl: string;
}

interface CRSCreditResponse {
  crsReportId: string;
  status: 'pending' | 'completed' | 'error';
  
  // On completion
  creditScores?: {
    equifax: number;
    experian: number;
    transunion: number;
    middle: number; // Used for underwriting
  };
  
  reportPdfUrl?: string;
}
```

#### 3.5.2 Background Check Order

```typescript
interface CRSBackgroundRequest {
  requestId: string;
  dealId: string;
  
  subjectType: 'individual' | 'entity';
  
  // For individuals
  individual?: {
    firstName: string;
    lastName: string;
    ssn: string;
    dateOfBirth: string;
    address: { /* ... */ };
  };
  
  // For entities
  entity?: {
    name: string;
    ein: string;
    state: string;
    type: string;
  };
  
  searches: [
    'criminal',
    'civil_litigation',
    'bankruptcy',
    'liens_judgments',
    'ofac',
    'foreclosure'
  ];
  
  callbackUrl: string;
}

interface CRSBackgroundResponse {
  crsReportId: string;
  status: 'pending' | 'completed' | 'error';
  
  // Summary flags
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

### 3.6 Insurance Quote Request (First Choice)

Insurance quotes are requested via email (no API available).

#### 3.6.1 Auto-Generated Email

```typescript
interface InsuranceQuoteEmail {
  to: 'quotes@firstchoiceinsurance.com';
  cc: 'underwriting@usdvcapital.com';
  subject: `Insurance Quote Request - ${propertyAddress} - ${dealId}`;
  
  body: `
    Property Address: ${property.fullAddress}
    Property Type: ${property.type}
    Units: ${property.units}
    
    Loan Type: ${deal.loanType}
    Loan Amount: ${formatCurrency(deal.loanAmount)}
    
    Coverage Needed:
    ${deal.loanType === 'dscr' ? 
      '- Dwelling/Property Insurance\n- Flood Insurance (if applicable)' :
      '- Builders Risk Insurance\n- General Liability ($500k minimum)'}
    
    Borrower: ${borrower.name}
    Entity: ${entity.name}
    
    Mortgagee Clause:
    [INVESTOR MORTGAGEE CLAUSE - Eastview/ArchWest]
    ISAOA/ATIMA
    
    Please send quote to: underwriting@usdvcapital.com
    Reference: Deal #${deal.id}
  `;
}
```

### 3.7 Report Status Tracking

#### 3.7.1 Report Statuses

| Status | Description |
|--------|-------------|
| `pending_order` | Awaiting trigger (deposit, etc.) |
| `ordered` | Order sent to provider |
| `assigned` | Vendor assigned (appraisal) |
| `scheduled` | Appointment scheduled |
| `in_progress` | Work underway |
| `received` | Report received, pending review |
| `reviewed` | AI analysis complete |
| `approved` | Passed review |
| `revision_needed` | Issues identified |
| `cancelled` | Order cancelled |

#### 3.7.2 Report Tracking UI

```
┌─────────────────────────────────────────────────────────────┐
│  THIRD-PARTY REPORTS: 123 Main St                           │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Report              Status          ETA        Actions      │
│  ──────────────────────────────────────────────────────     │
│  ✅ Credit Report    Received        -          [View]      │
│  ✅ Background       Received        -          [View]      │
│  🔄 Appraisal        Scheduled       Dec 15     [Track]     │
│  ✅ Title            Received        -          [View]      │
│  ✅ Flood Cert       Received        -          [View]      │
│  🔄 Feasibility      In Progress     Dec 14     [Track]     │
│  ⏳ Insurance        Requested       Dec 13     [Resend]    │
│                                                              │
│  [Order All Pending]  [Refresh Status]                      │
└─────────────────────────────────────────────────────────────┘
```

### 3.8 Report Ingestion

#### 3.8.1 Ingestion Methods

**Method 1: API Webhook (Preferred)**
- Single Source and CRS send completion webhooks
- INSPIRE downloads report PDF automatically
- Filed to deal data room

**Method 2: Email Parsing**
- Reports sent to `underwriting@usdvcapital.com`
- INSPIRE monitors inbox via IMAP/API
- AI identifies deal and report type from email content
- Attachment extracted and filed

#### 3.8.2 Email Parsing Logic

```typescript
async function parseIncomingReportEmail(email: Email): Promise<ParsedReport> {
  // Extract potential identifiers
  const subjectMatches = email.subject.match(/Deal #(\d+)|(\d+\s+\w+\s+(?:St|Ave|Blvd|Dr|Ln))/i);
  const bodyMatches = email.body.match(/Reference:\s*(\w+)|Property:\s*(.+)/i);
  
  // Identify report type from sender/subject
  const reportType = identifyReportType(email.from, email.subject);
  
  // Match to deal
  const deal = await matchToDeal(subjectMatches, bodyMatches, email.attachments);
  
  // Extract attachment
  const reportFile = email.attachments.find(a => 
    a.contentType === 'application/pdf' || 
    a.filename.endsWith('.pdf')
  );
  
  return {
    dealId: deal.id,
    reportType,
    file: reportFile,
    receivedAt: email.date,
    source: 'email',
    senderEmail: email.from
  };
}
```

### 3.9 API Failure Handling

When API ordering fails, system falls back to manual process:

```typescript
async function orderReport(deal: Deal, reportType: ReportType): Promise<OrderResult> {
  try {
    // Attempt API order
    const result = await singleSourceAPI.order(buildRequest(deal, reportType));
    return { success: true, orderId: result.orderId };
  } catch (error) {
    // Log failure
    await logAPIFailure(deal.id, reportType, error);
    
    // Create manual task
    await createTask({
      dealId: deal.id,
      type: 'manual_report_order',
      title: `Manually order ${reportType} - API failed`,
      description: `API order failed: ${error.message}. Please order via portal.`,
      assignTo: deal.assignedProcessor,
      priority: 'high'
    });
    
    // Notify team
    await notify({
      channel: ['email', 'roam'],
      recipients: [deal.assignedProcessor, deal.assignedLO],
      message: `API order failed for ${reportType} on ${deal.propertyAddress}. Manual order required.`
    });
    
    return { success: false, error: error.message, manualTaskCreated: true };
  }
}
```

---

## 4. Phase 6: Diligence Chase

### 4.1 Overview

Phase 6 manages the collection of all borrower-provided documents. Upon term sheet signing, INSPIRE automatically sends a tailored diligence request list and provides multiple frictionless upload methods.

### 4.2 Diligence Request List Generation

#### 4.2.1 List Customization Logic

The diligence list is customized based on:
- **Client Type:** New client vs. Existing client vs. Real Estate CFO client
- **Loan Type:** Fix & Flip, Ground-Up Construction, DSCR
- **Loan Purpose:** Purchase vs. Refinance
- **Property Type:** Single Family vs. Multi-family vs. Condo

#### 4.2.2 Master Diligence Checklist

**Category 1: Borrower Documents**

| Document | New Client | Existing Client | RE CFO Client | Notes |
|----------|------------|-----------------|---------------|-------|
| Articles of Organization/Incorporation | Required | On File | On File | |
| Operating Agreement / Bylaws | Required | On File | On File | |
| Certificate of Good Standing | Required | Verify Current | On File | Must be <90 days |
| EIN Letter (SS4) or W-9 | Required | On File | On File | |
| Last 2 months Bank Statements | Required | Required | On File | |
| Driver's License (all guarantors) | Required | On File | On File | |
| Passport / Green Card (if applicable) | Required | On File | On File | |
| Google Search (3 pages) - Sponsors | Required | Required | Required | USDV performs |
| Google Search (3 pages) - Entities | Required | Required | Required | USDV performs |

**Category 2: Property Documents - RTL (Fix & Flip / Ground-Up)**

| Document | Purchase | Refinance | Notes |
|----------|----------|-----------|-------|
| Purchase Contract / PSA | Required | Required (original) | |
| Plans & Specifications | Required | Required | Ground-up |
| Construction Budget / Scope of Work | Required | Required | |
| Permits (if on file) | If available | If available | |
| Feasibility Study | Third-party | Third-party | |
| Appraisal | Third-party | Third-party | |
| Flood Determination | Third-party | Third-party | |
| Insurance Certificates | Third-party | Third-party | Builders Risk + GL |
| Tax Certificate | Third-party (title) | Third-party (title) | |

**Category 3: Property Documents - DSCR**

| Document | Purchase | Refinance | Notes |
|----------|----------|-----------|-------|
| Purchase Contract / PSA | Required | N/A | |
| Lease Agreement(s) | Required | Required | All units |
| Proof of Rent Payment | Required | Required | Wire/ACH receipt or bank stmt |
| Security Deposit Proof | Required | Required | |
| Appraisal | Third-party | Third-party | |
| Collateral Desktop Analysis | Third-party | Third-party | |
| Flood Determination | Third-party | Third-party | |
| Insurance Certificates | Third-party | Third-party | Property + Flood |
| Tax Certificate | Third-party (title) | Third-party (title) | |

**Category 4: Closing Documents (from Title)**

| Document | Source | Notes |
|----------|--------|-------|
| Title Commitment Letter | Title Company | |
| Preliminary HUD / Settlement Statement | Title Company | |
| Closing Protection Letter | Title Company | |
| Escrow & Closing Instructions | Title Company | |
| Escrow Agent E&O Policy | Title Company | |
| Mortgage / Deed of Trust | Title Company | At closing |

**Category 5: Already Captured (Auto-Filed)**

| Document | Source | Phase |
|----------|--------|-------|
| Loan Application | Borrower | Phase 2 |
| Track Record / SREO | Borrower | Phase 2 |
| Personal Financial Statement | Borrower | Phase 2 |
| Credit Report | CRS | Phase 3-4 |
| Background Check | CRS | Phase 3-4 |

### 4.3 Diligence Request Email

#### 4.3.1 Auto-Send Trigger

Email sent automatically when term sheet is signed.

#### 4.3.2 Email Template

```
Subject: Action Required: Document Checklist for [Property Address]

Dear [Borrower Name],

Thank you for signing the term sheet for your loan on [Property Address]. 

To proceed with underwriting, please provide the following documents:

BORROWER DOCUMENTS
──────────────────
☐ Articles of Organization / Incorporation
☐ Operating Agreement
☐ Certificate of Good Standing (dated within 90 days)
☐ EIN Letter or signed W-9
☐ Last 2 months of bank statements
☐ Driver's License for [Guarantor 1], [Guarantor 2]

PROPERTY DOCUMENTS
──────────────────
☐ Purchase Contract / PSA
☐ [Scope of Work / Construction Budget] (if not already provided)
☐ [Lease Agreement + Proof of Rent Payment] (DSCR only)

HOW TO SUBMIT
─────────────
Option 1: Upload directly at [UPLOAD_LINK]
          (No login required - just drag and drop!)

Option 2: Reply to this email with attachments

Option 3: Send via WhatsApp to [INSPIRE WhatsApp Number]

We're targeting a close date of [Target Date]. Please submit documents 
within 3 business days to stay on track.

Questions? Reply to this email or call [LO Phone].

Best regards,
[Loan Officer Name]
USDV Capital
```

### 4.4 Intelligent Data Room

#### 4.4.1 Data Room Structure

Each deal has a dedicated data room in Google Drive:

```
/INSPIRE/
  /Deals/
    /[Deal_ID]_[Property_Address]/
      /01_Borrower_Docs/
        - Articles_of_Organization.pdf
        - Operating_Agreement.pdf
        - Certificate_Good_Standing_2024-12-01.pdf
        - Bank_Statements_Oct_2024.pdf
        - Bank_Statements_Nov_2024.pdf
        - DL_John_Smith.pdf
      /02_Property_Docs/
        - Purchase_Contract.pdf
        - Scope_of_Work.pdf
        - Plans_Specs.pdf
        - Permits.pdf
      /03_Third_Party_Reports/
        - Appraisal_2024-12-10.pdf
        - Title_Commitment_2024-12-08.pdf
        - Flood_Cert_2024-12-08.pdf
        - Feasibility_2024-12-12.pdf
        - Credit_Report_John_Smith.pdf
        - Background_Check_John_Smith.pdf
      /04_Closing_Docs/
        - Preliminary_HUD.pdf
        - Closing_Protection_Letter.pdf
      /05_Internal/
        - Credit_Memo.pdf
        - Exception_Requests.pdf
```

#### 4.4.2 Document Naming Convention

```
[DocumentType]_[Identifier]_[Date].pdf

Examples:
- Bank_Statements_Nov_2024.pdf
- DL_John_Smith.pdf
- Appraisal_2024-12-10.pdf
- Articles_of_Organization.pdf
- Lease_Unit_1.pdf
```

### 4.5 Document Ingestion Methods

#### 4.5.1 Method 1: Drag-and-Drop Upload Link (Public)

**URL:** `upload.usdvcapital.com/{deal_id}/{token}`

- No authentication required
- Unique per deal
- Token expires with deal close
- Anyone with link can upload (borrower, title, insurance, etc.)

**UI:**
```
┌─────────────────────────────────────────────────────────────┐
│                                                              │
│              📁 Upload Documents                             │
│              for 123 Main Street                             │
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │                                                      │    │
│  │     Drag and drop files here                        │    │
│  │              or                                     │    │
│  │         [Browse Files]                              │    │
│  │                                                      │    │
│  │     Accepted: PDF, JPG, PNG, DOC, DOCX, XLS, XLSX   │    │
│  │     Max file size: 50MB                             │    │
│  │                                                      │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                              │
│  Recently Uploaded:                                         │
│  ✅ Bank_Statement_Nov.pdf - Processing...                  │
│  ✅ Operating_Agreement.pdf - Filed to Borrower Docs        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

#### 4.5.2 Method 2: Email to underwriting@usdvcapital.com

- Borrower replies to diligence request email with attachments
- Or forwards documents directly
- AI parses email to identify deal and document types

**Parsing Logic:**
```typescript
async function parseIncomingDocumentEmail(email: Email): Promise<ParsedDocuments> {
  // Identify deal from:
  // 1. In-reply-to header (thread matching)
  // 2. Subject line deal ID or address
  // 3. Body content parsing
  // 4. Sender email matching to borrower
  
  const deal = await identifyDeal(email);
  
  const documents = await Promise.all(
    email.attachments.map(async (attachment) => {
      const classification = await aiClassifyDocument(attachment, deal);
      return {
        file: attachment,
        dealId: deal.id,
        documentType: classification.type,
        confidence: classification.confidence,
        suggestedName: classification.suggestedName
      };
    })
  );
  
  return { deal, documents };
}
```

#### 4.5.3 Method 3: WhatsApp (Phase 9)

Documents sent to INSPIRE's WhatsApp number are automatically captured and filed. (See Phase 9 PRD)

### 4.6 AI Document Classification

#### 4.6.1 Classification Categories

| Category | Document Types |
|----------|---------------|
| `borrower_entity` | Articles of Org, Operating Agreement, Cert of Good Standing, EIN Letter, W-9 |
| `borrower_identity` | Driver's License, Passport, Green Card |
| `borrower_financial` | Bank Statements, PFS, SREO, Tax Returns |
| `property_acquisition` | Purchase Contract, PSA, Assignment |
| `property_construction` | Plans, Specs, Scope of Work, Budget, Permits |
| `property_rental` | Lease, Rent Roll, Rent Receipts, Security Deposit Proof |
| `third_party_valuation` | Appraisal, BPO, CDA, Feasibility |
| `third_party_title` | Title Commitment, Title Policy, Payoff Letter |
| `third_party_other` | Flood Cert, Insurance, Tax Cert |
| `closing` | HUD, Closing Instructions, CPL, Note, Deed of Trust |
| `unknown` | Cannot classify with confidence |

#### 4.6.2 Classification Prompt

```typescript
const classificationPrompt = `
Analyze this document and classify it for a real estate loan file.

Document filename: ${filename}
First 2000 characters of extracted text:
${extractedText}

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
  }
}
`;
```

#### 4.6.3 Low Confidence Handling

If classification confidence < 0.8:
1. Flag for manual review
2. Create task for processor
3. Show in UI with "Needs Classification" badge

```typescript
if (classification.confidence < 0.8) {
  await createTask({
    dealId: deal.id,
    type: 'document_classification',
    title: `Classify document: ${filename}`,
    description: `AI confidence: ${classification.confidence}. Suggested: ${classification.documentType}`,
    assignTo: deal.assignedProcessor
  });
}
```

### 4.7 Document Versioning

#### 4.7.1 Version Tracking

When a document of the same type is uploaded again:

```typescript
interface DocumentVersion {
  documentId: string;
  version: number;
  filename: string;
  fileUrl: string;
  uploadedAt: Date;
  uploadedBy: string;
  uploadMethod: 'drag_drop' | 'email' | 'whatsapp' | 'direct';
  isCurrentVersion: boolean;
}
```

**Naming with Date:**
```
Bank_Statements_Nov_2024.pdf (v1)
Bank_Statements_Nov_2024_2024-12-05.pdf (v2 - uploaded Dec 5)
Bank_Statements_Dec_2024.pdf (different doc)
```

### 4.8 Document Expiration Tracking

#### 4.8.1 Documents with Expiration

| Document | Expiration Rule |
|----------|-----------------|
| Certificate of Good Standing | 90 days from issue |
| Credit Report | 120 days from pull |
| Appraisal | 120 days from report date |
| Insurance Policy | Policy expiration date |
| Title Commitment | 90 days typical |
| Bank Statements | 90 days from statement date |

#### 4.8.2 Expiration Alerts

```typescript
async function checkDocumentExpiration(deal: Deal): Promise<ExpirationAlert[]> {
  const alerts: ExpirationAlert[] = [];
  
  for (const doc of deal.documents) {
    if (doc.expirationDate) {
      const daysUntilExpiry = differenceInDays(doc.expirationDate, new Date());
      
      if (daysUntilExpiry <= 0) {
        alerts.push({
          documentId: doc.id,
          type: 'expired',
          message: `${doc.type} expired on ${formatDate(doc.expirationDate)}`
        });
      } else if (daysUntilExpiry <= 7) {
        alerts.push({
          documentId: doc.id,
          type: 'expiring_soon',
          message: `${doc.type} expires in ${daysUntilExpiry} days`
        });
      }
    }
  }
  
  return alerts;
}
```

### 4.9 Document Rejection Flow

#### 4.9.1 Rejection Reasons

| Reason | Description |
|--------|-------------|
| `illegible` | Document too blurry or low quality |
| `incomplete` | Missing pages or sections |
| `wrong_document` | Not the requested document |
| `outdated` | Document is expired or too old |
| `wrong_entity` | Document for different entity/person |
| `missing_signature` | Required signature missing |
| `other` | Custom reason |

#### 4.9.2 Rejection Workflow

```
1. AI flags document OR internal user flags document
        │
        ▼
2. Document marked "Pending Review" (not rejected yet)
        │
        ▼
3. Internal user reviews and confirms rejection
        │
        ▼
4. Select rejection reason + add notes
        │
        ▼
5. System generates rejection email to borrower
   - Specific document identified
   - Reason explained
   - Instructions to re-upload
   - CC internal team
        │
        ▼
6. Document status → "Rejected"
   Original file retained for audit
        │
        ▼
7. Checklist updated to show item as "Needs Re-upload"
```

#### 4.9.3 Rejection Email Template

```
Subject: Document Re-Upload Needed - [Property Address]

Dear [Borrower Name],

We've reviewed your uploaded documents for [Property Address] and 
need you to re-submit the following:

DOCUMENT: [Document Type]
ISSUE: [Rejection Reason]
DETAILS: [Specific notes from reviewer]

Please upload a corrected version at:
[UPLOAD_LINK]

If you have questions about what's needed, please reply to this email.

Best regards,
[Processor Name]
USDV Capital
```

### 4.10 Diligence Checklist UI

#### 4.10.1 Internal View

```
┌─────────────────────────────────────────────────────────────┐
│  DILIGENCE CHECKLIST: 123 Main St                           │
│  Client: John Smith (Existing Client)                       │
│  Loan Type: Fix & Flip | Progress: 14/18 (78%)             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  BORROWER DOCUMENTS                              [4/6]      │
│  ─────────────────                                          │
│  ✅ Articles of Organization        On File                 │
│  ✅ Operating Agreement              On File                 │
│  ⚠️  Certificate of Good Standing    Expires in 5 days      │
│  ✅ EIN Letter                       On File                 │
│  ✅ Bank Statements (2 mo)           Received Dec 5         │
│  ❌ Driver's License - Jane Doe      Missing                │
│                                                              │
│  PROPERTY DOCUMENTS                              [3/4]      │
│  ──────────────────                                         │
│  ✅ Purchase Contract                Received Dec 3         │
│  ✅ Scope of Work                    Received Dec 4         │
│  ✅ Plans & Specs                    Received Dec 4         │
│  ❌ Permits                          Requested              │
│                                                              │
│  THIRD-PARTY REPORTS                             [5/6]      │
│  ───────────────────                                        │
│  ✅ Credit Report                    Received               │
│  ✅ Background Check                 Received               │
│  🔄 Appraisal                        In Progress - ETA 12/15│
│  ✅ Title Commitment                 Received               │
│  ✅ Flood Cert                       Received               │
│  ✅ Feasibility                      Received               │
│                                                              │
│  CLOSING DOCUMENTS                               [2/4]      │
│  ─────────────────                                          │
│  ❌ Preliminary HUD                  Pending from Title     │
│  ❌ Closing Protection Letter        Pending from Title     │
│  ✅ Insurance Certificate            Received               │
│  ✅ Escrow Instructions              Received               │
│                                                              │
│  [Send Reminder]  [Mark Complete]  [View Data Room]         │
└─────────────────────────────────────────────────────────────┘
```

### 4.11 Automated Reminders

#### 4.11.1 Reminder Schedule

| Day | Action |
|-----|--------|
| Day 0 | Initial diligence request sent |
| Day 2 | Reminder #1 if items outstanding |
| Day 4 | Reminder #2 + escalation to LO |
| Day 7 | Urgent reminder + call task for LO |

#### 4.11.2 Reminder Email Template

```
Subject: Reminder: Outstanding Documents for [Property Address]

Dear [Borrower Name],

We're still waiting on the following documents to proceed with your loan:

☐ [Document 1]
☐ [Document 2]

Upload here: [UPLOAD_LINK]

Our target close date is [Date]. To stay on track, please submit 
these documents within the next 2 business days.

Questions? Call [LO Name] at [Phone].

Best regards,
USDV Capital
```

---

## 5. Technical Requirements

### 5.1 API Endpoints

```
# Third-Party Reports
POST   /api/deals/:id/reports/order
       → Order specific report type

POST   /api/deals/:id/reports/order-all
       → Order all pending reports

GET    /api/deals/:id/reports
       → Get all reports for deal

GET    /api/reports/:reportId
       → Get single report details

POST   /api/reports/:reportId/reorder
       → Reorder failed/cancelled report

POST   /api/webhooks/single-source
       → Handle Single Source callbacks

POST   /api/webhooks/crs
       → Handle CRS callbacks

# Diligence
GET    /api/deals/:id/diligence-checklist
       → Get customized checklist

POST   /api/deals/:id/diligence/send-request
       → Send diligence request email

POST   /api/deals/:id/diligence/send-reminder
       → Send reminder email

# Document Upload
POST   /api/upload/:dealId/:token
       → Public upload endpoint

GET    /api/upload/:dealId/:token/status
       → Check upload link validity

# Document Management
GET    /api/deals/:id/documents
       → Get all documents for deal

POST   /api/documents/:id/classify
       → Manually classify document

POST   /api/documents/:id/reject
       → Reject document with reason

GET    /api/documents/:id/versions
       → Get version history

# Email Ingestion
POST   /api/email/ingest
       → Webhook for incoming email processing
```

### 5.2 Data Models

```typescript
// Third-Party Report
model ThirdPartyReport {
  id                String   @id @default(uuid())
  dealId            String
  deal              Deal     @relation(fields: [dealId], references: [id])
  
  reportType        ReportType
  provider          Provider
  
  // Order tracking
  orderedAt         DateTime?
  externalOrderId   String?  // Provider's order ID
  status            ReportStatus
  
  // Assignment (appraisal)
  assignedVendor    String?
  scheduledDate     DateTime?
  estimatedComplete DateTime?
  
  // Receipt
  receivedAt        DateTime?
  documentId        String?  // Link to Document record
  document          Document? @relation(fields: [documentId], references: [id])
  
  // Cost tracking
  cost              Float?
  invoiceId         String?
  
  // AI Analysis (Phase 7)
  aiAnalyzedAt      DateTime?
  aiFlags           Json?
  
  createdAt         DateTime @default(now())
  updatedAt         DateTime @updatedAt
}

// Diligence Item
model DiligenceItem {
  id                String   @id @default(uuid())
  dealId            String
  deal              Deal     @relation(fields: [dealId], references: [id])
  
  category          DiligenceCategory
  documentType      String
  displayName       String
  
  // Status
  status            DiligenceStatus // required, on_file, received, rejected, waived
  isRequired        Boolean  @default(true)
  
  // Source
  source            DiligenceSource // borrower, third_party, title, internal
  
  // Linked document
  documentId        String?
  document          Document? @relation(fields: [documentId], references: [id])
  
  // For existing clients
  onFileFrom        String?  // Reference to prior deal
  
  // Rejection
  rejectedAt        DateTime?
  rejectionReason   String?
  rejectionNotes    String?
  
  // Waiver
  waivedAt          DateTime?
  waivedBy          String?
  waiverReason      String?
  
  createdAt         DateTime @default(now())
  updatedAt         DateTime @updatedAt
}

// Document (extended)
model Document {
  id                String   @id @default(uuid())
  dealId            String
  deal              Deal     @relation(fields: [dealId], references: [id])
  
  // Classification
  category          DocumentCategory
  documentType      String
  
  // File info
  filename          String
  originalFilename  String
  fileUrl           String   // Google Drive URL
  fileSize          Int
  mimeType          String
  
  // Versioning
  version           Int      @default(1)
  previousVersionId String?
  isCurrentVersion  Boolean  @default(true)
  
  // Upload tracking
  uploadedAt        DateTime @default(now())
  uploadMethod      UploadMethod // drag_drop, email, whatsapp, api, direct
  uploadedBy        String?  // User ID or "borrower" or "system"
  sourceEmail       String?  // If from email
  
  // AI Classification
  aiClassification  String?
  aiConfidence      Float?
  aiExtractedData   Json?
  
  // Review status
  reviewStatus      ReviewStatus // pending, approved, rejected
  reviewedAt        DateTime?
  reviewedBy        String?
  rejectionReason   String?
  rejectionNotes    String?
  
  // Expiration
  expirationDate    DateTime?
  expirationAlertSent Boolean @default(false)
  
  // Analysis flags (Phase 7)
  aiAnalyzed        Boolean  @default(false)
  flags             Json?    // Red/green flags
  
  createdAt         DateTime @default(now())
  updatedAt         DateTime @updatedAt
}

// Upload Link
model UploadLink {
  id                String   @id @default(uuid())
  dealId            String   @unique
  deal              Deal     @relation(fields: [dealId], references: [id])
  
  token             String   @unique
  expiresAt         DateTime?
  isActive          Boolean  @default(true)
  
  // Usage tracking
  uploadCount       Int      @default(0)
  lastUsedAt        DateTime?
  
  createdAt         DateTime @default(now())
}

// Enums
enum ReportType {
  credit
  background_individual
  background_entity
  appraisal
  title
  flood
  feasibility
  collateral_desktop
  insurance
}

enum ReportStatus {
  pending_order
  ordered
  assigned
  scheduled
  in_progress
  received
  reviewed
  approved
  revision_needed
  cancelled
}

enum DiligenceStatus {
  required
  on_file
  requested
  received
  rejected
  waived
}

enum ReviewStatus {
  pending
  approved
  rejected
}

enum UploadMethod {
  drag_drop
  email
  whatsapp
  api
  direct
}
```

### 5.3 External Integrations

| Service | Purpose | Priority |
|---------|---------|----------|
| Single Source API | Appraisal, Title, Flood, Feasibility, CDA | High |
| CRS API | Credit, Background | High |
| Google Drive API | Document storage | High |
| Gmail/IMAP | Email ingestion | High |
| SendGrid | Outbound emails | High |
| OCR Service | Document text extraction | High |
| LLM API | Document classification | High |

### 5.4 Background Jobs

| Job | Frequency | Purpose |
|-----|-----------|---------|
| `check-report-status` | Every 15 min | Poll Single Source/CRS for updates |
| `process-incoming-email` | Every 5 min | Parse underwriting@usdvcapital.com |
| `check-document-expiration` | Daily | Flag expiring documents |
| `send-diligence-reminders` | Daily | Send automated reminders |
| `sync-google-drive` | Every 10 min | Ensure Drive sync |

---

## 6. Notifications

### 6.1 Borrower Notifications

| Event | Channel | Template |
|-------|---------|----------|
| Diligence Request Sent | Email | Full checklist with upload link |
| Document Received | Email | Confirmation of receipt |
| Document Rejected | Email | Rejection reason + re-upload instructions |
| Reminder (Day 2) | Email | Outstanding items list |
| Reminder (Day 4) | Email + SMS | Urgent - items needed |
| All Docs Complete | Email | Thank you + next steps |

### 6.2 Internal Notifications

| Event | Channel | Recipients |
|-------|---------|------------|
| Report Ordered | Roam | Processor |
| Report Received | Email, Roam | Processor, Underwriter |
| Report Issue | Email, Roam | Processor, LO |
| Document Uploaded | In-app | Processor |
| Low Confidence Classification | In-app, Roam | Processor |
| Document Rejected | Roam | LO |
| All Diligence Complete | Email, Roam | Processor, Underwriter, LO |
| Document Expiring | Email | Processor |

---

## 7. Security Requirements

- Upload links use secure tokens (UUID + HMAC signature)
- Tokens validated server-side on every upload
- Documents scanned for malware before processing
- PII documents (SSN, DL) encrypted at rest
- Access logging for all document views
- Google Drive permissions restricted to USDV service account

---

## 8. Testing Requirements

### 8.1 Integration Tests

- Single Source API order/receive flow
- CRS API credit pull flow
- Email ingestion pipeline
- Google Drive sync
- Document classification accuracy

### 8.2 E2E Tests

1. Deposit paid → All reports auto-ordered
2. Report received via webhook → Filed correctly
3. Email with attachments → Parsed and filed
4. Drag-drop upload → Classified and filed
5. Document rejection → Borrower notified → Re-upload

### 8.3 Load Tests

- Concurrent uploads (10+ files)
- Email parsing throughput
- Classification API response time

---

## 9. Dependencies

| Dependency | Status | Notes |
|------------|--------|-------|
| Phase 4 Complete | Required | Term sheet + deposit triggers Phase 5 |
| Single Source API Docs | Needed | For integration |
| CRS API Docs | Needed | For integration |
| Google Drive Setup | Needed | Service account + folder structure |
| OCR Service Selection | Needed | For document text extraction |
| Email Monitoring Setup | Needed | underwriting@usdvcapital.com access |

---

## 10. Launch Checklist

- [ ] Single Source API integration tested
- [ ] CRS API integration tested
- [ ] Email parsing pipeline working
- [ ] Google Drive folder structure created
- [ ] Upload link generation working
- [ ] Document classification trained/tested
- [ ] Diligence checklist logic complete
- [ ] Reminder automation configured
- [ ] Rejection flow working
- [ ] All email templates created
- [ ] Webhook endpoints secured
- [ ] Background jobs scheduled
- [ ] UAT sign-off

---

*End of Phase 5-6 PRD*
