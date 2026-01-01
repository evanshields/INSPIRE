# INSPIRE - Master Product Requirements Document

**Product Name:** INSPIRE  
**Company:** USDV Capital  
**Document Type:** Master PRD  
**Version:** 1.0  
**Last Updated:** November 2025

---

## 1. Executive Summary

INSPIRE is a next-generation loan origination system (LOS) purpose-built for single-family business purpose lending. The platform consolidates the entire loan lifecycle—from lead intake through funding—into a unified, AI-powered experience that replaces fragmented manual processes with intelligent automation.

---

## 2. Problem Statement

### Current Pain Points

**Process Fragmentation:**
- Loan origination managed across 10+ disconnected platforms (Google Drive, email, WhatsApp, HubSpot, GoHighLevel, Zoom, Excel, etc.)
- No single source of truth for deal status, documents, or communications

**Manual, Time-Intensive Workflows:**
- Deal sizing performed manually in Excel
- Third-party reports ordered individually via portals and emails
- Each report manually reviewed for red flags
- Diligence items collected via email and WhatsApp with no unified storage
- Repeat borrower data re-collected instead of leveraged

**Lack of Intelligence:**
- No automated analysis against underwriting guidelines
- No proactive identification of deal exceptions
- No automated document classification or filing

**Operational Inefficiency:**
- High labor cost per loan
- Extended time-to-close
- Error-prone manual data entry
- Limited scalability

---

## 3. Solution Overview

INSPIRE addresses these challenges through:

1. **Unified Platform:** Single system replacing HubSpot, GoHighLevel, and manual processes
2. **Intelligent Automation:** AI-powered document analysis, classification, and filing
3. **Streamlined Borrower Experience:** Digital applications, quote selection, and document upload
4. **Integrated Third-Party Ordering:** API connections to key vendors (Single Source, CRS)
5. **Smart Data Room:** Automated document ingestion from email and drag-drop interfaces
6. **Real-Time Analysis:** Continuous review against USDV underwriting guidelines with red/green flag alerts
7. **Automated Credit Memos:** AI-generated deal packages with exception identification
8. **Pipeline Visibility:** Kanban-style deal tracking with per-deal closing dashboards

---

## 4. Loan Products Supported

| Loan Type | Description | Typical Timeline |
|-----------|-------------|------------------|
| Fix & Flip | Short-term financing for property renovation and resale | 2-3 weeks to close |
| Ground-Up Construction | Financing for new construction on vacant or tear-down lots | 2-3 weeks to close |
| DSCR Permanent | Long-term rental property financing based on debt service coverage ratio | 4-6 weeks to close |

**Note:** BRRRR strategy loans are NOT supported.

---

## 5. User Roles

### MVP (Full Access)
All internal USDV Capital team members with @usdvcapital.com email domain:

| Role | Description |
|------|-------------|
| C-Suite / Executives | Strategic oversight, exception approvals, fund release authorization |
| Loan Officers | Borrower relationships, deal origination, quote presentation |
| Processors | Diligence collection, document management, third-party coordination |
| Underwriters | Deal analysis, credit memo review, investor submission |
| Admin | System configuration, user management, audit access |

### Post-MVP Additions
- **Borrowers:** Limited portal access (deal status, document upload, outstanding items)
- **Ambassador Partners:** Referral tracking, deal submission, commission visibility

### Authentication
- Domain-based: @usdvcapital.com email grants automatic internal access
- OAuth support (Gmail) for streamlined login
- Email/password fallback option

---

## 6. Phase Overview

| Phase | Name | Description |
|-------|------|-------------|
| 1 | Intake / Pre-Qual | Quick App for new clients; streamlined entry for existing clients |
| 2 | Full Application | Digital loan application by product type with smart pre-fill |
| 3 | Deal Sizing | Automated population of RTL/DSCR sizers; LTV, rate, points, YSP calculation |
| 4 | Quote & Term Sheet | Multi-option quote presentation; borrower selection; auto-generated term sheet with e-sign; third-party deposit collection |
| 5 | Third-Party Reports | Automated ordering via API/email; auto-ingestion to deal data room |
| 6 | Diligence Chase | Smart diligence request lists; intelligent data room with drag-drop and email ingest; AI document classification |
| 7 | AI Analysis & Credit Memo | Real-time document review; red/green flag alerts; automated credit memo generation; exception identification |
| 8 | Pipeline & Closing | Kanban pipeline; per-deal closing dashboard/checklist; status tracking through funding |
| 9 | WhatsApp Integration | AI participant in borrower chats; automatic message logging and document extraction |

---

## 7. Tech Stack (Recommended)

### Frontend
- **Framework:** Next.js (React)
- **Styling:** Tailwind CSS
- **UI Components:** shadcn/ui or similar component library
- **Forms:** React Hook Form with Zod validation

### Backend
- **Runtime:** Node.js
- **Framework:** Next.js API routes or separate Express/Fastify service
- **Database:** PostgreSQL (relational data) + vector database for AI embeddings
- **ORM:** Prisma

### AI/ML Layer
- **LLM:** Claude API (document analysis, classification, memo generation)
- **Document Processing:** OCR integration for scanned documents
- **Embeddings:** For semantic search across documents and communications

### Infrastructure
- **Hosting:** Vercel (frontend) + AWS/GCP (backend services)
- **File Storage:** Google Drive API integration (primary) + S3 (backup/archival)
- **Email:** SendGrid or AWS SES (transactional email)
- **E-Signature:** DocuSign or PandaDoc API

### Integrations
- **Third-Party Reports:** Single Source API, CRS API
- **Payments:** Stripe (third-party deposit collection)
- **Communication:** WhatsApp Business API, Twilio (SMS)
- **Notifications:** Roam API, email, in-app

---

## 8. Shared Components

### 8.1 Authentication & Authorization
- Domain-based auto-authentication (@usdvcapital.com)
- OAuth 2.0 (Google)
- Email/password with secure password requirements
- Session management with JWT
- Future: Role-based permissions matrix

### 8.2 Notification System
- Multi-channel: Email (default), SMS, push, in-app
- User-configurable preferences
- Roam integration for team alerts
- Notification types:
  - Deal status changes
  - Document received/flagged
  - Task assignments
  - Deadline reminders
  - Borrower auto-reminders

### 8.3 Document Management Engine
- Unified ingestion (email parsing, drag-drop, direct upload, WhatsApp extraction)
- AI-powered classification against diligence checklist
- Automatic naming convention with date stamps
- Version control (v1, v2 or date-based)
- Expiration tracking with alerts
- Google Drive sync as primary storage

### 8.4 Global Search
- Search across deals, borrowers, properties, documents
- Filters: loan type, status, date range, investor, assigned user
- Full-text search within documents

### 8.5 Activity Logging & Audit Trail
- Every action logged (user, action, timestamp, affected record)
- Admin-accessible audit reports
- Compliance-ready export

### 8.6 Task Management
- Per-deal task creation and assignment
- Due dates and reminders
- Monday.com-style workflow tracking
- Bulk operations support

---

## 9. Core Data Models

### 9.1 Borrower / Sponsor
```
Borrower {
  id
  fullName
  email
  phone
  ssn (encrypted)
  dateOfBirth
  citizenship
  creditScore
  address
  driversLicense
  passport
  greenCard
  experienceMetrics {
    totalDeals
    dealsLast12Months
    dealsLast36Months
    propertiesOwned
  }
  personalFinancialStatement
  scheduleOfRealEstateOwned
  backgroundCheckStatus
  creditReportStatus
  isExistingClient
  isRealEstateCFOClient
  createdAt
  updatedAt
}
```

### 9.2 Entity
```
Entity {
  id
  name
  type (LLC, LP, Corp, Other)
  ein (encrypted)
  statesRegistered[]
  articlesOfOrganization
  articlesOfIncorporation
  operatingAgreement
  bylaws
  certificateOfGoodStanding
  einLetter
  w9
  owners[] {
    borrowerId
    ownershipPercentage
  }
  parentEntityId (for nested structures)
  createdAt
  updatedAt
}
```

### 9.3 Deal
```
Deal {
  id
  status (prospect, application, quote, initial_uw, processing, underwriting, closed, funded, archived)
  loanType (fix_flip, ground_up, dscr)
  borrowerId
  entityId
  coGuarantors[]
  propertyId
  investor (eastview, archwest, other)
  loanAmount
  interestRate
  ltv / ltc
  originationPoints
  ysp
  prepaymentStructure
  termSheetId
  quoteSelectedAt
  termSheetSignedAt
  depositPaidAt
  targetCloseDate
  actualCloseDate
  fundedDate
  assignedLoanOfficer
  assignedProcessor
  assignedUnderwriter
  notes[]
  tasks[]
  activityLog[]
  createdAt
  updatedAt
}
```

### 9.4 Property
```
Property {
  id
  address
  propertyType (single_family, commercial)
  commercialType (multifamily, hospitality, retail, office, industrial, mixed_use)
  bedrooms
  bathrooms
  squareFootage
  landOwned (boolean)
  purchasePrice
  currentMarketValue
  rehabBudget
  constructionBudget
  arv (afterRepairValue)
  projectedRent
  projectedExpenses {
    hoa
    taxes
    insurance
  }
  occupancyStatus
  permitStatus
  createdAt
  updatedAt
}
```

### 9.5 Document
```
Document {
  id
  dealId
  category (borrower, property, closing, third_party)
  type (articles_of_org, bank_statement, appraisal, title_commitment, etc.)
  fileName
  fileUrl (Google Drive)
  version
  uploadedAt
  uploadMethod (email, drag_drop, whatsapp, direct)
  aiClassification
  aiConfidenceScore
  reviewStatus (pending, approved, rejected)
  rejectionReason
  expirationDate
  isExpired
  flags[] (red_flag, green_flag)
  flagDetails
}
```

### 9.6 Quote
```
Quote {
  id
  dealId
  loanAmount
  interestRate
  ltv
  prepaymentStructure
  prepaymentType (step_down, level)
  prepaymentYears
  amortization (interest_only, amortizing)
  interestOnlyPeriod
  originationPoints
  ysp
  cashOut (boolean)
  cashOutAmount
  expiresAt
  selectedAt
  createdAt
}
```

### 9.7 Term Sheet
```
TermSheet {
  id
  dealId
  quoteId
  documentUrl
  sentAt
  signedAt
  signatureUrl
  expiresAt (2 business days default)
}
```

### 9.8 Third-Party Report
```
ThirdPartyReport {
  id
  dealId
  reportType (appraisal, title, flood, feasibility, collateral_desktop, credit, background, insurance)
  provider (single_source, marketwise, crs, exactus, trinity, first_choice)
  orderedAt
  receivedAt
  documentId
  status (ordered, received, reviewed)
  aiAnalysis
  flags[]
  cost
}
```

---

## 10. Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        BORROWER TOUCHPOINTS                      │
├─────────────────┬─────────────────┬─────────────────────────────┤
│   Quick App     │   Full App      │   Drag-Drop Upload Link     │
│   (Public)      │   (Auth/Public) │   (Public, per-deal)        │
└────────┬────────┴────────┬────────┴──────────────┬──────────────┘
         │                 │                       │
         ▼                 ▼                       ▼
┌─────────────────────────────────────────────────────────────────┐
│                         INSPIRE CORE                             │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐  │
│  │   Next.js   │  │   AI/LLM    │  │   Integration Layer     │  │
│  │   Frontend  │  │   Engine    │  │   (APIs, Webhooks)      │  │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘  │
│                                                                  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐  │
│  │  PostgreSQL │  │   Google    │  │   Notification          │  │
│  │  Database   │  │   Drive     │  │   Service               │  │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
         │                 │                       │
         ▼                 ▼                       ▼
┌─────────────────────────────────────────────────────────────────┐
│                      EXTERNAL INTEGRATIONS                       │
├──────────┬──────────┬──────────┬──────────┬──────────┬──────────┤
│  Single  │   CRS/   │ DocuSign │  Stripe  │ WhatsApp │   Roam   │
│  Source  │  Exactus │          │          │ Business │          │
│   API    │   API    │   API    │   API    │   API    │   API    │
└──────────┴──────────┴──────────┴──────────┴──────────┴──────────┘
```

### Data Flow Summary

1. **Inbound:** Borrower submits Quick App → Full App → data stored in PostgreSQL
2. **Sizing:** Deal data auto-populates sizer logic → outputs stored on Deal record
3. **Quotes:** Multiple quotes generated → presented via web UI → selection triggers term sheet
4. **Documents:** Ingested via email/drag-drop/WhatsApp → AI classifies → stored in Google Drive → metadata in PostgreSQL
5. **Analysis:** AI continuously reviews documents against underwriting guidelines → flags stored → credit memo generated
6. **Pipeline:** All deals visible in Kanban → clicking into deal shows closing dashboard

---

## 11. External Integrations

| Integration | Purpose | Method | Priority |
|-------------|---------|--------|----------|
| Single Source | Appraisal, Title, Flood, Feasibility, Collateral Desktop | API | High |
| CRS | Credit (tri-merge), Background Checks | API | High |
| Exactus | Credit, Background (backup) | API/TBD | Medium |
| Marketwise | Appraisal (backup) | Portal | Low |
| Trinity | Feasibility (backup) | Email | Low |
| First Choice Insurance | Property, Builders Risk, GL policies | Email/TBD | Medium |
| Google Drive | Document storage, data room | API | High |
| DocuSign / PandaDoc | E-signatures | API | High |
| Stripe | Payment processing (deposits) | API | High |
| WhatsApp Business | Borrower communication, doc extraction | API | High |
| Roam | Team notifications | API | Medium |
| SendGrid / AWS SES | Transactional email | API | High |

---

## 12. Security & Compliance

### Data Protection
- **Encryption at Rest:** AES-256 for all stored data
- **Encryption in Transit:** TLS 1.3 for all connections
- **PII Handling:** SSN, EIN, financial data encrypted with separate key management
- **Access Logging:** All PII access logged with user, timestamp, action

### Authentication Security
- Secure password requirements (12+ characters, complexity rules)
- Session timeout after inactivity
- Future: MFA support

### Compliance Considerations
- FCRA compliance for credit authorization
- State-specific lending disclosures (as applicable)
- Data retention: 1 year post-funding, then automated reminder to retain or purge

### Audit Trail
- Every system action logged
- Admin-accessible audit reports
- Exportable for compliance reviews

---

## 13. UX Principles

### Borrower-Facing
- Progress indicators on all multi-step forms
- Auto-save (never lose work)
- Mobile-optimized (responsive design)
- Clear validation with helpful error messages
- Confirmation screens after key actions

### Internal Team
- **Home Dashboard:** Deals needing attention, tasks due, alerts, KPIs
- **Quick Actions:** One-click common tasks
- **Bulk Operations:** Multi-select for status changes, exports
- **Keyboard Shortcuts:** Power user efficiency
- **Contextual Tooltips:** In-line help
- **Help Library:** Searchable documentation

### General
- Undo/confirmation for destructive actions
- Meaningful empty states with guidance
- Clear loading states during processing
- Minimal, clean UI - avoid clutter

---

## 14. Post-MVP Roadmap

| Feature | Description |
|---------|-------------|
| Borrower Portal | Logged-in borrower experience: deal status, doc upload, outstanding items |
| Communication Hub | Centralized log of all borrower communications across channels |
| Post-Close Servicing | Payment tracking, maturity dates, payoffs, extensions, modifications |
| Construction Draw Management | Draw schedules, inspections, disbursements for RTL loans |
| Investor Loan Tape & Reporting | Automated loan tape generation for Eastview, ArchWest, etc. |
| Renewal Pipeline | Proactive tracking for repeat borrower opportunities |
| Analytics Dashboard | Pipeline velocity, conversion rates, time-to-close, revenue metrics |
| Real Estate CFO.ai Integration | Direct data pull for existing CFO clients |
| Ambassador Program Management | Referral tracking, commissions, partner performance |
| Role-Based Permissions | Granular access control by user role |

---

## 15. Success Metrics

| Metric | Target |
|--------|--------|
| Time to Close (RTL) | ≤ 3 weeks |
| Time to Close (DSCR) | ≤ 6 weeks |
| Application Completion Rate | > 80% |
| Document Auto-Classification Accuracy | > 95% |
| Manual Data Entry Reduction | > 70% |
| Platforms Replaced | HubSpot, GoHighLevel, Excel sizers |

---

## 16. Dependencies

| Dependency | Status | Notes |
|------------|--------|-------|
| USDV Underwriting Manual | In Progress | To be created in separate workstream |
| Eastview RTL Sizer | Pending Upload | Excel file for Phase 3 logic |
| Eastview DSCR Sizer | Pending Upload | Excel file for Phase 3 logic |
| Quote HTML Templates | Pending Upload | For Phase 4 presentation |
| Term Sheet Template | Pending Upload | For Phase 4 auto-generation |
| Single Source API Documentation | Needed | For Phase 5 integration |
| CRS API Documentation | Needed | For Phase 5 integration |
| WhatsApp Business API Access | Needed | Requires Meta approval |

---

## 17. Open Questions

1. **Complex Ownership Structures:** How should nested entities and cross-entity guarantors be modeled and displayed in the UI? (See Appendix A for proposed approach)
2. **Multi-Property Deals:** Should portfolio loans have a single deal record with multiple properties, or multiple linked deal records?
3. **Investor Selection:** At what phase is the investor (Eastview, ArchWest, other) selected? Does this affect sizing logic?
4. **Rate Lock Source:** Where does rate lock data come from? Investor rate sheets?
5. **White-Label Quotes:** Should quote pages be brandable for Ambassador partners?

---

## Appendix A: Complex Ownership Structure Modeling

### Proposed Approach

**Nested Entities:**
- Entity model includes optional `parentEntityId` field
- UI displays entity hierarchy as expandable tree
- Ownership percentages roll up through the chain

**Multiple Guarantors Across Entities:**
- Deal model includes `coGuarantors[]` array
- Each guarantor linked to their respective entity
- Guarantor can appear on multiple deals across different entities
- Credit/background checks linked to Borrower record, reusable across deals

**UI Representation:**
```
Deal: 123 Main St Fix & Flip
├── Borrowing Entity: Main Street Holdings LLC
│   ├── Owner: John Smith (60%) [Guarantor]
│   └── Owner: Jane Doe (40%) [Guarantor]
│       └── Member of: Doe Family Trust
│           └── Beneficiary: Jane Doe (100%)
└── Co-Guarantor: Robert Smith (not an owner, but guaranteeing)
    └── Member of: Smith Capital LLC (separate entity)
```

**Benefits:**
- Clear visibility into full ownership/guarantor structure
- Reusable borrower/entity data across deals
- Compliance-ready documentation of all parties

---

*End of Master PRD*
