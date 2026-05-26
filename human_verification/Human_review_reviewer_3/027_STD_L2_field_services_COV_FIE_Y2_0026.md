# Verification Packet — COV_FIE_Y2_0026

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `field_services`
- **Difficulty level (1–5):** 2
- **Period type:** year
- **Period label:** FY 2024-25
- **Period start → end:** 2024-04-01 → 2025-03-31
- **Entity:** Silverline Distribution
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `vat`
- **Document count:** 15
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Office Supplies`, `Prepaid Insurance`, `Equipment`, `Vehicles`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Repairs Expense`, `Fuel Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-04-01_

**Assets**
- Cash: 162,683.48
- Accounts Receivable: 16,900.64
- Office Supplies: 2,216.15

**Liabilities**
- Accounts Payable: 15,575.32
- Accrued Expenses: 5,538.15

**Equity**
- Retained Earnings: 37,634.12
- Owner's Equity: 123,052.68


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-04-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/04/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount GBP 162,683.48
  - Section assets | Account Accounts Receivable | Amount GBP 16,900.64
  - Section assets | Account Office Supplies | Amount GBP 2,216.15
  - Section liabilities | Account Accounts Payable | Amount GBP 15,575.32
  - Section liabilities | Account Accrued Expenses | Amount GBP 5,538.15
  - Section equity | Account Retained Earnings | Amount GBP 37,634.12
  - Section equity | Account Owner's Equity | Amount GBP 123,052.68

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D012 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-04-19

```
SUPPLIER INVOICE
================

From
----
Silverline Distribution
75 Market Road, Mumbai
Document Date: 19/04/2024

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D012
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 02/05/2024

Supplier Header
---------------
Supplier: Vertex Supply Co.
Expense Category: Repairs Expense
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0005
Due Date: 02/05/2024
Subtotal: GBP 26,248.81
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 5,249.76
Total: GBP 31,498.57

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 16 | Unit Cost GBP 646.90 | 
Amount GBP 10,350.34
  - Description Preventive maintenance service parts | Quantity 29 | Unit Cost GBP 548.22 | 
Amount GBP 15,898.47

Footer
------
Generated for synthetic accounting research use.
Page marker: D012
```

### Document D002 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2024-05-12

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0001
Customer: Blue Finch Holdings
Job Site: Marina Site
Scope: Review pack
Approved Amount: GBP 36,264.76

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-05-13

```
CUSTOMER INVOICE
================

From
----
Silverline Distribution
75 Market Road, Mumbai
Date: 13/05/2024

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: FY 2024-25
Contract Ref: CTR-0001
Job Code: JOB-0001

Terms
-----
Due Date: 31/05/2024

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0001
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 31/05/2024
Subtotal: GBP 36,264.76
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 7,252.95
Total: GBP 43,517.71

Line Items
----------
Items:
  - Description Review pack | Amount GBP 12,002.39
  - Description Follow-up support | Amount GBP 24,262.37

Field Job
---------
Job Code: JOB-0001

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D014 — Cancellation Note

- **Type:** `cancellation_note`
- **Role:** `distractor_doc`
- **Date:** 2024-05-13

```
CANCELLATION NOTE
=================

From
----
Silverline Distribution
75 Market Road, Mumbai
Date: 13/05/2024

Reference Box
-------------
Document ID: D014
Document Type: cancellation_note
Period: FY 2024-25

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
Page marker: D014
```

### Document D010 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-03

```
SUPPLIER INVOICE
================

From
----
Silverline Distribution
75 Market Road, Mumbai
Date: 03/06/2024

To
--
Meridian Support LLP
Vendor remittance address on file

Reference Box
-------------
Document ID: D010
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 22/06/2024

Supplier Header
---------------
Supplier: Meridian Support LLP
Expense Category: Repairs Expense
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0003
Due Date: 22/06/2024
Subtotal: GBP 15,223.04
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 3,044.61
Total: GBP 18,267.65

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 28 | Unit Cost GBP 241.85 | 
Amount GBP 6,771.90
  - Description Preventive maintenance service parts | Quantity 10 | Unit Cost GBP 845.11 | 
Amount GBP 8,451.14

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D011 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-06

```
SUPPLIER INVOICE
================

From
----
Silverline Distribution
75 Market Road, Mumbai
Document Date: 06/06/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 22/06/2024

Supplier Header
---------------
Supplier: Pace Office Mart
Expense Category: Repairs Expense
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0004
Due Date: 22/06/2024
Subtotal: GBP 18,909.10
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 3,781.82
Total: GBP 22,690.92

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 26 | Unit Cost GBP 246.60 | 
Amount GBP 6,411.70
  - Description Preventive maintenance service parts | Quantity 17 | Unit Cost GBP 735.14 | 
Amount GBP 12,497.40

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D008 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-12

```
SUPPLIER INVOICE
================

From
----
Silverline Distribution
75 Market Road, Mumbai
Date: 12/06/2024

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D008
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 24/06/2024

Supplier Header
---------------
Supplier: Pace Office Mart
Expense Category: Repairs Expense
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0002
Due Date: 24/06/2024
Subtotal: GBP 17,293.78
Tax Label: VAT
Tax Rate: 20.00%
Tax Amount: GBP 3,458.76
Total: GBP 20,752.54

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 10 | Unit Cost GBP 732.35 | 
Amount GBP 7,323.49
  - Description Preventive maintenance service parts | Quantity 15 | Unit Cost GBP 664.69 | 
Amount GBP 9,970.29

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D004 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-06-29

```
SUPPLIER INVOICE
================

From
----
Silverline Distribution
75 Market Road, Mumbai
Document Date: 29/06/2024

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D004
Document Type: supplier_invoice
Period: FY 2024-25

Terms
-----
Due Date: 14/07/2024

Supplier Header
---------------
Supplier: Vertex Supply Co.
Expense Category: Repairs Expense
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 14/07/2024
Subtotal: GBP 23,485.63
Tax Label: VAT
Tax Rate: 10.00%
Tax Amount: GBP 2,348.56
Total: GBP 25,834.19

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 20 | Unit Cost GBP 418.60 | 
Amount GBP 8,371.95
  - Description Preventive maintenance service parts | Quantity 20 | Unit Cost GBP 755.68 | 
Amount GBP 15,113.68

Footer
------
Generated for synthetic accounting research use.
Page marker: D004
```

### Document D009 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-08-03

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0002
Merchant: Pace Office Mart
Total: GBP 387.27
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount GBP 100.73
  - Description Fuel Incidentals | Amount GBP 286.54
```

### Document D005 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2024-08-26

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Vertex Supply Co.
Total: GBP 904.27
Payment Method: Cash

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount GBP 350.71
  - Description Fuel Incidentals | Amount GBP 553.56
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-29

```
PAYMENT ADVICE
==============

From
----
Silverline Distribution
75 Market Road, Mumbai
Date: 29/12/2024

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: FY 2024-25
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Vertex Supply Co.
Amount: GBP 25,834.19
Reference: BILL-0001
Payment Method: ACH
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-01-09

```
PAYMENT ADVICE
==============

From
----
Silverline Distribution
75 Market Road, Mumbai
Date: 09/01/2025

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: FY 2024-25
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Blue Finch Holdings
Amount: GBP 43,517.71
Reference: INV-0001
Payment Method: Bank transfer
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D013 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
VENDOR STATEMENT
================

From
----
Silverline Distribution
75 Market Road, Mumbai
Date: 31/03/2025

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D013
Document Type: vendor_statement
Period: FY 2024-25

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Pace Office Mart
Closing Balance: GBP 43,443.46

Statement Lines
---------------
Lines:
  - Reference BILL-0002 | Document Type Open invoice | Amount GBP 20,752.54 | Status 
Outstanding
  - Reference BILL-0004 | Document Type Open invoice | Amount GBP 22,690.92 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Internal document packet copy.
Page marker: D013
```

### Document D015 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Silverline Distribution
75 Market Road, Mumbai
Date: 31/03/2025

Reference Box
-------------
Document ID: D015
Document Type: bank_statement
Period: FY 2024-25

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0026
Statement Currency: GBP
Opening Balance: GBP 162,683.48
Closing Balance: GBP 179,075.46

Statement Rows
--------------
Rows:
  - Date 03/08/2024 | Description Pace Office Mart receipt RCPT-0002 | Amount GBP -387.27 | 
Running Balance GBP 162,296.21
  - Date 26/08/2024 | Description Vertex Supply Co. receipt RCPT-0001 | Amount GBP -904.27 |
 Running Balance GBP 161,391.94
  - Date 29/12/2024 | Description Supplier settlement BILL-0001 | Amount GBP -25,834.19 | 
Running Balance GBP 135,557.75
  - Date 09/01/2025 | Description Customer settlement INV-0001 | Amount GBP 43,517.71 | 
Running Balance GBP 179,075.46

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D015
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 36,264.76 | D002, D003 | 2024-05-13 | job_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 7,252.95 | D002, D003 | 2024-05-13 | job_invoice_tax |
| 3 | Repairs Expense | Accounts Payable | 23,485.63 | D004 | 2024-06-29 | supplier_bill |
| 4 | Input Tax Receivable | Accounts Payable | 2,348.56 | D004 | 2024-06-29 | supplier_bill_tax |
| 5 | Fuel Expense | Cash | 904.27 | D005 | 2024-08-26 | fuel_receipt |
| 6 | Cash | Accounts Receivable | 43,517.71 | D006, D003 | 2025-01-09 | customer_payment |
| 7 | Accounts Payable | Cash | 25,834.19 | D007, D004 | 2024-12-29 | supplier_payment |
| 8 | Repairs Expense | Accounts Payable | 17,293.78 | D008 | 2024-06-12 | supplier_bill |
| 9 | Input Tax Receivable | Accounts Payable | 3,458.76 | D008 | 2024-06-12 | supplier_bill_tax |
| 10 | Fuel Expense | Cash | 387.27 | D009 | 2024-08-03 | fuel_receipt |
| 11 | Repairs Expense | Accounts Payable | 15,223.04 | D010 | 2024-06-03 | supplier_bill |
| 12 | Input Tax Receivable | Accounts Payable | 3,044.61 | D010 | 2024-06-03 | supplier_bill_tax |
| 13 | Repairs Expense | Accounts Payable | 18,909.10 | D011 | 2024-06-06 | supplier_bill |
| 14 | Input Tax Receivable | Accounts Payable | 3,781.82 | D011 | 2024-06-06 | supplier_bill_tax |
| 15 | Repairs Expense | Accounts Payable | 26,248.81 | D012 | 2024-04-19 | supplier_bill |
| 16 | Input Tax Receivable | Accounts Payable | 5,249.76 | D012 | 2024-04-19 | supplier_bill_tax |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 179,075.46
- Accounts Receivable: 16,900.64
- Office Supplies: 2,216.15
- Input Tax Receivable: 17,883.51

**Liabilities**
- Accounts Payable: 108,785.00
- Accrued Expenses: 5,538.15
- Sales Tax Payable: 7,252.95

**Equity**
- Retained Earnings: -28,553.02
- Owner's Equity: 123,052.68

**Totals:** Assets = 216,075.76; Liabilities = 121,576.10; Equity = 94,499.66
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
- Notes: Entries agree with the support.
