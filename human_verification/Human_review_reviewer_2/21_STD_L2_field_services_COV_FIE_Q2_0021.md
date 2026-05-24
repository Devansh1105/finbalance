# Verification Packet — COV_FIE_Q2_0021

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `field_services`
- **Difficulty level (1–5):** 2
- **Period type:** quarter
- **Period label:** Q3 FY 2025-26
- **Period start → end:** 2025-10-01 → 2025-12-31
- **Entity:** Cedar Manufacturing
- **Currency (display / functional):** USD / USD
- **Tax regime:** `gst`
- **Document count:** 10
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Office Supplies`, `Prepaid Insurance`, `Equipment`, `Vehicles`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Repairs Expense`, `Fuel Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-10-01_

**Assets**
- Cash: 37,005.13
- Accounts Receivable: 5,916.95
- Office Supplies: 1,244.59

**Liabilities**
- Accounts Payable: 3,006.33
- Accrued Expenses: 3,442.81

**Equity**
- Retained Earnings: 7,211.04
- Owner's Equity: 30,506.49


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
  - Section assets | Account Cash | Amount $37,005.13
  - Section assets | Account Accounts Receivable | Amount $5,916.95
  - Section assets | Account Office Supplies | Amount $1,244.59
  - Section liabilities | Account Accounts Payable | Amount $3,006.33
  - Section liabilities | Account Accrued Expenses | Amount $3,442.81
  - Section equity | Account Retained Earnings | Amount $7,211.04
  - Section equity | Account Owner's Equity | Amount $30,506.49

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2025-10-05

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0001
Customer: Aster Point Services
Job Site: East Tower
Scope: Support package
Approved Amount: $19,143.63

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-06

```
CUSTOMER INVOICE
================

From
----
Cedar Manufacturing
14 King Street, Pune
Document Date: 2025-10-06

To
--
Aster Point Services
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: Q3 FY 2025-26
Contract Ref: CTR-0001
Job Code: JOB-0001

Terms
-----
Due Date: 2025-10-24

Parties
-------
Customer: Aster Point Services
Contract Ref: CTR-0001
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2025-10-24
Subtotal: $19,143.63
Tax Label: GST
Tax Rate: 7.00%
Tax Amount: $1,340.05
Total: $20,483.68

Line Items
----------
Items:
  - Description Review pack | Amount $5,893.38
  - Description Follow-up support | Amount $13,250.25

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
- **Date:** 2025-10-11

```
SUPPLIER INVOICE
================

From
----
Cedar Manufacturing
14 King Street, Pune
Date: 2025-10-11

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D004
Document Type: supplier_invoice
Period: Q3 FY 2025-26

Terms
-----
Due Date: 2025-10-26

Supplier Header
---------------
Supplier: Vertex Supply Co.
Expense Category: Repairs Expense
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 2025-10-26
Subtotal: $14,674.11
Tax Label: GST
Tax Rate: 5.00%
Tax Amount: $733.71
Total: $15,407.82

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 12 | Unit Cost $255.53 | Amount 
$3,066.41
  - Description Preventive maintenance service parts | Quantity 21 | Unit Cost $552.75 | 
Amount $11,607.70

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D008 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-10-16

```
SUPPLIER INVOICE
================

From
----
Cedar Manufacturing
14 King Street, Pune
Date: 2025-10-16

To
--
Pace Office Mart
Vendor remittance address on file

Reference Box
-------------
Document ID: D008
Document Type: supplier_invoice
Period: Q3 FY 2025-26

Terms
-----
Due Date: 2025-11-05

Supplier Header
---------------
Supplier: Pace Office Mart
Expense Category: Repairs Expense
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: BILL-0002
Due Date: 2025-11-05
Subtotal: $2,373.90
Tax Label: GST
Tax Rate: 10.00%
Tax Amount: $237.39
Total: $2,611.29

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 25 | Unit Cost $42.38 | Amount 
$1,059.48
  - Description Preventive maintenance service parts | Quantity 19 | Unit Cost $69.18 | 
Amount $1,314.42

Footer
------
Internal document packet copy.
Page marker: D008
```

### Document D005 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-11-09

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Golden State Finance
Total: $25.23
Payment Method: Company card

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount $10.39
  - Description Fuel Incidentals | Amount $14.84
```

### Document D009 — Expense Receipt

- **Type:** `expense_receipt`
- **Role:** `posting_doc`
- **Date:** 2025-12-01

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0002
Merchant: Oakline Services
Total: $340.97
Payment Method: Company card

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount $124.75
  - Description Fuel Incidentals | Amount $216.22
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-12-12

```
PAYMENT ADVICE
==============

From
----
Cedar Manufacturing
14 King Street, Pune
Date: 2025-12-12

To
--
Aster Point Services

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q3 FY 2025-26
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Aster Point Services
Amount: $20,483.68
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
- **Date:** 2025-12-12

```
PAYMENT ADVICE
==============

From
----
Cedar Manufacturing
14 King Street, Pune
Document Date: 2025-12-12

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: Q3 FY 2025-26
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Vertex Supply Co.
Amount: $15,407.82
Reference: BILL-0001
Payment Method: Bank transfer
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D010 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-12-31

```
BANK STATEMENT
==============

From
----
Cedar Manufacturing
14 King Street, Pune
Date: 2025-12-31

Reference Box
-------------
Document ID: D010
Document Type: bank_statement
Period: Q3 FY 2025-26

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0021
Statement Currency: USD
Opening Balance: $37,005.13
Closing Balance: $41,714.79

Statement Rows
--------------
Rows:
  - Date 2025-11-09 | Description Golden State Finance receipt RCPT-0001 | Amount $-25.23 | 
Running Balance $36,979.90
  - Date 2025-12-01 | Description Oakline Services receipt RCPT-0002 | Amount $-340.97 | 
Running Balance $36,638.93
  - Date 2025-12-12 | Description Customer settlement INV-0001 | Amount $20,483.68 | Running
 Balance $57,122.61
  - Date 2025-12-12 | Description Supplier settlement BILL-0001 | Amount $-15,407.82 | 
Running Balance $41,714.79

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
| 1 | Accounts Receivable | Service Revenue | 19,143.63 | D002, D003 | 2025-10-06 | job_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 1,340.05 | D002, D003 | 2025-10-06 | job_invoice_tax |
| 3 | Repairs Expense | Accounts Payable | 14,674.11 | D004 | 2025-10-11 | supplier_bill |
| 4 | Input Tax Receivable | Accounts Payable | 733.71 | D004 | 2025-10-11 | supplier_bill_tax |
| 5 | Fuel Expense | Cash | 25.23 | D005 | 2025-11-09 | fuel_receipt |
| 6 | Cash | Accounts Receivable | 20,483.68 | D006, D003 | 2025-12-12 | customer_payment |
| 7 | Accounts Payable | Cash | 15,407.82 | D007, D004 | 2025-12-12 | supplier_payment |
| 8 | Repairs Expense | Accounts Payable | 2,373.90 | D008 | 2025-10-16 | supplier_bill |
| 9 | Input Tax Receivable | Accounts Payable | 237.39 | D008 | 2025-10-16 | supplier_bill_tax |
| 10 | Fuel Expense | Cash | 340.97 | D009 | 2025-12-01 | fuel_receipt |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 41,714.79
- Accounts Receivable: 5,916.95
- Office Supplies: 1,244.59
- Input Tax Receivable: 971.10

**Liabilities**
- Accounts Payable: 5,617.62
- Accrued Expenses: 3,442.81
- Sales Tax Payable: 1,340.05

**Equity**
- Retained Earnings: 8,940.46
- Owner's Equity: 30,506.49

**Totals:** Assets = 49,847.43; Liabilities = 10,400.48; Equity = 39,446.95
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
