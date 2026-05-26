# Verification Packet — COV_FIE_M1_0015

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `field_services`
- **Difficulty level (1–5):** 1
- **Period type:** month
- **Period label:** October 2025
- **Period start → end:** 2025-10-01 → 2025-10-31
- **Entity:** Silverline Advisors
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 6
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Office Supplies`, `Prepaid Insurance`, `Equipment`, `Vehicles`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Repairs Expense`, `Fuel Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-10-01_

**Assets**
- Cash: 55,205.97
- Accounts Receivable: 8,045.32

**Liabilities**
- Accounts Payable: 4,805.56

**Equity**
- Owner's Equity: 58,445.73


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-10-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2025-10-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $55,205.97
  - Section assets | Account Accounts Receivable | Amount $8,045.32
  - Section liabilities | Account Accounts Payable | Amount $4,805.56
  - Section equity | Account Owner's Equity | Amount $58,445.73

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2025-10-03

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0001
Customer: Aster Point Services
Job Site: Riverbank Plaza
Scope: Review pack
Approved Amount: $8,937.91

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-04

```
CUSTOMER INVOICE
================

From
----
Silverline Advisors
220 Lake View Road, Bengaluru
Document Date: 2025-10-04

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: October 2025
Contract Ref: CTR-0001
Job Code: JOB-0001

Terms
-----
Due Date: 2025-10-20

Parties
-------
Customer: Aster Point Services
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-10-20
Total: $8,937.91

Line Items
----------
Items:
  - Description Monthly retainer | Amount $3,251.78
  - Description Follow-up support | Amount $5,686.13

Field Job
---------
Job Code: JOB-0001

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D004 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-09

```
SUPPLIER INVOICE
================

From
----
Silverline Advisors
220 Lake View Road, Bengaluru
Date: 2025-10-09

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D004
Document Type: supplier_invoice
Period: October 2025

Terms
-----
Due Date: 2025-10-21

Supplier Header
---------------
Supplier: Golden State Finance
Expense Category: Repairs Expense
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 2025-10-21
Total: $1,972.39

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 6 | Unit Cost $118.97 | Amount 
$713.80
  - Description Preventive maintenance service parts | Quantity 20 | Unit Cost $62.93 | 
Amount $1,258.59

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D005 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-10-18

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Oakline Services
Total: $274.30
Payment Method: Company card

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount $89.90
  - Description Fuel Incidentals | Amount $184.40
```

### Document D006 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-10-31

```
BANK STATEMENT
==============

From
----
Silverline Advisors
220 Lake View Road, Bengaluru
Date: 2025-10-31

Reference Box
-------------
Document ID: D006
Document Type: bank_statement
Period: October 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0015
Statement Currency: USD
Opening Balance: $55,205.97
Closing Balance: $54,931.67

Statement Rows
--------------
Rows:
  - Date 2025-10-18 | Description Oakline Services receipt RCPT-0001 | Amount $-274.30 | 
Running Balance $54,931.67

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D006
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 8,937.91 | D002, D003 | 2025-10-04 | job_invoice |
| 2 | Repairs Expense | Accounts Payable | 1,972.39 | D004 | 2025-10-09 | supplier_bill |
| 3 | Fuel Expense | Cash | 274.30 | D005 | 2025-10-18 | fuel_receipt |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 54,931.67
- Accounts Receivable: 16,983.23

**Liabilities**
- Accounts Payable: 6,777.95

**Equity**
- Owner's Equity: 58,445.73
- Retained Earnings: 6,691.22

**Totals:** Assets = 71,914.90; Liabilities = 6,777.95; Equity = 65,136.95
**Balanced (A = L + E):** True

---

## 7. Verification Form

_Fill in your judgement below. For each question, mark one box and add notes where applicable._

### Q1 — Document analogy to real paperwork
We are not aiming for perfectly real documents — we are aiming for analogues that carry the same kind of information an accountant would normally extract. Treating these as stand-ins, do they convey roughly the same content (parties, dates, amounts, line items, references) that you would expect from the real-world equivalent for this industry and period?
- [x] Yes — analogous to what an accountant would receive
- [ ] Mostly — captures the right information, with rough edges
- [ ] No — missing key information an accountant would rely on, or structurally unlike the real equivalent
- Notes:

### Q2 — Are the expected journal entries correct?
Given only the documents in section 4 (and the opening trial balance), would you book exactly the entries in section 5?
- [x] Yes — entries match what I would book
- [ ] Mostly — minor account / amount issues (please describe)
- [ ] No — significant errors (missing entries, wrong entries, wrong amounts)
- Notes:

### Q3 — Are entries complete?
Are there any entries you would book that are MISSING from section 5? Or any entries in section 5 that should NOT be there?
- [x] Complete and exact
- [ ] Missing entries (list them in notes)
- [ ] Extra entries that should not be booked (list them)
- Notes:

### Q4 — Are document references correct?
For each expected entry, is `doc_refs` the set of documents that actually support that posting?
- [x] Yes, doc_refs are correct
- [ ] Mostly correct with minor mismatches
- [ ] Doc_refs are systematically wrong
- Notes:

### Q5 — Difficulty calibration
Is the difficulty level (section 1) appropriately calibrated for this packet? L1=trivial, L5=hardest.
- [x] Calibration feels right
- [ ] Too easy for this level
- [ ] Too hard for this level
- Notes:

### Q7 — Overall verdict
- [x] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
