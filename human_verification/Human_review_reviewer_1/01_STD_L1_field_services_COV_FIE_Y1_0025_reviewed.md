# Verification Packet — COV_FIE_Y1_0025

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `field_services`
- **Difficulty level (1–5):** 1
- **Period type:** year
- **Period label:** FY 2024
- **Period start → end:** 2024-01-01 → 2024-12-31
- **Entity:** Beacon Manufacturing
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `none`
- **Document count:** 10
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Office Supplies`, `Prepaid Insurance`, `Equipment`, `Vehicles`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Repairs Expense`, `Fuel Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-01-01_

**Assets**
- Cash: 133,169.71
- Accounts Receivable: 12,184.69

**Liabilities**
- Accounts Payable: 12,565.09

**Equity**
- Owner's Equity: 132,789.31


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-01-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/01/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 133.169,71
  - Section assets | Account Accounts Receivable | Amount EUR 12.184,69
  - Section liabilities | Account Accounts Payable | Amount EUR 12.565,09
  - Section equity | Account Owner's Equity | Amount EUR 132.789,31

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D006 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2024-02-16

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0002
Customer: Oak Harbor Foods
Job Site: Marina Site
Scope: Monthly retainer
Approved Amount: EUR 38.303,81

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D007 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-02-17

```
CUSTOMER INVOICE
================

From
----
Beacon Manufacturing
75 Market Road, Mumbai
Date: 17/02/2024

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D007
Document Type: customer_invoice
Period: FY 2024
Contract Ref: CTR-0002
Job Code: JOB-0002

Terms
-----
Due Date: 12/03/2024

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: CTR-0002
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 12/03/2024
Total: EUR 38.303,81

Line Items
----------
Items:
  - Description Consulting sprint | Amount EUR 9.194,15
  - Description Follow-up support | Amount EUR 29.109,66

Field Job
---------
Job Code: JOB-0002

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D002 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2024-02-23

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0001
Customer: Blue Finch Holdings
Job Site: East Tower
Scope: Monthly retainer
Approved Amount: EUR 17.710,94

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-02-24

```
CUSTOMER INVOICE
================

From
----
Beacon Manufacturing
75 Market Road, Mumbai
Date: 24/02/2024

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: FY 2024
Contract Ref: CTR-0001
Job Code: JOB-0001

Terms
-----
Due Date: 15/03/2024

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 15/03/2024
Total: EUR 17.710,94

Line Items
----------
Items:
  - Description Monthly retainer | Amount EUR 5.717,09
  - Description Follow-up support | Amount EUR 11.993,85

Field Job
---------
Job Code: JOB-0001

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D004 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-03

```
SUPPLIER INVOICE
================

From
----
Beacon Manufacturing
75 Market Road, Mumbai
Date: 03/04/2024

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D004
Document Type: supplier_invoice
Period: FY 2024

Terms
-----
Due Date: 24/04/2024

Supplier Header
---------------
Supplier: Vertex Supply Co.
Expense Category: Repairs Expense
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 24/04/2024
Total: EUR 15.120,76

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 30 | Unit Cost EUR 167,16 | 
Amount EUR 5.014,78
  - Description Preventive maintenance service parts | Quantity 25 | Unit Cost EUR 404,24 | 
Amount EUR 10.105,98

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D008 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-04-26

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0002
Merchant: Golden State Finance
Total: EUR 628,39
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount EUR 129,77
  - Description Fuel Incidentals | Amount EUR 498,62
```

### Document D005 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-06-04

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Prime Utility Desk
Total: EUR 1.139,40
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount EUR 354,45
  - Description Fuel Incidentals | Amount EUR 784,95
```

### Document D009 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2024-12-31

```
VENDOR STATEMENT
================

From
----
Beacon Manufacturing
75 Market Road, Mumbai
Document Date: 31/12/2024

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D009
Document Type: vendor_statement
Period: FY 2024

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Vertex Supply Co.
Closing Balance: EUR 15.120,76

Statement Lines
---------------
Lines:
  - Reference BILL-0001 | Document Type Open invoice | Amount EUR 15.120,76 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D010 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Beacon Manufacturing
75 Market Road, Mumbai
Date: 31/12/2024

Reference Box
-------------
Document ID: D010
Document Type: bank_statement
Period: FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0025
Statement Currency: EUR
Opening Balance: EUR 133.169,71
Closing Balance: EUR 131.401,92

Statement Rows
--------------
Rows:
  - Date 26/04/2024 | Description Golden State Finance receipt RCPT-0002 | Amount EUR 
-628,39 | Running Balance EUR 132.541,32
  - Date 04/06/2024 | Description Prime Utility Desk receipt RCPT-0001 | Amount EUR 
-1.139,40 | Running Balance EUR 131.401,92

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D010
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 17,710.94 | D002, D003 | 2024-02-24 | job_invoice |
| 2 | Repairs Expense | Accounts Payable | 15,120.76 | D004 | 2024-04-03 | supplier_bill |
| 3 | Fuel Expense | Cash | 1,139.40 | D005 | 2024-06-04 | fuel_receipt |
| 4 | Accounts Receivable | Service Revenue | 38,303.81 | D006, D007 | 2024-02-17 | job_invoice |
| 5 | Fuel Expense | Cash | 628.39 | D008 | 2024-04-26 | fuel_receipt |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 131,401.92
- Accounts Receivable: 68,199.44

**Liabilities**
- Accounts Payable: 27,685.85

**Equity**
- Owner's Equity: 132,789.31
- Retained Earnings: 39,126.20

**Totals:** Assets = 199,601.36; Liabilities = 27,685.85; Equity = 171,915.51
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
- Notes: Support ties reasonably well to postings.
