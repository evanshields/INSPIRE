# INSPIRE Shared Components Catalog

**Document Version:** 1.0  
**Last Updated:** December 2024  
**Status:** Implementation Ready

---

## 1. Overview

This document catalogs all shared components used across multiple phases of the INSPIRE loan origination system. Components are organized by category and include ShadCN base components, custom React components, and composition patterns.

---

## 2. Layout Components

### 2.1 NavigationShell

**Used In:** All pages  
**Purpose:** Main application shell with sidebar navigation and header

```typescript
// components/layout/NavigationShell.tsx
interface NavigationShellProps {
  children: React.ReactNode;
  user: User;
  notifications: Notification[];
  onSearch: () => void;
}

// ShadCN Components Used:
// - Sheet (mobile sidebar)
// - Button
// - Avatar
// - DropdownMenu
// - Badge (notification count)
```

### 2.2 DealHeader

**Used In:** All deal detail pages (P8-03, and all deal sub-routes)  
**Purpose:** Consistent deal header with key info and actions

```typescript
// components/layout/DealHeader.tsx
interface DealHeaderProps {
  deal: Deal;
  onStageChange: (stage: string) => void;
  onQuickAction: (action: string) => void;
  breadcrumbs?: Breadcrumb[];
}

// ShadCN Components Used:
// - Badge (status, loan type, flags)
// - Button
// - DropdownMenu (quick actions)
// - Breadcrumb
```

### 2.3 PageHeader

**Used In:** All list/dashboard pages  
**Purpose:** Page title with actions

```typescript
// components/layout/PageHeader.tsx
interface PageHeaderProps {
  title: string;
  description?: string;
  actions?: React.ReactNode;
  breadcrumbs?: Breadcrumb[];
}

// ShadCN Components Used:
// - Breadcrumb
```

---

## 3. Data Display Components

### 3.1 MetricCard

**Used In:** P3-01, P8-01, P8-03  
**Purpose:** Display key metrics with optional change indicator

```typescript
// components/cards/MetricCard.tsx
interface MetricCardProps {
  title: string;
  value: string | number;
  format?: 'currency' | 'percent' | 'number';
  change?: {
    value: number;
    direction: 'up' | 'down';
    period: string;
  };
  icon?: React.ReactNode;
  size?: 'sm' | 'md' | 'lg';
  onClick?: () => void;
}

// ShadCN Components Used:
// - Card
// - Badge (change indicator)
```

### 3.2 MetricTile

**Used In:** P3-01, P3-02, P7-05  
**Purpose:** Compact metric display for dashboards

```typescript
// components/cards/MetricTile.tsx
interface MetricTileProps {
  label: string;
  value: string | number;
  format?: 'currency' | 'percent' | 'number';
  variant?: 'default' | 'success' | 'warning' | 'danger';
  size?: 'sm' | 'md';
}

// ShadCN Components Used:
// - Card (optional)
// - Badge
```

### 3.3 DataTable

**Used In:** All list views  
**Purpose:** Reusable data table with sorting, filtering, pagination

```typescript
// components/tables/DataTable.tsx
interface DataTableProps<T> {
  data: T[];
  columns: ColumnDef<T>[];
  searchable?: boolean;
  searchPlaceholder?: string;
  filters?: FilterConfig[];
  pagination?: boolean;
  pageSize?: number;
  onRowClick?: (row: T) => void;
  emptyState?: React.ReactNode;
  isLoading?: boolean;
}

// ShadCN Components Used:
// - Table
// - Input (search)
// - Select (filters)
// - Button (pagination)
// - Skeleton (loading)
```

### 3.4 StatusBadge

**Used In:** All deal-related pages  
**Purpose:** Consistent status display

```typescript
// components/shared/StatusBadge.tsx
interface StatusBadgeProps {
  status: string;
  type?: 'deal' | 'document' | 'task' | 'quote' | 'report';
  size?: 'sm' | 'md';
}

// Status color mapping
const STATUS_COLORS = {
  deal: {
    prospect: 'slate',
    application: 'blue',
    quote: 'indigo',
    processing: 'purple',
    underwriting: 'violet',
    closing: 'pink',
    funded: 'green',
    archived: 'gray',
  },
  document: {
    required: 'yellow',
    received: 'green',
    rejected: 'red',
    waived: 'gray',
  },
  task: {
    pending: 'yellow',
    in_progress: 'blue',
    completed: 'green',
    cancelled: 'gray',
  },
  // ... more mappings
};

// ShadCN Components Used:
// - Badge
```

### 3.5 FlagIndicator

**Used In:** P7-01, P7-03, P8-02, P8-03  
**Purpose:** Display flag counts with severity colors

```typescript
// components/flags/FlagIndicator.tsx
interface FlagIndicatorProps {
  redCount: number;
  yellowCount: number;
  greenCount?: number;
  showLabels?: boolean;
  onClick?: () => void;
}

// ShadCN Components Used:
// - Badge
// - Tooltip
```

### 3.6 SLAIndicator

**Used In:** P8-01, P8-02, P8-03  
**Purpose:** Visual SLA status display

```typescript
// components/sla/SLAIndicator.tsx
interface SLAIndicatorProps {
  daysInStage: number;
  slaTarget: number;
  showProgress?: boolean;
  size?: 'sm' | 'md';
}

// Status calculation
// on_track: daysInStage < slaTarget * 0.8
// at_risk: daysInStage >= slaTarget * 0.8 && daysInStage <= slaTarget
// breached: daysInStage > slaTarget

// ShadCN Components Used:
// - Badge
// - Progress (optional)
// - Tooltip
```

---

## 4. Form Components

### 4.1 FormSection

**Used In:** P1-01, P1-02, P2-01  
**Purpose:** Grouping form fields with title

```typescript
// components/forms/FormSection.tsx
interface FormSectionProps {
  title: string;
  description?: string;
  children: React.ReactNode;
  collapsible?: boolean;
  defaultExpanded?: boolean;
}

// ShadCN Components Used:
// - Card
// - Collapsible (if collapsible)
// - Separator
```

### 4.2 AddressInput

**Used In:** P1-01, P2-01  
**Purpose:** Address autocomplete with Google Places

```typescript
// components/forms/AddressInput.tsx
interface AddressInputProps {
  value: Address;
  onChange: (address: Address) => void;
  label?: string;
  required?: boolean;
  error?: string;
}

interface Address {
  street: string;
  unit?: string;
  city: string;
  state: string;
  zip: string;
  county?: string;
  lat?: number;
  lng?: number;
}

// ShadCN Components Used:
// - Input
// - Label
// - Command (autocomplete dropdown)
```

### 4.3 CurrencyInput

**Used In:** P1-01, P2-01, P3-01  
**Purpose:** Formatted currency input

```typescript
// components/forms/CurrencyInput.tsx
interface CurrencyInputProps {
  value: number | undefined;
  onChange: (value: number | undefined) => void;
  label?: string;
  placeholder?: string;
  min?: number;
  max?: number;
  required?: boolean;
  error?: string;
}

// ShadCN Components Used:
// - Input
// - Label
```

### 4.4 PercentInput

**Used In:** P3-01, P3-02  
**Purpose:** Formatted percentage input

```typescript
// components/forms/PercentInput.tsx
interface PercentInputProps {
  value: number | undefined;
  onChange: (value: number | undefined) => void;
  label?: string;
  decimalPlaces?: number;
  min?: number;
  max?: number;
  required?: boolean;
  error?: string;
}

// ShadCN Components Used:
// - Input
// - Label
```

### 4.5 PhoneInput

**Used In:** P1-01, P2-01  
**Purpose:** Formatted phone number input

```typescript
// components/forms/PhoneInput.tsx
interface PhoneInputProps {
  value: string;
  onChange: (value: string) => void;
  label?: string;
  required?: boolean;
  error?: string;
}

// ShadCN Components Used:
// - Input
// - Label
```

### 4.6 SSNInput

**Used In:** P2-01  
**Purpose:** Masked SSN input with security

```typescript
// components/forms/SSNInput.tsx
interface SSNInputProps {
  value: string;
  onChange: (value: string) => void;
  label?: string;
  required?: boolean;
  error?: string;
  showMasked?: boolean;
}

// ShadCN Components Used:
// - Input
// - Label
// - Button (show/hide toggle)
```

### 4.7 FileUploader

**Used In:** P2-01, P6-02  
**Purpose:** Drag-and-drop file upload

```typescript
// components/upload/FileUploader.tsx
interface FileUploaderProps {
  onUpload: (files: File[]) => Promise<void>;
  accept?: string[];
  maxSize?: number; // bytes
  maxFiles?: number;
  multiple?: boolean;
  disabled?: boolean;
}

// ShadCN Components Used:
// - Card
// - Progress
// - Button
```

---

## 5. Dialog Components

### 5.1 ConfirmDialog

**Used In:** All pages with destructive actions  
**Purpose:** Confirmation modal for important actions

```typescript
// components/dialogs/ConfirmDialog.tsx
interface ConfirmDialogProps {
  open: boolean;
  onConfirm: () => void;
  onCancel: () => void;
  title: string;
  description: string;
  confirmLabel?: string;
  cancelLabel?: string;
  variant?: 'default' | 'destructive';
  isLoading?: boolean;
}

// ShadCN Components Used:
// - AlertDialog
// - Button
```

### 5.2 QuickViewDialog

**Used In:** P8-02 (Pipeline)  
**Purpose:** Quick deal preview without navigation

```typescript
// components/dialogs/QuickViewDialog.tsx
interface QuickViewDialogProps {
  deal: Deal;
  open: boolean;
  onClose: () => void;
  onViewFull: () => void;
}

// ShadCN Components Used:
// - Dialog
// - Card
// - Badge
// - Button
```

---

## 6. Activity & Timeline Components

### 6.1 ActivityItem

**Used In:** P8-01, P8-03, P8-05  
**Purpose:** Single activity log entry

```typescript
// components/activity/ActivityItem.tsx
interface ActivityItemProps {
  activity: Activity;
  showDeal?: boolean;
  onDealClick?: (dealId: string) => void;
}

// ShadCN Components Used:
// - Avatar
// - Badge
```

### 6.2 ActivityFeed

**Used In:** P8-01, P8-03  
**Purpose:** List of recent activities

```typescript
// components/activity/ActivityFeed.tsx
interface ActivityFeedProps {
  activities: Activity[];
  maxItems?: number;
  onViewAll?: () => void;
  onActivityClick?: (activity: Activity) => void;
}

// ShadCN Components Used:
// - Card
// - Button
// - Separator
```

### 6.3 Timeline

**Used In:** P8-03  
**Purpose:** Visual timeline of deal progress

```typescript
// components/timeline/Timeline.tsx
interface TimelineProps {
  events: TimelineEvent[];
  orientation?: 'vertical' | 'horizontal';
}

interface TimelineEvent {
  id: string;
  title: string;
  description?: string;
  timestamp: Date;
  status: 'completed' | 'current' | 'upcoming';
  icon?: React.ReactNode;
}

// ShadCN Components Used:
// - Badge
```

---

## 7. Task Components

### 7.1 TaskItem

**Used In:** P8-01, P8-03, P8-04  
**Purpose:** Single task display with actions

```typescript
// components/tasks/TaskItem.tsx
interface TaskItemProps {
  task: Task;
  onComplete: () => void;
  onClick: () => void;
  showDeal?: boolean;
}

// ShadCN Components Used:
// - Checkbox
// - Badge
// - Avatar
// - Button
```

### 7.2 TaskList

**Used In:** P8-01, P8-03  
**Purpose:** List of tasks

```typescript
// components/tasks/TaskList.tsx
interface TaskListProps {
  tasks: Task[];
  onTaskComplete: (taskId: string) => void;
  onTaskClick: (taskId: string) => void;
  emptyMessage?: string;
}

// ShadCN Components Used:
// - Card
```

---

## 8. Document Components

### 8.1 DocumentCard

**Used In:** P6-01, P6-03, P6-04  
**Purpose:** Document display with status

```typescript
// components/documents/DocumentCard.tsx
interface DocumentCardProps {
  document: Document;
  onView: () => void;
  onDownload: () => void;
  onDelete?: () => void;
  showStatus?: boolean;
}

// ShadCN Components Used:
// - Card
// - Badge
// - Button
// - DropdownMenu
```

### 8.2 DocumentList

**Used In:** P6-01, P8-03  
**Purpose:** List of documents

```typescript
// components/documents/DocumentList.tsx
interface DocumentListProps {
  documents: Document[];
  onView: (docId: string) => void;
  onDownload: (docId: string) => void;
  groupBy?: 'category' | 'type' | 'date';
}

// ShadCN Components Used:
// - Table
// - Badge
// - Button
```

---

## 9. Quote & Pricing Components

### 9.1 QuoteCard

**Used In:** P4-01, P4-02  
**Purpose:** Quote scenario display

```typescript
// components/quotes/QuoteCard.tsx
interface QuoteCardProps {
  quote: QuoteScenario;
  isSelected?: boolean;
  isRecommended?: boolean;
  onSelect: () => void;
  onViewDetails: () => void;
}

// ShadCN Components Used:
// - Card
// - Badge
// - Button
```

### 9.2 PricingTable

**Used In:** P3-01, P4-01  
**Purpose:** Loan pricing breakdown

```typescript
// components/pricing/PricingTable.tsx
interface PricingTableProps {
  pricing: LoanPricing;
  showDetails?: boolean;
}

interface LoanPricing {
  rate: number;
  originationFee: number;
  originationAmount: number;
  processingFee: number;
  thirdPartyDeposit: number;
  totalClosingCosts: number;
  monthlyPayment: number;
}

// ShadCN Components Used:
// - Table
// - Separator
```

---

## 10. Notification Components

### 10.1 NotificationItem

**Used In:** P8-08  
**Purpose:** Single notification display

```typescript
// components/notifications/NotificationItem.tsx
interface NotificationItemProps {
  notification: Notification;
  onClick: () => void;
  onDismiss: () => void;
}

// ShadCN Components Used:
// - Card
// - Badge
// - Button
```

### 10.2 NotificationBell

**Used In:** NavigationShell (all pages)  
**Purpose:** Header notification indicator

```typescript
// components/notifications/NotificationBell.tsx
interface NotificationBellProps {
  unreadCount: number;
  onClick: () => void;
}

// ShadCN Components Used:
// - Button
// - Badge
// - Popover
```

---

## 11. Search Components

### 11.1 GlobalSearch

**Used In:** All pages (Cmd+K)  
**Purpose:** Global search command palette

```typescript
// components/search/GlobalSearch.tsx
interface GlobalSearchProps {
  open: boolean;
  onClose: () => void;
  onSelect: (result: SearchResult) => void;
}

// ShadCN Components Used:
// - Command
// - Dialog
// - Badge
```

### 11.2 SearchInput

**Used In:** Various list pages  
**Purpose:** Inline search input

```typescript
// components/search/SearchInput.tsx
interface SearchInputProps {
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  onClear?: () => void;
}

// ShadCN Components Used:
// - Input
// - Button
```

---

## 12. Empty States

### 12.1 EmptyState

**Used In:** All list views  
**Purpose:** Display when no data available

```typescript
// components/shared/EmptyState.tsx
interface EmptyStateProps {
  icon?: React.ReactNode;
  title: string;
  description?: string;
  action?: {
    label: string;
    onClick: () => void;
  };
}

// ShadCN Components Used:
// - Card (optional)
// - Button
```

---

## 13. Loading States

### 13.1 PageLoader

**Used In:** All pages  
**Purpose:** Full page loading state

```typescript
// components/loading/PageLoader.tsx
interface PageLoaderProps {
  message?: string;
}

// ShadCN Components Used:
// - Skeleton
```

### 13.2 CardSkeleton

**Used In:** Dashboard, lists  
**Purpose:** Card loading skeleton

```typescript
// components/loading/CardSkeleton.tsx
interface CardSkeletonProps {
  lines?: number;
  showAvatar?: boolean;
}

// ShadCN Components Used:
// - Card
// - Skeleton
```

### 13.3 TableSkeleton

**Used In:** All table views  
**Purpose:** Table loading skeleton

```typescript
// components/loading/TableSkeleton.tsx
interface TableSkeletonProps {
  rows?: number;
  columns?: number;
}

// ShadCN Components Used:
// - Table
// - Skeleton
```

---

## 14. Utility Components

### 14.1 CopyButton

**Used In:** Various (deal IDs, links)  
**Purpose:** Copy to clipboard with feedback

```typescript
// components/shared/CopyButton.tsx
interface CopyButtonProps {
  value: string;
  label?: string;
}

// ShadCN Components Used:
// - Button
// - Tooltip
```

### 14.2 ExternalLink

**Used In:** Various  
**Purpose:** Link that opens in new tab

```typescript
// components/shared/ExternalLink.tsx
interface ExternalLinkProps {
  href: string;
  children: React.ReactNode;
}
```

### 14.3 FormattedDate

**Used In:** All pages with dates  
**Purpose:** Consistent date formatting

```typescript
// components/shared/FormattedDate.tsx
interface FormattedDateProps {
  date: Date | string;
  format?: 'short' | 'long' | 'relative' | 'datetime';
}
```

### 14.4 FormattedCurrency

**Used In:** All pages with currency  
**Purpose:** Consistent currency formatting

```typescript
// components/shared/FormattedCurrency.tsx
interface FormattedCurrencyProps {
  value: number;
  decimals?: number;
  showSign?: boolean;
}
```

### 14.5 FormattedPercent

**Used In:** All pages with percentages  
**Purpose:** Consistent percentage formatting

```typescript
// components/shared/FormattedPercent.tsx
interface FormattedPercentProps {
  value: number;
  decimals?: number;
  showSign?: boolean;
}
```

---

## 15. ShadCN Component Usage Summary

| ShadCN Component | Primary Use Cases |
|------------------|-------------------|
| `accordion` | Collapsible sections, FAQs |
| `alert` | Warnings, errors, info messages |
| `alert-dialog` | Confirmation dialogs |
| `avatar` | User avatars |
| `badge` | Status, counts, labels |
| `breadcrumb` | Navigation breadcrumbs |
| `button` | All actions |
| `calendar` | Date selection |
| `card` | Content containers |
| `checkbox` | Form inputs, task completion |
| `collapsible` | Expandable sections |
| `command` | Search, command palette |
| `dialog` | Modals |
| `dropdown-menu` | Action menus |
| `form` | Form containers |
| `input` | Text inputs |
| `label` | Form labels |
| `popover` | Tooltips, dropdowns |
| `progress` | Progress indicators |
| `radio-group` | Single selection |
| `scroll-area` | Scrollable containers |
| `select` | Dropdowns |
| `separator` | Visual dividers |
| `sheet` | Side panels, mobile nav |
| `skeleton` | Loading states |
| `switch` | Toggle inputs |
| `table` | Data tables |
| `tabs` | Tab navigation |
| `textarea` | Multi-line text |
| `toast` | Notifications |
| `tooltip` | Hover info |

---

## 16. Component Organization

```
components/
├── ui/                     # ShadCN components
│   ├── accordion.tsx
│   ├── alert.tsx
│   ├── badge.tsx
│   ├── button.tsx
│   ├── card.tsx
│   ├── ...
│
├── layout/                 # Layout components
│   ├── NavigationShell.tsx
│   ├── DealHeader.tsx
│   ├── PageHeader.tsx
│   └── Sidebar.tsx
│
├── cards/                  # Card components
│   ├── MetricCard.tsx
│   ├── MetricTile.tsx
│   └── ...
│
├── tables/                 # Table components
│   ├── DataTable.tsx
│   ├── RentRollTable.tsx
│   ├── T12Table.tsx
│   └── ...
│
├── forms/                  # Form components
│   ├── FormSection.tsx
│   ├── AddressInput.tsx
│   ├── CurrencyInput.tsx
│   └── ...
│
├── dialogs/                # Dialog components
│   ├── ConfirmDialog.tsx
│   ├── QuickViewDialog.tsx
│   └── ...
│
├── activity/               # Activity components
│   ├── ActivityItem.tsx
│   ├── ActivityFeed.tsx
│   └── ...
│
├── tasks/                  # Task components
│   ├── TaskItem.tsx
│   ├── TaskList.tsx
│   └── ...
│
├── documents/              # Document components
│   ├── DocumentCard.tsx
│   ├── DocumentList.tsx
│   └── ...
│
├── quotes/                 # Quote components
│   ├── QuoteCard.tsx
│   ├── QuoteComparison.tsx
│   └── ...
│
├── flags/                  # Flag components
│   ├── FlagIndicator.tsx
│   ├── FlagCard.tsx
│   └── ...
│
├── sla/                    # SLA components
│   ├── SLAIndicator.tsx
│   ├── SLADashboardWidget.tsx
│   └── ...
│
├── notifications/          # Notification components
│   ├── NotificationBell.tsx
│   ├── NotificationItem.tsx
│   └── ...
│
├── search/                 # Search components
│   ├── GlobalSearch.tsx
│   ├── SearchInput.tsx
│   └── ...
│
├── loading/                # Loading components
│   ├── PageLoader.tsx
│   ├── CardSkeleton.tsx
│   └── ...
│
├── shared/                 # Shared utilities
│   ├── StatusBadge.tsx
│   ├── EmptyState.tsx
│   ├── CopyButton.tsx
│   ├── FormattedDate.tsx
│   ├── FormattedCurrency.tsx
│   └── ...
│
├── upload/                 # Upload components
│   ├── FileUploader.tsx
│   ├── DragDropUploader.tsx
│   └── ...
│
└── timeline/               # Timeline components
    ├── Timeline.tsx
    └── ...
```

---

*End of Shared Components Catalog*

