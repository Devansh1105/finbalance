# Verification Packet — COV_WHO_M5_0049

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `wholesale_distribution`
- **Difficulty level (1–5):** 5
- **Period type:** month
- **Period label:** November 2024
- **Period start → end:** 2024-11-01 → 2024-11-30
- **Entity:** Northwind Operations
- **Currency (display / functional):** EUR / EUR
- **Tax regime:** `sales_tax`
- **Document count:** 21
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Inventory`, `Equipment`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Bad Debt Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-11-01_

**Assets**
- Cash: 67,488.25
- Inventory: 48,002.77
- Accounts Receivable: 8,009.98
- Office Supplies: 1,456.08
- Equipment: 9,539.90

**Liabilities**
- Accounts Payable: 11,790.56
- Accrued Expenses: 3,310.25
- Loans Payable: 8,453.45

**Equity**
- Retained Earnings: 12,026.08
- Owner's Equity: 98,916.64


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
  - Section assets | Account Cash | Amount EUR 67.488,25
  - Section assets | Account Inventory | Amount EUR 48.002,77
  - Section assets | Account Accounts Receivable | Amount EUR 8.009,98
  - Section assets | Account Office Supplies | Amount EUR 1.456,08
  - Section assets | Account Equipment | Amount EUR 9.539,90
  - Section liabilities | Account Accounts Payable | Amount EUR 11.790,56
  - Section liabilities | Account Accrued Expenses | Amount EUR 3.310,25
  - Section liabilities | Account Loans Payable | Amount EUR 8.453,45
  - Section equity | Account Retained Earnings | Amount EUR 12.026,08
  - Section equity | Account Owner's Equity | Amount EUR 98.916,64

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D002 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2024-11-08

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0001
Supplier: Oakline Services
Purchase Ref: PO-0001
Total Quantity: EUR 83,00

Received Items
--------------
Items:
  - Sku SKU-0001 | Description Refill Pack | Quantity 83 | Unit Cost EUR 31,90
```

### Document D015 — Tax Regime Notice

- **Type:** `tax_regime_notice`
- **Role:** `support_doc`
- **Date:** 2024-11-08

```
TAX REGIME NOTICE
=================

From
----
Northwind Operations
75 Market Road, Mumbai
Date: 08/11/2024

Reference Box
-------------
Document ID: D015
Document Type: tax_regime_notice
Period: November 2024

Tax Rule
--------
Notice Number: TAX-0001
Tax Regime: india_gst
Company Jurisdiction: Maharashtra
Counterparty Jurisdiction: Maharashtra
Tax Rate: 18.00%
Jurisdiction Tax Amount: EUR 2.121,29
Treatment: India GST same-state CGST+SGST input credit

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D016 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-08

```
SUPPLIER INVOICE
================

From
----
Northwind Operations
75 Market Road, Mumbai
Date: 08/11/2024

To
--
Vertex Supply Co.
Vendor remittance address on file

Reference Box
-------------
Document ID: D016
Document Type: supplier_invoice
Period: November 2024

Terms
-----
Due Date: 28/11/2024

Supplier Header
---------------
Supplier: Vertex Supply Co.
Goods Receipt Ref: GRN-TAX-0001
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: TAXSUP-0001
Due Date: 28/11/2024
Subtotal: EUR 11.784,96
Tax Label: India GST
Tax Rate: 18.00%
Tax Amount: EUR 2.121,29
CGST Amount: EUR 1.060,64
SGST Amount: EUR 1.060,65
Total: EUR 13.906,25

Supplier Bill Lines
-------------------
Lines:
  - Description Service Bundle | Quantity 1 | Unit Cost EUR 11.784,96 | Amount EUR 11.784,96

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D003 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-10

```
SUPPLIER INVOICE
================

From
----
Northwind Operations
75 Market Road, Mumbai
Document Date: 10/11/2024

To
--
Oakline Services
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: supplier_invoice
Period: November 2024

Terms
-----
Due Date: 25/11/2024

Supplier Header
---------------
Supplier: Oakline Services
Goods Receipt Ref: GRN-0001
Currency: EUR

Supplier Bill Details
---------------------
Invoice Number: SUP-0001
Due Date: 25/11/2024
Subtotal: EUR 2.647,70
Tax Label: Sales Tax
Tax Rate: 7.25%
Tax Amount: EUR 191,96
Total: EUR 2.839,66

Supplier Bill Lines
-------------------
Lines:
  - Description Refill Pack | Quantity 83 | Unit Cost EUR 31,90 | Amount EUR 2.647,70

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D017 — Tax Exemption Certificate

- **Type:** `tax_exemption_certificate`
- **Role:** `support_doc`
- **Date:** 2024-11-10

```
TAX EXEMPTION CERTIFICATE
=========================

From
----
Northwind Operations
75 Market Road, Mumbai
Date: 10/11/2024

To
--
Crescent Labs

Reference Box
-------------
Document ID: D017
Document Type: tax_exemption_certificate
Period: November 2024

Certificate
-----------
Certificate Number: EXEMPT-0001
Counterparty: Crescent Labs
Tax Regime: india_gst
Effective Date: 01/11/2024
Expiration Date: 30/11/2024
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
- **Date:** 2024-11-10

```
CUSTOMER TAX PROFILE
====================

From
----
Northwind Operations
75 Market Road, Mumbai
Date: 10/11/2024

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D018
Document Type: customer_tax_profile
Period: November 2024

Tax Profile
-----------
Profile ID: TAXPROF-0001
Customer: Crescent Labs
Customer Jurisdiction: Maharashtra
Company Jurisdiction: Maharashtra
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
- **Date:** 2024-11-10

```
CUSTOMER INVOICE
================

From
----
Northwind Operations
75 Market Road, Mumbai
Document Date: 10/11/2024

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D019
Document Type: customer_invoice
Period: November 2024
Shipment Ref: SHP-0002

Terms
-----
Due Date: 25/11/2024

Parties
-------
Customer: Crescent Labs
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 25/11/2024
Subtotal: EUR 14.614,22
Tax Label: India GST
Tax Rate: 0.00%
Tax Amount: EUR 0,00
Exemption Certificate: EXEMPT-0001
Total: EUR 14.614,22

Line Items
----------
Items:
  - Description Premium Kit | Amount EUR 14.614,22

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
- **Date:** 2024-11-14

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0001
Customer: Crescent Labs
Shipment Ref: SHP-0001
Billed Amount: EUR 2.962,92
Cost Basis Amount: EUR 1.974,56
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0002 | Description Filter Pack | Quantity 17 | Unit Price EUR 165,99 | Unit Cost
 EUR 116,15 | Extended Cost EUR 1.974,56
```

### Document D005 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-14

```
CUSTOMER INVOICE
================

From
----
Northwind Operations
75 Market Road, Mumbai
Document Date: 14/11/2024

To
--
Crescent Labs
Customer account on file

Reference Box
-------------
Document ID: D005
Document Type: customer_invoice
Period: November 2024
Shipment Ref: SHP-0001

Terms
-----
Due Date: 26/11/2024

Parties
-------
Customer: Crescent Labs
Currency: EUR

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 26/11/2024
Subtotal: EUR 2.821,83
Tax Label: Sales Tax
Tax Rate: 5.00%
Tax Amount: EUR 141,09
Total: EUR 2.962,92

Line Items
----------
Items:
  - Description Filter Pack | Amount EUR 2.821,83

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
- **Date:** 2024-11-17

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Stonebridge Finance
Opening Principal: EUR 1.063,95
Draw Amount: EUR 53.333,22
Principal Paid: EUR 0,00
Interest Paid: EUR 0,00
Ending Principal: EUR 54.397,17
Note: Scheduled lender activity for the selected period.
```

### Document D013 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-11-18

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Golden State Finance
Asset Name: CNC router
Asset Tag: TAG-0001
Useful Life Months: 36
Total: EUR 85.850,93
Paid Cash: EUR 22.794,99
Financed Amount: EUR 63.055,94
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-11-21

```
PAYMENT ADVICE
==============

From
----
Northwind Operations
75 Market Road, Mumbai
Document Date: 21/11/2024

To
--
Crescent Labs

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: November 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Crescent Labs
Amount: EUR 2.345,84
Reference: INV-0001
Payment Method: Wire
Payment For: Customer settlement

Footer
------
Generated for synthetic accounting research use.
Page marker: D006
```

### Document D020 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-11-21

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0002
Lender: Stonebridge Finance
Opening Principal: EUR 71.621,37
Draw Amount: EUR 0,00
Principal Paid: EUR 14.105,48
Interest Paid: EUR 1.140,85
Ending Principal: EUR 57.515,89
Note: Scheduled lender activity for the selected period.
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-11-24

```
PAYMENT ADVICE
==============

From
----
Northwind Operations
75 Market Road, Mumbai
Date: 24/11/2024

To
--
Oakline Services

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: November 2024
Reference: SUP-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Oakline Services
Amount: EUR 2.118,79
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
- **Date:** 2024-11-27

```
PAYROLL SUMMARY
===============

From
----
Northwind Operations
75 Market Road, Mumbai
Date: 27/11/2024

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: November 2024
Headcount: 8
Gross Pay: EUR 24.515,84
Employer Tax: 3.220,42
Cash Outflow: EUR 27.736,26

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D011 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-11-27

```
UTILITY INVOICE
===============

From
----
Northwind Operations
75 Market Road, Mumbai
Date: 27/11/2024

To
--
Harbor Utilities
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: utilities_statement
Period: November 2024

Terms
-----
Due Date: 07/12/2024

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Harbor Utilities
Pay To: Harbor Utilities
Service Period: November 2024
Due Date: 07/12/2024
Total: EUR 2.394,93

Charges
-------
Charges:
  - Description Electricity | Amount EUR 878,03
  - Description Water | Amount EUR 1.516,90

Footer
------
Internal document packet copy.
Page marker: D011
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2024-11-30

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0001
Location: Front store

Counted Items
-------------
Items:
  - Sku SKU-0003 | Description Service Bundle | System Qty 100 | Counted Qty 93 | Unit Cost 
EUR 28,11
```

### Document D009 — Inventory Adjustment Note

- **Type:** `inventory_adjustment_note`
- **Role:** `adjustment_doc`
- **Date:** 2024-11-30

```
INVENTORY ADJUSTMENT NOTE
=========================

Adjustment Summary
------------------
Note ID: ADJ-0001
Reason: Shrinkage found during physical count
Amount: EUR 196,77
Reference Sheet: COUNT-0001
```

### Document D014 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-11-30

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: EUR 9.539,90
Useful Life Months: 48
Current Period Charge: EUR 198,75
Accumulated Depreciation: 198,75
```

### Document D021 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-11-30

```
BANK STATEMENT
==============

From
----
Northwind Operations
75 Market Road, Mumbai
Date: 30/11/2024

Reference Box
-------------
Document ID: D021
Document Type: bank_statement
Period: November 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0049
Statement Currency: EUR
Opening Balance: EUR 67.488,25
Closing Balance: EUR 55.270,94

Statement Rows
--------------
Rows:
  - Date 17/11/2024 | Description Loan draw LOAN-0001 | Amount EUR 53.333,22 | Running 
Balance EUR 120.821,47
  - Date 18/11/2024 | Description Asset purchase ASSET-0001 | Amount EUR -22.794,99 | 
Running Balance EUR 98.026,48
  - Date 21/11/2024 | Description Customer settlement INV-0001 | Amount EUR 2.345,84 | 
Running Balance EUR 100.372,32
  - Date 21/11/2024 | Description Loan payment LOAN-0002 | Amount EUR -15.246,33 | Running 
Balance EUR 85.125,99
  - Date 24/11/2024 | Description Supplier settlement SUP-0001 | Amount EUR -2.118,79 | 
Running Balance EUR 83.007,20
  - Date 27/11/2024 | Description Payroll PAYRUN-0001 | Amount EUR -27.736,26 | Running 
Balance EUR 55.270,94

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
| 1 | Inventory | Accounts Payable | 2,647.70 | D002, D003 | 2024-11-10 | goods_receipt_purchase |
| 2 | Input Tax Receivable | Accounts Payable | 191.96 | D002, D003 | 2024-11-10 | goods_receipt_purchase_tax |
| 3 | Accounts Receivable | Sales Revenue | 2,821.83 | D004, D005 | 2024-11-14 | delivery_sale_sale |
| 4 | Cost of Goods Sold | Inventory | 1,974.56 | D004, D005 | 2024-11-14 | delivery_sale_cogs |
| 5 | Accounts Receivable | Sales Tax Payable | 141.09 | D004, D005 | 2024-11-14 | delivery_sale_tax |
| 6 | Cash | Accounts Receivable | 2,345.84 | D006, D005 | 2024-11-21 | customer_payment |
| 7 | Accounts Payable | Cash | 2,118.79 | D007, D003 | 2024-11-24 | supplier_payment |
| 8 | Inventory Shrinkage Expense | Inventory | 196.77 | D008, D009 | 2024-11-30 | inventory_adjustment |
| 9 | Salaries Expense | Cash | 24,515.84 | D010 | 2024-11-27 | payroll_gross |
| 10 | Payroll Tax Expense | Cash | 3,220.42 | D010 | 2024-11-27 | payroll_tax |
| 11 | Utilities Expense | Accounts Payable | 2,394.93 | D011 | 2024-11-27 | utilities_bill |
| 12 | Cash | Loans Payable | 53,333.22 | D012 | 2024-11-17 | loan_draw |
| 13 | Equipment | Cash | 22,794.99 | D013 | 2024-11-18 | equipment_purchase_cash |
| 14 | Equipment | Notes Payable | 63,055.94 | D013 | 2024-11-18 | equipment_purchase_financed |
| 15 | Depreciation Expense | Accumulated Depreciation | 198.75 | D014 | 2024-11-30 | depreciation |
| 16 | Inventory | Accounts Payable | 11,784.96 | D015, D016 | 2024-11-08 | jurisdictional_tax_invoice_purchase_inventory |
| 17 | Input CGST Receivable | Accounts Payable | 1,060.64 | D015, D016 | 2024-11-08 | jurisdictional_tax_invoice_input_cgst |
| 18 | Input SGST Receivable | Accounts Payable | 1,060.65 | D015, D016 | 2024-11-08 | jurisdictional_tax_invoice_input_sgst |
| 19 | Accounts Receivable | Sales Revenue | 14,614.22 | D017, D018, D019 | 2024-11-10 | jurisdictional_tax_invoice_exempt_sale |
| 20 | Loans Payable | Cash | 14,105.48 | D020 | 2024-11-21 | loan_repayment_principal |
| 21 | Interest Expense | Cash | 1,140.85 | D020 | 2024-11-21 | loan_repayment_interest |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 55,270.94
- Inventory: 60,264.10
- Accounts Receivable: 23,241.28
- Office Supplies: 1,456.08
- Equipment: 95,390.83
- Input Tax Receivable: 191.96
- Accumulated Depreciation: -198.75
- Input CGST Receivable: 1,060.64
- Input SGST Receivable: 1,060.65

**Liabilities**
- Accounts Payable: 28,812.61
- Accrued Expenses: 3,310.25
- Loans Payable: 47,681.19
- Sales Tax Payable: 141.09
- Notes Payable: 63,055.94

**Equity**
- Retained Earnings: -4,179.99
- Owner's Equity: 98,916.64

**Totals:** Assets = 237,737.73; Liabilities = 143,001.08; Equity = 94,736.65
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
- Notes: Ties out, accept.
