# Verification Packet — COV_FIE_M2_0016

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `field_services`
- **Difficulty level (1–5):** 2
- **Period type:** month
- **Period label:** December 2024
- **Period start → end:** 2024-12-01 → 2024-12-31
- **Entity:** Summit Advisors
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `us_sales_tax`
- **Document count:** 8
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Office Supplies`, `Prepaid Insurance`, `Equipment`, `Vehicles`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Service Revenue`, `Repairs Expense`, `Fuel Expense`, `Utilities Expense`, `Insurance Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-12-01_

**Assets**
- Cash: 34,017.15
- Accounts Receivable: 7,461.55
- Office Supplies: 1,525.45

**Liabilities**
- Accounts Payable: 4,764.25
- Accrued Expenses: 1,481.37

**Equity**
- Retained Earnings: 3,290.35
- Owner's Equity: 33,468.18


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-12-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 01/12/2024
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount EUR 34.017,15
  - Section assets | Account Accounts Receivable | Amount EUR 7.461,55
  - Section assets | Account Office Supplies | Amount EUR 1.525,45
  - Section liabilities | Account Accounts Payable | Amount EUR 4.764,25
  - Section liabilities | Account Accrued Expenses | Amount EUR 1.481,37
  - Section equity | Account Retained Earnings | Amount EUR 3.290,35
  - Section equity | Account Owner's Equity | Amount EUR 33.468,18

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D004 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-12-05

```
SUPPLIER INVOICE
================

From
----
Summit Advisors
220 Lake View Road, Bengaluru
Date: 05/12/2024

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D004
Document Type: supplier_invoice
Period: December 2024

Terms
-----
Due Date: 17/12/2024

Supplier Header
---------------
Supplier: Beacon Industrial Supply
Expense Category: Repairs Expense
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: BILL-0001
Due Date: 17/12/2024
Subtotal: EUR 4.947,28
Tax Label: US Sales Tax
Tax Rate: 7.25%
Tax Amount: EUR 358,68
Total: EUR 5.305,96

Supplier Bill Lines
-------------------
Lines:
  - Description Repair parts for field equipment | Quantity 8 | Unit Cost EUR 135,38 | 
Amount EUR 1.083,00
  - Description Preventive maintenance service parts | Quantity 16 | Unit Cost EUR 241,52 | 
Amount EUR 3.864,28

Footer
------
Internal document packet copy.
Page marker: D004
```

### Document D002 — Work Order

- **Type:** `work_order`
- **Role:** `support_doc`
- **Date:** 2024-12-06

```
WORK ORDER
==========

Work Order Details
------------------
Work Order Number: WO-0001
Customer: Blue Finch Holdings
Job Site: East Tower
Scope: Consulting sprint
Approved Amount: EUR 3.181,54

Notes
-----
Approved job scope supporting the related invoice.
```

### Document D003 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-12-07

```
CUSTOMER INVOICE
================

From
----
Summit Advisors
220 Lake View Road, Bengaluru
Date: 07/12/2024

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D003
Document Type: customer_invoice
Period: December 2024
Contract Ref: CTR-0001
Job Code: JOB-0001

Terms
-----
Due Date: 17/12/2024

Parties
-------
Customer: Blue Finch Holdings
Contract Ref: CTR-0001
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 17/12/2024
Subtotal: EUR 3.181,54
Tax Label: US Sales Tax
Tax Rate: 8.25%
Tax Amount: EUR 262,48
Total: EUR 3.444,02

Line Items
----------
Items:
  - Description Implementation work | Amount EUR 1.326,79
  - Description Follow-up support | Amount EUR 1.854,75

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
- **Date:** 2024-12-13

```
EXPENSE RECEIPT
===============

Receipt Details
---------------
Receipt Number: RCPT-0001
Merchant: Vertex Supply Co.
Total: EUR 100,01
Payment Method: Debit card

Receipt Lines
-------------
Lines:
  - Description Fuel Expense | Amount EUR 37,97
  - Description Fuel Incidentals | Amount EUR 62,04
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-25

```
PAYMENT ADVICE
==============

From
----
Summit Advisors
220 Lake View Road, Bengaluru
Date: 25/12/2024

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: December 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Blue Finch Holdings
Amount: EUR 3.444,02
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-12-26

```
PAYMENT ADVICE
==============

From
----
Summit Advisors
220 Lake View Road, Bengaluru
Document Date: 26/12/2024

To
--
Beacon Industrial Supply

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: December 2024
Reference: BILL-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Beacon Industrial Supply
Amount: EUR 5.305,96
Reference: BILL-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D007
```

### Document D008 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-12-31

```
BANK STATEMENT
==============

From
----
Summit Advisors
220 Lake View Road, Bengaluru
Date: 31/12/2024

Reference Box
-------------
Document ID: D008
Document Type: bank_statement
Period: December 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0016
Statement Currency: EUR
Opening Balance: EUR 34.017,15
Closing Balance: EUR 32.055,20

Statement Rows
--------------
Rows:
  - Date 13/12/2024 | Description Vertex Supply Co. receipt RCPT-0001 | Amount EUR -100,01 |
 Running Balance EUR 33.917,14
  - Date 25/12/2024 | Description Customer settlement INV-0001 | Amount EUR 3.444,02 | 
Running Balance EUR 37.361,16
  - Date 26/12/2024 | Description Supplier settlement BILL-0001 | Amount EUR -5.305,96 | 
Running Balance EUR 32.055,20

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D008
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Accounts Receivable | Service Revenue | 3,181.54 | D002, D003 | 2024-12-07 | job_invoice |
| 2 | Accounts Receivable | Sales Tax Payable | 262.48 | D002, D003 | 2024-12-07 | job_invoice_tax |
| 3 | Repairs Expense | Accounts Payable | 4,947.28 | D004 | 2024-12-05 | supplier_bill |
| 4 | Input Tax Receivable | Accounts Payable | 358.68 | D004 | 2024-12-05 | supplier_bill_tax |
| 5 | Fuel Expense | Cash | 100.01 | D005 | 2024-12-13 | fuel_receipt |
| 6 | Cash | Accounts Receivable | 3,444.02 | D006, D003 | 2024-12-25 | customer_payment |
| 7 | Accounts Payable | Cash | 5,305.96 | D007, D004 | 2024-12-26 | supplier_payment |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 32,055.20
- Accounts Receivable: 7,461.55
- Office Supplies: 1,525.45
- Input Tax Receivable: 358.68

**Liabilities**
- Accounts Payable: 4,764.25
- Accrued Expenses: 1,481.37
- Sales Tax Payable: 262.48

**Equity**
- Retained Earnings: 1,424.60
- Owner's Equity: 33,468.18

**Totals:** Assets = 41,400.88; Liabilities = 6,508.10; Equity = 34,892.78
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
