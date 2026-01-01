# INSPIRE - Phase 1-2 Product Requirements Document

**Product Name:** INSPIRE  
**Company:** USDV Capital  
**Document Type:** Phase 1-2 PRD (Intake / Pre-Qual + Full Application)  
**Version:** 1.0  
**Last Updated:** November 2025

---

## 1. Overview

This PRD covers the first two phases of INSPIRE's loan origination workflow:

- **Phase 1: Intake / Pre-Qualification (Quick App)** - Initial deal screening for new and existing clients
- **Phase 2: Full Application** - Comprehensive digital loan application by product type

These phases represent the borrower's entry point into INSPIRE and establish the foundation for all downstream processes.

---

## 2. Goals & Success Metrics

### Goals

1. Enable rapid deal intake with minimal friction
2. Pre-qualify deals before investing underwriting resources
3. Capture all required application data digitally
4. Leverage existing client data to reduce redundant entry
5. Create a mobile-friendly experience completable in ≤5 minutes per property

### Success Metrics

| Metric | Target |
|--------|--------|
| Quick App completion rate | >85% |
| Quick App average completion time | <3 minutes |
| Full App completion rate | >80% |
| Full App average completion time | <5 minutes per property |
| Data pre-fill accuracy | >95% |
| Mobile completion rate | >40% of submissions |

---

## 3. User Flows

### 3.1 High-Level User Journey

```
┌─────────────────────────────────────────────────────────────────────┐
│                         DEAL INTAKE                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────────────┐ │
│  │  New Client  │     │   Existing   │     │  Real Estate CFO     │ │
│  │              │     │   Client     │     │  Client              │ │
│  └──────┬───────┘     └──────┬───────┘     └──────────┬───────────┘ │
│         │                    │                        │             │
│         ▼                    ▼                        ▼             │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────────────┐ │
│  │  Quick App   │     │    OAuth     │     │       OAuth          │ │
│  │  (Public)    │     │    Login     │     │       Login          │ │
│  └──────┬───────┘     └──────┬───────┘     └──────────┬───────────┘ │
│         │                    │                        │             │
│         │                    ▼                        ▼             │
│         │             ┌──────────────┐     ┌──────────────────────┐ │
│         │             │ Select Entity│     │  Most Data Pre-      │ │
│         │             │ + Pre-Fill   │     │  Filled from CFO.ai  │ │
│         │             └──────┬───────┘     └──────────┬───────────┘ │
│         │                    │                        │             │
│         ▼                    ▼                        ▼             │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │                    PRE-QUALIFICATION                            ││
│  │                                                                 ││
│  │    ┌─────────────┐                    ┌─────────────┐          ││
│  │    │  QUALIFIED  │                    │ DISQUALIFIED│          ││
│  │    └──────┬──────┘                    └──────┬──────┘          ││
│  │           │                                  │                 ││
│  │           ▼                                  ▼                 ││
│  │    ┌─────────────┐                    ┌─────────────┐          ││
│  │    │    FULL     │                    │   Friendly  │          ││
│  │    │ APPLICATION │                    │   Denial +  │          ││
│  │    │  (Phase 2)  │                    │   Add to    │          ││
│  │    │             │                    │  Newsletter │          ││
│  │    └─────────────┘                    └─────────────┘          ││
│  └─────────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────┘
```

---

## 4. Phase 1: Intake / Pre-Qualification (Quick App)

### 4.1 Overview

The Quick App is a lightweight, public-facing form embedded at `borrower.usdvcapital.com` that allows prospective borrowers to submit initial deal information for pre-qualification.

### 4.2 Access Paths

#### Path A: New Client (No Auth Required)
- Public form at `borrower.usdvcapital.com`
- No login required
- Captures all required pre-qual data from scratch

#### Path B: Existing Client (OAuth Login)
- Login via Google OAuth or email/password
- System recognizes client and pre-fills known sponsor information
- Client selects which borrowing entity to use
- Pre-qualification fields auto-populate from stored data

#### Path C: Real Estate CFO.ai Client (OAuth Login)
- Same login flow as existing client
- Maximum pre-fill from CFO.ai integration (future)
- Sponsor info, entity docs, PFS, track record already on file

### 4.3 Quick App Form Fields

#### Section 1: Sponsor Information

| Field | Type | Required | Validation | Notes |
|-------|------|----------|------------|-------|
| Full Legal Name | Text | Yes | Min 2 chars | Primary guarantor |
| Email | Email | Yes | Valid email format | Used for account creation |
| Phone | Phone | Yes | Valid phone format | |
| Estimated Credit Score | Dropdown | Yes | 300-850 range | Options: <620, 620-659, 660-699, 700-739, 740-779, 780+ |

#### Section 2: Co-Guarantors (Optional, Repeatable)

| Field | Type | Required | Validation | Notes |
|-------|------|----------|------------|-------|
| Are there co-guarantors? | Boolean | Yes | | If yes, show fields below |
| Co-Guarantor Name | Text | Conditional | Min 2 chars | |
| Co-Guarantor Est. Credit Score | Dropdown | Conditional | Same options | |

*Allow adding up to 5 co-guarantors*

#### Section 3: Experience Metrics

| Field | Type | Required | Validation | Notes |
|-------|------|----------|------------|-------|
| Fix & Flip deals completed (last 3 years) | Number | Yes | ≥0 | |
| Ground-up construction deals completed (last 3 years) | Number | Yes | ≥0 | |
| Rental properties currently owned | Number | Yes | ≥0 | |

#### Section 4: Loan Type Selection

| Field | Type | Required | Options |
|-------|------|----------|---------|
| Loan Type | Radio | Yes | Fix & Flip / Bridge, Ground-Up Construction, DSCR Permanent |

*Loan type selection controls which additional fields appear*

#### Section 5: Property Information

| Field | Type | Required | Validation | Notes |
|-------|------|----------|------------|-------|
| Property Address | Address Autocomplete | Yes | Valid US address | Google Places API |
| Property Type | Radio | Yes | Single Family, Commercial | |
| *If Single Family:* | | | | |
| Bedrooms | Number | Conditional | 1-20 | |
| Bathrooms | Number | Conditional | 1-20 | Allow decimals (2.5) |
| Square Footage | Number | Conditional | >0 | |
| *If Commercial:* | | | | |
| Commercial Type | Dropdown | Conditional | Multifamily, Hospitality, Retail, Office, Industrial, Mixed-Use | Flag for manual review |

#### Section 6: Deal Economics (Conditional by Loan Type)

**For Fix & Flip / Bridge:**

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| Do you already own the property? | Boolean | Yes | |
| Purchase Price (if not owned) | Currency | Conditional | >0 |
| Original Purchase Price (if owned) | Currency | Conditional | >0 |
| Renovation/Rehab Budget | Currency | Yes | ≥0 |
| After Repair Value (ARV) | Currency | Yes | >0 |

**For Ground-Up Construction:**

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| Do you already own the land? | Boolean | Yes | |
| Land Purchase Price (if not owned) | Currency | Conditional | >0 |
| Original Land Purchase Price (if owned) | Currency | Conditional | >0 |
| Construction Budget | Currency | Yes | >0 |
| After Repair Value (ARV) | Currency | Yes | >0 |

**For DSCR Permanent:**

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| Current Property Value | Currency | Yes | >0 |
| Projected Monthly Rent | Currency | Yes | >0 |
| Annual Property Taxes | Currency | Yes | ≥0 |
| Annual Insurance | Currency | Yes | ≥0 |
| Monthly HOA (if applicable) | Currency | No | ≥0 |
| After Repair Value (ARV) | Currency | Yes | >0 |

### 4.4 Pre-Qualification Logic

The system evaluates the Quick App submission against basic criteria:

**Auto-Disqualify Conditions:**
- Estimated credit score <620 (all guarantors)
- Zero experience for Ground-Up Construction
- Commercial property type (flag for manual review, not auto-disqualify)

**Qualified Path:**
- Meets minimum credit threshold
- Has relevant experience for loan type
- Property type is eligible

### 4.5 Disqualification Flow

If the deal does not pass pre-qualification:

1. Display friendly denial message explaining why
2. Capture email for newsletter/nurture
3. Add lead to CRM with disqualification reason
4. Offer to contact USDV for questions

**Denial Message Template:**
```
Thank you for your interest in USDV Capital!

Based on the information provided, this deal doesn't currently fit 
within our lending guidelines because [REASON].

We'd love to stay in touch. We've added you to our newsletter where 
we share market insights and lending updates.

If you have questions or believe there's additional context we 
should consider, please contact us at loans@usdvcapital.com.
```

### 4.6 Quick App UX Requirements

- **Progress Indicator:** Show step X of Y
- **Auto-Save:** Save progress on each field blur (for logged-in users)
- **Mobile-First Design:** Fully responsive, thumb-friendly inputs
- **Address Autocomplete:** Google Places API integration
- **Inline Validation:** Real-time error feedback
- **Conditional Logic:** Show/hide fields based on selections
- **Completion Time:** Target <3 minutes

---

## 5. Phase 2: Full Application

### 5.1 Overview

Upon passing pre-qualification, the borrower proceeds to the Full Application. This is a comprehensive digital form that captures all information needed to size the deal and proceed to underwriting.

### 5.2 Application Tracks

Based on Loan Type selected in Quick App:

1. **Fix & Flip / Bridge Application**
2. **Ground-Up Construction Application**
3. **DSCR Rental Application**

### 5.3 Data Pre-Fill from Quick App

All applicable fields from Phase 1 pre-populate into Phase 2:

| Quick App Field | Full App Field |
|-----------------|----------------|
| Sponsor full name | Primary Guarantor: First Name, Last Name |
| Email | Primary Guarantor: Email |
| Phone | Primary Guarantor: Phone |
| Estimated credit score | Estimated Credit Score |
| Co-guarantor names + scores | Additional Guarantors section |
| Property address | Property Address |
| Loan type | Application track + Loan Purpose |
| Property type (SF/Commercial) | Property Type |
| Bedrooms / Bathrooms | Unit details |
| Property owned status | Lot Status / Refinance indicator |
| Purchase price | Purchase Price / Lot Purchase Price |
| Rehab/Construction budget | Total Budget |
| Projected rent (DSCR) | Estimated Market Monthly Rent |
| Expenses (DSCR) | Annual Taxes, Insurance, HOA |
| ARV | Estimated After Repair Value |
| Experience metrics | Experience section |

### 5.4 Shared Application Components (All Loan Types)

#### 5.4.1 Borrowing Entity Information

| Field | Type | Required | Options/Validation |
|-------|------|----------|-------------------|
| Entity Name | Text | Yes | Or "TBD" if unknown |
| Company Type | Radio | Yes | Limited Partnership, LLC, Corporation, Other |
| Business EIN | Text (masked) | Yes | XX-XXXXXXX format |
| Registered States | Multi-select | Yes | US States |

#### 5.4.2 Borrowing Entity Ownership

*Repeatable section for each owner*

| Field | Type | Required |
|-------|------|----------|
| First Name | Text | Yes |
| Last Name | Text | Yes |
| Ownership % | Percentage | Yes |

*Validation: Ownership must total 100%*

*Support for org chart upload if nested entities*

#### 5.4.3 Aggregate Experience (All Guarantors Combined)

| Field | Type | Required |
|-------|------|----------|
| Areas of RE Operation | Multi-checkbox | Yes |
| Options: Fix & Flip, New Construction, Rentals, Commercial, Multifamily, Mixed Use |
| Rental units owned (bought last 3 years) | Number | Yes |
| Total rental units owned (all time) | Number | Yes |
| Fix & Flips sold (last 3 years) | Number | Yes |
| New Construction builds (last 3 years) | Number | Yes |
| GC Status | Radio | Yes |
| Options: On Staff, Third Party |

#### 5.4.4 Primary Guarantor Information

| Field | Type | Required | Validation |
|-------|------|----------|------------|
| First Name | Text | Yes | |
| Last Name | Text | Yes | |
| Primary Street Address | Text | Yes | |
| City | Text | Yes | |
| State | Dropdown | Yes | US States |
| Zip | Text | Yes | 5 or 9 digit |
| Social Security Number | Text (masked) | Yes | XXX-XX-XXXX |
| Date of Birth | Date | Yes | Must be 18+ |
| Phone Number | Phone | Yes | |
| Email Address | Email | Yes | |
| Country of Citizenship | Dropdown | Yes | |
| Estimated Credit Score | Dropdown | Yes | |

#### 5.4.5 Background Questions (Per Guarantor)

| Question | Type | Required |
|----------|------|----------|
| Convicted of, plead guilty/no contest to, or currently accused of felony or crime involving fraud, financial malfeasance, or misrepresentation? | Yes/No | Yes |
| Party to any outstanding lawsuits? | Yes/No | Yes |
| Have any outstanding judgments? | Yes/No | Yes |
| Declared bankruptcy in past 4 years, or actively involved in bankruptcy? | Yes/No | Yes |
| Had foreclosure, deed in lieu, or short sale in past 3 years? | Yes/No | Yes |
| Recently delinquent on any mortgage or financial obligation? | Yes/No | Yes |

*If any "Yes" → Show text area for detailed explanation*

#### 5.4.6 Additional Guarantors

*Repeatable section - same fields as Primary Guarantor*

Button: "+ Add Co-Guarantor"

#### 5.4.7 Personal Financial Statement

*Option A: Upload existing PFS*
*Option B: Complete in-app:*

**Liquid Assets:**

| Field | Type |
|-------|------|
| Cash | Currency |
| Retirement Accounts | Currency |
| Stocks, Bonds | Currency |
| Other Liquid | Currency |
| **Total Liquid** | Calculated |

**Non-Liquid Assets:**

| Field | Type |
|-------|------|
| Real Estate Assets | Currency |
| Autos | Currency |
| Other Personal Property | Currency |
| **Total Non-Liquid** | Calculated |

**Liabilities:**

| Field | Type |
|-------|------|
| Real Estate Debt | Currency |
| Revolving Debt | Currency |
| Installment Debt | Currency |
| Notes Payable | Currency |
| Other Debt | Currency |
| **Total Debt** | Calculated |

**Net Worth:** Calculated (Total Liquid + Total Non-Liquid - Total Debt)

#### 5.4.8 Credit Authorization (FCRA Consent)

*Display FCRA disclosure text*
*Checkbox: "I authorize USDV Capital to pull my credit report"*
*E-signature field*

#### 5.4.9 Third-Party Contact Information

*Only required for first-time submissions or if contacts differ from prior loans*

**Property Access Contact:**
- Contact Name, Phone, Email

**Title Contact:**
- Company Name, Contact Name, Phone, Email

**Insurance Contact:**
- Company Name, Contact Name, Phone, Email

**Escrow/Closing Agent Contact:**
- Company Name, Contact Name, Phone, Email

---

### 5.5 Fix & Flip / Bridge Application - Property Section

#### 5.5.1 Property Information

| Field | Type | Required | Options |
|-------|------|----------|---------|
| Property Type | Radio | Yes | Single Family, Multi-Family (# units), Townhome, Condo |
| Address | Text | Yes | Pre-filled from Quick App |
| Unit # | Text | No | |
| City, State, Zip | Text | Yes | Pre-filled |

#### 5.5.2 Loan Details

| Field | Type | Required | Options |
|-------|------|----------|---------|
| Loan Purpose | Radio | Yes | Purchase, Refinance, Fix & Flip (rehab in progress), Bridge (no rehab) |
| Exit Strategy | Radio | Yes | Sell, Hold as Rental |
| Target Close Date | Date | Yes | |
| Requested Loan Amount | Currency | Yes | |
| Entity for Closing | Text | Yes | Pre-filled or "TBD" |
| Original Purchase Date (if refi) | Date | Conditional | |
| Time to Exit (months) | Number | Yes | |

#### 5.5.3 Deal Economics

| Field | Type | Required |
|-------|------|----------|
| Purchase Price | Currency | Yes |
| Current Market Value | Currency | Yes |
| Total Rehab Budget Remaining | Currency | Yes |
| Rehab Already Completed (verified) | Currency | Yes |
| Estimated After Repair Value | Currency | Yes |

#### 5.5.4 Property Questions

| Question | Type | Required |
|----------|------|----------|
| Will rehab draws be requested? | Yes/No | Yes |
| Are permits required? | Yes/No | Yes |
| → If yes, do you have permits? | Yes/No | Conditional |
| → If no, when expected? | Date | Conditional |
| Will property type change (e.g., SFR to duplex)? | Yes/No | Yes |
| Zoning changes required? | Yes/No | Yes |
| Intend to subdivide or request partial releases? | Yes/No | Yes |
| Existing mortgage on property? | Yes/No | Yes |
| → If yes, lender name | Text | Conditional |
| → Outstanding balance | Currency | Conditional |
| Other existing liens? | Yes/No | Yes |
| → If yes, lien holder names | Text | Conditional |
| → Outstanding balance | Currency | Conditional |
| Home under contract to be sold? | Yes/No | Yes |
| → Contract amount | Currency | Conditional |
| Using third-party GC? | Yes/No | Yes |
| → If no, does company have licensing? | Yes/No | Conditional |
| Will property have well or septic? | Yes/No | Yes |
| Relocating/adding mechanicals (HVAC, electrical, plumbing)? | Yes/No | Yes |

#### 5.5.5 Structural Questions (Affects Pricing/Eligibility)

*Display warning: "Inaccurately answering may change quoted terms/eligibility"*

| Question | Type | Required |
|----------|------|----------|
| Removing 2+ load-bearing walls? | Yes/No | Yes |
| Adding livable SF to existing structure (e.g., finishing basement/attic)? | Yes/No | Yes |
| Expanding building envelope (e.g., addition, ADU)? | Yes/No | Yes |

---

### 5.6 Ground-Up Construction Application - Property Section

#### 5.6.1 Property Information

| Field | Type | Required | Options |
|-------|------|----------|---------|
| Property Type | Radio | Yes | Single Family, Multi-Family (# units), Townhome, Condo |
| Address | Text | Yes | Pre-filled |
| City, State, Zip | Text | Yes | Pre-filled |

#### 5.6.2 Loan Details

| Field | Type | Required | Options |
|-------|------|----------|---------|
| Loan Purpose | Radio | Yes | Vacant Lot/Ground-Up, Tear Down & Rebuild, Mid-Construction Refinance |
| Lot Status | Radio | Yes | Purchasing Lot, Paying Off Lot Loan, Lot Owned Free & Clear |
| Exit Strategy | Radio | Yes | Sell, Hold as Rental |
| Requesting Cash Out? (if equity) | Yes/No | Conditional | |
| Target Close Date | Date | Yes | |
| Requested Loan Amount | Currency | Yes | |
| Entity for Closing | Text | Yes | |
| Original Purchase Date (if refi) | Date | Conditional | |
| Time to Exit (months) | Number | Yes | |

#### 5.6.3 Deal Economics

| Field | Type | Required |
|-------|------|----------|
| Lot Purchase Price | Currency | Yes |
| Current Lot Market Value | Currency | Yes |
| Total Construction Budget Remaining | Currency | Yes |
| Construction Already Completed (verified) | Currency | Yes |
| Estimated After Repair Value | Currency | Yes |

#### 5.6.4 Property Questions

| Question | Type | Required |
|----------|------|----------|
| Is lot properly zoned and platted with parcel ID? | Yes/No | Yes |
| Do you have required building permits? | Yes/No | Yes |
| → If no, when expected? | Date | Conditional |
| Any construction already completed (demo, foundation, etc.)? | Yes/No | Yes |
| → If yes, cost completed | Currency | Conditional |
| Is lot ready to build within 60 days? | Yes/No | Yes |
| Do you have plans and specs? | Yes/No | Yes |
| Zoning changes required? | Yes/No | Yes |
| Intend to subdivide or request partial releases? | Yes/No | Yes |
| Existing mortgage on lot? | Yes/No | Yes |
| → If yes, lien holder | Text | Conditional |
| → Outstanding balance | Currency | Conditional |
| Other existing liens? | Yes/No | Yes |
| Home under contract to be sold upon completion? | Yes/No | Yes |
| → Contract amount | Currency | Conditional |
| Using third-party GC? | Yes/No | Yes |
| Are utilities available at lot? | Yes/No | Yes |
| Will property have well or septic? | Yes/No | Yes |

---

### 5.7 DSCR Rental Application - Property Section

#### 5.7.1 Property Information

| Field | Type | Required | Options |
|-------|------|----------|---------|
| Property Type | Radio | Yes | Single Family, 2-4 Unit (# units), Townhome, Condo, Multifamily (# units) |
| Address | Text | Yes | Pre-filled |
| City, State, Zip | Text | Yes | Pre-filled |

*For multiple properties: Upload rent roll instead*

#### 5.7.2 Loan Details

| Field | Type | Required | Options |
|-------|------|----------|---------|
| Loan Purpose | Radio | Yes | Purchase, Refinance (Rate & Term), Refinance (Cash Out) |
| Original Purchase Date (if refi) | Date | Conditional | |
| Target Close Date | Date | Yes | |
| Requested Loan Amount | Currency | Yes | |
| Entity for Closing | Text | Yes | |
| Property Manager | Radio | Yes | Self Managed, Professional Management Company |

#### 5.7.3 Deal Economics

| Field | Type | Required |
|-------|------|----------|
| Current As-Is Market Value | Currency | Yes |
| Estimated Market Monthly Rent | Currency | Yes |
| Current Monthly Rent (if leased) | Currency | No |
| Annual Taxes | Currency | Yes |
| Annual Insurance | Currency | Yes |
| Annual HOA Dues | Currency | No |

#### 5.7.4 Property Questions

| Question | Type | Required |
|----------|------|----------|
| All properties currently rented? | Yes/No/NA | Yes |
| → If no, current occupancy % | Percentage | Conditional |
| All properties in rent-ready condition? | Yes/No/NA | Yes |
| Subject to lease purchase option or ground lease? | Yes/No/NA | Yes |
| Existing mortgage? | Yes/No/NA | Yes |
| → Mortgage company | Text | Conditional |
| → Outstanding balance | Currency | Conditional |
| Other existing liens? | Yes/No/NA | Yes |
| → Lien holders | Text | Conditional |
| → Outstanding balance | Currency | Conditional |
| Will sponsors/entity members/family occupy property? | Yes/No | Yes |
| *If refinance:* Properties vested in proposed borrowing entity? | Yes/No/NA | Conditional |
| → If no, how currently vested? | Text | Conditional |
| *If purchase:* Relationship with seller? | Yes/No/NA | Conditional |
| Is down payment/reserve borrowed or encumbered? | Yes/No/NA | Yes |

---

### 5.8 Scope of Work / Construction Budget

*Appears for Fix & Flip and Ground-Up Construction applications*

#### Option A: Upload Existing Scope of Work
- File upload (PDF, Excel, Word)
- AI will parse and validate

#### Option B: Complete In-App Budget Builder

**Header:**
- Date
- Property Address (pre-filled)
- Project Description (text area)

**Budget Line Items by Category:**

*Each line item has: Description, Location (interior items), Quantity, Budget*

**Preparation:**
- Plans/Permits
- Demolition

**Exterior:**
- Roof
- Trim/Soffit/Fascia
- Gutters/Downspouts
- Front Porch/Portico
- Rear Porch/Deck
- Paint
- Siding
- Windows
- Shutters
- Doors
- Garage
- Fence/Gate
- Yard/Landscaping

**Interior:**
- Foundation
- Framing/Carpentry
- Insulation
- Drywall
- Paint
- Light Fixtures

**Kitchen:**
- Ceiling/Wall Repair
- Appliances
- Cabinets
- Countertops/Backsplashes
- Sink/Faucet
- Fixtures
- Floors
- Other

**Bathroom:**
- Shower/Tub
- Toilet
- Vanity
- Cabinets
- Floors
- Other

**Mechanicals:**
- Plumbing Rough
- Plumbing Finish
- Electrical Rough
- Electrical Finish
- HVAC Rough
- HVAC Finish
- Hot Water Heater

**Flooring:**
- Carpet
- Tile
- Wood

**Completion:**
- Other Appliances
- Hardware & Accessories
- Smoke/Fire Alarms
- Clean Out/Haul Off
- Contingency Reserve

**Total:** Calculated sum

---

### 5.9 Investor Experience & Portfolio

*Appears for all loan types*

#### Option A: Upload Existing Track Record & SREO
- File upload (PDF, Excel)

#### Option B: Complete In-App

**Experience Summary:**

| Field | Type |
|-------|------|
| Properties (last 12 months) | Number |
| Properties (last 36 months) | Number |
| Properties (lifetime) | Number |

**Current Schedule of Real Estate Owned:**

*Repeatable rows:*

| Field | Type |
|-------|------|
| Address | Text |
| City, State, Zip | Text |
| Entity/Name on Title | Text |
| % Ownership | Percentage |
| Acquisition Date | Date |
| Investment Type | Dropdown (Rental, Fix & Flip, etc.) |
| Property Type | Dropdown (SFR, Multi, etc.) |
| Present Market Value | Currency |
| Mortgages & Liens | Currency |
| Net Rental Income | Currency |

**Recently Sold Properties:**

*Repeatable rows:*

| Field | Type |
|-------|------|
| Address | Text |
| City, State, Zip | Text |
| Entity/Name on Title | Text |
| % Ownership | Percentage |
| Acquisition Date | Date |
| Disposition Date | Date |
| Purchase Price | Currency |
| Rehab Cost | Currency |
| Disposition Price | Currency |

---

### 5.10 Business Purpose Certification & Signature

*Display full legal disclosure text:*

> Borrower or its members ("Borrower") hereby warrants and represents that they wish to continue with the loan application, that the loan is for commercial purposes and not consumer purposes, and that the loan proceeds are intended to be used for commercial purposes only, not for personal, family or household purposes. Borrower also represents that none of the parties securing the loan is currently occupied by Borrower as their primary residence or vacation home, and that Borrower shall not occupy or reside in any of the properties during the term of the loan.

*Checkbox:* "I confirm I have read and understand the Borrower Certification of Business Purpose, that the information provided is complete and accurate, and that the properties are non-owner-occupied investment properties."

*Electronic Signature Field*

*Date (auto-populated)*

---

## 6. Multi-Property / Portfolio Support

For borrowers submitting multiple properties:

1. After first property, show "Add Another Property" button
2. Property-specific sections repeat per property
3. Borrower/Entity info captured once
4. Summary view shows all properties before submission
5. Each property can be different loan types (uncommon but supported)

---

## 7. Existing Client Pre-Fill Logic

### 7.1 Data Retrieved on Login

When an existing client authenticates:

**From Prior Loans:**
- Borrowing entity information
- Entity ownership structure
- Guarantor personal information
- Background question responses (if recent)
- PFS (if recent)
- Track record / SREO
- Third-party contacts

### 7.2 Pre-Fill Confidence Indicators

Show visual indicator for pre-filled fields:
- Green checkmark: "Pre-filled from your records"
- Allow edit on all pre-filled fields
- Flag changed fields for audit

### 7.3 Document Auto-Attach

For existing clients with documents on file:
- Driver's license
- Passport / Green card
- Entity documents (Articles, Operating Agreement, etc.)
- W-9 / EIN Letter

Display: "We have these documents on file. Please confirm they're current or upload new versions."

---

## 8. Technical Requirements

### 8.1 Frontend

- **Framework:** Next.js (React)
- **Form Library:** React Hook Form
- **Validation:** Zod schema validation
- **Styling:** Tailwind CSS
- **Address Autocomplete:** Google Places API
- **File Upload:** Drag-and-drop with preview
- **Signature:** Embedded e-signature component

### 8.2 Backend

- **API:** Next.js API routes or Express
- **Database:** PostgreSQL
- **ORM:** Prisma
- **File Storage:** Google Drive API + S3 backup
- **Authentication:** NextAuth.js with Google OAuth + credentials

### 8.3 Integrations

- **Google Places API:** Address autocomplete
- **Google Drive:** Document storage
- **Email Service:** SendGrid for confirmations

### 8.4 Data Models

*Reference Master PRD for full data model definitions*

Key entities for Phase 1-2:
- Borrower
- Entity
- Deal
- Property
- Document

### 8.5 API Endpoints

```
POST /api/quick-app
  → Create new deal with status "prospect"
  → Return deal_id

POST /api/quick-app/:deal_id/qualify
  → Run pre-qualification logic
  → Update deal status to "qualified" or "disqualified"

GET /api/application/:deal_id
  → Return pre-filled application data

POST /api/application/:deal_id
  → Save application progress

PUT /api/application/:deal_id/submit
  → Validate complete application
  → Update deal status to "application"
  → Trigger notification

POST /api/application/:deal_id/documents
  → Upload supporting documents

GET /api/clients/:client_id/prefill
  → Return existing client data for pre-fill
```

---

## 9. Notifications

### 9.1 Borrower Notifications

| Event | Channel | Template |
|-------|---------|----------|
| Quick App submitted | Email | "Thank you for your submission" |
| Pre-qualified | Email | "Great news - you're pre-qualified!" |
| Disqualified | Email | Friendly denial (see 4.5) |
| Full App saved (incomplete) | Email | "Continue your application" (24hr reminder) |
| Full App submitted | Email | "Application received - next steps" |

### 9.2 Internal Notifications

| Event | Channel | Recipients |
|-------|---------|------------|
| New Quick App | Email, Roam | Loan Officers |
| Deal Qualified | Email, Roam | Assigned LO |
| Full App Submitted | Email, Roam | Assigned LO, Processors |

---

## 10. Security Requirements

- All PII fields encrypted at rest (SSN, DOB, etc.)
- TLS 1.3 for all data in transit
- SSN masked in UI (show last 4 only after entry)
- Session timeout after 30 minutes inactivity
- FCRA-compliant credit authorization capture
- Audit log for all data access

---

## 11. Accessibility Requirements

- WCAG 2.1 AA compliance
- Keyboard navigation support
- Screen reader compatible
- Sufficient color contrast
- Error messages associated with fields
- Focus management on form progression

---

## 12. Testing Requirements

### 12.1 Unit Tests

- Form validation logic
- Pre-qualification rules
- Pre-fill mapping
- Calculations (PFS totals, etc.)

### 12.2 Integration Tests

- OAuth flow
- API endpoints
- Database operations
- File upload/storage

### 12.3 E2E Tests

- New client Quick App → Full App flow
- Existing client pre-fill flow
- Disqualification flow
- Multi-property submission

### 12.4 UAT Scenarios

1. New borrower completes Quick App and Full App for Fix & Flip
2. Existing client logs in and submits new DSCR loan
3. Borrower is disqualified and receives proper messaging
4. Borrower uploads Scope of Work document
5. Borrower completes in-app budget builder
6. Mobile user completes full flow

---

## 13. Launch Checklist

- [ ] Domain configured: borrower.usdvcapital.com
- [ ] Google OAuth credentials configured
- [ ] Google Places API key active
- [ ] Email templates created and tested
- [ ] Database migrations applied
- [ ] File storage (Google Drive) connected
- [ ] SSL certificate active
- [ ] Analytics tracking implemented
- [ ] Error monitoring configured (Sentry)
- [ ] Load testing completed
- [ ] Security audit completed
- [ ] FCRA disclosure reviewed by legal
- [ ] UAT sign-off received

---

*End of Phase 1-2 PRD*
