# Phase 8: Operational Command Center - Cursor Implementation Task Plan

**Document Version:** 1.0
**Target File:** `inspire-ux.html`
**Last Updated:** January 2026
**Prerequisite:** Phases 1-7 must be complete in the HTML prototype

---

## Overview

This document provides a step-by-step implementation plan for adding Phase 8 (Operational Command Center) to the INSPIRE HTML prototype. Phase 8 enhances the existing dashboard, pipeline, and deal views with comprehensive operational features.

**Phase 8 adds/enhances these core capabilities:**
- Home Dashboard with KPIs, "Needs Attention", and activity feed
- Enhanced Kanban Pipeline with SLA tracking and better deal cards
- Task Management system across all deals
- Activity logging/audit trail
- Global Search (Cmd+K command palette)
- Notification system
- SLA tracking and visualization

---

## TASK 1: Enhance Home Dashboard

### 1.1 Update Dashboard KPI Cards

**Location:** In `#view-dashboard`, update the existing `kpi-grid` section

Replace the existing KPI grid with an enhanced version:

```html
<!-- KPI CARDS - Enhanced for Phase 8 -->
<!-- Layout: Grid (4 cols) -->
<div class="kpi-grid">

    <!-- Active Deals -->
    <article class="kpi-card" onclick="navigateTo('pipeline')">
        <div class="kpi-header">
            <span class="kpi-icon">📊</span>
            <h3>Active Deals</h3>
        </div>
        <span class="kpi-value">47</span>
        <div class="kpi-trend positive">
            <span class="trend-icon">↑</span>
            <span class="trend-value">+5 from last month</span>
        </div>
    </article>

    <!-- Closing This Week -->
    <article class="kpi-card" onclick="filterPipeline('closing_this_week')">
        <div class="kpi-header">
            <span class="kpi-icon">📅</span>
            <h3>Closing This Week</h3>
        </div>
        <span class="kpi-value">5</span>
        <div class="kpi-subtext">
            <span class="at-risk">2 at risk</span>
        </div>
        <span class="kpi-volume">$2.1M Volume</span>
    </article>

    <!-- Pipeline Value -->
    <article class="kpi-card" onclick="navigateTo('pipeline')">
        <div class="kpi-header">
            <span class="kpi-icon">💰</span>
            <h3>Pipeline Value</h3>
        </div>
        <span class="kpi-value">$28.5M</span>
        <div class="kpi-trend positive">
            <span class="trend-icon">↑</span>
            <span class="trend-value">+$2.1M MTD</span>
        </div>
        <div class="kpi-target">Target: $35M</div>
    </article>

    <!-- Closed This Month -->
    <article class="kpi-card">
        <div class="kpi-header">
            <span class="kpi-icon">🎉</span>
            <h3>Closed This Month</h3>
        </div>
        <span class="kpi-value">12</span>
        <span class="kpi-volume">$8.75M</span>
        <div class="kpi-trend positive">
            <span class="trend-icon">↑</span>
            <span class="trend-value">+3 vs last month</span>
        </div>
    </article>

</div>

<!-- Secondary KPI Row -->
<div class="kpi-grid secondary">

    <!-- Average Days to Close -->
    <article class="kpi-card compact">
        <h3>Avg Days to Close</h3>
        <span class="kpi-value">28</span>
        <div class="kpi-trend positive">
            <span>↓ 2 days improvement</span>
        </div>
    </article>

    <!-- Pull-Through Rate -->
    <article class="kpi-card compact">
        <h3>Pull-Through Rate</h3>
        <span class="kpi-value">72%</span>
        <div class="kpi-trend positive">
            <span>↑ 4% from last quarter</span>
        </div>
    </article>

    <!-- SLA Compliance -->
    <article class="kpi-card compact">
        <h3>SLA Compliance</h3>
        <span class="kpi-value">89%</span>
        <div class="kpi-trend positive">
            <span>↑ 3% improvement</span>
        </div>
    </article>

    <!-- My Tasks -->
    <article class="kpi-card compact" onclick="navigateTo('tasks')">
        <h3>My Open Tasks</h3>
        <span class="kpi-value">7</span>
        <div class="kpi-subtext">
            <span class="overdue">3 overdue</span>
        </div>
    </article>

</div>
```

### 1.2 Enhance "Needs Attention" Section

**Location:** In `#view-dashboard`, update the existing "Needs Attention" section

```html
<!-- NEEDS ATTENTION - Enhanced for Phase 8 -->
<section class="dashboard-section needs-attention">
    <header class="section-header">
        <div class="header-left">
            <h2>🔔 Needs Attention</h2>
            <span class="count-badge">8 items</span>
        </div>
        <div class="header-actions">
            <select onchange="filterNeedsAttention(this.value)">
                <option value="all">All Types</option>
                <option value="sla">SLA Issues</option>
                <option value="flags">Red Flags</option>
                <option value="docs">Documents</option>
                <option value="tasks">Tasks</option>
            </select>
            <button onclick="navigateTo('needs-attention')">View All</button>
        </div>
    </header>

    <div class="attention-list">

        <!-- SLA Breach -->
        <article class="attention-item priority-high">
            <div class="attention-icon">⏰</div>
            <div class="attention-content">
                <div class="attention-header">
                    <span class="attention-type sla-breach">SLA Breach</span>
                    <span class="attention-time">2 days overdue</span>
                </div>
                <h4>123 Main St, Austin TX</h4>
                <p>12 days in Processing (SLA: 10 days). Missing appraisal holding up progress.</p>
                <div class="attention-meta">
                    <span class="borrower">ABC Investments LLC</span>
                    <span class="assigned">Assigned: Sarah Johnson</span>
                </div>
            </div>
            <div class="attention-actions">
                <button onclick="navigateToDeal('deal_001', 'checklist')" class="primary-btn">View Checklist</button>
                <button onclick="escalateDeal('deal_001')">Escalate</button>
            </div>
        </article>

        <!-- Quote Expiring -->
        <article class="attention-item priority-high">
            <div class="attention-icon">📋</div>
            <div class="attention-content">
                <div class="attention-header">
                    <span class="attention-type quote-expiring">Quote Expiring</span>
                    <span class="attention-time">Expires in 2 days</span>
                </div>
                <h4>456 Oak Ave, Dallas TX</h4>
                <p>Quote sent 12/10, expires 12/17. Borrower has not responded.</p>
                <div class="attention-meta">
                    <span class="borrower">XYZ Holdings LLC</span>
                    <span class="loan-amount">$525,000</span>
                </div>
            </div>
            <div class="attention-actions">
                <button onclick="sendQuoteReminder('deal_002')" class="primary-btn">Send Reminder</button>
                <button onclick="navigateToDeal('deal_002', 'quotes')">View Quote</button>
            </div>
        </article>

        <!-- Red Flag Unresolved -->
        <article class="attention-item priority-high">
            <div class="attention-icon">🔴</div>
            <div class="attention-content">
                <div class="attention-header">
                    <span class="attention-type red-flag">Red Flag Unresolved</span>
                    <span class="attention-time">3 days open</span>
                </div>
                <h4>789 Pine Rd, Houston TX</h4>
                <p>FICO exception (655 vs 660 min) pending investor approval.</p>
                <div class="attention-meta">
                    <span class="borrower">123 Properties LLC</span>
                    <span class="stage">Stage: Underwriting</span>
                </div>
            </div>
            <div class="attention-actions">
                <button onclick="navigateToDeal('deal_003', 'exceptions')" class="primary-btn">View Exception</button>
                <button onclick="navigateToDeal('deal_003', 'analysis')">View Analysis</button>
            </div>
        </article>

        <!-- Document Expiring -->
        <article class="attention-item priority-medium">
            <div class="attention-icon">📄</div>
            <div class="attention-content">
                <div class="attention-header">
                    <span class="attention-type doc-expiring">Document Expiring</span>
                    <span class="attention-time">Expires in 5 days</span>
                </div>
                <h4>321 Elm St, San Antonio TX</h4>
                <p>Appraisal expires 12/20 (dated 8/22). Need recertification or new appraisal.</p>
                <div class="attention-meta">
                    <span class="borrower">Premier Homes LLC</span>
                    <span class="target-close">Target close: 12/28</span>
                </div>
            </div>
            <div class="attention-actions">
                <button onclick="orderRecertification('deal_004')" class="primary-btn">Order Recert</button>
                <button onclick="navigateToDeal('deal_004', 'documents')">View Docs</button>
            </div>
        </article>

        <!-- Rate Lock Expiring -->
        <article class="attention-item priority-high">
            <div class="attention-icon">🔒</div>
            <div class="attention-content">
                <div class="attention-header">
                    <span class="attention-type rate-lock">Rate Lock Expiring</span>
                    <span class="attention-time">Expires tomorrow</span>
                </div>
                <h4>654 Maple Dr, Austin TX</h4>
                <p>Rate lock expires 12/16. Closing scheduled 12/18. Need extension or expedite close.</p>
                <div class="attention-meta">
                    <span class="borrower">Sunset Properties</span>
                    <span class="rate">Rate: 10.5%</span>
                </div>
            </div>
            <div class="attention-actions">
                <button onclick="extendRateLock('deal_005')" class="primary-btn">Extend Lock</button>
                <button onclick="navigateToDeal('deal_005', 'overview')">View Deal</button>
            </div>
        </article>

        <!-- Task Overdue -->
        <article class="attention-item priority-medium">
            <div class="attention-icon">📋</div>
            <div class="attention-content">
                <div class="attention-header">
                    <span class="attention-type task-overdue">Task Overdue</span>
                    <span class="attention-time">1 day overdue</span>
                </div>
                <h4>987 Cedar Ln, Dallas TX</h4>
                <p>Task: "Review and approve credit memo" was due 12/14.</p>
                <div class="attention-meta">
                    <span class="assigned-to">Assigned to: Mike Chen</span>
                    <span class="created-by">Created by: Sarah Johnson</span>
                </div>
            </div>
            <div class="attention-actions">
                <button onclick="completeTask('task_001')" class="primary-btn">Complete Task</button>
                <button onclick="reassignTask('task_001')">Reassign</button>
            </div>
        </article>

        <!-- Stale Deal -->
        <article class="attention-item priority-low">
            <div class="attention-icon">💤</div>
            <div class="attention-content">
                <div class="attention-header">
                    <span class="attention-type stale">No Activity</span>
                    <span class="attention-time">6 days inactive</span>
                </div>
                <h4>543 Birch Blvd, Fort Worth TX</h4>
                <p>No activity since 12/9. Deal in Application stage.</p>
                <div class="attention-meta">
                    <span class="borrower">Oak Tree Investments</span>
                    <span class="stage">Stage: Application</span>
                </div>
            </div>
            <div class="attention-actions">
                <button onclick="addNote('deal_007')" class="primary-btn">Add Note</button>
                <button onclick="archiveDeal('deal_007')">Archive</button>
            </div>
        </article>

    </div>
</section>
```

### 1.3 Add Tasks Due Today Section

**Location:** In `#view-dashboard`, update the existing "My Tasks" section

```html
<!-- MY TASKS DUE TODAY - Enhanced for Phase 8 -->
<section class="dashboard-section tasks-today">
    <header class="section-header">
        <div class="header-left">
            <h2>📋 My Tasks Due Today</h2>
            <span class="count-badge">7 tasks</span>
        </div>
        <div class="header-actions">
            <button onclick="showQuickTaskModal()">+ Add Task</button>
            <button onclick="navigateTo('tasks')">View All Tasks</button>
        </div>
    </header>

    <div class="tasks-list">

        <!-- Task 1: High Priority -->
        <article class="task-item priority-high">
            <div class="task-checkbox">
                <input type="checkbox" id="task_001" onchange="toggleTask('task_001')">
            </div>
            <div class="task-content">
                <label for="task_001">Review appraisal and update sizing - 123 Main St</label>
                <div class="task-meta">
                    <span class="task-deal" onclick="navigateToDeal('deal_001', 'overview')">123 Main St, Austin TX</span>
                    <span class="task-due">Due: Today 5:00 PM</span>
                    <span class="task-priority high">High</span>
                </div>
            </div>
            <div class="task-actions">
                <button onclick="completeTask('task_001')">Complete</button>
            </div>
        </article>

        <!-- Task 2: High Priority -->
        <article class="task-item priority-high">
            <div class="task-checkbox">
                <input type="checkbox" id="task_002" onchange="toggleTask('task_002')">
            </div>
            <div class="task-content">
                <label for="task_002">Send closing instructions to title - 456 Oak Ave</label>
                <div class="task-meta">
                    <span class="task-deal" onclick="navigateToDeal('deal_002', 'overview')">456 Oak Ave, Dallas TX</span>
                    <span class="task-due">Due: Today 3:00 PM</span>
                    <span class="task-priority high">High</span>
                </div>
            </div>
            <div class="task-actions">
                <button onclick="completeTask('task_002')">Complete</button>
            </div>
        </article>

        <!-- Task 3: Medium Priority -->
        <article class="task-item priority-medium">
            <div class="task-checkbox">
                <input type="checkbox" id="task_003" onchange="toggleTask('task_003')">
            </div>
            <div class="task-content">
                <label for="task_003">Follow up with borrower on missing bank statements</label>
                <div class="task-meta">
                    <span class="task-deal" onclick="navigateToDeal('deal_003', 'overview')">789 Pine Rd, Houston TX</span>
                    <span class="task-due">Due: Today EOD</span>
                    <span class="task-priority medium">Medium</span>
                </div>
            </div>
            <div class="task-actions">
                <button onclick="completeTask('task_003')">Complete</button>
            </div>
        </article>

        <!-- Task 4: Overdue -->
        <article class="task-item priority-high overdue">
            <div class="task-checkbox">
                <input type="checkbox" id="task_004" onchange="toggleTask('task_004')">
            </div>
            <div class="task-content">
                <label for="task_004">Submit exception request for LTV variance</label>
                <div class="task-meta">
                    <span class="task-deal" onclick="navigateToDeal('deal_004', 'overview')">321 Elm St, San Antonio TX</span>
                    <span class="task-due overdue">Overdue: Was due yesterday</span>
                    <span class="task-priority high">High</span>
                </div>
            </div>
            <div class="task-actions">
                <button onclick="completeTask('task_004')">Complete</button>
            </div>
        </article>

        <!-- Task 5: Medium Priority -->
        <article class="task-item priority-medium">
            <div class="task-checkbox">
                <input type="checkbox" id="task_005" onchange="toggleTask('task_005')">
            </div>
            <div class="task-content">
                <label for="task_005">Order title update for 654 Maple Dr</label>
                <div class="task-meta">
                    <span class="task-deal" onclick="navigateToDeal('deal_005', 'overview')">654 Maple Dr, Austin TX</span>
                    <span class="task-due">Due: Today</span>
                    <span class="task-priority medium">Medium</span>
                </div>
            </div>
            <div class="task-actions">
                <button onclick="completeTask('task_005')">Complete</button>
            </div>
        </article>

    </div>
</section>
```

### 1.4 Add Pipeline Overview Chart

**Location:** In `#view-dashboard`, add after tasks section

```html
<!-- PIPELINE BY STAGE - Phase 8 -->
<section class="dashboard-section pipeline-overview">
    <header class="section-header">
        <div class="header-left">
            <h2>📊 Pipeline by Stage</h2>
        </div>
        <div class="header-actions">
            <button onclick="navigateTo('pipeline')">View Pipeline</button>
        </div>
    </header>

    <div class="pipeline-chart">
        <!-- Horizontal bar chart representation -->
        <div class="pipeline-stage-row">
            <div class="stage-label">
                <span class="stage-name">Prospect</span>
                <span class="stage-count">8 deals</span>
            </div>
            <div class="stage-bar-container">
                <div class="stage-bar" style="width: 40%;">
                    <span class="stage-volume">$4.8M</span>
                </div>
                <span class="at-risk-indicator" title="1 at risk">1 ⚠️</span>
            </div>
        </div>

        <div class="pipeline-stage-row">
            <div class="stage-label">
                <span class="stage-name">Application</span>
                <span class="stage-count">12 deals</span>
            </div>
            <div class="stage-bar-container">
                <div class="stage-bar" style="width: 60%;">
                    <span class="stage-volume">$7.2M</span>
                </div>
                <span class="at-risk-indicator" title="2 at risk">2 ⚠️</span>
            </div>
        </div>

        <div class="pipeline-stage-row">
            <div class="stage-label">
                <span class="stage-name">Quote</span>
                <span class="stage-count">6 deals</span>
            </div>
            <div class="stage-bar-container">
                <div class="stage-bar" style="width: 30%;">
                    <span class="stage-volume">$3.6M</span>
                </div>
            </div>
        </div>

        <div class="pipeline-stage-row">
            <div class="stage-label">
                <span class="stage-name">Initial UW</span>
                <span class="stage-count">5 deals</span>
            </div>
            <div class="stage-bar-container">
                <div class="stage-bar" style="width: 25%;">
                    <span class="stage-volume">$3.0M</span>
                </div>
            </div>
        </div>

        <div class="pipeline-stage-row">
            <div class="stage-label">
                <span class="stage-name">Processing</span>
                <span class="stage-count">10 deals</span>
            </div>
            <div class="stage-bar-container">
                <div class="stage-bar" style="width: 50%;">
                    <span class="stage-volume">$6.0M</span>
                </div>
                <span class="at-risk-indicator breach" title="3 at risk">3 🔴</span>
            </div>
        </div>

        <div class="pipeline-stage-row">
            <div class="stage-label">
                <span class="stage-name">Underwriting</span>
                <span class="stage-count">7 deals</span>
            </div>
            <div class="stage-bar-container">
                <div class="stage-bar" style="width: 35%;">
                    <span class="stage-volume">$4.2M</span>
                </div>
                <span class="at-risk-indicator" title="1 at risk">1 ⚠️</span>
            </div>
        </div>

        <div class="pipeline-stage-row">
            <div class="stage-label">
                <span class="stage-name">Closing</span>
                <span class="stage-count">4 deals</span>
            </div>
            <div class="stage-bar-container">
                <div class="stage-bar closing" style="width: 20%;">
                    <span class="stage-volume">$2.4M</span>
                </div>
            </div>
        </div>
    </div>

    <!-- SLA Summary -->
    <div class="sla-summary">
        <h4>SLA Performance</h4>
        <div class="sla-metrics">
            <div class="sla-metric">
                <span class="sla-label">On Track</span>
                <span class="sla-value success">37 deals (79%)</span>
            </div>
            <div class="sla-metric">
                <span class="sla-label">At Risk</span>
                <span class="sla-value warning">7 deals (15%)</span>
            </div>
            <div class="sla-metric">
                <span class="sla-label">Breached</span>
                <span class="sla-value error">3 deals (6%)</span>
            </div>
        </div>
    </div>
</section>
```

### 1.5 Add Recent Activity Feed

**Location:** In `#view-dashboard`, add after pipeline overview

```html
<!-- RECENT ACTIVITY - Phase 8 -->
<section class="dashboard-section recent-activity">
    <header class="section-header">
        <div class="header-left">
            <h2>📈 Recent Activity</h2>
        </div>
        <div class="header-actions">
            <button onclick="navigateTo('activity')">View All Activity</button>
        </div>
    </header>

    <div class="activity-feed">

        <!-- Activity: Document Upload -->
        <article class="activity-item">
            <div class="activity-avatar">
                <span class="avatar">JS</span>
            </div>
            <div class="activity-content">
                <p>
                    <strong>John Smith</strong> uploaded
                    <span class="activity-object">Appraisal_123_Main_St.pdf</span>
                </p>
                <div class="activity-meta">
                    <span class="activity-deal" onclick="navigateToDeal('deal_001', 'documents')">123 Main St, Austin TX</span>
                    <span class="activity-time">10 minutes ago</span>
                </div>
            </div>
        </article>

        <!-- Activity: Stage Change -->
        <article class="activity-item">
            <div class="activity-avatar">
                <span class="avatar">SJ</span>
            </div>
            <div class="activity-content">
                <p>
                    <strong>Sarah Johnson</strong> moved
                    <span class="activity-object">456 Oak Ave</span>
                    to <span class="activity-stage">Closing</span>
                </p>
                <div class="activity-meta">
                    <span class="activity-deal" onclick="navigateToDeal('deal_002', 'overview')">456 Oak Ave, Dallas TX</span>
                    <span class="activity-time">25 minutes ago</span>
                </div>
            </div>
        </article>

        <!-- Activity: Credit Memo Generated -->
        <article class="activity-item">
            <div class="activity-avatar system">
                <span class="avatar">🤖</span>
            </div>
            <div class="activity-content">
                <p>
                    <strong>System</strong> generated
                    <span class="activity-object">Credit Memo</span>
                    for 789 Pine Rd
                </p>
                <div class="activity-meta">
                    <span class="activity-deal" onclick="navigateToDeal('deal_003', 'credit-memo')">789 Pine Rd, Houston TX</span>
                    <span class="activity-time">45 minutes ago</span>
                </div>
            </div>
        </article>

        <!-- Activity: Quote Sent -->
        <article class="activity-item">
            <div class="activity-avatar">
                <span class="avatar">MC</span>
            </div>
            <div class="activity-content">
                <p>
                    <strong>Mike Chen</strong> sent
                    <span class="activity-object">Quote</span>
                    to borrower for 321 Elm St
                </p>
                <div class="activity-meta">
                    <span class="activity-deal" onclick="navigateToDeal('deal_004', 'quotes')">321 Elm St, San Antonio TX</span>
                    <span class="activity-time">1 hour ago</span>
                </div>
            </div>
        </article>

        <!-- Activity: Exception Approved -->
        <article class="activity-item">
            <div class="activity-avatar">
                <span class="avatar">LP</span>
            </div>
            <div class="activity-content">
                <p>
                    <strong>Lisa Park</strong> approved
                    <span class="activity-object">FICO Exception</span>
                    for 654 Maple Dr
                </p>
                <div class="activity-meta">
                    <span class="activity-deal" onclick="navigateToDeal('deal_005', 'exceptions')">654 Maple Dr, Austin TX</span>
                    <span class="activity-time">2 hours ago</span>
                </div>
            </div>
        </article>

        <!-- Activity: Deal Funded -->
        <article class="activity-item celebration">
            <div class="activity-avatar">
                <span class="avatar">🎉</span>
            </div>
            <div class="activity-content">
                <p>
                    <span class="activity-object">987 Cedar Ln</span>
                    has been <strong>funded</strong>!
                    <span class="funded-amount">$425,000</span>
                </p>
                <div class="activity-meta">
                    <span class="activity-deal" onclick="navigateToDeal('deal_006', 'overview')">987 Cedar Ln, Dallas TX</span>
                    <span class="activity-time">Yesterday 4:30 PM</span>
                </div>
            </div>
        </article>

    </div>
</section>
```

---

## TASK 2: Enhance Pipeline Board

### 2.1 Update Pipeline Header with Enhanced Filters

**Location:** In `#view-pipeline`, update the header section

```html
<!-- PIPELINE HEADER - Enhanced for Phase 8 -->
<header class="view-header pipeline-header">
    <div class="header-title-row">
        <h1>Pipeline</h1>
        <div class="pipeline-summary">
            <span class="summary-stat">47 Active Deals</span>
            <span class="summary-stat">$28.5M Total</span>
        </div>
    </div>

    <!-- FILTERS - Enhanced -->
    <div class="pipeline-toolbar">
        <div class="filter-group">
            <select id="filter-loan-type" onchange="applyFilters()">
                <option value="all">All Loan Types</option>
                <option value="fix_flip">Fix & Flip</option>
                <option value="ground_up">Ground-Up Construction</option>
                <option value="bridge">Bridge</option>
                <option value="dscr">DSCR</option>
            </select>

            <select id="filter-investor" onchange="applyFilters()">
                <option value="all">All Investors</option>
                <option value="eastview">Eastview</option>
                <option value="archwest">ArchWest</option>
            </select>

            <select id="filter-assigned" onchange="applyFilters()">
                <option value="all">All Assignees</option>
                <option value="mine">My Deals</option>
                <option value="user_001">Sarah Johnson</option>
                <option value="user_002">Mike Chen</option>
                <option value="user_003">Lisa Park</option>
            </select>

            <select id="filter-sla" onchange="applyFilters()">
                <option value="all">All SLA Status</option>
                <option value="on_track">On Track</option>
                <option value="at_risk">At Risk</option>
                <option value="breached">SLA Breached</option>
            </select>

            <select id="filter-flags" onchange="applyFilters()">
                <option value="all">All Flag Status</option>
                <option value="has_red">Has Red Flags</option>
                <option value="has_yellow">Has Yellow Flags</option>
                <option value="clean">No Flags</option>
            </select>
        </div>

        <div class="sort-group">
            <label>Sort by:</label>
            <select id="sort-by" onchange="sortPipeline()">
                <option value="updated">Last Updated</option>
                <option value="close_date">Target Close Date</option>
                <option value="amount_desc">Loan Amount (High to Low)</option>
                <option value="amount_asc">Loan Amount (Low to High)</option>
                <option value="days_in_stage">Days in Stage</option>
                <option value="created">Date Created</option>
            </select>
        </div>

        <div class="view-toggle">
            <button class="active" onclick="setPipelineView('kanban')">Kanban</button>
            <button onclick="setPipelineView('table')">Table</button>
        </div>

        <button onclick="showModal('modal-new-deal')" class="primary-btn">+ New Deal</button>
    </div>
</header>
```

### 2.2 Update Kanban Stages with Initial UW Stage

**Location:** In `#view-pipeline`, update the Kanban board

```html
<!-- KANBAN BOARD - Enhanced for Phase 8 -->
<div class="kanban-board">

    <!-- STAGE: PROSPECT -->
    <div class="kanban-column" data-stage="prospect">
        <header>
            <div class="stage-header">
                <h3>Prospect</h3>
                <span class="stage-count">8</span>
            </div>
            <span class="stage-volume">$4.8M</span>
            <div class="stage-sla">
                <span class="sla-target">SLA: 5 days</span>
                <span class="sla-at-risk">1 at risk</span>
            </div>
        </header>
        <div class="kanban-cards" ondragover="allowDrop(event)" ondrop="dropDeal(event, 'prospect')">
            <!-- Deal cards inserted here -->
        </div>
    </div>

    <!-- STAGE: APPLICATION -->
    <div class="kanban-column" data-stage="application">
        <header>
            <div class="stage-header">
                <h3>Application</h3>
                <span class="stage-count">12</span>
            </div>
            <span class="stage-volume">$7.2M</span>
            <div class="stage-sla">
                <span class="sla-target">SLA: 7 days</span>
                <span class="sla-at-risk">2 at risk</span>
            </div>
        </header>
        <div class="kanban-cards" ondragover="allowDrop(event)" ondrop="dropDeal(event, 'application')">
            <!-- Deal cards -->
        </div>
    </div>

    <!-- STAGE: QUOTE -->
    <div class="kanban-column" data-stage="quote">
        <header>
            <div class="stage-header">
                <h3>Quote</h3>
                <span class="stage-count">6</span>
            </div>
            <span class="stage-volume">$3.6M</span>
            <div class="stage-sla">
                <span class="sla-target">SLA: 3 days</span>
            </div>
        </header>
        <div class="kanban-cards" ondragover="allowDrop(event)" ondrop="dropDeal(event, 'quote')">
            <!-- Deal cards -->
        </div>
    </div>

    <!-- STAGE: INITIAL UW (NEW) -->
    <div class="kanban-column" data-stage="initial_uw">
        <header>
            <div class="stage-header">
                <h3>Initial UW</h3>
                <span class="stage-count">5</span>
            </div>
            <span class="stage-volume">$3.0M</span>
            <div class="stage-sla">
                <span class="sla-target">SLA: 5 days</span>
            </div>
        </header>
        <div class="kanban-cards" ondragover="allowDrop(event)" ondrop="dropDeal(event, 'initial_uw')">
            <!-- Deal cards -->
        </div>
    </div>

    <!-- STAGE: PROCESSING -->
    <div class="kanban-column" data-stage="processing">
        <header>
            <div class="stage-header">
                <h3>Processing</h3>
                <span class="stage-count">10</span>
            </div>
            <span class="stage-volume">$6.0M</span>
            <div class="stage-sla">
                <span class="sla-target">SLA: 10 days</span>
                <span class="sla-breached">3 breached</span>
            </div>
        </header>
        <div class="kanban-cards" ondragover="allowDrop(event)" ondrop="dropDeal(event, 'processing')">

            <!-- Sample Deal Card with full Phase 8 details -->
            <article class="deal-card state-warning"
                     draggable="true"
                     ondragstart="dragDeal(event, 'deal_001')"
                     onclick="navigateToDeal('deal_001', 'overview')">

                <div class="card-header">
                    <span class="address">123 Main St</span>
                    <div class="card-badges">
                        <span class="badge loan-type">F&F</span>
                        <span class="badge investor">Eastview</span>
                    </div>
                </div>

                <div class="card-body">
                    <div class="metrics-row">
                        <span class="loan-amount">$382,500</span>
                        <span class="metric">75% LTC</span>
                        <span class="metric">65% LTV</span>
                    </div>
                    <div class="borrower-row">
                        <span class="borrower">ABC Investments LLC</span>
                    </div>
                </div>

                <div class="card-indicators">
                    <div class="flags-row">
                        <span class="flag-indicator red" title="1 Red Flag">🔴 1</span>
                        <span class="flag-indicator yellow" title="2 Yellow Flags">⚠️ 2</span>
                    </div>
                    <div class="tasks-row">
                        <span class="tasks" title="3 open tasks">📋 3</span>
                    </div>
                </div>

                <div class="card-footer">
                    <div class="sla-indicator at-risk">
                        <span class="days">⏱️ 8 days</span>
                        <span class="status">At Risk</span>
                    </div>
                    <div class="target-close">
                        <span>📅 Dec 20</span>
                    </div>
                </div>

                <div class="card-assignee">
                    <span class="avatar" title="Sarah Johnson">SJ</span>
                </div>

                <div class="card-quick-actions">
                    <button onclick="event.stopPropagation(); showQuickActions('deal_001')">⋮</button>
                </div>
            </article>

        </div>
    </div>

    <!-- STAGE: UNDERWRITING -->
    <div class="kanban-column" data-stage="underwriting">
        <header>
            <div class="stage-header">
                <h3>Underwriting</h3>
                <span class="stage-count">7</span>
            </div>
            <span class="stage-volume">$4.2M</span>
            <div class="stage-sla">
                <span class="sla-target">SLA: 7 days</span>
                <span class="sla-at-risk">1 at risk</span>
            </div>
        </header>
        <div class="kanban-cards" ondragover="allowDrop(event)" ondrop="dropDeal(event, 'underwriting')">

            <!-- Sample DSCR Deal Card -->
            <article class="deal-card"
                     draggable="true"
                     ondragstart="dragDeal(event, 'deal_002')"
                     onclick="navigateToDeal('deal_002', 'overview')">

                <div class="card-header">
                    <span class="address">456 Oak Ave</span>
                    <div class="card-badges">
                        <span class="badge loan-type dscr">DSCR</span>
                        <span class="badge investor">ArchWest</span>
                    </div>
                </div>

                <div class="card-body">
                    <div class="metrics-row">
                        <span class="loan-amount">$525,000</span>
                        <span class="metric">75% LTV</span>
                        <span class="metric">1.35x DSCR</span>
                    </div>
                    <div class="borrower-row">
                        <span class="borrower">XYZ Holdings LLC</span>
                    </div>
                </div>

                <div class="card-indicators">
                    <div class="flags-row">
                        <span class="flag-indicator yellow" title="1 Yellow Flag">⚠️ 1</span>
                    </div>
                    <div class="memo-status">
                        <span class="memo-ready" title="Credit Memo Ready">📋 Memo Ready</span>
                    </div>
                </div>

                <div class="card-footer">
                    <div class="sla-indicator on-track">
                        <span class="days">⏱️ 3 days</span>
                        <span class="status">On Track</span>
                    </div>
                    <div class="target-close">
                        <span>📅 Dec 22</span>
                    </div>
                </div>

                <div class="card-assignee">
                    <span class="avatar" title="Mike Chen">MC</span>
                </div>
            </article>

        </div>
    </div>

    <!-- STAGE: CLOSING -->
    <div class="kanban-column" data-stage="closing">
        <header>
            <div class="stage-header">
                <h3>Closing</h3>
                <span class="stage-count">4</span>
            </div>
            <span class="stage-volume">$2.4M</span>
            <div class="stage-sla">
                <span class="sla-target">SLA: 5 days</span>
            </div>
        </header>
        <div class="kanban-cards" ondragover="allowDrop(event)" ondrop="dropDeal(event, 'closing')">
            <!-- Deal cards -->
        </div>
    </div>

    <!-- STAGE: FUNDED -->
    <div class="kanban-column" data-stage="funded">
        <header>
            <div class="stage-header">
                <h3>Funded</h3>
                <span class="stage-count">156</span>
            </div>
            <span class="stage-volume">$87.5M</span>
        </header>
        <div class="kanban-cards funded-cards">
            <p class="funded-summary">156 loans funded this year</p>
            <button onclick="viewFundedDeals()">View Funded Deals</button>
        </div>
    </div>

</div>
```

### 2.3 Add Quick Actions Dropdown

**Location:** Add after the Kanban board

```html
<!-- QUICK ACTIONS DROPDOWN - Phase 8 -->
<div id="quick-actions-dropdown" class="quick-actions-dropdown" style="display:none;">
    <div class="dropdown-header">
        <span class="deal-address">123 Main St</span>
        <button onclick="hideQuickActions()">×</button>
    </div>
    <ul class="dropdown-menu">
        <li onclick="quickAction('view')">
            <span class="action-icon">👁️</span>
            <span>View Deal</span>
        </li>
        <li onclick="quickAction('add_task')">
            <span class="action-icon">📋</span>
            <span>Add Task</span>
        </li>
        <li onclick="quickAction('add_note')">
            <span class="action-icon">📝</span>
            <span>Add Note</span>
        </li>
        <li onclick="quickAction('send_reminder')">
            <span class="action-icon">📧</span>
            <span>Send Reminder</span>
        </li>
        <li class="separator"></li>
        <li onclick="quickAction('move_stage')">
            <span class="action-icon">➡️</span>
            <span>Move to Stage...</span>
        </li>
        <li onclick="quickAction('reassign')">
            <span class="action-icon">👤</span>
            <span>Reassign</span>
        </li>
        <li class="separator"></li>
        <li onclick="quickAction('archive')" class="danger">
            <span class="action-icon">🗄️</span>
            <span>Archive Deal</span>
        </li>
    </ul>
</div>
```

---

## TASK 3: Add Task Manager View

### 3.1 Add Tasks Navigation Item

**Location:** In `#main-nav`, add Tasks to navigation

```html
<li><button onclick="navigateTo('tasks')">Tasks</button></li>
```

### 3.2 Create Tasks View

**Location:** Add new view section in `#main-content`

```html
<!-- VIEW: TASK MANAGER (Route: /tasks) - Phase 8 -->
<section id="view-tasks" class="view-section" style="display:none;">
    <header class="view-header">
        <div class="header-title-row">
            <h1>Task Manager</h1>
            <button onclick="showQuickTaskModal()" class="primary-btn">+ New Task</button>
        </div>

        <div class="task-toolbar">
            <!-- Tabs -->
            <div class="task-tabs">
                <button class="active" onclick="filterTasks('my')">My Tasks (7)</button>
                <button onclick="filterTasks('all')">All Tasks (24)</button>
                <button onclick="filterTasks('overdue')">Overdue (3)</button>
                <button onclick="filterTasks('completed')">Completed</button>
            </div>

            <!-- Filters -->
            <div class="task-filters">
                <select onchange="filterTasksBy('priority', this.value)">
                    <option value="all">All Priorities</option>
                    <option value="high">High</option>
                    <option value="medium">Medium</option>
                    <option value="low">Low</option>
                </select>

                <select onchange="filterTasksBy('category', this.value)">
                    <option value="all">All Categories</option>
                    <option value="follow_up">Follow Up</option>
                    <option value="document_request">Document Request</option>
                    <option value="review">Review</option>
                    <option value="approval">Approval</option>
                    <option value="closing">Closing</option>
                </select>

                <select onchange="filterTasksBy('assignee', this.value)">
                    <option value="all">All Assignees</option>
                    <option value="user_001">Sarah Johnson</option>
                    <option value="user_002">Mike Chen</option>
                    <option value="user_003">Lisa Park</option>
                </select>
            </div>
        </div>
    </header>

    <!-- Task List -->
    <div class="task-manager-content">

        <!-- Overdue Section -->
        <section class="task-group overdue">
            <h3 class="task-group-header">
                <span class="group-icon">🔴</span>
                Overdue (3)
            </h3>
            <div class="task-list">

                <article class="task-card overdue">
                    <div class="task-checkbox">
                        <input type="checkbox" id="task_overdue_1">
                    </div>
                    <div class="task-main">
                        <div class="task-header">
                            <label for="task_overdue_1" class="task-title">Submit exception request for LTV variance</label>
                            <span class="task-priority high">High</span>
                        </div>
                        <div class="task-details">
                            <span class="task-deal" onclick="navigateToDeal('deal_004', 'overview')">
                                📍 321 Elm St, San Antonio TX
                            </span>
                            <span class="task-category">Approval</span>
                        </div>
                        <div class="task-meta">
                            <span class="task-due overdue">Due: Yesterday</span>
                            <span class="task-assignee">
                                <span class="avatar">SJ</span> Sarah Johnson
                            </span>
                        </div>
                    </div>
                    <div class="task-actions">
                        <button onclick="completeTask('task_overdue_1')">Complete</button>
                        <button onclick="editTask('task_overdue_1')">Edit</button>
                    </div>
                </article>

                <article class="task-card overdue">
                    <div class="task-checkbox">
                        <input type="checkbox" id="task_overdue_2">
                    </div>
                    <div class="task-main">
                        <div class="task-header">
                            <label for="task_overdue_2" class="task-title">Follow up on missing contractor license</label>
                            <span class="task-priority medium">Medium</span>
                        </div>
                        <div class="task-details">
                            <span class="task-deal" onclick="navigateToDeal('deal_008', 'overview')">
                                📍 876 Walnut Ave, Houston TX
                            </span>
                            <span class="task-category">Document Request</span>
                        </div>
                        <div class="task-meta">
                            <span class="task-due overdue">Due: 2 days ago</span>
                            <span class="task-assignee">
                                <span class="avatar">MC</span> Mike Chen
                            </span>
                        </div>
                    </div>
                    <div class="task-actions">
                        <button onclick="completeTask('task_overdue_2')">Complete</button>
                        <button onclick="editTask('task_overdue_2')">Edit</button>
                    </div>
                </article>

            </div>
        </section>

        <!-- Due Today Section -->
        <section class="task-group due-today">
            <h3 class="task-group-header">
                <span class="group-icon">📅</span>
                Due Today (4)
            </h3>
            <div class="task-list">

                <article class="task-card">
                    <div class="task-checkbox">
                        <input type="checkbox" id="task_today_1">
                    </div>
                    <div class="task-main">
                        <div class="task-header">
                            <label for="task_today_1" class="task-title">Review appraisal and update sizing</label>
                            <span class="task-priority high">High</span>
                        </div>
                        <div class="task-details">
                            <span class="task-deal" onclick="navigateToDeal('deal_001', 'overview')">
                                📍 123 Main St, Austin TX
                            </span>
                            <span class="task-category">Review</span>
                        </div>
                        <div class="task-meta">
                            <span class="task-due">Due: Today 5:00 PM</span>
                            <span class="task-assignee">
                                <span class="avatar">SJ</span> Sarah Johnson
                            </span>
                        </div>
                    </div>
                    <div class="task-actions">
                        <button onclick="completeTask('task_today_1')">Complete</button>
                        <button onclick="editTask('task_today_1')">Edit</button>
                    </div>
                </article>

                <article class="task-card">
                    <div class="task-checkbox">
                        <input type="checkbox" id="task_today_2">
                    </div>
                    <div class="task-main">
                        <div class="task-header">
                            <label for="task_today_2" class="task-title">Send closing instructions to title</label>
                            <span class="task-priority high">High</span>
                        </div>
                        <div class="task-details">
                            <span class="task-deal" onclick="navigateToDeal('deal_002', 'overview')">
                                📍 456 Oak Ave, Dallas TX
                            </span>
                            <span class="task-category">Closing</span>
                        </div>
                        <div class="task-meta">
                            <span class="task-due">Due: Today 3:00 PM</span>
                            <span class="task-assignee">
                                <span class="avatar">MC</span> Mike Chen
                            </span>
                        </div>
                    </div>
                    <div class="task-actions">
                        <button onclick="completeTask('task_today_2')">Complete</button>
                        <button onclick="editTask('task_today_2')">Edit</button>
                    </div>
                </article>

            </div>
        </section>

        <!-- Upcoming Section -->
        <section class="task-group upcoming">
            <h3 class="task-group-header">
                <span class="group-icon">📆</span>
                Upcoming (5)
            </h3>
            <div class="task-list">

                <article class="task-card">
                    <div class="task-checkbox">
                        <input type="checkbox" id="task_upcoming_1">
                    </div>
                    <div class="task-main">
                        <div class="task-header">
                            <label for="task_upcoming_1" class="task-title">Order updated title commitment</label>
                            <span class="task-priority medium">Medium</span>
                        </div>
                        <div class="task-details">
                            <span class="task-deal" onclick="navigateToDeal('deal_005', 'overview')">
                                📍 654 Maple Dr, Austin TX
                            </span>
                            <span class="task-category">Document Request</span>
                        </div>
                        <div class="task-meta">
                            <span class="task-due">Due: Tomorrow</span>
                            <span class="task-assignee">
                                <span class="avatar">LP</span> Lisa Park
                            </span>
                        </div>
                    </div>
                    <div class="task-actions">
                        <button onclick="completeTask('task_upcoming_1')">Complete</button>
                        <button onclick="editTask('task_upcoming_1')">Edit</button>
                    </div>
                </article>

            </div>
        </section>

    </div>
</section>
```

### 3.3 Add Quick Task Modal

**Location:** Add to modals section

```html
<!-- MODAL: QUICK TASK - Phase 8 -->
<div id="modal-quick-task" class="modal" style="display:none;">
    <div class="modal-overlay" onclick="closeModal('modal-quick-task')"></div>
    <div class="modal-content">
        <header class="modal-header">
            <h2>Create Task</h2>
            <button onclick="closeModal('modal-quick-task')" class="close-btn">×</button>
        </header>

        <div class="modal-body">
            <form class="task-form">

                <div class="form-group">
                    <label for="task-title">Task Title *</label>
                    <input type="text" id="task-title" placeholder="What needs to be done?" required>
                </div>

                <div class="form-group">
                    <label for="task-description">Description</label>
                    <textarea id="task-description" rows="3" placeholder="Add details..."></textarea>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="task-deal">Related Deal</label>
                        <select id="task-deal">
                            <option value="">No deal selected</option>
                            <option value="deal_001">123 Main St, Austin TX</option>
                            <option value="deal_002">456 Oak Ave, Dallas TX</option>
                            <option value="deal_003">789 Pine Rd, Houston TX</option>
                            <option value="deal_004">321 Elm St, San Antonio TX</option>
                            <option value="deal_005">654 Maple Dr, Austin TX</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="task-assign">Assign To *</label>
                        <select id="task-assign" required>
                            <option value="user_001">Sarah Johnson</option>
                            <option value="user_002">Mike Chen</option>
                            <option value="user_003">Lisa Park</option>
                        </select>
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="task-due">Due Date *</label>
                        <input type="date" id="task-due" required>
                    </div>

                    <div class="form-group">
                        <label for="task-due-time">Due Time</label>
                        <input type="time" id="task-due-time">
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label for="task-priority">Priority</label>
                        <select id="task-priority">
                            <option value="medium">Medium</option>
                            <option value="high">High</option>
                            <option value="low">Low</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="task-category">Category</label>
                        <select id="task-category">
                            <option value="follow_up">Follow Up</option>
                            <option value="document_request">Document Request</option>
                            <option value="review">Review</option>
                            <option value="approval">Approval</option>
                            <option value="closing">Closing</option>
                            <option value="general">General</option>
                        </select>
                    </div>
                </div>

            </form>
        </div>

        <footer class="modal-footer">
            <button onclick="closeModal('modal-quick-task')">Cancel</button>
            <button onclick="createTask()" class="primary-btn">Create Task</button>
        </footer>
    </div>
</div>
```

---

## TASK 4: Add Activity Log View

### 4.1 Add Activity Navigation Item

**Location:** In `#main-nav`, add Activity to navigation (or ensure it exists)

```html
<li><button onclick="navigateTo('activity')">Activity</button></li>
```

### 4.2 Create Activity View

**Location:** Add new view section in `#main-content`

```html
<!-- VIEW: ACTIVITY LOG (Route: /activity) - Phase 8 -->
<section id="view-activity" class="view-section" style="display:none;">
    <header class="view-header">
        <h1>Activity Log</h1>

        <div class="activity-toolbar">
            <div class="activity-filters">
                <select onchange="filterActivity('action', this.value)">
                    <option value="all">All Actions</option>
                    <option value="deal_created">Deal Created</option>
                    <option value="stage_changed">Stage Changed</option>
                    <option value="document_uploaded">Document Uploaded</option>
                    <option value="quote_sent">Quote Sent</option>
                    <option value="exception_requested">Exception Requested</option>
                    <option value="credit_memo_generated">Credit Memo Generated</option>
                    <option value="task_completed">Task Completed</option>
                    <option value="deal_funded">Deal Funded</option>
                </select>

                <select onchange="filterActivity('user', this.value)">
                    <option value="all">All Users</option>
                    <option value="system">System</option>
                    <option value="user_001">Sarah Johnson</option>
                    <option value="user_002">Mike Chen</option>
                    <option value="user_003">Lisa Park</option>
                </select>

                <input type="date" onchange="filterActivity('date', this.value)" placeholder="Date">

                <input type="text" placeholder="Search activity..." onkeyup="searchActivity(this.value)">
            </div>

            <button onclick="exportActivity()">Export CSV</button>
        </div>
    </header>

    <div class="activity-log-content">

        <!-- Date Group: Today -->
        <section class="activity-date-group">
            <h3 class="date-header">Today - December 15, 2024</h3>

            <div class="activity-list">

                <article class="activity-entry">
                    <div class="activity-time">2:30 PM</div>
                    <div class="activity-avatar">
                        <span class="avatar">JS</span>
                    </div>
                    <div class="activity-details">
                        <p class="activity-text">
                            <strong>John Smith</strong> uploaded
                            <a href="#" onclick="viewDocument('doc_001')">Appraisal_123_Main_St.pdf</a>
                        </p>
                        <div class="activity-meta">
                            <span class="activity-deal" onclick="navigateToDeal('deal_001', 'documents')">123 Main St, Austin TX</span>
                            <span class="activity-action">Document Uploaded</span>
                        </div>
                    </div>
                </article>

                <article class="activity-entry">
                    <div class="activity-time">2:31 PM</div>
                    <div class="activity-avatar system">
                        <span class="avatar">🤖</span>
                    </div>
                    <div class="activity-details">
                        <p class="activity-text">
                            <strong>System</strong> analyzed document and created
                            <a href="#" onclick="navigateToDeal('deal_001', 'analysis')">1 yellow flag</a>
                        </p>
                        <div class="activity-meta">
                            <span class="activity-deal" onclick="navigateToDeal('deal_001', 'analysis')">123 Main St, Austin TX</span>
                            <span class="activity-action">Analysis Completed</span>
                        </div>
                    </div>
                </article>

                <article class="activity-entry">
                    <div class="activity-time">1:45 PM</div>
                    <div class="activity-avatar">
                        <span class="avatar">SJ</span>
                    </div>
                    <div class="activity-details">
                        <p class="activity-text">
                            <strong>Sarah Johnson</strong> moved deal to
                            <span class="stage-badge closing">Closing</span>
                        </p>
                        <div class="activity-meta">
                            <span class="activity-deal" onclick="navigateToDeal('deal_002', 'overview')">456 Oak Ave, Dallas TX</span>
                            <span class="activity-action">Stage Changed</span>
                            <span class="activity-change">Underwriting → Closing</span>
                        </div>
                    </div>
                </article>

                <article class="activity-entry">
                    <div class="activity-time">11:30 AM</div>
                    <div class="activity-avatar system">
                        <span class="avatar">🤖</span>
                    </div>
                    <div class="activity-details">
                        <p class="activity-text">
                            <strong>System</strong> generated
                            <a href="#" onclick="navigateToDeal('deal_003', 'credit-memo')">Credit Memo</a>
                        </p>
                        <div class="activity-meta">
                            <span class="activity-deal" onclick="navigateToDeal('deal_003', 'credit-memo')">789 Pine Rd, Houston TX</span>
                            <span class="activity-action">Credit Memo Generated</span>
                        </div>
                    </div>
                </article>

                <article class="activity-entry">
                    <div class="activity-time">10:15 AM</div>
                    <div class="activity-avatar">
                        <span class="avatar">MC</span>
                    </div>
                    <div class="activity-details">
                        <p class="activity-text">
                            <strong>Mike Chen</strong> sent
                            <a href="#" onclick="navigateToDeal('deal_004', 'quotes')">Quote</a>
                            to borrower
                        </p>
                        <div class="activity-meta">
                            <span class="activity-deal" onclick="navigateToDeal('deal_004', 'quotes')">321 Elm St, San Antonio TX</span>
                            <span class="activity-action">Quote Sent</span>
                        </div>
                    </div>
                </article>

                <article class="activity-entry">
                    <div class="activity-time">9:00 AM</div>
                    <div class="activity-avatar">
                        <span class="avatar">LP</span>
                    </div>
                    <div class="activity-details">
                        <p class="activity-text">
                            <strong>Lisa Park</strong> approved
                            <a href="#" onclick="navigateToDeal('deal_005', 'exceptions')">FICO Exception</a>
                        </p>
                        <div class="activity-meta">
                            <span class="activity-deal" onclick="navigateToDeal('deal_005', 'exceptions')">654 Maple Dr, Austin TX</span>
                            <span class="activity-action">Exception Approved</span>
                        </div>
                    </div>
                </article>

            </div>
        </section>

        <!-- Date Group: Yesterday -->
        <section class="activity-date-group">
            <h3 class="date-header">Yesterday - December 14, 2024</h3>

            <div class="activity-list">

                <article class="activity-entry celebration">
                    <div class="activity-time">4:30 PM</div>
                    <div class="activity-avatar">
                        <span class="avatar">🎉</span>
                    </div>
                    <div class="activity-details">
                        <p class="activity-text">
                            <strong>987 Cedar Ln</strong> was <span class="funded">FUNDED</span>!
                            <span class="funded-amount">$425,000</span>
                        </p>
                        <div class="activity-meta">
                            <span class="activity-deal" onclick="navigateToDeal('deal_006', 'overview')">987 Cedar Ln, Dallas TX</span>
                            <span class="activity-action">Deal Funded</span>
                        </div>
                    </div>
                </article>

                <article class="activity-entry">
                    <div class="activity-time">2:15 PM</div>
                    <div class="activity-avatar">
                        <span class="avatar">SJ</span>
                    </div>
                    <div class="activity-details">
                        <p class="activity-text">
                            <strong>Sarah Johnson</strong> completed task
                            "Review and approve credit memo"
                        </p>
                        <div class="activity-meta">
                            <span class="activity-deal" onclick="navigateToDeal('deal_006', 'overview')">987 Cedar Ln, Dallas TX</span>
                            <span class="activity-action">Task Completed</span>
                        </div>
                    </div>
                </article>

            </div>
        </section>

        <div class="load-more">
            <button onclick="loadMoreActivity()">Load More Activity</button>
        </div>

    </div>
</section>
```

---

## TASK 5: Add Global Search (Cmd+K)

### 5.1 Create Search Modal

**Location:** Add to modals section

```html
<!-- MODAL: GLOBAL SEARCH (Cmd+K) - Phase 8 -->
<div id="modal-global-search" class="modal search-modal" style="display:none;">
    <div class="modal-overlay" onclick="closeSearch()"></div>
    <div class="modal-content search-content">

        <div class="search-input-container">
            <span class="search-icon">🔍</span>
            <input type="text"
                   id="global-search-input"
                   placeholder="Search deals, borrowers, properties..."
                   oninput="handleSearch(this.value)"
                   autocomplete="off">
            <kbd class="search-shortcut">ESC</kbd>
        </div>

        <div class="search-results" id="search-results">

            <!-- Recent Searches -->
            <section class="search-section recent-searches">
                <h4>Recent Searches</h4>
                <ul>
                    <li onclick="performSearch('123 Main St')">
                        <span class="search-icon">🕐</span>
                        <span>123 Main St</span>
                    </li>
                    <li onclick="performSearch('ABC Investments')">
                        <span class="search-icon">🕐</span>
                        <span>ABC Investments</span>
                    </li>
                </ul>
            </section>

            <!-- Quick Actions -->
            <section class="search-section quick-actions">
                <h4>Quick Actions</h4>
                <ul>
                    <li onclick="navigateTo('pipeline')">
                        <span class="action-icon">📊</span>
                        <span>Go to Pipeline</span>
                        <kbd>⌘P</kbd>
                    </li>
                    <li onclick="navigateTo('tasks')">
                        <span class="action-icon">📋</span>
                        <span>Go to Tasks</span>
                        <kbd>⌘T</kbd>
                    </li>
                    <li onclick="showModal('modal-new-deal')">
                        <span class="action-icon">➕</span>
                        <span>New Deal</span>
                        <kbd>⌘N</kbd>
                    </li>
                    <li onclick="showQuickTaskModal()">
                        <span class="action-icon">📝</span>
                        <span>New Task</span>
                    </li>
                </ul>
            </section>

        </div>

        <!-- Search Results (shown when typing) -->
        <div class="search-results-dynamic" id="search-results-dynamic" style="display:none;">

            <!-- Deals Results -->
            <section class="search-section">
                <h4>Deals</h4>
                <ul id="search-deals">
                    <li onclick="navigateToDeal('deal_001', 'overview')">
                        <div class="result-main">
                            <span class="result-title">123 Main St, Austin TX</span>
                            <span class="result-subtitle">ABC Investments LLC • Fix & Flip • $382,500</span>
                        </div>
                        <span class="result-badge">Processing</span>
                    </li>
                </ul>
            </section>

            <!-- Borrowers Results -->
            <section class="search-section">
                <h4>Borrowers</h4>
                <ul id="search-borrowers">
                    <li onclick="navigateToBorrower('borrower_001')">
                        <div class="result-main">
                            <span class="result-title">ABC Investments LLC</span>
                            <span class="result-subtitle">John Smith • 3 active deals</span>
                        </div>
                    </li>
                </ul>
            </section>

        </div>

        <div class="search-footer">
            <span class="search-hint">
                <kbd>↑</kbd> <kbd>↓</kbd> to navigate •
                <kbd>Enter</kbd> to select •
                <kbd>ESC</kbd> to close
            </span>
        </div>

    </div>
</div>
```

### 5.2 Update Header with Search

**Location:** Update the header section to include search trigger

```html
<!-- Global Search in Header -->
<div class="global-search" onclick="openGlobalSearch()">
    <span class="search-icon">🔍</span>
    <input type="text" placeholder="Search... (⌘K)" readonly>
    <kbd class="search-kbd">⌘K</kbd>
</div>
```

---

## TASK 6: Add Notification System

### 6.1 Update Header with Notification Bell

**Location:** In the header, add notification bell

```html
<!-- Notifications Bell - Phase 8 -->
<div class="notification-bell-container">
    <button class="notification-bell" onclick="toggleNotifications()">
        <span class="bell-icon">🔔</span>
        <span class="notification-badge">3</span>
    </button>

    <!-- Notification Dropdown -->
    <div id="notification-dropdown" class="notification-dropdown" style="display:none;">
        <header class="notification-header">
            <h3>Notifications</h3>
            <button onclick="markAllNotificationsRead()">Mark all read</button>
        </header>

        <div class="notification-list">

            <article class="notification-item unread">
                <div class="notification-icon">🔴</div>
                <div class="notification-content">
                    <p class="notification-text">
                        <strong>Red Flag Alert</strong>: FICO exception needed for 123 Main St
                    </p>
                    <span class="notification-time">10 minutes ago</span>
                </div>
                <button class="notification-dismiss" onclick="dismissNotification('notif_001')">×</button>
            </article>

            <article class="notification-item unread">
                <div class="notification-icon">📄</div>
                <div class="notification-content">
                    <p class="notification-text">
                        <strong>Document Received</strong>: Appraisal uploaded for 456 Oak Ave
                    </p>
                    <span class="notification-time">25 minutes ago</span>
                </div>
                <button class="notification-dismiss" onclick="dismissNotification('notif_002')">×</button>
            </article>

            <article class="notification-item unread">
                <div class="notification-icon">✅</div>
                <div class="notification-content">
                    <p class="notification-text">
                        <strong>Task Completed</strong>: Mike Chen completed "Review credit memo"
                    </p>
                    <span class="notification-time">1 hour ago</span>
                </div>
                <button class="notification-dismiss" onclick="dismissNotification('notif_003')">×</button>
            </article>

            <article class="notification-item">
                <div class="notification-icon">⏰</div>
                <div class="notification-content">
                    <p class="notification-text">
                        <strong>SLA Warning</strong>: 789 Pine Rd approaching SLA limit
                    </p>
                    <span class="notification-time">2 hours ago</span>
                </div>
            </article>

            <article class="notification-item">
                <div class="notification-icon">🎉</div>
                <div class="notification-content">
                    <p class="notification-text">
                        <strong>Deal Funded!</strong> 987 Cedar Ln closed successfully
                    </p>
                    <span class="notification-time">Yesterday</span>
                </div>
            </article>

        </div>

        <footer class="notification-footer">
            <button onclick="navigateTo('notifications')">View All Notifications</button>
            <button onclick="openNotificationSettings()">Settings</button>
        </footer>
    </div>
</div>
```

---

## TASK 7: Enhance Deal Dashboard with Checklist Tab

### 7.1 Update Checklist Tab Content

**Location:** In `#view-deal-detail`, update the checklist tab

```html
<!-- TAB: CHECKLIST - Enhanced for Phase 8 -->
<div id="tab-checklist" class="tab-content" style="display:none;">
    <header class="tab-header">
        <h2>Closing Checklist</h2>
        <div class="checklist-actions">
            <span class="checklist-progress">
                Progress: <strong>28 / 36</strong> (78%)
            </span>
            <div class="progress-bar">
                <div class="progress-fill" style="width: 78%;"></div>
            </div>
            <button onclick="sendChecklistReminder()">Send Reminder</button>
            <button onclick="exportChecklist()">Export</button>
        </div>
    </header>

    <div class="checklist-content">

        <!-- BORROWER DOCUMENTS -->
        <section class="checklist-category">
            <header class="category-header collapsible" onclick="toggleChecklistCategory('borrower')">
                <div class="category-title">
                    <span class="category-icon">👤</span>
                    <h3>Borrower Documents</h3>
                </div>
                <div class="category-progress">
                    <span class="progress-count">6 / 8</span>
                    <span class="toggle-icon">▼</span>
                </div>
            </header>
            <div id="checklist-borrower" class="category-items">

                <article class="checklist-item complete">
                    <div class="item-status">
                        <span class="status-icon">✅</span>
                    </div>
                    <div class="item-content">
                        <span class="item-name">Articles of Organization</span>
                        <span class="item-date">Received 12/05/2024</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="viewDocument('articles')">View</button>
                    </div>
                </article>

                <article class="checklist-item complete">
                    <div class="item-status">
                        <span class="status-icon">✅</span>
                    </div>
                    <div class="item-content">
                        <span class="item-name">Operating Agreement</span>
                        <span class="item-date">Received 12/05/2024</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="viewDocument('op_agreement')">View</button>
                    </div>
                </article>

                <article class="checklist-item complete">
                    <div class="item-status">
                        <span class="status-icon">✅</span>
                    </div>
                    <div class="item-content">
                        <span class="item-name">Certificate of Good Standing</span>
                        <span class="item-date">Received 12/08/2024</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="viewDocument('good_standing')">View</button>
                    </div>
                </article>

                <article class="checklist-item complete">
                    <div class="item-status">
                        <span class="status-icon">✅</span>
                    </div>
                    <div class="item-content">
                        <span class="item-name">EIN Letter / W-9</span>
                        <span class="item-date">Received 12/05/2024</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="viewDocument('ein')">View</button>
                    </div>
                </article>

                <article class="checklist-item complete">
                    <div class="item-status">
                        <span class="status-icon">✅</span>
                    </div>
                    <div class="item-content">
                        <span class="item-name">Bank Statements (2 months)</span>
                        <span class="item-date">Received 12/10/2024</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="viewDocument('bank_statements')">View</button>
                    </div>
                </article>

                <article class="checklist-item complete">
                    <div class="item-status">
                        <span class="status-icon">✅</span>
                    </div>
                    <div class="item-content">
                        <span class="item-name">Driver's License - John Smith</span>
                        <span class="item-date">Received 12/05/2024</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="viewDocument('dl_john')">View</button>
                    </div>
                </article>

                <article class="checklist-item missing">
                    <div class="item-status">
                        <span class="status-icon">❌</span>
                    </div>
                    <div class="item-content">
                        <span class="item-name">Driver's License - Jane Smith</span>
                        <span class="item-status-text">Missing</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="requestDocument('dl_jane')">Request</button>
                        <button onclick="uploadDocument('dl_jane')">Upload</button>
                    </div>
                </article>

                <article class="checklist-item na">
                    <div class="item-status">
                        <span class="status-icon">N/A</span>
                    </div>
                    <div class="item-content">
                        <span class="item-name">Passport / Green Card</span>
                        <span class="item-status-text">Not Applicable</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="markRequired('passport')">Mark Required</button>
                    </div>
                </article>

            </div>
        </section>

        <!-- PROPERTY DOCUMENTS -->
        <section class="checklist-category">
            <header class="category-header collapsible" onclick="toggleChecklistCategory('property')">
                <div class="category-title">
                    <span class="category-icon">🏠</span>
                    <h3>Property Documents</h3>
                </div>
                <div class="category-progress">
                    <span class="progress-count">5 / 6</span>
                    <span class="toggle-icon">▼</span>
                </div>
            </header>
            <div id="checklist-property" class="category-items">

                <article class="checklist-item complete">
                    <div class="item-status"><span class="status-icon">✅</span></div>
                    <div class="item-content">
                        <span class="item-name">Purchase Contract / PSA</span>
                        <span class="item-date">Received 12/01/2024</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="viewDocument('psa')">View</button>
                    </div>
                </article>

                <article class="checklist-item complete">
                    <div class="item-status"><span class="status-icon">✅</span></div>
                    <div class="item-content">
                        <span class="item-name">Scope of Work / Budget</span>
                        <span class="item-date">Received 12/03/2024</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="viewDocument('sow')">View</button>
                    </div>
                </article>

                <article class="checklist-item complete">
                    <div class="item-status"><span class="status-icon">✅</span></div>
                    <div class="item-content">
                        <span class="item-name">Permits</span>
                        <span class="item-date">Received 12/07/2024</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="viewDocument('permits')">View</button>
                    </div>
                </article>

                <article class="checklist-item complete">
                    <div class="item-status"><span class="status-icon">✅</span></div>
                    <div class="item-content">
                        <span class="item-name">Contractor Agreement</span>
                        <span class="item-date">Received 12/07/2024</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="viewDocument('contractor')">View</button>
                    </div>
                </article>

                <article class="checklist-item in-progress">
                    <div class="item-status"><span class="status-icon">🔄</span></div>
                    <div class="item-content">
                        <span class="item-name">Payoff Letter</span>
                        <span class="item-status-text">Requested 12/12 - Pending</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="followUpDocument('payoff')">Follow Up</button>
                    </div>
                </article>

            </div>
        </section>

        <!-- THIRD-PARTY REPORTS -->
        <section class="checklist-category">
            <header class="category-header collapsible" onclick="toggleChecklistCategory('third_party')">
                <div class="category-title">
                    <span class="category-icon">📋</span>
                    <h3>Third-Party Reports</h3>
                </div>
                <div class="category-progress">
                    <span class="progress-count complete">7 / 7</span>
                    <span class="toggle-icon">▼</span>
                </div>
            </header>
            <div id="checklist-third-party" class="category-items">

                <article class="checklist-item complete">
                    <div class="item-status"><span class="status-icon">✅</span></div>
                    <div class="item-content">
                        <span class="item-name">Credit Report</span>
                        <span class="item-date">Received 12/05/2024</span>
                        <span class="item-note warning">Expires in 85 days</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="viewDocument('credit')">View</button>
                    </div>
                </article>

                <article class="checklist-item complete">
                    <div class="item-status"><span class="status-icon">✅</span></div>
                    <div class="item-content">
                        <span class="item-name">Background Check</span>
                        <span class="item-date">Received 12/05/2024</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="viewDocument('background')">View</button>
                    </div>
                </article>

                <article class="checklist-item complete">
                    <div class="item-status"><span class="status-icon">✅</span></div>
                    <div class="item-content">
                        <span class="item-name">Appraisal</span>
                        <span class="item-date">Received 12/15/2024</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="viewDocument('appraisal')">View</button>
                    </div>
                </article>

                <article class="checklist-item complete">
                    <div class="item-status"><span class="status-icon">✅</span></div>
                    <div class="item-content">
                        <span class="item-name">Title Commitment</span>
                        <span class="item-date">Received 12/12/2024</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="viewDocument('title')">View</button>
                    </div>
                </article>

                <article class="checklist-item complete">
                    <div class="item-status"><span class="status-icon">✅</span></div>
                    <div class="item-content">
                        <span class="item-name">Flood Determination</span>
                        <span class="item-date">Received 12/10/2024</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="viewDocument('flood')">View</button>
                    </div>
                </article>

                <article class="checklist-item complete">
                    <div class="item-status"><span class="status-icon">✅</span></div>
                    <div class="item-content">
                        <span class="item-name">Feasibility Study</span>
                        <span class="item-date">Received 12/08/2024</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="viewDocument('feasibility')">View</button>
                    </div>
                </article>

                <article class="checklist-item complete">
                    <div class="item-status"><span class="status-icon">✅</span></div>
                    <div class="item-content">
                        <span class="item-name">Insurance Certificate</span>
                        <span class="item-date">Received 12/14/2024</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="viewDocument('insurance')">View</button>
                    </div>
                </article>

            </div>
        </section>

        <!-- CLOSING DOCUMENTS -->
        <section class="checklist-category">
            <header class="category-header collapsible" onclick="toggleChecklistCategory('closing')">
                <div class="category-title">
                    <span class="category-icon">📄</span>
                    <h3>Closing Documents</h3>
                </div>
                <div class="category-progress">
                    <span class="progress-count">2 / 5</span>
                    <span class="toggle-icon">▼</span>
                </div>
            </header>
            <div id="checklist-closing" class="category-items">

                <article class="checklist-item complete">
                    <div class="item-status"><span class="status-icon">✅</span></div>
                    <div class="item-content">
                        <span class="item-name">Preliminary HUD</span>
                        <span class="item-date">Received 12/14/2024</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="viewDocument('prelim_hud')">View</button>
                    </div>
                </article>

                <article class="checklist-item complete">
                    <div class="item-status"><span class="status-icon">✅</span></div>
                    <div class="item-content">
                        <span class="item-name">Closing Protection Letter</span>
                        <span class="item-date">Received 12/14/2024</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="viewDocument('cpl')">View</button>
                    </div>
                </article>

                <article class="checklist-item missing">
                    <div class="item-status"><span class="status-icon">❌</span></div>
                    <div class="item-content">
                        <span class="item-name">Final HUD / Settlement Statement</span>
                        <span class="item-status-text">Pending</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="requestDocument('final_hud')">Request</button>
                    </div>
                </article>

                <article class="checklist-item missing">
                    <div class="item-status"><span class="status-icon">❌</span></div>
                    <div class="item-content">
                        <span class="item-name">Wire Instructions</span>
                        <span class="item-status-text">Pending</span>
                    </div>
                    <div class="item-actions">
                        <button onclick="requestDocument('wire')">Request</button>
                    </div>
                </article>

                <article class="checklist-item missing">
                    <div class="item-status"><span class="status-icon">❌</span></div>
                    <div class="item-content">
                        <span class="item-name">Funding Confirmation</span>
                        <span class="item-status-text">Not Started</span>
                    </div>
                    <div class="item-actions">
                        <button disabled>Pending Closing</button>
                    </div>
                </article>

            </div>
        </section>

    </div>
</div>
```

---

## TASK 8: Add Notes Tab to Deal Dashboard

### 8.1 Create Notes Tab Content

**Location:** In `#view-deal-detail`, add notes tab content

```html
<!-- TAB: NOTES - Phase 8 -->
<div id="tab-notes" class="tab-content" style="display:none;">
    <header class="tab-header">
        <h2>Internal Notes</h2>
        <span class="notes-count">5 notes</span>
    </header>

    <div class="notes-content">

        <!-- Add Note Form -->
        <div class="add-note-form">
            <textarea id="new-note-content" placeholder="Add an internal note... Use @mention to notify team members"></textarea>
            <div class="note-form-actions">
                <button onclick="addNote()" class="primary-btn">Add Note</button>
            </div>
        </div>

        <!-- Notes List -->
        <div class="notes-list">

            <article class="note-item">
                <div class="note-header">
                    <div class="note-author">
                        <span class="avatar">SJ</span>
                        <span class="author-name">Sarah Johnson</span>
                    </div>
                    <span class="note-time">Today at 2:30 PM</span>
                </div>
                <div class="note-content">
                    <p>Spoke with borrower about the FICO exception. He explained the score dropped due to high utilization during a recent acquisition. All balances are now paid down and score is recovering. Strong compensating factors documented in exception request.</p>
                </div>
                <div class="note-actions">
                    <button onclick="editNote('note_001')">Edit</button>
                    <button onclick="deleteNote('note_001')">Delete</button>
                </div>
            </article>

            <article class="note-item">
                <div class="note-header">
                    <div class="note-author">
                        <span class="avatar">MC</span>
                        <span class="author-name">Mike Chen</span>
                    </div>
                    <span class="note-time">Yesterday at 4:15 PM</span>
                </div>
                <div class="note-content">
                    <p>Appraisal received. ARV came in at $485K vs $520K expected (8% variance). Need to discuss with <span class="mention">@Sarah Johnson</span> about exception request.</p>
                </div>
            </article>

            <article class="note-item">
                <div class="note-header">
                    <div class="note-author">
                        <span class="avatar">LP</span>
                        <span class="author-name">Lisa Park</span>
                    </div>
                    <span class="note-time">Dec 12, 2024 at 10:00 AM</span>
                </div>
                <div class="note-content">
                    <p>Title came back clean. Standard utility easement on rear 10ft - no issues. Cleared for closing once remaining items complete.</p>
                </div>
            </article>

            <article class="note-item">
                <div class="note-header">
                    <div class="note-author">
                        <span class="avatar">SJ</span>
                        <span class="author-name">Sarah Johnson</span>
                    </div>
                    <span class="note-time">Dec 10, 2024 at 3:45 PM</span>
                </div>
                <div class="note-content">
                    <p>Borrower is experienced with 8 completed projects. Prior USDV relationship - 2 loans funded with no issues. Strong repeat borrower.</p>
                </div>
            </article>

            <article class="note-item">
                <div class="note-header">
                    <div class="note-author">
                        <span class="avatar">SJ</span>
                        <span class="author-name">Sarah Johnson</span>
                    </div>
                    <span class="note-time">Dec 1, 2024 at 9:00 AM</span>
                </div>
                <div class="note-content">
                    <p>New deal submitted. Borrower looking for quick close before year-end. Target close: 12/20. Property is a light rehab - cosmetic updates only.</p>
                </div>
            </article>

        </div>

    </div>
</div>
```

---

## TASK 9: Add JavaScript Functions for Phase 8

### 9.1 Add Phase 8 Navigation and Core Functions

**Location:** Add to the existing `<script>` section

```javascript
// ===== PHASE 8: OPERATIONAL COMMAND CENTER FUNCTIONS =====

// ===== NAVIGATION =====

function navigateTo(view) {
    // Hide all views
    document.querySelectorAll('.view-section').forEach(v => v.style.display = 'none');

    // Show requested view
    const viewElement = document.getElementById('view-' + view);
    if (viewElement) {
        viewElement.style.display = 'block';
    }

    // Update nav active state
    document.querySelectorAll('#main-nav button').forEach(btn => btn.classList.remove('active'));
}

// ===== GLOBAL SEARCH (Cmd+K) =====

document.addEventListener('keydown', function(e) {
    // Cmd+K or Ctrl+K to open search
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        openGlobalSearch();
    }
    // ESC to close
    if (e.key === 'Escape') {
        closeSearch();
        closeAllModals();
    }
});

function openGlobalSearch() {
    showModal('modal-global-search');
    setTimeout(() => {
        document.getElementById('global-search-input').focus();
    }, 100);
}

function closeSearch() {
    closeModal('modal-global-search');
    document.getElementById('global-search-input').value = '';
}

function handleSearch(query) {
    const dynamicResults = document.getElementById('search-results-dynamic');
    const staticResults = document.getElementById('search-results');

    if (query.length > 0) {
        dynamicResults.style.display = 'block';
        staticResults.style.display = 'none';
        // In real implementation: fetch and display results
        console.log('Searching for:', query);
    } else {
        dynamicResults.style.display = 'none';
        staticResults.style.display = 'block';
    }
}

function performSearch(query) {
    console.log('Performing search:', query);
    closeSearch();
}

// ===== NOTIFICATIONS =====

function toggleNotifications() {
    const dropdown = document.getElementById('notification-dropdown');
    dropdown.style.display = dropdown.style.display === 'none' ? 'block' : 'none';
}

function dismissNotification(notifId) {
    console.log('Dismissing notification:', notifId);
    alert('Notification dismissed');
}

function markAllNotificationsRead() {
    console.log('Marking all notifications as read');
    document.querySelectorAll('.notification-item.unread').forEach(item => {
        item.classList.remove('unread');
    });
    document.querySelector('.notification-badge').textContent = '0';
}

function openNotificationSettings() {
    alert('Opening notification settings...');
}

// ===== PIPELINE =====

function applyFilters() {
    console.log('Applying filters...');
    // In real implementation: filter the deals
}

function sortPipeline() {
    const sortBy = document.getElementById('sort-by').value;
    console.log('Sorting pipeline by:', sortBy);
}

function setPipelineView(view) {
    console.log('Setting pipeline view to:', view);
    document.querySelectorAll('.view-toggle button').forEach(btn => {
        btn.classList.remove('active');
    });
    event.target.classList.add('active');
}

function filterPipeline(filter) {
    console.log('Filtering pipeline:', filter);
    navigateTo('pipeline');
}

// Drag and drop
function allowDrop(event) {
    event.preventDefault();
}

function dragDeal(event, dealId) {
    event.dataTransfer.setData('dealId', dealId);
}

function dropDeal(event, toStage) {
    event.preventDefault();
    const dealId = event.dataTransfer.getData('dealId');
    console.log('Moving deal', dealId, 'to stage:', toStage);
    alert('Moving deal to ' + toStage + ' stage');
}

function showQuickActions(dealId) {
    event.stopPropagation();
    const dropdown = document.getElementById('quick-actions-dropdown');
    dropdown.style.display = 'block';
    dropdown.dataset.dealId = dealId;
    // Position near cursor
    dropdown.style.top = event.pageY + 'px';
    dropdown.style.left = event.pageX + 'px';
}

function hideQuickActions() {
    document.getElementById('quick-actions-dropdown').style.display = 'none';
}

function quickAction(action) {
    const dealId = document.getElementById('quick-actions-dropdown').dataset.dealId;
    console.log('Quick action:', action, 'for deal:', dealId);
    hideQuickActions();

    switch(action) {
        case 'view':
            navigateToDeal(dealId, 'overview');
            break;
        case 'add_task':
            showQuickTaskModal(dealId);
            break;
        case 'add_note':
            navigateToDeal(dealId, 'notes');
            break;
        case 'archive':
            if (confirm('Archive this deal?')) {
                alert('Deal archived');
            }
            break;
        default:
            alert('Action: ' + action);
    }
}

function viewFundedDeals() {
    alert('Viewing funded deals...');
}

// ===== TASKS =====

function showQuickTaskModal(dealId) {
    showModal('modal-quick-task');
    if (dealId) {
        document.getElementById('task-deal').value = dealId;
    }
}

function createTask() {
    const title = document.getElementById('task-title').value;
    const dealId = document.getElementById('task-deal').value;
    const assignee = document.getElementById('task-assign').value;
    const dueDate = document.getElementById('task-due').value;

    console.log('Creating task:', { title, dealId, assignee, dueDate });
    alert('Task created: ' + title);
    closeModal('modal-quick-task');
}

function filterTasks(filter) {
    console.log('Filtering tasks:', filter);
    document.querySelectorAll('.task-tabs button').forEach(btn => {
        btn.classList.remove('active');
    });
    event.target.classList.add('active');
}

function filterTasksBy(field, value) {
    console.log('Filtering tasks by', field, ':', value);
}

function toggleTask(taskId) {
    console.log('Toggling task:', taskId);
}

function completeTask(taskId) {
    console.log('Completing task:', taskId);
    alert('Task completed');
}

function editTask(taskId) {
    console.log('Editing task:', taskId);
    alert('Opening task editor...');
}

function reassignTask(taskId) {
    console.log('Reassigning task:', taskId);
    alert('Opening reassign dialog...');
}

// ===== NEEDS ATTENTION =====

function filterNeedsAttention(filter) {
    console.log('Filtering needs attention:', filter);
}

function escalateDeal(dealId) {
    console.log('Escalating deal:', dealId);
    alert('Escalating to manager...');
}

function sendQuoteReminder(dealId) {
    console.log('Sending quote reminder for:', dealId);
    alert('Quote reminder sent to borrower');
}

function extendRateLock(dealId) {
    console.log('Extending rate lock for:', dealId);
    alert('Rate lock extension requested');
}

function archiveDeal(dealId) {
    if (confirm('Are you sure you want to archive this deal?')) {
        console.log('Archiving deal:', dealId);
        alert('Deal archived');
    }
}

// ===== ACTIVITY =====

function filterActivity(field, value) {
    console.log('Filtering activity by', field, ':', value);
}

function searchActivity(query) {
    console.log('Searching activity:', query);
}

function exportActivity() {
    console.log('Exporting activity log...');
    alert('Exporting activity to CSV...');
}

function loadMoreActivity() {
    console.log('Loading more activity...');
    alert('Loading more...');
}

// ===== CHECKLIST =====

function toggleChecklistCategory(categoryId) {
    const items = document.getElementById('checklist-' + categoryId);
    if (items) {
        items.classList.toggle('collapsed');
    }
}

function requestDocument(docType) {
    console.log('Requesting document:', docType);
    alert('Document request sent to borrower');
}

function uploadDocument(docType) {
    console.log('Uploading document:', docType);
    alert('Opening file upload...');
}

function followUpDocument(docType) {
    console.log('Following up on document:', docType);
    alert('Follow-up email sent');
}

function markRequired(docType) {
    console.log('Marking as required:', docType);
}

function sendChecklistReminder() {
    console.log('Sending checklist reminder');
    alert('Reminder email sent to borrower with missing items');
}

function exportChecklist() {
    console.log('Exporting checklist');
    alert('Downloading checklist PDF...');
}

// ===== NOTES =====

function addNote() {
    const content = document.getElementById('new-note-content').value;
    if (content.trim()) {
        console.log('Adding note:', content);
        alert('Note added');
        document.getElementById('new-note-content').value = '';
    }
}

function editNote(noteId) {
    console.log('Editing note:', noteId);
    alert('Opening note editor...');
}

function deleteNote(noteId) {
    if (confirm('Delete this note?')) {
        console.log('Deleting note:', noteId);
        alert('Note deleted');
    }
}

// ===== HELPERS =====

function closeAllModals() {
    document.querySelectorAll('.modal').forEach(modal => {
        modal.style.display = 'none';
    });
}

// Close dropdowns when clicking outside
document.addEventListener('click', function(e) {
    // Close quick actions dropdown
    if (!e.target.closest('.card-quick-actions') && !e.target.closest('#quick-actions-dropdown')) {
        hideQuickActions();
    }

    // Close notification dropdown
    if (!e.target.closest('.notification-bell-container')) {
        document.getElementById('notification-dropdown').style.display = 'none';
    }
});
```

---

## TASK 10: Testing Checklist

After implementing all tasks, verify the following:

### Dashboard Tests
- [ ] All 8 KPI cards display with values
- [ ] KPI trends show up/down indicators
- [ ] "Needs Attention" section shows items with priority colors
- [ ] Needs Attention items have working action buttons
- [ ] Tasks Due Today section shows tasks with checkboxes
- [ ] Pipeline overview chart displays all stages
- [ ] SLA summary shows on-track/at-risk/breached counts
- [ ] Recent Activity feed displays with timestamps

### Pipeline Tests
- [ ] All 8 Kanban stages render (including Initial UW)
- [ ] Stage headers show count, volume, and SLA info
- [ ] Deal cards display all required information
- [ ] Deal cards show flag indicators (red/yellow)
- [ ] Deal cards show SLA status (on-track/at-risk/breached)
- [ ] Filters work (loan type, investor, assignee, SLA, flags)
- [ ] Sort dropdown changes card order
- [ ] Quick actions dropdown opens on card menu click
- [ ] Drag-and-drop starts (HTML5 drag events)

### Task Manager Tests
- [ ] Task Manager view loads with task groups
- [ ] Task tabs filter correctly (My Tasks, All, Overdue)
- [ ] Task filters work (priority, category, assignee)
- [ ] Quick Task modal opens and closes
- [ ] Task form validation works
- [ ] Complete button marks tasks done

### Activity Log Tests
- [ ] Activity Log view loads
- [ ] Activities grouped by date
- [ ] Filters work (action type, user, date)
- [ ] Search filters activity
- [ ] Export button triggers download

### Global Search Tests
- [ ] Cmd+K opens search modal
- [ ] ESC closes search modal
- [ ] Typing shows dynamic results
- [ ] Quick actions are clickable
- [ ] Recent searches display

### Notifications Tests
- [ ] Notification bell shows badge count
- [ ] Clicking bell opens dropdown
- [ ] Mark all read clears unread state
- [ ] Dismiss removes individual notification

### Checklist Tab Tests
- [ ] All 4 checklist categories display
- [ ] Categories are collapsible
- [ ] Progress counts are accurate
- [ ] Status icons are correct (✅❌🔄)
- [ ] Action buttons work (Request, Upload, View)

### Notes Tab Tests
- [ ] Notes tab displays notes
- [ ] Add note form works
- [ ] Edit/Delete buttons are functional
- [ ] @mentions are highlighted

---

## Reference Files

When implementing, reference these files for patterns and data:

1. **PRD:** `_PRDs/inspire-phase-8-prd.md` - Full requirements
2. **Implementation Plan:** `_PRDs/implementation-plans/phase-8-implementation.md` - Detailed specs
3. **Underwriting Manual:**
   - `USDV_Underwriting_Manual/sections/13_document_requirements.md` - Checklist items
4. **Existing HTML:** `inspire-ux.html` - Patterns for existing dashboard, pipeline
5. **Phase 7 Plan:** `_PRDs/Phase 7 Prototype QA/phase-7-cursor-implementation-tasks.md` - Related components

---

## Notes for Cursor

1. **Build on existing structure** - Phase 8 enhances existing dashboard and pipeline views
2. **Maintain consistency** - Use same patterns for cards, modals, tabs as existing code
3. **SLA indicators** - Use `on-track` (green), `at-risk` (yellow), `breached` (red) classes
4. **Priority colors** - Use `priority-high`, `priority-medium`, `priority-low` classes
5. **Keyboard shortcuts** - Implement Cmd+K for search at minimum
6. **Collapsible sections** - Use `collapsed` class toggle for expandable content
7. **Real-time feel** - Use onclick handlers that provide immediate feedback

---

*End of Phase 8 Cursor Implementation Task Plan*
