# Phase 8 Implementation Plan: Operational Command Center

**Document Version:** 1.0  
**PRD Reference:** INSPIRE Phase 8 PRD  
**Last Updated:** December 2024  
**Status:** Implementation Ready

---

## 1. Executive Summary

### 1.1 Phase Overview

Phase 8 delivers the operational command center for loan origination management:
- **Kanban Pipeline** - Visual deal tracking across all stages
- **Deal Closing Dashboard** - Comprehensive deal management with checklists
- **Home Dashboard** - KPIs, tasks, alerts, and pipeline overview
- **Task Management** - Unified task tracking across deals
- **Activity Logging** - Complete audit trail
- **SLA Tracking** - Phase duration monitoring
- **Global Search & Notifications** - Quick navigation and alerts

### 1.2 Success Metrics (from PRD)

| Metric | Target |
|--------|--------|
| Pipeline visibility | 100% real-time |
| Task completion tracking | 100% |
| SLA compliance visibility | Real-time |
| Average time to find deal | <5 seconds |
| Dashboard load time | <2 seconds |
| Notification delivery | <30 seconds |

### 1.3 Key Dependencies

| Dependency | Status | Notes |
|------------|--------|-------|
| Phases 1-7 Complete | Required | All deal data available |
| User Authentication | Required | Role-based access |
| WebSocket/SSE | Required | Real-time updates |
| Email Service | Required | Notifications |
| SMS Service | Optional | SMS notifications |

---

## 2. Page/Screen Inventory

### 2.1 Complete Page List

| Page ID | Page Name | Route | User Role | Entry Point |
|---------|-----------|-------|-----------|-------------|
| P8-01 | Home Dashboard | `/` | Internal | App entry |
| P8-02 | Pipeline Board | `/pipeline` | Internal | Navigation |
| P8-03 | Deal Closing Dashboard | `/deals/:id` | Internal | Pipeline, Search |
| P8-04 | Task Manager | `/tasks` | Internal | Navigation |
| P8-05 | Activity Log | `/activity` | Internal | Navigation |
| P8-06 | Reports | `/reports` | Internal | Navigation |
| P8-07 | Settings | `/settings` | Internal | Navigation |
| P8-08 | Notifications | `/notifications` | Internal | Header bell |

### 2.2 Navigation Structure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           INSPIRE NAVIGATION                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  SIDEBAR (Primary Navigation)                                                │
│  ├── Home Dashboard (/)                                                      │
│  ├── Pipeline (/pipeline)                                                    │
│  ├── Deals (/deals)                                                          │
│  │   └── Deal Detail (/deals/:id)                                            │
│  │       ├── Overview (default)                                              │
│  │       ├── Application (/deals/:id/application)                            │
│  │       ├── Sizing (/deals/:id/sizing)                                      │
│  │       ├── Quotes (/deals/:id/quotes)                                      │
│  │       ├── Reports (/deals/:id/reports)                                    │
│  │       ├── Diligence (/deals/:id/diligence)                                │
│  │       ├── Analysis (/deals/:id/analysis)                                  │
│  │       ├── Credit Memo (/deals/:id/credit-memo)                            │
│  │       ├── Documents (/deals/:id/documents)                                │
│  │       └── Activity (/deals/:id/activity)                                  │
│  ├── Borrowers (/borrowers)                                                  │
│  ├── Tasks (/tasks)                                                          │
│  ├── Reports (/reports)                                                      │
│  └── Settings (/settings)                                                    │
│                                                                              │
│  HEADER (Secondary Navigation)                                               │
│  ├── Global Search (Cmd+K)                                                   │
│  ├── Notifications Bell                                                      │
│  └── User Menu                                                               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Per-Page Specifications

---

### 3.1 P8-01: Home Dashboard

#### 3.1.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Central command center with KPIs, tasks, and alerts |
| **User Roles** | All internal users |
| **Entry Points** | App entry, Logo click |
| **PRD Reference** | Phase 8 PRD, Section 5 |

#### 3.1.2 Information Architecture

**Content Hierarchy:**
1. KPI Cards (top row)
2. "Needs Attention" Section
3. Tasks Due Today
4. Pipeline by Stage
5. Recent Activity

#### 3.1.3 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `card` | KPI cards, section cards |
| `badge` | Counts, status |
| `button` | Quick actions |
| `table` | Task list, activity list |
| `progress` | Pipeline progress |
| `chart` | Pipeline visualization |
| `avatar` | User avatars |
| `tooltip` | KPI explanations |

**React Custom Components:**

```typescript
// components/dashboard/HomeDashboard.tsx
interface HomeDashboardProps {
  kpis: DashboardKPIs;
  needsAttention: NeedsAttentionItem[];
  tasksDueToday: Task[];
  pipelineByStage: PipelineStageCount[];
  recentActivity: Activity[];
  userId: string;
}

// Main home dashboard
// Composition: Uses ShadCN Card, multiple custom components
```

```typescript
// components/dashboard/KPICard.tsx
interface KPICardProps {
  title: string;
  value: number | string;
  change?: {
    value: number;
    direction: 'up' | 'down';
    period: string;
  };
  icon: React.ReactNode;
  onClick?: () => void;
}

// Individual KPI display
// Composition: Uses ShadCN Card, Badge
```

```typescript
// components/dashboard/NeedsAttentionSection.tsx
interface NeedsAttentionSectionProps {
  items: NeedsAttentionItem[];
  onItemClick: (item: NeedsAttentionItem) => void;
  onDismiss: (itemId: string) => void;
}

// Needs attention list
// Composition: Uses ShadCN Card, Badge, Button
```

```typescript
// components/dashboard/TasksDueTodayCard.tsx
interface TasksDueTodayCardProps {
  tasks: Task[];
  onTaskClick: (taskId: string) => void;
  onTaskComplete: (taskId: string) => void;
  onViewAll: () => void;
}

// Today's tasks summary
// Composition: Uses ShadCN Card, Checkbox, Button
```

```typescript
// components/dashboard/PipelineOverviewChart.tsx
interface PipelineOverviewChartProps {
  stages: PipelineStageCount[];
  onStageClick: (stage: string) => void;
}

// Pipeline visualization
// Composition: Uses ShadCN Card, Chart (bar or funnel)
```

```typescript
// components/dashboard/RecentActivityFeed.tsx
interface RecentActivityFeedProps {
  activities: Activity[];
  onActivityClick: (activityId: string) => void;
  onViewAll: () => void;
}

// Recent activity list
// Composition: Uses ShadCN Card, Avatar, Badge
```

#### 3.1.4 Data Requirements

```typescript
interface DashboardKPIs {
  // Volume KPIs
  activeDeals: number;
  activeDealsChange: number;
  
  pipelineVolume: number; // Total $ in pipeline
  pipelineVolumeChange: number;
  
  closedThisMonth: number;
  closedThisMonthChange: number;
  
  closedVolumeThisMonth: number;
  closedVolumeThisMonthChange: number;
  
  // Velocity KPIs
  avgDaysToClose: number;
  avgDaysToCloseChange: number;
  
  avgDaysInStage: Record<string, number>;
  
  // Quality KPIs
  pullThroughRate: number; // % of apps that fund
  pullThroughRateChange: number;
  
  slaCompliance: number; // % within SLA
  slaComplianceChange: number;
}

interface NeedsAttentionItem {
  id: string;
  dealId: string;
  propertyAddress: string;
  borrowerName: string;
  
  // Reason for attention
  reason: NeedsAttentionReason;
  reasonDetail: string;
  
  // Priority
  priority: 'high' | 'medium' | 'low';
  
  // Timing
  dueDate?: Date;
  daysPastDue?: number;
  
  // Action
  actionRequired: string;
  actionUrl: string;
  
  createdAt: Date;
}

type NeedsAttentionReason = 
  | 'sla_breach'
  | 'sla_at_risk'
  | 'document_expiring'
  | 'document_rejected'
  | 'task_overdue'
  | 'quote_expiring'
  | 'rate_lock_expiring'
  | 'red_flag_unresolved'
  | 'exception_pending'
  | 'closing_incomplete'
  | 'borrower_response_needed';

interface PipelineStageCount {
  stage: string;
  stageLabel: string;
  count: number;
  volume: number;
  avgDaysInStage: number;
  slaTarget: number;
  atRisk: number;
}
```

#### 3.1.5 "Needs Attention" Logic (from PRD)

```typescript
const NEEDS_ATTENTION_RULES: NeedsAttentionRule[] = [
  {
    id: 'sla_breach',
    name: 'SLA Breach',
    priority: 'high',
    check: (deal) => {
      const daysInStage = daysSince(deal.stageEnteredAt);
      const slaTarget = SLA_TARGETS[deal.stage];
      return daysInStage > slaTarget;
    },
    message: (deal) => `SLA breached: ${daysSince(deal.stageEnteredAt)} days in ${deal.stage}`,
  },
  {
    id: 'sla_at_risk',
    name: 'SLA At Risk',
    priority: 'medium',
    check: (deal) => {
      const daysInStage = daysSince(deal.stageEnteredAt);
      const slaTarget = SLA_TARGETS[deal.stage];
      return daysInStage >= slaTarget * 0.8 && daysInStage <= slaTarget;
    },
    message: (deal) => `SLA at risk: ${daysInStage} of ${slaTarget} days`,
  },
  {
    id: 'document_expiring',
    name: 'Document Expiring',
    priority: 'medium',
    check: (deal) => {
      return deal.documents.some(d => 
        d.expirationDate && daysUntil(d.expirationDate) <= 14
      );
    },
    message: (deal) => {
      const expiring = deal.documents.filter(d => 
        d.expirationDate && daysUntil(d.expirationDate) <= 14
      );
      return `${expiring.length} document(s) expiring soon`;
    },
  },
  {
    id: 'quote_expiring',
    name: 'Quote Expiring',
    priority: 'high',
    check: (deal) => {
      return deal.activeQuote && daysUntil(deal.activeQuote.expiresAt) <= 3;
    },
    message: (deal) => `Quote expires in ${daysUntil(deal.activeQuote.expiresAt)} days`,
  },
  {
    id: 'red_flag_unresolved',
    name: 'Unresolved Red Flag',
    priority: 'high',
    check: (deal) => {
      return deal.flags.some(f => f.severity === 'red' && !f.resolvedAt);
    },
    message: (deal) => {
      const redFlags = deal.flags.filter(f => f.severity === 'red' && !f.resolvedAt);
      return `${redFlags.length} unresolved red flag(s)`;
    },
  },
  {
    id: 'task_overdue',
    name: 'Overdue Task',
    priority: 'medium',
    check: (deal) => {
      return deal.tasks.some(t => t.dueDate && isPast(t.dueDate) && !t.completedAt);
    },
    message: (deal) => {
      const overdue = deal.tasks.filter(t => t.dueDate && isPast(t.dueDate) && !t.completedAt);
      return `${overdue.length} overdue task(s)`;
    },
  },
];
```

#### 3.1.6 Mock Data

```json
{
  "kpis": {
    "activeDeals": 47,
    "activeDealsChange": 5,
    "pipelineVolume": 28500000,
    "pipelineVolumeChange": 2100000,
    "closedThisMonth": 12,
    "closedThisMonthChange": 3,
    "closedVolumeThisMonth": 8750000,
    "closedVolumeThisMonthChange": 1250000,
    "avgDaysToClose": 28,
    "avgDaysToCloseChange": -2,
    "pullThroughRate": 72,
    "pullThroughRateChange": 4,
    "slaCompliance": 89,
    "slaComplianceChange": 3
  },
  "needsAttention": [
    {
      "id": "attn_001",
      "dealId": "deal_abc123",
      "propertyAddress": "123 Main St, Austin, TX",
      "borrowerName": "ABC Investments LLC",
      "reason": "sla_breach",
      "reasonDetail": "12 days in Processing (SLA: 10 days)",
      "priority": "high",
      "daysPastDue": 2,
      "actionRequired": "Complete processing checklist",
      "actionUrl": "/deals/deal_abc123"
    },
    {
      "id": "attn_002",
      "dealId": "deal_def456",
      "propertyAddress": "456 Oak Ave, Dallas, TX",
      "borrowerName": "XYZ Holdings LLC",
      "reason": "quote_expiring",
      "reasonDetail": "Quote expires in 2 days",
      "priority": "high",
      "dueDate": "2024-12-17T00:00:00Z",
      "actionRequired": "Follow up on quote acceptance",
      "actionUrl": "/deals/deal_def456/quotes"
    },
    {
      "id": "attn_003",
      "dealId": "deal_ghi789",
      "propertyAddress": "789 Pine Rd, Houston, TX",
      "borrowerName": "123 Properties LLC",
      "reason": "red_flag_unresolved",
      "reasonDetail": "1 unresolved red flag",
      "priority": "high",
      "actionRequired": "Review and resolve FICO exception",
      "actionUrl": "/deals/deal_ghi789/analysis"
    }
  ],
  "tasksDueToday": [
    {
      "id": "task_001",
      "dealId": "deal_abc123",
      "title": "Review appraisal report",
      "dueDate": "2024-12-15T17:00:00Z",
      "priority": "high",
      "status": "pending"
    },
    {
      "id": "task_002",
      "dealId": "deal_def456",
      "title": "Send closing instructions to title",
      "dueDate": "2024-12-15T17:00:00Z",
      "priority": "medium",
      "status": "pending"
    }
  ],
  "pipelineByStage": [
    { "stage": "prospect", "stageLabel": "Prospect", "count": 8, "volume": 4800000, "avgDaysInStage": 3, "slaTarget": 5, "atRisk": 1 },
    { "stage": "application", "stageLabel": "Application", "count": 12, "volume": 7200000, "avgDaysInStage": 4, "slaTarget": 7, "atRisk": 2 },
    { "stage": "quote", "stageLabel": "Quote", "count": 6, "volume": 3600000, "avgDaysInStage": 2, "slaTarget": 3, "atRisk": 0 },
    { "stage": "processing", "stageLabel": "Processing", "count": 10, "volume": 6000000, "avgDaysInStage": 8, "slaTarget": 10, "atRisk": 3 },
    { "stage": "underwriting", "stageLabel": "Underwriting", "count": 7, "volume": 4200000, "avgDaysInStage": 5, "slaTarget": 7, "atRisk": 1 },
    { "stage": "closing", "stageLabel": "Closing", "count": 4, "volume": 2400000, "avgDaysInStage": 4, "slaTarget": 5, "atRisk": 0 }
  ],
  "recentActivity": [
    {
      "id": "act_001",
      "dealId": "deal_abc123",
      "action": "document_uploaded",
      "description": "Appraisal report uploaded",
      "userId": "user_001",
      "userName": "John Smith",
      "timestamp": "2024-12-15T14:30:00Z"
    },
    {
      "id": "act_002",
      "dealId": "deal_def456",
      "action": "stage_changed",
      "description": "Deal moved to Closing",
      "userId": "user_002",
      "userName": "Jane Doe",
      "timestamp": "2024-12-15T14:15:00Z"
    }
  ]
}
```

---

### 3.2 P8-02: Pipeline Board

#### 3.2.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Visual Kanban board for deal pipeline management |
| **User Roles** | All internal users |
| **Entry Points** | Navigation, Home dashboard |
| **PRD Reference** | Phase 8 PRD, Section 3 |

#### 3.2.2 Pipeline Stages (from PRD)

```typescript
const PIPELINE_STAGES: PipelineStage[] = [
  {
    id: 'prospect',
    label: 'Prospect',
    description: 'Initial inquiry, pre-qualification',
    slaTarget: 5,
    color: 'slate',
    allowedTransitions: ['application', 'archived'],
  },
  {
    id: 'application',
    label: 'Application',
    description: 'Full application submitted',
    slaTarget: 7,
    color: 'blue',
    allowedTransitions: ['quote', 'archived'],
  },
  {
    id: 'quote',
    label: 'Quote',
    description: 'Quote generated, awaiting acceptance',
    slaTarget: 3,
    color: 'indigo',
    allowedTransitions: ['initial_uw', 'archived'],
  },
  {
    id: 'initial_uw',
    label: 'Initial UW',
    description: 'Initial underwriting review',
    slaTarget: 5,
    color: 'violet',
    allowedTransitions: ['processing', 'archived'],
  },
  {
    id: 'processing',
    label: 'Processing',
    description: 'Document collection and verification',
    slaTarget: 10,
    color: 'purple',
    allowedTransitions: ['underwriting', 'archived'],
  },
  {
    id: 'underwriting',
    label: 'Underwriting',
    description: 'Full underwriting review',
    slaTarget: 7,
    color: 'fuchsia',
    allowedTransitions: ['closing', 'archived'],
  },
  {
    id: 'closing',
    label: 'Closing',
    description: 'Final docs and funding',
    slaTarget: 5,
    color: 'pink',
    allowedTransitions: ['funded', 'archived'],
  },
  {
    id: 'funded',
    label: 'Funded',
    description: 'Loan funded',
    slaTarget: null,
    color: 'green',
    allowedTransitions: ['archived'],
  },
  {
    id: 'archived',
    label: 'Archived',
    description: 'Withdrawn, declined, or cancelled',
    slaTarget: null,
    color: 'gray',
    allowedTransitions: [],
  },
];
```

#### 3.2.3 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `card` | Deal cards, stage columns |
| `badge` | Status, flags, SLA |
| `button` | Quick actions, filters |
| `select` | Filter dropdowns |
| `input` | Search |
| `avatar` | Assigned user |
| `tooltip` | Deal preview |
| `dropdown-menu` | Card actions |
| `dialog` | Quick view modal |

**React Custom Components:**

```typescript
// components/pipeline/PipelineBoard.tsx
interface PipelineBoardProps {
  deals: Deal[];
  stages: PipelineStage[];
  filters: PipelineFilters;
  onFiltersChange: (filters: PipelineFilters) => void;
  onDealMove: (dealId: string, toStage: string) => void;
  onDealClick: (dealId: string) => void;
}

// Main Kanban board
// Composition: Uses custom drag-drop, ShadCN Card
```

```typescript
// components/pipeline/PipelineColumn.tsx
interface PipelineColumnProps {
  stage: PipelineStage;
  deals: Deal[];
  onDrop: (dealId: string) => void;
  onDealClick: (dealId: string) => void;
}

// Individual stage column
// Composition: Uses ShadCN Card
```

```typescript
// components/pipeline/DealCard.tsx
interface DealCardProps {
  deal: Deal;
  onClick: () => void;
  onQuickAction: (action: string) => void;
  isDragging?: boolean;
}

// Deal card on Kanban
// Composition: Uses ShadCN Card, Badge, Avatar, DropdownMenu
```

```typescript
// components/pipeline/DealCardContent.tsx
interface DealCardContentProps {
  deal: Deal;
}

// Deal card content layout (from PRD 3.3)
// Shows: Address, Borrower, Loan Amount, LTV/DSCR, Days in Stage, Flags, Assigned
// Composition: Uses ShadCN Badge
```

```typescript
// components/pipeline/PipelineFilters.tsx
interface PipelineFiltersProps {
  filters: PipelineFilters;
  onChange: (filters: PipelineFilters) => void;
  loanOfficers: User[];
  processors: User[];
}

// Filter controls
// Composition: Uses ShadCN Select, Input, Button
```

```typescript
// components/pipeline/SLAIndicator.tsx
interface SLAIndicatorProps {
  daysInStage: number;
  slaTarget: number;
}

// Visual SLA status indicator
// Composition: Uses ShadCN Badge, Progress
```

#### 3.2.4 Deal Card Design (from PRD Section 3.3)

```typescript
interface DealCardDisplay {
  // Primary info
  propertyAddress: string;
  city: string;
  state: string;
  
  // Borrower
  borrowerName: string;
  
  // Loan details
  loanAmount: number;
  loanType: string;
  
  // Key metrics (conditional)
  ltv?: number;  // RTL
  ltc?: number;  // RTL
  dscr?: number; // DSCR
  
  // Status
  daysInStage: number;
  slaTarget: number;
  slaStatus: 'on_track' | 'at_risk' | 'breached';
  
  // Flags
  redFlagCount: number;
  yellowFlagCount: number;
  
  // Assignment
  assignedTo: {
    id: string;
    name: string;
    avatar: string;
  };
  
  // Priority indicator
  priority?: 'high' | 'normal';
}
```

#### 3.2.5 Drag-and-Drop Rules (from PRD Section 3.4)

```typescript
const DRAG_DROP_RULES = {
  // Only allow forward progression (with exceptions)
  validateMove: (deal: Deal, fromStage: string, toStage: string): boolean => {
    const stage = PIPELINE_STAGES.find(s => s.id === fromStage);
    return stage?.allowedTransitions.includes(toStage) || false;
  },
  
  // Require confirmation for certain moves
  requiresConfirmation: (fromStage: string, toStage: string): boolean => {
    return toStage === 'archived';
  },
  
  // Require reason for archive
  requiresReason: (toStage: string): boolean => {
    return toStage === 'archived';
  },
  
  // Auto-actions on stage change
  onStageChange: async (deal: Deal, toStage: string) => {
    // Log activity
    await logActivity({
      dealId: deal.id,
      action: 'stage_changed',
      details: { from: deal.stage, to: toStage },
    });
    
    // Update SLA tracking
    await updateSLATracking(deal.id, toStage);
    
    // Trigger stage-specific automations
    await triggerStageAutomations(deal.id, toStage);
  },
};
```

#### 3.2.6 Mock Data

```json
{
  "filters": {
    "search": "",
    "loanType": null,
    "assignedTo": null,
    "slaStatus": null,
    "dateRange": null
  },
  "deals": [
    {
      "id": "deal_001",
      "stage": "processing",
      "propertyAddress": "123 Main St",
      "city": "Austin",
      "state": "TX",
      "borrowerName": "ABC Investments LLC",
      "loanAmount": 382500,
      "loanType": "fix_flip",
      "ltc": 75,
      "ltv": 65,
      "daysInStage": 8,
      "slaTarget": 10,
      "slaStatus": "at_risk",
      "redFlagCount": 1,
      "yellowFlagCount": 2,
      "assignedTo": {
        "id": "user_001",
        "name": "John Smith",
        "avatar": "/avatars/john.jpg"
      },
      "priority": "high"
    },
    {
      "id": "deal_002",
      "stage": "underwriting",
      "propertyAddress": "456 Oak Ave",
      "city": "Dallas",
      "state": "TX",
      "borrowerName": "XYZ Holdings LLC",
      "loanAmount": 525000,
      "loanType": "dscr",
      "dscr": 1.35,
      "daysInStage": 3,
      "slaTarget": 7,
      "slaStatus": "on_track",
      "redFlagCount": 0,
      "yellowFlagCount": 1,
      "assignedTo": {
        "id": "user_002",
        "name": "Jane Doe",
        "avatar": "/avatars/jane.jpg"
      }
    }
  ],
  "stageCounts": {
    "prospect": 8,
    "application": 12,
    "quote": 6,
    "initial_uw": 5,
    "processing": 10,
    "underwriting": 7,
    "closing": 4,
    "funded": 156,
    "archived": 89
  }
}
```

---

### 3.3 P8-03: Deal Closing Dashboard

#### 3.3.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Comprehensive deal management with all details and actions |
| **User Roles** | All internal users |
| **Entry Points** | Pipeline card, Search, Direct URL |
| **PRD Reference** | Phase 8 PRD, Section 4 |

#### 3.3.2 Dashboard Tabs (from PRD Section 4.3)

```typescript
const DEAL_DASHBOARD_TABS = [
  {
    id: 'overview',
    label: 'Overview',
    icon: 'LayoutDashboard',
    description: 'Deal summary, key metrics, quick actions',
  },
  {
    id: 'checklist',
    label: 'Checklist',
    icon: 'CheckSquare',
    description: 'Closing checklist and task management',
  },
  {
    id: 'documents',
    label: 'Documents',
    icon: 'FileText',
    description: 'Data room and document management',
  },
  {
    id: 'analysis',
    label: 'Analysis',
    icon: 'BarChart',
    description: 'AI analysis, flags, and credit memo',
  },
  {
    id: 'activity',
    label: 'Activity',
    icon: 'Activity',
    description: 'Activity log and audit trail',
  },
  {
    id: 'notes',
    label: 'Notes',
    icon: 'MessageSquare',
    description: 'Internal notes and comments',
  },
];
```

#### 3.3.3 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `card` | Section cards |
| `tabs` | Dashboard tabs |
| `badge` | Status badges |
| `button` | Actions |
| `progress` | Checklist progress |
| `checkbox` | Checklist items |
| `table` | Document list, activity log |
| `avatar` | User avatars |
| `separator` | Section dividers |
| `alert` | Warnings, flags |

**React Custom Components:**

```typescript
// components/deals/DealClosingDashboard.tsx
interface DealClosingDashboardProps {
  deal: Deal;
  activeTab: string;
  onTabChange: (tab: string) => void;
}

// Main deal dashboard
// Composition: Uses ShadCN Tabs, Card
```

```typescript
// components/deals/DealHeader.tsx
interface DealHeaderProps {
  deal: Deal;
  onStageChange: (stage: string) => void;
  onQuickAction: (action: string) => void;
}

// Deal header with key info and actions
// Composition: Uses ShadCN Badge, Button, DropdownMenu
```

```typescript
// components/deals/DealOverviewTab.tsx
interface DealOverviewTabProps {
  deal: Deal;
  metrics: DealMetrics;
  flags: Flag[];
  recentActivity: Activity[];
}

// Overview tab content
// Composition: Uses ShadCN Card, Badge
```

```typescript
// components/deals/DealChecklistTab.tsx
interface DealChecklistTabProps {
  deal: Deal;
  checklist: ChecklistCategory[];
  onItemComplete: (itemId: string) => void;
  onItemAssign: (itemId: string, userId: string) => void;
}

// Checklist tab content
// Composition: Uses ShadCN Checkbox, Progress, Accordion
```

```typescript
// components/deals/DealDocumentsTab.tsx
interface DealDocumentsTabProps {
  deal: Deal;
  documents: Document[];
  folders: DataRoomFolder[];
  onUpload: (files: File[]) => void;
  onView: (docId: string) => void;
}

// Documents tab content
// Composition: Uses ShadCN Table, Button
```

```typescript
// components/deals/DealActivityTab.tsx
interface DealActivityTabProps {
  deal: Deal;
  activities: Activity[];
  onLoadMore: () => void;
}

// Activity tab content
// Composition: Uses ShadCN Card, Avatar, Badge
```

```typescript
// components/deals/DealNotesTab.tsx
interface DealNotesTabProps {
  deal: Deal;
  notes: Note[];
  onAddNote: (content: string) => void;
  onEditNote: (noteId: string, content: string) => void;
}

// Notes tab content
// Composition: Uses ShadCN Textarea, Button, Avatar
```

#### 3.3.4 Checklist Categories (from PRD Section 4.4)

```typescript
const CHECKLIST_CATEGORIES: ChecklistCategory[] = [
  {
    id: 'borrower',
    label: 'Borrower',
    items: [
      { id: 'entity_docs', label: 'Entity Documents', required: true },
      { id: 'guarantor_ids', label: 'Guarantor IDs', required: true },
      { id: 'bank_statements', label: 'Bank Statements', required: true },
      { id: 'credit_report', label: 'Credit Report', required: true, autoPopulated: true },
      { id: 'background_check', label: 'Background Check', required: true, autoPopulated: true },
    ],
  },
  {
    id: 'property',
    label: 'Property',
    items: [
      { id: 'purchase_contract', label: 'Purchase Contract', required: true, loanTypes: ['purchase'] },
      { id: 'appraisal', label: 'Appraisal', required: true, autoPopulated: true },
      { id: 'title_commitment', label: 'Title Commitment', required: true, autoPopulated: true },
      { id: 'insurance', label: 'Insurance Certificate', required: true },
      { id: 'flood_cert', label: 'Flood Determination', required: true, autoPopulated: true },
      { id: 'scope_of_work', label: 'Scope of Work', required: true, loanTypes: ['fix_flip', 'ground_up'] },
      { id: 'leases', label: 'Lease Agreements', required: true, loanTypes: ['dscr'] },
    ],
  },
  {
    id: 'underwriting',
    label: 'Underwriting',
    items: [
      { id: 'sizing_complete', label: 'Sizing Complete', required: true },
      { id: 'quote_accepted', label: 'Quote Accepted', required: true },
      { id: 'term_sheet_signed', label: 'Term Sheet Signed', required: true },
      { id: 'analysis_complete', label: 'AI Analysis Complete', required: true },
      { id: 'credit_memo_approved', label: 'Credit Memo Approved', required: true },
      { id: 'exceptions_resolved', label: 'Exceptions Resolved', required: true },
    ],
  },
  {
    id: 'closing',
    label: 'Closing',
    items: [
      { id: 'final_title', label: 'Final Title Policy', required: true },
      { id: 'closing_protection', label: 'Closing Protection Letter', required: true },
      { id: 'hud_approved', label: 'HUD/Settlement Approved', required: true },
      { id: 'wire_instructions', label: 'Wire Instructions Verified', required: true },
      { id: 'docs_signed', label: 'Loan Documents Signed', required: true },
      { id: 'funding_approved', label: 'Funding Approved', required: true },
    ],
  },
];
```

#### 3.3.5 Quick Actions (from PRD Section 4.5)

```typescript
const DEAL_QUICK_ACTIONS = [
  {
    id: 'send_reminder',
    label: 'Send Reminder',
    icon: 'Mail',
    stages: ['application', 'processing'],
  },
  {
    id: 'generate_quote',
    label: 'Generate Quote',
    icon: 'Calculator',
    stages: ['application'],
  },
  {
    id: 'order_reports',
    label: 'Order Reports',
    icon: 'FileSearch',
    stages: ['processing'],
  },
  {
    id: 'run_analysis',
    label: 'Run Analysis',
    icon: 'BarChart',
    stages: ['processing', 'underwriting'],
  },
  {
    id: 'generate_memo',
    label: 'Generate Credit Memo',
    icon: 'FileText',
    stages: ['underwriting'],
  },
  {
    id: 'schedule_closing',
    label: 'Schedule Closing',
    icon: 'Calendar',
    stages: ['closing'],
  },
  {
    id: 'approve_funding',
    label: 'Approve Funding',
    icon: 'CheckCircle',
    stages: ['closing'],
  },
];
```

---

### 3.4 P8-04: Task Manager

#### 3.4.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Unified task management across all deals |
| **User Roles** | All internal users |
| **Entry Points** | Navigation, Dashboard |
| **PRD Reference** | Phase 8 PRD, Section 6 |

#### 3.4.2 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `card` | Task cards |
| `checkbox` | Task completion |
| `badge` | Priority, status |
| `button` | Add task, filters |
| `select` | Filter dropdowns |
| `input` | Search, quick add |
| `table` | Task list view |
| `tabs` | View tabs (My Tasks, All, By Deal) |
| `dialog` | Task detail modal |
| `calendar` | Date picker |

**React Custom Components:**

```typescript
// components/tasks/TaskManager.tsx
interface TaskManagerProps {
  tasks: Task[];
  filters: TaskFilters;
  view: 'list' | 'board' | 'calendar';
  onFiltersChange: (filters: TaskFilters) => void;
  onTaskCreate: (task: CreateTaskInput) => void;
  onTaskUpdate: (taskId: string, updates: Partial<Task>) => void;
  onTaskComplete: (taskId: string) => void;
}

// Main task manager
// Composition: Uses ShadCN Table, Tabs, Card
```

```typescript
// components/tasks/TaskListView.tsx
interface TaskListViewProps {
  tasks: Task[];
  onTaskClick: (taskId: string) => void;
  onTaskComplete: (taskId: string) => void;
  sortBy: string;
  onSortChange: (sortBy: string) => void;
}

// List view of tasks
// Composition: Uses ShadCN Table, Checkbox, Badge
```

```typescript
// components/tasks/TaskCard.tsx
interface TaskCardProps {
  task: Task;
  onClick: () => void;
  onComplete: () => void;
  onAssign: (userId: string) => void;
}

// Individual task card
// Composition: Uses ShadCN Card, Checkbox, Badge, Avatar
```

```typescript
// components/tasks/QuickTaskInput.tsx
interface QuickTaskInputProps {
  dealId?: string;
  onSubmit: (task: CreateTaskInput) => void;
}

// Quick task creation input
// Composition: Uses ShadCN Input, Button
```

```typescript
// components/tasks/TaskDetailDialog.tsx
interface TaskDetailDialogProps {
  task: Task;
  open: boolean;
  onClose: () => void;
  onUpdate: (updates: Partial<Task>) => void;
  onDelete: () => void;
}

// Task detail modal
// Composition: Uses ShadCN Dialog, Form
```

#### 3.4.3 Data Requirements

```typescript
interface Task {
  id: string;
  
  // Content
  title: string;
  description?: string;
  
  // Association
  dealId?: string;
  deal?: {
    id: string;
    propertyAddress: string;
    borrowerName: string;
  };
  
  // Assignment
  assignedTo?: string;
  assignedUser?: User;
  createdBy: string;
  
  // Timing
  dueDate?: Date;
  reminderDate?: Date;
  
  // Status
  status: 'pending' | 'in_progress' | 'completed' | 'cancelled';
  completedAt?: Date;
  completedBy?: string;
  
  // Priority
  priority: 'high' | 'medium' | 'low';
  
  // Category
  category: TaskCategory;
  
  // Source
  source: 'manual' | 'system' | 'checklist' | 'sla';
  sourceId?: string;
  
  createdAt: Date;
  updatedAt: Date;
}

type TaskCategory = 
  | 'follow_up'
  | 'document_request'
  | 'review'
  | 'approval'
  | 'closing'
  | 'general';

interface TaskFilters {
  status?: string[];
  priority?: string[];
  category?: string[];
  assignedTo?: string;
  dealId?: string;
  dueDate?: {
    from?: Date;
    to?: Date;
  };
  search?: string;
}
```

---

### 3.5 P8-05: Activity Log

#### 3.5.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Complete audit trail of all system activity |
| **User Roles** | All internal users |
| **Entry Points** | Navigation, Deal dashboard |
| **PRD Reference** | Phase 8 PRD, Section 7 |

#### 3.5.2 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `card` | Activity cards |
| `badge` | Action type badges |
| `avatar` | User avatars |
| `button` | Filters, load more |
| `select` | Filter dropdowns |
| `input` | Search |
| `table` | Activity list |
| `separator` | Date separators |

**React Custom Components:**

```typescript
// components/activity/ActivityLog.tsx
interface ActivityLogProps {
  activities: Activity[];
  filters: ActivityFilters;
  onFiltersChange: (filters: ActivityFilters) => void;
  onLoadMore: () => void;
  hasMore: boolean;
}

// Main activity log
// Composition: Uses ShadCN Card, Table
```

```typescript
// components/activity/ActivityItem.tsx
interface ActivityItemProps {
  activity: Activity;
  onDealClick: (dealId: string) => void;
  onUserClick: (userId: string) => void;
}

// Individual activity item
// Composition: Uses ShadCN Card, Avatar, Badge
```

```typescript
// components/activity/ActivityFilters.tsx
interface ActivityFiltersProps {
  filters: ActivityFilters;
  onChange: (filters: ActivityFilters) => void;
  users: User[];
  actionTypes: string[];
}

// Activity filter controls
// Composition: Uses ShadCN Select, Input, DatePicker
```

#### 3.5.3 Data Requirements

```typescript
interface Activity {
  id: string;
  
  // Association
  dealId?: string;
  deal?: {
    id: string;
    propertyAddress: string;
    borrowerName: string;
  };
  
  // Actor
  userId?: string;
  user?: User;
  systemGenerated: boolean;
  
  // Action
  action: ActivityAction;
  actionLabel: string;
  
  // Details
  description: string;
  details?: Record<string, any>;
  
  // Metadata
  ipAddress?: string;
  userAgent?: string;
  
  timestamp: Date;
}

type ActivityAction = 
  | 'deal_created'
  | 'deal_updated'
  | 'stage_changed'
  | 'document_uploaded'
  | 'document_classified'
  | 'document_rejected'
  | 'quote_generated'
  | 'quote_sent'
  | 'quote_accepted'
  | 'term_sheet_signed'
  | 'report_ordered'
  | 'report_received'
  | 'analysis_completed'
  | 'flag_created'
  | 'flag_resolved'
  | 'exception_requested'
  | 'exception_approved'
  | 'exception_denied'
  | 'credit_memo_generated'
  | 'credit_memo_approved'
  | 'task_created'
  | 'task_completed'
  | 'note_added'
  | 'email_sent'
  | 'user_assigned';
```

---

### 3.6 Global Search

#### 3.6.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | Quick search across deals, borrowers, addresses |
| **Activation** | Cmd+K / Ctrl+K or search icon |
| **PRD Reference** | Phase 8 PRD, Section 8 |

#### 3.6.2 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `command` | Command palette |
| `dialog` | Search modal |
| `input` | Search input |
| `badge` | Result type badges |

**React Custom Components:**

```typescript
// components/search/GlobalSearch.tsx
interface GlobalSearchProps {
  open: boolean;
  onClose: () => void;
  onSelect: (result: SearchResult) => void;
}

// Global search command palette
// Composition: Uses ShadCN Command
```

```typescript
// components/search/SearchResults.tsx
interface SearchResultsProps {
  query: string;
  results: SearchResult[];
  isLoading: boolean;
  onSelect: (result: SearchResult) => void;
}

// Search results display
// Composition: Uses ShadCN Command items
```

#### 3.6.3 Search Configuration

```typescript
interface SearchResult {
  id: string;
  type: 'deal' | 'borrower' | 'property' | 'document';
  title: string;
  subtitle: string;
  url: string;
  metadata?: Record<string, any>;
}

const SEARCH_CONFIG = {
  // Searchable fields by type
  deal: ['propertyAddress', 'borrowerName', 'loanNumber', 'dealId'],
  borrower: ['name', 'entityName', 'email', 'phone'],
  property: ['address', 'city', 'state', 'zip'],
  document: ['filename', 'documentType'],
  
  // Keyboard shortcuts
  shortcuts: [
    { key: 'k', modifier: 'meta', action: 'open_search' },
    { key: 'k', modifier: 'ctrl', action: 'open_search' },
    { key: 'Escape', action: 'close_search' },
  ],
  
  // Recent searches
  maxRecentSearches: 5,
};
```

---

### 3.7 Notifications

#### 3.7.1 Overview

| Attribute | Value |
|-----------|-------|
| **Purpose** | In-app, email, and SMS notifications |
| **Entry Points** | Header bell icon, /notifications |
| **PRD Reference** | Phase 8 PRD, Section 9 |

#### 3.7.2 Component Breakdown

**ShadCN Components:**
| Component | Usage |
|-----------|-------|
| `popover` | Notification dropdown |
| `card` | Notification cards |
| `badge` | Unread count |
| `button` | Mark read, settings |
| `switch` | Notification preferences |
| `tabs` | Notification categories |

**React Custom Components:**

```typescript
// components/notifications/NotificationBell.tsx
interface NotificationBellProps {
  unreadCount: number;
  onClick: () => void;
}

// Header notification bell
// Composition: Uses ShadCN Badge, Button
```

```typescript
// components/notifications/NotificationDropdown.tsx
interface NotificationDropdownProps {
  notifications: Notification[];
  onNotificationClick: (id: string) => void;
  onMarkAllRead: () => void;
  onViewAll: () => void;
}

// Notification dropdown
// Composition: Uses ShadCN Popover, Card
```

```typescript
// components/notifications/NotificationItem.tsx
interface NotificationItemProps {
  notification: Notification;
  onClick: () => void;
  onDismiss: () => void;
}

// Individual notification
// Composition: Uses ShadCN Card, Badge
```

```typescript
// components/notifications/NotificationPreferences.tsx
interface NotificationPreferencesProps {
  preferences: NotificationPreferences;
  onChange: (preferences: NotificationPreferences) => void;
}

// Notification settings
// Composition: Uses ShadCN Switch, Card
```

#### 3.7.3 Data Requirements

```typescript
interface Notification {
  id: string;
  userId: string;
  
  // Content
  type: NotificationType;
  title: string;
  message: string;
  
  // Association
  dealId?: string;
  deal?: {
    id: string;
    propertyAddress: string;
  };
  
  // Status
  read: boolean;
  readAt?: Date;
  
  // Action
  actionUrl?: string;
  actionLabel?: string;
  
  // Delivery
  channels: ('in_app' | 'email' | 'sms')[];
  emailSentAt?: Date;
  smsSentAt?: Date;
  
  createdAt: Date;
}

type NotificationType = 
  | 'deal_assigned'
  | 'stage_changed'
  | 'document_uploaded'
  | 'document_rejected'
  | 'quote_expiring'
  | 'rate_lock_expiring'
  | 'sla_at_risk'
  | 'sla_breached'
  | 'task_assigned'
  | 'task_due'
  | 'task_overdue'
  | 'exception_approved'
  | 'exception_denied'
  | 'credit_memo_ready'
  | 'closing_scheduled'
  | 'deal_funded';

interface NotificationPreferences {
  userId: string;
  
  // Channel preferences by type
  preferences: {
    type: NotificationType;
    inApp: boolean;
    email: boolean;
    sms: boolean;
  }[];
  
  // Digest settings
  emailDigest: 'immediate' | 'hourly' | 'daily' | 'never';
  quietHours?: {
    start: string; // "22:00"
    end: string;   // "08:00"
  };
}
```

---

## 4. SLA Tracking

### 4.1 SLA Configuration (from PRD Section 7.3)

```typescript
const SLA_CONFIG: Record<string, SLAConfig> = {
  prospect: {
    target: 5,
    unit: 'business_days',
    warningThreshold: 0.8, // 80% = 4 days
    escalation: ['loan_officer'],
  },
  application: {
    target: 7,
    unit: 'business_days',
    warningThreshold: 0.8,
    escalation: ['loan_officer', 'processor'],
  },
  quote: {
    target: 3,
    unit: 'business_days',
    warningThreshold: 0.67,
    escalation: ['loan_officer'],
  },
  initial_uw: {
    target: 5,
    unit: 'business_days',
    warningThreshold: 0.8,
    escalation: ['underwriter'],
  },
  processing: {
    target: 10,
    unit: 'business_days',
    warningThreshold: 0.8,
    escalation: ['processor', 'loan_officer'],
  },
  underwriting: {
    target: 7,
    unit: 'business_days',
    warningThreshold: 0.8,
    escalation: ['underwriter', 'credit_manager'],
  },
  closing: {
    target: 5,
    unit: 'business_days',
    warningThreshold: 0.8,
    escalation: ['closer', 'loan_officer'],
  },
};

interface SLAStatus {
  dealId: string;
  stage: string;
  
  // Timing
  stageEnteredAt: Date;
  targetDate: Date;
  businessDaysInStage: number;
  
  // Status
  status: 'on_track' | 'at_risk' | 'breached';
  percentComplete: number;
  
  // Escalation
  escalationSent: boolean;
  escalationSentAt?: Date;
}
```

### 4.2 SLA Dashboard Widget

```typescript
// components/sla/SLADashboardWidget.tsx
interface SLADashboardWidgetProps {
  compliance: number;
  atRisk: number;
  breached: number;
  byStage: {
    stage: string;
    onTrack: number;
    atRisk: number;
    breached: number;
  }[];
}

// SLA overview widget
// Composition: Uses ShadCN Card, Progress, Badge
```

---

## 5. API Contract (Mock)

### 5.1 Dashboard Endpoints

```typescript
// GET /api/dashboard
// Get dashboard data
interface GetDashboardResponse {
  kpis: DashboardKPIs;
  needsAttention: NeedsAttentionItem[];
  tasksDueToday: Task[];
  pipelineByStage: PipelineStageCount[];
  recentActivity: Activity[];
}

// GET /api/dashboard/kpis
// Get KPIs only
interface GetKPIsResponse {
  kpis: DashboardKPIs;
}
```

### 5.2 Pipeline Endpoints

```typescript
// GET /api/pipeline
// Get pipeline data
interface GetPipelineRequest {
  filters?: PipelineFilters;
}

interface GetPipelineResponse {
  deals: Deal[];
  stageCounts: Record<string, number>;
}

// PUT /api/deals/:id/stage
// Change deal stage
interface ChangeStageRequest {
  stage: string;
  reason?: string;
}

interface ChangeStageResponse {
  deal: Deal;
  activity: Activity;
}
```

### 5.3 Task Endpoints

```typescript
// GET /api/tasks
// Get tasks
interface GetTasksRequest {
  filters?: TaskFilters;
  page?: number;
  limit?: number;
}

interface GetTasksResponse {
  tasks: Task[];
  total: number;
  page: number;
  pages: number;
}

// POST /api/tasks
// Create task
interface CreateTaskRequest {
  title: string;
  description?: string;
  dealId?: string;
  assignedTo?: string;
  dueDate?: string;
  priority: string;
  category: string;
}

interface CreateTaskResponse {
  task: Task;
}

// PUT /api/tasks/:id
// Update task
interface UpdateTaskRequest {
  title?: string;
  description?: string;
  assignedTo?: string;
  dueDate?: string;
  priority?: string;
  status?: string;
}

interface UpdateTaskResponse {
  task: Task;
}

// POST /api/tasks/:id/complete
// Complete task
interface CompleteTaskResponse {
  task: Task;
}
```

### 5.4 Activity Endpoints

```typescript
// GET /api/activity
// Get activity log
interface GetActivityRequest {
  filters?: ActivityFilters;
  page?: number;
  limit?: number;
}

interface GetActivityResponse {
  activities: Activity[];
  total: number;
  page: number;
  pages: number;
}

// GET /api/deals/:id/activity
// Get deal activity
interface GetDealActivityResponse {
  activities: Activity[];
}
```

### 5.5 Search Endpoints

```typescript
// GET /api/search
// Global search
interface SearchRequest {
  query: string;
  types?: ('deal' | 'borrower' | 'property' | 'document')[];
  limit?: number;
}

interface SearchResponse {
  results: SearchResult[];
  total: number;
}
```

### 5.6 Notification Endpoints

```typescript
// GET /api/notifications
// Get notifications
interface GetNotificationsRequest {
  unreadOnly?: boolean;
  page?: number;
  limit?: number;
}

interface GetNotificationsResponse {
  notifications: Notification[];
  unreadCount: number;
  total: number;
}

// PUT /api/notifications/:id/read
// Mark notification read
interface MarkReadResponse {
  notification: Notification;
}

// PUT /api/notifications/read-all
// Mark all read
interface MarkAllReadResponse {
  count: number;
}

// GET /api/notifications/preferences
// Get preferences
interface GetPreferencesResponse {
  preferences: NotificationPreferences;
}

// PUT /api/notifications/preferences
// Update preferences
interface UpdatePreferencesRequest {
  preferences: NotificationPreferences;
}

interface UpdatePreferencesResponse {
  preferences: NotificationPreferences;
}
```

---

## 6. Real-Time Updates

### 6.1 WebSocket Events

```typescript
const WEBSOCKET_EVENTS = {
  // Pipeline updates
  'deal:created': (deal: Deal) => void,
  'deal:updated': (deal: Deal) => void,
  'deal:stage_changed': (data: { dealId: string; from: string; to: string }) => void,
  
  // Task updates
  'task:created': (task: Task) => void,
  'task:updated': (task: Task) => void,
  'task:completed': (taskId: string) => void,
  
  // Notifications
  'notification:new': (notification: Notification) => void,
  
  // Activity
  'activity:new': (activity: Activity) => void,
  
  // SLA alerts
  'sla:at_risk': (data: { dealId: string; stage: string }) => void,
  'sla:breached': (data: { dealId: string; stage: string }) => void,
};
```

### 6.2 Real-Time Hook

```typescript
// hooks/useRealTimeUpdates.ts
function useRealTimeUpdates() {
  const { subscribe, unsubscribe } = useWebSocket();
  
  useEffect(() => {
    // Subscribe to relevant events
    subscribe('deal:updated', handleDealUpdate);
    subscribe('task:created', handleTaskCreate);
    subscribe('notification:new', handleNewNotification);
    
    return () => {
      unsubscribe('deal:updated', handleDealUpdate);
      unsubscribe('task:created', handleTaskCreate);
      unsubscribe('notification:new', handleNewNotification);
    };
  }, []);
}
```

---

## 7. Background Jobs

| Job | Frequency | Purpose |
|-----|-----------|---------|
| `check-sla-status` | Every 15 min | Update SLA status, send alerts |
| `send-task-reminders` | Daily 8am | Send task due reminders |
| `generate-daily-digest` | Daily 6am | Email digest of activity |
| `cleanup-old-notifications` | Daily | Archive old notifications |
| `recalculate-kpis` | Every hour | Update dashboard KPIs |
| `sync-activity-log` | Continuous | Real-time activity logging |

---

## 8. Open Questions & Assumptions

### 8.1 Open Questions

| # | Question | Impact | Owner |
|---|----------|--------|-------|
| 1 | Drag-and-drop library preference? | UX | Engineering |
| 2 | WebSocket vs SSE for real-time? | Architecture | Engineering |
| 3 | Email digest frequency options? | User preference | Product |
| 4 | Mobile app notifications? | Scope | Product |

### 8.2 Assumptions Made

| # | Assumption | Rationale |
|---|------------|-----------|
| 1 | WebSocket for real-time updates | Better for bidirectional |
| 2 | Business days for SLA calculation | Standard practice |
| 3 | Notifications stored 90 days | Reasonable retention |
| 4 | Search indexes updated in real-time | Best UX |

---

## 9. Implementation Checklist

### 9.1 Home Dashboard

- [ ] KPI cards
- [ ] KPI calculations
- [ ] Needs attention logic
- [ ] Needs attention display
- [ ] Tasks due today
- [ ] Pipeline overview chart
- [ ] Recent activity feed
- [ ] Real-time updates

### 9.2 Pipeline Board

- [ ] Kanban layout
- [ ] Stage columns
- [ ] Deal cards
- [ ] Drag-and-drop
- [ ] Stage transition validation
- [ ] Filters (loan type, assignee, SLA)
- [ ] Search
- [ ] SLA indicators
- [ ] Real-time updates

### 9.3 Deal Dashboard

- [ ] Deal header
- [ ] Tab navigation
- [ ] Overview tab
- [ ] Checklist tab
- [ ] Documents tab
- [ ] Analysis tab
- [ ] Activity tab
- [ ] Notes tab
- [ ] Quick actions
- [ ] Stage change

### 9.4 Task Management

- [ ] Task list view
- [ ] Task filters
- [ ] Quick task creation
- [ ] Task detail modal
- [ ] Task assignment
- [ ] Task completion
- [ ] Due date reminders
- [ ] Task categories

### 9.5 Activity & Audit

- [ ] Activity log page
- [ ] Activity filters
- [ ] Activity item display
- [ ] Deal activity view
- [ ] Activity logging service
- [ ] Audit trail storage

### 9.6 Global Features

- [ ] Global search (Cmd+K)
- [ ] Search indexing
- [ ] Notification bell
- [ ] Notification dropdown
- [ ] Notification preferences
- [ ] Email notifications
- [ ] SMS notifications (optional)
- [ ] WebSocket integration

### 9.7 SLA Tracking

- [ ] SLA calculation service
- [ ] SLA status indicators
- [ ] SLA dashboard widget
- [ ] SLA breach alerts
- [ ] SLA reporting

### 9.8 Testing

- [ ] Unit tests: KPI calculations
- [ ] Unit tests: SLA calculations
- [ ] Unit tests: Needs attention logic
- [ ] Integration tests: Pipeline operations
- [ ] Integration tests: Task management
- [ ] E2E tests: Full dashboard flow
- [ ] E2E tests: Pipeline drag-drop
- [ ] Performance tests: Dashboard load
- [ ] WebSocket tests: Real-time updates

---

## 10. UW Manual Integration

This section maps Phase 8 implementation components to the USDV Underwriting Manual sections. Phase 8 primarily uses the manual for closing checklist validation and document currency checks.

### 10.1 Manual Section Cross-References

| Implementation Component | UW Manual Section | Usage |
|--------------------------|-------------------|-------|
| **Closing Checklist** | | |
| Required closing documents | Section 13.6: Closing Documents | Complete closing doc list |
| Final verification checks | Section 13.8: Currency Requirements | Pre-close validation |
| Document expiration recheck | Section 13.8: Currency Requirements | Currency validation |
| Title requirements | Section 14.4: Title Analysis | Final title requirements |
| Insurance requirements | Section 14.5: Insurance Analysis | Final insurance requirements |
| **Pipeline Stage Definitions** | | |
| Stage progression rules | Section 1: Investment Philosophy | Loan lifecycle stages |
| Stage-specific requirements | Section 13: Document Requirements | What's needed at each stage |
| **SLA Tracking** | | |
| Phase duration targets | Internal SLA (not in manual) | Operational targets |

### 10.2 Closing Checklist from Manual

Reference Section 13.6 for closing document requirements:

**Required Closing Documents:**

| Document | RTL | DSCR | Responsibility |
|----------|-----|------|----------------|
| Final Title Commitment | ✓ | ✓ | Title Company |
| Title Policy | ✓ | ✓ | Title Company |
| Closing Protection Letter | ✓ | ✓ | Title Company |
| HUD-1 / Settlement Statement | ✓ | ✓ | Title Company |
| Escrow Instructions | ✓ | ✓ | Title Company |
| Wire Instructions | ✓ | ✓ | Title Company |
| Final Insurance Certificate | ✓ | ✓ | Borrower/Agent |
| Flood Insurance (if required) | ✓ | ✓ | Borrower/Agent |
| Signed Loan Documents | ✓ | ✓ | Borrower |
| Entity Resolution | ✓ | ✓ | Borrower |
| Funding Authorization | ✓ | ✓ | Internal |

### 10.3 Pre-Close Verification Checklist

From Section 13.8, verify before closing:

| Check | Requirement | Action if Failed |
|-------|-------------|------------------|
| Credit Report Currency | < 120 days | Re-pull credit |
| Appraisal Currency | < 120 days | Update or new appraisal |
| Title Commitment Currency | < 30 days | Update title |
| Insurance Effective | Covers loan term | Update policy |
| Bank Statements | < 90 days | Request updated statements |
| Good Standing | < 90 days | Request updated certificate |
| All Flags Resolved | No open red flags | Resolve or exception |
| All Exceptions Approved | Approved status | Obtain approval |

### 10.4 Stage-to-Document Mapping

Map pipeline stages to required document completion:

| Stage | Required Documents (from Manual) | Completion % |
|-------|----------------------------------|--------------|
| Prospect | None | 0% |
| Application | Quick App + Full App | 10% |
| Quote | Application complete | 15% |
| Initial UW | Credit + Background ordered | 25% |
| Processing | All borrower docs, reports ordered | 50% |
| Underwriting | All docs received, analysis complete | 75% |
| Closing | Closing docs, final verifications | 95% |
| Funded | All docs executed | 100% |

### 10.5 Glossary Integration for UI

Use Section 16 (Glossary) for pipeline and dashboard terminology:

**Pipeline Stage Definitions:**
- **Prospect**: Initial inquiry, pre-qualification pending
- **Application**: Full application submitted, awaiting review
- **Quote**: Quote generated, awaiting borrower acceptance
- **Initial UW**: Initial underwriting review, reports ordering
- **Processing**: Document collection and verification
- **Underwriting**: Full underwriting review and credit memo
- **Closing**: Final docs and funding preparation
- **Funded**: Loan funded and closed

**Dashboard Metric Definitions:**
- **Pull-Through Rate**: % of applications that fund
- **SLA Compliance**: % of deals within stage time targets
- **Pipeline Volume**: Total $ amount of active deals
- **Days to Close**: Average days from application to funding

### 10.6 "Needs Attention" Logic from Manual

Map "Needs Attention" reasons to manual sections:

| Attention Reason | Manual Reference | Threshold |
|------------------|------------------|-----------|
| Document Expiring | Section 13.8 | 14 days before expiration |
| Quote Expiring | Section 11.14 | 3 days before expiration |
| Rate Lock Expiring | Section 11.14 | 5 days before expiration |
| Red Flag Unresolved | Section 14 | Any unresolved red flag |
| Exception Pending | Section 12 | Any pending exception |
| Missing Documents | Section 13 | Required doc not received |

### 10.7 Checklist Category Mapping

Map deal dashboard checklist categories to manual sections:

| Checklist Category | Manual Section | Auto-Populated Items |
|--------------------|----------------|---------------------|
| Borrower | Section 13.3 | Credit report, background check |
| Property | Section 13.4 | Appraisal, title, flood |
| Third-Party | Section 13.5 | All ordered reports |
| Underwriting | Section 15 | Sizing, quote, credit memo |
| Closing | Section 13.6 | Title policy, HUD, CPL |

### 10.8 Python Library Integration

| Validation Need | Python Class | Method |
|-----------------|--------------|--------|
| Document currency check | `DiligenceChecker` | `check_document_currency()` |
| Closing checklist generation | `DiligenceChecker` | `generate_closing_checklist()` |
| Pre-close validation | `DiligenceChecker` | `validate_pre_close()` |

---

*End of Phase 8 Implementation Plan*

