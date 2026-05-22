# Verification Packet — COV_FIE_Q3_0022

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `field_services`
- **Difficulty level (1–5):** 3
- **Period type:** quarter
- **Period label:** Q4 FY 2025-26
- **Period start → end:** 2025-01-01 → 2025-03-31
- **Entity:** Pioneer Advisors
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `us_sales_tax`
- **Document count:** 13
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Office Supplies`, `Prepaid Insurance`, `Equipment`, `Vehicles`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Repairs Expense`, `Fuel Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 79,016.61
- Accounts Receivable: 12,072.05
- Office Supplies: 2,661.16
- Vehicles: 12,855.81
- Prepaid Insurance: 2,738.35

**Liabilities**
- Accounts Payable: 3,585.28
- Accrued Expenses: 1,048.54

**Equity**
- Retained Earnings: 6,176.31
- Owner's Equity: 98,533.85


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2025-01-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/01/2025
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 79.016,61
  - Section assets | Account Accounts Receivable | Amount EUR 12.072,05
  - Section assets | Account Office Supplies | Amount EUR 2.661,16
  - Section assets | Account Vehicles | Amount EUR 12.855,81
  - Section assets | Account Prepaid Insurance | Amount EUR 2.738,35
  - Section liabilities | Account Accounts Payable | Amount EUR 3.585,28
  - Section liabilities | Account Accrued Expenses | Amount EUR 1.048,54
  - Section equity | Account Retained Earnings | Amount EUR 6.176,31
  - Section equity | Account Owner's Equity | Amount EUR 98.533,85

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D012 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-10

```
SUPPLIER INVOICE
================

From
----
Pioneer Advisors
220 Lake View Road, Bengaluru
Date: 10/01/2025

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D012
Document Type: supplier_invoice
Period: Q4 FY 2025-26

Terms
-----
Due Date: 20/01/2025

Supplier Header
---------------
Supplier: Prime Utility Desk
Expense Category: Repairs Expense
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: BILL-0002
Due Date: 20/01/2025
Subtotal: EUR 4.117,68
Tax Label: US Sales Tax
Tax Rate: 6.25%
Tax Amount: EUR 257,36
Total: EUR 4.375,04

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 3 | Unit Cost EUR 336,10 | 
Amount EUR 1.008,29
  - Description Preventive maintenance service parts | Quantity 6 | Unit Cost EUR 518,23 | 
Amount EUR 3.109,39

Footer
------
Internal document packet copy.
Page marker: D012
```

### Document D002 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2025-01-11

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0001
Customer: Aster Point Services
Job Site: North Yard
Scope: Review pack
Approved Amount: EUR 10.553,96

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-12

```
CUSTOMER INVOICE
================

From
----
Pioneer Advisors
220 Lake View Road, Bengaluru
Date: 12/01/2025

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: Q4 FY 2025-26
Contract Ref: CTR-0001
Job Code: JOB-0001

Terms
-----
Due Date: 28/01/2025

Parties
-------
Customer: Aster Point Services
Contract Ref: CTR-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 28/01/2025
Subtotal: EUR 10.553,96
Tax Label: US Sales Tax
Tax Rate: 7.25%
Tax Amount: EUR 765,16
Total: EUR 11.319,12

Line Items
----------
Items:
  - Description Implementation work | Amount EUR 2.891,43
  - Description Follow-up support | Amount EUR 7.662,53

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
- **Date:** 2025-01-16

```
SUPPLIER INVOICE
================

From
----
Pioneer Advisors
220 Lake View Road, Bengaluru
Date: 16/01/2025

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D004
Document Type: supplier_invoice
Period: Q4 FY 2025-26

Terms
-----
Due Date: 28/01/2025

Supplier Header
---------------
Supplier: Golden State Finance
Expense Category: Repairs Expense
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 28/01/2025
Subtotal: EUR 6.723,91
Tax Label: US Sales Tax
Tax Rate: 6.25%
Tax Amount: EUR 420,24
Total: EUR 7.144,15

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 17 | Unit Cost EUR 115,12 | 
Amount EUR 1.957,00
  - Description Preventive maintenance service parts | Quantity 18 | Unit Cost EUR 264,83 | 
Amount EUR 4.766,91

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D010 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2025-01-24

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0002
Customer: Metro Edge Partners
Job Site: East Tower
Scope: Support package
Approved Amount: EUR 27.158,37

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D011 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-25

```
CUSTOMER INVOICE
================

From
----
Pioneer Advisors
220 Lake View Road, Bengaluru
Date: 25/01/2025

To
--
Metro Edge Partners
Customer account on file

Reference Box
-------------
Document ID: D011
Document Type: customer_invoice
Period: Q4 FY 2025-26
Contract Ref: CTR-0002
Job Code: JOB-0002

Terms
-----
Due Date: 08/02/2025

Parties
-------
Customer: Metro Edge Partners
Contract Ref: CTR-0002
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 08/02/2025
Subtotal: EUR 27.158,37
Tax Label: US Sales Tax
Tax Rate: 8.25%
Tax Amount: EUR 2.240,57
Total: EUR 29.398,94

Line Items
----------
Items:
  - Description Review pack | Amount EUR 11.686,24
  - Description Follow-up support | Amount EUR 15.472,13

Field Job
---------
Job Code: JOB-0002

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D005 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-02-27

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Oakline Services
Total: EUR 110,74
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount EUR 29,92
  - Description Fuel Incidentals | Amount EUR 80,82
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-03-09

```
PAYMENT ADVICE
==============

From
----
Pioneer Advisors
220 Lake View Road, Bengaluru
Date: 09/03/2025

To
--
Aster Point Services

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q4 FY 2025-26
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Aster Point Services
Amount: EUR 11.319,12
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-03-11

```
PAYMENT ADVICE
==============

From
----
Pioneer Advisors
220 Lake View Road, Bengaluru
Date: 11/03/2025

To
--
Golden State Finance

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: Q4 FY 2025-26
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Golden State Finance
Amount: EUR 7.144,15
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-03-22

```
PAYROLL SUMMARY
===============

From
----
Pioneer Advisors
220 Lake View Road, Bengaluru
Date: 22/03/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q4 FY 2025-26
Headcount: 12
Gross Pay: EUR 33.449,87
Employer Tax: 3.275,36
Cash Outflow: EUR 36.725,23

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D009 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
SERVICE PERIOD MEMO
===================

From
----
Pioneer Advisors
220 Lake View Road, Bengaluru
Document Date: 31/03/2025

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: Q4 FY 2025-26
Reference: Q4 FY 2025-26

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: Q4 FY 2025-26
Recognized Amount: EUR 4.447,43

Explanation
-----------
Narrative: Accrue unpaid repairs expense incurred before period end.

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D013 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Pioneer Advisors
220 Lake View Road, Bengaluru
Document Date: 31/03/2025

Reference Box
-------------
Document ID: D013
Document Type: bank_statement
Period: Q4 FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0022
Statement Currency: EUR
Opening Balance: EUR 79.016,61
Closing Balance: EUR 46.355,61

Statement Rows
--------------
Rows:
  - Date 27/02/2025 | Description Oakline Services receipt RCPT-0001 | Amount EUR -110,74 | 
Running Balance EUR 78.905,87
  - Date 09/03/2025 | Description Customer settlement INV-0001 | Amount EUR 11.319,12 | 
Running Balance EUR 90.224,99
  - Date 11/03/2025 | Description Supplier settlement BILL-0001 | Amount EUR -7.144,15 | 
Running Balance EUR 83.080,84
  - Date 22/03/2025 | Description Payroll PAYRUN-0001 | Amount EUR -36.725,23 | Running 
Balance EUR 46.355,61

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D013
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 10,553.96 | D002, D003 | 2025-01-12 | job_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 765.16 | D002, D003 | 2025-01-12 | job_invoice_tax |
| 3 | Repairs Expense | Accounts Payable | 6,723.91 | D004 | 2025-01-16 | supplier_bill |
| 4 | Input Tax Receivable | Accounts Payable | 420.24 | D004 | 2025-01-16 | supplier_bill_tax |
| 5 | Fuel Expense | Cash | 110.74 | D005 | 2025-02-27 | fuel_receipt |
| 6 | Cash | Accounts Receivable | 11,319.12 | D006, D003 | 2025-03-09 | customer_payment |
| 7 | Accounts Payable | Cash | 7,144.15 | D007, D004 | 2025-03-11 | supplier_payment |
| 8 | Salaries Expense | Cash | 33,449.87 | D008 | 2025-03-22 | payroll_gross |
| 9 | Payroll Tax Expense | Cash | 3,275.36 | D008 | 2025-03-22 | payroll_tax |
| 10 | Repairs Expense | Accrued Expenses | 4,447.43 | D009 | 2025-03-31 | expense_accrual |
| 11 | Accounts Receivable | Service Revenue | 27,158.37 | D010, D011 | 2025-01-25 | job_invoice |
| 12 | Accounts Receivable | Sales Tax Payable | 2,240.57 | D010, D011 | 2025-01-25 | job_invoice_tax |
| 13 | Repairs Expense | Accounts Payable | 4,117.68 | D012 | 2025-01-10 | supplier_bill |
| 14 | Input Tax Receivable | Accounts Payable | 257.36 | D012 | 2025-01-10 | supplier_bill_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 46,355.61
- Accounts Receivable: 41,470.99
- Office Supplies: 2,661.16
- Vehicles: 12,855.81
- Prepaid Insurance: 2,738.35
- Input Tax Receivable: 677.60

**Liabilities**
- Accounts Payable: 7,960.32
- Accrued Expenses: 5,495.97
- Sales Tax Payable: 3,005.73

**Equity**
- Retained Earnings: -8,236.35
- Owner's Equity: 98,533.85

**Totals:** Assets = 106,759.52; Liabilities = 16,462.02; Equity = 90,297.50
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
