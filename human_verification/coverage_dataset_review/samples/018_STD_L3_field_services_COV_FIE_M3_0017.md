# Verification Packet — COV_FIE_M3_0017

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `field_services`
- **Difficulty level (1–5):** 3
- **Period type:** month
- **Period label:** November 2024
- **Period start → end:** 2024-11-01 → 2024-11-30
- **Entity:** Willow Advisors
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `india_gst`
- **Document count:** 10
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Office Supplies`, `Prepaid Insurance`, `Equipment`, `Vehicles`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Repairs Expense`, `Fuel Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-11-01_

**Assets**
- Cash: 46,288.69
- Accounts Receivable: 2,263.45
- Office Supplies: 929.57
- Vehicles: 11,360.53

**Liabilities**
- Accounts Payable: 4,277.32
- Accrued Expenses: 1,805.52

**Equity**
- Retained Earnings: 10,992.07
- Owner's Equity: 43,767.33


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-11-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/11/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 46,288.69
  - Section assets | Account Accounts Receivable | Amount GBP 2,263.45
  - Section assets | Account Office Supplies | Amount GBP 929.57
  - Section assets | Account Vehicles | Amount GBP 11,360.53
  - Section liabilities | Account Accounts Payable | Amount GBP 4,277.32
  - Section liabilities | Account Accrued Expenses | Amount GBP 1,805.52
  - Section equity | Account Retained Earnings | Amount GBP 10,992.07
  - Section equity | Account Owner's Equity | Amount GBP 43,767.33

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D004 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-03

```
SUPPLIER INVOICE
================

From
----
Willow Advisors
220 Lake View Road, Bengaluru
Date: 03/11/2024

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D004
Document Type: supplier_invoice
Period: November 2024

Terms
-----
Due Date: 24/11/2024

Supplier Header
---------------
Supplier: Prime Utility Desk
Expense Category: Repairs Expense
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 24/11/2024
Subtotal: GBP 2,849.46
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 512.90
CGST Amount: GBP 256.45
SGST Amount: GBP 256.45
Total: GBP 3,362.36

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 30 | Unit Cost GBP 34.84 | 
Amount GBP 1,045.05
  - Description Preventive maintenance service parts | Quantity 29 | Unit Cost GBP 62.22 | 
Amount GBP 1,804.41

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D009 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-04

```
SUPPLIER INVOICE
================

From
----
Willow Advisors
220 Lake View Road, Bengaluru
Document Date: 04/11/2024

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D009
Document Type: supplier_invoice
Period: November 2024

Terms
-----
Due Date: 23/11/2024

Supplier Header
---------------
Supplier: Beacon Industrial Supply
Expense Category: Repairs Expense
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0002
Due Date: 23/11/2024
Subtotal: GBP 1,050.94
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 126.11
CGST Amount: GBP 63.05
SGST Amount: GBP 63.06
Total: GBP 1,177.05

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 21 | Unit Cost GBP 18.00 | 
Amount GBP 378.03
  - Description Preventive maintenance service parts | Quantity 14 | Unit Cost GBP 48.06 | 
Amount GBP 672.91

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D002 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2024-11-06

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0001
Customer: Oak Harbor Foods
Job Site: Riverbank Plaza
Scope: Consulting sprint
Approved Amount: GBP 3,081.11

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-07

```
CUSTOMER INVOICE
================

From
----
Willow Advisors
220 Lake View Road, Bengaluru
Date: 07/11/2024

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: November 2024
Contract Ref: CTR-0001
Job Code: JOB-0001

Terms
-----
Due Date: 18/11/2024

Parties
-------
Customer: Oak Harbor Foods
Contract Ref: CTR-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 18/11/2024
Subtotal: GBP 3,081.11
Tax Label: India GST
Tax Rate: 5.00%
Tax Amount: GBP 154.06
CGST Amount: GBP 77.03
SGST Amount: GBP 77.03
Total: GBP 3,235.17

Line Items
----------
Items:
  - Description Monthly retainer | Amount GBP 765.14
  - Description Follow-up support | Amount GBP 2,315.97

Field Job
---------
Job Code: JOB-0001

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D005 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-11-15

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Golden State Finance
Total: GBP 6.34
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount GBP 2.50
  - Description Fuel Incidentals | Amount GBP 3.84
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-11-23

```
PAYMENT ADVICE
==============

From
----
Willow Advisors
220 Lake View Road, Bengaluru
Document Date: 23/11/2024

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: November 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Prime Utility Desk
Amount: GBP 3,362.36
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-11-24

```
PAYMENT ADVICE
==============

From
----
Willow Advisors
220 Lake View Road, Bengaluru
Date: 24/11/2024

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: November 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Oak Harbor Foods
Amount: GBP 3,235.17
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-11-26

```
PAYROLL SUMMARY
===============

From
----
Willow Advisors
220 Lake View Road, Bengaluru
Date: 26/11/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: November 2024
Headcount: 7
Gross Pay: GBP 10,176.02
Employer Tax: 1,418.47
Cash Outflow: GBP 11,594.49

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D010 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-11-30

```
BANK STATEMENT
==============

From
----
Willow Advisors
220 Lake View Road, Bengaluru
Document Date: 30/11/2024

Reference Box
-------------
Document ID: D010
Document Type: bank_statement
Period: November 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0017
Statement Currency: GBP
Opening Balance: GBP 46,288.69
Closing Balance: GBP 34,560.67

Statement Rows
--------------
Rows:
  - Date 15/11/2024 | Description Golden State Finance receipt RCPT-0001 | Amount GBP -6.34 
| Running Balance GBP 46,282.35
  - Date 23/11/2024 | Description Supplier settlement BILL-0001 | Amount GBP -3,362.36 | 
Running Balance GBP 42,919.99
  - Date 24/11/2024 | Description Customer settlement INV-0001 | Amount GBP 3,235.17 | 
Running Balance GBP 46,155.16
  - Date 26/11/2024 | Description Payroll PAYRUN-0001 | Amount GBP -11,594.49 | Running 
Balance GBP 34,560.67

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 3,081.11 | D002, D003 | 2024-11-07 | job_invoice |
| 2 | Accounts Receivable | CGST Payable | 77.03 | D002, D003 | 2024-11-07 | job_invoice_tax_cgst |
| 3 | Accounts Receivable | SGST Payable | 77.03 | D002, D003 | 2024-11-07 | job_invoice_tax_sgst |
| 4 | Repairs Expense | Accounts Payable | 2,849.46 | D004 | 2024-11-03 | supplier_bill |
| 5 | Input CGST Receivable | Accounts Payable | 256.45 | D004 | 2024-11-03 | supplier_bill_tax_cgst |
| 6 | Input SGST Receivable | Accounts Payable | 256.45 | D004 | 2024-11-03 | supplier_bill_tax_sgst |
| 7 | Fuel Expense | Cash | 6.34 | D005 | 2024-11-15 | fuel_receipt |
| 8 | Cash | Accounts Receivable | 3,235.17 | D006, D003 | 2024-11-24 | customer_payment |
| 9 | Accounts Payable | Cash | 3,362.36 | D007, D004 | 2024-11-23 | supplier_payment |
| 10 | Salaries Expense | Cash | 10,176.02 | D008 | 2024-11-26 | payroll_gross |
| 11 | Payroll Tax Expense | Cash | 1,418.47 | D008 | 2024-11-26 | payroll_tax |
| 12 | Repairs Expense | Accounts Payable | 1,050.94 | D009 | 2024-11-04 | supplier_bill |
| 13 | Input CGST Receivable | Accounts Payable | 63.05 | D009 | 2024-11-04 | supplier_bill_tax_cgst |
| 14 | Input SGST Receivable | Accounts Payable | 63.06 | D009 | 2024-11-04 | supplier_bill_tax_sgst |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 34,560.67
- Accounts Receivable: 2,263.45
- Office Supplies: 929.57
- Vehicles: 11,360.53
- Input CGST Receivable: 319.50
- Input SGST Receivable: 319.51

**Liabilities**
- Accounts Payable: 5,454.37
- Accrued Expenses: 1,805.52
- CGST Payable: 77.03
- SGST Payable: 77.03

**Equity**
- Retained Earnings: -1,428.05
- Owner's Equity: 43,767.33

**Totals:** Assets = 49,753.23; Liabilities = 7,413.95; Equity = 42,339.28
**Balanced (A = L + E):** True

---

## 7. Verification Form

_Fill in your judgement below. For each question, mark one box and add notes where applicable._

### Q1 — Document analogy to real paperwork
We are not aiming for perfectly real documents — we are aiming for analogues that carry the same kind of information an accountant would normally extract. Treating these as stand-ins, do they convey roughly the same content (parties, dates, amounts, line items, references) that you would expect from the real-world equivalent for this industry and period?
- [ ] Yes — analogous to what an accountant would receive
- [ ] Mostly — captures the right information, with rough edges
- [ ] No — missing key information an accountant would rely on, or structurally unlike the real equivalent
- Notes:

### Q2 — Are the expected journal entries correct?
Given only the documents in section 4 (and the opening trial balance), would you book exactly the entries in section 5?
- [ ] Yes — entries match what I would book
- [ ] Mostly — minor account / amount issues (please describe)
- [ ] No — significant errors (missing entries, wrong entries, wrong amounts)
- Notes:

### Q3 — Are entries complete?
Are there any entries you would book that are MISSING from section 5? Or any entries in section 5 that should NOT be there?
- [ ] Complete and exact
- [ ] Missing entries (list them in notes)
- [ ] Extra entries that should not be booked (list them)
- Notes:

### Q4 — Are document references correct?
For each expected entry, is `doc_refs` the set of documents that actually support that posting?
- [ ] Yes, doc_refs are correct
- [ ] Mostly correct with minor mismatches
- [ ] Doc_refs are systematically wrong
- Notes:

### Q5 — Difficulty calibration
Is the difficulty level (section 1) appropriately calibrated for this packet? L1=trivial, L5=hardest.
- [ ] Calibration feels right
- [ ] Too easy for this level
- [ ] Too hard for this level
- Notes:

### Q7 — Overall verdict
- [ ] Acceptable as ground truth for benchmark evaluation
- [ ] Acceptable with minor fixes (notes below)
- [ ] Not acceptable as ground truth
- Notes:
