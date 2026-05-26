# Verification Packet — COV_WHO_Q4_0053

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `wholesale_distribution`
- **Difficulty level (1–5):** 4
- **Period type:** quarter
- **Period label:** Q1 FY 2025
- **Period start → end:** 2025-01-01 → 2025-03-31
- **Entity:** Northwind Advisors
- **Currency (display / functional):** GBP / GBP
- **Tax regime:** `india_gst`
- **Document count:** 24
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Inventory`, `Equipment`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Bad Debt Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2025-01-01_

**Assets**
- Cash: 87,380.49
- Inventory: 74,766.88
- Accounts Receivable: 9,846.00
- Office Supplies: 2,352.25
- Equipment: 22,416.85

**Liabilities**
- Accounts Payable: 12,770.49
- Accrued Expenses: 4,567.69
- Loans Payable: 16,932.71
- Notes Payable: 7,505.05

**Equity**
- Retained Earnings: 26,017.03
- Owner's Equity: 128,969.50


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
  - Section assets | Account Cash | Amount GBP 87,380.49
  - Section assets | Account Inventory | Amount GBP 74,766.88
  - Section assets | Account Accounts Receivable | Amount GBP 9,846.00
  - Section assets | Account Office Supplies | Amount GBP 2,352.25
  - Section assets | Account Equipment | Amount GBP 22,416.85
  - Section liabilities | Account Accounts Payable | Amount GBP 12,770.49
  - Section liabilities | Account Accrued Expenses | Amount GBP 4,567.69
  - Section liabilities | Account Loans Payable | Amount GBP 16,932.71
  - Section liabilities | Account Notes Payable | Amount GBP 7,505.05
  - Section equity | Account Retained Earnings | Amount GBP 26,017.03
  - Section equity | Account Owner's Equity | Amount GBP 128,969.50

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D015 — Tax Regime Notice

- **Type:** `tax_regime_notice`
- **Role:** `support_doc`
- **Date:** 2025-01-05

```
TAX REGIME NOTICE
=================

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Document Date: 05/01/2025

Reference Box
-------------
Document ID: D015
Document Type: tax_regime_notice
Period: Q1 FY 2025

Tax Rule
--------
Notice Number: TAX-0001
Tax Regime: india_gst
Company Jurisdiction: Karnataka
Counterparty Jurisdiction: Karnataka
Tax Rate: 12.00%
Jurisdiction Tax Amount: GBP 5,488.05
Treatment: India GST same-state CGST+SGST input credit

Footer
------
Generated for synthetic accounting research use.
Page marker: D015
```

### Document D016 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-05

```
SUPPLIER INVOICE
================

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Date: 05/01/2025

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D016
Document Type: supplier_invoice
Period: Q1 FY 2025

Terms
-----
Due Date: 19/01/2025

Supplier Header
---------------
Supplier: Beacon Industrial Supply
Goods Receipt Ref: GRN-TAX-0001
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: TAXSUP-0001
Due Date: 19/01/2025
Subtotal: GBP 45,733.78
Tax Label: India GST
Tax Rate: 12.00%
Tax Amount: GBP 5,488.05
CGST Amount: GBP 2,744.03
SGST Amount: GBP 2,744.02
Total: GBP 51,221.83

Supplier Bill Lines
-------------------
Lines:
  - Description Widget B | Quantity 1 | Unit Cost GBP 45,733.78 | Amount GBP 45,733.78

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D002 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2025-01-14

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0001
Supplier: Vertex Supply Co.
Purchase Ref: PO-0001
Total Quantity: GBP 43.00

Received Items
--------------
Items:
  - Sku SKU-0001 | Description Service Bundle | Quantity 43 | Unit Cost GBP 83.06
```

### Document D003 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-01-16

```
SUPPLIER INVOICE
================

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Date: 16/01/2025

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: supplier_invoice
Period: Q1 FY 2025

Terms
-----
Due Date: 03/02/2025

Supplier Header
---------------
Supplier: Vertex Supply Co.
Goods Receipt Ref: GRN-0001
Currency: GBP

Supplier Bill Details
---------------------
Invoice Number: SUP-0001
Due Date: 03/02/2025
Subtotal: GBP 3,571.58
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 642.88
CGST Amount: GBP 321.44
SGST Amount: GBP 321.44
Total: GBP 4,214.46

Supplier Bill Lines
-------------------
Lines:
  - Description Service Bundle | Quantity 43 | Unit Cost GBP 83.06 | Amount GBP 3,571.58

Footer
------
Internal document packet copy.
Page marker: D003
```

### Document D017 — Tax Exemption Certificate

- **Type:** `tax_exemption_certificate`
- **Role:** `support_doc`
- **Date:** 2025-02-10

```
TAX EXEMPTION CERTIFICATE
=========================

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Date: 10/02/2025

To
--
Crescent Labs

Reference Box
-------------
Document ID: D017
Document Type: tax_exemption_certificate
Period: Q1 FY 2025

Certificate
-----------
Certificate Number: EXEMPT-0001
Counterparty: Crescent Labs
Tax Regime: india_gst
Effective Date: 01/01/2025
Expiration Date: 31/03/2025
Exemption Status: Valid
Exempt Reason: Resale exemption certificate overrides default invoice tax treatment.

Footer
------
Internal document packet copy.
Page marker: D017
```

### Document D018 — Customer Tax Profile

- **Type:** `customer_tax_profile`
- **Role:** `support_doc`
- **Date:** 2025-02-10

```
CUSTOMER TAX PROFILE
====================

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Date: 10/02/2025

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D018
Document Type: customer_tax_profile
Period: Q1 FY 2025

Tax Profile
-----------
Profile ID: TAXPROF-0001
Customer: Crescent Labs
Customer Jurisdiction: Karnataka
Company Jurisdiction: Karnataka
Same State: True
Exemption Certificate: EXEMPT-0001

Footer
------
Internal document packet copy.
Page marker: D018
```

### Document D019 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-10

```
CUSTOMER INVOICE
================

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Document Date: 10/02/2025

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D019
Document Type: customer_invoice
Period: Q1 FY 2025
Shipment Ref: SHP-0002

Terms
-----
Due Date: 26/02/2025

Parties
-------
Customer: Crescent Labs
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 26/02/2025
Subtotal: GBP 62,605.26
Tax Label: India GST
Tax Rate: 0.00%
Tax Amount: GBP 0.00
Exemption Certificate: EXEMPT-0001
Total: GBP 62,605.26

Line Items
----------
Items:
  - Description Widget B | Amount GBP 62,605.26

Shipment Link
-------------
Shipment Ref: SHP-0002

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D004 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2025-02-20

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0001
Customer: Riverfront Group
Shipment Ref: SHP-0001
Billed Amount: GBP 9,737.90
Cost Basis Amount: GBP 5,779.81
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0002 | Description Widget A | Quantity 38 | Unit Price GBP 217.17 | Unit Cost 
GBP 152.10 | Extended Cost GBP 5,779.81
```

### Document D005 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-02-20

```
CUSTOMER INVOICE
================

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Document Date: 20/02/2025

To
--
Riverfront Group
Customer account on file

Reference Box
-------------
Document ID: D005
Document Type: customer_invoice
Period: Q1 FY 2025
Shipment Ref: SHP-0001

Terms
-----
Due Date: 04/03/2025

Parties
-------
Customer: Riverfront Group
Currency: GBP

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 04/03/2025
Subtotal: GBP 8,252.46
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: GBP 1,485.44
CGST Amount: GBP 742.72
SGST Amount: GBP 742.72
Total: GBP 9,737.90

Line Items
----------
Items:
  - Description Widget A | Amount GBP 8,252.46

Shipment Link
-------------
Shipment Ref: SHP-0001

Footer
------
Generated for synthetic accounting research use.
Page marker: D005
```

### Document D012 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2025-02-27

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: First City Bank
Opening Principal: GBP 19,554.70
Draw Amount: GBP 83,227.34
Principal Paid: GBP 0.00
Interest Paid: GBP 0.00
Ending Principal: GBP 102,782.04
Note: Scheduled lender activity for the selected period.
```

### Document D013 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2025-03-02

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Oakline Services
Asset Name: Office laptops
Asset Tag: TAG-0001
Useful Life Months: 36
Total: GBP 67,802.93
Paid Cash: GBP 16,429.75
Financed Amount: GBP 51,373.18
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-03-04

```
PAYMENT ADVICE
==============

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Date: 04/03/2025

To
--
Riverfront Group

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: Q1 FY 2025
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Riverfront Group
Amount: GBP 8,782.41
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D011 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2025-03-06

```
UTILITY INVOICE
===============

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Document Date: 06/03/2025

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: utilities_statement
Period: Q1 FY 2025

Terms
-----
Due Date: 14/03/2025

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: Q1 FY 2025
Due Date: 14/03/2025
Total: GBP 3,572.39

Charges
-------
Charges:
  - Description Electricity | Amount GBP 1,118.31
  - Description Water | Amount GBP 2,454.08

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2025-03-08

```
PAYMENT ADVICE
==============

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Date: 08/03/2025

To
--
Vertex Supply Co.

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: Q1 FY 2025
Reference: SUP-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Vertex Supply Co.
Amount: GBP 2,374.42
Reference: SUP-0001
Payment Method: Wire
Payment For: Supplier settlement

Footer
------
Internal document packet copy.
Page marker: D007
```

### Document D010 — Payroll Summary

- **Type:** `payroll_summary`
- **Role:** `posting_doc`
- **Date:** 2025-03-14

```
PAYROLL SUMMARY
===============

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Document Date: 14/03/2025

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: Payroll for Q1 FY 2025
Headcount: 10
Gross Pay: GBP 38,359.26
Employer Tax: 3,448.65
Cash Outflow: GBP 41,807.91

Footer
------
Generated for synthetic accounting research use.
Page marker: D010
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0001
Location: Back room

Counted Items
-------------
Items:
  - Sku SKU-0003 | Description Refill Pack | System Qty 100 | Counted Qty 90 | Unit Cost GBP
 31.83
```

### Document D009 — Inventory Adjustment Note

- **Type:** `inventory_adjustment_note`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
INVENTORY ADJUSTMENT NOTE
=========================

Adjustment Summary
------------------
Note ID: ADJ-0001
Reason: Shrinkage found during physical count
Amount: GBP 318.30
Reference Sheet: COUNT-0001
```

### Document D014 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: GBP 22,416.85
Useful Life Months: 48
Current Period Charge: GBP 1,401.06
Accumulated Depreciation: 1,401.06
```

### Document D020 — AR Aging Summary

- **Type:** `ar_aging_summary`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
AR AGING SUMMARY
================

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Document Date: 31/03/2025

Reference Box
-------------
Document ID: D020
Document Type: ar_aging_summary
Period: Q1 FY 2025

Aging Summary
-------------
Summary ID: AGING-0001
Period: Q1 FY 2025
Total Open: GBP 955.49

Customer Lines
--------------
Lines:
  - Customer Riverfront Group | Reference INV-0001 | Current GBP 669.87 | Past Due 285.62

Notes
-----
Accounts receivable review prepared for collectability assessment.

Footer
------
Generated for synthetic accounting research use.
Page marker: D020
```

### Document D021 — Credit Memo

- **Type:** `credit_memo`
- **Role:** `adjustment_doc`
- **Date:** 2025-03-31

```
CREDIT MEMO
===========

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Date: 31/03/2025

To
--
Riverfront Group

Reference Box
-------------
Document ID: D021
Document Type: credit_memo
Period: Q1 FY 2025
Reference: INV-0001

Approval / Context
------------------
Reason: Bad debt writeoff approved after aging review

Credit Memo
-----------
Memo Number: CM-0001
Counterparty: Riverfront Group
Reference: INV-0001
Reason: Bad debt writeoff approved after aging review
Amount: GBP 285.62

Footer
------
Internal document packet copy.
Page marker: D021
```

### Document D022 — Vendor Statement

- **Type:** `vendor_statement`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
VENDOR STATEMENT
================

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Date: 31/03/2025

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D022
Document Type: vendor_statement
Period: Q1 FY 2025

Statement Header
----------------
Statement Number: VSTMT-0001
Vendor: Beacon Industrial Supply
Closing Balance: GBP 51,221.83

Statement Lines
---------------
Lines:
  - Reference TAXSUP-0001 | Document Type Open invoice | Amount GBP 51,221.83 | Status 
Outstanding

Notes
-----
Period-end statement received from the vendor billing desk.

Footer
------
Internal document packet copy.
Page marker: D022
```

### Document D023 — Memo

- **Type:** `memo`
- **Role:** `distractor_doc`
- **Date:** 2025-03-31

```
MEMO
====

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Document Date: 31/03/2025

Reference Box
-------------
Document ID: D023
Document Type: memo
Period: Q1 FY 2025

Approval / Context
------------------
Subject: Scanning checklist for back-office staff

Memo Summary
------------
Memo ID: INFO-0001
Subject: Scanning checklist for back-office staff
Audience: All Staff

Memo Body
---------
Narrative: The packet may include supporting correspondence gathered during the close 
review.

Notes
-----
Administrative note included in the scanned packet.

Footer
------
Generated for synthetic accounting research use.
Page marker: D023
```

### Document D024 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2025-03-31

```
BANK STATEMENT
==============

From
----
Northwind Advisors
90 Hill Park, Hyderabad
Document Date: 31/03/2025

Reference Box
-------------
Document ID: D024
Document Type: bank_statement
Period: Q1 FY 2025

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0053
Statement Currency: GBP
Opening Balance: GBP 87,380.49
Closing Balance: GBP 118,778.16

Statement Rows
--------------
Rows:
  - Date 27/02/2025 | Description Loan draw LOAN-0001 | Amount GBP 83,227.34 | Running 
Balance GBP 170,607.83
  - Date 02/03/2025 | Description Asset purchase ASSET-0001 | Amount GBP -16,429.75 | 
Running Balance GBP 154,178.08
  - Date 04/03/2025 | Description Customer settlement INV-0001 | Amount GBP 8,782.41 | 
Running Balance GBP 162,960.49
  - Date 08/03/2025 | Description Supplier settlement SUP-0001 | Amount GBP -2,374.42 | 
Running Balance GBP 160,586.07
  - Date 14/03/2025 | Description Payroll PAYRUN-0001 | Amount GBP -41,807.91 | Running 
Balance GBP 118,778.16

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Generated for synthetic accounting research use.
Page marker: D024
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 3,571.58 | D002, D003 | 2025-01-16 | goods_receipt_purchase |
| 2 | Input CGST Receivable | Accounts Payable | 321.44 | D002, D003 | 2025-01-16 | goods_receipt_purchase_tax_cgst |
| 3 | Input SGST Receivable | Accounts Payable | 321.44 | D002, D003 | 2025-01-16 | goods_receipt_purchase_tax_sgst |
| 4 | Accounts Receivable | Sales Revenue | 8,252.46 | D004, D005 | 2025-02-20 | delivery_sale_sale |
| 5 | Cost of Goods Sold | Inventory | 5,779.81 | D004, D005 | 2025-02-20 | delivery_sale_cogs |
| 6 | Accounts Receivable | CGST Payable | 742.72 | D004, D005 | 2025-02-20 | delivery_sale_tax_cgst |
| 7 | Accounts Receivable | SGST Payable | 742.72 | D004, D005 | 2025-02-20 | delivery_sale_tax_sgst |
| 8 | Cash | Accounts Receivable | 8,782.41 | D006, D005 | 2025-03-04 | customer_payment |
| 9 | Accounts Payable | Cash | 2,374.42 | D007, D003 | 2025-03-08 | supplier_payment |
| 10 | Inventory Shrinkage Expense | Inventory | 318.30 | D008, D009 | 2025-03-31 | inventory_adjustment |
| 11 | Salaries Expense | Cash | 38,359.26 | D010 | 2025-03-14 | payroll_gross |
| 12 | Payroll Tax Expense | Cash | 3,448.65 | D010 | 2025-03-14 | payroll_tax |
| 13 | Utilities Expense | Accounts Payable | 3,572.39 | D011 | 2025-03-06 | utilities_bill |
| 14 | Cash | Loans Payable | 83,227.34 | D012 | 2025-02-27 | loan_draw |
| 15 | Equipment | Cash | 16,429.75 | D013 | 2025-03-02 | equipment_purchase_cash |
| 16 | Equipment | Notes Payable | 51,373.18 | D013 | 2025-03-02 | equipment_purchase_financed |
| 17 | Depreciation Expense | Accumulated Depreciation | 1,401.06 | D014 | 2025-03-31 | depreciation |
| 18 | Inventory | Accounts Payable | 45,733.78 | D015, D016 | 2025-01-05 | jurisdictional_tax_invoice_purchase_inventory |
| 19 | Input CGST Receivable | Accounts Payable | 2,744.03 | D015, D016 | 2025-01-05 | jurisdictional_tax_invoice_input_cgst |
| 20 | Input SGST Receivable | Accounts Payable | 2,744.02 | D015, D016 | 2025-01-05 | jurisdictional_tax_invoice_input_sgst |
| 21 | Accounts Receivable | Sales Revenue | 62,605.26 | D017, D018, D019 | 2025-02-10 | jurisdictional_tax_invoice_exempt_sale |
| 22 | Bad Debt Expense | Accounts Receivable | 285.62 | D020, D021, D005 | 2025-03-31 | bad_debt_review |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 118,778.16
- Inventory: 117,974.13
- Accounts Receivable: 73,121.13
- Office Supplies: 2,352.25
- Equipment: 90,219.78
- Input CGST Receivable: 3,065.47
- Input SGST Receivable: 3,065.46
- Accumulated Depreciation: -1,401.06

**Liabilities**
- Accounts Payable: 69,404.75
- Accrued Expenses: 4,567.69
- Loans Payable: 100,160.05
- Notes Payable: 58,878.23
- CGST Payable: 742.72
- SGST Payable: 742.72

**Equity**
- Retained Earnings: 43,709.66
- Owner's Equity: 128,969.50

**Totals:** Assets = 407,175.32; Liabilities = 234,496.16; Equity = 172,679.16
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
