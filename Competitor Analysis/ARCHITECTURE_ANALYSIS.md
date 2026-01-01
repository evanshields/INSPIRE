# Baseline Software Architecture Analysis
## USDV Capital, Inc. Dashboard - Technical Breakdown

**Analysis Date:** 2025-01-01  
**Target URL:** https://usdvcapitalinc.baselinesoftware.com/admin/dashboard

**Pages Actually Reviewed:**
- **Dashboard Page** (`/admin/dashboard`) - Full page structure, components, and interactions reviewed
- **Inbox/Mail Page** (`/admin/mail`) - Full page structure, components, email list structure, and interactions reviewed
- **Tasks Page** (`/admin/tasks`) - Full page structure, components, task list structure, and interactions reviewed
- **Contacts Page** (`/admin/contacts`) - Full page structure, components, contact list structure with filter tabs (All/Companies/People), and interactions reviewed
- **Borrowers Page** (`/admin/borrowers`) - Type-filtered contact list page, components, and structure reviewed
- **Investors Page** (`/admin/investors`) - Type-filtered contact list page with unique "Invested" column, components, and structure reviewed
- **Vendors Page** (`/admin/vendors`) - Type-filtered contact list page with unique columns (Role, Email, Phone, Cash), components, and structure reviewed
- **Quotes Page** (`/admin/quotes`) - Quote/loan quote management page with quote list table, components, and structure reviewed
- **Quote Detail Page** (`/admin/quotes/all/{uuid}`) - Quote detail/edit page with tab navigation (Type, Borrower, Details, Options), form sections, and structure reviewed
- **Pipeline Page** (`/admin/loans`) - Kanban board view and table view of loan pipeline with columns (Lead, Processing, Underwriting Approved, Closed), loan cards/rows, and structure reviewed
- **Loan Detail Page** (`/admin/loans/{loanId}`) - Loan detail page with subtab navigation (General, Documents, Contacts, Charges, Funding, Application, Collateral, Mail, and more), comprehensive loan information sections, and structure being reviewed
- **Navigation Structure** - Sidebar navigation visible on all pages showing all available routes (includes separate links for Borrowers, Investors, Vendors in addition to Contacts)

**Analysis Limitations:**
- Navigation attempts to other pages (Inbox, Tasks) were attempted but did not successfully navigate, likely due to authentication requirements or SPA routing behavior
- Architecture analysis for other pages is inferred from the navigation structure and common SPA patterns
- Component structure for non-dashboard pages is recommended/inferred rather than observed

---

## Executive Summary

The Baseline Software platform is a sophisticated financial management application for capital investment firms, featuring a modern single-page application (SPA) architecture with a hierarchical navigation structure, component-based UI design, and integrated AI capabilities.

**Note:** This analysis is based on direct observations of the Dashboard page (`/admin/dashboard`), the Inbox/Mail page (`/admin/mail`), and the Tasks page (`/admin/tasks`) that were successfully accessed and reviewed via Browser MCP. The navigation structure and routing patterns were observed from the persistent sidebar visible on all pages. Analysis of other pages and their specific components is inferred from common SPA patterns, the observed navigation hierarchy, and patterns observed in the reviewed pages.

---

## Methodology & Scope

### What Was Directly Observed:
1. **Dashboard Page** (`/admin/dashboard`):
   - Full page layout and structure
   - Component hierarchy and visual design
   - Metric cards (4 cards with data)
   - Two chart components (Loans Per Month, Income)
   - AI chat widget interface
   - Top header with notifications and user menu
   - Sidebar navigation structure (all 12 navigation items visible)

2. **Inbox/Mail Page** (`/admin/mail`):
   - Full page layout and email list structure
   - Tab navigation (Inbox, Drafts, Sent)
   - Email list table with columns (checkbox, sender, subject/preview, timestamp)
   - Search functionality
   - Compose button
   - Pagination ("Showing 50 of 133", "Load more" button)
  - Email previews with attachments displayed
  - Bulk selection functionality
  - Sidebar navigation (consistent across pages)

3. **Tasks Page** (`/admin/tasks`):
   - Full page layout and task list structure
   - Filter buttons (All, My Tasks)
   - Task list table with columns (checkbox, task name, loan/property link, due date, assignee, status)
   - Search functionality
   - New Task button
   - Task status indicators (To Do, Done)
   - Assignee tooltips (initials display)
   - Related loan links (navigable to loan detail pages)
   - Pagination display ("Showing 43 of 43")
   - Completed tasks marked with checked checkboxes
   - Sidebar navigation (consistent across pages)

### What Was Inferred/Recommended:
1. **Other Page Content**: Structure and components for pages other than dashboard
2. **Routing Implementation**: Specific routing library and configuration details
3. **State Management**: Specific state management library choices
4. **Styling Implementation**: Specific CSS framework/library used
5. **Backend Architecture**: API structure, authentication implementation

### Data Sources:
- Browser MCP snapshots of the Dashboard page
- Visible navigation structure from sidebar
- URL patterns from navigation links
- Component patterns observed on dashboard
- Screenshot/image descriptions of the dashboard layout
- Common SPA architecture patterns and best practices

---

## 1. Navigation Flow

### 1.1 Hierarchical Structure
The application uses a **persistent left-sidebar navigation** pattern with the following hierarchy:

```
/admin (Base Route)
├── /dashboard       - Main dashboard view
├── /mail            - Inbox/Email management
├── /tasks           - Task management
├── /contacts        - Contact management (may have sub-items)
├── /quotes          - Quote management
├── /loans           - Pipeline/Loan management
├── /servicing       - Active loans servicing
├── /payments/due    - Payments management (sub-route)
├── /payouts/ready   - Payouts management (sub-route)
├── /reports         - Reports/analytics
├── /funds           - Fund management
└── /offerings       - Offering management
```

### 1.2 Navigation Patterns
- **Persistent Sidebar**: Left navigation remains visible across all routes (approximately 20% viewport width)
- **Active State Indication**: Current route highlighted with darker background and left border accent
- **URL-based Routing**: Clean, RESTful URL structure indicating client-side routing
- **Nested Routes**: Support for sub-routes (e.g., `/payments/due`, `/payouts/ready`)

### 1.3 User Experience Flow
1. User logs in → redirected to `/admin/dashboard`
2. Sidebar navigation always accessible
3. Clicking navigation items updates URL and main content area
4. No full page reloads (SPA behavior)
5. "Get help" link at bottom of sidebar for support

---

## 2. Component Structure

### 2.1 Layout Components

#### **AppShell**
- **Persistent Sidebar** (Left)
  - Company branding/logo ("USDV Capital, Inc.")
  - Navigation menu items with icons
  - Help link footer
  
- **Main Content Area** (Right, ~80% width)
  - Dynamic content based on route
  - Page title (H1)
  - Route-specific components

- **Top Header Bar**
  - Notification bell icon (Alt+T keyboard shortcut)
  - User profile/avatar ("EA" initials)
  - Likely search or global actions

### 2.2 Dashboard-Specific Components

#### **Metric Cards** (Stat Cards)
- **Reusable Component Pattern**: Four metric cards displayed horizontally
- **Structure**:
  - Title (e.g., "Principal Balance", "Active Loans")
  - Value (numeric or formatted text)
  - Optional icon or trend indicator
- **Styling**: White background, rounded corners, subtle shadow, consistent spacing
- **Data**: Dynamic values (e.g., "25" Active Loans, "14" Active Borrowers)

#### **Chart Components**
- **Chart Container**: Two side-by-side charts on dashboard
- **Chart Types**: Line charts for time-series data
- **Features**:
  - Title/label
  - Axes (X: time, Y: values)
  - Multiple data series with color coding
  - Legend for series identification
  - Interactive tooltips (inferred from chart library patterns)

**Chart 1: "Loans Per Month"**
- Time range: Nov 24 - May 26
- Series: "Closing Loans" (blue), "Maturing Loans" (green)
- Y-axis: 0-10 loan count

**Chart 2: "Income"**
- Time range: Dec 24 - Dec 25
- Single series: Income values
- Y-axis: $0 - $10 (currency formatted)

#### **AI Chat Interface**
- **Component**: "Baseline Agent" chat widget
- **Structure**:
  - Header text: "How can I help you today?"
  - Brand label: "Ask Baseline"
  - Text input: "Ask a question..."
  - Submit button (disabled state when empty)
  - Disclaimer: "Baseline Agent can make mistakes. Check important info."
- **Placement**: Bottom-right or floating position (common pattern)

### 2.3 Inbox/Mail Page-Specific Components

#### **Page Header & Toolbar**
- **Page Title**: "Inbox" heading (H1)
- **Tab Navigation**: Three tab options visible
  - "Inbox" (likely active/selected state)
  - "Drafts"
  - "Sent"
  - Text-based tabs (no icons visible in snapshot)
  - Likely uses tab switching to filter email list

- **Search Functionality**:
  - Search input box with placeholder "Search inbox"
  - Positioned in toolbar area
  - Likely debounced search with real-time filtering

- **Compose Button**:
  - Primary action button labeled "Compose"
  - Positioned in toolbar (likely right-aligned)
  - Opens email composition interface

#### **Email List Table**
- **Table Structure**: Standard HTML table with semantic structure
  - `<table>` element with `<rowgroup>` and `<row>` elements
  - Multiple columns per row

- **Table Columns**:
  1. **Checkbox Column**: 
     - Bulk selection checkbox in header row
     - Individual checkboxes per email row
     - Allows multi-select for batch operations
  
  2. **Sender Column**:
     - Displays sender name/email
     - Examples: "Andy Bybee", "Abel from Riverside", "GovOS - Durango"
     - Some entries show "via" notation (e.g., "via USDV Social Media")
     - Text-only, no avatars visible in snapshot
  
  3. **Subject/Preview Column**:
     - Subject line displayed
     - Preview text (truncated with ellipsis)
     - Attachment indicators shown inline:
       - File names (e.g., "image.png", "Term Sheet.pdf")
       - File sizes (e.g., "127 B", "122.36 kB", "638.21 kB")
       - Multiple attachments shown with "+N" notation (e.g., "+7", "+10")
     - Rich text preview showing email content snippets
  
  4. **Timestamp Column**:
     - Relative times for recent emails (e.g., "11:19 AM", "10:36 AM")
     - Absolute dates for older emails (e.g., "Dec 29", "Nov 18")
     - Right-aligned, compact format

- **Email Row Structure**:
  - Each email is a table row (`<row>`)
  - Rows are clickable (likely opens email detail view)
  - Hover states likely provide visual feedback
  - Rows contain full email metadata as accessible text

- **Email Data Observed**:
  - Subject lines with preview text
  - Sender information (name, organization, email addresses)
  - Timestamps (relative and absolute)
  - Attachment metadata (file names and sizes)
  - Email content snippets in preview

#### **Pagination Component**
- **Pagination Display**: 
  - Text indicator: "Showing 50 of 133"
  - Indicates current page/view and total items
  - Positioned below email list

- **Load More Button**:
  - Button labeled "Load more"
  - Infinite scroll pattern (loads next batch)
  - Positioned below pagination text
  - Likely loads next 50 items when clicked

#### **Bulk Actions** (Inferred)
- **Selection State**:
  - Master checkbox for "select all"
  - Individual checkboxes per row
  - Selected state likely triggers action toolbar
  - Common bulk actions: Archive, Delete, Mark as Read, Move to Folder

#### **Email Content Features Observed**
- **Attachment Handling**:
  - Multiple attachment types (images, PDFs, Excel files)
  - File size display
  - Attachment count indicators ("+N more")
  - Inline attachment previews possible

- **Email Threading** (Inferred):
  - Some emails appear related (e.g., multiple "Tallahassee Portfolio GUC Loan Request" emails)
  - Threading likely indicated visually or via subject line prefixes
  - Reply chains visible in preview text

- **Email Status Indicators** (Inferred):
  - Read/unread states (likely shown via styling)
  - Important/flagged emails (common email UI pattern)
  - Draft indicators for unsent emails

### 2.4 Tasks Page-Specific Components

#### **Page Header & Toolbar**
- **Page Title**: "Tasks" heading (H1)
- **Filter Buttons**: 
  - Two filter options: "All" and "My Tasks"
  - Button-based filter UI (not tabs)
  - "All" appears to be active/selected (based on button styling pattern)
  - Filters task list by scope (all tasks vs. user's tasks)

- **Search Functionality**:
  - Search input box with placeholder "Search"
  - Positioned in toolbar area
  - Likely searches across task names, loan properties, assignees

- **New Task Button**:
  - Primary action button labeled "New Task"
  - Positioned in toolbar (likely right-aligned)
  - Opens task creation interface/form

#### **Task List Table**
- **Table Structure**: Standard HTML table with semantic structure
  - `<table>` element with header row and data rows
  - Column headers: Task, Loan, Due Date, Assignee, Status

- **Table Columns**:
  1. **Task Column**: 
     - Checkbox for selection
     - Task name/description text
     - Inline checkbox and text (task title editable/clickable)
     - Examples: "Size deal", "Place Title Order", "Google Borrower", "Call borrower"
  
  2. **Loan Column**:
     - Property address displayed as link
     - Links to loan detail pages: `/admin/loans/{loanId}`
     - Format: `/admin/loans/9153606`, `/admin/loans/12721595`, etc.
     - Some tasks may not have associated loans (empty cell)
     - Address examples: "4151 Sonoma Blvd", "34 Woodsman Dr", "315 NW 53rd St"
  
  3. **Due Date Column**:
     - Date format: "Sep 24, 2025", "Oct 3, 2025", "Dec 2, 2025"
     - Some tasks have no due date (empty cell)
     - Tasks sorted by due date (dates first, no-date tasks at bottom)
  
  4. **Assignee Column**:
     - Displays assignee initials (e.g., "EA", "TB", "KB")
     - Multiple assignees shown with space (e.g., "KB EA", "TB EA", "TB KB")
     - Tooltip on hover showing full assignee information
     - Empty cell if no assignee
  
  5. **Status Column**:
     - Status badge/indicator
     - Values observed: "To Do", "Done"
     - Status affects checkbox state (Done tasks are checked)
     - Visual distinction between status types
  
  6. **Actions Column** (Empty in snapshot):
     - Likely contains action buttons (Edit, Delete, etc.)
     - May appear on hover or be conditionally rendered

- **Task Row Structure**:
  - Each task is a table row
  - Rows are selectable via checkbox
  - Completed tasks have checked checkboxes
  - Task name is clickable (likely opens task detail/edit view)
  - Loan address is clickable (navigates to loan detail page)

- **Task Data Patterns Observed**:
  - **Task Types**: 
    - Generic tasks ("Size deal", "Place Title Order")
    - Research tasks ("Google Borrower", "Google Property")
    - Communication tasks ("Call borrower")
    - Follow-up tasks ("Insurance Follow Up", "Manage/Update - Accolend Needs List")
  
  - **Task Relationships**:
    - Many tasks linked to specific loans/properties
    - Tasks grouped by property (same property has multiple tasks)
    - Tasks can exist without loan association (e.g., "Automation for Corp docs")
  
  - **Status Management**:
    - Tasks have completion status (To Do, Done)
    - Completed tasks marked with checked checkbox
    - Status badge displayed in Status column
    - Completed tasks may be filtered out or shown separately

- **Sorting/Grouping** (Observed):
  - Tasks sorted by due date (most recent first)
  - Tasks without due dates appear at bottom of list
  - May support sorting by other columns (clickable headers)

#### **Pagination Component**
- **Pagination Display**: 
  - Text indicator: "Showing 43 of 43"
  - All tasks fit on single page/view
  - Similar pattern to Inbox page but no "Load more" needed
  - May show "Load more" if tasks exceed page limit

#### **Task Status System**
- **Status Values Observed**:
  - "To Do": Active/incomplete tasks
  - "Done": Completed tasks
  
- **Status Indicators**:
  - Status badge in Status column
  - Checkbox state tied to status (Done = checked)
  - Visual distinction (likely color coding or styling)

#### **Assignee System**
- **Assignee Display**:
  - Initials shown (e.g., EA, TB, KB)
  - Multiple assignees displayed with space separator
  - Tooltip on hover shows full name/info
  - Empty state when no assignee

#### **Loan Integration**
- **Deep Linking**:
  - Task loan column links to `/admin/loans/{loanId}`
  - Creates cross-page navigation within application
  - Loan IDs are numeric (e.g., 9153606, 12721595, 1401275)
  - Supports task-to-loan workflow navigation

### 2.5 Contacts Page-Specific Components

#### **Page Header & Toolbar**
- **Page Title**: "Contacts" heading (H1)
- **Filter Buttons**: 
  - Three filter options: "All", "Companies", "People"
  - Button-based filter UI (similar to Tasks page)
  - "All" appears to be active/selected
  - Filters contact list by entity type (all contacts vs. companies vs. individuals)

- **Search Functionality**:
  - Search input box with placeholder "Search"
  - Positioned in toolbar area
  - Likely searches across contact names, companies, types

- **Export Button**:
  - Secondary action button labeled "Export"
  - Allows exporting contact list data (likely CSV/Excel)
  - Positioned in toolbar

- **Add Contacts Button**:
  - Primary action button labeled "Add Contacts"
  - Opens contact creation interface/form
  - Positioned in toolbar (right-aligned)

#### **Contact List Table**
- **Table Structure**: Standard HTML table with semantic structure
  - `<table>` element with header row and data rows
  - Column headers: Name, Associated With, Owner, Type, Last Activity, Status

- **Table Columns**:
  1. **Name Column**: 
     - Contact name (person or company name)
     - Examples: "10000 Voyager LLC", "Alberto Becerra (Borrower Attorney)", "SingleSource"
     - Clickable (likely opens contact detail view)
     - Supports both person names and company names
  
  2. **Associated With Column**:
     - Shows relationship to other contacts
     - Person-to-company associations (e.g., "Rodrigo Fachini Tavares" associated with "4151 Sonoma LLC")
     - Company-to-person associations (e.g., "EquiRent Partners LLC" associated with "Andres Delgado")
     - Can be empty if no association
     - Clickable links with tooltips showing full details
     - Multiple associations shown (e.g., "Chrissy Ziccardi +4" indicates 4 additional people)
  
  3. **Owner Column**:
     - Displays owner/assignee initials (e.g., "EA", "TB", "KB", "HH")
     - Similar to Tasks page assignee system
     - Tooltip on hover showing full owner information
     - Can be empty if no owner assigned
  
  4. **Type Column**:
     - Contact type badge/indicator
     - Values observed: "Borrower", "Vendor", "Investor"
     - Categorizes contacts by their role in the business
     - Multiple types possible (inferred - single value shown per contact)
  
  5. **Last Activity Column**:
     - Timestamp of last activity/interaction
     - Relative times (e.g., "2 months ago", "3 months ago", "3 weeks ago")
     - Empty if no activity recorded
     - Helps identify active vs. inactive contacts
  
  6. **Status Column**:
     - Status badge/indicator
     - Values observed: "Draft", "Active"
     - "Draft" indicates incomplete/unverified contact
     - "Active" indicates verified and active contact
     - Visual distinction between status types

- **Contact Row Structure**:
  - Each contact is a table row
  - Rows are clickable (likely opens contact detail view)
  - Contacts can be companies or individuals
  - Bidirectional relationships shown (person ↔ company)

- **Contact Data Patterns Observed**:
  - **Contact Types**: 
    - **Borrowers**: Most common type (e.g., "10000 Voyager LLC", "Rodrigo Fachini Tavares")
    - **Vendors**: Service providers (e.g., "Chris Porto", "SingleSource", "Jee Law PA")
    - **Investors**: Investment entities (e.g., "Eastview", "Test Fund", "USDV Capital, Inc.")
  
  - **Contact Relationships**:
    - Person-to-company relationships (e.g., person works for/owns company)
    - Company-to-person relationships (e.g., company has employees/owners)
    - Multiple people can be associated with one company ("+4" notation)
    - Relationships are bidirectional (same relationship shown from both perspectives)
  
  - **Contact Status**:
    - "Draft": New or incomplete contact records
    - "Active": Verified and actively used contacts
    - Most contacts in snapshot are "Draft" status
    - Active contacts tend to have "Last Activity" timestamps
  
  - **Name Patterns**:
    - Company names: LLC, INC, PA suffixes
    - Person names: First and last name
    - Some contacts have descriptive suffixes (e.g., "(Borrower Attorney)")
    - Mix of individual names and company names

#### **Pagination Component**
- **Pagination Display**: 
  - Text indicator: "Showing 50 of 51"
  - One more contact available
  - Similar pattern to Inbox page

- **Load More Button**:
  - Button labeled "Load more"
  - Infinite scroll pattern (loads next batch)
  - Positioned below pagination text
  - Likely loads next 50 items when clicked

#### **Contact Type System**
- **Type Values Observed**:
  - "Borrower": Entities that borrow money (individuals and companies)
  - "Vendor": Service providers (law firms, title companies, insurance, etc.)
  - "Investor": Investment entities and funds
  
- **Type Indicators**:
  - Type badge in Type column
  - Visual distinction (likely color coding or styling)
  - May be filterable (separate routes for Borrowers, Investors, Vendors visible in sidebar)

#### **Contact Status System**
- **Status Values Observed**:
  - "Draft": Incomplete or unverified contact records
  - "Active": Verified and actively used contacts
  
- **Status Indicators**:
  - Status badge in Status column
  - Visual distinction (likely color coding or styling)
  - Active contacts have "Last Activity" timestamps
  - Draft contacts typically have empty "Last Activity"

#### **Owner/Assignee System**
- **Owner Display**:
  - Initials shown (e.g., EA, TB, KB, HH)
  - Similar to Tasks page assignee system
  - Tooltip on hover shows full name/info
  - Empty state when no owner assigned
  - Indicates who manages/owns the relationship with the contact

#### **Relationship Management**
- **Bidirectional Relationships**:
  - Person-company relationships shown from both perspectives
  - Same relationship appears in multiple rows (once for person, once for company)
  - Supports complex organizational structures
  - Tooltips provide detailed relationship information

### 2.6 Type-Specific Contact Pages (Borrowers/Investors/Vendors)

The application provides separate routes for type-specific contact filtering: `/admin/borrowers`, `/admin/investors`, and `/admin/vendors`. These pages share the same component structure as the Contacts page but are pre-filtered by contact type.

#### **Borrowers Page Structure** (Observed)

**URL**: `/admin/borrowers`  
**Page Title**: "Borrowers"

**Key Differences from Contacts Page**:
1. **Missing Type Column**: Since all contacts are pre-filtered to Borrowers, the "Type" column is removed
2. **Button Text**: "Add Borrower" instead of "Add Contacts"
3. **Table Columns**: 5 columns instead of 6 (Name, Associated With, Owner, Last Activity, Status)
4. **Pre-filtered Data**: Only Borrower-type contacts displayed
5. **Pagination**: "Showing 37 of 37" (all contacts visible, no Load more button needed)

**Shared Components with Contacts Page**:
- Same filter buttons: "All", "Companies", "People"
- Same search functionality
- Same Export button
- Same table structure (minus Type column)
- Same owner/assignee system
- Same status system (Draft, Active)
- Same relationship management (Associated With column)
- Same pagination pattern (when more than one page of results)

#### **Investors Page Structure** (Observed)

**URL**: `/admin/investors`  
**Page Title**: "Investors"

**Key Differences from Contacts Page**:
1. **Missing Type Column**: Since all contacts are pre-filtered to Investors, the "Type" column is removed
2. **Button Text**: "Add Investor" instead of "Add Contacts"
3. **Table Columns**: 6 columns (Name, Associated With, **Invested** (unique), Owner, Last Activity, Status)
4. **Pre-filtered Data**: Only Investor-type contacts displayed
5. **Pagination**: "Showing 3 of 3" (all contacts visible, no Load more button needed)
6. **Unique Column**: "Invested" column shows investment amounts (currently showing "-" for all entries, likely monetary values when populated)

**Invested Column Details**:
- **Purpose**: Displays investment amount/value for each investor
- **Data Type**: Monetary value (currency formatted)
- **Display**: Shows "-" when no investment data available
- **Position**: Third column (between "Associated With" and "Owner")
- **Type-Specific**: This column only appears on Investors page, not on Borrowers or Contacts pages

**Shared Components with Contacts Page**:
- Same filter buttons: "All", "Companies", "People"
- Same search functionality
- Same Export button
- Same table structure (with type-specific column variations)
- Same owner/assignee system
- Same status system (Draft, Active)
- Same relationship management (Associated With column)
- Same pagination pattern

#### **Vendors Page Structure** (Observed)

**URL**: `/admin/vendors`  
**Page Title**: "Vendors"

**Key Differences from Contacts Page**:
1. **Missing Type Column**: Since all contacts are pre-filtered to Vendors, the "Type" column is removed
2. **Button Text**: "Add Vendor" instead of "Add Contacts"
3. **Table Columns**: 8 columns (Name, **Role** (unique), Associated With, **Email** (unique), **Phone** (unique), **Cash** (unique), Owner, Actions)
4. **Pre-filtered Data**: Only Vendor-type contacts displayed
5. **Pagination**: "Showing 11 of 11" (all contacts visible, no Load more button needed)
6. **Missing Columns**: No "Last Activity" or "Status" columns
7. **Unique Columns**: Multiple vendor-specific columns not present on other contact type pages

**Unique Column Details**:

1. **Role Column**:
   - **Purpose**: Displays vendor's role or job title
   - **Examples**: "Title Agent", "Insurance Agent"
   - **Position**: Second column (after Name)
   - **Data Type**: Text
   - **Display**: Shows "-" when no role specified

2. **Email Column**:
   - **Purpose**: Displays vendor email addresses
   - **Format**: Clickable mailto links
   - **Examples**: "cporto@singlesourceproperty.com", "john@jeelawpa.com"
   - **Position**: Fourth column (after Associated With)
   - **Interactive**: Clicking email opens email client with pre-filled recipient
   - **Display**: Shows "-" when no email available

3. **Phone Column**:
   - **Purpose**: Displays vendor phone numbers
   - **Format**: Formatted phone numbers (e.g., "(954) 923-0906", "(866) 620-7577")
   - **Position**: Fifth column (after Email)
   - **Data Type**: Formatted phone number string
   - **Display**: Shows "-" when no phone number available

4. **Cash Column**:
   - **Purpose**: Displays cash/payment information (likely payment history or balance)
   - **Position**: Sixth column (after Phone, before Owner)
   - **Data Type**: Monetary value (currency formatted)
   - **Display**: Currently showing "-" for all entries, likely shows payment amounts when populated
   - **Type-Specific**: This column only appears on Vendors page

**Shared Components with Contacts Page**:
- Same filter buttons: "All", "Companies", "People"
- Same search functionality
- Same Export button
- Same owner/assignee system
- Same relationship management (Associated With column)
- Same pagination pattern

**Notable Absences**:
- **No Last Activity Column**: Vendors page does not track last activity timestamps
- **No Status Column**: Vendors page does not show Draft/Active status badges
- **No Type Column**: Pre-filtered to Vendors only

**Vendor Data Patterns Observed**:
- **Vendor Roles**: Primarily "Title Agent" and "Insurance Agent" roles
- **Email Links**: All vendor emails are clickable mailto links
- **Phone Formatting**: Phone numbers displayed in standard format (XXX) XXX-XXXX
- **Company Associations**: Many vendors associated with companies (e.g., "SingleSource", "Jee Law PA")
- **Multiple Contacts per Company**: Some companies have multiple vendor contacts (e.g., SingleSource has multiple Title Agents)

### 2.8 Quotes Page-Specific Components

#### **Page Header & Toolbar**
- **Page Title**: "Quotes" heading (H1)
- **Filter Buttons**: 
  - Two filter options: "All" and "Archived"
  - Button-based filter UI (similar to Tasks/Contacts pages)
  - "All" appears to be active/selected (based on button styling pattern)
  - Filters quote list by status (all quotes vs. archived quotes)

- **Search Functionality**:
  - Search input box with placeholder "Search"
  - Positioned in toolbar area
  - Likely searches across quote names, borrower names, types

- **Add Quote Button**:
  - Primary action button labeled "Add Quote"
  - Opens quote creation interface/form
  - Positioned in toolbar (right-aligned)

#### **Quote List Table**
- **Table Structure**: Standard HTML table with semantic structure
  - `<table>` element with header row and data rows
  - Column headers: Name, Type, Borrower, Last Updated, Status

- **Table Columns**:
  1. **Name Column**: 
     - Quote name or property address
     - Examples: "2802 Flora Ave N", "Test Quote Sept 24th", "3307 26th St W"
     - Mix of property addresses and descriptive quote names
     - Clickable (likely opens quote detail/edit view)
  
  2. **Type Column**:
     - Loan/quote type badge
     - Values observed: "Bridge + Rehab", "Construction"
     - Categorizes quotes by loan product type
     - Visual distinction (likely color coding or styling)
  
  3. **Borrower Column**:
     - Borrower/company name associated with the quote
     - Examples: "EquiRent Partners LLC", "Test Company", "Test 2 Company"
     - Links to borrower contact (inferred)
     - Clickable (likely navigates to borrower detail page)
  
  4. **Last Updated Column**:
     - Date of last update/modification
     - Format: "MM/DD/YYYY" (e.g., "12/30/2025", "09/24/2025")
     - Sorted by date (most recent first, based on visible data)
     - Helps track quote activity and recency
  
  5. **Status Column**:
     - Status badge/indicator
     - Values observed: "Draft"
     - Indicates quote lifecycle stage
     - Other statuses likely include: "Sent", "Accepted", "Rejected", "Archived"
     - Visual distinction (likely color coding or styling)
  
  6. **Actions Column** (Empty in snapshot):
     - Likely contains action buttons (Edit, Delete, Archive, Send, etc.)
     - May appear on hover or be conditionally rendered

- **Quote Row Structure**:
  - Each quote is a table row
  - Rows are clickable (likely opens quote detail view)
  - Quotes linked to borrowers
  - Sorted by Last Updated date (most recent first)

- **Quote Data Patterns Observed**:
  - **Quote Types**: 
    - "Bridge + Rehab": Bridge loan with rehabilitation
    - "Construction": Construction loan
    - Other types likely exist (DSCR, Fix & Flip, etc.)
  
  - **Naming Patterns**:
    - Property addresses used as quote names (e.g., "2802 Flora Ave N")
    - Descriptive names for test quotes (e.g., "Test Quote Sept 24th")
    - Address-based naming suggests quotes are property-specific
  
  - **Borrower Relationships**:
    - Each quote linked to a borrower/company
    - Same borrower can have multiple quotes
    - Borrower names match contact names (e.g., "EquiRent Partners LLC")
  
  - **Status Management**:
    - All visible quotes are "Draft" status
    - Archive filter suggests archived quotes exist
    - Status workflow: Draft → Sent → Accepted/Rejected → Archived

- **Sorting** (Observed):
  - Quotes sorted by Last Updated date (most recent first)
  - Date format: MM/DD/YYYY
  - Chronological ordering helps prioritize recent quotes

#### **Pagination Component**
- **Pagination Display**: 
  - Text indicator: "Showing 8 of 8"
  - All quotes fit on single page/view
  - Similar pattern to other list pages
  - May show "Load more" if quotes exceed page limit

#### **Quote Status System**
- **Status Values Observed**:
  - "Draft": Incomplete or unsent quotes
  
- **Status Indicators** (Inferred):
  - Status badge in Status column
  - Visual distinction (likely color coding or styling)
  - Status workflow progression (Draft → Sent → Accepted/Rejected → Archived)

#### **Archive System**
- **Archive Filter**: 
  - "Archived" button filters to show archived quotes
  - Archived quotes likely excluded from default "All" view
  - Archive status likely separate from or related to main status

#### **Borrower Integration**
- **Borrower Linking**:
  - Borrower column shows associated borrower/company
  - Likely links to borrower detail/contact page
  - Creates cross-page navigation within application
  - Supports quote-to-borrower workflow navigation

### 2.9 Quote Detail Page Structure (Observed)

#### **URL Structure**
- **Pattern**: `/admin/quotes/all/{quoteId}`
- **Quote ID**: UUID format (e.g., `76c84a83-9f8b-42bf-b4fe-5c12390491a8`)
- **Page Title**: Property address or quote name (e.g., "2802 Flora Ave N")
- **Route Type**: Detail/edit view (separate from list view)

#### **Page Layout**
- **Navigation**: "Back" button to return to quotes list
- **Action Buttons**: "Save & Exit" button (top-right)
- **Tab Navigation**: Four tabs visible: "Type", "Borrower", "Details", "Options"
- **Active Tab**: "Details" tab currently active (observed)
- **Multi-Section Form**: Tab-based form with multiple sections

#### **Tab Structure** (Observed)
1. **Type Tab**: Quote/loan type selection (not fully visible in current view)
2. **Borrower Tab**: Borrower selection/assignment (not fully visible in current view)
3. **Details Tab**: Property and loan details (currently active, fully visible)
4. **Options Tab**: Additional quote options/configurations (not fully visible in current view)

#### **Details Tab Sections** (Observed)

**1. Property Address Section**
- **Heading**: "Property address" (H4)
- **Form Fields**:
  - **Street Address 1**: Combobox with autocomplete ("Enter an address")
    - Pre-filled: "2802 Flora Ave N"
    - Google Places API integration (inferred from combobox pattern)
  - **Street Address 2**: Textbox (optional secondary address)
  - **City**: Textbox (e.g., "Lehigh Acres")
  - **Province/State**: Combobox (e.g., "Florida")
  - **Postal Code/Zip**: Textbox (e.g., "33971")
  - **Country**: Combobox (e.g., "United States")

**2. Details Section**
- **Heading**: "Details" (H4)
- **Loan Details Fields**:
  - **Loan Amount**: Textbox with currency formatting (e.g., "$182,700.00")
  - **Rate**: Textbox with percentage formatting (e.g., "10.75%")
  - **Term**: Textbox (e.g., "12 months")
  - **Origination**: Date textbox (e.g., "12/29/2025")
  
- **Property Details Fields**:
  - **Gross Livable Area (GLA)**: Textbox (appears twice - may be duplicate field or different sections)
  - **Property Type**: Combobox (e.g., "Single-Family")
  - **Purchase Price**: Currency textbox
  - **Purchase Date**: Date textbox
  - **As Is Value**: Currency textbox
  - **ARV - Lender**: Currency textbox (After Repair Value)
  - **Total Rehab**: Currency textbox (e.g., "$0.00")

**3. Navigation/Action Section** (Bottom)
- **Back Button**: Returns to previous view
- **See Options Button**: Disabled state (likely enables when required fields are filled)
- **Save & Exit Button**: Top-right (saves quote and returns to list)

#### **Form Field Patterns**
- **Currency Fields**: Formatted with dollar sign and decimals (e.g., "$182,700.00")
- **Percentage Fields**: Formatted with % symbol (e.g., "10.75%")
- **Date Fields**: Text input with date formatting (e.g., "12/29/2025")
- **Comboboxes**: Dropdown/autocomplete fields (State, Country, Property Type, Address)
- **Textboxes**: Standard text input fields

#### **Form Validation** (Inferred)
- **Required Fields**: "See Options" button disabled suggests required field validation
- **Format Validation**: Currency, percentage, and date fields likely validate format
- **Address Validation**: Google Places autocomplete ensures valid addresses

#### **State Management** (Inferred)
- **Form State**: All field values stored in component state
- **Dirty State**: Tracks unsaved changes
- **Validation State**: Tracks field-level and form-level validation
- **Save State**: Handles save operations and success/error states
- **Navigation State**: Maintains context for "Back" button navigation

#### **Component Structure** (Inferred)
```
<QuoteDetailPage quoteId={uuid}>
  <QuoteHeader>
    <BackButton />
    <PageTitle />
    <SaveExitButton />
  </QuoteHeader>
  <QuoteTabs>
    <Tab name="Type" />
    <Tab name="Borrower" />
    <Tab name="Details" active />
    <Tab name="Options" />
  </QuoteTabs>
  <QuoteForm>
    {activeTab === 'Details' && <DetailsTab>
      <PropertyAddressSection>
        <AddressFields />
      </PropertyAddressSection>
      <DetailsSection>
        <LoanDetailsFields />
        <PropertyDetailsFields />
      </DetailsSection>
    </DetailsTab>}
    {activeTab === 'Type' && <TypeTab />}
    {activeTab === 'Borrower' && <BorrowerTab />}
    {activeTab === 'Options' && <OptionsTab />}
  </QuoteForm>
  <QuoteFooter>
    <BackButton />
    <SeeOptionsButton disabled={!isValid} />
  </QuoteFooter>
</QuoteDetailPage>
```

#### **Quote Workflow** (Inferred)
1. **Create Quote**: Navigate to quote creation (tab navigation through sections)
2. **Fill Details**: Complete property and loan details
3. **Select Type**: Choose loan type (Bridge + Rehab, Construction, etc.)
4. **Assign Borrower**: Link quote to borrower/contact
5. **Configure Options**: Set additional quote options
6. **Save**: Save quote and return to list
7. **Next Steps**: "See Options" button likely progresses to next workflow stage

### 2.10 Pipeline Page-Specific Components (Kanban Board View)

#### **Page Header & Toolbar**
- **Page Title**: "Pipeline" heading (H1)
- **View Toggle**: 
  - Button labeled "Pipeline View" (indicates alternative view available)
  - Suggests multiple view modes (Kanban vs. List/Table view)
  
- **Summary Statistics**:
  - Text display: "24 loans · $6,774,149.00"
  - Shows total loan count and total dollar amount
  - Aggregated across all pipeline columns
  - Positioned between view toggle and filter buttons

- **Filter Button**:
  - Button labeled "Filter"
  - Opens filter interface/dropdown
  - Allows filtering loans by various criteria

- **Sort Button**:
  - Button labeled "Sort"
  - Opens sort options/dropdown
  - Allows sorting loans within columns

- **Search Functionality**:
  - Search input box with placeholder "Search"
  - Positioned in toolbar area
  - Likely searches across loan properties, borrowers, loan types

- **Export Button**:
  - Secondary action button labeled "Export"
  - Allows exporting pipeline data
  - Positioned in toolbar

- **Add Loan Button**:
  - Primary action button labeled "Add Loan"
  - Opens loan creation interface/form
  - Positioned in toolbar (right-aligned)

#### **Kanban Board Structure**
- **Layout**: Horizontal column layout (Kanban board)
- **Columns**: Multiple pipeline stage columns
- **Column Structure**: Each column represents a pipeline stage

**Observed Columns**:
1. **Lead Column**:
   - **Header**: "Lead"
   - **Count**: 5 loans
   - **Total Amount**: $2,485,143.00
   - **Stage**: Initial/early stage of pipeline

2. **Processing Column**:
   - **Header**: "Processing"
   - **Count**: 2 loans
   - **Total Amount**: $365,400.00
   - **Stage**: Active processing stage

3. **Underwriting Approved Column**:
   - **Header**: "Underwriting Approved"
   - **Count**: 1 loan
   - **Total Amount**: $208,500.00
   - **Stage**: Underwriting completed, awaiting next steps

4. **Closed Column**:
   - **Header**: "Closed"
   - **Count**: 16 loans
   - **Total Amount**: $3,715,106.00
   - **Stage**: Completed/closed loans

#### **Loan Card Structure** (Kanban Cards)
Each loan is represented as a card within a column. Cards contain:

1. **Property Address**:
   - Primary text/element
   - Examples: "315 NW 53rd St", "2802 Flora Ave N", "1016 Butler St"
   - Clickable (likely opens loan detail view)
   - Prominent display at top of card

2. **Time Indicator**:
   - Relative time display
   - Examples: "1w" (1 week), "4w" (4 weeks), "2mo" (2 months), "3mo" (3 months)
   - Indicates how long loan has been in current stage
   - Compact format

3. **Status/Label Badge**:
   - Status indicator badge
   - Examples: 
     - "New Lead - Ambassador"
     - "Application Received"
     - "Pending Lender Closing"
     - "Pending Servicing Approval"
     - "USDV Funded"
   - Color-coded or styled badges
   - Provides additional context beyond column stage

4. **Loan Amount**:
   - Currency formatted amount
   - Examples: "$1,601,043.00", "$182,700.00", "$208,500.00"
   - Prominent display
   - Helps assess loan value at a glance

5. **Borrower Name**:
   - Borrower/company name
   - Examples: "EquiRent Partners LLC", "Vista Homes 6 LLC", "IC Development LLC"
   - Text display
   - May be clickable to navigate to borrower

6. **Loan Type**:
   - Loan product type badge
   - Examples: 
     - "Ground Up Construction"
     - "Construction"
     - "DSCR"
     - "Fix & Flip - No Credit"
     - "Fix & Flip | Bridge (RTL)"
   - Categorizes loan by product
   - Visual distinction (likely color coding)

7. **Transaction Type** (Optional):
   - Transaction category
   - Examples: "Purchase", "Refinance"
   - May not appear on all cards
   - Provides additional loan context

8. **Date** (Optional):
   - Date display
   - Format: "MMM DD, YYYY" (e.g., "Sep 30, 2025", "Dec 29, 2025", "Aug 21, 2025")
   - May show origination date, close date, or milestone date
   - Not present on all cards

9. **Owner/Assignee**:
   - Initials display with tooltip
   - Examples: "EA", "HH", "TB", "KB", "HH EA" (multiple assignees)
   - Similar to Tasks/Contacts assignee system
   - Tooltip shows full name/info on hover
   - Indicates who manages the loan

#### **Kanban Board Features** (Inferred)
- **Drag and Drop**: Cards likely draggable between columns to change pipeline stage
- **Column Totals**: Each column shows count and total dollar amount
- **Card Interaction**: Cards clickable to open loan detail view
- **Column Sorting**: Loans within columns may be sortable
- **Column Filtering**: Filtering may affect cards within columns
- **Horizontal Scroll**: Additional columns may be accessible via horizontal scroll
- **Responsive Layout**: Columns may stack or adapt on smaller screens

### 2.11 Pipeline Table View Structure (Observed)

#### **View Toggle**
- **Button State**: "Table View" button active (indicates table view mode)
- **Alternative View**: "Pipeline View" available (Kanban board view)
- **Same URL**: Both views use same route (`/admin/loans`)
- **View State**: View mode likely stored in URL query param or component state

#### **Page Header & Toolbar** (Same as Kanban View)
- **Page Title**: "Pipeline" heading (H1) - unchanged
- **Summary Statistics**: "24 loans · $6,774,149.00" - same aggregated totals
- **Filter Button**: Same filter functionality
- **Sort Button**: Same sort functionality
- **Search**: Same search functionality
- **Export Button**: Same export functionality
- **Add Loan Button**: Same add loan functionality

#### **Table Structure**
- **Table Element**: Standard HTML table with rowgroups
- **Column Headers**: 
  1. **Loan** - Property address
  2. **Borrower** - Borrower/company name(s)
  3. **Closing Date** - Loan closing date
  4. **Use of Funds** - Transaction type (Purchase, Refinance, or "-")
  5. **Product** - Loan product type
  6. **Amount** - Loan amount (currency formatted or "-")
  7. **Owner** - Owner/assignee initials with tooltip
  8. **Substage** - Status badge (clickable/editable button)
  9. **Time Indicator** - Relative time (e.g., "1w", "4w", "2mo", "3mo")

#### **Grouped Rows by Pipeline Stage**
- **Group Headers**: Table rows that group loans by pipeline stage
- **Group Format**: "Stage Name Count TotalAmount" (e.g., "Lead 5 $2,485,143.00")
- **Groups Observed**:
  1. **Lead**: "Lead 5 $2,485,143.00"
  2. **Processing**: "Processing 2 $365,400.00"
  3. **Approved**: "Approved 1 $208,500.00" (corresponds to "Underwriting Approved" in Kanban)
  4. **Closed**: "Closed 16 $3,715,106.00"

- **Group Behavior** (Inferred):
  - Groups likely collapsible/expandable (click header to collapse/expand)
  - Group totals calculated dynamically
  - Groups maintain stage organization while allowing table view
  - Visual distinction between group headers and data rows

#### **Table Row Structure** (Loan Data Rows)

Each loan row contains:

1. **Loan Column** (Property Address):
   - Property address text (e.g., "315 NW 53rd St", "2802 Flora Ave N")
   - Clickable (opens loan detail view)
   - Primary identifier for loan

2. **Borrower Column**:
   - Borrower/company name(s)
   - **Multiple Borrowers**: Comma-separated list when multiple borrowers
     - Example: "EquiRent Partners LLC , Andres Delgado"
     - Example: "JBPERETTI INC , IC Development LLC , Alberto Becerra (Borrower Attorney)"
   - Single borrower shows single name
   - May include borrower attorney or related contacts

3. **Closing Date Column**:
   - Date format: "MM/DD/YYYY" (e.g., "09/30/2025", "12/29/2025", "08/21/2025")
   - **Empty State**: Shows "-" when closing date not set
   - Date display varies by loan

4. **Use of Funds Column**:
   - Transaction type: "Purchase", "Refinance"
   - **Empty State**: Shows "-" when not applicable or not set
   - Indicates loan purpose/transaction type

5. **Product Column**:
   - Loan product type
   - Examples: "Ground Up Construction", "DSCR", "Fix & Flip - No Credit", "Fix & Flip | Bridge (RTL)"
   - Same product types as Kanban view

6. **Amount Column**:
   - Currency formatted amount (e.g., "$1,601,043", "$182,700", "$246,000")
   - **Empty State**: Shows "-" when amount not set
   - Same formatting as Kanban view

7. **Owner Column**:
   - Owner/assignee initials (e.g., "EA", "HH EA", "TB", "KB")
   - Tooltip on hover shows full name/info
   - Same system as Kanban view
   - **Empty State**: Some rows may have empty owner (tooltip element present but no initials)

8. **Substage Column**:
   - Status badge with button element
   - Clickable/editable status button
   - Examples: "New Lead - Ambassador", "Application Received", "Pending Lender Closing", "Pending Servicing Approval", "USDV Funded"
   - Tooltip on hover shows status name
   - Allows quick status updates (inferred from button structure)

9. **Time Indicator Column**:
   - Relative time display (last column)
   - Format: "1w" (1 week), "4w" (4 weeks), "2mo" (2 months), "3mo" (3 months), "3w" (3 weeks)
   - Indicates time since last update or stage entry
   - Same as Kanban card time indicator

#### **Table View Features** (Observed/Inferred)
- **Sortable Columns**: Column headers likely clickable for sorting
- **Column Resizing**: Columns may be resizable
- **Column Reordering**: Columns may be reorderable (inferred)
- **Row Selection**: Rows likely selectable (checkbox or click)
- **Row Actions**: Right-click or action menu may be available
- **Expandable Groups**: Stage groups likely collapsible/expandable
- **Scrollable**: Table scrolls vertically if rows exceed viewport
- **Responsive**: Table may adapt layout on smaller screens (horizontal scroll, stacked layout)

#### **Data Differences from Kanban View**
- **Multiple Borrowers**: Table view shows multiple borrowers per loan (comma-separated)
- **Stage Label**: "Approved" in table vs. "Underwriting Approved" in Kanban (same stage, different label)
- **More Detailed Information**: Closing Date, Use of Funds explicitly shown as columns
- **Editable Status**: Substage column appears to be directly editable via button click
- **Grouped Organization**: Loans grouped by stage with group headers and totals

#### **Shared Data Elements**
Both Kanban and Table views share:
- Same loan data (property, borrower, amount, product type, status, owner, time)
- Same pipeline stages (Lead, Processing, Underwriting Approved/Approved, Closed)
- Same summary statistics
- Same filter, sort, search, export functionality
- Same toolbar and header structure

#### **Pipeline Stages Workflow** (Observed)
Based on column structure:
1. **Lead** → Initial contact/inquiry stage
2. **Processing** → Active application processing
3. **Underwriting Approved** → Underwriting completed
4. **Closed** → Loan closed/completed

Additional stages likely exist (not visible in current view):
- May include: "Application", "Underwriting", "Approved", "Closing", etc.

#### **Loan Status System** (Observed)
Status badges provide additional granularity within stages:
- **New Lead - Ambassador**: New lead source identification
- **Application Received**: Application submitted
- **Pending Lender Closing**: Awaiting lender closing
- **Pending Servicing Approval**: Awaiting servicing transfer
- **USDV Funded**: USDV-funded loans

Status badges work in combination with column stages to provide detailed loan state.

#### **Loan Types Observed**
- **Ground Up Construction**: New construction loans
- **Construction**: Construction/renovation loans
- **DSCR**: Debt Service Coverage Ratio loans
- **Fix & Flip - No Credit**: Fix and flip loans without credit requirements
- **Fix & Flip | Bridge (RTL)**: Fix and flip with bridge/rehab-to-let

#### **Transaction Types Observed**
- **Purchase**: Property purchase loans
- **Refinance**: Property refinancing loans

### 2.12 Loan Detail Page Structure (Observed)

#### **URL Structure**
- **Pattern**: `/admin/loans/{loanId}`
- **Loan ID**: Numeric ID format (e.g., `9153606`)
- **Page Title**: Property address (e.g., "4151 Sonoma Blvd")
- **Route Type**: Detail view (accessed from Pipeline page by clicking loan card/row)

#### **Page Header & Breadcrumb Navigation**
- **Breadcrumb Navigation**: 
  - "Pipeline" button (links back to `/admin/loans`)
  - Property address button ("4151 Sonoma Blvd") - current page
  - Hierarchical navigation path
- **Page Title**: Property address as H1 heading
- **Loan Status Badge**: "Closed" status indicator
- **Substatus Badge**: "Pending Servicing Approval" - additional status detail
- **Loan Metadata Display**:
  - **ID**: "ID 9153606" - Loan identifier
  - **Primary Borrower**: "4151 Sonoma LLC" (clickable link to Contacts subtab `/admin/loans/9153606/contacts`)
  - **Closing Date**: "10/10/2025" - Closing date display
  - **Product**: "DSCR" with "Customize" link (links to `/admin/loans/9153606/product`)
  - **Use of Funds**: "Refinance" - Transaction type

#### **Subtab Navigation**
- **Subtab Structure**: Horizontal tab navigation below header
- **Visible Tabs**:
  1. **General** - Currently active (default tab)
  2. **Documents** - Document management
  3. **Contacts** - Contact/borrower management
  4. **Charges** - Fee/charge management
  5. **Funding** - Funding information
  6. **Application** - Application details
  7. **Collateral** - Collateral information
  8. **Ellipses Menu** - Additional tabs/menu items
  9. **Mail** - Mail/messaging related to loan

- **Tab Behavior**: Tabs navigate to different sections of loan detail
- **Active Tab Indicator**: Visual distinction for active tab
- **URL Updates**: Likely updates URL with subtab identifier (e.g., `/admin/loans/{loanId}/contacts`)

#### **General Tab Structure** (Currently Active)

The General tab contains multiple sections with loan information:

**1. Terms Section**
- **Heading**: "Terms" (H4)
- **Edit Button**: Allows editing loan terms
- **Fields Displayed**:
  - **Loan Amount**: "$1,125,000.00" (currency formatted)
  - **Rate**: "6.25%" (percentage)
  - **Term**: "60 months" (duration)
  - **Origination**: "10/10/2025" (date)
  - **Maturity**: "10/09/2030" (date)

**2. Parameters Section**
- **Heading**: "Parameters" (H4)
- **Fields Displayed**:
  - **Rate Type**: "Fixed"
  - **Due Date**: "1" (day of month)
  - **Frequency**: "Monthly"
  - **Amortization Type**: "Fully Amortized"
  - **Amortization Term**: "60 months"
  - **First Payment**: "-" (empty/not set)

**3. Statistics Section**
- **Heading**: "Statistics" (H4)
- **Read-only Button**: Disabled, indicates read-only mode
- **Fields Displayed**:
  - **Loan To Value (LTV)**: "-" (empty/not calculated)

**4. Collateral Summary Section**
- **Heading**: "Collateral Summary" (H4)
- **Read-only Button**: Disabled, indicates read-only mode
- **Fields Displayed**:
  - **Purchase Price**: "$1,504,960.00" (currency formatted)
  - **As Is Value**: "-" (empty/not set)
  - **After-Repair Value (ARV)**: "-" (empty/not set)

**5. Payment Section**
- **Heading**: "Payment" (H4)
- **Edit Button**: Allows editing payment information
- **Fields Displayed**:
  - **Principal & Interest**: "$21,880.42" (currency formatted)
  - **To Trust**: "-" (empty/not set)
  - **Regular Payment**: "$21,880.42" (currency formatted)
  - **Paid Through**: "-" (empty/not set)
  - **Last Payment**: "-" (empty/not set)
  - **Next Payment Due**: "11/01/2025" (date)

**6. Classes Section**
- **Heading**: "Classes" (H4)
- **Edit Button**: Allows editing loan classes
- **Table Structure**:
  - Columns: "Name", "Amount", "Rate"
  - Data Row: "Senior" class with empty amount and rate fields ("-", "-")

**7. Banking Details Section**
- **Heading**: "Banking Details" (H4)
- **Edit Button**: Allows editing banking information
- **Fields Displayed**:
  - **Account Name**: "-" (empty/not set)
  - **Account Number**: "-" (empty/not set)
  - **Routing Number**: "-" (empty/not set)
  - **Type**: "-" (empty/not set)

**8. Closing Agent Section**
- **Heading**: "Closing Agent" (H4)
- **Empty State**: Text "This loan doesn't currently have a closing agent."
- **Add Link**: "Add a closing agent" - link to add closing agent
- **Conditional Display**: Shows empty state when no closing agent assigned

**9. Spread Allocation Section**
- **Heading**: "Spread Allocation" (H4)
- **Edit Button**: Allows editing spread allocation
- **As of Date**: "As of today" - indicates current date calculation
- **Table Structure**:
  - Columns: "Name", "Rate"
  - Data Row: "UC USDV Capital, Inc. Surplus and Deficit" with "0%" rate
  - Shows allocation breakdown for loan spread

#### **Section Patterns** (Observed)
- **Read-only Sections**: Some sections have "Read-only" disabled buttons (Statistics, Collateral Summary)
- **Editable Sections**: Most sections have "Edit" buttons (Terms, Payment, Classes, Banking Details, Spread Allocation)
- **Empty State Handling**: Fields show "-" when empty/not set
- **Currency Formatting**: Monetary values formatted with dollar sign and decimals
- **Date Formatting**: Dates in MM/DD/YYYY format
- **Percentage Formatting**: Rates shown with % symbol
- **Section Organization**: Logical grouping of related loan information

#### **Documents Tab Structure** (Observed)

**URL Structure**
- **Pattern**: `/admin/loans/{loanId}/documents`
- **Subtab Route**: Extends loan detail route with `/documents` path

**Page Header**
- **Select All Checkbox**: Checkbox button at top-left for bulk selection
- **Heading**: "Documents" (H3)
- **Generate Button**: Primary action button labeled "Generate"
  - Likely generates or creates new documents
  - Positioned top-right of documents section

**Document Categories**
Documents are organized into collapsible/expandable categories:

**1. Borrower Category**
- **Header**: "Borrower" with checkbox (for category selection)
- **Completion Status**: "10/11" - Shows 10 completed out of 11 total documents
- **Icon**: Image/icon indicator (likely folder/document icon)
- **Expandable**: Category can be expanded/collapsed
- **Documents Table**: Contains 11 documents (10 with files, 1 pending)

**2. Guarantor Category**
- **Header**: "Guarantor" with checkbox
- **Completion Status**: "4/9" - Shows 4 completed out of 9 total documents
- **Icon**: Image/icon indicator
- **Expandable**: Category can be expanded/collapsed
- **Documents Table**: Contains 9 documents (4 with files, 5 pending/requested/expired)

**3. Collateral Category**
- **Header**: "Collateral" with checkbox
- **Completion Status**: "2/8" - Shows 2 completed out of 8 total documents
- **Icon**: Image/icon indicator
- **Expandable**: Category can be expanded/collapsed
- **Documents Table**: Contains 8 documents (2 with files, 6 pending/in review/requested)

**4. Loan Category**
- **Header**: "Loan" with checkbox
- **Completion Status**: "0/5" - Shows 0 completed out of 5 total documents
- **Icon**: Image/icon indicator
- **Expandable**: Category can be expanded/collapsed
- **Documents Table**: Contains 5 documents (1 with file in review, 4 pending)

**5. Closing Category**
- **Header**: "Closing" with checkbox
- **Completion Status**: "0/10" - Shows 0 completed out of 10 total documents
- **Icon**: Image/icon indicator
- **Expandable**: Category can be expanded/collapsed
- **Documents Table**: Contains 10 documents (7 with files in review, 3 pending)

**6. Other Category**
- **Header**: "Other" with disabled checkbox
- **Completion Status**: "0/0" - Empty category
- **Icon**: Image/icon indicator
- **Empty State**: "This section is empty. Create new document"
- **No Documents**: Category has no documents

**Document Table Structure**
Each category contains a table with the following columns:

1. **Name Column**:
   - Document name with file type extension (PDF, PNG, JPG)
   - Examples: "Articles of Incorporation PDF", "Bank Statement PDF", "Appraisal Report PDF"
   - Checkbox in cell for document selection
   - Clickable (likely opens document viewer)

2. **Size Column**:
   - File size in human-readable format
   - Examples: "114.82 kB", "4.02 MB", "535.93 kB"
   - Empty for documents without files (pending/requested status)
   - Formatted with kB (kilobytes) or MB (megabytes)

3. **Uploaded Date Column**:
   - Date when document was uploaded
   - Format: "MMM DD, YYYY" (e.g., "Sep 26, 2025", "Oct 1, 2025", "Oct 16, 2025")
   - Empty for documents without files (pending/requested status)

4. **Status Column**:
   - Document status badge
   - Statuses observed:
     - **"Accepted"** - Document approved/accepted
     - **"Pending"** - Document awaiting upload/review
     - **"In review"** - Document currently being reviewed
     - **"Expired"** - Document expired (e.g., Credit Report)
     - **"Requested"** - Document requested but not yet provided
   - Color-coded status badges (inferred)

5. **Actions Column**:
   - Empty cell (likely contains action menu/buttons on hover)
   - May contain: View, Download, Delete, Replace actions

**Document Status System** (Observed)
- **Accepted**: Document has been reviewed and approved
- **Pending**: Document is expected but not yet uploaded
- **In review**: Document uploaded and currently under review
- **Expired**: Document has expired (time-sensitive documents like credit reports)
- **Requested**: Document has been requested from borrower/guarantor

**Document Types Observed**
- **Borrower Documents**: Articles of Incorporation, Articles of Organization, Bank Statements, Certificate of Good Standing, EIN, Entity Background, Entity Status, Experience Form, Operating Agreement, etc.
- **Guarantor Documents**: Background checks, Credit Reports, Bank Statements, Driver's License, Passport, Green Card, Authorization Forms
- **Collateral Documents**: Appraisal Report, Appraisal Review, CDA Collateral Desktop Analysis, Flood Certificate, Insurance Policies, Lease Agreement, Purchase Contract
- **Loan Documents**: ACH Form, Application, Commitment Letter, Executed Loan Docs, VOM (Verification of Mortgage)
- **Closing Documents**: CPL, Errors & Omissions Policy, Existing Loan Payoff, Funding Shield, HUD/Alta, Lien Search, Tax Certificate, Title Commitment, W9, Wire Instructions

**Category Completion Tracking**
- Each category shows completion ratio (e.g., "10/11", "4/9")
- Visual indicator of document collection progress
- Helps track which categories need more documents

**Selection System**
- **Category Checkbox**: Selects all documents in category
- **Document Checkbox**: Individual document selection
- **Select All Checkbox**: Selects all documents across all categories
- Enables bulk operations (download, delete, status update, etc.)

**File Format Support**
- **PDF**: Primary document format (most common)
- **PNG**: Image format (e.g., Driver's License)
- **JPG**: Image format (e.g., Passport)
- File type indicated in document name

**Empty State Handling**
- "Other" category shows empty state message
- Empty state: "This section is empty. Create new document"
- Indicates ability to create custom documents

#### **Document Detail/Viewer Page Structure** (Observed)

**URL Structure**
- **Pattern**: `/admin/loans/{loanId}/documents/{documentId}`
- **Document ID**: UUID format (e.g., `807accc8-f184-4c6d-8640-971984580f33`)
- **Page Navigation**: Hash-based page navigation (e.g., `#page-0`, `#page-1`, `#page-2`)
- **Route Type**: Detail view (accessed by clicking document name in Documents tab)

**Page Header**
- **Back Button**: Button at top-left to navigate back to Documents list
- **Document Title**: Document name as H3 heading (e.g., "Articles of Incorporation")
- **Document Metadata**:
  - File type: "PDF" (or other file type)
  - Last Updated: "Sep 26, 2025 at 11:51 am"
  - Date format: "MMM DD, YYYY at HH:MM am/pm"
  - Combined display: "PDF Last Updated Sep 26, 2025 at 11:51 am"

**Status Badge**
- **Status Button**: Status badge/button (e.g., "Accepted")
- **Status Display**: Shows current document status
- **Status Values**: Same as Documents tab (Accepted, Pending, In review, Expired, Requested)
- **Visual Indicator**: Color-coded status button

**Action Buttons**
Toolbar with multiple action buttons:
1. **Download Button**: Downloads document file
2. **Send for Signature Button**: Initiates signature workflow
3. **Request Document Button**: Requests document from borrower/guarantor
4. **Print Button**: Prints document
5. **Share Button**: Shares document (likely opens share dialog/modal)
6. **Comment Button**: Opens comments/annotation interface
7. **Additional Buttons**: More action buttons (likely menu or additional actions)

**Document Viewer**
- **Page Navigation**: 
  - Thumbnail navigation with clickable page links
  - URL hash fragments for direct page linking (`#page-0`, `#page-1`, `#page-2`, etc.)
  - Page thumbnails displayed as images
  - Multiple pages visible in thumbnail view
- **Document Display**:
  - Document pages rendered as images
  - Multiple page images displayed (observed 5+ pages)
  - PDF viewer functionality (inferred from PDF file type)
  - Scrollable document view (inferred)

**Page Navigation Structure**
- **Thumbnail Links**: Each page has a thumbnail image link
- **Hash Navigation**: Links use URL hash fragments (`#page-0`, `#page-1`, etc.)
- **Page Numbering**: Zero-indexed page numbers
- **Direct Linking**: Allows direct linking to specific pages
- **Visual Preview**: Thumbnails provide visual preview of pages

**Document Viewer Features** (Inferred)
- **Zoom Controls**: Likely zoom in/out functionality
- **Page Navigation**: Previous/Next page buttons (inferred)
- **Full Screen**: May support full-screen viewing
- **Search**: May support text search within document
- **Annotations**: Comment button suggests annotation capabilities
- **Print Preview**: Print button suggests print functionality

**Component Structure** (Inferred)
```
<DocumentDetailPage loanId={numericId} documentId={uuid}>
  <DocumentHeader>
    <BackButton />
    <DocumentTitle>{documentName}</DocumentTitle>
    <DocumentMetadata>
      <FileType>{fileType}</FileType>
      <LastUpdated>{lastUpdated}</LastUpdated>
    </DocumentMetadata>
  </DocumentHeader>
  <DocumentToolbar>
    <StatusBadge>{status}</StatusBadge>
    <DownloadButton />
    <SendForSignatureButton />
    <RequestDocumentButton />
    <PrintButton />
    <ShareButton />
    <CommentButton />
    <MoreActionsButton />
  </DocumentToolbar>
  <DocumentViewer>
    <PageThumbnails>
      {pages.map((page, index) => (
        <PageThumbnailLink href={`#page-${index}`}>
          <PageThumbnailImage />
        </PageThumbnailLink>
      ))}
    </PageThumbnails>
    <DocumentPages>
      {pages.map((page, index) => (
        <DocumentPage id={`page-${index}`}>
          <PageImage src={page.imageUrl} />
        </DocumentPage>
      ))}
    </DocumentPages>
  </DocumentViewer>
  <DocumentControls>
    <ZoomControls />
    <PageNavigation />
    <FullScreenButton />
  </DocumentControls>
</DocumentDetailPage>
```

**Navigation Pattern**
- **From Documents List**: Click document name → Navigate to `/admin/loans/{loanId}/documents/{documentId}`
- **Back Navigation**: Back button → Returns to `/admin/loans/{loanId}/documents`
- **Hash Navigation**: URL hash changes for page navigation (`#page-0`, `#page-1`)
- **Deep Linking**: Direct URLs to specific document pages supported

**Document Actions Workflow** (Inferred)
- **Download**: Downloads original document file
- **Send for Signature**: Opens signature request workflow (DocuSign, HelloSign, etc.)
- **Request Document**: Sends request to borrower/guarantor for document
- **Print**: Opens print dialog or generates print view
- **Share**: Opens share dialog (email, link sharing, permissions)
- **Comment**: Opens annotation/commenting interface for collaborative review

#### **Contacts Tab Structure** (Observed)

**URL Structure**
- **Pattern**: `/admin/loans/{loanId}/contacts`
- **Subtab Route**: Extends loan detail route with `/contacts` path
- **Linked from Header**: Primary Borrower link in loan header links to this tab

**Contact Cards Section**
Displayed at top of page, above the contacts table:
- **Borrower Card**:
  - Company/Entity name: "4151 Sonoma LLC"
  - Phone number: "(407) 922-0250" (clickable tel: link)
  - Role indicator: "Borrower"
  - Clickable name link (links to borrower detail page `/admin/borrowers/{borrowerId}`)

- **Guarantor Card**:
  - Person name: "Rodrigo Fachini Tavares"
  - Email: "rodrigo.fachini@gmail.com" (clickable mailto: link)
  - Phone number: "(407) 922-0250" (clickable tel: link)
  - Role indicator: "Guarantor"
  - Clickable name link (links to borrower/contact detail page `/admin/borrowers/{contactId}`)

**Page Header**
- **Heading**: "All Contacts" (H3)
- **Add Contact Button**: Primary action button labeled "Add Contact"
  - Allows adding new contacts to the loan
  - Opens contact addition interface/modal

**Contacts Table Structure**
Table with grouped rows and the following columns:

**Table Columns:**
1. **Name Column**:
   - Contact/company name
   - Clickable link to contact detail page
   - Examples: "4151 Sonoma LLC", "Rodrigo Fachini Tavares"

2. **Role Column**:
   - Contact role in relation to loan
   - Examples: "Borrower", "Guarantor"
   - Role types observed: Borrower, Guarantor (Viewers likely also supported)

3. **Associated With Column**:
   - Shows related contact/entity
   - Tooltip on hover showing full name
   - Examples: "Rodrigo Fachini Tavares" (associated with company), "4151 Sonoma LLC" (associated with person)
   - Clickable link to associated contact detail page

4. **Email Column**:
   - Email address (if available)
   - Clickable mailto: link (when email present)
   - Shows "-" when email not available

5. **Phone Column**:
   - Phone number
   - Clickable tel: link
   - Format: "(XXX) XXX-XXXX" (e.g., "(407) 922-0250")

6. **Owner Column**:
   - Owner/assignee initials (e.g., "KB", "EA")
   - Tooltip on hover showing full name
   - Similar to Tasks/Contacts assignee system

7. **Status Column**:
   - Contact status badge
   - Status observed: "Active"
   - Other statuses likely: Inactive, Pending, etc.

8. **Actions Column**:
   - Action button/menu (likely appears on hover)
   - May contain: Edit, Remove, View Details actions

**Table Grouping**
- **Group Header**: "Borrowers, Guarantors and Viewers"
  - Groups contacts by role category
  - Single row spanning multiple columns
  - Visual organization of related contacts

**Contact Types/Roles Observed**
- **Borrower**: Primary borrowing entity (company or person)
- **Guarantor**: Guarantor contact (person or entity)
- **Viewers**: Likely contacts with view-only access (not visible in current data)

**Contact Relationships**
- **Company ↔ Person**: Company "4151 Sonoma LLC" associated with person "Rodrigo Fachini Tavares"
- **Bidirectional Association**: Person shows company as "Associated With", company shows person as "Associated With"
- **Cross-Linking**: Clicking associated contact navigates to that contact's detail page

**Contact Detail Navigation**
- **From Name**: Clicking contact name → Navigate to `/admin/borrowers/{contactId}`
- **From Associated With**: Clicking associated contact → Navigate to associated contact detail page
- **Deep Linking**: Direct URLs to contact detail pages
- **Context Preservation**: Maintains loan context (breadcrumbs or back navigation)

**Contact Data Patterns**
- **Company Contacts**: Have company name, may have phone, associated with person
- **Person Contacts**: Have person name, email, phone, associated with company
- **Contact Information**: Varies by contact type (company vs. person)
- **Role-Based Display**: Different information shown based on role

**Integration with Loan Header**
- **Primary Borrower Link**: Header metadata shows "Primary Borrower" with link
- **Link Destination**: Links to Contacts tab (`/admin/loans/{loanId}/contacts`)
- **Quick Access**: Provides quick navigation to contact information

#### **Charges Tab Structure** (Observed)

**URL Structure**
- **Pattern**: `/admin/loans/{loanId}/charges`
- **Subtab Route**: Extends loan detail route with `/charges` path

**Page Header**
- **Heading**: "Charges" (H4)
- **Export Button**: Secondary action button labeled "Export"
  - Exports charges data (likely to CSV/Excel)
- **Add Charge Button**: Primary action button labeled "Add Charge"
  - Opens charge creation interface/modal
  - Allows adding new charges/fees to the loan

**Charges Table Structure**
Table with the following columns:

**Table Columns:**
1. **Date Column**:
   - Charge date
   - Format: "MMM DD, YYYY" (e.g., "Sep 4, 2025")
   - Date when charge was created or applied

2. **Description Column**:
   - Charge description/type
   - Examples: "Origination (Points)", "Processing"
   - Describes what the charge is for

3. **Payable To Column**:
   - Entity/person to whom charge is payable
   - Shows "-" when not specified or not applicable
   - May link to contact/vendor detail page

4. **Due Date Column**:
   - Due date for the charge
   - Shows "-" when not set
   - Date format likely: "MMM DD, YYYY"

5. **Original Amount Column**:
   - Original charge amount
   - Shows "-" when not set
   - Currency formatted (inferred)

6. **Amount Due Column**:
   - Current amount due/remaining
   - Shows "-" when not set or fully paid
   - Currency formatted (inferred)

7. **Status Column**:
   - Charge status badge
   - Status observed: "Unpaid"
   - Other statuses likely: Paid, Partially Paid, Waived, etc.

8. **Actions Column**:
   - Action button/menu (likely appears on hover)
   - May contain: Edit, Delete, Mark as Paid, Waive actions

**Charge Data Observed**
- **Origination (Points)**: Charge dated "Sep 4, 2025", Status "Unpaid", no amounts or dates specified
- **Processing**: Charge dated "Sep 4, 2025", Status "Unpaid", no amounts or dates specified

**Charge Status System** (Observed)
- **Unpaid**: Charge has not been paid
- **Other Statuses** (Inferred): Paid, Partially Paid, Waived, Cancelled

**Charge Types Observed**
- **Origination (Points)**: Origination fee/points charge
- **Processing**: Processing fee charge
- **Other Types** (Inferred): Underwriting, Appraisal, Title, Recording, Legal, Inspection, etc.

**Empty State**
- Empty row displayed when no charges exist (shows "-" in columns)
- Indicates table structure even when empty

**Charge Management Features** (Inferred)
- **Add Charge**: Create new charges with date, description, amount, due date, payable to
- **Edit Charge**: Modify existing charge details
- **Delete Charge**: Remove charges from loan
- **Mark as Paid**: Update charge status to paid
- **Waive Charge**: Waive/forgive charge
- **Export**: Export charges list for accounting/reporting

#### **Funding Tab Structure** (Observed)

**URL Structure**
- **Pattern**: `/admin/loans/{loanId}/funding`
- **Subtab Route**: Extends loan detail route with `/funding` path

**Funding Section**

**Section Header**
- **Heading**: "Funding" (H4)
- **Export Button**: Secondary action button labeled "Export"
  - Exports funding data (likely to CSV/Excel)
- **Transfer Button**: Action button labeled "Transfer"
  - Likely transfers funding between accounts/investors
- **Add Funding Button**: Primary action button labeled "Add Funding"
  - Opens funding addition interface/modal
  - Allows adding new funding/investor participation

**Funding Table Structure**
Table with the following columns:

**Table Columns:**
1. **Investor Column**:
   - Investor name/entity
   - Checkbox in header (disabled) - likely for bulk selection
   - Individual investor rows may have checkboxes for selection

2. **Yield Column**:
   - Yield/return rate percentage
   - Shows expected or actual yield for investor

3. **Invested / Committed Column**:
   - Amount invested or committed by investor
   - Combined column showing both invested and committed amounts
   - Currency formatted (inferred)

4. **Returned Column**:
   - Amount returned to investor
   - Shows principal/returns paid back
   - Currency formatted (inferred)

5. **Balance Column**:
   - Current balance/remaining amount
   - Outstanding investment balance
   - Currency formatted (inferred)

6. **Income Column**:
   - Income/earnings for investor
   - Shows income generated from investment
   - Currency formatted (inferred)

7. **Status Column**:
   - Funding/investment status badge
   - Status values likely: Active, Completed, Pending, etc.

8. **Actions Column**:
   - Action button/menu (likely appears on hover)
   - May contain: Edit, Remove, View Details actions

**Funding Table Empty State**
- **Message**: "None have been created yet"
- **Display**: Single cell spanning table width
- **Indicates**: No funding/investor participation records exist

**History Section**

**Section Header**
- **Heading**: "History" (H4)
- **Export Button**: Secondary action button labeled "Export"
  - Exports funding history data

**History Table Structure**
Table with the following columns:

**Table Columns:**
1. **Date Column**:
   - Transaction/event date
   - Format likely: "MMM DD, YYYY"

2. **Type Column**:
   - Transaction/event type
   - Types likely: Funding, Return, Transfer, Payment, etc.

3. **Principal Column**:
   - Principal amount for transaction
   - Currency formatted (inferred)

4. **Status Column**:
   - Transaction status badge
   - Status values likely: Completed, Pending, Failed, etc.

5. **Actions Column**:
   - Action button/menu (likely appears on hover)
   - May contain: View, Edit, Cancel actions

**History Table Empty State**
- **Message**: "None have been created yet"
- **Display**: Single cell spanning table width
- **Indicates**: No funding history records exist

**Funding Features** (Inferred)
- **Add Funding**: Add investor participation with yield, invested amount
- **Transfer**: Transfer funding between investors or accounts
- **Track Returns**: Track returned amounts and balances
- **Income Tracking**: Track income/earnings for each investor
- **History Logging**: Maintain history of all funding transactions
- **Export**: Export funding and history data for reporting

**Investor Funding Workflow** (Inferred)
1. **Add Funding**: Create investor participation record
2. **Set Yield**: Define yield/return rate for investor
3. **Track Investment**: Monitor invested/committed amounts
4. **Record Returns**: Log returned amounts to investors
5. **Calculate Balance**: Track remaining balance
6. **Track Income**: Record income/earnings
7. **History Logging**: All transactions logged in History section

#### **Application Tab Structure** (Observed)

**URL Structure**
- **Pattern**: `/admin/loans/{loanId}/application`
- **Subtab Route**: Extends loan detail route with `/application` path
- **Read-only View**: Displays application data submitted by borrower

**Application Header**
- **Submission Info**: "Application submitted by [borrower name]" with clickable link
  - Link: "Rodrigo Fachini Tavares" (links to `/admin/borrowers/{borrowerId}`)
  - Submission Date: "on Sep 26, 2025"
  - Format: "on MMM DD, YYYY"
- **Request Changes Button**: Action button labeled "Request Changes"
  - Allows requesting changes/revisions to application
  - May send notification to borrower
- **Download PDF Button**: Action button labeled "Download PDF"
  - Downloads application as PDF document
  - Exports formatted application for records/review

**Transaction Details Section**
- **Heading**: "Transaction Details" (H4)
- **Fields Displayed**:
  - **Use of Funds**: "Cash Out Refinance" (transaction type)
  - **Exit Strategy**: "Hold" (loan exit strategy)
  - **Loan Amount**: "$900,000.00" (currency formatted)
  - **Closing Date**: "10/10/2025" (date format)

**Property Section**
- **Heading**: "Property" (H4)
- **Fields Displayed**:
  - **Property Address**: "4151 Sonoma Blvd, Kissimmee, Florida, United States 34741"
    - Full address with street, city, state, country, zip code
  - **Property Type**: "Single-Family" (property classification)
  - **Purchase Price**: "$1,504,960.00" (currency formatted)
  - **ARV** (After-Repair Value): "$1,684,860.00" (currency formatted)
  - **Total Rehab**: "$180,000.00" (currency formatted)

**Borrower Details Section**
- **Heading**: "Borrower Details" (H4)

**Borrower Subsection**
- **Heading**: "Borrower" (H4)
- **Fields Displayed**:
  - **Company Name**: "4151 Sonoma LLC"
  - **Type**: "Limited Liability Company" (entity type)
  - **Jurisdiction**: "Florida" (state of incorporation/organization)
  - **Phone**: "(407) 922-0250" (formatted phone number)

**Guarantor Subsection**
- **Heading**: "Guarantor" (H4)
- **Fields Displayed**:
  - **Full Name**: "Rodrigo Fachini Tavares"
  - **Credit Score**: "771" (numeric credit score)
  - **Number of Flips**: "-" (empty/not specified, may be numeric count)
  - **Phone**: "(407) 922-0250" (formatted phone number)
  - **Email**: "rodrigo.fachini@gmail.com" (clickable mailto: link)

**Declarations Section**
- **Heading**: "Declarations" (H4)
- **Questions and Answers**:
  1. **"Are there any outstanding judgments against you?"**
     - Answer: "No"
  2. **"Have you been declared bankrupt in the past 7 years?"**
     - Answer: "No"
  3. **"Have you had property foreclosed upon or given title or deed in lieu thereof in the last 7 years?"**
     - Answer: "No"
- **Disclosure Agreement**:
  - Text: "I agree with the terms and certify that the information provided is true and accurate"
  - **Signature**: Image display of signature
  - **Signed Date**: "Signed Sep 26, 2025"
  - Format: "Signed MMM DD, YYYY"

**Application Data Patterns**
- **Read-only Display**: All fields displayed as read-only text
- **Formatted Values**: Currency, dates, phone numbers formatted consistently
- **Linked Values**: Borrower name, email linked to contact pages/actions
- **Section Organization**: Logical grouping of related application information
- **Yes/No Questions**: Binary answers to declaration questions

**Application Workflow** (Inferred)
1. **Borrower Submission**: Borrower fills out application form (in borrower-facing interface)
2. **Application Review**: Admin reviews application in this tab
3. **Request Changes**: Admin can request changes if needed
4. **Download/Export**: Admin can download application as PDF
5. **Underwriting**: Application data used for loan underwriting process

**Integration with Borrower Portal** (Inferred)
- **Borrower-facing Form**: Application form exists in borrower portal/interface
- **Data Sync**: Application data synced between borrower and admin views
- **Status Tracking**: Application submission status tracked
- **Change Requests**: Request Changes button may notify borrower to update application

#### **Collateral Tab Structure** (Observed)

**URL Structure**
- **Pattern**: `/admin/loans/{loanId}/collateral`
- **Subtab Route**: Extends loan detail route with `/collateral` path

**Page Header**
- **Heading**: "Collateral Details" (H3)
- **Order Flood Report Button**: Disabled action button
  - Likely orders flood report for property
  - Disabled state indicates not available or already ordered
- **Add New Property Button**: Disabled action button
  - Allows adding additional properties as collateral
  - Disabled state indicates not available or not applicable

**Map Integration**
- **Google Maps Embed**: Interactive map showing property location
- **Map Controls**: 
  - Keyboard shortcuts button
  - Map Data button
  - "Open this area in Google Maps" link (opens in new window)
  - Links to Google Maps terms and "Report a map error"
- **Map Coordinates**: Latitude/longitude embedded (28.319106, -81.448791)
- **Map Zoom**: Zoom level set (z=10)
- **Integration**: Full Google Maps API integration for property visualization

**Property Details Section**
- **Heading**: "Property Details" (H4)
- **Address Display**:
  - Street: "4151 Sonoma Blvd"
  - City, State, Zip: "Kissimmee, Florida 34741"
  - Country: "United States"
  - County: "-" (empty/not displayed)
- **Tab Navigation**: 
  - Tabs visible: "Property Details", "Valuations", "Insurance", "Flood Report"
  - Likely switches between different property information views
  - "Property Details" tab currently active

**Property Value Section**
- **Heading**: "Property Value" (H4)
- **Edit Button**: Allows editing property value information
- **Fields Displayed**:
  - **Purchase Price**: "$1,504,960.00" (currency formatted)
  - **Purchase Date**: "05/09/2024" (date format: MM/DD/YYYY)
  - **Existing Debt**: "$0" (currency formatted)
  - **As Is Value**: "-" (empty/not set)
  - **ARV - Lender**: "-" (empty/not set)
  - **ARV - Borrower**: "$1,684,860.00" (currency formatted)
  - **Appraisal Ordered**: "Yes" (boolean/status indicator)

**Taxes & HOA Section**
- **Heading**: "Taxes & HOA" (H4)
- **Edit Button**: Allows editing taxes and HOA information
- **Fields Displayed**:
  - **Property Taxes**: "-" (empty/not set)
  - **HOA Fees**: "-" (empty/not set)
  - **HOA Due Date**: "-" (empty/not set)

**Property Features Section**
- **Heading**: "Property Features" (H4)
- **Edit Button**: Allows editing property features
- **Fields Displayed**:
  - **Units**: "1" (numeric count)
  - **Gross Livable Area (GLA)**: "-" (empty/not set)
  - **Property Type**: "Single-Family" (property classification)
  - **Year Built**: "-" (empty/not set)
  - **Construction Materials**: "Concrete Block" (construction type)

**Unit Details Section**
- **Heading**: "Unit Details" (H4)
- **Add Unit Button**: Action button labeled "Add Unit"
  - Allows adding individual units (for multi-unit properties)
- **Open Worksheet Button**: Action button labeled "Open Worksheet"
  - Opens unit worksheet/analysis tool
  - May open modal, new page, or spreadsheet-like interface

**Section Patterns** (Observed)
- **Editable Sections**: Most sections have "Edit" buttons (Property Value, Taxes & HOA, Property Features)
- **Empty State Handling**: Fields show "-" when empty/not set
- **Currency Formatting**: Monetary values formatted with dollar sign and decimals
- **Date Formatting**: Dates in MM/DD/YYYY format
- **Boolean Display**: Yes/No values shown as text ("Yes")
- **Map Integration**: Google Maps embedded for property visualization

**Property Information Organization**
- **Main Sections**: Property Details, Property Value, Taxes & HOA, Property Features, Unit Details
- **Sub-tabs**: Property Details section has sub-tabs (Property Details, Valuations, Insurance, Flood Report)
- **Comprehensive Coverage**: All aspects of collateral property information included

**Valuation Data**
- **Multiple ARV Values**: Separate ARV values for Lender and Borrower
- **Purchase Information**: Purchase price and date tracked
- **As Is Value**: Current property value
- **Appraisal Status**: Tracks whether appraisal has been ordered

**Ellipses/More Menu Structure** (Observed)

**Menu Trigger**
- **Location**: Ellipses icon/menu button positioned after "Collateral" tab
- **Label**: "More" (inferred from tab structure)
- **Type**: Dropdown/popup menu
- **Visibility**: Clicking ellipses opens menu with additional subtabs/actions

**Menu Options** (Observed)
The ellipses menu contains the following clickable options:

1. **Amortization Schedule**
   - Navigates to amortization schedule view/subtab
   - Shows loan payment schedule over time

2. **Payments**
   - Navigates to payments view/subtab
   - Shows payment history and schedule

3. **Change Log**
   - Navigates to change log view/subtab
   - Shows audit trail/history of loan changes

4. **Email Log**
   - Navigates to email log view/subtab
   - Shows email communication history for loan

5. **Notifications**
   - Navigates to notifications view/subtab
   - Shows notification history/alerts for loan

6. **Settings**
   - Navigates to loan settings view/subtab
   - Allows configuring loan settings/preferences

7. **Generate Quote**
   - Action button (may trigger workflow)
   - Generates quote from loan data

8. **Mark Loan as Sold**
   - Action button (may trigger workflow)
   - Updates loan status to "Sold"

9. **Move to Servicing**
   - Action button (may trigger workflow)
   - Transfers loan to servicing status/interface

10. **Share with Funding Partner**
    - Action button (may trigger workflow/modal)
    - Shares loan information with funding partner

11. **Deny & Archive**
    - Action button (destructive action)
    - Denies loan application and archives it

12. **Archive**
    - Action button
    - Archives loan (without denying)

13. **Duplicate**
    - Action button
    - Creates duplicate copy of loan

14. **Delete**
    - Action button (destructive action)
    - Deletes loan (likely requires confirmation)

**Menu Organization** (Inferred)
- **Navigation Items**: Items that navigate to subtabs (Amortization Schedule, Payments, Change Log, Email Log, Notifications, Settings)
- **Action Items**: Items that trigger actions/workflows (Generate Quote, Mark Loan as Sold, Move to Servicing, Share with Funding Partner)
- **Management Items**: Items for loan lifecycle management (Deny & Archive, Archive, Duplicate, Delete)
- **Visual Separators**: May have visual separators between groups (not visible in snapshot but common pattern)

**Menu Behavior** (Inferred)
- **Clickable Areas**: Each menu item is clickable/navigable
- **Navigation**: Clicking navigation items likely updates URL to corresponding subtab route
- **Actions**: Clicking action items may trigger modals, workflows, or confirmations
- **Menu Dismissal**: Menu closes after selection or click outside

**Route Patterns** (Inferred)
Navigation items likely use route patterns:
- `/admin/loans/{loanId}/amortization` or `/admin/loans/{loanId}/schedule`
- `/admin/loans/{loanId}/payments`
- `/admin/loans/{loanId}/changelog` or `/admin/loans/{loanId}/changes`
- `/admin/loans/{loanId}/emaillog` or `/admin/loans/{loanId}/emails`
- `/admin/loans/{loanId}/notifications`
- `/admin/loans/{loanId}/settings`

**Component Structure** (Inferred)
```
<LoanSubTabs>
  <Tab name="General" />
  <Tab name="Documents" />
  <Tab name="Contacts" />
  <Tab name="Charges" />
  <Tab name="Funding" />
  <Tab name="Application" />
  <Tab name="Collateral" />
  <MoreMenu>
    <MenuItem type="navigation" label="Amortization Schedule" route="/admin/loans/{loanId}/amortization" />
    <MenuItem type="navigation" label="Payments" route="/admin/loans/{loanId}/payments" />
    <MenuItem type="navigation" label="Change Log" route="/admin/loans/{loanId}/changelog" />
    <MenuItem type="navigation" label="Email Log" route="/admin/loans/{loanId}/emaillog" />
    <MenuItem type="navigation" label="Notifications" route="/admin/loans/{loanId}/notifications" />
    <MenuItem type="navigation" label="Settings" route="/admin/loans/{loanId}/settings" />
    <MenuSeparator />
    <MenuItem type="action" label="Generate Quote" onClick={generateQuote} />
    <MenuItem type="action" label="Mark Loan as Sold" onClick={markAsSold} />
    <MenuItem type="action" label="Move to Servicing" onClick={moveToServicing} />
    <MenuItem type="action" label="Share with Funding Partner" onClick={shareWithFundingPartner} />
    <MenuSeparator />
    <MenuItem type="action" label="Deny & Archive" onClick={denyAndArchive} destructive />
    <MenuItem type="action" label="Archive" onClick={archive} />
    <MenuItem type="action" label="Duplicate" onClick={duplicate} />
    <MenuItem type="action" label="Delete" onClick={delete} destructive />
  </MoreMenu>
  <Tab name="Mail" />
</LoanSubTabs>
```

#### **Amortization Schedule Tab Structure** (Observed)

**URL Structure**
- **Pattern**: `/admin/loans/{loanId}/amortization`
- **Subtab Route**: Extends loan detail route with `/amortization` path
- **Access**: Accessed from ellipses/More menu

**Page Header**
- **Heading**: "Amortization Schedule" (H4)
- **Export Button**: Action button labeled "Export"
  - Exports amortization schedule data (likely to CSV/Excel/PDF)
  - Positioned top-right of section

**Amortization Schedule Table**
Table showing loan payment schedule with the following columns:

**Table Columns:**
1. **Payment Column**:
   - Payment number (sequential: 1, 2, 3, etc.)
   - Numeric display

2. **Due Column**:
   - Payment due date
   - Format: "MM/DD/YYYY" (e.g., "11/01/2025", "12/01/2025", "01/01/2026")
   - Monthly payment dates

3. **Principal Column**:
   - Principal payment amount
   - Currency formatted (e.g., "$16,021.05", "$16,104.49")
   - First payment shows "-" (interest-only payment)
   - Subsequent payments show principal amount
   - Principal increases over time (amortization schedule)

4. **Interest Column**:
   - Interest payment amount
   - Currency formatted (e.g., "$4,238.01", "$5,859.37", "$5,775.93")
   - First payment: "$4,238.01" (interest-only)
   - Interest decreases over time as principal is paid down

5. **Total Payment Column**:
   - Total payment amount (Principal + Interest)
   - Currency formatted
   - Consistent amount: "$21,880.42" for most payments
   - First payment: "$4,238.01" (interest-only)

6. **Balance Column**:
   - Remaining loan balance after payment
   - Currency formatted (e.g., "$1,125,000.00", "$1,108,978.95")
   - Decreases with each payment
   - Shows loan payoff progression

**Payment Schedule Patterns** (Observed)
- **Payment 1**: Interest-only payment ($4,238.01), no principal ("-"), balance unchanged ($1,125,000.00)
- **Payment 2-60**: Regular amortized payments with principal and interest
- **Principal Increase**: Principal payment increases each period (amortization schedule)
- **Interest Decrease**: Interest payment decreases each period (as balance decreases)
- **Total Payment**: Consistent total payment amount ($21,880.42) for most payments
- **Balance Reduction**: Balance decreases with each principal payment

**Pagination**
- **Display**: "Showing 50 of 61" (50 payments displayed, 61 total)
- **Load More Button**: Button labeled "Load more"
  - Loads next batch of payments (likely loads remaining 11 payments)
  - Infinite scroll pattern or pagination

**Schedule Calculation** (Inferred)
- **Loan Terms**: Based on loan amount, rate, and term from loan details
- **Amortization Method**: Fully amortized (based on General tab information)
- **First Payment**: Interest-only payment (deferred principal start)
- **Regular Payments**: Standard amortization calculation (principal + interest = total)
- **Balance Calculation**: Starting balance - principal payment = new balance

**Export Functionality**
- **Export Button**: Exports full amortization schedule
- **Export Format**: Likely CSV, Excel, or PDF
- **Export Scope**: All 61 payments (full schedule)

#### **Change Log Tab Structure** (Observed)

**URL Structure**
- **Pattern**: `/admin/loans/{loanId}/changeLog`
- **Subtab Route**: Extends loan detail route with `/changeLog` path (camelCase)
- **Access**: Accessed from ellipses/More menu

**Page Header**
- **Heading**: "Change Log" (H4)
- **Filter Button**: Action button labeled "Filter"
  - Opens filter interface/dropdown
  - Allows filtering change log entries by criteria
- **Search Box**: Search input with placeholder "Search"
  - Allows searching change log entries
  - Searches across change descriptions, users, references

**Change Log Table**
Table showing audit trail of all loan changes with the following columns:

**Table Columns:**
1. **Timestamp Column**:
   - Date and time of change
   - Format: "MMM DD, YYYY at HH:MM am/pm" (e.g., "Nov 7, 2025 at 6:49 pm", "Sep 26, 2025 at 12:06 pm")
   - Chronological ordering (newest first, inferred)

2. **User Column**:
   - User initials who made the change
   - Examples: "TB", "EA", "RF"
   - Tooltip likely shows full name on hover
   - Different users: Admin users (EA, TB) and Borrower (RF)

3. **Reference Column**:
   - Field/attribute that was changed
   - Examples: "Status", "Substatus", "Loan Amount", "Rate", "Purchase Price"
   - May also show action descriptions (e.g., "Evan A. Shields created 4151 Sonoma Blvd")

4. **Change Details Column**:
   - Old value → New value format
   - Examples:
     - "Approved Closed" (status change)
     - "$900,000.00 $1,125,000.00" (loan amount change)
     - "3.000% 6.250%" (rate change)
     - "(blank) Fully Amortized" (field set from empty)
   - Shows before/after values for field changes
   - May be empty for certain action types

**Change Types Observed**
1. **Status Changes**:
   - Status field changes (e.g., "Underwriting Approved", "Approved Closed")
   - Status transitions through loan lifecycle

2. **Substatus Changes**:
   - Substatus field changes (e.g., "Pending Insurance", "Pending Servicing Approval")
   - More granular status updates

3. **Field Value Changes**:
   - Loan Amount, Rate, Term, Origination, Maturity
   - Amortization Type, Due Date
   - Purchase Date, Appraisal Ordered, Existing Debt
   - Purchase Price, ARV - Borrower, Exit Strategy, Loan Type
   - Number Of Grace Days
   - Application form fields (declaration questions)

4. **Action Events**:
   - "created 4151 Sonoma Blvd" - Loan creation
   - "updated 4151 Sonoma Blvd" - General loan updates
   - "signed application 4151 Sonoma Blvd" - Application signature

5. **Application Submission**:
   - Multiple application form fields changed by borrower (RF)
   - Shows borrower completing application form
   - Signature event logged

**Change Value Formats**
- **Currency**: "$900,000.00 $1,125,000.00" (old → new)
- **Percentage**: "3.000% 6.250%" (old → new)
- **Date**: "10/10/2025 10/10/2025" (no change) or "(blank) 05/09/2024" (set from empty)
- **Boolean/Text**: "(blank) Yes", "(blank) No", "(blank) Hold", "(blank) Rentals"
- **Status Values**: "Approved Closed", "Underwriting Approved", "Pending Insurance", etc.
- **Empty State**: "(blank)" indicates field was previously empty

**User Types**
- **Admin Users**: "EA" (Evan A. Shields), "TB" (likely another admin)
- **Borrower**: "RF" (Rodrigo Fachini Tavares)
- User identification via initials with tooltips

**Change Log Features**
- **Complete Audit Trail**: All changes to loan tracked
- **Chronological Order**: Changes listed chronologically (newest first)
- **User Attribution**: Each change attributed to user who made it
- **Value Tracking**: Before/after values shown for field changes
- **Action Logging**: System actions (create, update) logged
- **Search/Filter**: Search and filter capabilities for finding specific changes

**Pagination/Display**
- **Display**: "Showing 31 of 31" (all changes visible)
- **No Pagination**: All changes fit on single page (or small enough dataset)
- **Full History**: Complete change history displayed

**Component Structure** (Inferred)
```
<ChangeLogTab loanId={numericId}>
  <ChangeLogHeader>
    <ChangeLogTitle>Change Log</ChangeLogTitle>
    <FilterButton onClick={openFilter} />
    <SearchBox placeholder="Search" onChange={handleSearch} />
  </ChangeLogHeader>
  <ChangeLogTable>
    <TableHeader>
      <ColumnHeader>Timestamp</ColumnHeader>
      <ColumnHeader>User</ColumnHeader>
      <ColumnHeader>Reference</ColumnHeader>
      <ColumnHeader>Change Details</ColumnHeader>
    </TableHeader>
    {changes.map(change => (
      <ChangeRow
        timestamp={change.timestamp}
        user={change.user}
        reference={change.reference}
        oldValue={change.oldValue}
        newValue={change.newValue}
        changeType={change.type} // field_change, status_change, action
      />
    ))}
  </ChangeLogTable>
  <ChangeLogFooter>
    <DisplayCount>Showing {visibleCount} of {totalCount}</DisplayCount>
  </ChangeLogFooter>
</ChangeLogTab>
```

#### **Email Log Tab Structure** (Observed)

**URL Structure**
- **Pattern**: `/admin/loans/{loanId}/emailLog`
- **Subtab Route**: Extends loan detail route with `/emailLog` path (camelCase)
- **Access**: Accessed from ellipses/More menu

**Page Header**
- **Heading**: "Email Log" (H4)
- **Filter Button**: Action button labeled "Filter"
  - Opens filter interface/dropdown
  - Allows filtering email log entries by criteria (recipient, date, status, etc.)

**Email Log Table**
Table showing all emails sent related to the loan with the following columns:

**Table Columns:**
1. **To Column**:
   - Recipient name(s)
   - Examples: "Rodrigo Fachini Tavares", "Evan A. Shields", "Kian Billings", "Wendy Castillo", "Mikey Rosello", "Todd Billings"
   - Clickable (tooltip on hover showing full name)
   - May link to contact/borrower detail page

2. **Subject Column**:
   - Email subject line
   - Examples:
     - "Your loan has been approved"
     - "Download Ready for 4151 Sonoma Blvd"
     - "A document has been uploaded (Entity Status)"
     - "You have 1 document requests"
     - "Application Received"
   - Clickable (likely opens email detail/view)

3. **Sent Column**:
   - Date email was sent
   - Format: "MMM DD" (e.g., "Nov 7", "Oct 9", "Sep 26")
   - Tooltip on hover shows full date/time
   - Abbreviated format (month and day only)

4. **Status Column**:
   - Email status badge
   - Status observed: "Sent"
   - Other statuses likely: Pending, Failed, Bounced, Opened, etc. (not visible in current data)

**Email Types Observed**
1. **Loan Approval Emails**:
   - Subject: "Your loan has been approved"
   - Sent to borrower (Rodrigo Fachini Tavares)
   - Notifies borrower of loan approval

2. **Document Download Ready Emails**:
   - Subject: "Download Ready for 4151 Sonoma Blvd"
   - Sent to admin users (Evan A. Shields, Kian Billings)
   - Notifies when documents are ready for download

3. **Document Upload Notifications**:
   - Subject: "A document has been uploaded ([Document Name])"
   - Sent to admin users (Evan A. Shields)
   - Notifies when documents are uploaded
   - Document types: Entity Status, Bank Statement, Passport, Property/Dwelling Insurance Policy, Drivers License, Bank Statement - Current Month, Bank Statement - Previous Month, EIN, Purchase Contract, Operating Agreement, Articles of Incorporation

4. **Document Request Emails**:
   - Subject: "You have [X] document requests"
   - Sent to borrower (Rodrigo Fachini Tavares)
   - Notifies borrower of pending document requests
   - Shows count of requested documents (11, 7, 4, 1)

5. **Application Received Emails**:
   - Subject: "Application Received"
   - Sent to multiple recipients (Kian Billings, Wendy Castillo, Mikey Rosello, Todd Billings, Evan A. Shields, Rodrigo Fachini Tavares)
   - Notifies when application is received
   - Sent to borrower and team members

**Email Recipients**
- **Borrower**: Rodrigo Fachini Tavares (loan-related notifications)
- **Admin Users**: Evan A. Shields, Kian Billings (document and loan updates)
- **Team Members**: Wendy Castillo, Mikey Rosello, Todd Billings (application notifications)

**Email Communication Patterns**
- **Borrower Communications**: Approval notices, document requests
- **Internal Communications**: Document uploads, download ready notifications
- **Team Notifications**: Application received, shared updates
- **Automated Emails**: System-generated notifications for document events

**Date Patterns**
- **Most Recent**: Nov 7, 2025 (loan approval)
- **Recent Activity**: Oct 9, Oct 6, Oct 1 (document-related)
- **Application Period**: Sep 26, 2025 (application submission, document uploads)
- **Initial Requests**: Sep 25, Sep 4 (document requests)

**Display/Pagination**
- **Display**: "Showing 26 of 26" (all emails visible)
- **No Pagination**: All emails fit on single page
- **Complete History**: Full email communication history for loan

**Email Log Features**
- **Complete Email History**: All emails related to loan tracked
- **Chronological Order**: Emails listed chronologically (newest first, inferred)
- **Recipient Tracking**: Shows who received each email
- **Subject Tracking**: Shows email subject/topic
- **Status Tracking**: Email delivery status
- **Filter/Search**: Filter capability for finding specific emails
- **Integration**: Connected to email system for sending and tracking

**Component Structure** (Inferred)
```
<EmailLogTab loanId={numericId}>
  <EmailLogHeader>
    <EmailLogTitle>Email Log</EmailLogTitle>
    <FilterButton onClick={openFilter} />
  </EmailLogHeader>
  <EmailLogTable>
    <TableHeader>
      <ColumnHeader>To</ColumnHeader>
      <ColumnHeader>Subject</ColumnHeader>
      <ColumnHeader>Sent</ColumnHeader>
      <ColumnHeader>Status</ColumnHeader>
    </TableHeader>
    {emails.map(email => (
      <EmailRow
        recipient={email.recipient}
        subject={email.subject}
        sentDate={email.sentDate}
        status={email.status}
        link={email.detailLink}
      />
    ))}
  </EmailLogTable>
  <EmailLogFooter>
    <DisplayCount>Showing {visibleCount} of {totalCount}</DisplayCount>
  </EmailLogFooter>
</EmailLogTab>
```

#### **Notifications Tab Structure** (Observed)

**URL Structure**
- **Pattern**: `/admin/loans/{loanId}/notifications`
- **Subtab Route**: Extends loan detail route with `/notifications` path
- **Access**: Accessed from ellipses/More menu
- **Purpose**: Notification preferences/settings configuration page

**Page Structure**
- **Notification Categories**: Organized by functional area
- **Notification Items**: Each notification type has description and toggle controls
- **Configuration Interface**: Allows enabling/disabling notifications and delivery methods

**Notification Categories and Types**

**1. Budgets Category**
- **Budget Approved**: Sent to borrowers and guarantors when a budget is approved by the lender
- **Budget Rejected**: Sent to borrowers and guarantors when a budget is rejected by the lender
- **Budget Submitted**: Sent to the account owners on the loan when a budget is submitted

**2. Documents Category**
- **Document Rejected**: Sent to the contact when a document they uploaded was rejected by the lender
- **Document Requested**: Sent to the contact when the lender requests a document (5 min batches)
- **Document Shared**: Sent to the contact with whom a document is shared. If shared from a loan, these notifications will be delivered to both borrowers and guarantors
- **Document Uploaded**: Sent to account owners on a loan when a document is uploaded

**3. Draw Requests Category**
- **Draw Approved**: Sent to borrowers and guarantors when a draw is approved by the lender
- **Draw Rejected**: Sent to borrowers and guarantors when a draw is rejected by the lender
- **Draw Released**: Sent to borrowers and guarantors when a draw is released by the lender
- **Draw Rollback**: Sent to borrowers and guarantors when a draw is rolled back from an approved status by the lender
- **Draw Submitted**: Sent to the account owners on a loan when the draw is submitted by the borrower

**4. E-signature Category**
- **Document was Recalled**: Sent to the signers of a document when it is recalled
- **Signing Complete (Owners)**: Sent to the account owners on a loan when all signers have completed their signatures on a document
- **Signing Complete (Signers)**: Sent to all document signers when all signers have completed their signatures on a document
- **Signing was Declined**: Sent to the account owners on a loan or contact when a signer declined to sign a document
- **Thanks for Signing**: Sent to a signer when they have completed their signature on a document
- **Time to Sign**: Sent to a signer on a document when it's their turn to sign

**5. General Category**
- **Loan Share Accepted**: Sent to all lender account admins when a loan you've shared with a funding partner is accepted
- **Loan Share Rejected**: Sent to all lender account admins when a loan you've shared with a funding partner is rejected
- **Loan Shared**: Sent to all lender account admins when a loan is shared with you by a linked lender
- **New Comment**: Sent to a user when they have been tagged in a comment

**6. Origination Category**
- **Application Received (Admin)**: Sent to all account admins informing them that a loan application was received
- **Application Received (Borrower)**: Sent to the borrower when they submit a loan application, informing them it was received
- **Application Underwriting**: Sent to borrowers and guarantors when an application is moved into the underwriting stage
- **Loan Approved**: Sent to borrowers and guarantors when an application is moved into the approved stage
- **Loan Denied**: Sent to borrowers and guarantors when their loan application is denied by the lender
- **Loan Funded**: Sent to borrowers and guarantors when funding is released on the loan by the lender
- **Loan Processing**: Sent to borrowers and guarantors when an application is moved into the Processing stage
- **Request Application (Borrower)**: Sent to the selected contact when the lender requests a loan application to be completed
- **Request Application Changes (Borrower)**: Sent to the selected contact when the lender requests changes to a loan application

**7. Payments Category**
- **Payment Due**: Sent to borrowers and guarantors when their next payment is due at the interval selected by the lender in general settings
- **Payment Failed**: Let the borrower know that their payment failed
- **Payment Initiated (Borrower)**: Let the borrower know that their payments have been successfully initiated
- **Payment Initiated (Lender)**: Let the lender know that a borrower has successfully initiated payments
- **Payment Returned**: Sent to the loan owners when a payment is returned via integrated ACH
- **Payment Warning**: Sent to the loan owners when a payment was collected, but the bank issued a warning about the payment collection

**8. Statements Category**
- **Borrower Statement**: Sent to borrowers and guarantors on the due date of their regular payment

**Notification Item Structure**
Each notification type includes:
- **Notification Name**: Title/name of the notification
- **Description**: Text explaining when the notification is sent and to whom
- **Toggle Control**: Combobox/dropdown labeled "Email & Notification"
  - Likely options: Email only, Notification only, Both, Neither/Disabled
  - Allows configuring delivery method for each notification type

**Notification Configuration Features**
- **Per-Notification Control**: Each notification type can be configured independently
- **Delivery Method Selection**: Choose between email, in-app notification, or both
- **Category Organization**: Notifications grouped by functional area
- **Descriptive Text**: Each notification includes description of when it's triggered
- **Recipient Information**: Descriptions specify who receives each notification

**Notification Recipients** (From Descriptions)
- **Borrowers and Guarantors**: Most loan status and payment notifications
- **Account Owners**: Loan-level notifications
- **Lender Account Admins**: Administrative and sharing notifications
- **Contacts**: Document and application-related notifications
- **Signers**: E-signature workflow notifications
- **Tagged Users**: Comment notifications

**Component Structure** (Inferred)
```
<NotificationsTab loanId={numericId}>
  <NotificationsHeader>
    <NotificationsTitle>Notifications</NotificationsTitle>
  </NotificationsHeader>
  <NotificationCategories>
    <NotificationCategory name="Budgets">
      <NotificationItem
        name="Budget Approved"
        description="Sent to borrowers and guarantors when a budget is approved by the lender."
        deliveryMethod={deliveryMethod}
        onChange={updateDeliveryMethod}
      />
      <NotificationItem name="Budget Rejected" ... />
      <NotificationItem name="Budget Submitted" ... />
    </NotificationCategory>
    <NotificationCategory name="Documents">
      <NotificationItem name="Document Rejected" ... />
      <NotificationItem name="Document Requested" ... />
      <NotificationItem name="Document Shared" ... />
      <NotificationItem name="Document Uploaded" ... />
    </NotificationCategory>
    <NotificationCategory name="Draw Requests">
      <NotificationItem name="Draw Approved" ... />
      <NotificationItem name="Draw Rejected" ... />
      <NotificationItem name="Draw Released" ... />
      <NotificationItem name="Draw Rollback" ... />
      <NotificationItem name="Draw Submitted" ... />
    </NotificationCategory>
    <NotificationCategory name="E-signature">
      <NotificationItem name="Document was Recalled" ... />
      <NotificationItem name="Signing Complete (Owners)" ... />
      <NotificationItem name="Signing Complete (Signers)" ... />
      <NotificationItem name="Signing was Declined" ... />
      <NotificationItem name="Thanks for Signing" ... />
      <NotificationItem name="Time to Sign" ... />
    </NotificationCategory>
    <NotificationCategory name="General">
      <NotificationItem name="Loan Share Accepted" ... />
      <NotificationItem name="Loan Share Rejected" ... />
      <NotificationItem name="Loan Shared" ... />
      <NotificationItem name="New Comment" ... />
    </NotificationCategory>
    <NotificationCategory name="Origination">
      <NotificationItem name="Application Received (Admin)" ... />
      <NotificationItem name="Application Received (Borrower)" ... />
      <NotificationItem name="Application Underwriting" ... />
      <NotificationItem name="Loan Approved" ... />
      <NotificationItem name="Loan Denied" ... />
      <NotificationItem name="Loan Funded" ... />
      <NotificationItem name="Loan Processing" ... />
      <NotificationItem name="Request Application (Borrower)" ... />
      <NotificationItem name="Request Application Changes (Borrower)" ... />
    </NotificationCategory>
    <NotificationCategory name="Payments">
      <NotificationItem name="Payment Due" ... />
      <NotificationItem name="Payment Failed" ... />
      <NotificationItem name="Payment Initiated (Borrower)" ... />
      <NotificationItem name="Payment Initiated (Lender)" ... />
      <NotificationItem name="Payment Returned" ... />
      <NotificationItem name="Payment Warning" ... />
    </NotificationCategory>
    <NotificationCategory name="Statements">
      <NotificationItem name="Borrower Statement" ... />
    </NotificationCategory>
  </NotificationCategories>
</NotificationsTab>
```

#### **Settings Tab Structure** (Observed)

**URL Structure**
- **Pattern**: `/admin/loans/{loanId}/settings`
- **Subtab Route**: Extends loan detail route with `/settings` path
- **Access**: Accessed from ellipses/More menu
- **Purpose**: Loan-level configuration and settings page

**Page Header**
- **Heading**: "Loan Settings" (H4)
- **Configuration Sections**: Multiple editable sections for loan settings

**Loan Settings Section**
- **Heading**: "Loan Settings" (H4)
- **Edit Button**: Allows editing loan settings
- **Fields Displayed**:
  - **Interest Accrual Method**: "Regular Period" (calculation method)
  - **Negative Amortization**: "Unpaid Interest" (handling method)
  - **Unpaid Interest**: "Unpaid Interest" (display/calculation)
  - **Unpaid Interest Handling**: "Include When Calculating Interest" (calculation behavior)
  - **Calculate Daily Rate Using**: "-" (empty/not set)
  - **Calculate Days Between Dates Using**: "Actual Number Of Days" (day count method)

**Late Charges Section**
- **Heading**: "Late Charges" (H4)
- **Edit Button**: Allows editing late charge settings
- **Fields Displayed**:
  - **Late Charge Method**: "-" (empty/not set)
  - **Number Of Grace Days**: "10 days" (numeric with unit)
  - **Grace Days Method**: "Calendar Days" (calculation method)
  - **Minimum Late Charge**: "-" (empty/not set)
  - **Percentage Of P&I**: "-" (empty/not set, percentage of Principal & Interest)
  - **Additional Daily Amount**: "-" (empty/not set)

**Prepayment Penalty Section**
- **Heading**: "Prepayment Penalty" (H4)
- **Edit Button**: Allows editing prepayment penalty settings
- **Fields Displayed**:
  - **Prepayment type**: "-" (empty/not set)
  - **Penalty Expiration**: "-" (empty/not set)

**Default Interest Section**
- **Heading**: "Default Interest" (H4)
- **Edit Button**: Allows editing default interest settings
- **Fields Displayed**:
  - **Default After**: "-" (empty/not set, likely days or date)
  - **Default Days Method**: "Calendar Days" (calculation method)
  - **Effective Until**: "-" (empty/not set, date)
  - **Default Rate Method**: "-" (empty/not set)
  - **Default Rate**: "-" (empty/not set, percentage)
  - **Distribute to Investors**: "No" (boolean)
  - **Start of Default**: "Default Date" (trigger point)

**Lender of Record Section**
- **Heading**: "Lender of Record" (H4)
- **Edit Button**: Allows editing lender information
- **Fields Displayed**:
  - **Name**: "USDV Capital, Inc." (lender entity name)
  - **Jurisdiction**: "United States" (legal jurisdiction)
  - **Type of corporation**: "Corporation" (entity type)
  - **Address**: "-" (empty/not set)

**Payment Collection Section**
- **Heading**: "Payment Collection" (H4, visible at bottom)
- **Content**: Section visible but fields not fully displayed in current view
- **Likely Contains**: Payment collection method, payment processing settings, ACH settings, etc.

**Section Patterns** (Observed)
- **Editable Sections**: All sections have "Edit" buttons for configuration
- **Empty State Handling**: Fields show "-" when empty/not set
- **Formatted Values**: Numeric values with units (e.g., "10 days"), text values, boolean values ("No")
- **Section Organization**: Logical grouping of related loan configuration settings

**Settings Categories**
1. **Interest/Loan Calculation**: Interest accrual, negative amortization, unpaid interest handling
2. **Late Charges**: Grace periods, late charge calculation methods
3. **Prepayment**: Prepayment penalty configuration
4. **Default Interest**: Default rate and timing configuration
5. **Lender Information**: Lender of record details
6. **Payment Collection**: Payment processing configuration

**Configuration Features** (Inferred)
- **Edit Mode**: Edit buttons enable editing configuration
- **Validation**: Settings likely validated when saved
- **Calculation Impact**: Settings affect loan calculations (interest, payments, late charges)
- **Compliance**: Lender information important for compliance/legal purposes

**Component Structure** (Inferred)
```
<SettingsTab loanId={numericId}>
  <SettingsHeader>
    <SettingsTitle>Loan Settings</SettingsTitle>
  </SettingsHeader>
  <LoanSettingsSection editable>
    <SectionTitle>Loan Settings</SectionTitle>
    <EditButton onClick={openEditModal} />
    <Field label="Interest Accrual Method" value={interestAccrualMethod} />
    <Field label="Negative Amortization" value={negativeAmortization} />
    <Field label="Unpaid Interest" value={unpaidInterest} />
    <Field label="Unpaid Interest Handling" value={unpaidInterestHandling} />
    <Field label="Calculate Daily Rate Using" value={dailyRateMethod} />
    <Field label="Calculate Days Between Dates Using" value={dayCountMethod} />
  </LoanSettingsSection>
  <LateChargesSection editable>
    <SectionTitle>Late Charges</SectionTitle>
    <EditButton onClick={openEditModal} />
    <Field label="Late Charge Method" value={lateChargeMethod} />
    <Field label="Number Of Grace Days" value={graceDays} />
    <Field label="Grace Days Method" value={graceDaysMethod} />
    <Field label="Minimum Late Charge" value={minimumLateCharge} />
    <Field label="Percentage Of P&I" value={percentageOfPAndI} />
    <Field label="Additional Daily Amount" value={additionalDailyAmount} />
  </LateChargesSection>
  <PrepaymentPenaltySection editable>
    <SectionTitle>Prepayment Penalty</SectionTitle>
    <EditButton onClick={openEditModal} />
    <Field label="Prepayment type" value={prepaymentType} />
    <Field label="Penalty Expiration" value={penaltyExpiration} />
  </PrepaymentPenaltySection>
  <DefaultInterestSection editable>
    <SectionTitle>Default Interest</SectionTitle>
    <EditButton onClick={openEditModal} />
    <Field label="Default After" value={defaultAfter} />
    <Field label="Default Days Method" value={defaultDaysMethod} />
    <Field label="Effective Until" value={effectiveUntil} />
    <Field label="Default Rate Method" value={defaultRateMethod} />
    <Field label="Default Rate" value={defaultRate} />
    <Field label="Distribute to Investors" value={distributeToInvestors} boolean />
    <Field label="Start of Default" value={startOfDefault} />
  </DefaultInterestSection>
  <LenderOfRecordSection editable>
    <SectionTitle>Lender of Record</SectionTitle>
    <EditButton onClick={openEditModal} />
    <Field label="Name" value={lenderName} />
    <Field label="Jurisdiction" value={jurisdiction} />
    <Field label="Type of corporation" value={corporationType} />
    <Field label="Address" value={address} />
  </LenderOfRecordSection>
  <PaymentCollectionSection editable>
    <SectionTitle>Payment Collection</SectionTitle>
    <EditButton onClick={openEditModal} />
    <PaymentCollectionFields />
  </PaymentCollectionSection>
</SettingsTab>
```

#### **Loans/Servicing Section Structure** (Observed)

**URL Structure**
- **Pattern**: `/admin/servicing`
- **Page Title**: "Loans"
- **Navigation Label**: "Loans" (in sidebar navigation)
- **Purpose**: Active loans servicing view (loans that have moved past pipeline stage)
- **Note**: This section appears somewhat redundant with Pipeline section, as both allow adding loans to pipeline

**Page Header**
- **Heading**: "Loans" (H1)
- **View Toggle Buttons**:
  - **"Active" Button**: Toggle for active loans view (default state)
  - **"Settled" Button**: Toggle for settled/completed loans view
- **Filter Button**: Opens filter options/dropdown
- **Search Box**: Search input with placeholder "Search"
  - Allows searching loans by various criteria
- **Export Button**: Action button labeled "Export"
  - Exports loan data (likely to CSV/Excel/PDF)
- **Add Loan Button**: Primary action button labeled "Add Loan"
  - Opens modal/dialog for adding new loan
  - Modal allows adding loan directly to pipeline (creates loan entry)

**Loans Table Structure**
Table displaying active/servicing loans with the following columns:

1. **Name Column**:
   - Property address or loan identifier
   - Example: "123 Main Street"
   - Clickable link (likely navigates to loan detail page)

2. **Origination Date Column**:
   - Date loan was originated
   - Shows "-" when not set

3. **Borrower Column**:
   - Borrower name/entity
   - Example: "Test Company"

4. **Principal Balance Column**:
   - Current principal balance amount
   - Formatted as currency (e.g., "$0")

5. **Maturity Date Column**:
   - Loan maturity/end date
   - Shows "-" when not set

6. **Owner Column**:
   - Loan owner/assigned user
   - Displayed as initials (e.g., "TB")
   - Tooltip shows full name on hover

7. **Status Column**:
   - Loan servicing status
   - Example: "Performing" (indicates loan is performing as expected)
   - Status badges likely used for visual indication

**Loan Data Observed**
- **Loan Example**: "123 Main Street - Test Company"
  - Name: "123 Main Street"
  - Origination Date: "-" (not set)
  - Borrower: "Test Company"
  - Principal Balance: "$0"
  - Maturity Date: "-" (not set)
  - Owner: "TB" (with tooltip)
  - Status: "Performing"

**Display/Pagination**
- **Display**: "Showing 1 of 1" (single loan visible in current view)
- **Pagination**: Likely supports pagination for larger datasets

**Add Loan Modal** (Observed)
When "Add Loan" button is clicked, a multi-step modal appears:

**Modal Structure**:
- **Progress Indicator**: "Step 1 of 3" (indicates multi-step form)
- **Modal Title**: "Add New Loan"

**Step 1 Fields** (Observed):
1. **Loan Name Field**:
   - Text input labeled "Loan Name"
   - Required field (shows "The field is required" validation)
   - Free-text input for loan identifier/name

2. **Product Field**:
   - Dropdown/combobox labeled "Product"
   - Example value: "Accolend Fix & Flip"
   - Allows selecting loan product type

3. **Borrower(s) Field**:
   - Dropdown/combobox labeled "Borrower(s)"
   - Default: "Select..."
   - "Create a new borrower" option available
   - Allows selecting existing borrower or creating new one
   - Supports multiple borrower selection

4. **Guarantor(s) Field**:
   - Dropdown/combobox labeled "Guarantor(s)"
   - Default: "Select..."
   - "Create a new guarantor" option available
   - Allows selecting existing guarantor or creating new one
   - Supports multiple guarantor selection

5. **Loan Owners Field**:
   - Field labeled "Loan Owners"
   - Tooltip available for additional information
   - Likely multi-select dropdown or similar input

**Modal Actions**:
- **Cancel Button**: Closes modal without saving
- **Next Button**: Advances to next step (Step 2 of 3)

**Step 2 and Step 3**: Not visible in current view (user needs to progress through modal)

**Relationship to Pipeline**
- **Similar Functionality**: Both Loans/Servicing section and Pipeline section allow adding loans
- **Redundancy**: User observation that this seems redundant, as Pipeline already provides similar "Add Loan" functionality
- **Potential Purpose**: Loans/Servicing section may be intended for loans that have moved past the pipeline stage (active/servicing loans), while Pipeline is for loans in origination/processing stages
- **Workflow**: Adding loan from either section likely adds it to pipeline for processing

**Status Categories**
- **Active**: Loans currently in servicing (default view)
- **Settled**: Loans that have been paid off/completed
- **Performing**: Loan status indicating normal payment performance

**Component Structure** (Inferred)
```
<ServicingPage>
  <PageHeader>
    <PageTitle>Loans</PageTitle>
    <ViewToggle>
      <ToggleButton active>Active</ToggleButton>
      <ToggleButton>Settled</ToggleButton>
    </ViewToggle>
    <FilterButton onClick={openFilter} />
    <SearchBox placeholder="Search" onChange={handleSearch} />
    <ExportButton onClick={exportLoans} />
    <AddLoanButton onClick={openAddLoanModal} />
  </PageHeader>
  <LoansTable>
    <TableHeader>
      <ColumnHeader>Name</ColumnHeader>
      <ColumnHeader>Origination Date</ColumnHeader>
      <ColumnHeader>Borrower</ColumnHeader>
      <ColumnHeader>Principal Balance</ColumnHeader>
      <ColumnHeader>Maturity Date</ColumnHeader>
      <ColumnHeader>Owner</ColumnHeader>
      <ColumnHeader>Status</ColumnHeader>
    </TableHeader>
    {loans.map(loan => (
      <LoanRow
        name={loan.name}
        originationDate={loan.originationDate}
        borrower={loan.borrower}
        principalBalance={loan.principalBalance}
        maturityDate={loan.maturityDate}
        owner={loan.owner}
        status={loan.status}
        onClick={navigateToLoanDetail}
      />
    ))}
  </LoansTable>
  <DisplayCount>Showing {visibleCount} of {totalCount}</DisplayCount>
</ServicingPage>

<AddLoanModal isOpen={isModalOpen} onClose={closeModal}>
  <ModalHeader>
    <ProgressIndicator>Step {currentStep} of {totalSteps}</ProgressIndicator>
    <ModalTitle>Add New Loan</ModalTitle>
  </ModalHeader>
  <ModalContent>
    {currentStep === 1 && (
      <Step1Form>
        <TextField
          label="Loan Name"
          value={loanName}
          onChange={setLoanName}
          required
          error={errors.loanName}
        />
        <ProductCombobox
          label="Product"
          value={selectedProduct}
          onChange={setSelectedProduct}
          options={products}
        />
        <BorrowerCombobox
          label="Borrower(s)"
          value={selectedBorrowers}
          onChange={setSelectedBorrowers}
          options={borrowers}
          onCreateNew={createNewBorrower}
          multiple
        />
        <GuarantorCombobox
          label="Guarantor(s)"
          value={selectedGuarantors}
          onChange={setSelectedGuarantors}
          options={guarantors}
          onCreateNew={createNewGuarantor}
          multiple
        />
        <LoanOwnersField
          label="Loan Owners"
          value={selectedOwners}
          onChange={setSelectedOwners}
          tooltip={loanOwnersTooltip}
        />
      </Step1Form>
    )}
    {currentStep === 2 && <Step2Form />}
    {currentStep === 3 && <Step3Form />}
  </ModalContent>
  <ModalFooter>
    <CancelButton onClick={closeModal}>Cancel</CancelButton>
    <NextButton onClick={nextStep} disabled={!isStepValid}>
      Next
    </NextButton>
  </ModalFooter>
</AddLoanModal>
```

#### **Payments Section Structure** (Observed)

**URL Structure**
- **Pattern**: `/admin/payments/due`
- **Page Title**: "Payments"
- **Navigation Label**: "Payments" (in sidebar navigation)
- **Sub-route**: `/due` indicates sub-sections (likely includes `/processed`, `/overdue`, etc.)
- **Purpose**: Payment management and collection interface for borrower payments
- **Note**: User observation that this section appears redundant as payment functionality is covered in other parts of the app (likely in loan detail pages)

**Page Header**
- **Heading**: "Payments" (H1)
- **View Toggle/Status Indicators**: "Due Processed" text visible (likely tabs or toggle buttons for filtering payment status)
  - **Due**: Payments that are due/outstanding
  - **Processed**: Payments that have been processed/completed

**Page Content**
- **Empty/Initial State Message**:
  - **Heading**: "Your scheduled payments from borrowers go here" (H4)
  - **Description**: "Manage, collect and record payments from all your borrowers in one place."
  - **Purpose**: Empty state messaging explaining the section's purpose
  - **Indicates**: This section aggregates payments across all loans/borrowers

**Payment Management Features** (Inferred from Description)
- **Payment Aggregation**: View all borrower payments in one place
- **Payment Management**: Manage payment schedules, statuses, and records
- **Payment Collection**: Interface for recording and tracking payment collections
- **Cross-Loan View**: Payments from all loans consolidated in single view

**Relationship to Other Sections**
- **Loan Detail Pages**: Payments are likely managed at the individual loan level (e.g., in loan detail page Payments tab from ellipses menu)
- **Redundancy**: User observation that this standalone Payments section may be redundant since payment functionality exists elsewhere in the app
- **Potential Value**: May provide aggregate/portfolio-level payment views that aren't available in individual loan contexts

**Sub-routes/Sections** (Inferred from URL Pattern)
- `/admin/payments/due` - Payments that are due/outstanding (current view)
- `/admin/payments/processed` - Likely route for processed payments (inferred from "Due Processed" toggle)
- Additional sub-routes may exist for different payment views/filters

**Component Structure** (Inferred)
```
<PaymentsPage>
  <PageHeader>
    <PageTitle>Payments</PageTitle>
    <PaymentViewTabs>
      <Tab active>Due</Tab>
      <Tab>Processed</Tab>
    </PaymentViewTabs>
  </PageHeader>
  <PaymentContent>
    {hasPayments ? (
      <PaymentsTable>
        <TableHeader>
          {/* Payment table columns inferred */}
          <ColumnHeader>Loan</ColumnHeader>
          <ColumnHeader>Borrower</ColumnHeader>
          <ColumnHeader>Due Date</ColumnHeader>
          <ColumnHeader>Amount</ColumnHeader>
          <ColumnHeader>Status</ColumnHeader>
          <ColumnHeader>Actions</ColumnHeader>
        </TableHeader>
        {payments.map(payment => (
          <PaymentRow payment={payment} />
        ))}
      </PaymentsTable>
    ) : (
      <EmptyState>
        <EmptyStateHeading>Your scheduled payments from borrowers go here</EmptyStateHeading>
        <EmptyStateDescription>
          Manage, collect and record payments from all your borrowers in one place.
        </EmptyStateDescription>
      </EmptyState>
    )}
  </PaymentContent>
</PaymentsPage>
```

#### **Payouts Section Structure** (Observed)

**URL Structure**
- **Pattern**: `/admin/payouts/ready`
- **Page Title**: "Payouts"
- **Navigation Label**: "Payouts" (in sidebar navigation)
- **Sub-route**: `/ready` indicates sub-sections (likely includes `/pending`, `/completed`, etc.)
- **Purpose**: Payout management interface for investor payouts
- **Note**: User observation that this section appears redundant as payout functionality is covered in other parts of the app (likely in Funding tabs within loan detail pages)

**Page Header**
- **Heading**: "Payouts" (H1)
- **View Toggle/Status Indicators**: Likely includes tabs or toggle buttons for filtering payout status (e.g., Ready, Pending, Completed)
  - **Ready**: Payouts that are ready to be processed
  - Other status filters likely exist (inferred from sub-route pattern)

**Page Content**
- **Empty/Initial State Message**:
  - **Heading**: "All your payouts in one place" (H4)
  - **Description**: "This is where you'll see a detailed view of all your past and scheduled payouts to investors."
  - **Purpose**: Empty state messaging explaining the section's purpose
  - **Indicates**: This section aggregates investor payouts across all loans/investments

**Payout Management Features** (Inferred from Description)
- **Payout Aggregation**: View all investor payouts in one place
- **Historical View**: See past payouts that have been completed
- **Scheduled View**: See scheduled/future payouts to investors
- **Detailed View**: Comprehensive payout information and tracking
- **Cross-Loan View**: Payouts from all loans/investments consolidated in single view

**Relationship to Other Sections**
- **Loan Detail Pages - Funding Tab**: Payouts are likely managed at the individual loan level within the Funding tab (e.g., investor funding, payout history)
- **Investor Management**: Payouts may also be referenced in investor-related sections
- **Redundancy**: User observation that this standalone Payouts section may be redundant since payout functionality exists elsewhere in the app
- **Potential Value**: May provide aggregate/portfolio-level payout views that aren't available in individual loan contexts

**Sub-routes/Sections** (Inferred from URL Pattern)
- `/admin/payouts/ready` - Payouts that are ready to be processed (current view)
- `/admin/payouts/pending` - Likely route for pending payouts
- `/admin/payouts/completed` - Likely route for completed/past payouts
- Additional sub-routes may exist for different payout views/filters

**Payout Context**
- **Investor Focus**: Payouts are directed to investors
- **Loan Relationship**: Payouts are tied to loans (likely related to loan payments received from borrowers)
- **Cash Flow Distribution**: Manages distribution of loan proceeds/payments to investors

**Component Structure** (Inferred)
```
<PayoutsPage>
  <PageHeader>
    <PageTitle>Payouts</PageTitle>
    <PayoutViewTabs>
      <Tab active>Ready</Tab>
      <Tab>Pending</Tab>
      <Tab>Completed</Tab>
    </PayoutViewTabs>
  </PageHeader>
  <PayoutContent>
    {hasPayouts ? (
      <PayoutsTable>
        <TableHeader>
          {/* Payout table columns inferred */}
          <ColumnHeader>Loan</ColumnHeader>
          <ColumnHeader>Investor</ColumnHeader>
          <ColumnHeader>Amount</ColumnHeader>
          <ColumnHeader>Due Date</ColumnHeader>
          <ColumnHeader>Status</ColumnHeader>
          <ColumnHeader>Actions</ColumnHeader>
        </TableHeader>
        {payouts.map(payout => (
          <PayoutRow payout={payout} />
        ))}
      </PayoutsTable>
    ) : (
      <EmptyState>
        <EmptyStateHeading>All your payouts in one place</EmptyStateHeading>
        <EmptyStateDescription>
          This is where you'll see a detailed view of all your past and scheduled payouts to investors.
        </EmptyStateDescription>
      </EmptyState>
    )}
  </PayoutContent>
</PayoutsPage>
```

#### **Reports Section Structure** (Observed)

**URL Structure**
- **Pattern**: `/admin/reports`
- **Page Title**: "Reports"
- **Navigation Label**: "Reports" (in sidebar navigation)
- **Purpose**: Centralized reporting hub providing various report types and custom report functionality

**Page Header**
- **Heading**: "Reports" (H1)

**Report Categories/Sections**
The Reports page is organized into multiple report categories, each with a heading (H4) and description paragraph. Each report section likely links to a detailed report view or generation interface:

**1. Payment History**
- **Heading**: "Payment History" (H4)
- **Description**: "All payments performed across all loans."
- **Purpose**: Comprehensive payment reporting across portfolio

**2. Archived Loans**
- **Heading**: "Archived Loans" (H4)
- **Description**: "A summary of all archived loans. From these report you will be able to restore or access the details."
- **Features**: Summary report with ability to restore or access archived loan details
- **Purpose**: Track and manage archived loans

**3. Sold Loans**
- **Heading**: "Sold Loans" (H4)
- **Description**: "A summary of all sold loans. From these report you will be able to restore or access the details."
- **Features**: Summary report with ability to restore or access sold loan details
- **Purpose**: Track loans that have been sold

**4. Investor Transactions**
- **Heading**: "Investor Transactions" (H4)
- **Description**: "A general report with all the transactions made to all investors"
- **Purpose**: Comprehensive investor transaction reporting

**5. Liquidated Loans**
- **Heading**: "Liquidated Loans" (H4)
- **Description**: "A summary of all loans that have been liquidated."
- **Purpose**: Track loans that have been liquidated

**6. Sent to Servicing**
- **Heading**: "Sent to Servicing" (H4)
- **Description**: "A summary of all loans that have been transferred to servicing. From these report you will be able to restore or access the details."
- **Features**: Summary report with ability to restore or access servicing loan details
- **Purpose**: Track loans transferred to servicing

**7. Insurance**
- **Heading**: "Insurance" (H4)
- **Description**: "A list of all insurance on loans in servicing."
- **Purpose**: Insurance tracking for servicing loans

**8. Trust Balance**
- **Heading**: "Trust Balance" (H4)
- **Description**: "A list of all loans with a trust balance."
- **Purpose**: Track loans with trust account balances

**9. Trust Transactions**
- **Heading**: "Trust Transactions" (H4)
- **Description**: "All the movement of funds within a loan."
- **Purpose**: Track all trust account fund movements

**10. 1098 Tax Report**
- **Heading**: "1098 Tax Report" (H4)
- **Description**: "Borrower report of all interest paid in the tax year."
- **Purpose**: Tax reporting for borrowers (IRS Form 1098)

**11. 1099 Tax Report**
- **Heading**: "1099 Tax Report" (H4)
- **Description**: "Investor report of all interest paid in the tax year."
- **Purpose**: Tax reporting for investors (IRS Form 1099)

**12. Loan Tape**
- **Heading**: "Loan Tape" (H4)
- **Description**: "A list of all loans and their fields."
- **Purpose**: Comprehensive loan data export/report (common in loan servicing/securitization)

**13. Draw Requests**
- **Heading**: "Draw Requests" (H4)
- **Description**: "A list of all draw requests on all loans."
- **Purpose**: Track all draw requests across portfolio (construction/rehab loans)

**14. Paid Charges**
- **Heading**: "Paid Charges" (H4)
- **Description**: "A list of all paid charges on all loans."
- **Purpose**: Track all paid loan charges/fees

**15. Unpaid Charges**
- **Heading**: "Unpaid Charges" (H4)
- **Description**: "A list of all unpaid charges on all loans."
- **Purpose**: Track outstanding/unpaid loan charges/fees

**16. Unpaid Interest**
- **Heading**: "Unpaid Interest" (H4)
- **Description**: "A list of all unpaid interests on all loans."
- **Purpose**: Track outstanding/unpaid interest amounts

**17. Loan Valuations**
- **Heading**: "Loan Valuations" (H4)
- **Description**: "A list of valuations on collateral for all loans."
- **Purpose**: Track all property valuations/appraisals across portfolio

**18. Custom Reports**
- **Heading**: "Custom Reports" (H4)
- **Create Button**: "Create Custom Report" button
  - Allows users to create custom reports
  - Opens custom report builder/configuration interface

**Custom Reports Table**
- **Table Structure**:
  - **Name Column**: Custom report name (e.g., "Data Checker")
  - **Description Column**: Report description (can be empty)
  - **Created Column**: Creation date (format: "MMM D, YYYY", e.g., "Dec 5, 2025")
  - **Actions Column**: Likely contains action buttons (Edit, Delete, Run, etc.)

**Custom Report Example**
- **Name**: "Data Checker"
- **Description**: Empty/not provided
- **Created**: "Dec 5, 2025"
- **Display**: "Showing 1 of 1" (one custom report visible)

**Report Organization Pattern**
- **Card/Section Layout**: Each report type displayed as a section with heading and description
- **Clickable Sections**: Likely clickable to access/generate specific reports
- **Custom Reports Section**: Separate section at bottom with table view and creation capability
- **Comprehensive Coverage**: Covers all major aspects of loan management (payments, loans, investors, charges, taxes, insurance, trust, draws, valuations)

**Report Categories Summary**
1. **Loan Status Reports**: Archived, Sold, Liquidated, Sent to Servicing
2. **Financial Reports**: Payment History, Trust Balance, Trust Transactions
3. **Tax Reports**: 1098 (Borrower), 1099 (Investor)
4. **Investor Reports**: Investor Transactions, 1099 Tax Report
5. **Charge Reports**: Paid Charges, Unpaid Charges, Unpaid Interest
6. **Loan Data Reports**: Loan Tape, Loan Valuations
7. **Operational Reports**: Draw Requests, Insurance
8. **Custom Reports**: User-defined custom reports

**Component Structure** (Inferred)
```
<ReportsPage>
  <PageHeader>
    <PageTitle>Reports</PageTitle>
  </PageHeader>
  <ReportSections>
    <ReportSection
      title="Payment History"
      description="All payments performed across all loans."
      onClick={navigateToPaymentHistoryReport}
    />
    <ReportSection
      title="Archived Loans"
      description="A summary of all archived loans. From these report you will be able to restore or access the details."
      onClick={navigateToArchivedLoansReport}
      features={['restore', 'accessDetails']}
    />
    <ReportSection
      title="Sold Loans"
      description="A summary of all sold loans. From these report you will be able to restore or access the details."
      onClick={navigateToSoldLoansReport}
      features={['restore', 'accessDetails']}
    />
    <ReportSection
      title="Investor Transactions"
      description="A general report with all the transactions made to all investors"
      onClick={navigateToInvestorTransactionsReport}
    />
    <ReportSection
      title="Liquidated Loans"
      description="A summary of all loans that have been liquidated."
      onClick={navigateToLiquidatedLoansReport}
    />
    <ReportSection
      title="Sent to Servicing"
      description="A summary of all loans that have been transferred to servicing. From these report you will be able to restore or access the details."
      onClick={navigateToServicingLoansReport}
      features={['restore', 'accessDetails']}
    />
    <ReportSection
      title="Insurance"
      description="A list of all insurance on loans in servicing."
      onClick={navigateToInsuranceReport}
    />
    <ReportSection
      title="Trust Balance"
      description="A list of all loans with a trust balance."
      onClick={navigateToTrustBalanceReport}
    />
    <ReportSection
      title="Trust Transactions"
      description="All the movement of funds within a loan."
      onClick={navigateToTrustTransactionsReport}
    />
    <ReportSection
      title="1098 Tax Report"
      description="Borrower report of all interest paid in the tax year."
      onClick={navigateTo1098Report}
    />
    <ReportSection
      title="1099 Tax Report"
      description="Investor report of all interest paid in the tax year."
      onClick={navigateTo1099Report}
    />
    <ReportSection
      title="Loan Tape"
      description="A list of all loans and their fields."
      onClick={navigateToLoanTapeReport}
    />
    <ReportSection
      title="Draw Requests"
      description="A list of all draw requests on all loans."
      onClick={navigateToDrawRequestsReport}
    />
    <ReportSection
      title="Paid Charges"
      description="A list of all paid charges on all loans."
      onClick={navigateToPaidChargesReport}
    />
    <ReportSection
      title="Unpaid Charges"
      description="A list of all unpaid charges on all loans."
      onClick={navigateToUnpaidChargesReport}
    />
    <ReportSection
      title="Unpaid Interest"
      description="A list of all unpaid interests on all loans."
      onClick={navigateToUnpaidInterestReport}
    />
    <ReportSection
      title="Loan Valuations"
      description="A list of valuations on collateral for all loans."
      onClick={navigateToLoanValuationsReport}
    />
  </ReportSections>
  <CustomReportsSection>
    <CustomReportsHeader>
      <CustomReportsTitle>Custom Reports</CustomReportsTitle>
      <CreateCustomReportButton onClick={openCustomReportBuilder}>
        Create Custom Report
      </CreateCustomReportButton>
    </CustomReportsHeader>
    <CustomReportsTable>
      <TableHeader>
        <ColumnHeader>Name</ColumnHeader>
        <ColumnHeader>Description</ColumnHeader>
        <ColumnHeader>Created</ColumnHeader>
        <ColumnHeader>Actions</ColumnHeader>
      </TableHeader>
      {customReports.map(report => (
        <CustomReportRow
          name={report.name}
          description={report.description}
          created={report.created}
          onRun={runReport}
          onEdit={editReport}
          onDelete={deleteReport}
        />
      ))}
    </CustomReportsTable>
    <DisplayCount>Showing {visibleCount} of {totalCount}</DisplayCount>
  </CustomReportsSection>
</ReportsPage>
```

#### **Funds Section Structure** (Observed)

**URL Structure**
- **Pattern**: `/admin/funds`
- **Page Title**: "Funds"
- **Navigation Label**: "Funds" (in sidebar navigation)
- **Purpose**: Investment fund management interface for managing funds, portfolios, and investors

**Page Header**
- **Heading**: "Funds" (H1)
- **Add Fund Button**: Primary action button labeled "Add Fund"
  - Opens modal/dialog for creating new fund
  - Allows adding new investment fund entities

**Fund Cards/List**
The Funds page displays fund cards (or list items) showing fund information. Each fund card displays:

**Fund Card Structure**:
- **Fund Name/Heading**: Fund name displayed as heading (H4)
  - Example: "USDV CAPITAL HOLDINGS"
- **Fund Metrics** (displayed as text/statistics):
  - **Balance**: Fund balance amount (currency formatted, e.g., "$0")
  - **Portfolio**: Number of investments (e.g., "0 investments")
  - **Investors**: Number of investors (e.g., "0 investors")

**Fund Data Observed**
- **Fund Example**: "USDV CAPITAL HOLDINGS"
  - Balance: "$0"
  - Portfolio: "0 investments"
  - Investors: "0 investors"

**Fund Management Features** (Inferred)
- **Fund Creation**: Add new funds via "Add Fund" button
- **Fund Overview**: View fund balance, portfolio size, and investor count
- **Fund Navigation**: Likely clickable fund cards that navigate to fund detail pages
- **Portfolio Tracking**: Track number of investments within each fund
- **Investor Management**: Track number of investors associated with each fund
- **Balance Tracking**: Track fund balance/available capital

**Fund Context**
- **Investment Fund Entity**: Funds are multi-investor fund entities that pool capital from multiple investors
- **Portfolio Management**: Funds contain portfolios of investments (likely loans)
- **Investor Relations**: Funds have associated investors who provide capital
- **Capital Management**: Track fund balance/available capital for investments
- **Note**: This section manages multi-investor funds, not funding of particular loans (which is handled in loan detail Funding tabs)

**Display Pattern**
- **Card/Grid Layout**: Funds displayed as cards (or list items) with key metrics
- **Summary Metrics**: Each card shows balance, portfolio size, and investor count
- **Minimal Data**: Current view shows single fund with zero balances/counts (likely new/empty fund)

**Component Structure** (Inferred)
```
<FundsPage>
  <PageHeader>
    <PageTitle>Funds</PageTitle>
    <AddFundButton onClick={openAddFundModal} />
  </PageHeader>
  <FundsGrid>
    {funds.map(fund => (
      <FundCard
        name={fund.name}
        balance={fund.balance}
        portfolioCount={fund.portfolioCount}
        investorCount={fund.investorCount}
        onClick={navigateToFundDetail}
      >
        <FundName>{fund.name}</FundName>
        <FundMetrics>
          <Metric label="Balance" value={fund.balance} format="currency" />
          <Metric label="Portfolio" value={fund.portfolioCount} unit="investments" />
          <Metric label="Investors" value={fund.investorCount} unit="investors" />
        </FundMetrics>
      </FundCard>
    ))}
  </FundsGrid>
</FundsPage>

<AddFundModal isOpen={isModalOpen} onClose={closeModal}>
  <ModalHeader>
    <ModalTitle>Add Fund</ModalTitle>
  </ModalHeader>
  <ModalContent>
    <FundForm
      onSubmit={createFund}
      fields={['name', 'description', 'initialBalance', ...]}
    />
  </ModalContent>
  <ModalFooter>
    <CancelButton onClick={closeModal}>Cancel</CancelButton>
    <CreateButton onClick={submitForm}>Create Fund</CreateButton>
  </ModalFooter>
</AddFundModal>
```

#### **Offerings Section Structure** (Observed)

**URL Structure**
- **Pattern**: `/admin/offerings`
- **Page Title**: "Offerings"
- **Navigation Label**: "Offerings" (in sidebar navigation)
- **Purpose**: Loan offering management interface for creating and managing investment opportunity offerings to investors
- **Note**: User observation that this section is not relevant for the INSPIRE app (likely specific to Baseline's investor offering/marketing features)

**Page Header**
- **Heading**: "Offerings" (H1)
- **Add Offering Button**: Primary action button labeled "Add Offering"
  - Opens modal/dialog for creating new loan offering

**Page Content**
- **Empty/Initial State Message**:
  - **Heading**: "Create a loan offering" (H4)
  - **Description**: "Create loan offerings to showcase investment opportunities to your investor audiences."
  - **Purpose**: Empty state messaging explaining the section's purpose
  - **Indicates**: This section is used to create marketing/investment opportunity presentations for investors

**Add Offering Modal** (Observed)
When "Add Offering" button is clicked, a modal appears for creating a new offering:

**Modal Structure**:
- **Modal Title**: "Add a New Offering"

**Modal Fields**:
1. **Offering Type Field**:
   - Dropdown/combobox labeled "Offering Type"
   - Default: "Select..."
   - Allows selecting type of offering (e.g., Public, Private, etc.)
   - Types not fully visible in current view

2. **Public Offering Name Field**:
   - Text input labeled "Public Offering Name"
   - Character limit indicator: "0/100 Characters Remaining"
   - Maximum length: 100 characters
   - Allows naming the public offering

**Modal Actions**:
- **Cancel Button**: Closes modal without saving
- **Save Button**: Saves and creates the new offering

**Offering Management Features** (Inferred)
- **Offering Creation**: Create loan offerings to present to investors
- **Investment Opportunity Marketing**: Showcase loan investment opportunities
- **Investor Audience Targeting**: Present offerings to investor audiences
- **Offering Types**: Support for different offering types (Public, Private, etc.)
- **Offering Configuration**: Configure offering details, name, type, etc.

**Offering Context**
- **Investment Marketing**: Offerings appear to be marketing/investment opportunity presentations
- **Loan Presentation**: Showcase specific loans or loan portfolios as investment opportunities
- **Investor Relations**: Used to present investment opportunities to potential or existing investors
- **Regulatory Compliance**: "Public Offering" terminology suggests potential securities/regulatory compliance features

**Display Pattern**
- **Empty State**: Landing page shows empty state with creation prompt
- **Creation Interface**: Modal-based creation interface
- **Likely List View**: After creation, likely displays list/grid of offerings (not visible in current empty state)

**Component Structure** (Inferred)
```
<OfferingsPage>
  <PageHeader>
    <PageTitle>Offerings</PageTitle>
    <AddOfferingButton onClick={openAddOfferingModal} />
  </PageHeader>
  <OfferingContent>
    {hasOfferings ? (
      <OfferingsList>
        {offerings.map(offering => (
          <OfferingCard offering={offering} onClick={navigateToOfferingDetail} />
        ))}
      </OfferingsList>
    ) : (
      <EmptyState>
        <EmptyStateHeading>Create a loan offering</EmptyStateHeading>
        <EmptyStateDescription>
          Create loan offerings to showcase investment opportunities to your investor audiences.
        </EmptyStateDescription>
      </EmptyState>
    )}
  </OfferingContent>
</OfferingsPage>

<AddOfferingModal isOpen={isModalOpen} onClose={closeModal}>
  <ModalHeader>
    <ModalTitle>Add a New Offering</ModalTitle>
  </ModalHeader>
  <ModalContent>
    <OfferingForm>
      <OfferingTypeCombobox
        label="Offering Type"
        value={selectedOfferingType}
        onChange={setSelectedOfferingType}
        options={offeringTypes}
        placeholder="Select..."
      />
      <PublicOfferingNameField
        label="Public Offering Name"
        value={offeringName}
        onChange={setOfferingName}
        maxLength={100}
        characterCount={offeringName.length}
      />
      <CharacterCount>0/100 Characters Remaining</CharacterCount>
      {/* Additional fields likely exist */}
    </OfferingForm>
  </ModalContent>
  <ModalFooter>
    <CancelButton onClick={closeModal}>Cancel</CancelButton>
    <SaveButton onClick={saveOffering} disabled={!isFormValid}>
      Save
    </SaveButton>
  </ModalFooter>
</AddOfferingModal>
```

**Component Structure** (Inferred)
```
<MailTab loanId={numericId}>

**URL Structure**
- **Pattern**: `/admin/loans/{loanId}/mail`
- **Subtab Route**: Extends loan detail route with `/mail` path
- **Access**: Main tab (visible in tab navigation, not in ellipses menu)
- **Purpose**: Loan-specific email/message communication view

**Page Header**
- **Select All Checkbox**: Checkbox button at top-left for bulk selection
- **Heading**: "All Mail" (H2)
- **Search Box**: Search input with placeholder "Search"
  - Allows searching emails/messages within loan context
  - Searches across subject, body, sender
- **Compose Button**: Primary action button labeled "Compose"
  - Opens email composition interface
  - Allows composing new email related to loan

**Mail Table Structure**
Table showing all emails/messages related to the loan with the following structure:

**Table Columns:**
1. **Checkbox Column**:
   - Checkbox for individual email selection
   - Enables bulk actions

2. **Sender Column**:
   - Sender name/entity
   - Examples: "USDV Capital Inc.", "Evan Shields"
   - System-generated emails from "USDV Capital Inc."
   - Manual emails from individual users (e.g., "Evan Shields")

3. **Subject/Preview Column**:
   - Email subject line followed by email body preview
   - Format: Subject + body text preview (truncated)
   - Examples:
     - "Your loan has been approvedYOUR LOAN HAS BEEN APPROVED We are pleased to inform you that your loan application has been appro"
     - "Download Ready for 4151 Sonoma BlvdDOWNLOAD READY FOR 4151 SONOMA BLVD Your download for loan 4151 Sonoma Blvd is ready. Click the"
     - "A document has been uploaded (Entity Status)ENTITY STATUS Rodrigo Fachini Tavares has uploaded a document. Summary: This document is a certi image.png"
   - Preview text shows email content
   - Image references visible in preview (e.g., "image.png")
   - Attachment information visible (e.g., "pg.2.pdf 620.11 kB")

4. **Date Column**:
   - Email date
   - Format: "MMM DD" (e.g., "Nov 7", "Oct 9", "Sep 26")
   - Abbreviated format (month and day only)

**Email Types Observed**
1. **Loan Approval Emails**:
   - Subject: "Your loan has been approved"
   - System-generated notification

2. **Download Ready Emails**:
   - Subject: "Download Ready for 4151 Sonoma Blvd"
   - Notifies when downloads are ready

3. **Document Upload Notifications**:
   - Subject: "A document has been uploaded ([Document Name])"
   - Shows document type in subject
   - Includes document summary in preview
   - Image references in preview
   - Document types: Entity Status, Bank Statement, Passport, Property/Dwelling Insurance Policy, Drivers License, Bank Statement - Current Month, Bank Statement - Previous Month, EIN, Purchase Contract, Operating Agreement, Articles of Incorporation

4. **Document Request Emails**:
   - Subject: "You have [X] document requests"
   - Shows count of requested documents (11, 7, 4, 1)

5. **Application Received Emails**:
   - Subject: "Application Received"
   - Notifies when application is received

6. **Manual Emails**:
   - Subject: "DSCR Loan | Rodrigo Fachini | 4151 Sonoma Blvd, Kissimmee, FL 34741"
   - Body preview shows message content
   - Includes attachments (e.g., "Investor Experience and Portfolio Form v3.2 pg.2.pdf 620.11 kB")
   - From individual users (e.g., "Evan Shields")

**Email Preview Features**
- **Subject + Body**: Shows subject line followed by body preview
- **Truncation**: Preview text truncated with ellipsis
- **Image References**: Shows image references (e.g., "image.png")
- **Attachment Info**: Shows attachment name and size (e.g., "pg.2.pdf 620.11 kB")
- **Rich Content**: Preview includes formatted content (all caps headers, summary text)

**Email Senders**
- **System Sender**: "USDV Capital Inc." (automated/system-generated emails)
- **User Senders**: Individual users (e.g., "Evan Shields") for manual/composed emails

**Date Patterns**
- **Most Recent**: Nov 7, 2025 (loan approval)
- **Recent Activity**: Oct 9, Oct 6, Oct 1 (document-related)
- **Application Period**: Sep 26, 2025 (application submission, document uploads)
- **Initial Requests**: Sep 25, Sep 4 (document requests)

**Display/Pagination**
- **Display**: "Showing 23 of 23" (all emails visible)
- **No Pagination**: All emails fit on single page
- **Complete History**: Full email communication history for loan

**Mail Tab Features**
- **Loan-Specific View**: All emails filtered to this loan context
- **Search**: Search emails within loan
- **Compose**: Send new emails related to loan
- **Bulk Selection**: Select multiple emails for actions
- **Chronological Order**: Emails listed chronologically (newest first, inferred)
- **Preview**: Rich email preview with subject and body text
- **Attachment Info**: Attachment details visible in preview

**Integration with Main Mail Page**
- **Filtered View**: This is a filtered view of the main Inbox/Mail page
- **Loan Context**: All emails automatically filtered to this loan
- **Same Functionality**: Similar to main mail page but scoped to loan

**Component Structure** (Inferred)
```
<MailTab loanId={numericId}>
  <MailHeader>
    <SelectAllCheckbox />
    <MailTitle>All Mail</MailTitle>
    <SearchBox placeholder="Search" onChange={handleSearch} />
    <ComposeButton onClick={openComposeModal} />
  </MailHeader>
  <MailTable>
    <TableHeader>
      <ColumnHeader>Checkbox</ColumnHeader>
      <ColumnHeader>Sender</ColumnHeader>
      <ColumnHeader>Subject/Preview</ColumnHeader>
      <ColumnHeader>Date</ColumnHeader>
    </TableHeader>
    {emails.map(email => (
      <EmailRow
        selected={email.selected}
        sender={email.sender}
        subject={email.subject}
        preview={email.bodyPreview}
        date={email.date}
        attachments={email.attachments}
        onClick={openEmailDetail}
      />
    ))}
  </MailTable>
  <MailFooter>
    <DisplayCount>Showing {visibleCount} of {totalCount}</DisplayCount>
  </MailFooter>
</MailTab>
```

**Component Structure** (Inferred)
```
<AmortizationScheduleTab loanId={numericId}>
  <AmortizationHeader>
    <AmortizationTitle>Amortization Schedule</AmortizationTitle>
    <ExportButton onClick={exportSchedule} />
  </AmortizationHeader>
  <AmortizationTable>
    <TableHeader>
      <ColumnHeader>Payment</ColumnHeader>
      <ColumnHeader>Due</ColumnHeader>
      <ColumnHeader>Principal</ColumnHeader>
      <ColumnHeader>Interest</ColumnHeader>
      <ColumnHeader>Total Payment</ColumnHeader>
      <ColumnHeader>Balance</ColumnHeader>
    </TableHeader>
    {payments.map(payment => (
      <PaymentRow
        paymentNumber={payment.number}
        dueDate={payment.dueDate}
        principal={payment.principal}
        interest={payment.interest}
        totalPayment={payment.total}
        balance={payment.balance}
      />
    ))}
  </AmortizationTable>
  <Pagination>
    <DisplayCount>Showing {visibleCount} of {totalCount}</DisplayCount>
    {hasMore && <LoadMoreButton onClick={loadMore} />}
  </Pagination>
</AmortizationScheduleTab>
```

**Component Structure** (Inferred)
```
<CollateralTab loanId={numericId}>
  <CollateralHeader>
    <CollateralTitle>Collateral Details</CollateralTitle>
    <OrderFloodReportButton disabled />
    <AddNewPropertyButton disabled />
  </CollateralHeader>
  <MapSection>
    <GoogleMapsEmbed coordinates={coordinates} zoom={10} />
    <MapControls>
      <KeyboardShortcutsButton />
      <MapDataButton />
      <OpenInGoogleMapsLink />
      <TermsLink />
      <ReportErrorLink />
    </MapControls>
  </MapSection>
  <PropertyDetailsSection>
    <PropertyDetailsHeader>
      <PropertyDetailsTitle>Property Details</PropertyDetailsTitle>
      <PropertyDetailsTabs>
        <Tab name="Property Details" active />
        <Tab name="Valuations" />
        <Tab name="Insurance" />
        <Tab name="Flood Report" />
      </PropertyDetailsTabs>
    </PropertyDetailsHeader>
    <AddressDisplay>
      <Street>{street}</Street>
      <CityStateZip>{cityStateZip}</CityStateZip>
      <Country>{country}</Country>
      <County>{county}</County>
    </AddressDisplay>
  </PropertyDetailsSection>
  <PropertyValueSection editable>
    <PropertyValueTitle>Property Value</PropertyValueTitle>
    <EditButton />
    <Field label="Purchase Price" value={purchasePrice} />
    <Field label="Purchase Date" value={purchaseDate} />
    <Field label="Existing Debt" value={existingDebt} />
    <Field label="As Is Value" value={asIsValue} />
    <Field label="ARV - Lender" value={arvLender} />
    <Field label="ARV - Borrower" value={arvBorrower} />
    <Field label="Appraisal Ordered" value={appraisalOrdered} />
  </PropertyValueSection>
  <TaxesHOASection editable>
    <TaxesHOATitle>Taxes & HOA</TaxesHOATitle>
    <EditButton />
    <Field label="Property Taxes" value={propertyTaxes} />
    <Field label="HOA Fees" value={hoaFees} />
    <Field label="HOA Due Date" value={hoaDueDate} />
  </TaxesHOASection>
  <PropertyFeaturesSection editable>
    <PropertyFeaturesTitle>Property Features</PropertyFeaturesTitle>
    <EditButton />
    <Field label="Units" value={units} />
    <Field label="Gross Livable Area (GLA)" value={gla} />
    <Field label="Property Type" value={propertyType} />
    <Field label="Year Built" value={yearBuilt} />
    <Field label="Construction Materials" value={constructionMaterials} />
  </PropertyFeaturesSection>
  <UnitDetailsSection>
    <UnitDetailsTitle>Unit Details</UnitDetailsTitle>
    <AddUnitButton />
    <OpenWorksheetButton />
  </UnitDetailsSection>
</CollateralTab>
```

#### **Component Structure** (Inferred)
```
<FundingTab loanId={numericId}>
  <FundingSection>
    <FundingHeader>
      <FundingTitle>Funding</FundingTitle>
      <ExportButton />
      <TransferButton />
      <AddFundingButton onClick={openAddFundingModal} />
    </FundingHeader>
    <FundingTable>
      <TableHeader>
        <ColumnHeader>Investor</ColumnHeader>
        <ColumnHeader>Yield</ColumnHeader>
        <ColumnHeader>Invested / Committed</ColumnHeader>
        <ColumnHeader>Returned</ColumnHeader>
        <ColumnHeader>Balance</ColumnHeader>
        <ColumnHeader>Income</ColumnHeader>
        <ColumnHeader>Status</ColumnHeader>
        <ColumnHeader>Actions</ColumnHeader>
      </TableHeader>
      {fundings.length > 0 ? (
        fundings.map(funding => (
          <FundingRow
            investor={funding.investor}
            yield={funding.yield}
            invested={funding.invested}
            committed={funding.committed}
            returned={funding.returned}
            balance={funding.balance}
            income={funding.income}
            status={funding.status}
          />
        ))
      ) : (
        <EmptyState>None have been created yet</EmptyState>
      )}
    </FundingTable>
  </FundingSection>
  <HistorySection>
    <HistoryHeader>
      <HistoryTitle>History</HistoryTitle>
      <ExportButton />
    </HistoryHeader>
    <HistoryTable>
      <TableHeader>
        <ColumnHeader>Date</ColumnHeader>
        <ColumnHeader>Type</ColumnHeader>
        <ColumnHeader>Principal</ColumnHeader>
        <ColumnHeader>Status</ColumnHeader>
        <ColumnHeader>Actions</ColumnHeader>
      </TableHeader>
      {history.length > 0 ? (
        history.map(transaction => (
          <HistoryRow
            date={transaction.date}
            type={transaction.type}
            principal={transaction.principal}
            status={transaction.status}
          />
        ))
      ) : (
        <EmptyState>None have been created yet</EmptyState>
      )}
    </HistoryTable>
  </HistorySection>
</FundingTab>
```

**Component Structure** (Inferred)
```
<ChargesTab loanId={numericId}>
  <ChargesHeader>
    <ChargesTitle>Charges</ChargesTitle>
    <ExportButton />
    <AddChargeButton onClick={openAddChargeModal} />
  </ChargesHeader>
  <ChargesTable>
    <TableHeader>
      <ColumnHeader>Date</ColumnHeader>
      <ColumnHeader>Description</ColumnHeader>
      <ColumnHeader>Payable To</ColumnHeader>
      <ColumnHeader>Due Date</ColumnHeader>
      <ColumnHeader>Original Amount</ColumnHeader>
      <ColumnHeader>Amount Due</ColumnHeader>
      <ColumnHeader>Status</ColumnHeader>
      <ColumnHeader>Actions</ColumnHeader>
    </TableHeader>
    {charges.map(charge => (
      <ChargeRow
        date={charge.date}
        description={charge.description}
        payableTo={charge.payableTo}
        dueDate={charge.dueDate}
        originalAmount={charge.originalAmount}
        amountDue={charge.amountDue}
        status={charge.status}
      />
    ))}
  </ChargesTable>
</ChargesTab>
```

#### **Component Structure** (Inferred)
```
<LoanDetailPage loanId={numericId}>
  <LoanHeader>
    <Breadcrumb>
      <BreadcrumbItem label="Pipeline" link="/admin/loans" />
      <BreadcrumbItem label={propertyAddress} active />
    </Breadcrumb>
    <LoanTitle>{propertyAddress}</LoanTitle>
    <LoanStatusBadge>Closed</LoanStatusBadge>
    <SubstatusBadge>Pending Servicing Approval</SubstatusBadge>
    <LoanMetadata>
      <MetadataItem label="ID" value={loanId} />
      <MetadataItem label="Primary Borrower" value={borrowerName} link={`/admin/loans/${loanId}/contacts`} />
      <MetadataItem label="Closing Date" value={closingDate} />
      <MetadataItem label="Product" value={product} link={`/admin/loans/${loanId}/product`} />
      <MetadataItem label="Use of Funds" value={useOfFunds} />
    </LoanMetadata>
  </LoanHeader>
  <LoanSubTabs>
    <Tab name="General" active />
    <Tab name="Documents" />
    <Tab name="Contacts" />
    <Tab name="Charges" />
    <Tab name="Funding" />
    <Tab name="Application" />
    <Tab name="Collateral" />
    <Tab name="More" icon="ellipses" />
    <Tab name="Mail" />
  </LoanSubTabs>
  <LoanContent>
    {activeTab === 'General' && <GeneralTab>
      <TermsSection editable />
      <ParametersSection />
      <StatisticsSection readOnly />
      <CollateralSummarySection readOnly />
      <PaymentSection editable />
      <ClassesSection editable />
      <BankingDetailsSection editable />
      <ClosingAgentSection />
      <SpreadAllocationSection editable />
    </GeneralTab>}
    {activeTab === 'Contacts' && <ContactsTab>
      <ContactCards>
        <ContactCard type="borrower" name="4151 Sonoma LLC" phone="(407) 922-0250" link="/admin/borrowers/14285364" />
        <ContactCard type="guarantor" name="Rodrigo Fachini Tavares" email="rodrigo.fachini@gmail.com" phone="(407) 922-0250" link="/admin/borrowers/11642432" />
      </ContactCards>
      <ContactsHeader>
        <ContactsTitle>All Contacts</ContactsTitle>
        <AddContactButton />
      </ContactsHeader>
      <ContactsTable>
        <TableGroupHeader>Borrowers, Guarantors and Viewers</TableGroupHeader>
        <ContactRow /> (repeat for each contact)
      </ContactsTable>
    </ContactsTab>}
    {activeTab === 'Charges' && <ChargesTab>
      <ChargesHeader>
        <ChargesTitle>Charges</ChargesTitle>
        <ExportButton />
        <AddChargeButton />
      </ChargesHeader>
      <ChargesTable>
        <ChargeRow /> (repeat for each charge)
      </ChargesTable>
    </ChargesTab>}
    {activeTab === 'Funding' && <FundingTab>
      <FundingSection>
        <FundingHeader>
          <FundingTitle>Funding</FundingTitle>
          <ExportButton />
          <TransferButton />
          <AddFundingButton />
        </FundingHeader>
        <FundingTable>
          <FundingRow /> (repeat for each funding/investor)
        </FundingTable>
      </FundingSection>
      <HistorySection>
        <HistoryHeader>
          <HistoryTitle>History</HistoryTitle>
          <ExportButton />
        </HistoryHeader>
        <HistoryTable>
          <HistoryRow /> (repeat for each history transaction)
        </HistoryTable>
      </HistorySection>
    </FundingTab>}
    {activeTab === 'Application' && <ApplicationTab>
      <ApplicationHeader>
        <SubmissionInfo>
          <Text>Application submitted by</Text>
          <BorrowerLink>{borrowerName}</BorrowerLink>
          <Date>on {submissionDate}</Date>
        </SubmissionInfo>
        <RequestChangesButton />
        <DownloadPDFButton />
      </ApplicationHeader>
      <TransactionDetailsSection>
        <Field label="Use of Funds" value={useOfFunds} />
        <Field label="Exit Strategy" value={exitStrategy} />
        <Field label="Loan Amount" value={loanAmount} />
        <Field label="Closing Date" value={closingDate} />
      </TransactionDetailsSection>
      <PropertySection>
        <Field label="Property Address" value={propertyAddress} />
        <Field label="Property Type" value={propertyType} />
        <Field label="Purchase Price" value={purchasePrice} />
        <Field label="ARV" value={arv} />
        <Field label="Total Rehab" value={totalRehab} />
      </PropertySection>
      <BorrowerDetailsSection>
        <BorrowerSubsection>
          <Field label="Company Name" value={companyName} />
          <Field label="Type" value={entityType} />
          <Field label="Jurisdiction" value={jurisdiction} />
          <Field label="Phone" value={phone} />
        </BorrowerSubsection>
        <GuarantorSubsection>
          <Field label="Full Name" value={guarantorName} />
          <Field label="Credit Score" value={creditScore} />
          <Field label="Number of Flips" value={numberOfFlips} />
          <Field label="Phone" value={guarantorPhone} />
          <Field label="Email" value={guarantorEmail} link />
        </GuarantorSubsection>
      </BorrowerDetailsSection>
      <DeclarationsSection>
        <Question question={questions.judgments} answer={answers.judgments} />
        <Question question={questions.bankruptcy} answer={answers.bankruptcy} />
        <Question question={questions.foreclosure} answer={answers.foreclosure} />
        <DisclosureAgreement />
        <Signature image={signatureImage} />
        <SignedDate>{signedDate}</SignedDate>
      </DeclarationsSection>
    </ApplicationTab>}
    {activeTab === 'Collateral' && <CollateralTab>
      <CollateralHeader>
        <CollateralTitle>Collateral Details</CollateralTitle>
        <OrderFloodReportButton disabled />
        <AddNewPropertyButton disabled />
      </CollateralHeader>
      <MapSection>
        <GoogleMapsEmbed />
      </MapSection>
      <PropertyDetailsSection>
        <AddressDisplay />
        <PropertyDetailsTabs>
          <Tab name="Property Details" active />
          <Tab name="Valuations" />
          <Tab name="Insurance" />
          <Tab name="Flood Report" />
        </PropertyDetailsTabs>
      </PropertyDetailsSection>
      <PropertyValueSection editable>
        <EditButton />
        <PropertyValueFields />
      </PropertyValueSection>
      <TaxesHOASection editable>
        <EditButton />
        <TaxesHOAFields />
      </TaxesHOASection>
      <PropertyFeaturesSection editable>
        <EditButton />
        <PropertyFeaturesFields />
      </PropertyFeaturesSection>
      <UnitDetailsSection>
        <AddUnitButton />
        <OpenWorksheetButton />
      </UnitDetailsSection>
    </CollateralTab>}
    {activeTab === 'Documents' && <DocumentsTab>
      <DocumentsHeader>
        <SelectAllCheckbox />
        <DocumentsTitle>Documents</DocumentsTitle>
        <GenerateButton />
      </DocumentsHeader>
      <DocumentCategories>
        <DocumentCategory name="Borrower" completed={10} total={11} expandable>
          <DocumentsTable />
        </DocumentCategory>
        <DocumentCategory name="Guarantor" completed={4} total={9} expandable>
          <DocumentsTable />
        </DocumentCategory>
        <DocumentCategory name="Collateral" completed={2} total={8} expandable>
          <DocumentsTable />
        </DocumentCategory>
        <DocumentCategory name="Loan" completed={0} total={5} expandable>
          <DocumentsTable />
        </DocumentCategory>
        <DocumentCategory name="Closing" completed={0} total={10} expandable>
          <DocumentsTable />
        </DocumentCategory>
        <DocumentCategory name="Other" completed={0} total={0} expandable>
          <EmptyState>This section is empty. Create new document</EmptyState>
        </DocumentCategory>
      </DocumentCategories>
    </DocumentsTab>}
    {activeTab === 'Contacts' && <ContactsTab>
      <ContactCards>
        <ContactCard type="borrower" name="4151 Sonoma LLC" phone="(407) 922-0250" />
        <ContactCard type="guarantor" name="Rodrigo Fachini Tavares" email="rodrigo.fachini@gmail.com" phone="(407) 922-0250" />
      </ContactCards>
      <ContactsHeader>
        <ContactsTitle>All Contacts</ContactsTitle>
        <AddContactButton />
      </ContactsHeader>
      <ContactsTable>
        <TableGroupHeader>Borrowers, Guarantors and Viewers</TableGroupHeader>
        <ContactRow /> (repeat for each contact)
      </ContactsTable>
    </ContactsTab>}
    {activeTab === 'Charges' && <ChargesTab />}
    {activeTab === 'Funding' && <FundingTab />}
    {activeTab === 'Application' && <ApplicationTab />}
    {activeTab === 'Collateral' && <CollateralTab />}
    {activeTab === 'Mail' && <MailTab />}
  </LoanContent>
</LoanDetailPage>
```

**Component Reusability Pattern**:
- Contacts page component likely accepts a `type` prop/route param
- Type-specific pages render same component with `type="borrower"` (or investor/vendor)
- **Column Configuration**: Each type can have unique columns:
  - **Investors**: Includes "Invested" column (shows investment amounts) - 6 columns total
  - **Borrowers**: Standard columns without Type - 5 columns (Name, Associated With, Owner, Last Activity, Status)
  - **Vendors**: Completely different column set - 8 columns (Name, Role, Associated With, Email, Phone, Cash, Owner) - No Last Activity or Status columns
- Conditional column rendering based on whether type is filtered or not and type-specific column configuration
- Button text dynamically changes based on type

**Routing Strategy**:
- Separate routes for each type: `/admin/borrowers`, `/admin/investors`, `/admin/vendors`
- These routes are siblings to `/admin/contacts`, not nested
- Sidebar navigation shows all four links (Contacts, Borrowers, Investors, Vendors)
- Likely share the same component with different data/query params

**Implementation Pattern** (Recommended):
```javascript
// Shared ContactsList component
<ContactsList 
  type="borrower"  // or "investor" or "vendor" or null for all
  showTypeColumn={!type}  // Hide type column when type is filtered
  addButtonText={type ? `Add ${capitalize(type)}` : "Add Contacts"}
  columns={getColumnsForType(type)}  // Type-specific column configuration
/>

// Column configuration example
const getColumnsForType = (type) => {
  const baseColumns = ['name', 'associatedWith', 'owner', 'lastActivity', 'status'];
  
  switch(type) {
    case 'investor':
      return ['name', 'associatedWith', 'invested', 'owner', 'lastActivity', 'status'];
    case 'borrower':
      return ['name', 'associatedWith', 'owner', 'lastActivity', 'status'];
    case 'vendor':
      return ['name', 'role', 'associatedWith', 'email', 'phone', 'cash', 'owner'];
    default: // All contacts
      return ['name', 'associatedWith', 'type', 'owner', 'lastActivity', 'status'];
  }
};
```

### 2.9 Component Hierarchy (Inferred)

```
<App>
  <AppShell>
    <Sidebar>
      <BrandLogo />
      <Navigation>
        <NavItem route="/admin/dashboard" />
        <NavItem route="/admin/mail" />
        <NavItem route="/admin/tasks" />
        ... (other nav items)
      </Navigation>
      <HelpLink />
    </Sidebar>
    <MainContent>
      <Header>
        <PageTitle />
        <NotificationIcon />
        <UserMenu />
      </Header>
      <PageContent>
        {route === '/dashboard' && <Dashboard>
          <MetricCards>
            <MetricCard />
            <MetricCard />
            <MetricCard />
            <MetricCard />
          </MetricCards>
          <ChartGrid>
            <Chart title="Loans Per Month" />
            <Chart title="Income" />
          </ChartGrid>
          <AIChatWidget />
        </Dashboard>}
        {route === '/mail' && <MailPage>
          <MailTabs tabs={['Inbox', 'Drafts', 'Sent']} />
          <MailToolbar>
            <SearchBox placeholder="Search inbox" />
            <ComposeButton />
          </MailToolbar>
          <EmailList>
            <EmailListItem /> (repeat for each email)
          </EmailList>
          <Pagination />
        </MailPage>}
        {route === '/tasks' && <TasksPage>
          <TaskFilters>
            <FilterButton label="All" />
            <FilterButton label="My Tasks" />
          </TaskFilters>
          <TaskToolbar>
            <SearchBox placeholder="Search" />
            <NewTaskButton />
          </TaskToolbar>
          <TaskList>
            <TaskListItem /> (repeat for each task)
          </TaskList>
          <Pagination />
        </TasksPage>}
        {route === '/contacts' && <ContactsPage>
          <ContactFilters>
            <FilterButton label="All" />
            <FilterButton label="Companies" />
            <FilterButton label="People" />
          </ContactFilters>
          <ContactToolbar>
            <SearchBox placeholder="Search" />
            <ExportButton />
            <AddContactsButton />
          </ContactToolbar>
          <ContactList>
            <ContactListItem /> (repeat for each contact)
          </ContactList>
          <Pagination />
        </ContactsPage>}
        {route === '/quotes' && <QuotesPage>
          <QuoteFilters>
            <FilterButton label="All" />
            <FilterButton label="Archived" />
          </QuoteFilters>
          <QuoteToolbar>
            <SearchBox placeholder="Search" />
            <AddQuoteButton />
          </QuoteToolbar>
          <QuoteList>
            <QuoteListItem /> (repeat for each quote)
          </QuoteList>
          <Pagination />
        </QuotesPage>}
        {route === '/loans' && <PipelinePage>
          <PipelineHeader>
            <ViewToggleButton label={viewMode === 'kanban' ? 'Table View' : 'Pipeline View'} />
            <SummaryStats count={24} total="$6,774,149.00" />
            <FilterButton />
            <SortButton />
            <SearchBox placeholder="Search" />
            <ExportButton />
            <AddLoanButton />
          </PipelineHeader>
          {viewMode === 'kanban' ? <KanbanBoard>
            <KanbanColumn stage="Lead" count={5} total="$2,485,143.00">
              <LoanCard /> (repeat for each loan)
            </KanbanColumn>
            <KanbanColumn stage="Processing" count={2} total="$365,400.00">
              <LoanCard /> (repeat for each loan)
            </KanbanColumn>
            <KanbanColumn stage="Underwriting Approved" count={1} total="$208,500.00">
              <LoanCard /> (repeat for each loan)
            </KanbanColumn>
            <KanbanColumn stage="Closed" count={16} total="$3,715,106.00">
              <LoanCard /> (repeat for each loan)
            </KanbanColumn>
          </KanbanBoard> : <PipelineTable>
            <TableGroup stage="Lead" count={5} total="$2,485,143.00">
              <LoanRow /> (repeat for each loan)
            </TableGroup>
            <TableGroup stage="Processing" count={2} total="$365,400.00">
              <LoanRow /> (repeat for each loan)
            </TableGroup>
            <TableGroup stage="Approved" count={1} total="$208,500.00">
              <LoanRow /> (repeat for each loan)
            </TableGroup>
            <TableGroup stage="Closed" count={16} total="$3,715,106.00">
              <LoanRow /> (repeat for each loan)
            </TableGroup>
          </PipelineTable>}
        </PipelinePage>}
        {route === '/borrowers' && <ContactsPage type="borrower">
          <ContactFilters>
            <FilterButton label="All" />
            <FilterButton label="Companies" />
            <FilterButton label="People" />
          </ContactFilters>
          <ContactToolbar>
            <SearchBox placeholder="Search" />
            <ExportButton />
            <AddContactButton label="Add Borrower" />
          </ContactToolbar>
          <ContactList showTypeColumn={false}>
            <ContactListItem /> (repeat for each borrower)
          </ContactList>
          <Pagination />
        </ContactsPage>}
        {route === '/investors' && <ContactsPage type="investor">
          {/* Similar structure to borrowers */}
        </ContactsPage>}
        {route === '/vendors' && <ContactsPage type="vendor">
          {/* Similar structure to borrowers */}
        </ContactsPage>}
        ... (other route components)
      </PageContent>
    </MainContent>
  </AppShell>
</App>
```

---

## 3. Routing Strategy

### 3.1 Routing Implementation
- **Type**: Client-side routing (SPA)
- **Pattern**: Hierarchical, RESTful URLs
- **Base Path**: `/admin` (indicates admin section)

### 3.2 Route Structure Analysis

**Flat Routes:**
- `/admin/dashboard`
- `/admin/mail`
- `/admin/tasks`
- `/admin/contacts`
- `/admin/quotes`
- `/admin/loans`
- `/admin/servicing`
- `/admin/reports`
- `/admin/funds`
- `/admin/offerings`

**Nested Routes:**
- `/admin/payments/due` (payment sub-section)
- `/admin/payouts/ready` (payout sub-section)

### 3.3 Routing Patterns (Recommended Implementation)
```javascript
// React Router example structure
<Routes>
  <Route path="/admin" element={<AppLayout />}>
    <Route path="dashboard" element={<Dashboard />} />
    <Route path="mail" element={<Mail />} />
    <Route path="tasks" element={<Tasks />} />
    <Route path="contacts" element={<Contacts />} />
    <Route path="quotes" element={<Quotes />} />
    <Route path="loans" element={<Pipeline />} />
    <Route path="servicing" element={<Loans />} />
    <Route path="payments">
      <Route path="due" element={<PaymentsDue />} />
    </Route>
    <Route path="payouts">
      <Route path="ready" element={<PayoutsReady />} />
    </Route>
    <Route path="reports" element={<Reports />} />
    <Route path="funds" element={<Funds />} />
    <Route path="offerings" element={<Offerings />} />
  </Route>
</Routes>
```

### 3.4 Route Guards & Authentication
- Likely protected routes (all under `/admin`)
- Authentication state management required
- Redirect to login if unauthenticated

---

## 4. State Management

### 4.1 State Requirements (Inferred)

#### **Global State:**
- **Authentication**: User session, permissions
- **Navigation**: Active route, sidebar state
- **UI State**: Notifications, modal states, theme preferences
- **User Profile**: Current user data ("EA" initials shown)

#### **Route-Specific State:**
- **Dashboard**: 
  - Metric values (Principal Balance, Active Loans, etc.)
  - Chart data (time-series data for loans and income)
  - AI chat history/state

- **Mail/Inbox** (Observed):
  - Email list data (50+ emails loaded)
  - Selected email IDs (for bulk actions)
  - Active tab state (Inbox/Drafts/Sent)
  - Search query/filter state
  - Pagination state (current page, total count: 133)
  - Email read/unread status
  - Attachment metadata
  - Scroll position (for maintaining view on navigation back)

- **Tasks** (Observed):
  - Task list data (43 tasks visible)
  - Selected task IDs (for bulk actions)
  - Active filter state (All/My Tasks)
  - Search query/filter state
  - Task status state (To Do, Done)
  - Assignee information
  - Due date filtering/sorting
  - Task-to-loan relationship mapping
  - Completion state (checked/unchecked checkboxes)

- **Contacts** (Observed):
  - Contact list data (51 contacts visible, showing 50)
  - Selected contact IDs (for bulk actions)
  - Active filter state (All/Companies/People)
  - Contact type filtering (Borrower/Vendor/Investor visible in table)
  - Search query/filter state
  - Contact status (Draft, Active)
  - Owner/assignee information (initials)
  - Associated relationships (person-company associations)
  - Last activity timestamps
  - Pagination state (50 of 51, with Load more)

- **Tasks**: Task list, filters, statuses
- **Contacts**: Contact list, search/filter state
- And similar patterns for other routes

### 4.2 State Management Patterns (Recommended)

#### **Option 1: Context API + React Query (Modern Approach)**
```javascript
// Global context for auth, UI state
const AppContext = createContext();

// React Query for server state
useQuery(['dashboard', 'metrics'], fetchDashboardMetrics);
useQuery(['dashboard', 'charts'], fetchChartData);
```

#### **Option 2: Redux/Zustand (Centralized State)**
```javascript
// Store structure
{
  auth: { user, token, isAuthenticated },
  ui: { sidebarOpen, notifications, theme },
  dashboard: { metrics, chartData, isLoading },
  mail: { messages, filters, selected },
  // ... other feature states
}
```

#### **Option 3: Server State + Local State**
- Server state: React Query / SWR for API data
- Local state: useState/useReducer for UI interactions
- Global state: Context API for shared UI state

### 4.3 Data Fetching Patterns
- **Initial Load**: Fetch dashboard metrics and charts on mount
- **Polling/Real-time**: May use WebSockets or polling for live updates
- **Lazy Loading**: Charts and heavy components loaded on demand
- **Caching**: Chart data and metrics likely cached with TTL

---

## 5. Styling Methodology

### 5.1 Design System Characteristics

#### **Color Palette:**
- **Primary Background**: Light gray (#f5f5f5 or similar) for sidebar
- **Content Background**: White (#ffffff) for cards and main area
- **Text**: Dark gray/black for primary text
- **Accent Colors**: 
  - Blue: Active states, primary actions, chart lines
  - Green: Secondary chart series, positive indicators
  - Gray shades: Borders, dividers, inactive states

#### **Typography:**
- **Font Family**: Modern sans-serif (likely Inter, Roboto, or system font stack)
- **Hierarchy**: 
  - H1: Large, bold (page titles)
  - Body: Medium weight, readable size
  - Labels: Smaller, medium weight
- **Font Loading**: Google Fonts or web-safe fonts

#### **Spacing System:**
- Consistent padding/margin (likely 4px or 8px base unit)
- Card spacing: ~16-24px between cards
- Content padding: ~24-32px from edges

#### **Component Styling:**
- **Cards**: 
  - White background
  - Rounded corners (8-12px border-radius)
  - Subtle box-shadow (elevation)
  - Padding: 16-24px
- **Navigation Items**:
  - Hover states (background color change)
  - Active state (darker background + left border accent)
  - Icon + text alignment
  - Padding: ~12-16px vertical
- **Buttons**:
  - Primary: Blue background, white text
  - Disabled: Gray background, disabled cursor

#### **Table/List Styling** (Observed on Inbox Page):
- **Email List Table**:
  - Clean, minimal table design
  - Alternating row backgrounds (likely for readability)
  - Column alignment: Left for text, right for timestamps
  - Row hover states (background color change)
  - Truncated text with ellipsis for long content
  - Compact spacing between rows
  - Subtle borders or dividers between rows

- **Tab Navigation**:
  - Text-based tabs (minimal styling)
  - Active tab highlighted (likely underline or background)
  - Spacing between tab items

- **Search Input**:
  - Standard text input styling
  - Integrated into toolbar layout
  - Consistent with overall design system

### 5.2 Styling Approach (Recommended Implementation)

#### **Option 1: Tailwind CSS + Component Library**
```jsx
// Tailwind utility classes
<div className="bg-white rounded-lg shadow-sm p-6">
  <h2 className="text-lg font-semibold mb-4">Principal Balance</h2>
  <span className="text-3xl font-bold">-</span>
</div>
```

#### **Option 2: CSS Modules / Styled Components**
```jsx
// Component-scoped styles
import styles from './MetricCard.module.css';

<div className={styles.card}>
  <h2 className={styles.title}>Principal Balance</h2>
  <span className={styles.value}>-</span>
</div>
```

#### **Option 3: CSS-in-JS (Emotion, Styled Components)**
```jsx
const Card = styled.div`
  background: white;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  padding: 24px;
`;
```

#### **Option 4: Component Library (shadcn/ui, Material-UI, Chakra UI)**
- Pre-built components with consistent styling
- Theme customization
- Accessible by default

### 5.3 Responsive Design
- **Desktop-first**: Optimized for desktop (sidebar always visible)
- **Breakpoints**: Likely uses standard breakpoints (768px, 1024px, 1280px)
- **Mobile**: Sidebar may collapse to hamburger menu on small screens

### 5.4 Theme Support
- Light theme (observed)
- Dark theme support likely available (common in modern apps)
- Theme state managed globally

---

## 6. Interactive Behaviors

### 6.1 Navigation Interactions

#### **Sidebar Navigation:**
- **Click**: Navigate to route, update active state
- **Hover**: Visual feedback (background color change)
- **Active State**: Persistent highlighting with accent border
- **Keyboard Navigation**: Likely supports arrow keys, Tab navigation

#### **Route Transitions:**
- Smooth transitions between routes (CSS transitions or animations)
- Loading states during data fetch
- URL updates without page reload

### 6.2 Dashboard Interactions

#### **Metric Cards:**
- **Hover**: Subtle elevation or border highlight
- **Click**: May navigate to detailed view or modal
- **Tooltip**: Additional context on hover

#### **Charts:**
- **Hover**: Tooltip showing exact values at data point
- **Click**: May filter or drill down into data
- **Legend Interaction**: Toggle series visibility (common pattern)
- **Zoom/Pan**: Possible in advanced chart implementations

#### **AI Chat Widget:**
- **Input Focus**: Button enables when text entered
- **Submit**: Send message, display response
- **Conversation History**: Maintains chat context
- **Typing Indicator**: Shows when AI is processing
- **Error Handling**: Displays errors if API fails

### 6.2.5 Inbox/Mail Page Interactions (Observed)

#### **Tab Navigation:**
- **Click**: Switches between Inbox, Drafts, Sent views
- **Active State**: Current tab visually highlighted
- **URL Update**: May update URL query param or route (e.g., `/admin/mail?tab=drafts`)
- **Data Refetch**: Loads appropriate email list for selected tab

#### **Email List Interactions:**
- **Row Click**: Opens email detail view (likely in modal, side panel, or new route)
- **Checkbox Selection**: 
  - Individual: Selects/deselects single email
  - Bulk: Selects/deselects all visible emails
  - Selection state likely triggers action toolbar
- **Hover**: Visual feedback (background color change, pointer cursor)
- **Scroll**: Infinite scroll or pagination loads more emails
- **Keyboard Navigation**: Arrow keys to navigate between emails (common pattern)

#### **Search Functionality:**
- **Input**: Typing triggers search (likely debounced)
- **Real-time Filtering**: Email list updates as user types
- **Clear Search**: X button or clear action resets to full list
- **Search Scope**: Searches across sender, subject, and content

#### **Compose Button:**
- **Click**: Opens email composition interface
- **Modal/Side Panel**: Likely opens overlay for composing
- **Form Fields**: To, CC, BCC, Subject, Body, Attachments
- **Save Draft**: Auto-saves or manual save to Drafts folder
- **Send**: Submits email and refreshes list

#### **Pagination/Load More:**
- **Load More Button**: 
  - Click loads next batch (likely 50 more items)
  - Updates "Showing X of Y" counter
  - Appends to existing list (infinite scroll pattern)
- **Scroll to Load** (Possible): May also load on scroll to bottom

#### **Email Detail View** (Inferred):
- **Open Email**: Clicking row opens full email view
- **Close**: Back button or close action returns to list
- **Actions**: Reply, Reply All, Forward, Archive, Delete
- **Attachment Download**: Click to download/view attachments
- **Thread Navigation**: Navigate between emails in thread

#### **Bulk Actions** (Inferred):
- **Action Toolbar**: Appears when emails selected
- **Actions**: Delete, Archive, Mark as Read, Move to Folder, etc.
- **Confirmation**: Likely requires confirmation for destructive actions

### 6.2.6 Tasks Page Interactions (Observed)

#### **Filter Navigation:**
- **Button Click**: Switches between "All" and "My Tasks" views
- **Active State**: Selected filter button visually highlighted
- **Data Filtering**: Filters task list by scope (all tasks vs. user's assigned tasks)
- **URL Update**: May update URL query param (e.g., `/admin/tasks?filter=my-tasks`)

#### **Task List Interactions:**
- **Row Click**: Opens task detail/edit view (likely in modal, side panel, or inline expansion)
- **Checkbox Selection**: 
  - Individual: Selects/deselects single task
  - Bulk selection for batch operations
  - Completed tasks pre-checked (status = "Done")
- **Task Name Click**: Opens task detail/edit interface
- **Loan Link Click**: Navigates to loan detail page (`/admin/loans/{loanId}`)
- **Assignee Tooltip**: Hover shows full assignee information
- **Status Badge**: Visual indicator of task completion status

#### **Search Functionality:**
- **Input**: Typing triggers search (likely debounced)
- **Real-time Filtering**: Task list updates as user types
- **Search Scope**: Searches across task names, loan properties, assignees, descriptions
- **Clear Search**: Resets to unfiltered list

#### **New Task Button:**
- **Click**: Opens task creation interface
- **Modal/Form**: Likely opens overlay or form for creating new task
- **Form Fields**: Task name, description, due date, assignee, related loan, status
- **Save/Create**: Creates task and refreshes list

#### **Task Status Management:**
- **Status Change**: Checkbox toggle or status badge click changes status
- **Completion**: Checking task updates status to "Done"
- **Reopen**: Unchecking "Done" task may change status back to "To Do"
- **Bulk Status Change**: Change status for multiple selected tasks

#### **Task Editing** (Inferred):
- **Inline Edit**: Click task name to edit
- **Detail View**: Full task detail/edit modal or panel
- **Field Editing**: Edit task name, due date, assignee, status, description
- **Save Changes**: Updates task and refreshes list

#### **Sorting** (Observed):
- **Default Sort**: By due date (most recent first)
- **No-Date Tasks**: Appear at bottom of list
- **Column Sorting**: Headers may be clickable to sort by column
- **Sort Indicators**: Visual indicators for current sort column and direction

#### **Bulk Actions** (Inferred):
- **Selection State**: Selecting multiple tasks triggers action toolbar
- **Actions**: Mark as Done, Delete, Reassign, Change Due Date, etc.
- **Confirmation**: Destructive actions require confirmation

#### **Loan Navigation:**
- **Deep Links**: Clicking loan address navigates to loan detail page
- **Cross-Page Navigation**: Maintains context (breadcrumbs or back button)
- **Related Tasks**: Loan detail page likely shows associated tasks

#### **Pagination** (Observed):
- **Current State**: All 43 tasks visible on single page
- **Load More**: May appear if tasks exceed page limit
- **Infinite Scroll**: Possible alternative to pagination buttons

### 6.2.7 Contacts Page Interactions (Observed)

#### **Filter Navigation:**
- **Button Click**: Switches between "All", "Companies", and "People" views
- **Active State**: Selected filter button visually highlighted
- **Data Filtering**: Filters contact list by entity type (all contacts vs. companies vs. individuals)
- **URL Update**: May update URL query param (e.g., `/admin/contacts?filter=companies`)

#### **Contact List Interactions:**
- **Row Click**: Opens contact detail/edit view (likely in modal, side panel, or route)
- **Name Click**: Opens contact detail view
- **Associated With Link**: Click navigates to associated contact detail
- **Tooltip Interaction**: Hover over associated contacts or owner shows full details
- **Hover**: Visual feedback (background color change, pointer cursor)

#### **Search Functionality:**
- **Input**: Typing triggers search (likely debounced)
- **Real-time Filtering**: Contact list updates as user types
- **Search Scope**: Searches across contact names, companies, types, relationships
- **Clear Search**: Resets to unfiltered list

#### **Add Contacts Button:**
- **Click**: Opens contact creation interface
- **Modal/Form**: Likely opens overlay or form for creating new contact
- **Form Fields**: Name, type (Borrower/Vendor/Investor), company association, owner, status
- **Save/Create**: Creates contact and refreshes list

#### **Export Button:**
- **Click**: Exports contact list to file (CSV/Excel format)
- **Export Scope**: Exports currently filtered/visible contacts
- **Export Columns**: All table columns exported
- **Download**: Triggers file download

#### **Contact Type Filtering** (Inferred):
- **Type Column**: Shows contact type (Borrower/Vendor/Investor)
- **Type Filtering**: Separate routes visible in sidebar for `/admin/borrowers`, `/admin/investors`, `/admin/vendors`
- **Type Switching**: May filter by type within Contacts page or navigate to type-specific pages

#### **Status Management** (Observed):
- **Status Display**: Status badge shows "Draft" or "Active"
- **Status Change**: Likely editable in contact detail view
- **Status Filtering**: May support filtering by status (inferred)

#### **Owner Assignment** (Observed):
- **Owner Display**: Initials shown with tooltip on hover
- **Owner Assignment**: Likely editable in contact detail view
- **Owner Filtering**: May support filtering by owner (inferred)

#### **Relationship Management** (Observed):
- **Bidirectional Links**: Associated contacts are clickable links
- **Relationship Navigation**: Clicking associated contact navigates to that contact
- **Multiple Associations**: "+N" notation indicates additional associated contacts
- **Relationship Editing**: Likely editable in contact detail view

#### **Contact Detail View** (Inferred):
- **Open Contact**: Clicking row or name opens contact detail
- **Full Information**: Shows all contact details, relationships, activity history
- **Edit Mode**: Allows editing all contact fields
- **Relationship Management**: Add/remove associations with other contacts
- **Activity Timeline**: Shows last activity and activity history
- **Actions**: Edit, Delete, Change Status, Assign Owner, etc.

#### **Bulk Actions** (Inferred):
- **Selection**: May support checkbox selection for multiple contacts
- **Bulk Operations**: Export selected, change status, assign owner, delete
- **Action Toolbar**: Appears when contacts selected

#### **Pagination** (Observed):
- **Current State**: Showing 50 of 51 contacts
- **Load More Button**: Loads next batch of contacts
- **Infinite Scroll**: Load more pattern (similar to Inbox)

### 6.2.8 Type-Specific Contact Pages (Borrowers/Investors/Vendors) Interactions

The Borrowers, Investors, and Vendors pages share the same interaction patterns as the Contacts page, with the following differences:

#### **Type-Specific Behavior** (Observed on Borrowers and Investors Pages):
- **Pre-filtered List**: Only contacts of the specified type are displayed
- **No Type Column**: Type column is hidden since all contacts share the same type
- **Type-Specific Button**: "Add Borrower" (or "Add Investor"/"Add Vendor") instead of generic "Add Contacts"
- **Navigation**: Sidebar links provide direct access to each type-specific view
- **Type-Specific Columns**: Each type can have unique columns:
  - **Investors**: Includes "Invested" column (shows investment amounts) - 6 columns
  - **Borrowers**: Standard columns without Type - 5 columns (includes Last Activity and Status)
  - **Vendors**: Completely different column set - 8 columns (Role, Email, Phone, Cash) - No Last Activity or Status
- **Column Configuration**: Component adapts columns based on contact type with significant variations
- **Email/Phone Integration**: Vendors page includes clickable email links and formatted phone numbers

#### **Shared Interactions** (Same as Contacts Page):
- **Filter Navigation**: All/Companies/People filters work the same way
- **Search**: Searches within the filtered type
- **Export**: Exports only the filtered type
- **Contact Detail**: Clicking contacts opens same detail view
- **Relationships**: Associated contacts work the same (may link to contacts of different types)
- **Status Management**: Draft/Active status management identical
- **Owner Assignment**: Same owner/assignee system

#### **Type Switching**:
- **Sidebar Navigation**: Clicking "Borrowers", "Investors", or "Vendors" navigates to type-specific page
- **URL Change**: Route changes to `/admin/borrowers`, `/admin/investors`, or `/admin/vendors`
- **Data Refetch**: Loads contacts filtered by the selected type
- **Component Reuse**: Same component with different type prop/query

#### **Cross-Type Navigation**:
- **Associated Contacts**: Clicking "Associated With" links may navigate to contacts of different types
- **Context Preservation**: May maintain breadcrumb or back navigation context
- **Type Context**: Detail views likely show contact type clearly

### 6.2.9 Quotes Page Interactions (Observed)

#### **Filter Navigation:**
- **Button Click**: Switches between "All" and "Archived" views
- **Active State**: Selected filter button visually highlighted
- **Data Filtering**: Filters quote list by archive status (all quotes vs. archived quotes)
- **URL Update**: May update URL query param (e.g., `/admin/quotes?filter=archived`)

#### **Quote List Interactions:**
- **Row Click**: Opens quote detail/edit view (likely in modal, side panel, or route)
- **Name Click**: Opens quote detail view
- **Borrower Click**: Click navigates to borrower detail/contact page
- **Type Badge**: Visual indicator of loan type
- **Hover**: Visual feedback (background color change, pointer cursor)

#### **Search Functionality:**
- **Input**: Typing triggers search (likely debounced)
- **Real-time Filtering**: Quote list updates as user types
- **Search Scope**: Searches across quote names, borrower names, types, property addresses
- **Clear Search**: Resets to unfiltered list

#### **Add Quote Button:**
- **Click**: Opens quote creation interface
- **Modal/Form**: Likely opens overlay or form for creating new quote
- **Form Fields**: Quote name/property address, type, borrower selection, loan details, terms
- **Save/Create**: Creates quote and refreshes list

#### **Quote Status Management** (Observed):
- **Status Display**: Status badge shows "Draft" (and inferred: Sent, Accepted, Rejected, Archived)
- **Status Change**: Likely editable in quote detail view
- **Status Workflow**: Progression through quote lifecycle (Draft → Sent → Accepted/Rejected → Archived)
- **Archive Action**: Quotes can be archived (separate from status or related)

#### **Quote Detail View** (Inferred):
- **Open Quote**: Clicking row or name opens quote detail
- **Full Information**: Shows all quote details, borrower info, loan terms, pricing
- **Edit Mode**: Allows editing all quote fields
- **Borrower Link**: Click borrower to navigate to borrower detail
- **Actions**: Edit, Delete, Archive, Send to Borrower, Convert to Loan, etc.

#### **Quote Type Filtering** (Inferred):
- **Type Column**: Shows quote type (Bridge + Rehab, Construction)
- **Type Filtering**: May support filtering by quote type
- **Type Badges**: Visual indicators for different loan product types

#### **Borrower Navigation:**
- **Deep Links**: Clicking borrower name navigates to borrower detail page
- **Cross-Page Navigation**: Maintains context (breadcrumbs or back button)
- **Related Quotes**: Borrower detail page likely shows associated quotes

#### **Archive System:**
- **Archive Filter**: "Archived" button shows only archived quotes
- **Archive Action**: Quotes can be archived (likely in detail view or bulk actions)
- **Archive Status**: Separate view for archived quotes

#### **Sorting** (Observed):
- **Default Sort**: By Last Updated date (most recent first)
- **Date Format**: MM/DD/YYYY format
- **Column Sorting**: Headers may be clickable to sort by column
- **Sort Indicators**: Visual indicators for current sort column and direction

#### **Bulk Actions** (Inferred):
- **Selection**: May support checkbox selection for multiple quotes
- **Bulk Operations**: Archive, Delete, Send, Export
- **Action Toolbar**: Appears when quotes selected

#### **Pagination** (Observed):
- **Current State**: All 8 quotes visible on single page
- **Load More**: May appear if quotes exceed page limit
- **Infinite Scroll**: Possible alternative to pagination buttons

### 6.2.10 Pipeline Page Interactions (Observed)

#### **View Toggle:**
- **View Modes**: Two view modes available:
  1. **Pipeline View** (Kanban board) - Visual column-based layout
  2. **Table View** - Tabular data with grouped rows by stage
- **Button State**: Button text changes to indicate current view ("Pipeline View" when in Kanban, "Table View" when in table)
- **View Switching**: Clicking toggle switches between Kanban and table views
- **State Preservation**: Filters, sort, search preserved when switching views
- **URL Update**: May update URL query param (e.g., `/admin/loans?view=kanban` or `/admin/loans?view=table`)
- **Same Data**: Both views display same loan data, different presentation format

#### **Summary Statistics:**
- **Display**: Shows aggregated totals ("24 loans · $6,774,149.00")
- **Real-time Updates**: Updates as loans move between columns or are filtered
- **Calculation**: Sums across all visible loans/columns
- **Filtering Impact**: Statistics update based on active filters

#### **Filter System:**
- **Filter Button**: Opens filter interface/dropdown
- **Filter Criteria**: Likely filters by loan type, borrower, assignee, date range, amount range, status
- **Multi-Filter Support**: Multiple filters can likely be applied simultaneously
- **Column Impact**: Filters affect which loans appear in which columns
- **Visual Indicators**: Active filters likely shown with badges or indicators

#### **Sort System:**
- **Sort Button**: Opens sort options/dropdown
- **Sort Criteria**: Likely sorts by amount, date, borrower, property, assignee
- **Sort Scope**: May sort within columns or across entire board
- **Sort Direction**: Ascending/descending toggle
- **Visual Indicators**: Active sort shown with indicators

#### **Search Functionality:**
- **Input**: Typing triggers search (likely debounced)
- **Real-time Filtering**: Cards update as user types
- **Search Scope**: Searches across property addresses, borrower names, loan types, loan amounts
- **Cross-Column Search**: Searches across all columns simultaneously
- **Clear Search**: Resets to unfiltered view

#### **Kanban Card Interactions:**
- **Card Click**: Opens loan detail view (likely in modal, side panel, or route)
- **Card Hover**: Visual feedback (elevation, border highlight)
- **Drag and Drop**: Cards draggable between columns (changes pipeline stage)
- **Card Selection**: May support multi-select for bulk actions
- **Context Menu**: Right-click or menu button may show actions (Edit, Delete, Move, etc.)

#### **Column Interactions:**
- **Column Headers**: Show stage name, count, and total amount
- **Column Totals**: Calculated dynamically based on cards in column
- **Column Resize**: Columns may be resizable (inferred)
- **Column Reorder**: Columns may be reorderable (inferred)
- **Column Actions**: Column header may have actions (Filter, Sort, etc.)

#### **Drag and Drop Behavior** (Inferred):
- **Card Dragging**: Click and hold to drag card
- **Drop Zones**: Column drop zones highlight on drag over
- **Stage Update**: Dropping card updates loan's pipeline stage
- **API Update**: Drop action triggers API call to update loan stage
- **Visual Feedback**: Drag preview, drop zone highlighting
- **Undo/Redo**: May support undo/redo for drag operations
- **Bulk Move**: Multiple selected cards may be moved together

#### **Loan Detail Navigation:**
- **Open Loan**: Clicking card opens loan detail view
- **Detail View**: Shows full loan information, documents, history
- **Navigation**: Back button or close returns to pipeline
- **Context Preservation**: Maintains pipeline view state on return

#### **Add Loan Button:**
- **Click**: Opens loan creation interface
- **Modal/Form**: Likely opens overlay or form for creating new loan
- **Form Fields**: Property, borrower, loan type, amount, terms, etc.
- **Initial Stage**: New loans likely start in "Lead" column
- **Auto-Refresh**: Pipeline updates after loan creation

#### **Export Functionality:**
- **Export Button**: Exports pipeline data to file (CSV/Excel)
- **Export Scope**: Exports currently filtered/visible loans
- **Export Format**: Likely includes all card data (property, borrower, amount, type, stage, etc.)

#### **Pipeline Stage Workflow:**
- **Stage Progression**: Loans move through stages (Lead → Processing → Underwriting → Closed)
- **Manual Movement**: Drag-and-drop allows manual stage changes
- **Automatic Progression**: Some stages may auto-advance based on conditions
- **Stage Rules**: Business rules may govern stage transitions
- **Stage Actions**: Each stage may have specific actions/requirements

#### **Loan Status Badges:**
- **Status Display**: Additional status badges within stages
- **Status Management**: Status may be editable in loan detail view
- **Status Filtering**: May filter by status badge in addition to stage
- **Status Workflow**: Status badges provide granular state within stages

#### **Bulk Actions** (Inferred):
- **Selection**: May support checkbox selection for multiple loans
- **Bulk Operations**: Move to stage, assign owner, export, delete
- **Action Toolbar**: Appears when loans selected
- **Multi-Column Selection**: Can select loans across multiple columns

#### **Kanban View Interactions:**
- **Drag and Drop**: Cards draggable between columns to change pipeline stage
- **Card Click**: Opens loan detail view
- **Card Hover**: Visual feedback (elevation, border highlight)
- **Column Totals**: Each column shows count and total dollar amount
- **Column Sorting**: Loans within columns may be sortable
- **Column Filtering**: Filtering affects cards within columns
- **Horizontal Scroll**: Additional columns accessible via horizontal scroll
- **Responsive Layout**: Columns may stack or adapt on smaller screens
- **Touch Support**: Drag-and-drop works on touch devices

#### **Table View Interactions:**
- **Row Click**: Clicking row opens loan detail view
- **Row Hover**: Visual feedback (highlight, elevation)
- **Column Sorting**: Clicking column header sorts by that column (ascending/descending)
- **Group Header Click**: Clicking group header (e.g., "Lead 5 $2,485,143.00") likely collapses/expands group
- **Substage Button Click**: Clicking substage status button opens status selection dropdown/modal
- **Owner Tooltip**: Hovering over owner initials shows full name/info
- **Substage Tooltip**: Hovering over substage badge shows status details
- **Row Selection**: Rows selectable for bulk actions (checkbox or click)
- **Table Scrolling**: Vertical scroll when rows exceed viewport height
- **Column Resizing**: Columns resizable via drag handles (inferred)
- **Column Reordering**: Columns reorderable (inferred)
- **Multiple Borrowers**: Table view shows comma-separated borrower list when multiple borrowers exist
- **Editable Fields**: Substage field directly editable via button interaction

#### **View-Specific Features:**
- **Kanban View**: 
  - Drag-and-drop card movement between columns
  - Visual card-based presentation
  - Column-based organization
- **Table View**:
  - Sortable columns
  - Grouped rows by stage
  - More detailed column data
  - Editable substage field
  - Multiple borrower display

### 6.3 Form Interactions

#### **Search/Filter Inputs:**
- **Debounced Search**: Delays API calls while typing
- **Auto-complete**: Suggestions dropdown
- **Clear Button**: X icon to clear input
- **Validation**: Real-time or on blur

#### **Button States:**
- **Default**: Primary styling
- **Hover**: Darker shade or elevation
- **Active/Clicked**: Pressed state
- **Disabled**: Grayed out, non-interactive
- **Loading**: Spinner icon, disabled state

### 6.4 Keyboard Shortcuts
- **Alt+T**: Open notifications (indicated in UI)
- **Common Patterns** (likely implemented):
  - `/` or `Ctrl+K`: Focus search
  - `Esc`: Close modals/dropdowns
  - `Tab`: Navigate between focusable elements
  - Arrow keys: Navigate lists/tables

### 6.5 Real-time Updates
- **Notifications**: Real-time badge count updates
- **Metrics**: May poll or use WebSockets for live data
- **Chat**: Real-time message delivery
- **Collaboration**: Multiple users' actions reflected (if applicable)

### 6.6 Error Handling & Loading States
- **Loading Indicators**: Skeletons, spinners, or progress bars
- **Error Boundaries**: Graceful error display
- **Empty States**: Friendly messages when no data
- **Offline Handling**: Service worker or offline indicator

---

## 7. Technical Stack Recommendations

Based on the architecture analysis, here's a recommended tech stack for implementing a similar application:

### 7.1 Frontend Framework
- **React** (with TypeScript) or **Next.js** (if SSR needed)
- **Vue.js** or **Angular** (alternative options)

### 7.2 Routing
- **React Router v6** (if React)
- **Vue Router** (if Vue)
- **Angular Router** (if Angular)

### 7.3 State Management
- **React Query / TanStack Query** (server state)
- **Zustand** or **Jotai** (lightweight global state)
- **Redux Toolkit** (if complex state needs)

### 7.4 Styling
- **Tailwind CSS** + **shadcn/ui** (recommended for INSPIRE)
- **CSS Modules** (alternative)
- **Styled Components** (CSS-in-JS option)

### 7.5 Charts
- **Recharts** (React)
- **Chart.js** (framework agnostic)
- **ApexCharts** (feature-rich)
- **D3.js** (custom charts)

### 7.6 Forms
- **React Hook Form** + **Zod** (validation)
- **Formik** (alternative)

### 7.7 HTTP Client
- **Axios** or **Fetch API**
- **React Query** (includes data fetching)

### 7.8 Build Tools
- **Vite** (modern, fast)
- **Next.js** (if using Next.js)
- **Webpack** (alternative)

### 7.9 Type Safety
- **TypeScript** (strongly recommended)

### 7.10 Testing
- **Vitest** (unit tests)
- **React Testing Library** (component tests)
- **Playwright** or **Cypress** (E2E tests)

---

## 8. Architecture Recommendations for INSPIRE

### 8.1 Core Principles
1. **Component-Based Architecture**: Reusable, composable components
2. **Separation of Concerns**: Clear boundaries between UI, business logic, and data
3. **Type Safety**: TypeScript throughout
4. **Performance**: Code splitting, lazy loading, memoization
5. **Accessibility**: WCAG compliance, keyboard navigation, screen reader support
6. **Maintainability**: Clear file structure, consistent patterns, documentation

### 8.2 Project Structure (Recommended)
```
inspire/
├── src/
│   ├── components/
│   │   ├── ui/              # shadcn/ui components
│   │   ├── layout/          # AppShell, Sidebar, Header
│   │   ├── dashboard/       # Dashboard-specific components
│   │   └── shared/          # Shared components
│   ├── pages/               # Route pages
│   ├── hooks/               # Custom React hooks
│   ├── lib/                 # Utilities, API client
│   ├── store/               # State management (if needed)
│   ├── types/               # TypeScript types
│   ├── styles/              # Global styles
│   └── App.tsx
├── public/
└── package.json
```

### 8.3 Key Architectural Decisions

#### **Layout System:**
- Implement persistent sidebar with responsive behavior
- Use CSS Grid or Flexbox for layout
- Consider sidebar collapse on mobile

#### **Navigation:**
- Use React Router with nested routes
- Implement active state management
- Add route guards for authentication

#### **Data Fetching:**
- Use React Query for server state
- Implement proper loading and error states
- Consider caching strategies

#### **Component Library:**
- Use shadcn/ui for consistent, customizable components
- Build custom components on top of shadcn/ui base
- Maintain design system tokens

#### **State Management:**
- Use React Query for server state
- Use Context API or Zustand for global UI state
- Use local state (useState) for component-specific state

### 8.4 Performance Optimizations
- **Code Splitting**: Lazy load route components
- **Memoization**: React.memo, useMemo, useCallback where appropriate
- **Image Optimization**: Next.js Image or similar
- **Bundle Size**: Tree shaking, analyze bundle size
- **Caching**: React Query cache, service worker for offline

### 8.5 Security Considerations
- **Authentication**: Secure token storage (httpOnly cookies preferred)
- **Authorization**: Role-based access control (RBAC)
- **XSS Prevention**: Sanitize user input
- **CSRF Protection**: Use CSRF tokens
- **API Security**: Validate and sanitize API responses

---

## 9. Implementation Roadmap (Suggested)

### Phase 1: Foundation
1. Set up project structure (React + TypeScript + Vite)
2. Install and configure routing (React Router)
3. Install and configure styling (Tailwind + shadcn/ui)
4. Create AppShell layout (Sidebar + MainContent)
5. Implement basic navigation structure

### Phase 2: Core Components
1. Build reusable UI components (Card, Button, Input, etc.)
2. Implement navigation components (NavItem, Sidebar)
3. Create layout components (Header, Footer if needed)
4. Set up theme system

### Phase 3: Dashboard
1. Implement Dashboard page
2. Create MetricCard component
3. Integrate chart library
4. Build AI chat widget (if applicable)
5. Implement data fetching with React Query

### Phase 4: Additional Pages
1. Implement other route pages
2. Add forms and validation
3. Implement search/filter functionality
4. Add data tables/lists

### Phase 5: Polish & Optimization
1. Add loading states and error handling
2. Implement responsive design
3. Add animations/transitions
4. Performance optimization
5. Accessibility improvements
6. Testing

---

## 10. Conclusion

The Baseline Software platform demonstrates a well-structured, modern web application architecture suitable for enterprise financial management. Based on observations of the Dashboard, Inbox, and Tasks pages, key takeaways for INSPIRE:

1. **Clear Navigation Hierarchy**: Persistent sidebar with logical grouping, consistent across all pages
2. **Component Reusability**: Consistent UI patterns and reusable components (confirmed across Dashboard and Inbox pages)
3. **Data-Rich Interfaces**: Complex data display patterns (tables, lists, charts) with proper pagination and loading states
4. **Type Safety**: TypeScript recommended for maintainability
5. **Modern Stack**: React, React Router, React Query, Tailwind CSS
6. **Performance**: Code splitting, lazy loading, efficient data fetching (infinite scroll/pagination patterns)
7. **User Experience**: Smooth transitions, loading states, error handling, search functionality
8. **Design System**: Consistent styling, spacing, and component patterns across different page types
9. **Table/List Patterns**: Well-structured data tables with selection, sorting, and filtering capabilities
10. **Multi-tab Interfaces**: Clean tab navigation for filtering/grouping related content
11. **Task Management Patterns**: Status-based workflows, assignee tracking, deep linking to related entities
12. **Filter Systems**: Button-based filters (Tasks) vs. tab-based filters (Inbox) - flexible filtering approaches

By following these architectural patterns and recommendations, INSPIRE can achieve a similar level of sophistication while maintaining code quality, performance, and developer experience. The observed patterns from Dashboard (metrics/charts), Inbox (email tables/lists), and Tasks (task management with status workflows) provide excellent templates for other data-heavy pages in the application.

