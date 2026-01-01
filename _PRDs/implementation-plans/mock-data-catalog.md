# INSPIRE Mock Data Catalog

**Document Version:** 1.0  
**Last Updated:** December 2024  
**Status:** Implementation Ready

---

## 1. Overview

This document consolidates all mock data examples from the INSPIRE implementation plans into a single catalog. Use these examples for:
- Development and testing
- UI prototyping
- API contract validation
- Demo environments

---

## 2. Core Entities

### 2.1 Deal

```typescript
interface Deal {
  id: string;
  
  // Basic info
  propertyAddress: string;
  city: string;
  state: string;
  zip: string;
  propertyType: PropertyType;
  units?: number;
  
  // Loan info
  loanType: LoanType;
  loanPurpose: LoanPurpose;
  loanAmount: number;
  
  // Status
  stage: PipelineStage;
  stageEnteredAt: Date;
  status: DealStatus;
  
  // Relationships
  borrowerId: string;
  borrower?: Borrower;
  loanOfficerId: string;
  processorId?: string;
  underwriterId?: string;
  
  // Metrics (calculated)
  ltv?: number;
  ltc?: number;
  dscr?: number;
  
  // Flags
  redFlagCount: number;
  yellowFlagCount: number;
  
  // Timestamps
  createdAt: Date;
  updatedAt: Date;
  fundedAt?: Date;
}
```

**Mock Deal (Fix & Flip):**

```json
{
  "id": "deal_rtl_001",
  "propertyAddress": "123 Main Street",
  "city": "Austin",
  "state": "TX",
  "zip": "78701",
  "propertyType": "sfr",
  "units": 1,
  "loanType": "fix_flip",
  "loanPurpose": "purchase",
  "loanAmount": 382500,
  "stage": "processing",
  "stageEnteredAt": "2024-12-07T10:00:00Z",
  "status": "active",
  "borrowerId": "borrower_001",
  "loanOfficerId": "user_lo_001",
  "processorId": "user_proc_001",
  "ltc": 75,
  "ltv": 65,
  "redFlagCount": 1,
  "yellowFlagCount": 2,
  "createdAt": "2024-12-01T09:00:00Z",
  "updatedAt": "2024-12-15T14:30:00Z"
}
```

**Mock Deal (DSCR):**

```json
{
  "id": "deal_dscr_001",
  "propertyAddress": "456 Oak Avenue",
  "city": "Dallas",
  "state": "TX",
  "zip": "75201",
  "propertyType": "sfr",
  "units": 1,
  "loanType": "dscr",
  "loanPurpose": "refinance",
  "loanAmount": 525000,
  "stage": "underwriting",
  "stageEnteredAt": "2024-12-12T14:00:00Z",
  "status": "active",
  "borrowerId": "borrower_002",
  "loanOfficerId": "user_lo_002",
  "processorId": "user_proc_001",
  "underwriterId": "user_uw_001",
  "dscr": 1.35,
  "ltv": 70,
  "redFlagCount": 0,
  "yellowFlagCount": 1,
  "createdAt": "2024-12-05T11:00:00Z",
  "updatedAt": "2024-12-15T16:00:00Z"
}
```

**Mock Deal (Ground Up):**

```json
{
  "id": "deal_guc_001",
  "propertyAddress": "789 Pine Road",
  "city": "Houston",
  "state": "TX",
  "zip": "77001",
  "propertyType": "sfr",
  "units": 1,
  "loanType": "ground_up",
  "loanPurpose": "construction",
  "loanAmount": 850000,
  "stage": "quote",
  "stageEnteredAt": "2024-12-14T09:00:00Z",
  "status": "active",
  "borrowerId": "borrower_003",
  "loanOfficerId": "user_lo_001",
  "ltc": 80,
  "ltv": 60,
  "redFlagCount": 0,
  "yellowFlagCount": 0,
  "createdAt": "2024-12-10T10:00:00Z",
  "updatedAt": "2024-12-14T09:00:00Z"
}
```

---

### 2.2 Borrower

```typescript
interface Borrower {
  id: string;
  
  // Entity info
  entityName: string;
  entityType: EntityType;
  entityState: string;
  ein?: string;
  
  // Contact
  primaryContact: string;
  email: string;
  phone: string;
  
  // Experience
  experienceScore: number;
  projectsCompleted: number;
  projectsLast36Months: number;
  
  // Credit
  fico: number;
  
  // Client status
  clientType: 'new' | 'existing' | 're_cfo';
  priorDeals?: string[];
  
  createdAt: Date;
  updatedAt: Date;
}
```

**Mock Borrower (Experienced):**

```json
{
  "id": "borrower_001",
  "entityName": "ABC Investments LLC",
  "entityType": "llc",
  "entityState": "TX",
  "ein": "12-3456789",
  "primaryContact": "John Smith",
  "email": "john@abcinvestments.com",
  "phone": "(512) 555-1234",
  "experienceScore": 8,
  "projectsCompleted": 12,
  "projectsLast36Months": 8,
  "fico": 680,
  "clientType": "existing",
  "priorDeals": ["deal_xyz789", "deal_xyz790"],
  "createdAt": "2023-06-15T00:00:00Z",
  "updatedAt": "2024-12-01T00:00:00Z"
}
```

**Mock Borrower (New):**

```json
{
  "id": "borrower_002",
  "entityName": "XYZ Holdings LLC",
  "entityType": "llc",
  "entityState": "TX",
  "ein": "98-7654321",
  "primaryContact": "Jane Doe",
  "email": "jane@xyzholdings.com",
  "phone": "(214) 555-5678",
  "experienceScore": 3,
  "projectsCompleted": 3,
  "projectsLast36Months": 3,
  "fico": 720,
  "clientType": "new",
  "createdAt": "2024-12-05T00:00:00Z",
  "updatedAt": "2024-12-05T00:00:00Z"
}
```

---

### 2.3 Guarantor

```typescript
interface Guarantor {
  id: string;
  borrowerId: string;
  
  // Identity
  firstName: string;
  lastName: string;
  email: string;
  phone: string;
  dateOfBirth: string;
  ssn: string; // Encrypted
  
  // Ownership
  ownershipPercent: number;
  
  // Credit
  fico: number;
  
  // Address
  address: Address;
  
  // Background
  usCitizen: boolean;
  
  createdAt: Date;
  updatedAt: Date;
}
```

**Mock Guarantor:**

```json
{
  "id": "guarantor_001",
  "borrowerId": "borrower_001",
  "firstName": "John",
  "lastName": "Smith",
  "email": "john@abcinvestments.com",
  "phone": "(512) 555-1234",
  "dateOfBirth": "1975-06-15",
  "ssn": "***-**-1234",
  "ownershipPercent": 100,
  "fico": 680,
  "address": {
    "street": "456 Elm Street",
    "city": "Austin",
    "state": "TX",
    "zip": "78702"
  },
  "usCitizen": true,
  "createdAt": "2023-06-15T00:00:00Z",
  "updatedAt": "2024-12-01T00:00:00Z"
}
```

---

### 2.4 Property

```typescript
interface Property {
  id: string;
  dealId: string;
  
  // Location
  address: string;
  unit?: string;
  city: string;
  state: string;
  zip: string;
  county: string;
  
  // Characteristics
  propertyType: PropertyType;
  units: number;
  squareFeet: number;
  lotSize?: number;
  yearBuilt: number;
  bedrooms?: number;
  bathrooms?: number;
  
  // Condition
  condition: 'excellent' | 'good' | 'fair' | 'poor';
  
  // Values
  purchasePrice?: number;
  asIsValue?: number;
  arv?: number;
  
  // For DSCR
  monthlyRent?: number;
  annualTaxes?: number;
  annualInsurance?: number;
  hoaMonthly?: number;
  
  createdAt: Date;
  updatedAt: Date;
}
```

**Mock Property (RTL):**

```json
{
  "id": "property_001",
  "dealId": "deal_rtl_001",
  "address": "123 Main Street",
  "city": "Austin",
  "state": "TX",
  "zip": "78701",
  "county": "Travis",
  "propertyType": "sfr",
  "units": 1,
  "squareFeet": 1850,
  "lotSize": 6500,
  "yearBuilt": 1985,
  "bedrooms": 3,
  "bathrooms": 2,
  "condition": "fair",
  "purchasePrice": 400000,
  "asIsValue": 425000,
  "arv": 585000,
  "createdAt": "2024-12-01T09:00:00Z",
  "updatedAt": "2024-12-15T14:30:00Z"
}
```

**Mock Property (DSCR):**

```json
{
  "id": "property_002",
  "dealId": "deal_dscr_001",
  "address": "456 Oak Avenue",
  "city": "Dallas",
  "state": "TX",
  "zip": "75201",
  "county": "Dallas",
  "propertyType": "sfr",
  "units": 1,
  "squareFeet": 2200,
  "yearBuilt": 2010,
  "bedrooms": 4,
  "bathrooms": 2.5,
  "condition": "good",
  "asIsValue": 750000,
  "monthlyRent": 3500,
  "annualTaxes": 9000,
  "annualInsurance": 2400,
  "hoaMonthly": 0,
  "createdAt": "2024-12-05T11:00:00Z",
  "updatedAt": "2024-12-15T16:00:00Z"
}
```

---

## 3. Application Data

### 3.1 Quick Application

```json
{
  "id": "quickapp_001",
  "dealId": "deal_rtl_001",
  "status": "completed",
  "submittedAt": "2024-12-01T09:30:00Z",
  "data": {
    "loanType": "fix_flip",
    "propertyAddress": "123 Main Street, Austin, TX 78701",
    "purchasePrice": 400000,
    "rehabBudget": 110000,
    "arv": 585000,
    "borrowerName": "John Smith",
    "entityName": "ABC Investments LLC",
    "email": "john@abcinvestments.com",
    "phone": "(512) 555-1234",
    "experienceLevel": "8+",
    "estimatedFico": "660-699"
  },
  "prequalResult": {
    "qualified": true,
    "estimatedLoanAmount": 382500,
    "estimatedRate": "11.25-11.75%",
    "ltc": 75,
    "ltv": 65,
    "flags": []
  }
}
```

### 3.2 Full Application

```json
{
  "id": "fullapp_001",
  "dealId": "deal_rtl_001",
  "status": "completed",
  "submittedAt": "2024-12-02T14:00:00Z",
  "sections": {
    "borrower": {
      "entityName": "ABC Investments LLC",
      "entityType": "llc",
      "entityState": "TX",
      "ein": "12-3456789",
      "formationDate": "2018-03-15"
    },
    "guarantors": [
      {
        "firstName": "John",
        "lastName": "Smith",
        "ownershipPercent": 100,
        "email": "john@abcinvestments.com",
        "phone": "(512) 555-1234",
        "dateOfBirth": "1975-06-15",
        "ssn": "***-**-1234",
        "address": {
          "street": "456 Elm Street",
          "city": "Austin",
          "state": "TX",
          "zip": "78702"
        },
        "usCitizen": true
      }
    ],
    "property": {
      "address": "123 Main Street",
      "city": "Austin",
      "state": "TX",
      "zip": "78701",
      "propertyType": "sfr",
      "units": 1,
      "squareFeet": 1850,
      "yearBuilt": 1985,
      "condition": "fair"
    },
    "loan": {
      "loanType": "fix_flip",
      "loanPurpose": "purchase",
      "purchasePrice": 400000,
      "rehabBudget": 110000,
      "arv": 585000,
      "exitStrategy": "sell"
    },
    "experience": {
      "projectsCompleted": 12,
      "projectsLast36Months": 8,
      "similarProjects": 6,
      "defaultHistory": false,
      "references": [
        {
          "name": "First National Bank",
          "contact": "Mike Johnson",
          "phone": "(512) 555-9999"
        }
      ]
    },
    "declarations": {
      "bankruptcyLast7Years": false,
      "foreclosureLast7Years": false,
      "lawsuitsPending": false,
      "judgmentsOutstanding": false,
      "delinquentFederalDebt": false,
      "partyToLawsuit": false
    }
  }
}
```

---

## 4. Sizing & Quotes

### 4.1 RTL Sizer Output

```json
{
  "id": "sizing_rtl_001",
  "dealId": "deal_rtl_001",
  "loanType": "fix_flip",
  "generatedAt": "2024-12-03T10:00:00Z",
  "inputs": {
    "purchasePrice": 400000,
    "asIsValue": 425000,
    "rehabBudget": 110000,
    "arv": 585000,
    "fico": 680,
    "experience": 8
  },
  "sizing": {
    "maxLoanAmount": 382500,
    "initialAdvance": 300000,
    "rehabHoldback": 82500,
    "ltc": 75,
    "ltv": 65,
    "arvLtv": 65,
    "purchaseLtv": 75
  },
  "pricing": {
    "baseRate": 11.0,
    "adjustments": [
      { "reason": "FICO 680 (below 700)", "adjustment": 0.25 },
      { "reason": "Experience 8+ projects", "adjustment": -0.25 }
    ],
    "finalRate": 11.0,
    "originationFee": 2.0,
    "originationAmount": 7650,
    "processingFee": 1295,
    "thirdPartyDeposit": 3500
  },
  "term": {
    "months": 12,
    "extensions": 2,
    "extensionFee": 0.5
  },
  "reserves": {
    "required": 38250,
    "verified": 450000,
    "met": true
  }
}
```

### 4.2 DSCR Sizer Output

```json
{
  "id": "sizing_dscr_001",
  "dealId": "deal_dscr_001",
  "loanType": "dscr",
  "generatedAt": "2024-12-06T11:00:00Z",
  "inputs": {
    "propertyValue": 750000,
    "monthlyRent": 3500,
    "annualTaxes": 9000,
    "annualInsurance": 2400,
    "hoaMonthly": 0,
    "fico": 720,
    "experience": 3
  },
  "income": {
    "grossMonthlyRent": 3500,
    "annualGrossRent": 42000,
    "vacancyRate": 5,
    "effectiveGrossIncome": 39900,
    "managementFee": 3990,
    "noi": 24510
  },
  "sizing": {
    "maxLoanAmount": 525000,
    "ltv": 70,
    "dscr": 1.35
  },
  "pricing": {
    "baseRate": 7.5,
    "adjustments": [
      { "reason": "DSCR 1.35", "adjustment": 0 },
      { "reason": "FICO 720", "adjustment": 0 },
      { "reason": "LTV 70%", "adjustment": 0.125 }
    ],
    "finalRate": 7.625,
    "originationFee": 1.5,
    "originationAmount": 7875,
    "processingFee": 995
  },
  "term": {
    "type": "30_year_fixed",
    "amortization": 360,
    "prepaymentPenalty": "5-4-3-2-1"
  }
}
```

### 4.3 Quote Scenarios

```json
{
  "dealId": "deal_rtl_001",
  "generatedAt": "2024-12-03T10:30:00Z",
  "expiresAt": "2024-12-10T23:59:59Z",
  "scenarios": [
    {
      "id": "quote_001_a",
      "name": "Standard",
      "isRecommended": true,
      "loanAmount": 382500,
      "rate": 11.0,
      "originationFee": 2.0,
      "term": 12,
      "ltc": 75,
      "ltv": 65,
      "monthlyPayment": 3506,
      "totalClosingCosts": 12445
    },
    {
      "id": "quote_001_b",
      "name": "Lower Rate",
      "isRecommended": false,
      "loanAmount": 357500,
      "rate": 10.75,
      "originationFee": 2.5,
      "term": 12,
      "ltc": 70,
      "ltv": 61,
      "monthlyPayment": 3203,
      "totalClosingCosts": 13733
    },
    {
      "id": "quote_001_c",
      "name": "Max Leverage",
      "isRecommended": false,
      "loanAmount": 408000,
      "rate": 11.5,
      "originationFee": 2.0,
      "term": 12,
      "ltc": 80,
      "ltv": 70,
      "monthlyPayment": 3910,
      "totalClosingCosts": 12955
    }
  ],
  "selectedScenarioId": null,
  "status": "pending"
}
```

---

## 5. Third-Party Reports

### 5.1 Report Status

```json
{
  "dealId": "deal_rtl_001",
  "reports": [
    {
      "id": "report_001",
      "reportType": "credit",
      "provider": "crs",
      "status": "received",
      "orderedAt": "2024-12-08T10:00:00Z",
      "receivedAt": "2024-12-08T10:05:00Z",
      "documentId": "doc_credit_001",
      "cost": 65
    },
    {
      "id": "report_002",
      "reportType": "background_individual",
      "provider": "crs",
      "status": "received",
      "orderedAt": "2024-12-08T10:00:00Z",
      "receivedAt": "2024-12-08T10:10:00Z",
      "documentId": "doc_bg_001",
      "cost": 85
    },
    {
      "id": "report_003",
      "reportType": "appraisal",
      "provider": "single_source",
      "status": "scheduled",
      "orderedAt": "2024-12-10T14:00:00Z",
      "externalOrderId": "SS-2024-12345",
      "assignedVendor": "ABC Appraisals",
      "scheduledDate": "2024-12-15T10:00:00Z",
      "estimatedCompletion": "2024-12-17T17:00:00Z",
      "cost": 650
    },
    {
      "id": "report_004",
      "reportType": "title",
      "provider": "single_source",
      "status": "received",
      "orderedAt": "2024-12-08T14:00:00Z",
      "receivedAt": "2024-12-09T16:00:00Z",
      "documentId": "doc_title_001",
      "cost": 0
    },
    {
      "id": "report_005",
      "reportType": "flood",
      "provider": "single_source",
      "status": "received",
      "orderedAt": "2024-12-10T14:00:00Z",
      "receivedAt": "2024-12-10T14:30:00Z",
      "documentId": "doc_flood_001",
      "cost": 25
    },
    {
      "id": "report_006",
      "reportType": "feasibility",
      "provider": "single_source",
      "status": "in_progress",
      "orderedAt": "2024-12-10T14:00:00Z",
      "externalOrderId": "SS-2024-12346",
      "estimatedCompletion": "2024-12-14T17:00:00Z",
      "cost": 350
    },
    {
      "id": "report_007",
      "reportType": "insurance",
      "provider": "first_choice",
      "status": "ordered",
      "orderedAt": "2024-12-08T14:00:00Z",
      "cost": 0
    }
  ],
  "summary": {
    "total": 7,
    "received": 4,
    "inProgress": 2,
    "pending": 1,
    "totalCost": 1175
  }
}
```

---

## 6. Diligence Checklist

```json
{
  "dealId": "deal_rtl_001",
  "clientType": "existing",
  "loanType": "fix_flip",
  "progress": {
    "overall": 78,
    "byCategory": {
      "borrower": { "complete": 6, "total": 8 },
      "property": { "complete": 5, "total": 6 },
      "third_party": { "complete": 5, "total": 6 },
      "closing": { "complete": 2, "total": 4 }
    }
  },
  "items": [
    {
      "id": "item_001",
      "category": "borrower",
      "documentType": "articles_of_organization",
      "displayName": "Articles of Organization",
      "status": "on_file",
      "onFileFrom": "deal_xyz789",
      "onFileDate": "2024-06-15T00:00:00Z"
    },
    {
      "id": "item_002",
      "category": "borrower",
      "documentType": "operating_agreement",
      "displayName": "Operating Agreement",
      "status": "on_file",
      "onFileFrom": "deal_xyz789",
      "onFileDate": "2024-06-15T00:00:00Z"
    },
    {
      "id": "item_003",
      "category": "borrower",
      "documentType": "certificate_good_standing",
      "displayName": "Certificate of Good Standing",
      "status": "received",
      "documentId": "doc_cgs_001",
      "expirationDate": "2025-03-10T00:00:00Z"
    },
    {
      "id": "item_004",
      "category": "borrower",
      "documentType": "bank_statements",
      "displayName": "Bank Statements (2 months)",
      "status": "received",
      "documentId": "doc_bank_001"
    },
    {
      "id": "item_005",
      "category": "borrower",
      "documentType": "drivers_license",
      "displayName": "Driver's License - John Smith",
      "status": "on_file",
      "onFileFrom": "deal_xyz789"
    },
    {
      "id": "item_006",
      "category": "property",
      "documentType": "purchase_contract",
      "displayName": "Purchase Contract",
      "status": "received",
      "documentId": "doc_psa_001"
    },
    {
      "id": "item_007",
      "category": "property",
      "documentType": "scope_of_work",
      "displayName": "Scope of Work / Budget",
      "status": "received",
      "documentId": "doc_sow_001"
    },
    {
      "id": "item_008",
      "category": "third_party",
      "documentType": "credit_report",
      "displayName": "Credit Report",
      "status": "received",
      "documentId": "doc_credit_001",
      "autoPopulated": true
    },
    {
      "id": "item_009",
      "category": "third_party",
      "documentType": "appraisal",
      "displayName": "Appraisal",
      "status": "requested",
      "linkedReportId": "report_003"
    },
    {
      "id": "item_010",
      "category": "closing",
      "documentType": "preliminary_hud",
      "displayName": "Preliminary HUD",
      "status": "required"
    }
  ],
  "expiringDocuments": [
    {
      "documentType": "certificate_good_standing",
      "expirationDate": "2025-03-10T00:00:00Z",
      "daysUntilExpiry": 85
    }
  ]
}
```

---

## 7. Analysis & Flags

### 7.1 Analysis Summary

```json
{
  "dealId": "deal_rtl_001",
  "summary": {
    "riskScore": 35,
    "confidenceScore": 92,
    "redFlags": 2,
    "yellowFlags": 5,
    "greenFlags": 28,
    "totalChecks": 35,
    "categoryScores": {
      "borrower": 85,
      "property": 90,
      "valuation": 75,
      "title": 95,
      "insurance": 100,
      "financial": 80
    },
    "documentsAnalyzed": 12,
    "documentsTotal": 14,
    "lastAnalyzedAt": "2024-12-15T14:30:00Z",
    "criticalFindings": [
      "FICO score 680 below minimum 700 for investor",
      "ARV variance 8% exceeds 5% threshold"
    ],
    "exceptionsIdentified": 2,
    "creditMemoStatus": "ready",
    "creditMemoId": "memo_001"
  }
}
```

### 7.2 Flags

```json
{
  "dealId": "deal_rtl_001",
  "flags": [
    {
      "id": "flag_001",
      "category": "credit",
      "severity": "red",
      "title": "FICO Below Minimum",
      "description": "Middle FICO score 680 is below investor minimum of 700",
      "guidelineRef": "Archwest DSCR 3.1.2",
      "guidelineText": "Minimum FICO score of 700 required",
      "actualValue": 680,
      "expectedValue": 700,
      "isException": true,
      "exceptionStatus": "approved",
      "exceptionId": "exc_001",
      "createdAt": "2024-12-10T10:15:00Z"
    },
    {
      "id": "flag_002",
      "category": "valuation",
      "severity": "red",
      "title": "ARV Variance High",
      "description": "Appraisal ARV differs from feasibility by 8%",
      "guidelineRef": "Archwest RTL 5.2.1",
      "guidelineText": "ARV variance must be within 5%",
      "actualValue": "8%",
      "threshold": "5%",
      "isException": true,
      "exceptionStatus": "pending",
      "exceptionId": "exc_002",
      "createdAt": "2024-12-15T14:00:00Z"
    },
    {
      "id": "flag_003",
      "category": "experience",
      "severity": "yellow",
      "title": "Limited Track Record",
      "description": "Borrower has completed 3 projects in past 36 months",
      "guidelineRef": "Archwest RTL 2.3.1",
      "guidelineText": "5+ projects preferred for Tier 1 pricing",
      "actualValue": 3,
      "expectedValue": 5,
      "isException": false,
      "createdAt": "2024-12-10T10:15:00Z"
    },
    {
      "id": "flag_004",
      "category": "title",
      "severity": "green",
      "title": "Clear Title",
      "description": "No liens or encumbrances found",
      "guidelineRef": "Standard",
      "isException": false,
      "createdAt": "2024-12-09T16:30:00Z"
    }
  ]
}
```

### 7.3 Exception

```json
{
  "id": "exc_001",
  "dealId": "deal_rtl_001",
  "flagId": "flag_001",
  "exceptionType": "credit_fico",
  "justification": "Borrower's FICO dropped due to high utilization during recent acquisition. Has since paid down and score is recovering. Strong track record with 8 successful projects.",
  "compensatingFactors": [
    {
      "type": "experience",
      "description": "8 completed projects in past 36 months"
    },
    {
      "type": "cash_reserves",
      "description": "$450,000 verified liquid reserves"
    },
    {
      "type": "low_ltv",
      "description": "LTV of 65% vs max 75%"
    }
  ],
  "status": "approved",
  "requestedBy": "user_lo_001",
  "requestedAt": "2024-12-10T15:00:00Z",
  "reviewedBy": "user_uw_001",
  "reviewedAt": "2024-12-11T10:00:00Z",
  "approvedBy": "user_cm_001",
  "approvedAt": "2024-12-11T14:00:00Z",
  "decision": "approved",
  "decisionNotes": "Approved with 10bps rate adjustment. Strong compensating factors mitigate credit risk.",
  "conditions": ["10bps rate adjustment applied"],
  "requiresInvestorApproval": false
}
```

---

## 8. Credit Memo

```json
{
  "id": "memo_001",
  "dealId": "deal_rtl_001",
  "version": 1,
  "status": "approved",
  "generatedAt": "2024-12-15T16:00:00Z",
  "generatedBy": "ai",
  "approvedBy": "user_uw_001",
  "approvedAt": "2024-12-15T17:00:00Z",
  "sections": {
    "executiveSummary": {
      "loanAmount": 382500,
      "loanType": "Fix & Flip",
      "purpose": "Purchase + Rehab",
      "propertyAddress": "123 Main Street, Austin, TX 78701",
      "borrowerName": "ABC Investments LLC",
      "keyMetrics": {
        "ltc": 75,
        "ltv": 65,
        "fico": 680,
        "experience": 8
      },
      "recommendation": "approve_with_conditions",
      "conditions": [
        "FICO exception approved with 10bps rate adjustment",
        "Verify rehab budget with contractor bids"
      ],
      "keyStrengths": [
        "Experienced borrower with 8 completed projects",
        "Strong cash reserves ($450K liquid)",
        "Conservative LTV at 65%",
        "Repeat borrower with clean payment history"
      ],
      "keyRisks": [
        "FICO 680 below 700 minimum",
        "ARV variance of 8% between appraisal and feasibility"
      ]
    },
    "borrowerAnalysis": {
      "entityInfo": {
        "name": "ABC Investments LLC",
        "type": "LLC",
        "state": "Texas",
        "formation": "2018"
      },
      "guarantors": [
        {
          "name": "John Smith",
          "ownership": 100,
          "fico": 680,
          "netWorth": 1250000,
          "liquidity": 450000
        }
      ],
      "experience": {
        "totalProjects": 12,
        "projectsLast36Months": 8,
        "similarProjects": 6,
        "defaultHistory": false
      },
      "creditAnalysis": {
        "middleFico": 680,
        "derogatory": [],
        "bankruptcies": [],
        "foreclosures": []
      },
      "backgroundAnalysis": {
        "criminal": false,
        "litigation": false,
        "judgments": false,
        "ofac": false
      }
    },
    "propertyAnalysis": {
      "address": "123 Main Street, Austin, TX 78701",
      "propertyType": "SFR",
      "squareFeet": 1850,
      "yearBuilt": 1985,
      "condition": "Fair - needs cosmetic rehab",
      "marketAnalysis": "Austin market remains strong with 5% YoY appreciation. Subject neighborhood has seen 8% appreciation. Strong rental demand."
    },
    "valuationAnalysis": {
      "asIsValue": 425000,
      "arv": 585000,
      "appraisalDate": "2024-12-15",
      "appraiser": "ABC Appraisals",
      "appraisalType": "Full Interior",
      "comparableAnalysis": "Three comparable sales within 0.5 miles, all within 6 months. Adjustments reasonable.",
      "valueConclusion": "ARV supported by comparables. 8% variance from feasibility study due to different comp selection.",
      "feasibilityComparison": {
        "feasibilityARV": 540000,
        "appraisalARV": 585000,
        "variance": 8,
        "explanation": "Appraisal used more recent sales showing market appreciation"
      }
    },
    "financialAnalysis": {
      "acquisitionCost": 400000,
      "rehabBudget": 110000,
      "totalCost": 510000,
      "ltc": 75,
      "arv": 585000,
      "ltv": 65,
      "cashReserves": 450000,
      "reserveRequirement": 38250,
      "reservesMet": true
    },
    "riskAssessment": {
      "overallRisk": "moderate",
      "riskScore": 35,
      "riskFactors": [
        {
          "category": "Credit",
          "risk": "moderate",
          "description": "FICO 680 below 700 minimum",
          "mitigant": "Strong experience and reserves"
        },
        {
          "category": "Valuation",
          "risk": "moderate",
          "description": "8% ARV variance",
          "mitigant": "Conservative LTV provides cushion"
        }
      ],
      "strengths": [
        "Experienced operator with proven track record",
        "Strong liquidity position",
        "Conservative leverage",
        "Strong market fundamentals"
      ],
      "weaknesses": [
        "Below-minimum FICO score",
        "ARV variance requires monitoring"
      ],
      "mitigants": [
        "10bps rate adjustment for FICO exception",
        "Conservative LTV provides valuation cushion",
        "Draw inspection to verify rehab progress"
      ]
    },
    "recommendation": {
      "decision": "approve_with_conditions",
      "conditions": [
        "FICO exception approved with 10bps rate adjustment",
        "Verify contractor bids for rehab budget",
        "Standard draw inspection schedule"
      ],
      "pricing": {
        "rate": 11.1,
        "originationFee": 2.0,
        "term": 12
      },
      "underwriterNotes": "Strong borrower profile mitigates FICO concern. ARV variance within acceptable range given conservative LTV."
    }
  }
}
```

---

## 9. Dashboard Data

### 9.1 KPIs

```json
{
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
}
```

### 9.2 Needs Attention

```json
{
  "items": [
    {
      "id": "attn_001",
      "dealId": "deal_rtl_001",
      "propertyAddress": "123 Main St, Austin, TX",
      "borrowerName": "ABC Investments LLC",
      "reason": "sla_breach",
      "reasonDetail": "12 days in Processing (SLA: 10 days)",
      "priority": "high",
      "daysPastDue": 2,
      "actionRequired": "Complete processing checklist",
      "actionUrl": "/deals/deal_rtl_001"
    },
    {
      "id": "attn_002",
      "dealId": "deal_dscr_002",
      "propertyAddress": "456 Oak Ave, Dallas, TX",
      "borrowerName": "XYZ Holdings LLC",
      "reason": "quote_expiring",
      "reasonDetail": "Quote expires in 2 days",
      "priority": "high",
      "dueDate": "2024-12-17T00:00:00Z",
      "actionRequired": "Follow up on quote acceptance",
      "actionUrl": "/deals/deal_dscr_002/quotes"
    },
    {
      "id": "attn_003",
      "dealId": "deal_rtl_003",
      "propertyAddress": "789 Pine Rd, Houston, TX",
      "borrowerName": "123 Properties LLC",
      "reason": "red_flag_unresolved",
      "reasonDetail": "1 unresolved red flag",
      "priority": "high",
      "actionRequired": "Review and resolve FICO exception",
      "actionUrl": "/deals/deal_rtl_003/analysis"
    }
  ]
}
```

### 9.3 Pipeline by Stage

```json
{
  "stages": [
    { "stage": "prospect", "stageLabel": "Prospect", "count": 8, "volume": 4800000, "avgDaysInStage": 3, "slaTarget": 5, "atRisk": 1 },
    { "stage": "application", "stageLabel": "Application", "count": 12, "volume": 7200000, "avgDaysInStage": 4, "slaTarget": 7, "atRisk": 2 },
    { "stage": "quote", "stageLabel": "Quote", "count": 6, "volume": 3600000, "avgDaysInStage": 2, "slaTarget": 3, "atRisk": 0 },
    { "stage": "initial_uw", "stageLabel": "Initial UW", "count": 5, "volume": 3000000, "avgDaysInStage": 3, "slaTarget": 5, "atRisk": 0 },
    { "stage": "processing", "stageLabel": "Processing", "count": 10, "volume": 6000000, "avgDaysInStage": 8, "slaTarget": 10, "atRisk": 3 },
    { "stage": "underwriting", "stageLabel": "Underwriting", "count": 7, "volume": 4200000, "avgDaysInStage": 5, "slaTarget": 7, "atRisk": 1 },
    { "stage": "closing", "stageLabel": "Closing", "count": 4, "volume": 2400000, "avgDaysInStage": 4, "slaTarget": 5, "atRisk": 0 }
  ]
}
```

---

## 10. Tasks

```json
{
  "tasks": [
    {
      "id": "task_001",
      "dealId": "deal_rtl_001",
      "title": "Review appraisal report",
      "description": "Review completed appraisal and verify ARV against feasibility",
      "assignedTo": "user_uw_001",
      "dueDate": "2024-12-15T17:00:00Z",
      "priority": "high",
      "status": "pending",
      "category": "review",
      "source": "system",
      "createdAt": "2024-12-15T14:00:00Z"
    },
    {
      "id": "task_002",
      "dealId": "deal_dscr_001",
      "title": "Send closing instructions to title",
      "description": "Prepare and send closing instructions to title company",
      "assignedTo": "user_closer_001",
      "dueDate": "2024-12-15T17:00:00Z",
      "priority": "medium",
      "status": "pending",
      "category": "closing",
      "source": "manual",
      "createdAt": "2024-12-14T10:00:00Z"
    },
    {
      "id": "task_003",
      "dealId": "deal_rtl_002",
      "title": "Follow up on missing bank statements",
      "description": "Contact borrower for October bank statements",
      "assignedTo": "user_proc_001",
      "dueDate": "2024-12-14T17:00:00Z",
      "priority": "medium",
      "status": "completed",
      "completedAt": "2024-12-14T15:30:00Z",
      "completedBy": "user_proc_001",
      "category": "document_request",
      "source": "checklist",
      "createdAt": "2024-12-12T09:00:00Z"
    }
  ]
}
```

---

## 11. Activity Log

```json
{
  "activities": [
    {
      "id": "act_001",
      "dealId": "deal_rtl_001",
      "userId": "user_uw_001",
      "action": "document_uploaded",
      "actionLabel": "Document Uploaded",
      "description": "Appraisal report uploaded",
      "details": {
        "documentType": "appraisal",
        "filename": "123_Main_St_Appraisal.pdf"
      },
      "timestamp": "2024-12-15T14:30:00Z"
    },
    {
      "id": "act_002",
      "dealId": "deal_dscr_001",
      "userId": "user_lo_001",
      "action": "stage_changed",
      "actionLabel": "Stage Changed",
      "description": "Deal moved to Closing",
      "details": {
        "from": "underwriting",
        "to": "closing"
      },
      "timestamp": "2024-12-15T14:15:00Z"
    },
    {
      "id": "act_003",
      "dealId": "deal_rtl_001",
      "userId": null,
      "systemGenerated": true,
      "action": "analysis_completed",
      "actionLabel": "Analysis Completed",
      "description": "AI analysis completed for appraisal",
      "details": {
        "documentType": "appraisal",
        "flagsGenerated": 2
      },
      "timestamp": "2024-12-15T14:35:00Z"
    },
    {
      "id": "act_004",
      "dealId": "deal_rtl_001",
      "userId": "user_cm_001",
      "action": "exception_approved",
      "actionLabel": "Exception Approved",
      "description": "FICO exception approved with conditions",
      "details": {
        "exceptionId": "exc_001",
        "conditions": ["10bps rate adjustment"]
      },
      "timestamp": "2024-12-11T14:00:00Z"
    }
  ]
}
```

---

## 12. Users

```json
{
  "users": [
    {
      "id": "user_lo_001",
      "name": "Mike Johnson",
      "email": "mike.johnson@usdvcapital.com",
      "role": "loan_officer",
      "avatar": "/avatars/mike.jpg",
      "active": true
    },
    {
      "id": "user_lo_002",
      "name": "Sarah Williams",
      "email": "sarah.williams@usdvcapital.com",
      "role": "loan_officer",
      "avatar": "/avatars/sarah.jpg",
      "active": true
    },
    {
      "id": "user_proc_001",
      "name": "Emily Davis",
      "email": "emily.davis@usdvcapital.com",
      "role": "processor",
      "avatar": "/avatars/emily.jpg",
      "active": true
    },
    {
      "id": "user_uw_001",
      "name": "Robert Chen",
      "email": "robert.chen@usdvcapital.com",
      "role": "underwriter",
      "avatar": "/avatars/robert.jpg",
      "active": true
    },
    {
      "id": "user_cm_001",
      "name": "Jennifer Martinez",
      "email": "jennifer.martinez@usdvcapital.com",
      "role": "credit_manager",
      "avatar": "/avatars/jennifer.jpg",
      "active": true
    },
    {
      "id": "user_closer_001",
      "name": "David Kim",
      "email": "david.kim@usdvcapital.com",
      "role": "closer",
      "avatar": "/avatars/david.jpg",
      "active": true
    }
  ]
}
```

---

## 13. Notifications

```json
{
  "notifications": [
    {
      "id": "notif_001",
      "userId": "user_uw_001",
      "type": "document_uploaded",
      "title": "New Document",
      "message": "Appraisal uploaded for 123 Main St",
      "dealId": "deal_rtl_001",
      "read": false,
      "actionUrl": "/deals/deal_rtl_001/documents",
      "createdAt": "2024-12-15T14:30:00Z"
    },
    {
      "id": "notif_002",
      "userId": "user_lo_001",
      "type": "sla_at_risk",
      "title": "SLA At Risk",
      "message": "Deal approaching SLA deadline in Processing",
      "dealId": "deal_rtl_002",
      "read": true,
      "readAt": "2024-12-15T10:00:00Z",
      "actionUrl": "/deals/deal_rtl_002",
      "createdAt": "2024-12-15T08:00:00Z"
    },
    {
      "id": "notif_003",
      "userId": "user_proc_001",
      "type": "task_assigned",
      "title": "New Task",
      "message": "Review bank statements for ABC Investments",
      "dealId": "deal_rtl_001",
      "read": false,
      "actionUrl": "/tasks/task_004",
      "createdAt": "2024-12-15T09:00:00Z"
    }
  ],
  "unreadCount": 2
}
```

---

*End of Mock Data Catalog*

