# Verification Packet — COV_WHO_M4_0048

_Read the documents in section 4. Then check whether the expected journal entries in section 5 and the expected balance sheet in section 6 are what you would book given those documents. Use the form at the bottom._

## 1. Record Context

- **Industry:** `wholesale_distribution`
- **Difficulty level (1–5):** 4
- **Period type:** month
- **Period label:** August 2024
- **Period start → end:** 2024-08-01 → 2024-08-31
- **Entity:** Silverline Clinic
- **Currency (display / functional):** USD / USD
- **Tax regime:** `none`
- **Document count:** 20
- **Labeled as inconsistent:** False

## 2. Allowed Account Names

_These are the only account names the model is allowed to use._

`Cash`, `Accounts Receivable`, `Inventory`, `Equipment`, `Office Supplies`, `Input Tax Receivable`, `Input CGST Receivable`, `Input SGST Receivable`, `Input IGST Receivable`, `Accumulated Depreciation`, `Accounts Payable`, `Accrued Expenses`, `Loans Payable`, `Notes Payable`, `Sales Tax Payable`, `CGST Payable`, `SGST Payable`, `IGST Payable`, `Owner's Equity`, `Retained Earnings`, `Sales Revenue`, `Cost of Goods Sold`, `Bad Debt Expense`, `Utilities Expense`, `Inventory Shrinkage Expense`, `Salaries Expense`, `Payroll Tax Expense`, `Depreciation Expense`, `Interest Expense`

## 3. Opening Trial Balance

_As of 2024-08-01_

**Assets**
- Cash: 50,486.95
- Inventory: 25,890.81
- Accounts Receivable: 5,396.42
- Office Supplies: 742.06
- Equipment: 12,747.58

**Liabilities**
- Accounts Payable: 7,120.53
- Accrued Expenses: 973.42
- Loans Payable: 7,007.03

**Equity**
- Retained Earnings: 4,752.69
- Owner's Equity: 75,410.15


## 4. Documents in this packet

_Each document has a role. `posting_doc` directly creates one or more journal entries. `support_doc` enables computation (rates, schedules, certificates). `adjustment_doc` is for period-end adjustments. `distractor_doc` should NOT generate any entries. `opening_trial_balance` is starting state only._

### Document D001 — Opening Trial Balance

- **Type:** `opening_trial_balance`
- **Role:** `posting_doc`
- **Date:** 2024-08-01

```
OPENING TRIAL BALANCE
=====================

Summary
-------
Statement Date: 2024-08-01
Prepared By: Synthetic finance engine

Account Lines
-------------
Accounts:
  - Section assets | Account Cash | Amount $50,486.95
  - Section assets | Account Inventory | Amount $25,890.81
  - Section assets | Account Accounts Receivable | Amount $5,396.42
  - Section assets | Account Office Supplies | Amount $742.06
  - Section assets | Account Equipment | Amount $12,747.58
  - Section liabilities | Account Accounts Payable | Amount $7,120.53
  - Section liabilities | Account Accrued Expenses | Amount $973.42
  - Section liabilities | Account Loans Payable | Amount $7,007.03
  - Section equity | Account Retained Earnings | Amount $4,752.69
  - Section equity | Account Owner's Equity | Amount $75,410.15

Notes
-----
Opening balances are source inputs and should tie to the rest of the packet.
```

### Document D015 — Tax Regime Notice

- **Type:** `tax_regime_notice`
- **Role:** `support_doc`
- **Date:** 2024-08-04

```
TAX REGIME NOTICE
=================

From
----
Silverline Clinic
18 Marina Avenue, Chennai
Date: 2024-08-04

Reference Box
-------------
Document ID: D015
Document Type: tax_regime_notice
Period: August 2024

Tax Rule
--------
Notice Number: TAX-0001
Tax Regime: us_sales_tax
Company Jurisdiction: New York
Counterparty Jurisdiction: Texas
Tax Rate: 7.25%
Jurisdiction Tax Amount: $2,061.59
Treatment: US purchase sales tax capitalized into inventory cost

Footer
------
Internal document packet copy.
Page marker: D015
```

### Document D016 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-08-04

```
SUPPLIER INVOICE
================

From
----
Silverline Clinic
18 Marina Avenue, Chennai
Date: 2024-08-04

To
--
Golden State Finance
Vendor remittance address on file

Reference Box
-------------
Document ID: D016
Document Type: supplier_invoice
Period: August 2024

Terms
-----
Due Date: 2024-08-17

Supplier Header
---------------
Supplier: Golden State Finance
Goods Receipt Ref: GRN-TAX-0001
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: TAXSUP-0001
Due Date: 2024-08-17
Subtotal: $28,435.69
Tax Label: US Sales Tax
Tax Rate: 7.25%
Tax Amount: $2,061.59
Total: $30,497.28

Supplier Bill Lines
-------------------
Lines:
  - Description Refill Pack | Quantity 1 | Unit Cost $28,435.69 | Amount $28,435.69

Footer
------
Internal document packet copy.
Page marker: D016
```

### Document D002 — Goods Receipt Note

- **Type:** `goods_receipt_note`
- **Role:** `support_doc`
- **Date:** 2024-08-06

```
GOODS RECEIPT NOTE
==================

Receipt Summary
---------------
GRN Number: GRN-0001
Supplier: Beacon Industrial Supply
Purchase Ref: PO-0001
Total Quantity: $67.00

Received Items
--------------
Items:
  - Sku SKU-0001 | Description Refill Pack | Quantity 67 | Unit Cost $24.00
```

### Document D003 — Supplier Invoice

- **Type:** `supplier_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-08-08

```
SUPPLIER INVOICE
================

From
----
Silverline Clinic
18 Marina Avenue, Chennai
Document Date: 2024-08-08

To
--
Beacon Industrial Supply
Vendor remittance address on file

Reference Box
-------------
Document ID: D003
Document Type: supplier_invoice
Period: August 2024

Terms
-----
Due Date: 2024-08-24

Supplier Header
---------------
Supplier: Beacon Industrial Supply
Goods Receipt Ref: GRN-0001
Currency: USD

Supplier Bill Details
---------------------
Invoice Number: SUP-0001
Due Date: 2024-08-24
Total: $1,608.00

Supplier Bill Lines
-------------------
Lines:
  - Description Refill Pack | Quantity 67 | Unit Cost $24.00 | Amount $1,608.00

Footer
------
Generated for synthetic accounting research use.
Page marker: D003
```

### Document D004 — Delivery Note

- **Type:** `delivery_note`
- **Role:** `support_doc`
- **Date:** 2024-08-11

```
DELIVERY NOTE
=============

Delivery Summary
----------------
Delivery Number: DLV-0001
Customer: Blue Finch Holdings
Shipment Ref: SHP-0001
Billed Amount: $1,216.80
Cost Basis Amount: $791.21
Cost Basis Source: Perpetual inventory cost layer for shipped SKU.

Delivered Items
---------------
Items:
  - Sku SKU-0002 | Description Widget A | Quantity 15 | Unit Price $81.12 | Unit Cost $52.75
 | Extended Cost $791.21
```

### Document D005 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-08-11

```
CUSTOMER INVOICE
================

From
----
Silverline Clinic
18 Marina Avenue, Chennai
Date: 2024-08-11

To
--
Blue Finch Holdings
Customer account on file

Reference Box
-------------
Document ID: D005
Document Type: customer_invoice
Period: August 2024
Shipment Ref: SHP-0001

Terms
-----
Due Date: 2024-08-29

Parties
-------
Customer: Blue Finch Holdings
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0001
Due Date: 2024-08-29
Total: $1,216.80

Line Items
----------
Items:
  - Description Widget A | Amount $1,216.80

Shipment Link
-------------
Shipment Ref: SHP-0001

Footer
------
Internal document packet copy.
Page marker: D005
```

### Document D013 — Equipment Invoice

- **Type:** `equipment_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-08-14

```
EQUIPMENT INVOICE
=================

Asset Purchase
--------------
Invoice Number: ASSET-0001
Vendor: Pace Office Mart
Asset Name: Display fixtures
Asset Tag: TAG-0001
Useful Life Months: 36
Total: $30,196.89
Paid Cash: $6,549.12
Financed Amount: $23,647.77
Note Reference: NOTE-0001
Financing Instrument: Promissory note payable for financed portion.
```

### Document D012 — Loan Statement

- **Type:** `loan_statement`
- **Role:** `posting_doc`
- **Date:** 2024-08-18

```
LOAN STATEMENT
==============

Loan Activity
-------------
Loan Number: LOAN-0001
Lender: Aurora Capital
Opening Principal: $2,717.55
Draw Amount: $74,130.88
Principal Paid: $0.00
Interest Paid: $0.00
Ending Principal: $76,848.43
Note: Scheduled lender activity for the selected period.
```

### Document D017 — Tax Exemption Certificate

- **Type:** `tax_exemption_certificate`
- **Role:** `support_doc`
- **Date:** 2024-08-18

```
TAX EXEMPTION CERTIFICATE
=========================

From
----
Silverline Clinic
18 Marina Avenue, Chennai
Date: 2024-08-18

To
--
Oak Harbor Foods

Reference Box
-------------
Document ID: D017
Document Type: tax_exemption_certificate
Period: August 2024

Certificate
-----------
Certificate Number: EXEMPT-0001
Counterparty: Oak Harbor Foods
Tax Regime: us_sales_tax
Effective Date: 2024-08-01
Expiration Date: 2024-08-31
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
- **Date:** 2024-08-18

```
CUSTOMER TAX PROFILE
====================

From
----
Silverline Clinic
18 Marina Avenue, Chennai
Document Date: 2024-08-18

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D018
Document Type: customer_tax_profile
Period: August 2024

Tax Profile
-----------
Profile ID: TAXPROF-0001
Customer: Oak Harbor Foods
Customer Jurisdiction: Texas
Company Jurisdiction: New York
Same State: False
Exemption Certificate: EXEMPT-0001

Footer
------
Generated for synthetic accounting research use.
Page marker: D018
```

### Document D019 — Customer Invoice

- **Type:** `customer_invoice`
- **Role:** `posting_doc`
- **Date:** 2024-08-18

```
CUSTOMER INVOICE
================

From
----
Silverline Clinic
18 Marina Avenue, Chennai
Document Date: 2024-08-18

To
--
Oak Harbor Foods
Customer account on file

Reference Box
-------------
Document ID: D019
Document Type: customer_invoice
Period: August 2024
Shipment Ref: SHP-0002

Terms
-----
Due Date: 2024-09-02

Parties
-------
Customer: Oak Harbor Foods
Currency: USD

Invoice Details
---------------
Invoice Number: INV-0002
Due Date: 2024-09-02
Subtotal: $34,221.85
Tax Label: US Sales Tax
Tax Rate: 0.00%
Tax Amount: $0.00
Exemption Certificate: EXEMPT-0001
Total: $34,221.85

Line Items
----------
Items:
  - Description Premium Kit | Amount $34,221.85

Shipment Link
-------------
Shipment Ref: SHP-0002

Footer
------
Generated for synthetic accounting research use.
Page marker: D019
```

### Document D011 — Utility Invoice

- **Type:** `utilities_statement`
- **Role:** `posting_doc`
- **Date:** 2024-08-21

```
UTILITY INVOICE
===============

From
----
Silverline Clinic
18 Marina Avenue, Chennai
Document Date: 2024-08-21

To
--
Metro Water
Vendor remittance address on file

Reference Box
-------------
Document ID: D011
Document Type: utilities_statement
Period: August 2024

Terms
-----
Due Date: 2024-09-08

Invoice Summary
---------------
Statement Number: UTIL-0001
Invoice Number: UTILINV-0001
Provider: Metro Water
Pay To: Metro Water
Service Period: August 2024
Due Date: 2024-09-08
Total: $1,069.33

Charges
-------
Charges:
  - Description Electricity | Amount $347.15
  - Description Water | Amount $722.18

Footer
------
Generated for synthetic accounting research use.
Page marker: D011
```

### Document D006 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-08-22

```
PAYMENT ADVICE
==============

From
----
Silverline Clinic
18 Marina Avenue, Chennai
Date: 2024-08-22

To
--
Blue Finch Holdings

Reference Box
-------------
Document ID: D006
Document Type: payment_advice
Period: August 2024
Reference: INV-0001

Payment Details
---------------
Advice Number: PAY-0001
Counterparty: Blue Finch Holdings
Amount: $907.51
Reference: INV-0001
Payment Method: Card
Payment For: Customer settlement

Footer
------
Internal document packet copy.
Page marker: D006
```

### Document D007 — Payment Advice

- **Type:** `payment_advice`
- **Role:** `support_doc`
- **Date:** 2024-08-26

```
PAYMENT ADVICE
==============

From
----
Silverline Clinic
18 Marina Avenue, Chennai
Date: 2024-08-26

To
--
Beacon Industrial Supply

Reference Box
-------------
Document ID: D007
Document Type: payment_advice
Period: August 2024
Reference: SUP-0001

Payment Details
---------------
Advice Number: PAY-0002
Counterparty: Beacon Industrial Supply
Amount: $1,116.97
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
- **Date:** 2024-08-27

```
PAYROLL SUMMARY
===============

From
----
Silverline Clinic
18 Marina Avenue, Chennai
Date: 2024-08-27

Payroll Summary
---------------
Run Number: PAYRUN-0001
Pay Period: August 2024
Headcount: 10
Gross Pay: $11,223.98
Employer Tax: 1,508.95
Cash Outflow: $12,732.93

Footer
------
Internal document packet copy.
Page marker: D010
```

### Document D008 — Stock Count Sheet

- **Type:** `stock_count_sheet`
- **Role:** `support_doc`
- **Date:** 2024-08-31

```
STOCK COUNT SHEET
=================

Count Summary
-------------
Sheet ID: COUNT-0001
Location: Warehouse A

Counted Items
-------------
Items:
  - Sku SKU-0003 | Description Premium Kit | System Qty 100 | Counted Qty 96 | Unit Cost 
$11.61
```

### Document D009 — Inventory Adjustment Note

- **Type:** `inventory_adjustment_note`
- **Role:** `adjustment_doc`
- **Date:** 2024-08-31

```
INVENTORY ADJUSTMENT NOTE
=========================

Adjustment Summary
------------------
Note ID: ADJ-0001
Reason: Shrinkage found during physical count
Amount: $46.44
Reference Sheet: COUNT-0001
```

### Document D014 — Depreciation Schedule

- **Type:** `depreciation_schedule`
- **Role:** `adjustment_doc`
- **Date:** 2024-08-31

```
DEPRECIATION SCHEDULE
=====================

Depreciation Schedule
---------------------
Schedule ID: DEP-0001
Asset Name: Equipment
Asset Tag: OPEN-EQU
Cost: $12,747.58
Useful Life Months: 48
Current Period Charge: $265.57
Accumulated Depreciation: 265.57
```

### Document D020 — Bank Statement

- **Type:** `bank_statement`
- **Role:** `support_doc`
- **Date:** 2024-08-31

```
BANK STATEMENT
==============

From
----
Silverline Clinic
18 Marina Avenue, Chennai
Date: 2024-08-31

Reference Box
-------------
Document ID: D020
Document Type: bank_statement
Period: August 2024

Account Summary
---------------
Account Name: Operating Account
Account Number: 1002-0048
Statement Currency: USD
Opening Balance: $50,486.95
Closing Balance: $105,126.32

Statement Rows
--------------
Rows:
  - Date 2024-08-14 | Description Asset purchase ASSET-0001 | Amount $-6,549.12 | Running 
Balance $43,937.83
  - Date 2024-08-18 | Description Loan draw LOAN-0001 | Amount $74,130.88 | Running Balance 
$118,068.71
  - Date 2024-08-22 | Description Customer settlement INV-0001 | Amount $907.51 | Running 
Balance $118,976.22
  - Date 2024-08-26 | Description Supplier settlement SUP-0001 | Amount $-1,116.97 | Running
 Balance $117,859.25
  - Date 2024-08-27 | Description Payroll PAYRUN-0001 | Amount $-12,732.93 | Running Balance
 $105,126.32

Notes
-----
Generated from the internal cash ledger so that every listed movement is consistent.

Footer
------
Internal document packet copy.
Page marker: D020
```

## 5. Expected Journal Entries (ground truth)

| # | Debit | Credit | Amount | Doc refs | Posting date | Label |
|---|---|---|---:|---|---|---|
| 1 | Inventory | Accounts Payable | 1,608.00 | D002, D003 | 2024-08-08 | goods_receipt_purchase |
| 2 | Accounts Receivable | Sales Revenue | 1,216.80 | D004, D005 | 2024-08-11 | delivery_sale_sale |
| 3 | Cost of Goods Sold | Inventory | 791.21 | D004, D005 | 2024-08-11 | delivery_sale_cogs |
| 4 | Cash | Accounts Receivable | 907.51 | D006, D005 | 2024-08-22 | customer_payment |
| 5 | Accounts Payable | Cash | 1,116.97 | D007, D003 | 2024-08-26 | supplier_payment |
| 6 | Inventory Shrinkage Expense | Inventory | 46.44 | D008, D009 | 2024-08-31 | inventory_adjustment |
| 7 | Salaries Expense | Cash | 11,223.98 | D010 | 2024-08-27 | payroll_gross |
| 8 | Payroll Tax Expense | Cash | 1,508.95 | D010 | 2024-08-27 | payroll_tax |
| 9 | Utilities Expense | Accounts Payable | 1,069.33 | D011 | 2024-08-21 | utilities_bill |
| 10 | Cash | Loans Payable | 74,130.88 | D012 | 2024-08-18 | loan_draw |
| 11 | Equipment | Cash | 6,549.12 | D013 | 2024-08-14 | equipment_purchase_cash |
| 12 | Equipment | Notes Payable | 23,647.77 | D013 | 2024-08-14 | equipment_purchase_financed |
| 13 | Depreciation Expense | Accumulated Depreciation | 265.57 | D014 | 2024-08-31 | depreciation |
| 14 | Inventory | Accounts Payable | 30,497.28 | D015, D016 | 2024-08-04 | jurisdictional_tax_invoice_us_purchase_cost_includes_tax |
| 15 | Accounts Receivable | Sales Revenue | 34,221.85 | D017, D018, D019 | 2024-08-18 | jurisdictional_tax_invoice_exempt_sale |

## 6. Expected Final Balance Sheet (ground truth)

**Assets**
- Cash: 105,126.32
- Inventory: 57,158.44
- Accounts Receivable: 39,927.56
- Office Supplies: 742.06
- Equipment: 42,944.47
- Accumulated Depreciation: -265.57

**Liabilities**
- Accounts Payable: 39,178.17
- Accrued Expenses: 973.42
- Loans Payable: 81,137.91
- Notes Payable: 23,647.77

**Equity**
- Retained Earnings: 25,285.86
- Owner's Equity: 75,410.15

**Totals:** Assets = 245,633.28; Liabilities = 144,937.27; Equity = 100,696.01
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
