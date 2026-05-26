# Verification Packet — COV_FIE_Y3_0027

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `field_services`
- **Difficulty level (1–5):** 3
- **Period type:** year
- **Period label:** FY 2024
- **Period start → end:** 2024-01-01 → 2024-12-31
- **Entity:** Northwind Builders
- **Currency (display / functional):** USD / USD
- **Tax regime:** `gst`
- **Document count:** 21
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Office Supplies`, `Prepaid Insurance`, `Equipment`, `Vehicles`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Repairs Expense`, `Fuel Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-01-01_

**Assets**
- Cash: 214,168.83
- Accounts Receivable: 28,013.62
- Office Supplies: 4,223.99
- Vehicles: 41,713.47
- Prepaid Insurance: 7,267.89

**Liabilities**
- Accounts Payable: 9,176.25
- Accrued Expenses: 2,877.63

**Equity**
- Retained Earnings: 17,859.18
- Owner's Equity: 265,474.74


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
Statement Date: 2024-01-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $214,168.83
  - Section assets | Account Accounts Receivable | Amount $28,013.62
  - Section assets | Account Office Supplies | Amount $4,223.99
  - Section assets | Account Vehicles | Amount $41,713.47
  - Section assets | Account Prepaid Insurance | Amount $7,267.89
  - Section liabilities | Account Accounts Payable | Amount $9,176.25
  - Section liabilities | Account Accrued Expenses | Amount $2,877.63
  - Section equity | Account Retained Earnings | Amount $17,859.18
  - Section equity | Account Owner's Equity | Amount $265,474.74

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D015 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-09

```
SUPPLIER INVOICE
================

From
----
Northwind Builders
90 Hill Park, Hyderabad
Date: 2024-03-09

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D015
Document Type: supplier_invoice
Period: FY 2024

Terms
-----
Due Date: 2024-03-21

Supplier Header
---------------
Supplier: Pace Office Mart
Expense Category: Repairs Expense
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: BILL-0004
Due Date: 2024-03-21
Subtotal: $31,355.23
Tax Label: GST
Tax Rate: 5.00%
Tax Amount: $1,567.76
Total: $32,922.99

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 10 | Unit Cost $819.60 | Amount 
$8,196.01
  - Description Preventive maintenance service parts | Quantity 16 | Unit Cost $1,447.45 | 
Amount $23,159.22

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D014 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-15

```
SUPPLIER INVOICE
================

From
----
Northwind Builders
90 Hill Park, Hyderabad
Date: 2024-03-15

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D014
Document Type: supplier_invoice
Period: FY 2024

Terms
-----
Due Date: 2024-03-28

Supplier Header
---------------
Supplier: Meridian Support LLP
Expense Category: Repairs Expense
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: BILL-0003
Due Date: 2024-03-28
Subtotal: $20,810.38
Tax Label: GST
Tax Rate: 5.00%
Tax Amount: $1,040.52
Total: $21,850.90

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 13 | Unit Cost $369.25 | Amount 
$4,800.23
  - Description Preventive maintenance service parts | Quantity 17 | Unit Cost $941.77 | 
Amount $16,010.15

Footer
------
Internal document packet copy.
Page marker: D014
```

### Document D002 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2024-03-22

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0001
Customer: Crescent Labs
Job Site: North Yard
Scope: Review pack
Approved Amount: $25,187.89

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-23

```
CUSTOMER INVOICE
================

From
----
Northwind Builders
90 Hill Park, Hyderabad
Document Date: 2024-03-23

To
--
Crescent Labs
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
Due Date: 2024-04-16

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2024-04-16
Subtotal: $25,187.89
Tax Label: GST
Tax Rate: 7.00%
Tax Amount: $1,763.15
Total: $26,951.04

Line Items
----------
Items:
  - Description Support package | Amount $9,627.81
  - Description Follow-up support | Amount $15,560.08

Field Job
---------
Job Code: JOB-0001

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D017 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-03-23

```
SECONDARY COPY
==============

From
----
Northwind Builders
90 Hill Park, Hyderabad
Date: 2024-03-23

To
--
Crescent Labs

Reference Box
-------------
Document ID: D017
Document Type: secondary_copy
Period: FY 2024

Copy Summary
------------
Copy ID: COPY-0001
Source Reference: INV-0001
Counterparty: Crescent Labs
Total: $26,951.04
Copy Context: Forwarded copy attached to the customer correspondence bundle.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D020 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2024-03-23

```
CANCELLATION NOTE
=================

From
----
Northwind Builders
90 Hill Park, Hyderabad
Date: 2024-03-23

Reference Box
-------------
Document ID: D020
Document Type: cancellation_note
Period: FY 2024

Cancellation Summary
--------------------
Note Number: CNCL-0001
Withdrawn Reference: INV-0001-OLD
Replacement Reference: INV-0001

Background
----------
Narrative: INV-0001-OLD is withdrawn and must not be posted. Use INV-0001 as the only valid 
invoice.

Footer
------
Internal document packet copy.
Page marker: D020
```

### Document D016 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-29

```
SUPPLIER INVOICE
================

From
----
Northwind Builders
90 Hill Park, Hyderabad
Date: 2024-03-29

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D016
Document Type: supplier_invoice
Period: FY 2024

Terms
-----
Due Date: 2024-04-11

Supplier Header
---------------
Supplier: Golden State Finance
Expense Category: Repairs Expense
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: BILL-0005
Due Date: 2024-04-11
Subtotal: $39,650.44
Tax Label: GST
Tax Rate: 10.00%
Tax Amount: $3,965.04
Total: $43,615.48

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 16 | Unit Cost $804.91 | Amount 
$12,878.62
  - Description Preventive maintenance service parts | Quantity 20 | Unit Cost $1,338.59 | 
Amount $26,771.82

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D019 — Secondary Copy

- **Type:** `secondary_copy`
- **Role:** `distractor_doc`
- **Date:** 2024-03-29

```
SECONDARY COPY
==============

From
----
Northwind Builders
90 Hill Park, Hyderabad
Date: 2024-03-29

To
--
Golden State Finance

Reference Box
-------------
Document ID: D019
Document Type: secondary_copy
Period: FY 2024

Copy Summary
------------
Copy ID: COPY-0002
Source Reference: BILL-0005
Counterparty: Golden State Finance
Total: $43,615.48
Copy Context: Second scan captured during the filing review.

Notes
-----
Filed with the scanned month-end paperwork.

Footer
------
Internal document packet copy.
Page marker: D019
```

### Document D013 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-03-31

```
SUPPLIER INVOICE
================

From
----
Northwind Builders
90 Hill Park, Hyderabad
Date: 2024-03-31

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D013
Document Type: supplier_invoice
Period: FY 2024

Terms
-----
Due Date: 2024-04-16

Supplier Header
---------------
Supplier: Vertex Supply Co.
Expense Category: Repairs Expense
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: BILL-0002
Due Date: 2024-04-16
Subtotal: $24,731.85
Tax Label: GST
Tax Rate: 5.00%
Tax Amount: $1,236.59
Total: $25,968.44

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 18 | Unit Cost $505.67 | Amount 
$9,102.02
  - Description Preventive maintenance service parts | Quantity 20 | Unit Cost $781.49 | 
Amount $15,629.83

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D004 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-05

```
SUPPLIER INVOICE
================

From
----
Northwind Builders
90 Hill Park, Hyderabad
Date: 2024-04-05

To
--
Prime Utility Desk
Vendor remittance address on file

Reference Box
-------------
Document ID: D004
Document Type: supplier_invoice
Period: FY 2024

Terms
-----
Due Date: 2024-04-17

Supplier Header
---------------
Supplier: Prime Utility Desk
Expense Category: Repairs Expense
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 2024-04-17
Subtotal: $39,025.76
Tax Label: GST
Tax Rate: 5.00%
Tax Amount: $1,951.29
Total: $40,977.05

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 8 | Unit Cost $1,052.38 | Amount
 $8,419.00
  - Description Preventive maintenance service parts | Quantity 2 | Unit Cost $15,303.38 | 
Amount $30,606.76

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D010 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2024-04-10

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0002
Customer: Crescent Labs
Job Site: East Tower
Scope: Review pack
Approved Amount: $62,312.39

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D011 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-11

```
CUSTOMER INVOICE
================

From
----
Northwind Builders
90 Hill Park, Hyderabad
Document Date: 2024-04-11

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D011
Document Type: customer_invoice
Period: FY 2024
Contract Ref: CTR-0002
Job Code: JOB-0002

Terms
-----
Due Date: 2024-05-01

Parties
-------
Customer: Crescent Labs
Contract Ref: CTR-0002
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2024-05-01
Subtotal: $62,312.39
Tax Label: GST
Tax Rate: 10.00%
Tax Amount: $6,231.24
Total: $68,543.63

Line Items
----------
Items:
  - Description Review pack | Amount $15,447.11
  - Description Follow-up support | Amount $46,865.28

Field Job
---------
Job Code: JOB-0002

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D005 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-07-05

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Oakline Services
Total: $1,316.70
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount $289.85
  - Description Fuel Incidentals | Amount $1,026.85
```

### Document D012 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-08-06

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0002
Merchant: Oakline Services
Total: $921.72
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount $361.94
  - Description Fuel Incidentals | Amount $559.78
```

### Document D008 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2024-09-20

```
PAYROLL SUMMARY
===============

From
----
Northwind Builders
90 Hill Park, Hyderabad
Date: 2024-09-20

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Annual payroll summary for FY 2024
Headcount: 7
Gross Pay: $24,324.64
Employer Tax: 2,070.36
Cash Outflow: $26,395.00

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-10-08

```
PAYMENT ADVICE
==============

From
----
Northwind Builders
90 Hill Park, Hyderabad
Document Date: 2024-10-08

To
--
Crescent Labs

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: FY 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Crescent Labs
Amount: $26,951.04
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-11-10

```
PAYMENT ADVICE
==============

From
----
Northwind Builders
90 Hill Park, Hyderabad
Date: 2024-11-10

To
--
Prime Utility Desk

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: FY 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Prime Utility Desk
Amount: $40,977.05
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D009 — Service Period Memo

- **Type:** `service_period_memo`
- **Role:** `adjustment_doc`
- **Date:** 2024-12-31

```
SERVICE PERIOD MEMO
===================

From
----
Northwind Builders
90 Hill Park, Hyderabad
Document Date: 2024-12-31

Reference Box
-------------
Document ID: D009
Document Type: service_period_memo
Period: FY 2024
Reference: FY 2024

Approval / Context
------------------
Subject: Month-end expense accrual

Memo Summary
------------
Memo ID: ACCR-0001
Subject: Month-end expense accrual
Reference: FY 2024
Recognized Amount: $6,813.36

Explanation
-----------
Narrative: Accrue unpaid repairs expense incurred before period end.

Footer
------
Generated for synthetic accounting research use.
Page marker: D009
```

### Document D018 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2024-12-31

```
VENDOR STATEMENT
================

From
----
Northwind Builders
90 Hill Park, Hyderabad
Document Date: 2024-12-31

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D018
Document Type: vendor_statement
Period: FY 2024

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Golden State Finance
Closing Balance: $43,615.48

Statement Lines
---------------
Lines:
  - Reference BILL-0005 | Document Type Open invoice | Amount $43,615.48 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D021 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Northwind Builders
90 Hill Park, Hyderabad
Date: 2024-12-31

Reference Box
-------------
Document ID: D021
Document Type: bank_statement
Period: FY 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0027
Statement Currency: USD
Opening Balance: $214,168.83
Closing Balance: $171,509.40

Statement Rows
--------------
Rows:
  - Date 2024-07-05 | Description Oakline Services receipt RCPT-0001 | Amount $-1,316.70 | 
Running Balance $212,852.13
  - Date 2024-08-06 | Description Oakline Services receipt RCPT-0002 | Amount $-921.72 | 
Running Balance $211,930.41
  - Date 2024-09-20 | Description Payroll PAYRUN-0001 | Amount $-26,395.00 | Running Balance
 $185,535.41
  - Date 2024-10-08 | Description Customer settlement INV-0001 | Amount $26,951.04 | Running
 Balance $212,486.45
  - Date 2024-11-10 | Description Supplier settlement BILL-0001 | Amount $-40,977.05 | 
Running Balance $171,509.40

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D021
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 25,187.89 | D002, D003 | 2024-03-23 | job_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 1,763.15 | D002, D003 | 2024-03-23 | job_invoice_tax |
| 3 | Repairs Expense | Accounts Payable | 39,025.76 | D004 | 2024-04-05 | supplier_bill |
| 4 | Input Tax Receivable | Accounts Payable | 1,951.29 | D004 | 2024-04-05 | supplier_bill_tax |
| 5 | Fuel Expense | Cash | 1,316.70 | D005 | 2024-07-05 | fuel_receipt |
| 6 | Cash | Accounts Receivable | 26,951.04 | D006, D003 | 2024-10-08 | customer_payment |
| 7 | Accounts Payable | Cash | 40,977.05 | D007, D004 | 2024-11-10 | supplier_payment |
| 8 | Salaries Expense | Cash | 24,324.64 | D008 | 2024-09-20 | payroll_gross |
| 9 | Payroll Tax Expense | Cash | 2,070.36 | D008 | 2024-09-20 | payroll_tax |
| 10 | Repairs Expense | Accrued Expenses | 6,813.36 | D009 | 2024-12-31 | expense_accrual |
| 11 | Accounts Receivable | Service Revenue | 62,312.39 | D010, D011 | 2024-04-11 | job_invoice |
| 12 | Accounts Receivable | Sales Tax Payable | 6,231.24 | D010, D011 | 2024-04-11 | job_invoice_tax |
| 13 | Fuel Expense | Cash | 921.72 | D012 | 2024-08-06 | fuel_receipt |
| 14 | Repairs Expense | Accounts Payable | 24,731.85 | D013 | 2024-03-31 | supplier_bill |
| 15 | Input Tax Receivable | Accounts Payable | 1,236.59 | D013 | 2024-03-31 | supplier_bill_tax |
| 16 | Repairs Expense | Accounts Payable | 20,810.38 | D014 | 2024-03-15 | supplier_bill |
| 17 | Input Tax Receivable | Accounts Payable | 1,040.52 | D014 | 2024-03-15 | supplier_bill_tax |
| 18 | Repairs Expense | Accounts Payable | 31,355.23 | D015 | 2024-03-09 | supplier_bill |
| 19 | Input Tax Receivable | Accounts Payable | 1,567.76 | D015 | 2024-03-09 | supplier_bill_tax |
| 20 | Repairs Expense | Accounts Payable | 39,650.44 | D016 | 2024-03-29 | supplier_bill |
| 21 | Input Tax Receivable | Accounts Payable | 3,965.04 | D016 | 2024-03-29 | supplier_bill_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 171,509.40
- Accounts Receivable: 96,557.25
- Office Supplies: 4,223.99
- Vehicles: 41,713.47
- Prepaid Insurance: 7,267.89
- Input Tax Receivable: 9,761.20

**Liabilities**
- Accounts Payable: 133,534.06
- Accrued Expenses: 9,690.99
- Sales Tax Payable: 7,994.39

**Equity**
- Retained Earnings: -85,660.98
- Owner's Equity: 265,474.74

**Totals:** Assets = 331,033.20; Liabilities = 151,219.44; Equity = 179,813.76
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
- Notes: No concerns here.
