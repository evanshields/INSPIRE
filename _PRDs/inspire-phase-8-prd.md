# INSPIRE - Phase 8 Product Requirements Document

**Product Name:** INSPIRE  
**Company:** USDV Capital  
**Document Type:** Phase 8 PRD (Pipeline & Closing Dashboard)  
**Version:** 1.0  
**Last Updated:** November 2025

---

## 1. Overview

Phase 8 is the operational command center of INSPIRE. It provides a unified view of all deals in the pipeline via a Kanban board, per-deal closing dashboards, task management, and KPI tracking. This is where the internal team manages day-to-day loan origination operations.

### Core Capabilities

1. **Kanban Pipeline** - Visual deal tracking across all stages
2. **Closing Dashboard** - Per-deal checklist and status management
3. **Home Dashboard** - KPIs, tasks, alerts, deals needing attention
4. **Task Management** - Assign, track, and complete tasks per deal
5. **Activity Logging** - Complete audit trail of all actions
6. **SLA Tracking** - Monitor time-to-close and phase durations
7. **Reporting** - Pipeline analytics and performance metrics

---

## 2. Goals & Success Metrics

### Goals

1. Provide complete pipeline visibility in one view
2. Eliminate spreadsheet-based deal tracking
3. Enable proactive management of at-risk deals
4. Track SLAs and identify bottlenecks
5. Support team collaboration with task assignment
6. Maintain complete audit trail for compliance

### Success Metrics

| Metric | Target |
|--------|--------|
| Pipeline load time | <2 seconds |
| Deals visible per view | All active deals |
| Task completion rate | >90% on-time |
| SLA compliance (RTL) | >85% within 3 weeks |
| SLA compliance (DSCR) | >85% within 6 weeks |
| User adoption | 100% of internal team |

---

## 3. Kanban Pipeline

### 3.1 Pipeline Stages

| Stage | Status Code | Description | Entry Trigger |
|-------|-------------|-------------|---------------|
| **Prospect** | `prospect` | Lead received, Quick App submitted | Quick App submission |
| **Application** | `application` | Full Application in progress or submitted | Qualified from Quick App |
| **Quote** | `quote` | Quotes presented, awaiting borrower selection | Full App submitted + Sized |
| **Initial UW** | `initial_uw` | Term sheet signed, deposit paid, reports ordering | Quote selected + Term sheet signed + Deposit paid |
| **Processing** | `processing` | Diligence collection in progress | All third-party reports ordered |
| **Underwriting** | `underwriting` | Package complete, under review, pending approval | All diligence received |
| **Closing** | `closing` | Approved, closing docs in progress | Credit memo approved + Exceptions cleared |
| **Funded** | `funded` | Loan closed and funded | Wire sent + Confirmation received |
| **Archived** | `archived` | Dead, declined, or withdrawn deals | Manual move or auto-archive after 90 days inactive |

### 3.2 Pipeline Board Layout

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│  INSPIRE PIPELINE                                           [+ New Deal]  [Filters ▼]   │
│  ─────────────────                                                                      │
│  View: [All] [My Deals] [RTL] [DSCR]    Sort: [Updated] [Close Date] [Amount]          │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                         │
│ PROSPECT    APPLICATION    QUOTE    INITIAL UW    PROCESSING    UW    CLOSING  FUNDED  │
│    (5)          (3)         (4)        (2)           (6)        (3)     (2)      (8)   │
│ ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐ ┌────────┐     │
│ │123 Main│  │456 Oak │  │789 Pine│  │321 Elm │  │654 Maple│  │987 Cedar│ │111 Birch│   │
│ │F&F     │  │DSCR    │  │GU Const│  │F&F     │  │DSCR     │  │F&F     │ │DSCR    │    │
│ │$425K   │  │$380K   │  │$1.2M   │  │$550K   │  │$290K    │  │$675K   │ │$420K   │    │
│ │J.Smith │  │M.Jones │  │R.Brown │  │A.Davis │  │S.Wilson │  │T.Moore │ │L.Taylor│    │
│ │🔴 2    │  │        │  │🟡 1    │  │        │  │🔴 1     │  │        │ │        │    │
│ │12/20   │  │12/22   │  │1/5     │  │12/18   │  │12/28    │  │12/15   │ │12/14   │    │
│ └────────┘  └────────┘  └────────┘  └────────┘  └────────┘  └────────┘ └────────┘     │
│ ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐ ┌────────┐     │
│ │...     │  │...     │  │...     │  │...     │  │...     │  │...     │ │...     │     │
│ └────────┘  └────────┘  └────────┘  └────────┘  └────────┘  └────────┘ └────────┘     │
│                                                                                         │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.3 Deal Card Design

Each card on the Kanban board displays:

```
┌────────────────────────────────┐
│ 🏠 123 Main Street             │  ← Property Address
│ Fix & Flip                     │  ← Loan Type
├────────────────────────────────┤
│ $425,000          75% LTV      │  ← Loan Amount, Key Metric
│ John Smith        Eastview     │  ← Borrower, Investor
├────────────────────────────────┤
│ 🔴 2 flags   📋 3 tasks        │  ← Red Flags, Open Tasks
│ 📅 Close: Dec 20               │  ← Target Close Date
│ 👤 Sarah (LO)                  │  ← Assigned LO
├────────────────────────────────┤
│ ⏱️ 5 days in stage             │  ← Time in current stage
│ [View] [Quick Actions ▼]       │  ← Action buttons
└────────────────────────────────┘
```

### 3.4 Card Color Coding

| Indicator | Meaning |
|-----------|---------|
| 🟢 Green border | On track, no issues |
| 🟡 Yellow border | Warning - approaching SLA or has yellow flags |
| 🔴 Red border | At risk - past SLA or has red flags |
| ⚫ Gray border | Stale - no activity in 7+ days |

### 3.5 Drag-and-Drop Rules

| From Stage | To Stage | Allowed? | Validation Required |
|------------|----------|----------|---------------------|
| Prospect | Application | ✅ | Pre-qualification passed |
| Application | Quote | ✅ | Full app complete + Sized |
| Quote | Initial UW | ✅ | Quote selected + Term sheet signed + Deposit paid |
| Initial UW | Processing | ✅ | All reports ordered |
| Processing | Underwriting | ✅ | Diligence checklist 100% |
| Underwriting | Closing | ✅ | Credit memo approved, no open red flags |
| Closing | Funded | ✅ | Wire confirmed |
| Any | Archived | ✅ | Manual confirmation |
| Archived | Any | ✅ | Manual reactivation |
| Skip stages | - | ❌ | Not allowed (sequential only) |
| Backward move | - | ⚠️ | Requires confirmation + reason |

### 3.6 Pipeline Filters

| Filter | Options |
|--------|---------|
| Loan Type | All, Fix & Flip, Ground-Up Construction, DSCR |
| Investor | All, Eastview, ArchWest, Other |
| Assigned LO | All, [User list] |
| Assigned Processor | All, [User list] |
| Flag Status | All, Has Red Flags, Has Yellow Flags, Clean |
| Date Range | All, This Week, This Month, Custom |
| Loan Amount | All, <$250K, $250K-$500K, $500K-$1M, >$1M |
| State | All, [State list] |
| SLA Status | All, On Track, At Risk, Past Due |

### 3.7 Pipeline Sorting

| Sort Option | Description |
|-------------|-------------|
| Last Updated | Most recent activity first |
| Target Close Date | Nearest close date first |
| Loan Amount | Highest first |
| Days in Stage | Longest first (identify stuck deals) |
| Created Date | Newest first |
| Borrower Name | Alphabetical |

---

## 4. Deal Closing Dashboard

### 4.1 Dashboard Access

Click any deal card → Opens full closing dashboard

### 4.2 Dashboard Layout

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│  ← Back to Pipeline                                                                     │
│                                                                                         │
│  123 MAIN STREET, MIAMI FL 33139                                          [Actions ▼]  │
│  Fix & Flip | $425,000 | 75% LTV | Eastview                                            │
│  Borrower: John Smith (Smith Investments LLC)                                          │
│  Status: PROCESSING                                                    Target: Dec 20  │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                         │
│  ┌─────────────────────────────────────────────────────────────────────────────────┐   │
│  │  PROGRESS                                                                        │   │
│  │  ═══════════════════════════════════════════════════════●═══════════            │   │
│  │  Prospect → App → Quote → Initial UW → Processing → UW → Closing → Funded      │   │
│  │                                           ▲                                      │   │
│  │                                        You are here                              │   │
│  └─────────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                         │
│  ┌──────────────────────────┐  ┌──────────────────────────┐  ┌──────────────────────┐  │
│  │  FLAGS                   │  │  TASKS                   │  │  TIMELINE            │  │
│  │  🟢 12  🟡 2  🔴 1       │  │  📋 3 open, 8 complete   │  │  📅 12 days to close │  │
│  │  [View All Flags]        │  │  [View Tasks]            │  │  ⏱️ 6 days in stage  │  │
│  └──────────────────────────┘  └──────────────────────────┘  └──────────────────────┘  │
│                                                                                         │
├───────────────────────────────────┬─────────────────────────────────────────────────────┤
│                                   │                                                     │
│  TABS: [Checklist] [Documents]    │  DEAL SUMMARY                                      │
│        [Analysis] [Activity]      │  ─────────────                                     │
│        [Notes] [Tasks]            │                                                     │
│                                   │  Loan Details                                       │
│  ┌────────────────────────────┐   │  • Amount: $425,000                                │
│  │  CLOSING CHECKLIST         │   │  • Rate: 11.5%                                     │
│  │  Progress: 78% (28/36)     │   │  • Term: 12 months                                 │
│  │                            │   │  • LTV: 75% | LTC: 85% | LTARV: 68%               │
│  │  BORROWER DOCS     [6/8]   │   │  • Points: 2.0 | YSP: 1.5                         │
│  │  ──────────────────        │   │                                                     │
│  │  ✅ Articles of Org        │   │  Property                                          │
│  │  ✅ Operating Agreement    │   │  • Type: Single Family                             │
│  │  ✅ Good Standing          │   │  • Size: 1,850 sf | 3 bed / 2 bath                │
│  │  ✅ EIN Letter             │   │  • Purchase: $340,000                              │
│  │  ✅ Bank Statements        │   │  • Rehab: $85,000                                  │
│  │  ✅ DL - John Smith        │   │  • ARV: $525,000                                   │
│  │  ❌ DL - Jane Smith        │   │                                                     │
│  │  ❌ Passport (if needed)   │   │  Borrower                                          │
│  │                            │   │  • Sponsor: John Smith                             │
│  │  PROPERTY DOCS     [5/6]   │   │  • Entity: Smith Investments LLC                   │
│  │  ──────────────────        │   │  • FICO: 720                                       │
│  │  ✅ Purchase Contract      │   │  • Experience: 8 deals                             │
│  │  ✅ Scope of Work          │   │                                                     │
│  │  ✅ Plans & Specs          │   │  Team                                              │
│  │  ✅ Permits                │   │  • LO: Sarah Johnson                               │
│  │  ✅ Contractor Agreement   │   │  • Processor: Mike Chen                            │
│  │  🔄 Payoff Letter          │   │  • Underwriter: Lisa Park                          │
│  │                            │   │                                                     │
│  │  THIRD-PARTY      [7/7]    │   │  Key Dates                                         │
│  │  ──────────────────        │   │  • App Submitted: Nov 28                           │
│  │  ✅ Credit Report          │   │  • Term Sheet: Dec 2                               │
│  │  ✅ Background Check       │   │  • Target Close: Dec 20                            │
│  │  ✅ Appraisal              │   │  • Rate Lock Expires: Dec 22                       │
│  │  ✅ Title Commitment       │   │                                                     │
│  │  ✅ Flood Cert             │   │                                                     │
│  │  ✅ Feasibility            │   │  [Edit Deal] [View Credit Memo]                    │
│  │  ✅ Insurance              │   │  [Generate Docs] [Send to Investor]                │
│  │                            │   │                                                     │
│  │  CLOSING DOCS      [2/5]   │   │                                                     │
│  │  ──────────────────        │   │                                                     │
│  │  ✅ Preliminary HUD        │   │                                                     │
│  │  ✅ CPL                    │   │                                                     │
│  │  ❌ Final HUD              │   │                                                     │
│  │  ❌ Wire Instructions      │   │                                                     │
│  │  ❌ Funding Confirmation   │   │                                                     │
│  │                            │   │                                                     │
│  └────────────────────────────┘   │                                                     │
│                                   │                                                     │
└───────────────────────────────────┴─────────────────────────────────────────────────────┘
```

### 4.3 Checklist Categories

**Category 1: Borrower Documents**
| Item | Required For | Status Options |
|------|--------------|----------------|
| Articles of Organization/Incorporation | All | ✅ ❌ 🔄 N/A |
| Operating Agreement / Bylaws | All | ✅ ❌ 🔄 N/A |
| Certificate of Good Standing | All | ✅ ❌ 🔄 ⚠️ Expiring |
| EIN Letter or W-9 | All | ✅ ❌ 🔄 N/A |
| Bank Statements (2 months) | All | ✅ ❌ 🔄 ⚠️ Expiring |
| Driver's License (per guarantor) | All | ✅ ❌ 🔄 N/A |
| Passport / Green Card | If applicable | ✅ ❌ 🔄 N/A |
| PFS / SREO | All | ✅ ❌ 🔄 N/A |

**Category 2: Property Documents**
| Item | Required For | Status Options |
|------|--------------|----------------|
| Purchase Contract / PSA | Purchase | ✅ ❌ 🔄 N/A |
| Scope of Work / Budget | RTL | ✅ ❌ 🔄 N/A |
| Plans & Specifications | Ground-Up | ✅ ❌ 🔄 N/A |
| Permits | RTL (if required) | ✅ ❌ 🔄 N/A |
| Contractor Agreement | RTL (if 3rd party GC) | ✅ ❌ 🔄 N/A |
| Payoff Letter / VOM | Refinance | ✅ ❌ 🔄 N/A |
| Lease Agreement | DSCR | ✅ ❌ 🔄 N/A |
| Rent Payment Proof | DSCR | ✅ ❌ 🔄 N/A |
| Security Deposit Proof | DSCR | ✅ ❌ 🔄 N/A |

**Category 3: Third-Party Reports**
| Item | Required For | Status Options |
|------|--------------|----------------|
| Credit Report | All | ✅ ❌ 🔄 ⚠️ Expiring |
| Background Check | All | ✅ ❌ 🔄 N/A |
| Appraisal | All | ✅ ❌ 🔄 ⚠️ Expiring |
| Title Commitment | All | ✅ ❌ 🔄 N/A |
| Flood Determination | All | ✅ ❌ 🔄 N/A |
| Feasibility Study | RTL | ✅ ❌ 🔄 N/A |
| Collateral Desktop Analysis | DSCR | ✅ ❌ 🔄 N/A |
| Insurance Certificate | All | ✅ ❌ 🔄 ⚠️ Expiring |

**Category 4: Closing Documents**
| Item | Required For | Status Options |
|------|--------------|----------------|
| Preliminary HUD | All | ✅ ❌ 🔄 N/A |
| Closing Protection Letter | All | ✅ ❌ 🔄 N/A |
| Escrow Instructions | All | ✅ ❌ 🔄 N/A |
| Final HUD | All | ✅ ❌ 🔄 N/A |
| Wire Instructions | All | ✅ ❌ 🔄 N/A |
| Note | All | ✅ ❌ 🔄 N/A |
| Deed of Trust / Mortgage | All | ✅ ❌ 🔄 N/A |
| Loan Agreement | All | ✅ ❌ 🔄 N/A |
| Guarantee | All | ✅ ❌ 🔄 N/A |
| Business Purpose Affidavit | All | ✅ ❌ 🔄 N/A |
| Funding Confirmation | All | ✅ ❌ 🔄 N/A |

**Category 5: Internal Items**
| Item | Required For | Status Options |
|------|--------------|----------------|
| Credit Memo | All | ✅ ❌ 🔄 N/A |
| Exception Approvals | If needed | ✅ ❌ 🔄 N/A |
| Investor Approval | All | ✅ ❌ 🔄 N/A |
| Rate Lock Confirmation | All | ✅ ❌ 🔄 ⚠️ Expiring |

### 4.4 Checklist Status Legend

| Status | Icon | Meaning |
|--------|------|---------|
| Complete | ✅ | Document received and approved |
| Missing | ❌ | Document required but not received |
| In Progress | 🔄 | Requested or pending |
| Expiring Soon | ⚠️ | Document will expire within 7 days |
| Expired | 🔴 | Document has expired, needs refresh |
| Not Applicable | N/A | Not required for this deal |
| Waived | ⏭️ | Waived by underwriter (with reason) |

### 4.5 Dashboard Tabs

**Tab 1: Checklist** (Default)
- Full closing checklist by category
- Click item to view/upload document
- Bulk actions: Send reminder, Request doc

**Tab 2: Documents**
- All documents in data room
- Filter by category, status, date
- Preview, download, replace

**Tab 3: Analysis**
- AI analysis results (Phase 7)
- All flags with status
- Exception requests
- Credit memo

**Tab 4: Activity**
- Complete audit log
- Filter by user, action type, date
- Export to PDF/CSV

**Tab 5: Notes**
- Internal notes (not in credit memo)
- Add new note
- Tag team members (@mentions)

**Tab 6: Tasks**
- All tasks for this deal
- Create new task
- Assign, set due date, mark complete

---

## 5. Home Dashboard

### 5.1 Dashboard Purpose

First screen users see when logging in. Provides at-a-glance view of their workload and pipeline health.

### 5.2 Home Dashboard Layout

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│  Good morning, Sarah                                           Dec 10, 2024 | 9:15 AM  │
│  ───────────────────                                                                    │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                         │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐        │
│  │  ACTIVE DEALS  │  │  CLOSING THIS  │  │  PIPELINE      │  │  MY TASKS      │        │
│  │                │  │  WEEK          │  │  VALUE         │  │                │        │
│  │      24        │  │       5        │  │   $12.4M       │  │      7         │        │
│  │  ↑ 3 from last │  │  2 at risk     │  │  ↑ $1.2M MTD   │  │  3 due today   │        │
│  └────────────────┘  └────────────────┘  └────────────────┘  └────────────────┘        │
│                                                                                         │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                         │
│  🔔 NEEDS ATTENTION                                                    [View All]      │
│  ─────────────────                                                                      │
│                                                                                         │
│  🔴 123 Main St - Red flag: Insurance mortgagee clause incorrect       [View Deal]     │
│  🔴 456 Oak Ave - Past target close date (was Dec 8)                   [View Deal]     │
│  🟡 789 Pine Rd - Appraisal expires in 5 days                          [View Deal]     │
│  🟡 321 Elm St - No activity in 6 days                                 [View Deal]     │
│  ⏰ 654 Maple Dr - Rate lock expires tomorrow                          [View Deal]     │
│                                                                                         │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                         │
│  📋 MY TASKS DUE TODAY                                                 [View All]      │
│  ────────────────────                                                                   │
│                                                                                         │
│  ☐ Call borrower re: missing bank statements - 123 Main St             [Complete]      │
│  ☐ Review appraisal - 789 Pine Rd                                      [Complete]      │
│  ☐ Submit exception request - 456 Oak Ave                              [Complete]      │
│                                                                                         │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                         │
│  📊 PIPELINE BY STAGE                                                                  │
│  ───────────────────                                                                    │
│                                                                                         │
│  Prospect      ████████████████████                              5 deals    $2.1M      │
│  Application   ████████████                                      3 deals    $1.4M      │
│  Quote         ████████████████                                  4 deals    $1.9M      │
│  Initial UW    ████████                                          2 deals    $1.1M      │
│  Processing    ████████████████████████                          6 deals    $2.8M      │
│  Underwriting  ████████████                                      3 deals    $1.5M      │
│  Closing       ████████                                          2 deals    $0.9M      │
│                                                                                         │
│  [View Pipeline]                                                                        │
│                                                                                         │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                         │
│  📈 RECENT ACTIVITY                                                    [View All]      │
│  ──────────────────                                                                     │
│                                                                                         │
│  • 9:10 AM - Appraisal received for 321 Elm St                         [View]          │
│  • 9:02 AM - John Smith uploaded bank statements for 123 Main St       [View]          │
│  • 8:45 AM - Credit memo generated for 654 Maple Dr                    [View]          │
│  • 8:30 AM - Quote selected by borrower for 789 Pine Rd                [View]          │
│  • Yesterday - 987 Cedar Ln moved to Funded 🎉                         [View]          │
│                                                                                         │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

### 5.3 "Needs Attention" Logic

A deal appears in "Needs Attention" if:
- Has any open red flags
- Past target close date
- Documents expiring within 7 days
- Rate lock expiring within 3 days
- No activity in 5+ days (stale)
- SLA at risk (>80% of allowed time elapsed)

### 5.4 KPI Cards

| KPI | Calculation | Drill-down |
|-----|-------------|------------|
| Active Deals | Count where status not in (funded, archived) | Pipeline view |
| Closing This Week | Target close date within 7 days | Filtered pipeline |
| Pipeline Value | Sum of loan amounts (active) | Pipeline view |
| My Tasks | Open tasks assigned to current user | Tasks view |

---

## 6. Task Management

### 6.1 Task Structure

```typescript
interface Task {
  id: string;
  dealId: string;
  
  // Task details
  title: string;
  description?: string;
  category: TaskCategory;
  
  // Assignment
  assignedTo: string;        // User ID
  assignedBy: string;        // User ID
  
  // Timing
  dueDate: Date;
  dueTime?: string;          // Optional specific time
  
  // Priority
  priority: 'low' | 'medium' | 'high' | 'urgent';
  
  // Status
  status: 'open' | 'in_progress' | 'complete' | 'cancelled';
  completedAt?: Date;
  completedBy?: string;
  
  // Recurrence (optional)
  isRecurring: boolean;
  recurringPattern?: string;
  
  // Notifications
  reminderSent: boolean;
  reminderAt?: Date;
  
  createdAt: Date;
  updatedAt: Date;
}

enum TaskCategory {
  document_collection = 'Document Collection',
  borrower_communication = 'Borrower Communication',
  third_party_followup = 'Third Party Follow-up',
  underwriting = 'Underwriting',
  closing = 'Closing',
  general = 'General'
}
```

### 6.2 Task Categories

| Category | Examples |
|----------|----------|
| Document Collection | Request bank statements, Follow up on missing DL |
| Borrower Communication | Call borrower, Send quote, Schedule call |
| Third Party Follow-up | Follow up on appraisal, Check title status |
| Underwriting | Review credit, Prepare exception request |
| Closing | Order wire, Confirm funding, Send closing docs |
| General | Internal meeting, Training, Other |

### 6.3 Quick Task Creation

From any deal card or dashboard:
```
[+ Quick Task]
├── Request Document
├── Call Borrower
├── Follow Up (3rd Party)
├── Review Document
├── Submit for Approval
└── Custom Task...
```

### 6.4 Task Views

**My Tasks View:**
- List of all tasks assigned to current user
- Filter by status, priority, due date, category
- Sort by due date, priority, deal
- Bulk complete/reassign

**Deal Tasks View:**
- All tasks for specific deal
- Create, assign, complete
- Task history

**Team Tasks View (Manager):**
- All tasks across team
- Filter by assignee
- Workload balancing

---

## 7. Activity Logging

### 7.1 Activity Log Structure

```typescript
interface ActivityLog {
  id: string;
  dealId: string;
  
  // Actor
  userId: string;
  userName: string;
  userRole: string;
  
  // Action
  action: ActivityAction;
  category: ActivityCategory;
  
  // Details
  description: string;
  metadata: Record<string, any>;  // Additional context
  
  // Related entities
  documentId?: string;
  taskId?: string;
  flagId?: string;
  
  // Timestamp
  timestamp: Date;
  
  // IP/Session (for security audit)
  ipAddress?: string;
  sessionId?: string;
}

enum ActivityAction {
  // Deal actions
  deal_created = 'Deal Created',
  deal_status_changed = 'Status Changed',
  deal_assigned = 'Deal Assigned',
  deal_updated = 'Deal Updated',
  
  // Document actions
  document_uploaded = 'Document Uploaded',
  document_classified = 'Document Classified',
  document_approved = 'Document Approved',
  document_rejected = 'Document Rejected',
  document_viewed = 'Document Viewed',
  
  // Analysis actions
  analysis_completed = 'Analysis Completed',
  flag_created = 'Flag Created',
  flag_resolved = 'Flag Resolved',
  exception_requested = 'Exception Requested',
  exception_approved = 'Exception Approved',
  exception_denied = 'Exception Denied',
  
  // Task actions
  task_created = 'Task Created',
  task_assigned = 'Task Assigned',
  task_completed = 'Task Completed',
  
  // Communication
  email_sent = 'Email Sent',
  note_added = 'Note Added',
  
  // Credit memo
  credit_memo_generated = 'Credit Memo Generated',
  credit_memo_approved = 'Credit Memo Approved',
  
  // Closing
  wire_sent = 'Wire Sent',
  funding_confirmed = 'Funding Confirmed'
}
```

### 7.2 Activity Log UI

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  ACTIVITY LOG: 123 Main Street                                              │
│  ──────────────────────────                                                 │
│  Filter: [All Actions ▼] [All Users ▼] [All Dates ▼]    [Export]           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Dec 10, 2024                                                               │
│  ─────────────                                                              │
│  9:15 AM   Sarah Johnson    📄 Document Uploaded                            │
│            Appraisal received and auto-classified                           │
│                                                                             │
│  9:16 AM   System           🤖 Analysis Completed                           │
│            Appraisal analyzed - 1 yellow flag created                       │
│                                                                             │
│  9:20 AM   Mike Chen        ✅ Flag Acknowledged                            │
│            ARV variance acknowledged - within acceptable range              │
│                                                                             │
│  Dec 9, 2024                                                                │
│  ────────────                                                               │
│  4:30 PM   John Smith       📄 Document Uploaded (via upload link)          │
│            Bank_Statements_Nov_2024.pdf                                     │
│                                                                             │
│  3:15 PM   Sarah Johnson    📧 Email Sent                                   │
│            Diligence reminder sent to borrower                              │
│                                                                             │
│  [Load More]                                                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 8. SLA Tracking

### 8.1 SLA Definitions

| Loan Type | Target Close | Warning At | Critical At |
|-----------|--------------|------------|-------------|
| RTL (Fix & Flip) | 21 days | 14 days | 18 days |
| RTL (Ground-Up) | 21 days | 14 days | 18 days |
| DSCR | 42 days | 28 days | 35 days |

### 8.2 Phase Duration Targets

| Phase | RTL Target | DSCR Target |
|-------|------------|-------------|
| Prospect → Application | 2 days | 2 days |
| Application → Quote | 1 day | 1 day |
| Quote → Initial UW | 2 days | 2 days |
| Initial UW → Processing | 1 day | 1 day |
| Processing → Underwriting | 5 days | 14 days |
| Underwriting → Closing | 3 days | 7 days |
| Closing → Funded | 3 days | 5 days |

### 8.3 SLA Dashboard Widget

```
┌─────────────────────────────────────────────────────────────────┐
│  SLA PERFORMANCE (Last 30 Days)                                 │
│  ──────────────────────────────                                 │
│                                                                 │
│  RTL Loans                           DSCR Loans                 │
│  ──────────                          ──────────                 │
│  On-time: 85% (17/20)                On-time: 82% (9/11)       │
│  Avg Days to Close: 19               Avg Days to Close: 38     │
│                                                                 │
│  Bottlenecks:                                                   │
│  • Processing phase avg 6 days (target: 5)                      │
│  • Appraisal turnaround avg 8 days                             │
│                                                                 │
│  [View Detailed Report]                                         │
└─────────────────────────────────────────────────────────────────┘
```

### 8.4 Deal SLA Indicator

On each deal card and dashboard:
```
⏱️ SLA Status: ON TRACK
   Day 12 of 21 (57%)
   ████████████░░░░░░░░░
```

Or:
```
⏱️ SLA Status: AT RISK
   Day 18 of 21 (86%)
   ██████████████████░░░
   3 days remaining
```

---

## 9. Quick Actions

### 9.1 Deal Card Quick Actions

| Action | Function |
|--------|----------|
| View Deal | Open closing dashboard |
| Send Reminder | Email borrower with outstanding items |
| Add Note | Quick note without opening deal |
| Create Task | Quick task creation |
| Move to Stage | Change status (with validation) |
| Assign | Change LO/Processor/Underwriter |
| Archive | Move to archived (with reason) |

### 9.2 Bulk Actions

Select multiple deals on pipeline:
| Action | Function |
|--------|----------|
| Send Bulk Reminder | Email all selected borrowers |
| Reassign | Change assignment for all |
| Export | Download deal summary CSV |
| Add Tag | Apply tag to all |

---

## 10. Search & Navigation

### 10.1 Global Search

Search bar at top of every page:
```
🔍 Search deals, borrowers, properties, documents...
```

**Search Results:**
- Deals (by address, borrower name, deal ID)
- Borrowers (by name, email, phone)
- Properties (by address)
- Documents (by name, content)

### 10.2 Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `⌘ + K` | Open global search |
| `⌘ + N` | New deal |
| `⌘ + P` | Go to pipeline |
| `⌘ + H` | Go to home dashboard |
| `⌘ + T` | My tasks |
| `Esc` | Close modal / Go back |
| `?` | Show keyboard shortcuts |

---

## 11. Notifications & Alerts

### 11.1 In-App Notifications

Bell icon in header with badge count:
```
🔔 (3)
├── 🔴 New red flag on 123 Main St - 2 min ago
├── 📄 Appraisal received for 456 Oak Ave - 15 min ago
└── ✅ Task completed by Mike Chen - 1 hour ago
```

### 11.2 Notification Preferences

Users can configure per notification type:
| Event | Email | In-App | Roam | SMS |
|-------|-------|--------|------|-----|
| Red flag on my deal | ✅ | ✅ | ✅ | ❌ |
| Document received | ❌ | ✅ | ❌ | ❌ |
| Task assigned to me | ✅ | ✅ | ✅ | ❌ |
| Task due today | ✅ | ✅ | ❌ | ❌ |
| Deal status change | ❌ | ✅ | ❌ | ❌ |
| SLA warning | ✅ | ✅ | ✅ | ❌ |

---

## 12. Technical Requirements

### 12.1 API Endpoints

```
# Pipeline
GET    /api/pipeline
       → Get all deals in pipeline (with filters)

GET    /api/pipeline/stats
       → Get pipeline statistics

PUT    /api/deals/:id/status
       → Update deal status (with validation)

POST   /api/deals/:id/move
       → Move deal to new stage

# Deal Dashboard
GET    /api/deals/:id/dashboard
       → Get full dashboard data

GET    /api/deals/:id/checklist
       → Get closing checklist

PUT    /api/deals/:id/checklist/:itemId
       → Update checklist item status

GET    /api/deals/:id/activity
       → Get activity log

# Tasks
GET    /api/tasks
       → Get tasks (with filters)

GET    /api/tasks/my
       → Get current user's tasks

POST   /api/tasks
       → Create task

PUT    /api/tasks/:id
       → Update task

DELETE /api/tasks/:id
       → Delete task

POST   /api/tasks/:id/complete
       → Mark task complete

# Home Dashboard
GET    /api/dashboard/home
       → Get home dashboard data

GET    /api/dashboard/needs-attention
       → Get deals needing attention

GET    /api/dashboard/stats
       → Get KPI stats

# Search
GET    /api/search?q={query}
       → Global search

# Activity
GET    /api/activity
       → Get activity feed (global)

GET    /api/deals/:id/activity
       → Get deal activity

# SLA
GET    /api/sla/report
       → Get SLA performance report

GET    /api/deals/:id/sla
       → Get deal SLA status
```

### 12.2 Data Models

```typescript
// Pipeline Stage
model PipelineStage {
  id                String   @id @default(uuid())
  code              String   @unique  // prospect, application, etc.
  name              String
  order             Int
  color             String
  
  // SLA
  targetDaysRTL     Int?
  targetDaysDSCR    Int?
  
  // Validation
  entryRequirements Json     // Rules for entering this stage
  exitRequirements  Json     // Rules for leaving this stage
  
  deals             Deal[]
}

// Task
model Task {
  id                String   @id @default(uuid())
  dealId            String
  deal              Deal     @relation(fields: [dealId], references: [id])
  
  title             String
  description       String?
  category          String
  
  assignedToId      String
  assignedTo        User     @relation("TaskAssignee", fields: [assignedToId], references: [id])
  assignedById      String
  assignedBy        User     @relation("TaskAssigner", fields: [assignedById], references: [id])
  
  dueDate           DateTime
  dueTime           String?
  priority          String   // low, medium, high, urgent
  
  status            String   // open, in_progress, complete, cancelled
  completedAt       DateTime?
  completedById     String?
  completedBy       User?    @relation("TaskCompleter", fields: [completedById], references: [id])
  
  isRecurring       Boolean  @default(false)
  recurringPattern  String?
  
  reminderSent      Boolean  @default(false)
  reminderAt        DateTime?
  
  createdAt         DateTime @default(now())
  updatedAt         DateTime @updatedAt
}

// Activity Log
model ActivityLog {
  id                String   @id @default(uuid())
  dealId            String?
  deal              Deal?    @relation(fields: [dealId], references: [id])
  
  userId            String
  user              User     @relation(fields: [userId], references: [id])
  
  action            String
  category          String
  description       String
  metadata          Json?
  
  documentId        String?
  taskId            String?
  flagId            String?
  
  timestamp         DateTime @default(now())
  
  ipAddress         String?
  sessionId         String?
  
  @@index([dealId])
  @@index([userId])
  @@index([timestamp])
}

// Checklist Item
model ChecklistItem {
  id                String   @id @default(uuid())
  dealId            String
  deal              Deal     @relation(fields: [dealId], references: [id])
  
  category          String   // borrower, property, third_party, closing, internal
  itemKey           String   // Unique key for item type
  displayName       String
  
  status            String   // complete, missing, in_progress, expiring, expired, na, waived
  
  documentId        String?  // Link to document if received
  document          Document? @relation(fields: [documentId], references: [id])
  
  requiredFor       String[] // Loan types this applies to
  
  expirationDate    DateTime?
  
  waivedAt          DateTime?
  waivedBy          String?
  waiverReason      String?
  
  notes             String?
  
  createdAt         DateTime @default(now())
  updatedAt         DateTime @updatedAt
  
  @@unique([dealId, itemKey])
}

// User Notification Preferences
model NotificationPreference {
  id                String   @id @default(uuid())
  userId            String   @unique
  user              User     @relation(fields: [userId], references: [id])
  
  preferences       Json     // Map of event type to channels
  
  createdAt         DateTime @default(now())
  updatedAt         DateTime @updatedAt
}

// Extend Deal model
model Deal {
  // ... existing fields ...
  
  // Stage tracking
  stageEnteredAt    DateTime?
  daysInStage       Int      @default(0)
  
  // SLA
  slaTargetDate     DateTime?
  slaStatus         String?  // on_track, warning, critical, overdue
  
  // Assignment
  assignedLOId      String?
  assignedLO        User?    @relation("DealLO", fields: [assignedLOId], references: [id])
  assignedProcessorId String?
  assignedProcessor User?    @relation("DealProcessor", fields: [assignedProcessorId], references: [id])
  assignedUWId      String?
  assignedUW        User?    @relation("DealUW", fields: [assignedUWId], references: [id])
  
  // Checklist progress
  checklistProgress Float?   // 0.0 - 1.0
  
  // Relations
  tasks             Task[]
  activityLogs      ActivityLog[]
  checklistItems    ChecklistItem[]
}
```

### 12.3 Real-Time Updates

Use WebSockets or Server-Sent Events for:
- Pipeline card movements
- Task status changes
- New documents received
- Flag status changes
- Activity feed updates

```typescript
// WebSocket events
interface PipelineEvent {
  type: 'deal_moved' | 'deal_updated' | 'deal_created';
  dealId: string;
  data: Partial<Deal>;
}

interface TaskEvent {
  type: 'task_created' | 'task_updated' | 'task_completed';
  taskId: string;
  dealId: string;
  data: Partial<Task>;
}

interface DocumentEvent {
  type: 'document_received' | 'document_classified';
  documentId: string;
  dealId: string;
  data: Partial<Document>;
}
```

### 12.4 Background Jobs

| Job | Frequency | Purpose |
|-----|-----------|---------|
| `update-days-in-stage` | Hourly | Calculate days in current stage |
| `check-sla-status` | Hourly | Update SLA status for all deals |
| `send-task-reminders` | Every 15 min | Send reminders for due tasks |
| `check-document-expiration` | Daily | Flag expiring documents |
| `auto-archive-stale` | Daily | Archive deals inactive 90+ days |
| `generate-sla-report` | Weekly | Generate SLA performance report |

---

## 13. Security & Permissions

### 13.1 MVP Permissions (All Users)

All internal users with @usdvcapital.com email have full access to:
- View all deals
- Edit any deal
- Create/complete tasks
- Upload documents
- View activity logs

### 13.2 Future Role-Based Permissions

| Permission | Admin | UW | LO | Processor |
|------------|-------|----|----|-----------|
| View all deals | ✅ | ✅ | ✅ | ✅ |
| Edit deal | ✅ | ✅ | ✅ | ✅ |
| Move to Funded | ✅ | ✅ | ❌ | ❌ |
| Approve exceptions | ✅ | ✅ | ❌ | ❌ |
| Delete deal | ✅ | ❌ | ❌ | ❌ |
| View audit logs | ✅ | ❌ | ❌ | ❌ |
| Manage users | ✅ | ❌ | ❌ | ❌ |

---

## 14. Testing Requirements

### 14.1 Unit Tests
- Pipeline filter logic
- SLA calculation
- Checklist generation by loan type
- Stage transition validation

### 14.2 Integration Tests
- Deal CRUD operations
- Task assignment and completion
- Activity logging
- Real-time updates

### 14.3 E2E Tests
1. Create deal → Move through all stages → Fund
2. Bulk operations on pipeline
3. Task lifecycle (create → assign → complete)
4. Search functionality
5. Filter and sort combinations

### 14.4 Performance Tests
- Pipeline load with 100+ deals
- Activity log query performance
- Real-time update latency

---

## 15. Dependencies

| Dependency | Status | Notes |
|------------|--------|-------|
| Phases 1-7 Complete | Required | Data flows from prior phases |
| User authentication | Required | For assignment and activity tracking |
| WebSocket infrastructure | Required | For real-time updates |
| Notification service | Required | For alerts and reminders |

---

## 16. Launch Checklist

- [ ] Pipeline board renders correctly
- [ ] All stage transitions validated
- [ ] Deal cards display all required info
- [ ] Closing dashboard functional
- [ ] Checklist auto-generates by loan type
- [ ] Task CRUD working
- [ ] Activity logging complete
- [ ] SLA calculations accurate
- [ ] Global search functional
- [ ] Filters and sorting work
- [ ] Real-time updates working
- [ ] Notifications configured
- [ ] Keyboard shortcuts implemented
- [ ] Mobile responsive
- [ ] Performance benchmarks met
- [ ] UAT sign-off

---

*End of Phase 8 PRD*
