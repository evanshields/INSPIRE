# Phase 7: AI Analysis & Credit Memo - Cursor Implementation Task Plan

**Document Version:** 1.0
**Target File:** `inspire-ux.html`
**Last Updated:** January 2026
**Prerequisite:** Phases 1-6 must be complete in the HTML prototype

---

## Overview

This document provides a step-by-step implementation plan for adding Phase 7 (AI Analysis & Credit Memo) to the INSPIRE HTML prototype. Follow each task sequentially, completing all subtasks before moving to the next main task.

**Phase 7 adds these core capabilities:**
- Analysis Dashboard with flag aggregation
- Document-level AI analysis views
- Flag management system (Red/Yellow/Green)
- Exception request workflow
- Credit Memo viewer and editor
- Risk assessment visualizations

---

## TASK 1: Add Phase 7 Navigation & Tab Structure

### 1.1 Add Analysis Tab to Deal Detail Tabs

**Location:** Inside `<div class="deal-tabs">` → `<nav class="tab-nav">`

Find the existing Analysis tab button and ensure it has proper onclick handler:
```html
<button onclick="switchDealTab('tab-analysis')">Analysis (AI)</button>
```

### 1.2 Add Credit Memo Tab to Deal Detail Tabs

**Location:** Inside `<div class="deal-tabs">` → `<nav class="tab-nav">`

Add new Credit Memo tab after the Analysis tab:
```html
<button onclick="switchDealTab('tab-credit-memo')">Credit Memo</button>
```

### 1.3 Add Exceptions Tab to Deal Detail Tabs

**Location:** Inside `<div class="deal-tabs">` → `<nav class="tab-nav">`

Add new Exceptions tab after Credit Memo:
```html
<button onclick="switchDealTab('tab-exceptions')">Exceptions</button>
```

---

## TASK 2: Implement Analysis Dashboard Tab (P7-01)

### 2.1 Create Analysis Tab Content Container

**Location:** Add new tab content section after existing tabs in `view-deal-detail`

```html
<!-- TAB: ANALYSIS (AI) - Phase 7 -->
<div id="tab-analysis" class="tab-content" style="display:none;">
    <header class="tab-header">
        <h2>AI Analysis Dashboard</h2>
        <div class="analysis-actions">
            <button onclick="reanalyzeAll()">Re-Analyze All Documents</button>
            <button onclick="navigateToCreditMemo()" class="primary-btn">Generate Credit Memo</button>
            <button onclick="exportFlags()">Export Flags</button>
        </div>
        <p class="last-analyzed">Last analyzed: 2 minutes ago</p>
    </header>

    <!-- Content continues in next subtasks -->
</div>
```

### 2.2 Add Overall Analysis Summary Cards

**Location:** Inside `#tab-analysis`, after the header

```html
<!-- OVERALL ANALYSIS STATUS -->
<!-- Component: Card Grid (4-col) -->
<div class="analysis-summary-grid">

    <!-- Risk Score Card -->
    <article class="summary-card">
        <h3>Risk Score</h3>
        <div class="risk-gauge">
            <!-- Visual gauge: 0-100, color-coded -->
            <span class="score">35</span>
            <span class="rating state-warning">MODERATE</span>
        </div>
        <p>Based on 35 checks across 12 documents</p>
    </article>

    <!-- Flag Summary Card -->
    <article class="summary-card">
        <h3>Flag Summary</h3>
        <div class="flag-counts">
            <span class="flag-count green" onclick="filterFlags('green')">
                <span class="icon">✅</span>
                <span class="count">28</span>
                <span class="label">Green</span>
            </span>
            <span class="flag-count yellow" onclick="filterFlags('yellow')">
                <span class="icon">⚠️</span>
                <span class="count">5</span>
                <span class="label">Yellow</span>
            </span>
            <span class="flag-count red" onclick="filterFlags('red')">
                <span class="icon">🔴</span>
                <span class="count">2</span>
                <span class="label">Red</span>
            </span>
        </div>
    </article>

    <!-- Documents Analyzed Card -->
    <article class="summary-card">
        <h3>Documents Analyzed</h3>
        <div class="progress-circle">
            <span class="value">12 / 14</span>
            <span class="percent">86%</span>
        </div>
        <p>2 documents pending analysis</p>
    </article>

    <!-- Exceptions Card -->
    <article class="summary-card">
        <h3>Exceptions</h3>
        <div class="exception-summary">
            <span class="count">2</span>
            <span class="label">Required</span>
        </div>
        <ul class="exception-status">
            <li><span class="status pending">1 Pending</span></li>
            <li><span class="status approved">1 Approved</span></li>
        </ul>
        <button onclick="switchDealTab('tab-exceptions')">Manage Exceptions</button>
    </article>

</div>
```

### 2.3 Add Critical Findings Section (Red Flags)

**Location:** Inside `#tab-analysis`, after summary cards

```html
<!-- CRITICAL FINDINGS (RED FLAGS) -->
<!-- Component: Alert Cards -->
<section class="findings-section state-error">
    <header>
        <h3>🔴 Red Flags - Action Required</h3>
        <span class="count">2</span>
    </header>

    <div class="flag-cards">

        <!-- Red Flag 1: FICO -->
        <article class="flag-card red">
            <div class="flag-header">
                <span class="category">Credit</span>
                <span class="severity">🔴 Red Flag</span>
            </div>
            <h4>FICO Score Below Minimum</h4>
            <p class="finding">Middle FICO score of <strong>655</strong> is below investor minimum of <strong>660</strong>.</p>
            <div class="comparison">
                <span class="actual">Actual: 655</span>
                <span class="expected">Required: ≥660</span>
                <span class="variance">-5 points</span>
            </div>
            <p class="guideline-ref">
                <em>Reference: Eastview RTL Guidelines Section 2.1 - "Minimum FICO score of 660 required"</em>
            </p>
            <div class="flag-actions">
                <button onclick="requestException('flag_001')" class="primary-btn">Request Exception</button>
                <button onclick="viewDocument('credit_report')">View Credit Report</button>
                <button onclick="resolveFlag('flag_001')">Mark Resolved</button>
            </div>
            <div class="exception-status">
                <span class="badge pending">Exception Pending</span>
                <span class="submitted">Submitted 12/15/2024 by Sarah Johnson</span>
            </div>
        </article>

        <!-- Red Flag 2: ARV Variance -->
        <article class="flag-card red">
            <div class="flag-header">
                <span class="category">Valuation</span>
                <span class="severity">🔴 Red Flag</span>
            </div>
            <h4>ARV Variance Exceeds Threshold</h4>
            <p class="finding">Appraisal ARV of <strong>$485,000</strong> differs from feasibility by <strong>8%</strong>, exceeding 5% threshold.</p>
            <div class="comparison">
                <span class="actual">Appraisal ARV: $485,000</span>
                <span class="expected">Feasibility ARV: $520,000</span>
                <span class="variance">-$35,000 (-6.7%)</span>
            </div>
            <p class="impact">
                <strong>Impact:</strong> LTARV increases from 68% to 73%. Still within maximum (75%).
            </p>
            <p class="guideline-ref">
                <em>Reference: Eastview RTL Guidelines Section 5.2.1 - "ARV variance must be within 5%"</em>
            </p>
            <div class="flag-actions">
                <button onclick="requestException('flag_002')" class="primary-btn">Request Exception</button>
                <button onclick="viewDocument('appraisal')">View Appraisal</button>
                <button onclick="viewDocument('feasibility')">View Feasibility</button>
            </div>
        </article>

    </div>
</section>
```

### 2.4 Add Yellow Flags Section (Warnings)

**Location:** Inside `#tab-analysis`, after red flags section

```html
<!-- WARNING FLAGS (YELLOW) -->
<!-- Component: Alert Cards (Collapsible) -->
<section class="findings-section state-warning">
    <header class="collapsible" onclick="toggleSection('yellow-flags')">
        <h3>⚠️ Yellow Flags - Review Recommended</h3>
        <span class="count">5</span>
        <span class="toggle-icon">▼</span>
    </header>

    <div id="yellow-flags" class="flag-cards">

        <!-- Yellow Flag 1: Experience -->
        <article class="flag-card yellow">
            <div class="flag-header">
                <span class="category">Experience</span>
                <span class="severity">⚠️ Yellow</span>
            </div>
            <h4>Limited Track Record</h4>
            <p class="finding">Borrower has completed <strong>3 projects</strong> in past 36 months. 5+ preferred for Tier 1 pricing.</p>
            <div class="comparison">
                <span class="actual">Actual: 3 deals</span>
                <span class="expected">Preferred: 5+ deals</span>
            </div>
            <p class="guideline-ref">
                <em>Reference: USDV Manual Section 2.3.1 - Experience Classification</em>
            </p>
            <div class="flag-actions">
                <button onclick="acknowledgeFlag('flag_003')">Acknowledge</button>
                <button onclick="viewDocument('experience_docs')">View Documentation</button>
            </div>
        </article>

        <!-- Yellow Flag 2: Large Deposit -->
        <article class="flag-card yellow">
            <div class="flag-header">
                <span class="category">Financial</span>
                <span class="severity">⚠️ Yellow</span>
            </div>
            <h4>Large Deposit Requires Sourcing</h4>
            <p class="finding">$45,000 deposit on 11/15/2024 exceeds $10,000 threshold. Source verification recommended.</p>
            <div class="flag-actions">
                <button onclick="requestLOE('flag_004')">Request LOE</button>
                <button onclick="viewDocument('bank_statements')">View Bank Statement</button>
                <button onclick="acknowledgeFlag('flag_004')">Acknowledge</button>
            </div>
        </article>

        <!-- Yellow Flag 3: Easement -->
        <article class="flag-card yellow">
            <div class="flag-header">
                <span class="category">Title</span>
                <span class="severity">⚠️ Yellow</span>
            </div>
            <h4>Easement Noted in Title</h4>
            <p class="finding">Utility easement on rear 10ft of property noted in Schedule B-II.</p>
            <p class="impact">Standard utility easement - no adverse impact expected.</p>
            <div class="flag-actions">
                <button onclick="viewDocument('title_commitment')">View Title</button>
                <button onclick="acknowledgeFlag('flag_005')">Acknowledge</button>
            </div>
        </article>

        <!-- Yellow Flag 4: Appraisal Age -->
        <article class="flag-card yellow">
            <div class="flag-header">
                <span class="category">Documentation</span>
                <span class="severity">⚠️ Yellow</span>
            </div>
            <h4>Appraisal Approaching Expiration</h4>
            <p class="finding">Appraisal dated 11/18/2024 will expire in <strong>28 days</strong> (120-day limit).</p>
            <div class="flag-actions">
                <button onclick="orderRecertification()">Order Recertification</button>
                <button onclick="acknowledgeFlag('flag_006')">Acknowledge</button>
            </div>
        </article>

        <!-- Yellow Flag 5: Insurance Term -->
        <article class="flag-card yellow">
            <div class="flag-header">
                <span class="category">Insurance</span>
                <span class="severity">⚠️ Yellow</span>
            </div>
            <h4>Policy Expires Before Loan Maturity</h4>
            <p class="finding">Insurance policy expires 10/15/2025. Loan maturity is 12/15/2025.</p>
            <div class="flag-actions">
                <button onclick="requestRenewal()">Request Renewal</button>
                <button onclick="acknowledgeFlag('flag_007')">Acknowledge</button>
            </div>
        </article>

    </div>
</section>
```

### 2.5 Add Green Flags Section (Passing Checks)

**Location:** Inside `#tab-analysis`, after yellow flags section

```html
<!-- PASSING CHECKS (GREEN) -->
<!-- Component: Collapsible List -->
<section class="findings-section state-success">
    <header class="collapsible" onclick="toggleSection('green-flags')">
        <h3>✅ Passing Checks</h3>
        <span class="count">28</span>
        <span class="toggle-icon">▼</span>
    </header>

    <div id="green-flags" class="flag-list collapsed">

        <!-- Group by Category -->
        <div class="flag-group">
            <h4>Credit (6 checks)</h4>
            <ul>
                <li>✅ Credit report current (dated 11/20/2024 - within 120 days)</li>
                <li>✅ No mortgage lates in 24 months</li>
                <li>✅ No bankruptcy within 4 years</li>
                <li>✅ No foreclosure within 4 years</li>
                <li>✅ No open collections over $5,000</li>
                <li>✅ Minimum 3 trade lines requirement met (8 active)</li>
            </ul>
        </div>

        <div class="flag-group">
            <h4>Background (4 checks)</h4>
            <ul>
                <li>✅ Background check clear - no criminal records</li>
                <li>✅ OFAC/AML screening passed</li>
                <li>✅ No active litigation</li>
                <li>✅ No unresolved judgments over $10,000</li>
            </ul>
        </div>

        <div class="flag-group">
            <h4>Entity (4 checks)</h4>
            <ul>
                <li>✅ Entity in good standing (Certificate dated 11/25/2024)</li>
                <li>✅ EIN verified</li>
                <li>✅ Operating agreement on file</li>
                <li>✅ All guarantors documented</li>
            </ul>
        </div>

        <div class="flag-group">
            <h4>Property (5 checks)</h4>
            <ul>
                <li>✅ Property type eligible (SFR)</li>
                <li>✅ Square footage meets minimum (1,850 sf)</li>
                <li>✅ Condition rating acceptable (C4)</li>
                <li>✅ Zoning compliant (Residential)</li>
                <li>✅ Not in flood zone (Zone X)</li>
            </ul>
        </div>

        <div class="flag-group">
            <h4>Title (4 checks)</h4>
            <ul>
                <li>✅ Clear title - no adverse liens</li>
                <li>✅ No tax liens</li>
                <li>✅ No mechanic's liens</li>
                <li>✅ Legal access confirmed</li>
            </ul>
        </div>

        <div class="flag-group">
            <h4>Financial (5 checks)</h4>
            <ul>
                <li>✅ Liquidity verified: $185,000 (required: $142,000)</li>
                <li>✅ Bank statements current (dated 11/22/2024)</li>
                <li>✅ No NSF/overdrafts in 90 days</li>
                <li>✅ Reserves requirement met (130% of required)</li>
                <li>✅ Closing costs verified</li>
            </ul>
        </div>

    </div>
</section>
```

### 2.6 Add Document Analysis Summary Table

**Location:** Inside `#tab-analysis`, after green flags section

```html
<!-- DOCUMENT ANALYSIS SUMMARY -->
<!-- Component: Data Table -->
<section class="document-analysis-section">
    <header>
        <h3>Document-by-Document Analysis</h3>
        <div class="filters">
            <select onchange="filterDocAnalysis(this.value)">
                <option value="all">All Documents</option>
                <option value="flagged">Flagged Only</option>
                <option value="pending">Pending Analysis</option>
            </select>
        </div>
    </header>

    <table class="analysis-table">
        <thead>
            <tr>
                <th>Document</th>
                <th>Type</th>
                <th>Analyzed</th>
                <th>Status</th>
                <th>Flags</th>
                <th>Confidence</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr class="has-red-flag">
                <td>Tri-Merge Credit Report</td>
                <td>Credit Report</td>
                <td>12/10/2024 10:15 AM</td>
                <td><span class="badge complete">Complete</span></td>
                <td>
                    <span class="flag-dot red" title="1 Red Flag">🔴</span>
                </td>
                <td>95%</td>
                <td>
                    <button onclick="viewDocAnalysis('credit_report')">View</button>
                    <button onclick="reanalyzeDoc('credit_report')">Re-analyze</button>
                </td>
            </tr>
            <tr class="has-red-flag">
                <td>Full Appraisal Report</td>
                <td>Appraisal</td>
                <td>12/15/2024 2:00 PM</td>
                <td><span class="badge complete">Complete</span></td>
                <td>
                    <span class="flag-dot red" title="1 Red Flag">🔴</span>
                    <span class="flag-dot yellow" title="1 Yellow Flag">⚠️</span>
                </td>
                <td>88%</td>
                <td>
                    <button onclick="viewDocAnalysis('appraisal')">View</button>
                    <button onclick="reanalyzeDoc('appraisal')">Re-analyze</button>
                </td>
            </tr>
            <tr>
                <td>Title Commitment</td>
                <td>Title</td>
                <td>12/12/2024 4:30 PM</td>
                <td><span class="badge complete">Complete</span></td>
                <td>
                    <span class="flag-dot yellow" title="1 Yellow Flag">⚠️</span>
                </td>
                <td>92%</td>
                <td>
                    <button onclick="viewDocAnalysis('title')">View</button>
                </td>
            </tr>
            <tr>
                <td>Hazard Insurance Certificate</td>
                <td>Insurance</td>
                <td>12/14/2024 9:00 AM</td>
                <td><span class="badge complete">Complete</span></td>
                <td>
                    <span class="flag-dot yellow" title="1 Yellow Flag">⚠️</span>
                </td>
                <td>96%</td>
                <td>
                    <button onclick="viewDocAnalysis('insurance')">View</button>
                </td>
            </tr>
            <tr>
                <td>Background Check Report</td>
                <td>Background</td>
                <td>12/11/2024 11:30 AM</td>
                <td><span class="badge complete">Complete</span></td>
                <td>
                    <span class="flag-dot green" title="All Clear">✅</span>
                </td>
                <td>98%</td>
                <td>
                    <button onclick="viewDocAnalysis('background')">View</button>
                </td>
            </tr>
            <tr>
                <td>Bank Statements (Nov)</td>
                <td>Bank Statement</td>
                <td>12/13/2024 3:15 PM</td>
                <td><span class="badge complete">Complete</span></td>
                <td>
                    <span class="flag-dot yellow" title="1 Yellow Flag">⚠️</span>
                </td>
                <td>90%</td>
                <td>
                    <button onclick="viewDocAnalysis('bank_statements')">View</button>
                </td>
            </tr>
            <tr>
                <td>Operating Agreement</td>
                <td>Entity Docs</td>
                <td>12/09/2024 8:45 AM</td>
                <td><span class="badge complete">Complete</span></td>
                <td>
                    <span class="flag-dot green" title="All Clear">✅</span>
                </td>
                <td>94%</td>
                <td>
                    <button onclick="viewDocAnalysis('entity')">View</button>
                </td>
            </tr>
            <tr class="pending">
                <td>Feasibility Study</td>
                <td>Feasibility</td>
                <td>-</td>
                <td><span class="badge pending">Pending</span></td>
                <td>-</td>
                <td>-</td>
                <td>
                    <button onclick="analyzeDoc('feasibility')">Analyze Now</button>
                </td>
            </tr>
            <tr class="pending">
                <td>Contractor License</td>
                <td>Contractor</td>
                <td>-</td>
                <td><span class="badge pending">Pending</span></td>
                <td>-</td>
                <td>-</td>
                <td>
                    <button onclick="analyzeDoc('contractor')">Analyze Now</button>
                </td>
            </tr>
        </tbody>
    </table>
</section>
```

### 2.7 Add Category Score Breakdown

**Location:** Inside `#tab-analysis`, after document analysis table

```html
<!-- CATEGORY SCORE BREAKDOWN -->
<!-- Component: Progress Bars / Score Cards -->
<section class="category-scores-section">
    <h3>Analysis by Category</h3>

    <div class="category-scores-grid">

        <div class="category-score-card">
            <div class="category-header">
                <span class="category-name">Borrower</span>
                <span class="category-score">85</span>
            </div>
            <div class="score-bar">
                <div class="score-fill" style="width: 85%;" data-color="green"></div>
            </div>
            <p class="category-detail">Credit: Good | Experience: 8 deals | Background: Clear</p>
        </div>

        <div class="category-score-card">
            <div class="category-header">
                <span class="category-name">Property</span>
                <span class="category-score">90</span>
            </div>
            <div class="score-bar">
                <div class="score-fill" style="width: 90%;" data-color="green"></div>
            </div>
            <p class="category-detail">SFR in Austin | Condition C4 | Good market</p>
        </div>

        <div class="category-score-card">
            <div class="category-header">
                <span class="category-name">Valuation</span>
                <span class="category-score state-warning">75</span>
            </div>
            <div class="score-bar">
                <div class="score-fill" style="width: 75%;" data-color="yellow"></div>
            </div>
            <p class="category-detail">ARV variance 8% | Comps adequate</p>
        </div>

        <div class="category-score-card">
            <div class="category-header">
                <span class="category-name">Title</span>
                <span class="category-score">95</span>
            </div>
            <div class="score-bar">
                <div class="score-fill" style="width: 95%;" data-color="green"></div>
            </div>
            <p class="category-detail">Clear title | Standard utility easement</p>
        </div>

        <div class="category-score-card">
            <div class="category-header">
                <span class="category-name">Insurance</span>
                <span class="category-score state-warning">80</span>
            </div>
            <div class="score-bar">
                <div class="score-fill" style="width: 80%;" data-color="yellow"></div>
            </div>
            <p class="category-detail">Coverage adequate | Policy renewal needed</p>
        </div>

        <div class="category-score-card">
            <div class="category-header">
                <span class="category-name">Financial</span>
                <span class="category-score">88</span>
            </div>
            <div class="score-bar">
                <div class="score-fill" style="width: 88%;" data-color="green"></div>
            </div>
            <p class="category-detail">Reserves: 130% | Large deposit flagged</p>
        </div>

    </div>
</section>
```

---

## TASK 3: Implement Document Analysis Detail Modal (P7-02)

### 3.1 Create Document Analysis Detail Modal

**Location:** Add to modals section at end of `view-deal-detail` or in a dedicated modals container

```html
<!-- MODAL: DOCUMENT ANALYSIS DETAIL -->
<div id="modal-doc-analysis" class="modal" style="display:none;">
    <div class="modal-overlay" onclick="closeModal('modal-doc-analysis')"></div>
    <div class="modal-content large">
        <header class="modal-header">
            <h2>Document Analysis: Appraisal Report</h2>
            <button onclick="closeModal('modal-doc-analysis')" class="close-btn">×</button>
        </header>

        <div class="modal-body">

            <!-- Document Info -->
            <section class="doc-info-section">
                <div class="doc-meta">
                    <span>Document Type: <strong>Appraisal</strong></span>
                    <span>File: <strong>Appraisal_123_Main_St.pdf</strong></span>
                    <span>Analyzed: <strong>12/15/2024 2:00 PM</strong></span>
                    <span>Confidence: <strong>88%</strong></span>
                </div>
                <div class="doc-actions">
                    <button onclick="viewPDF('appraisal')">View PDF</button>
                    <button onclick="reanalyzeDoc('appraisal')">Re-Analyze</button>
                </div>
            </section>

            <!-- Extracted Data -->
            <section class="extracted-data-section">
                <h3>Extracted Data</h3>
                <div class="data-grid">
                    <div class="data-item">
                        <label>As-Is Value</label>
                        <span class="value">$425,000</span>
                    </div>
                    <div class="data-item">
                        <label>After-Repair Value (ARV)</label>
                        <span class="value">$485,000</span>
                    </div>
                    <div class="data-item">
                        <label>Property Type</label>
                        <span class="value">Single Family Residence</span>
                    </div>
                    <div class="data-item">
                        <label>Square Footage</label>
                        <span class="value">1,850 sf</span>
                    </div>
                    <div class="data-item">
                        <label>Condition Rating</label>
                        <span class="value">C4</span>
                    </div>
                    <div class="data-item">
                        <label>Appraiser</label>
                        <span class="value">John Smith, SRA</span>
                    </div>
                    <div class="data-item">
                        <label>License #</label>
                        <span class="value">TX-12345</span>
                    </div>
                    <div class="data-item">
                        <label>Report Date</label>
                        <span class="value">11/18/2024</span>
                    </div>
                </div>
            </section>

            <!-- Analysis Results -->
            <section class="analysis-results-section">
                <h3>Analysis Results</h3>
                <table class="results-table">
                    <thead>
                        <tr>
                            <th>Check</th>
                            <th>Result</th>
                            <th>Finding</th>
                            <th>Guideline</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="pass">
                            <td>Report Currency</td>
                            <td>✅ Pass</td>
                            <td>Report dated 11/18/2024 (27 days old)</td>
                            <td>Must be within 120 days</td>
                        </tr>
                        <tr class="pass">
                            <td>Appraiser License</td>
                            <td>✅ Pass</td>
                            <td>State certified appraiser (not trainee)</td>
                            <td>Must be state certified</td>
                        </tr>
                        <tr class="pass">
                            <td>Property Type</td>
                            <td>✅ Pass</td>
                            <td>SFR - eligible property type</td>
                            <td>SFR, Condo, 2-4 Unit eligible</td>
                        </tr>
                        <tr class="pass">
                            <td>Square Footage</td>
                            <td>✅ Pass</td>
                            <td>1,850 sf exceeds 600 sf minimum</td>
                            <td>Minimum 600 sf for SFR</td>
                        </tr>
                        <tr class="pass">
                            <td>Condition Rating</td>
                            <td>✅ Pass</td>
                            <td>C4 condition acceptable</td>
                            <td>C1-C4 acceptable; C5-C6 require exception</td>
                        </tr>
                        <tr class="fail">
                            <td>ARV Variance</td>
                            <td>🔴 Fail</td>
                            <td>8% variance from feasibility ($485K vs $520K)</td>
                            <td>Variance must be within 5%</td>
                        </tr>
                        <tr class="pass">
                            <td>Comparable Age</td>
                            <td>✅ Pass</td>
                            <td>All comparables within 6 months</td>
                            <td>Comps must be within 6 months</td>
                        </tr>
                        <tr class="pass">
                            <td>Comparable Location</td>
                            <td>✅ Pass</td>
                            <td>All comparables within same neighborhood</td>
                            <td>Comps should be in same market area</td>
                        </tr>
                    </tbody>
                </table>
            </section>

            <!-- AI Summary -->
            <section class="ai-summary-section">
                <h3>AI Summary</h3>
                <p class="ai-narrative">
                    As-is value of $425,000 and ARV of $585,000 are supported by comparable sales
                    within the immediate neighborhood. Subject property is a 3BR/2BA single-family
                    residence in C4 condition, appropriate for the proposed rehabilitation scope.
                    ARV shows <strong>8% variance from feasibility study</strong>, primarily due to the
                    appraiser's use of more recent sales reflecting continued market appreciation
                    in the Austin MSA. This variance exceeds the 5% threshold and requires exception
                    or loan resizing. The appraisal methodology is sound and the value conclusion
                    is well-supported by the comparable analysis.
                </p>
            </section>

        </div>

        <footer class="modal-footer">
            <button onclick="closeModal('modal-doc-analysis')">Close</button>
        </footer>
    </div>
</div>
```

---

## TASK 4: Implement Flag Manager Section (P7-03)

### 4.1 Add Flag Manager as Sub-View of Analysis Tab

This can be a toggle within the Analysis tab or a separate modal. For the prototype, add a modal:

```html
<!-- MODAL: FLAG MANAGER -->
<div id="modal-flag-manager" class="modal" style="display:none;">
    <div class="modal-overlay" onclick="closeModal('modal-flag-manager')"></div>
    <div class="modal-content extra-large">
        <header class="modal-header">
            <h2>Flag Manager - 123 Main Street</h2>
            <button onclick="closeModal('modal-flag-manager')" class="close-btn">×</button>
        </header>

        <div class="modal-body">

            <!-- Filter Toolbar -->
            <div class="flag-manager-toolbar">
                <div class="filters">
                    <select id="flag-severity-filter">
                        <option value="all">All Severities</option>
                        <option value="red">Red Flags Only</option>
                        <option value="yellow">Yellow Flags Only</option>
                        <option value="green">Green (Passing) Only</option>
                    </select>
                    <select id="flag-category-filter">
                        <option value="all">All Categories</option>
                        <option value="credit">Credit</option>
                        <option value="background">Background</option>
                        <option value="experience">Experience</option>
                        <option value="property">Property</option>
                        <option value="valuation">Valuation</option>
                        <option value="title">Title</option>
                        <option value="insurance">Insurance</option>
                        <option value="financial">Financial</option>
                    </select>
                    <select id="flag-status-filter">
                        <option value="all">All Statuses</option>
                        <option value="open">Open</option>
                        <option value="acknowledged">Acknowledged</option>
                        <option value="resolved">Resolved</option>
                        <option value="exception">Exception Requested</option>
                    </select>
                </div>
                <div class="actions">
                    <button onclick="exportFlagsCSV()">Export CSV</button>
                    <button onclick="bulkAcknowledge()">Bulk Acknowledge</button>
                </div>
            </div>

            <!-- Tabs: Active / Resolved / All -->
            <div class="flag-tabs">
                <button class="active">Active (7)</button>
                <button>Resolved (3)</button>
                <button>Exceptions (2)</button>
                <button>All (12)</button>
            </div>

            <!-- Flag List -->
            <table class="flags-table">
                <thead>
                    <tr>
                        <th><input type="checkbox" /></th>
                        <th>Severity</th>
                        <th>Category</th>
                        <th>Flag</th>
                        <th>Document</th>
                        <th>Status</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><input type="checkbox" /></td>
                        <td><span class="severity-badge red">🔴 Red</span></td>
                        <td>Credit</td>
                        <td>
                            <strong>FICO Below Minimum</strong>
                            <p>Actual: 655 | Required: ≥660</p>
                        </td>
                        <td>Credit Report</td>
                        <td><span class="status-badge exception">Exception Pending</span></td>
                        <td>
                            <button>View</button>
                            <button>View Exception</button>
                        </td>
                    </tr>
                    <tr>
                        <td><input type="checkbox" /></td>
                        <td><span class="severity-badge red">🔴 Red</span></td>
                        <td>Valuation</td>
                        <td>
                            <strong>ARV Variance High</strong>
                            <p>8% variance exceeds 5% threshold</p>
                        </td>
                        <td>Appraisal</td>
                        <td><span class="status-badge open">Open</span></td>
                        <td>
                            <button>View</button>
                            <button onclick="showModal('modal-exception-request')">Request Exception</button>
                        </td>
                    </tr>
                    <tr>
                        <td><input type="checkbox" /></td>
                        <td><span class="severity-badge yellow">⚠️ Yellow</span></td>
                        <td>Experience</td>
                        <td>
                            <strong>Limited Track Record</strong>
                            <p>3 deals in 36 months (5+ preferred)</p>
                        </td>
                        <td>Experience Docs</td>
                        <td><span class="status-badge acknowledged">Acknowledged</span></td>
                        <td>
                            <button>View</button>
                        </td>
                    </tr>
                    <tr>
                        <td><input type="checkbox" /></td>
                        <td><span class="severity-badge yellow">⚠️ Yellow</span></td>
                        <td>Financial</td>
                        <td>
                            <strong>Large Deposit Unsourced</strong>
                            <p>$45,000 on 11/15 needs LOE</p>
                        </td>
                        <td>Bank Statements</td>
                        <td><span class="status-badge open">Open</span></td>
                        <td>
                            <button>View</button>
                            <button>Request LOE</button>
                        </td>
                    </tr>
                    <!-- Additional flags... -->
                </tbody>
            </table>

        </div>

        <footer class="modal-footer">
            <button onclick="closeModal('modal-flag-manager')">Close</button>
        </footer>
    </div>
</div>
```

---

## TASK 5: Implement Exception Request System (P7-04)

### 5.1 Create Exception Request Modal

```html
<!-- MODAL: EXCEPTION REQUEST -->
<div id="modal-exception-request" class="modal" style="display:none;">
    <div class="modal-overlay" onclick="closeModal('modal-exception-request')"></div>
    <div class="modal-content large">
        <header class="modal-header">
            <h2>Request Exception</h2>
            <button onclick="closeModal('modal-exception-request')" class="close-btn">×</button>
        </header>

        <div class="modal-body">

            <!-- Exception Context -->
            <section class="exception-context">
                <h3>Flag Being Excepted</h3>
                <div class="context-card">
                    <div class="flag-summary">
                        <span class="severity-badge red">🔴 Red Flag</span>
                        <span class="category">Credit</span>
                    </div>
                    <h4>FICO Score Below Minimum</h4>
                    <p>Middle FICO score of <strong>655</strong> is below investor minimum of <strong>660</strong>.</p>
                    <p class="guideline-ref">
                        <em>Eastview RTL Guidelines Section 2.1: "Minimum FICO score of 660 required for all guarantors"</em>
                    </p>
                </div>
            </section>

            <!-- Exception Form -->
            <form class="exception-form">

                <!-- Exception Type -->
                <div class="form-group">
                    <label>Exception Type *</label>
                    <select id="exception-type" required>
                        <option value="">Select Type...</option>
                        <option value="credit_fico" selected>Credit - FICO Below Threshold</option>
                        <option value="credit_events">Credit - Derogatory Events</option>
                        <option value="experience">Experience Shortfall</option>
                        <option value="ltv_ltc">Leverage Exception (LTV/LTC/LTARV)</option>
                        <option value="dscr">DSCR Below Minimum</option>
                        <option value="property">Property Type/Condition</option>
                        <option value="valuation">Valuation Variance</option>
                        <option value="documentation">Documentation Timing</option>
                        <option value="other">Other</option>
                    </select>
                </div>

                <!-- Variance Details -->
                <div class="form-row">
                    <div class="form-group">
                        <label>Guideline Requirement</label>
                        <input type="text" value="Minimum FICO score of 660" readonly>
                    </div>
                    <div class="form-group">
                        <label>Actual Value</label>
                        <input type="text" value="655" readonly>
                    </div>
                    <div class="form-group">
                        <label>Variance</label>
                        <input type="text" value="5 points below minimum" readonly>
                    </div>
                </div>

                <!-- Justification -->
                <div class="form-group">
                    <label>Justification / Explanation *</label>
                    <textarea id="exception-justification" rows="4" required
                        placeholder="Explain why this exception should be approved. Include any context about the borrower's situation.">Borrower's FICO dropped due to high credit utilization during recent acquisition. All balances have been paid down and score is recovering. Borrower has demonstrated strong payment history across 8 prior projects with no defaults. Strong track record mitigates FICO concern.</textarea>
                </div>

                <!-- Compensating Factors -->
                <div class="form-group">
                    <label>Compensating Factors *</label>
                    <p class="helper-text">Select all factors that strengthen this deal despite the exception.</p>

                    <div class="compensating-factors-grid">
                        <label class="factor-checkbox">
                            <input type="checkbox" checked>
                            <span>Strong Experience (8+ completed projects)</span>
                        </label>
                        <label class="factor-checkbox">
                            <input type="checkbox" checked>
                            <span>Excess Liquidity ($185K - 130% of required)</span>
                        </label>
                        <label class="factor-checkbox">
                            <input type="checkbox" checked>
                            <span>Conservative Leverage (LTV 65%)</span>
                        </label>
                        <label class="factor-checkbox">
                            <input type="checkbox">
                            <span>Strong DSCR (>1.25x)</span>
                        </label>
                        <label class="factor-checkbox">
                            <input type="checkbox" checked>
                            <span>Repeat Borrower - Good History</span>
                        </label>
                        <label class="factor-checkbox">
                            <input type="checkbox">
                            <span>Cross-Collateralization</span>
                        </label>
                        <label class="factor-checkbox">
                            <input type="checkbox">
                            <span>Additional Collateral</span>
                        </label>
                        <label class="factor-checkbox">
                            <input type="checkbox">
                            <span>Rate Buydown / Pricing Adjustment</span>
                        </label>
                    </div>
                </div>

                <!-- Quantified Compensating Factors -->
                <div class="form-group">
                    <label>Quantified Compensating Factors</label>
                    <div class="quantified-factors">
                        <div class="factor-row">
                            <span class="factor-name">Liquidity:</span>
                            <input type="text" value="$185,000 verified (130% of $142,000 requirement)">
                        </div>
                        <div class="factor-row">
                            <span class="factor-name">Experience:</span>
                            <input type="text" value="8 completed projects in past 36 months">
                        </div>
                        <div class="factor-row">
                            <span class="factor-name">LTV Cushion:</span>
                            <input type="text" value="65% LTV vs 75% maximum (10 point cushion)">
                        </div>
                        <button type="button" onclick="addCompensatingFactor()">+ Add Factor</button>
                    </div>
                </div>

                <!-- Supporting Documents -->
                <div class="form-group">
                    <label>Supporting Documentation</label>
                    <div class="supporting-docs">
                        <label class="doc-checkbox">
                            <input type="checkbox" checked>
                            <span>Credit Report (dated 11/20/2024)</span>
                        </label>
                        <label class="doc-checkbox">
                            <input type="checkbox" checked>
                            <span>Bank Statements ($185K verified)</span>
                        </label>
                        <label class="doc-checkbox">
                            <input type="checkbox" checked>
                            <span>Experience Summary (8 deals documented)</span>
                        </label>
                        <label class="doc-checkbox">
                            <input type="checkbox">
                            <span>Letter of Explanation</span>
                        </label>
                    </div>
                </div>

                <!-- Approval Tier Display -->
                <div class="approval-tier-section">
                    <h4>Approval Authority</h4>
                    <div class="tier-indicator">
                        <span class="tier tier-3 active">Tier 3: Investor Approval Required</span>
                        <p class="tier-description">
                            FICO exceptions >10 points below minimum require investor approval.
                            This exception will be submitted to <strong>Eastview</strong> for review.
                        </p>
                    </div>
                </div>

            </form>

        </div>

        <footer class="modal-footer">
            <button onclick="closeModal('modal-exception-request')">Cancel</button>
            <button onclick="saveExceptionDraft()" class="secondary-btn">Save Draft</button>
            <button onclick="submitException()" class="primary-btn">Submit Exception Request</button>
        </footer>
    </div>
</div>
```

### 5.2 Add Exceptions Tab Content

**Location:** Add as new tab content in `view-deal-detail`

```html
<!-- TAB: EXCEPTIONS - Phase 7 -->
<div id="tab-exceptions" class="tab-content" style="display:none;">
    <header class="tab-header">
        <h2>Exception Management</h2>
        <button onclick="showModal('modal-exception-request')" class="primary-btn">New Exception Request</button>
    </header>

    <!-- Exception Summary -->
    <div class="exception-summary-cards">
        <article class="summary-card">
            <h3>Active Exceptions</h3>
            <span class="count">2</span>
        </article>
        <article class="summary-card">
            <span class="status pending">1 Pending Review</span>
            <span class="status approved">1 Approved</span>
            <span class="status denied">0 Denied</span>
        </article>
    </div>

    <!-- Exception List -->
    <section class="exceptions-list">

        <!-- Exception 1: Approved -->
        <article class="exception-card approved">
            <header class="exception-header">
                <div class="exception-id">
                    <span class="id">EXC-2024-001</span>
                    <span class="status-badge approved">✅ Approved</span>
                </div>
                <span class="date">Submitted: 12/10/2024 | Approved: 12/12/2024</span>
            </header>

            <div class="exception-body">
                <h4>Credit Exception - FICO Below Minimum</h4>
                <p><strong>Flag:</strong> FICO 655 vs. 660 minimum (5 points below)</p>
                <p><strong>Investor:</strong> Eastview</p>

                <div class="compensating-factors">
                    <h5>Compensating Factors Cited:</h5>
                    <ul>
                        <li>8 completed projects in 36 months</li>
                        <li>$185,000 verified liquidity (130% of requirement)</li>
                        <li>65% LTV (10 point cushion to max)</li>
                        <li>Repeat borrower with perfect payment history</li>
                    </ul>
                </div>

                <div class="approval-details">
                    <h5>Investor Response:</h5>
                    <p class="approval-notes">
                        "Exception approved. Strong compensating factors noted. Apply 10bps rate adjustment."
                    </p>
                    <p><strong>Conditions:</strong></p>
                    <ul>
                        <li>10bps rate adjustment applied (10.5% → 10.6%)</li>
                    </ul>
                    <p><strong>Approved By:</strong> M. Thompson, Eastview Capital</p>
                </div>
            </div>

            <footer class="exception-footer">
                <button onclick="viewExceptionDetail('EXC-2024-001')">View Full Request</button>
            </footer>
        </article>

        <!-- Exception 2: Pending -->
        <article class="exception-card pending">
            <header class="exception-header">
                <div class="exception-id">
                    <span class="id">EXC-2024-002</span>
                    <span class="status-badge pending">⏳ Pending Review</span>
                </div>
                <span class="date">Submitted: 12/15/2024</span>
            </header>

            <div class="exception-body">
                <h4>Valuation Exception - ARV Variance</h4>
                <p><strong>Flag:</strong> 8% ARV variance exceeds 5% threshold</p>
                <p><strong>Investor:</strong> Eastview</p>

                <div class="compensating-factors">
                    <h5>Compensating Factors Cited:</h5>
                    <ul>
                        <li>Conservative 65% LTV provides value cushion</li>
                        <li>Appraised ARV ($485K) is lower than feasibility ($520K) - conservative</li>
                        <li>Strong market appreciation (6% YoY in Austin MSA)</li>
                    </ul>
                </div>

                <div class="pending-info">
                    <p><em>Awaiting investor review. Expected response within 2 business days.</em></p>
                </div>
            </div>

            <footer class="exception-footer">
                <button onclick="viewExceptionDetail('EXC-2024-002')">View Request</button>
                <button onclick="withdrawException('EXC-2024-002')">Withdraw</button>
            </footer>
        </article>

    </section>

    <!-- Exception History -->
    <section class="exception-history">
        <h3>Exception Request Template</h3>
        <p>Use the USDV standard exception request format when submitting to investors.</p>
        <button onclick="showExceptionTemplate()">View Template</button>
        <button onclick="downloadExceptionTemplate()">Download Word Template</button>
    </section>
</div>
```

---

## TASK 6: Implement Credit Memo Tab (P7-05)

### 6.1 Create Credit Memo Tab Content

**Location:** Add as new tab content in `view-deal-detail`

```html
<!-- TAB: CREDIT MEMO - Phase 7 -->
<div id="tab-credit-memo" class="tab-content" style="display:none;">
    <header class="tab-header">
        <h2>Credit Memorandum</h2>
        <div class="memo-actions">
            <span class="memo-status"><strong>Status:</strong> <span class="badge ready">Ready for Review</span></span>
            <button onclick="regenerateCreditMemo()">Regenerate</button>
            <button onclick="editCreditMemo()">Edit Memo</button>
            <button onclick="exportCreditMemo('pdf')" class="primary-btn">Export PDF</button>
            <button onclick="exportCreditMemo('docx')">Export Word</button>
        </div>
    </header>

    <!-- Memo Version Info -->
    <div class="memo-meta">
        <span>Version: 1.0</span>
        <span>Generated: 12/15/2024 4:30 PM</span>
        <span>Generated By: AI (Claude)</span>
        <span>Last Edited: -</span>
    </div>

    <!-- Credit Memo Content -->
    <div class="credit-memo-viewer">

        <!-- MEMO HEADER -->
        <header class="memo-document-header">
            <div class="memo-title-block">
                <h1>CREDIT MEMORANDUM</h1>
                <div class="memo-header-details">
                    <p><strong>Property:</strong> 123 Main Street, Austin, TX 78701</p>
                    <p><strong>Loan Type:</strong> Fix & Flip</p>
                    <p><strong>Loan Amount:</strong> $382,500</p>
                    <p><strong>Investor:</strong> Eastview Capital</p>
                    <p><strong>Prepared By:</strong> INSPIRE AI Analysis</p>
                    <p><strong>Date:</strong> December 15, 2024</p>
                    <p><strong>Deal ID:</strong> DEAL-2024-1234</p>
                </div>
            </div>
        </header>

        <!-- SECTION 1: EXECUTIVE SUMMARY -->
        <section class="memo-section" id="memo-exec-summary">
            <h2>1. Executive Summary</h2>

            <div class="deal-snapshot">
                <h3>Deal Snapshot</h3>
                <div class="snapshot-grid">
                    <div class="snapshot-item">
                        <label>Property</label>
                        <span>123 Main Street, Austin, TX 78701</span>
                    </div>
                    <div class="snapshot-item">
                        <label>Property Type</label>
                        <span>Single Family Residence</span>
                    </div>
                    <div class="snapshot-item">
                        <label>Loan Type</label>
                        <span>Fix & Flip</span>
                    </div>
                    <div class="snapshot-item">
                        <label>Loan Purpose</label>
                        <span>Purchase + Rehab</span>
                    </div>
                </div>
            </div>

            <div class="loan-terms">
                <h3>Loan Terms</h3>
                <div class="terms-grid">
                    <div class="term-item">
                        <label>Loan Amount</label>
                        <span>$382,500</span>
                    </div>
                    <div class="term-item">
                        <label>Interest Rate</label>
                        <span>10.6%</span>
                    </div>
                    <div class="term-item">
                        <label>Term</label>
                        <span>12 Months</span>
                    </div>
                    <div class="term-item">
                        <label>Structure</label>
                        <span>Interest-Only</span>
                    </div>
                </div>
            </div>

            <div class="key-metrics">
                <h3>Key Metrics</h3>
                <div class="metrics-grid">
                    <div class="metric-item">
                        <label>As-Is Value</label>
                        <span>$425,000</span>
                    </div>
                    <div class="metric-item">
                        <label>After-Repair Value</label>
                        <span>$485,000</span>
                    </div>
                    <div class="metric-item">
                        <label>Rehab Budget</label>
                        <span>$85,000</span>
                    </div>
                    <div class="metric-item">
                        <label>As-Is LTV</label>
                        <span>65%</span>
                    </div>
                    <div class="metric-item">
                        <label>LTC</label>
                        <span>75%</span>
                    </div>
                    <div class="metric-item">
                        <label>LTARV</label>
                        <span>73%</span>
                    </div>
                    <div class="metric-item">
                        <label>FICO</label>
                        <span>655</span>
                    </div>
                    <div class="metric-item">
                        <label>Experience</label>
                        <span>8 deals / 36mo</span>
                    </div>
                </div>
            </div>

            <div class="recommendation-block">
                <h3>Recommendation</h3>
                <div class="recommendation approved-with-conditions">
                    <span class="recommendation-badge">APPROVE WITH CONDITIONS</span>
                    <p class="rationale">
                        Strong borrower profile with extensive experience mitigates the 5-point FICO shortfall.
                        Conservative leverage provides cushion for the ARV variance. Deal fundamentals are solid
                        with clear exit strategy and adequate reserves.
                    </p>
                </div>
            </div>

            <div class="key-strengths">
                <h3>Key Strengths</h3>
                <ul>
                    <li>Experienced sponsor with 8 completed projects in target market</li>
                    <li>Conservative leverage at 65% LTV with 10-point cushion to maximum</li>
                    <li>Strong liquidity: $185,000 verified (130% of requirement)</li>
                    <li>Repeat borrower with perfect payment history on prior USDV loans</li>
                    <li>Property in appreciating Austin market with strong fundamentals</li>
                </ul>
            </div>

            <div class="key-risks">
                <h3>Key Risks / Exceptions Required</h3>
                <ul>
                    <li>🔴 FICO 655 requires credit exception (5 points below 660 minimum) - <strong>APPROVED with 10bps rate adjustment</strong></li>
                    <li>🔴 ARV variance of 8% exceeds 5% threshold - <strong>Exception pending</strong></li>
                    <li>⚠️ First project in Austin market (borrower has 8 projects in Houston)</li>
                    <li>⚠️ Aggressive 4-month rehab timeline for scope of work</li>
                </ul>
            </div>

            <div class="exception-summary">
                <h3>Exception Status</h3>
                <div class="exception-counts">
                    <span><strong>2</strong> Requested</span> |
                    <span><strong>1</strong> Approved</span> |
                    <span><strong>1</strong> Pending</span> |
                    <span><strong>0</strong> Denied</span>
                </div>
            </div>
        </section>

        <!-- SECTION 2: BORROWER ANALYSIS -->
        <section class="memo-section" id="memo-borrower-analysis">
            <h2>2. Borrower Analysis</h2>

            <div class="sponsor-overview">
                <h3>Sponsor Overview</h3>
                <table class="sponsor-table">
                    <thead>
                        <tr>
                            <th>Guarantor</th>
                            <th>Ownership</th>
                            <th>FICO</th>
                            <th>Experience</th>
                            <th>Role</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>John Smith</td>
                            <td>100%</td>
                            <td>655 (Middle of 648/655/672)</td>
                            <td>8 deals / 36mo, 12 lifetime</td>
                            <td>Sponsor / Operator</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="entity-structure">
                <h3>Borrowing Entity</h3>
                <table class="entity-table">
                    <tr><td>Entity Name:</td><td>ABC Investments LLC</td></tr>
                    <tr><td>Entity Type:</td><td>Limited Liability Company</td></tr>
                    <tr><td>Formation State:</td><td>Texas</td></tr>
                    <tr><td>Formation Date:</td><td>March 2018</td></tr>
                    <tr><td>EIN:</td><td>XX-XXXXXXX</td></tr>
                    <tr><td>Property State Registration:</td><td>Active (TX)</td></tr>
                    <tr><td>Guarantee Type:</td><td>Full Recourse</td></tr>
                </table>
            </div>

            <div class="credit-analysis">
                <h3>Credit Analysis</h3>
                <div class="credit-highlights">
                    <h4>Credit Highlights</h4>
                    <ul class="highlight-list">
                        <li class="warning">⚠️ Middle FICO of 655 is 5 points below 660 minimum
                            <br><em>→ Mitigated by: Strong experience, excess liquidity, low leverage</em>
                        </li>
                        <li class="pass">✅ 8 active trade lines with 10+ years history</li>
                        <li class="pass">✅ No mortgage lates in past 24 months</li>
                        <li class="pass">✅ No bankruptcy, foreclosure, or short sale history</li>
                        <li class="pass">✅ No open collections or judgments</li>
                        <li class="pass">✅ 28% utilization across revolving accounts</li>
                    </ul>
                </div>
            </div>

            <div class="background-check">
                <h3>Background Check Summary</h3>
                <ul class="background-list">
                    <li class="pass">✅ Clear criminal background check - no financial crimes</li>
                    <li class="pass">✅ No active civil litigation</li>
                    <li class="pass">✅ OFAC/AML screening passed</li>
                    <li class="pass">✅ No UCC filings that conflict with proposed financing</li>
                    <li class="pass">✅ No unresolved tax liens or judgments</li>
                </ul>
            </div>

            <div class="experience-summary">
                <h3>Experience & Track Record</h3>
                <table class="experience-table">
                    <tr><td>Verified Experience (36 months):</td><td>8 deals</td></tr>
                    <tr><td>Lifetime Experience:</td><td>12 deals</td></tr>
                    <tr><td>Borrower Classification:</td><td>Class A (FICO 655 + 8 deals = 58 points)</td></tr>
                </table>

                <h4>Recent Deals:</h4>
                <ol>
                    <li>456 Oak St, Houston TX - Mar 2024 - Sold ($45K profit)</li>
                    <li>789 Pine Ave, Houston TX - Nov 2023 - Sold ($52K profit)</li>
                    <li>321 Elm Blvd, Houston TX - Jul 2023 - Sold ($38K profit)</li>
                </ol>

                <h4>Track Record Highlights:</h4>
                <ul>
                    <li>Average project duration: 5.5 months</li>
                    <li>Average profit per deal: $42,000</li>
                    <li>No project losses</li>
                    <li>100% of projects completed on-time</li>
                </ul>
            </div>

            <div class="financial-strength">
                <h3>Financial Strength</h3>

                <h4>Liquidity Analysis</h4>
                <table class="liquidity-table">
                    <tr><td>Cash / Checking:</td><td>$65,000</td></tr>
                    <tr><td>Savings / Money Market:</td><td>$95,000</td></tr>
                    <tr><td>Investment Accounts (70%):</td><td>$25,000</td></tr>
                    <tr class="total"><td><strong>Total Verified Liquidity:</strong></td><td><strong>$185,000</strong></td></tr>
                </table>

                <h4>Liquidity Requirements</h4>
                <table class="requirements-table">
                    <tr><td>Down Payment:</td><td>$95,000</td></tr>
                    <tr><td>Closing Costs:</td><td>$12,500</td></tr>
                    <tr><td>Reserves (6 months PITIA):</td><td>$34,500</td></tr>
                    <tr class="total"><td><strong>Total Required:</strong></td><td><strong>$142,000</strong></td></tr>
                </table>

                <p class="surplus"><strong>Surplus:</strong> $43,000 (130% of requirement) ✅</p>
            </div>
        </section>

        <!-- SECTION 3: PROPERTY ANALYSIS -->
        <section class="memo-section" id="memo-property-analysis">
            <h2>3. Property Analysis</h2>

            <div class="property-overview">
                <h3>Property Overview</h3>
                <table class="property-table">
                    <tr><td>Address:</td><td>123 Main Street</td></tr>
                    <tr><td>City, State, Zip:</td><td>Austin, TX 78701</td></tr>
                    <tr><td>County:</td><td>Travis County</td></tr>
                    <tr><td>Property Type:</td><td>Single Family Residence</td></tr>
                    <tr><td>Bedrooms / Bathrooms:</td><td>3 / 2</td></tr>
                    <tr><td>Square Footage:</td><td>1,850 sf</td></tr>
                    <tr><td>Lot Size:</td><td>0.18 acres (7,840 sf)</td></tr>
                    <tr><td>Year Built:</td><td>1985</td></tr>
                    <tr><td>Zoning:</td><td>SF-3 (Single Family Residential)</td></tr>
                </table>
            </div>

            <div class="market-summary">
                <h3>Market Summary</h3>
                <table class="market-table">
                    <tr><td>MSA:</td><td>Austin-Round Rock-Georgetown, TX</td></tr>
                    <tr><td>Population:</td><td>2.3 million</td></tr>
                    <tr><td>Median Household Income:</td><td>$85,000</td></tr>
                    <tr><td>Median Home Price:</td><td>$525,000</td></tr>
                    <tr><td>YoY Appreciation:</td><td>+6.2%</td></tr>
                    <tr><td>Days on Market (Median):</td><td>28 days</td></tr>
                    <tr><td>Market Trend:</td><td>Appreciating</td></tr>
                </table>
            </div>

            <div class="condition-assessment">
                <h3>Condition Assessment</h3>
                <p><strong>Condition Rating:</strong> C4</p>
                <p>Property is adequately maintained with minor deferred maintenance. Kitchen and bathrooms
                   are dated and will be fully renovated. Roof has 5+ years remaining life. HVAC system
                   is 12 years old and will be replaced as part of rehabilitation.</p>
            </div>

            <div class="valuation-summary">
                <h3>Valuation</h3>
                <table class="valuation-table">
                    <tr><td>As-Is Value:</td><td>$425,000</td></tr>
                    <tr><td>After-Repair Value:</td><td>$485,000</td></tr>
                    <tr><td>Value Created:</td><td>$60,000 (14% increase)</td></tr>
                    <tr><td>Appraisal Date:</td><td>November 18, 2024</td></tr>
                    <tr><td>Appraiser:</td><td>John Smith, SRA (TX-12345)</td></tr>
                </table>
            </div>
        </section>

        <!-- SECTION 4: DEAL ECONOMICS -->
        <section class="memo-section" id="memo-deal-economics">
            <h2>4. Deal Economics</h2>

            <div class="sources-uses">
                <h3>Sources and Uses</h3>

                <div class="sources-uses-grid">
                    <div class="sources">
                        <h4>Sources of Funds</h4>
                        <table>
                            <tr><td>Loan Proceeds (Initial):</td><td>$297,500</td></tr>
                            <tr><td>Rehab Holdback:</td><td>$85,000</td></tr>
                            <tr><td>Borrower Equity:</td><td>$95,000</td></tr>
                            <tr class="total"><td><strong>Total Sources:</strong></td><td><strong>$477,500</strong></td></tr>
                        </table>
                    </div>

                    <div class="uses">
                        <h4>Uses of Funds</h4>
                        <table>
                            <tr><td>Purchase Price:</td><td>$340,000</td></tr>
                            <tr><td>Closing Costs:</td><td>$12,500</td></tr>
                            <tr><td>Rehab Budget:</td><td>$85,000</td></tr>
                            <tr><td>Interest Reserve (3 months):</td><td>$10,000</td></tr>
                            <tr><td>Contingency:</td><td>$30,000</td></tr>
                            <tr class="total"><td><strong>Total Uses:</strong></td><td><strong>$477,500</strong></td></tr>
                        </table>
                    </div>
                </div>
            </div>

            <div class="leverage-analysis">
                <h3>Leverage Analysis</h3>
                <table class="leverage-table">
                    <tr><td>As-Is LTV:</td><td>65%</td><td>(Max: 75%)</td><td class="pass">✅ 10pt cushion</td></tr>
                    <tr><td>Loan-to-Cost (LTC):</td><td>75%</td><td>(Max: 85%)</td><td class="pass">✅ 10pt cushion</td></tr>
                    <tr><td>Loan-to-ARV (LTARV):</td><td>73%</td><td>(Max: 75%)</td><td class="pass">✅ 2pt cushion</td></tr>
                </table>
                <p><strong>Binding Constraint:</strong> LTARV at 73%</p>
            </div>

            <div class="pricing-summary">
                <h3>Pricing</h3>
                <table class="pricing-table">
                    <tr><td>Interest Rate:</td><td>10.6%</td></tr>
                    <tr><td>Origination Points:</td><td>2.0%</td></tr>
                    <tr><td>YSP:</td><td>1.0%</td></tr>
                </table>
                <p><em>Note: 10bps rate adjustment applied per credit exception approval.</em></p>
            </div>

            <div class="exit-strategy">
                <h3>Exit Strategy</h3>
                <p><strong>Primary Exit:</strong> Sale</p>
                <table class="exit-table">
                    <tr><td>Projected Sale Price:</td><td>$485,000</td></tr>
                    <tr><td>Selling Costs (8%):</td><td>($38,800)</td></tr>
                    <tr><td>Net Sale Proceeds:</td><td>$446,200</td></tr>
                    <tr><td>Loan Payoff:</td><td>($382,500)</td></tr>
                    <tr><td>Holding Costs:</td><td>($15,000)</td></tr>
                    <tr class="total"><td><strong>Net Profit to Borrower:</strong></td><td><strong>$48,700</strong></td></tr>
                </table>
                <p><strong>Return on Investment:</strong> 51% | <strong>Annualized ROI:</strong> 102% (6-month hold)</p>
            </div>
        </section>

        <!-- SECTION 5: THIRD-PARTY REPORTS -->
        <section class="memo-section" id="memo-third-party">
            <h2>5. Third-Party Report Summary</h2>

            <div class="appraisal-summary">
                <h3>Appraisal Summary</h3>
                <table>
                    <tr><td>Appraiser:</td><td>John Smith, SRA (TX-12345)</td></tr>
                    <tr><td>Report Date:</td><td>November 18, 2024</td></tr>
                    <tr><td>As-Is Value:</td><td>$425,000</td></tr>
                    <tr><td>ARV:</td><td>$485,000</td></tr>
                    <tr><td>Condition:</td><td>C4</td></tr>
                </table>
                <p class="note warning">⚠️ ARV variance of 8% from feasibility requires exception (threshold: 5%)</p>
            </div>

            <div class="title-summary">
                <h3>Title Summary</h3>
                <table>
                    <tr><td>Title Company:</td><td>ABC Title Company</td></tr>
                    <tr><td>Commitment Date:</td><td>December 12, 2024</td></tr>
                    <tr><td>Policy Amount:</td><td>$382,500</td></tr>
                    <tr><td>Liens/Encumbrances:</td><td>None (clear title)</td></tr>
                </table>
                <p class="note">⚠️ Standard utility easement on rear 10ft noted in Schedule B-II</p>
            </div>

            <div class="insurance-summary">
                <h3>Insurance Summary</h3>
                <table>
                    <tr><td>Carrier:</td><td>XYZ Insurance</td></tr>
                    <tr><td>Policy Number:</td><td>POL-123456</td></tr>
                    <tr><td>Coverage Amount:</td><td>$425,000</td></tr>
                    <tr><td>Effective Date:</td><td>December 15, 2024</td></tr>
                    <tr><td>Expiration Date:</td><td>October 15, 2025</td></tr>
                    <tr><td>Mortgagee Clause:</td><td>Correct</td></tr>
                </table>
                <p class="note warning">⚠️ Policy expires before loan maturity (10/15/25 vs 12/15/25)</p>
            </div>
        </section>

        <!-- SECTION 6: RISK ASSESSMENT -->
        <section class="memo-section" id="memo-risk-assessment">
            <h2>6. Risk Assessment</h2>

            <div class="overall-risk">
                <h3>Overall Risk Rating</h3>
                <div class="risk-gauge">
                    <span class="risk-score">35</span>
                    <span class="risk-rating moderate">MODERATE RISK</span>
                </div>
                <p class="risk-rationale">
                    Deal presents moderate risk due to FICO shortfall and ARV variance. These are substantially
                    mitigated by strong borrower experience, conservative leverage, and excess liquidity.
                    Recommend approval with conditions.
                </p>
            </div>

            <div class="risk-factors">
                <h3>Risk Factors by Category</h3>
                <table class="risk-factors-table">
                    <thead>
                        <tr>
                            <th>Category</th>
                            <th>Risk Level</th>
                            <th>Description</th>
                            <th>Mitigant</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Credit</td>
                            <td><span class="risk-badge moderate">Moderate</span></td>
                            <td>FICO 655 below 660 minimum</td>
                            <td>Strong experience, reserves, rate adjustment</td>
                        </tr>
                        <tr>
                            <td>Valuation</td>
                            <td><span class="risk-badge moderate">Moderate</span></td>
                            <td>8% ARV variance</td>
                            <td>Conservative LTV provides cushion</td>
                        </tr>
                        <tr>
                            <td>Experience</td>
                            <td><span class="risk-badge low">Low</span></td>
                            <td>8 projects completed</td>
                            <td>N/A - strength</td>
                        </tr>
                        <tr>
                            <td>Market</td>
                            <td><span class="risk-badge low">Low</span></td>
                            <td>Strong Austin market</td>
                            <td>N/A - strength</td>
                        </tr>
                        <tr>
                            <td>Execution</td>
                            <td><span class="risk-badge moderate">Moderate</span></td>
                            <td>Aggressive 4-month timeline</td>
                            <td>Draw inspection schedule, experienced GC</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="flag-summary">
                <h3>Flag Summary</h3>
                <table class="flag-summary-table">
                    <tr><td>🔴 Red Flags:</td><td>2</td><td>FICO (exception approved), ARV variance (pending)</td></tr>
                    <tr><td>⚠️ Yellow Flags:</td><td>5</td><td>Experience, large deposit, easement, appraisal age, insurance term</td></tr>
                    <tr><td>✅ Green Flags:</td><td>28</td><td>All other checks passed</td></tr>
                </table>
            </div>
        </section>

        <!-- SECTION 7: CONDITIONS & EXCEPTIONS -->
        <section class="memo-section" id="memo-conditions">
            <h2>7. Conditions & Exceptions</h2>

            <div class="conditions-precedent">
                <h3>Conditions Precedent to Closing</h3>
                <ul>
                    <li>✅ Credit exception approved (10bps rate adjustment)</li>
                    <li>⏳ ARV variance exception pending investor approval</li>
                    <li>⏳ Verify contractor bids for rehab budget</li>
                    <li>⏳ Obtain insurance policy renewal commitment through loan maturity</li>
                    <li>✅ Standard draw inspection schedule</li>
                </ul>
            </div>

            <div class="exceptions-list">
                <h3>Exceptions Requested</h3>
                <table class="exceptions-table">
                    <thead>
                        <tr>
                            <th>Type</th>
                            <th>Description</th>
                            <th>Status</th>
                            <th>Conditions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Credit - FICO</td>
                            <td>FICO 655 (5 pts below 660 min)</td>
                            <td><span class="status-badge approved">Approved</span></td>
                            <td>10bps rate adjustment</td>
                        </tr>
                        <tr>
                            <td>Valuation - ARV</td>
                            <td>8% ARV variance (5% threshold)</td>
                            <td><span class="status-badge pending">Pending</span></td>
                            <td>-</td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <div class="recommendation-final">
                <h3>Final Recommendation</h3>
                <div class="recommendation-box approved-with-conditions">
                    <h4>APPROVE WITH CONDITIONS</h4>
                    <ul>
                        <li>Credit exception approved with 10bps rate adjustment</li>
                        <li>ARV variance exception pending investor approval</li>
                        <li>Verify contractor bids for rehab budget</li>
                        <li>Standard draw inspection schedule</li>
                    </ul>
                </div>

                <div class="pricing-final">
                    <h4>Pricing Summary</h4>
                    <table>
                        <tr><td>Rate:</td><td>10.6%</td></tr>
                        <tr><td>Origination:</td><td>2.0%</td></tr>
                        <tr><td>Term:</td><td>12 months</td></tr>
                    </table>
                </div>

                <div class="underwriter-notes">
                    <h4>Underwriter Notes</h4>
                    <p>
                        Strong borrower profile mitigates FICO concern. Repeat borrower with 8 projects and
                        perfect payment history. ARV variance within acceptable range given conservative LTV.
                        Recommend standard draw inspection schedule given 4-month timeline.
                    </p>
                </div>
            </div>
        </section>

        <!-- MEMO FOOTER / SIGNATURES -->
        <footer class="memo-footer">
            <div class="signature-block">
                <div class="signature">
                    <p>Prepared by INSPIRE AI Analysis</p>
                    <p>Date: December 15, 2024</p>
                </div>
                <div class="signature">
                    <p>Reviewed by: ____________________</p>
                    <p>Date: ____________________</p>
                </div>
                <div class="signature">
                    <p>Approved by: ____________________</p>
                    <p>Date: ____________________</p>
                </div>
            </div>
        </footer>

    </div>

    <!-- Memo Actions Footer -->
    <div class="memo-actions-footer">
        <button onclick="approveCreditMemo()" class="primary-btn">Approve Memo</button>
        <button onclick="requestChanges()">Request Changes</button>
        <button onclick="regenerateCreditMemo()">Regenerate with Updates</button>
    </div>
</div>
```

---

## TASK 7: Add JavaScript Navigation Functions

### 7.1 Add Phase 7 Navigation Functions

**Location:** Add to the existing `<script>` section at the bottom of the HTML file

```javascript
// ===== PHASE 7: AI ANALYSIS FUNCTIONS =====

// Flag filtering
function filterFlags(severity) {
    console.log('Filter flags by:', severity);
    // In real implementation: filter the flag display
    alert('Filtering flags by: ' + severity);
}

// Section toggle for collapsible sections
function toggleSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.classList.toggle('collapsed');
    }
}

// View document analysis detail
function viewDocAnalysis(docType) {
    console.log('View analysis for:', docType);
    showModal('modal-doc-analysis');
}

// Re-analyze document
function reanalyzeDoc(docType) {
    console.log('Re-analyzing:', docType);
    alert('Re-analyzing document: ' + docType);
}

// Analyze pending document
function analyzeDoc(docType) {
    console.log('Analyzing:', docType);
    alert('Starting analysis for: ' + docType);
}

// Re-analyze all documents
function reanalyzeAll() {
    alert('Re-analyzing all documents. This may take a few minutes...');
}

// Navigate to credit memo tab
function navigateToCreditMemo() {
    switchDealTab('tab-credit-memo');
}

// Export flags
function exportFlags() {
    alert('Exporting flags to CSV...');
}

function exportFlagsCSV() {
    alert('Exporting all flags to CSV...');
}

// ===== FLAG ACTIONS =====

function requestException(flagId) {
    console.log('Requesting exception for flag:', flagId);
    showModal('modal-exception-request');
}

function resolveFlag(flagId) {
    console.log('Resolving flag:', flagId);
    alert('Mark flag as resolved: ' + flagId);
}

function acknowledgeFlag(flagId) {
    console.log('Acknowledging flag:', flagId);
    alert('Flag acknowledged: ' + flagId);
}

function requestLOE(flagId) {
    console.log('Requesting LOE for flag:', flagId);
    alert('Letter of Explanation requested');
}

function orderRecertification() {
    alert('Ordering appraisal recertification...');
}

function requestRenewal() {
    alert('Requesting insurance policy renewal...');
}

// Bulk actions
function bulkAcknowledge() {
    alert('Bulk acknowledging selected flags...');
}

// ===== EXCEPTION FUNCTIONS =====

function addCompensatingFactor() {
    alert('Adding new compensating factor row...');
}

function saveExceptionDraft() {
    alert('Exception request saved as draft.');
}

function submitException() {
    alert('Exception request submitted to investor.');
    closeModal('modal-exception-request');
}

function viewExceptionDetail(exceptionId) {
    console.log('View exception:', exceptionId);
    alert('Viewing exception: ' + exceptionId);
}

function withdrawException(exceptionId) {
    if (confirm('Are you sure you want to withdraw this exception request?')) {
        alert('Exception withdrawn: ' + exceptionId);
    }
}

function showExceptionTemplate() {
    alert('Opening USDV Exception Request Template...');
}

function downloadExceptionTemplate() {
    alert('Downloading exception template...');
}

// ===== CREDIT MEMO FUNCTIONS =====

function regenerateCreditMemo() {
    if (confirm('This will regenerate the credit memo with latest data. Continue?')) {
        alert('Regenerating credit memo...');
    }
}

function editCreditMemo() {
    alert('Opening credit memo editor...');
}

function exportCreditMemo(format) {
    alert('Exporting credit memo as ' + format.toUpperCase() + '...');
}

function approveCreditMemo() {
    if (confirm('Approve this credit memo?')) {
        alert('Credit memo approved.');
    }
}

function requestChanges() {
    alert('Opening change request dialog...');
}

// ===== DOCUMENT VIEWER =====

function viewPDF(docType) {
    console.log('Opening PDF viewer for:', docType);
    alert('Opening document viewer for: ' + docType);
}

function viewDocument(docType) {
    console.log('View document:', docType);
    alert('Opening document: ' + docType);
}

// Filter document analysis
function filterDocAnalysis(filter) {
    console.log('Filtering document analysis:', filter);
}
```

---

## TASK 8: Update Dashboard with Phase 7 Elements

### 8.1 Update "Needs Attention" Section with AI Flags

**Location:** In `view-dashboard`, update the "Needs Attention" section to include AI analysis alerts

Find the existing "Needs Attention" section and add/update:

```html
<!-- 1. NEEDS ATTENTION (Priority) - Updated with AI Analysis -->
<section class="dashboard-group state-warning">
    <h2>🔴 Needs Attention</h2>
    <ul>
        <li>
            <span class="badge ai-flag">AI Flag</span>
            <strong>123 Main St</strong> - Red Flag: FICO 655 below 660 minimum (Exception Pending)
            <button onclick="navigateToDeal('123', 'analysis')">View Analysis</button>
            <button onclick="navigateToDeal('123', 'exceptions')">View Exception</button>
        </li>
        <li>
            <span class="badge ai-flag">AI Flag</span>
            <strong>123 Main St</strong> - Red Flag: ARV variance 8% exceeds 5% threshold
            <button onclick="navigateToDeal('123', 'analysis')">Request Exception</button>
        </li>
        <li>
            <strong>456 Oak Ave</strong> - Past Target Close (Dec 28)
            <button onclick="navigateToDeal('456', 'overview')">View</button>
        </li>
        <li>
            <span class="badge doc-expiring">Expiring</span>
            <strong>789 Pine Rd</strong> - Appraisal expires in 5 days
            <button onclick="navigateToDeal('789', 'checklist')">Order Recertification</button>
        </li>
    </ul>
</section>
```

### 8.2 Add Credit Memo Status to KPIs

**Location:** In `view-dashboard`, add a KPI card for credit memo status

```html
<!-- Add to kpi-grid -->
<article class="kpi-card">
    <h3>Credit Memos</h3>
    <span class="value">3</span>
    <span class="subtext">Ready for Review</span>
    <button onclick="navigateTo('pipeline')">View All</button>
</article>
```

---

## TASK 9: Update Pipeline Cards with Analysis Indicators

### 9.1 Add Flag Indicators to Deal Cards

**Location:** Update existing deal cards in the kanban board to show flag counts

Update deal cards in Processing and Underwriting stages to show:

```html
<article class="deal-card state-warning" onclick="navigateToDeal('123', 'overview')">
    <div class="card-header">
        <span class="address">123 Main St</span>
        <span class="badge">F&F</span>
    </div>
    <div class="metrics">$382.5k • Eastview</div>

    <!-- Phase 7: Flag indicators -->
    <div class="analysis-indicators">
        <span class="flag-indicator red" title="2 Red Flags">🔴 2</span>
        <span class="flag-indicator yellow" title="5 Yellow Flags">⚠️ 5</span>
        <span class="memo-status" title="Credit Memo Ready">📋 Ready</span>
    </div>

    <div class="tasks">📋 3 Tasks</div>
</article>
```

---

## TASK 10: Testing Checklist

After implementing all tasks, verify the following:

### Navigation Tests
- [ ] Analysis (AI) tab loads and displays content
- [ ] Credit Memo tab loads and displays full memo
- [ ] Exceptions tab loads and displays exception list
- [ ] All tab switching works correctly
- [ ] Back navigation works from all views

### Analysis Dashboard Tests
- [ ] Summary cards display (Risk Score, Flag Counts, Documents, Exceptions)
- [ ] Red flags section displays with action buttons
- [ ] Yellow flags section is collapsible
- [ ] Green flags section is collapsible
- [ ] Document analysis table displays all documents
- [ ] Category score breakdown displays

### Flag Manager Tests
- [ ] Flag manager modal opens
- [ ] Filters work (severity, category, status)
- [ ] Flag actions are clickable (View, Request Exception, Acknowledge)

### Exception Request Tests
- [ ] Exception request modal opens from flag actions
- [ ] Form fields are populated with flag context
- [ ] Compensating factors checkboxes work
- [ ] Submit and Save Draft buttons are clickable

### Credit Memo Tests
- [ ] All 7 sections of credit memo display
- [ ] Tables render correctly with data
- [ ] Export buttons are functional
- [ ] Approve button shows confirmation

### Dashboard Integration Tests
- [ ] "Needs Attention" shows AI flags
- [ ] Pipeline deal cards show flag indicators
- [ ] Navigation from dashboard to analysis works

---

## Reference Files

When implementing, reference these files for patterns and data:

1. **PRD:** `_PRDs/inspire-phase-7-prd.md` - Full requirements
2. **Implementation Plan:** `_PRDs/implementation-plans/phase-7-implementation.md` - Detailed specs
3. **Underwriting Manual:**
   - `USDV_Underwriting_Manual/sections/12_exception_management.md` - Exception types and process
   - `USDV_Underwriting_Manual/sections/15_credit_memo_risk_assessment.md` - Credit memo structure
4. **Existing HTML:** `inspire-ux.html` - Patterns for tabs, modals, cards
5. **Mock Data Catalog:** `_PRDs/implementation-plans/mock-data-catalog.md` - Sample data patterns

---

## Notes for Cursor

1. **Follow existing patterns** - Use the same HTML structure, class naming, and JavaScript patterns as existing tabs
2. **Keep it semantic** - Use appropriate HTML5 elements (article, section, header, footer)
3. **Add component comments** - Include comments indicating which ShadCN components would be used in production
4. **Use consistent mock data** - The deal at 123 Main St should have consistent data across all views
5. **State indicators** - Use `state-error`, `state-warning`, `state-success` classes for visual states
6. **Collapsible sections** - Use the `collapsible` class and `toggleSection()` function for expandable content

---

*End of Phase 7 Cursor Implementation Task Plan*
