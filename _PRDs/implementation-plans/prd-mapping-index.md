# INSPIRE PRD to Implementation Plan Mapping Index

**Document Version:** 1.0  
**Last Updated:** December 2024  
**Purpose:** Cross-reference between PRD sections and implementation plan sections

---

## 1. Quick Reference

| PRD | Implementation Plan | Pages | Key Features |
|-----|---------------------|-------|--------------|
| Phase 1-2 | `phase-1-2-implementation.md` | P1-01 to P2-01 | Quick App, Full Application |
| Phase 3-4 | `phase-3-4-implementation.md` | P3-01 to P4-04 | Sizing, Quotes, Term Sheet |
| Phase 5-6 | `phase-5-6-implementation.md` | P5-01 to P6-04 | Reports, Diligence Chase |
| Phase 7 | `phase-7-implementation.md` | P7-01 to P7-06 | AI Analysis, Credit Memo |
| Phase 8 | `phase-8-implementation.md` | P8-01 to P8-08 | Pipeline, Dashboard, Tasks |

---

## 2. Phase 1-2: Intake & Full Application

### PRD Section → Implementation Mapping

| PRD Section | PRD Title | Impl Section | Impl Page |
|-------------|-----------|--------------|-----------|
| 2.1 | Quick App Overview | 3.1 | P1-01 |
| 2.2 | Quick App User Flow | 3.1.2 | P1-01 |
| 2.3 | Quick App Form Fields | 3.1.3, 3.1.4 | P1-01 |
| 2.4 | Pre-Qualification Logic | 3.1.5 | P1-01 |
| 2.5 | Pre-Qualification Results | 3.1.6 | P1-01 |
| 3.1 | Full App Overview | 3.2 | P2-01 |
| 3.2 | Full App User Flow | 3.2.2 | P2-01 |
| 3.3 | Borrower Section | 3.2.3 | P2-01 |
| 3.4 | Guarantor Section | 3.2.3 | P2-01 |
| 3.5 | Property Section | 3.2.3 | P2-01 |
| 3.6 | Loan Details Section | 3.2.3 | P2-01 |
| 3.7 | Experience Section | 3.2.3 | P2-01 |
| 3.8 | Declarations Section | 3.2.3 | P2-01 |
| 3.9 | Document Upload | 3.2.3 | P2-01 |
| 4.1 | Application States | 3.2.4 | P2-01 |
| 4.2 | Save & Resume | 3.2.5 | P2-01 |
| 5.1 | Technical Requirements | 5 | API Contract |
| 5.2 | Data Models | 4 | Data Requirements |
| 5.3 | API Endpoints | 5 | API Contract |

### Key Data Types

| PRD Reference | Implementation Type | Location |
|---------------|---------------------|----------|
| Quick App Form | `QuickAppFormData` | 3.1.3 |
| Pre-Qual Result | `PreQualificationResult` | 3.1.5 |
| Full App Data | `FullApplicationData` | 3.2.3 |
| Borrower | `Borrower` | 4.1 |
| Guarantor | `Guarantor` | 4.2 |
| Property | `Property` | 4.3 |

---

## 3. Phase 3-4: Deal Sizing & Quote Generation

### PRD Section → Implementation Mapping

| PRD Section | PRD Title | Impl Section | Impl Page |
|-------------|-----------|--------------|-----------|
| 2.1 | Deal Sizing Overview | 3.1 | P3-01 |
| 2.2 | RTL Sizer Logic | 3.1.4 | P3-01 |
| 2.3 | DSCR Sizer Logic | 3.1.5 | P3-01 |
| 2.4 | Leverage Limits | 3.1.6 | P3-01 |
| 2.5 | Pricing Calculations | 3.1.7 | P3-01 |
| 2.6 | Sizer Output Structure | 3.1.8 | P3-01 |
| 2.7 | Sizer UI | 3.1.3 | P3-01 |
| 3.1 | Quote Generation Overview | 3.2 | P4-01 |
| 3.2 | Quote Scenarios | 3.2.4 | P4-01 |
| 3.3 | Quote Data Structure | 3.2.5 | P4-01 |
| 3.4 | Quote Presentation UI | 3.2.3 | P4-01 |
| 3.5 | Quote Selection Flow | 3.3 | P4-02 |
| 3.6 | Quote Expiration | 3.2.6 | P4-01 |
| 4.1 | Term Sheet Generation | 3.4 | P4-03 |
| 4.2 | Term Sheet Data Mapping | 3.4.4 | P4-03 |
| 4.3 | E-Signature (Dropbox Sign) | 3.4.5 | P4-03 |
| 5.1 | Third-Party Deposit | 3.5 | P4-04 |
| 5.2 | Invoice Generation | 3.5.3 | P4-04 |
| 5.3 | Payment (Stripe) | 3.5.4 | P4-04 |

### Key Data Types

| PRD Reference | Implementation Type | Location |
|---------------|---------------------|----------|
| RTL Sizer Output | `RTLSizerOutput` | 3.1.4 |
| DSCR Sizer Output | `DSCRSizerOutput` | 3.1.5 |
| Quote Scenario | `QuoteScenario` | 3.2.4 |
| Term Sheet | `TermSheet` | 3.4.4 |
| Deposit Invoice | `DepositInvoice` | 3.5.3 |

### External Integrations

| PRD Reference | Integration | Impl Section |
|---------------|-------------|--------------|
| 4.3 | Dropbox Sign | 4.1 |
| 5.3 | Stripe | 4.2 |

---

## 4. Phase 5-6: Third-Party Reports & Diligence Chase

### PRD Section → Implementation Mapping

| PRD Section | PRD Title | Impl Section | Impl Page |
|-------------|-----------|--------------|-----------|
| 3.1 | Reports Overview | 3.1 | P5-01 |
| 3.2 | Credit Report | 3.1.5 | P5-01 |
| 3.3 | Background Check | 3.1.5 | P5-01 |
| 3.4 | Appraisal | 3.1.5 | P5-01 |
| 3.5 | Title Report | 3.1.5 | P5-01 |
| 3.6 | Flood Determination | 3.1.5 | P5-01 |
| 3.7 | Feasibility Study | 3.1.5 | P5-01 |
| 3.8 | Insurance Quote | 3.1.5 | P5-01 |
| 3.9 | Report Status Tracking | 3.1.4 | P5-01 |
| 4.1 | Diligence Overview | 3.2 | P6-01 |
| 4.2 | Checklist Generation | 3.2.5 | P6-01 |
| 4.3 | Client Type Logic | 3.2.5 | P6-01 |
| 4.4 | Loan Type Logic | 3.2.5 | P6-01 |
| 4.5 | Document Upload (Borrower) | 3.3 | P6-02 |
| 4.5.1 | Drag-Drop Upload | 3.3.2 | P6-02 |
| 4.6 | AI Document Classification | 4 | Classification |
| 4.7 | Document Review Queue | 3.4 | P6-03 |
| 4.8 | Document Versioning | 3.4.3 | P6-03 |
| 4.9 | Expiration Tracking | 3.2.4 | P6-01 |
| 4.10 | Rejection Flow | 3.4.3 | P6-03 |
| 4.11 | Data Room | 3.5 | P6-04 |

### Key Data Types

| PRD Reference | Implementation Type | Location |
|---------------|---------------------|----------|
| Third-Party Report | `ThirdPartyReport` | 3.1.4 |
| Report Type | `ReportType` | 3.1.4 |
| Report Status | `ReportStatus` | 3.1.4 |
| Diligence Item | `DiligenceItem` | 3.2.4 |
| Document for Review | `DocumentForReview` | 3.4.3 |
| Classification Result | `ClassificationResult` | 4.3 |

### External Integrations

| PRD Reference | Integration | Impl Section |
|---------------|-------------|--------------|
| 3.2-3.3 | CRS API | 5.2 |
| 3.4-3.7 | Single Source API | 5.1 |
| 4.11 | Google Drive | 5 |
| 4.6 | LLM (Claude/GPT) | 4 |

---

## 5. Phase 7: AI Analysis & Credit Memo

### PRD Section → Implementation Mapping

| PRD Section | PRD Title | Impl Section | Impl Page |
|-------------|-----------|--------------|-----------|
| 3.1 | Analysis Overview | 3.1 | P7-01 |
| 3.2 | Analysis Pipeline | 4.1 | Analysis Pipeline |
| 3.3 | Credit Report Analysis | 4.1 | Analysis Rules |
| 3.4 | Background Analysis | 4.1 | Analysis Rules |
| 3.5 | Appraisal Analysis | 4.1 | Analysis Rules |
| 3.6 | Title Analysis | 4.1 | Analysis Rules |
| 3.7 | Insurance Analysis | 4.1 | Analysis Rules |
| 3.8 | Lease Analysis | 4.1 | Analysis Rules |
| 3.9 | Bank Statement Analysis | 4.1 | Analysis Rules |
| 4.1 | Flag System Overview | 3.2 | P7-03 |
| 4.2 | Flag Types | 3.2.3 | P7-03 |
| 4.3 | Flag Data Structure | 3.1.4 | P7-01 |
| 4.4 | Flag Display | 3.2.3 | P7-03 |
| 5.1 | Exception Overview | 3.3 | P7-04 |
| 5.2 | Exception Request | 3.3.3 | P7-04 |
| 5.3 | Compensating Factors | 3.3.3 | P7-04 |
| 5.4 | Exception Approval | 3.3.3 | P7-04 |
| 6.1 | Credit Memo Overview | 3.4 | P7-05 |
| 6.2 | Credit Memo Structure | 3.4.2 | P7-05 |
| 6.3 | Credit Memo Generation | 4.3 | Generation Prompt |
| 6.4 | Credit Memo Editor | 3.5 | P7-06 |
| 6.5 | Credit Memo Approval | 3.4.3 | P7-05 |
| 6.6 | Credit Memo Export | 3.4.3 | P7-05 |

### Key Data Types

| PRD Reference | Implementation Type | Location |
|---------------|---------------------|----------|
| Analysis Summary | `AnalysisSummary` | 3.1.4 |
| Document Analysis | `DocumentAnalysis` | 3.1.4 |
| Flag | `Flag` | 3.1.4 |
| Flag Severity | `FlagSeverity` | 3.1.4 |
| Exception | `Exception` | 3.3.3 |
| Credit Memo | `CreditMemo` | 3.4.2 |
| Executive Summary | `ExecutiveSummary` | 3.4.2 |
| Risk Assessment | `RiskAssessment` | 3.4.2 |

### External Integrations

| PRD Reference | Integration | Impl Section |
|---------------|-------------|--------------|
| 3.2, 6.3 | LLM (Claude/GPT) | 4 |

---

## 6. Phase 8: Operational Command Center

### PRD Section → Implementation Mapping

| PRD Section | PRD Title | Impl Section | Impl Page |
|-------------|-----------|--------------|-----------|
| 3.1 | Pipeline Overview | 3.2 | P8-02 |
| 3.2 | Pipeline Stages | 3.2.2 | P8-02 |
| 3.3 | Deal Card Design | 3.2.4 | P8-02 |
| 3.4 | Drag-Drop Rules | 3.2.5 | P8-02 |
| 3.5 | Pipeline Filters | 3.2.3 | P8-02 |
| 3.6 | Pipeline Sorting | 3.2.3 | P8-02 |
| 4.1 | Deal Dashboard Overview | 3.3 | P8-03 |
| 4.2 | Dashboard Header | 3.3.3 | P8-03 |
| 4.3 | Dashboard Tabs | 3.3.2 | P8-03 |
| 4.4 | Checklist Categories | 3.3.4 | P8-03 |
| 4.5 | Quick Actions | 3.3.5 | P8-03 |
| 5.1 | Home Dashboard Overview | 3.1 | P8-01 |
| 5.2 | KPIs | 3.1.4 | P8-01 |
| 5.3 | Needs Attention Logic | 3.1.5 | P8-01 |
| 5.4 | Tasks Due Today | 3.1.3 | P8-01 |
| 5.5 | Pipeline Overview | 3.1.3 | P8-01 |
| 5.6 | Recent Activity | 3.1.3 | P8-01 |
| 6.1 | Task Management | 3.4 | P8-04 |
| 6.2 | Task Structure | 3.4.3 | P8-04 |
| 6.3 | Task Categories | 3.4.3 | P8-04 |
| 6.4 | Quick Task Creation | 3.4.2 | P8-04 |
| 6.5 | Task Views | 3.4.2 | P8-04 |
| 7.1 | Activity Logging | 3.5 | P8-05 |
| 7.2 | Activity Structure | 3.5.3 | P8-05 |
| 7.3 | SLA Tracking | 4 | SLA Tracking |
| 7.4 | SLA Definitions | 4.1 | SLA Config |
| 7.5 | SLA Dashboard Widget | 4.2 | SLA Widget |
| 8.1 | Global Search | 3.6 | Global Search |
| 8.2 | Keyboard Shortcuts | 3.6.3 | Search Config |
| 9.1 | Notifications Overview | 3.7 | Notifications |
| 9.2 | In-App Notifications | 3.7.2 | P8-08 |
| 9.3 | Email Notifications | 3.7.3 | Notifications |
| 9.4 | SMS Notifications | 3.7.3 | Notifications |
| 9.5 | Notification Preferences | 3.7.3 | Notifications |

### Key Data Types

| PRD Reference | Implementation Type | Location |
|---------------|---------------------|----------|
| Pipeline Stage | `PipelineStage` | 3.2.2 |
| Deal Card Display | `DealCardDisplay` | 3.2.4 |
| Dashboard KPIs | `DashboardKPIs` | 3.1.4 |
| Needs Attention Item | `NeedsAttentionItem` | 3.1.4 |
| Task | `Task` | 3.4.3 |
| Activity | `Activity` | 3.5.3 |
| SLA Status | `SLAStatus` | 4.1 |
| Notification | `Notification` | 3.7.3 |
| Notification Preferences | `NotificationPreferences` | 3.7.3 |

---

## 7. Cross-Phase Features

### Shared Components (All Phases)

| Component | Used In Phases | Document |
|-----------|----------------|----------|
| NavigationShell | All | shared-components.md |
| DealHeader | 3-8 | shared-components.md |
| StatusBadge | All | shared-components.md |
| MetricCard | 3, 7, 8 | shared-components.md |
| DataTable | All | shared-components.md |
| FileUploader | 1-2, 5-6 | shared-components.md |
| ActivityFeed | 7, 8 | shared-components.md |
| TaskItem | 8 | shared-components.md |
| FlagIndicator | 7, 8 | shared-components.md |
| SLAIndicator | 8 | shared-components.md |

### Shared Data Types (All Phases)

| Type | Used In Phases | Document |
|------|----------------|----------|
| Deal | All | mock-data-catalog.md |
| Borrower | All | mock-data-catalog.md |
| Guarantor | 1-2, 7 | mock-data-catalog.md |
| Property | 1-2, 3-4, 7 | mock-data-catalog.md |
| Document | 5-7 | mock-data-catalog.md |
| User | All | mock-data-catalog.md |
| Activity | 7, 8 | mock-data-catalog.md |
| Task | 8 | mock-data-catalog.md |
| Notification | 8 | mock-data-catalog.md |

---

## 8. Implementation Dependencies

### Phase Dependencies

```
Phase 1-2 (Application)
    ↓
Phase 3-4 (Sizing & Quotes)
    ↓
Phase 5-6 (Reports & Diligence)
    ↓
Phase 7 (AI Analysis)
    ↓
Phase 8 (Command Center)
```

### Feature Dependencies Within Phases

| Feature | Depends On |
|---------|------------|
| Pre-Qualification (1) | None |
| Full Application (2) | Quick App (1) |
| Deal Sizing (3) | Full Application (2) |
| Quote Generation (4) | Deal Sizing (3) |
| Term Sheet (4) | Quote Selection (4) |
| Deposit Collection (4) | Term Sheet Signed (4) |
| Report Ordering (5) | Deposit Received (4) |
| Diligence Chase (6) | Term Sheet Signed (4) |
| AI Analysis (7) | Documents Received (5-6) |
| Credit Memo (7) | AI Analysis (7) |
| Pipeline (8) | All phases |
| Dashboard (8) | All phases |

---

## 9. API Endpoint Index

### Phase 1-2 Endpoints

| Endpoint | Method | PRD Ref | Impl Ref |
|----------|--------|---------|----------|
| `/api/quick-app` | POST | 2.3 | 5.1 |
| `/api/quick-app/:id/prequal` | POST | 2.4 | 5.1 |
| `/api/applications` | POST | 3.1 | 5.2 |
| `/api/applications/:id` | GET/PUT | 3.1 | 5.2 |
| `/api/applications/:id/submit` | POST | 3.1 | 5.2 |

### Phase 3-4 Endpoints

| Endpoint | Method | PRD Ref | Impl Ref |
|----------|--------|---------|----------|
| `/api/deals/:id/sizing` | POST | 2.1 | 5.1 |
| `/api/deals/:id/quotes` | GET/POST | 3.1 | 5.2 |
| `/api/quotes/:id/select` | POST | 3.5 | 5.2 |
| `/api/deals/:id/term-sheet` | POST | 4.1 | 5.3 |
| `/api/term-sheets/:id/sign` | POST | 4.3 | 5.3 |
| `/api/deals/:id/deposit` | POST | 5.1 | 5.4 |
| `/api/deposits/:id/payment` | POST | 5.3 | 5.4 |

### Phase 5-6 Endpoints

| Endpoint | Method | PRD Ref | Impl Ref |
|----------|--------|---------|----------|
| `/api/deals/:id/reports` | GET | 3.1 | 7.1 |
| `/api/deals/:id/reports/order` | POST | 3.1 | 7.1 |
| `/api/deals/:id/diligence-checklist` | GET | 4.1 | 7.2 |
| `/api/deals/:id/diligence/send-request` | POST | 4.5 | 7.2 |
| `/api/upload/:dealId/:token` | POST | 4.5.1 | 7.3 |
| `/api/documents/:id/classify` | POST | 4.6 | 7.3 |
| `/api/documents/:id/reject` | POST | 4.10 | 7.3 |

### Phase 7 Endpoints

| Endpoint | Method | PRD Ref | Impl Ref |
|----------|--------|---------|----------|
| `/api/deals/:id/analysis` | GET | 3.1 | 5.1 |
| `/api/deals/:id/analysis/run` | POST | 3.2 | 5.1 |
| `/api/deals/:id/flags` | GET | 4.1 | 5.2 |
| `/api/flags/:id/resolve` | POST | 4.4 | 5.2 |
| `/api/flags/:id/exception` | POST | 5.1 | 5.2 |
| `/api/exceptions/:id/approve` | POST | 5.4 | 5.3 |
| `/api/deals/:id/credit-memo` | GET | 6.1 | 5.4 |
| `/api/deals/:id/credit-memo/generate` | POST | 6.3 | 5.4 |
| `/api/credit-memos/:id/approve` | POST | 6.5 | 5.4 |

### Phase 8 Endpoints

| Endpoint | Method | PRD Ref | Impl Ref |
|----------|--------|---------|----------|
| `/api/dashboard` | GET | 5.1 | 5.1 |
| `/api/pipeline` | GET | 3.1 | 5.2 |
| `/api/deals/:id/stage` | PUT | 3.4 | 5.2 |
| `/api/tasks` | GET/POST | 6.1 | 5.3 |
| `/api/tasks/:id` | PUT | 6.1 | 5.3 |
| `/api/tasks/:id/complete` | POST | 6.1 | 5.3 |
| `/api/activity` | GET | 7.1 | 5.4 |
| `/api/search` | GET | 8.1 | 5.5 |
| `/api/notifications` | GET | 9.1 | 5.6 |
| `/api/notifications/preferences` | GET/PUT | 9.5 | 5.6 |

---

## 10. External Integration Index

| Integration | Provider | Used In | PRD Ref | Impl Ref |
|-------------|----------|---------|---------|----------|
| E-Signature | Dropbox Sign | Phase 4 | 4.3 | P3-4: 4.1 |
| Payment | Stripe | Phase 4 | 5.3 | P3-4: 4.2 |
| Credit/Background | CRS | Phase 5 | 3.2-3.3 | P5-6: 5.2 |
| Appraisal/Title | Single Source | Phase 5 | 3.4-3.7 | P5-6: 5.1 |
| Document Storage | Google Drive | Phase 6 | 4.11 | P5-6: 5 |
| AI/LLM | Claude/GPT | Phase 6-7 | 4.6, 6.3 | P5-6: 4, P7: 4 |
| Address Autocomplete | Google Places | Phase 1-2 | 3.5 | P1-2: 4.2 |

---

## 11. Document Reference

### Implementation Plan Documents

| Document | Location | Content |
|----------|----------|---------|
| Phase 1-2 Implementation | `phase-1-2-implementation.md` | Quick App, Full Application |
| Phase 3-4 Implementation | `phase-3-4-implementation.md` | Sizing, Quotes, Term Sheet |
| Phase 5-6 Implementation | `phase-5-6-implementation.md` | Reports, Diligence |
| Phase 7 Implementation | `phase-7-implementation.md` | AI Analysis, Credit Memo |
| Phase 8 Implementation | `phase-8-implementation.md` | Pipeline, Dashboard |
| Shared Components | `shared-components.md` | Reusable components |
| Mock Data Catalog | `mock-data-catalog.md` | Sample data |
| PRD Mapping Index | `prd-mapping-index.md` | This document |

### Source PRD Documents

| Document | Location |
|----------|----------|
| Phase 1-2 PRD | `_PRDs/inspire-phase-1-2-prd.md` |
| Phase 3-4 PRD | `_PRDs/inspire-phase-3-4-prd.md` |
| Phase 5-6 PRD | `_PRDs/inspire-phase-5-6-prd.md` |
| Phase 7 PRD | `_PRDs/inspire-phase-7-prd.md` |
| Phase 8 PRD | `_PRDs/inspire-phase-8-prd.md` |
| Master PRD | `_PRDs/inspire-master-prd.md` |

---

*End of PRD Mapping Index*

