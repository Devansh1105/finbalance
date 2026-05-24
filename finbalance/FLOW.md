# FinBalance Generation Flow

This file explains the **current** `finbalance/` flow in simple words.

It covers:

- how one normal record is made
- where distractor documents are added
- how negative-control records are made
- how currency/date format variation works
- how indirect tax, ASC 606, fixed assets, deferred tax, lease accounting, and foreign-currency support work
- how the benchmark asks models to report inconsistencies

## One Record In One Picture

```text
industry + level + period type
    ->
choose period range
    ->
choose record display format
  - currency style
  - date style
    ->
choose record accounting profile
  - functional currency
  - indirect-tax regime
    ->
build master data
    ->
build opening balance
    ->
pick business scenarios from the industry schema
    ->
each scenario creates:
  - document seeds
  - journal entries
  - bank rows
    ->
add distractor documents
    ->
add opening trial balance doc
add bank statement doc
    ->
render all document seeds into PDF-style files + OCR text
    ->
validate the clean record
    ->
run the ledger
    ->
if this is a normal record:
  keep expected entries + expected balance sheet
if this is a negative-control record:
  mutate one visible document to make the record inconsistent
  store expected inconsistency code instead of entries/balance sheet
    ->
final dataset record
```

## The Main Objects

### `PeriodSpec`

Defined in [types.py](/home/devanshagarwal/projects/finbalance/finbalance/types.py).

This says what time span the record covers:

- `month`, `quarter`, or `year`
- start date
- end date
- period label
- fiscal start month

### `DocSchema`

Also in [types.py](/home/devanshagarwal/projects/finbalance/finbalance/types.py).

This says what one document type looks like:

- required fields
- optional fields
- visible sections
- layout variants
- which values must show up in OCR text

The actual schema files live in [doc_schemas/](/home/devanshagarwal/projects/finbalance/finbalance/doc_schemas).

### `IndustrySchema`

Also in [types.py](/home/devanshagarwal/projects/finbalance/finbalance/types.py).

This says how one industry works:

- allowed account list
- opening-balance rules
- business scenarios
- scenario plans by period and difficulty
- allowed distractor document types

The industry files live in [industry_schemas/](/home/devanshagarwal/projects/finbalance/finbalance/industry_schemas).

### `BusinessScenario`

This is one reusable business situation.

Examples:

- customer invoice
- supplier payment
- payroll
- prepaid rent
- subscription billing
- revenue release
- production batch moving into finished goods

The reusable builders live in [generation/scenario_factories.py](/home/devanshagarwal/projects/finbalance/finbalance/generation/scenario_factories.py).

### `BusinessState`

This is the working state while one record is being built.

It keeps:

- period info
- opening balance
- entity name and address
- display format:
  - currency code
  - currency symbol/prefix
  - date format
- accounting profile:
  - functional currency
  - tax regime / tax label
- all document seeds
- all journal entries
- bank rows
- open receivables and payables
- open foreign-currency receivables and payables
- deferred revenue items
- inventory / batch state
- contract subledger for ASC 606 bundled allocations
- enriched asset register for depreciation, disposals, and deferred tax
- lease subledger for ROU asset and lease liability schedules
- jurisdiction profile for company/customer/vendor tax jurisdiction
- tax context for regime, rate, account mapping, and exemption treatment
- inconsistency metadata when needed

## A Concrete Example

This call generates one **clean** record:

```python
DocumentBenchmarkBuilder(seed=42).generate_record(
    "FLOW_EXAMPLE",
    "subscription_saas",
    4,
    "/tmp/finbalance_flow",
    period_type="year",
)
```

This call generates one **negative-control** record:

```python
DocumentBenchmarkBuilder(seed=42).generate_record(
    "FLOW_NEGATIVE",
    "subscription_saas",
    4,
    "/tmp/finbalance_flow",
    period_type="year",
    negative_control=True,
)
```

## Step 1: Builder Entry

Code:
- [generation/builder.py](/home/devanshagarwal/projects/finbalance/finbalance/generation/builder.py)

Input:

```text
record_id    = FLOW_EXAMPLE
industry     = subscription_saas
level        = 4
period_type  = year
```

Output:

- one `DocumentRecord`

## Step 2: Period Is Chosen

Code:
- [generation/helpers.py](/home/devanshagarwal/projects/finbalance/finbalance/generation/helpers.py)

The builder creates a `PeriodSpec`.

Example:

```text
period_type        = year
start_date         = 2025-01-01
end_date           = 2025-12-31
label              = FY 2025
fiscal_start_month = 1
```

## Step 3: Display Format Is Chosen

Code:
- [generation/helpers.py](/home/devanshagarwal/projects/finbalance/finbalance/generation/helpers.py)

Before documents are built, the record gets one display profile.

That profile controls:

- currency style
- date style

Most records are:

- `USD`
- `YYYY-MM-DD`

A small fixed subset of generated datasets use:

- `GBP` or `EUR`
- `DD/MM/YYYY`

Important:

- one record uses one currency style
- one record uses one date style
- one record has one functional currency for the answer
- some documents may still be shown in a different source currency when FX scenarios are present
- the accounting truth does **not** change because of formatting
- only the visible document surface changes

## Step 4: Master Data Is Built

Code:
- [generation/master_data.py](/home/devanshagarwal/projects/finbalance/finbalance/generation/master_data.py)

What goes in:

- industry
- random generator
- chosen period

What comes out:

- customers
- vendors
- products
- services
- tenants
- patients
- lenders
- subscription plans
- raw materials
- finished goods

This master data keeps names and references consistent across documents.

## Step 5: Opening Balance Is Built

Code:

- industry file, for example [industry_schemas/subscription_saas.py](/home/devanshagarwal/projects/finbalance/finbalance/industry_schemas/subscription_saas.py)
- shared helper [industry_schemas/common.py](/home/devanshagarwal/projects/finbalance/finbalance/industry_schemas/common.py)

What happens:

- the chosen industry picks balance-sheet accounts that make sense for that industry
- year records allow richer opening balances than month records
- the opening balances are also scaled by:
  - industry
  - period type
  - difficulty

So a SaaS yearly record can now start with much larger balances than a small monthly professional-services record.

Example output shape:

```text
Assets:
  Cash
  Accounts Receivable
  Prepaid Insurance
  Equipment
  Office Supplies

Liabilities:
  Accounts Payable
  Accrued Expenses
  Unearned Revenue
  Loans Payable

Equity:
  Share Capital
  Retained Earnings
```

## Step 6: Scenarios Are Picked

Code:
- [generation/builder.py](/home/devanshagarwal/projects/finbalance/finbalance/generation/builder.py)
- industry file for the chosen industry

The builder looks at:

```text
industry_schema.period_plans[period_type][difficulty_level]
```

That tells it:

- which scenarios are mandatory
- which scenarios are optional
- how many documents the final record should roughly contain

For `subscription_saas`, year level 4 can include:

```text
subscription_invoice
revenue_release
customer_payment
hosting_bill
vendor_payment
payroll
loan_draw
bundled_contract_allocation
interbank_transfer
expense_accrual
credit_memo
renewal_invoice
subscription_cash_invoice
```

Difficulty levels remain public `1` through `5`:

- Level 1: one-step visible postings
- Level 2: simple two-doc support chains and directly visible tax or FX arithmetic
- Level 3: one schedule, partial settlement, simple correction, or simple rollforward
- Level 4: one subledger-driven multi-step scenario such as jurisdictional tax, ASC 606, asset disposal, or baseline lease accounting
- Level 5: multi-schedule compositional reasoning, including deferred tax, lease modification, and disposal plus deferred tax

## Step 7: Each Scenario Creates Documents And Entries

Code:
- [generation/scenario_factories.py](/home/devanshagarwal/projects/finbalance/finbalance/generation/scenario_factories.py)

This is the main place where business logic is turned into:

- document seeds
- journal entries
- bank rows

### Example: `subscription_invoice`

Input:

```text
customer = Blue Finch Holdings
plan     = Enterprise License
months   = 12
total    = 916,333.09
```

Output:

- one support doc:
  - `subscription_order_form`
- one posting doc:
  - `customer_invoice`
- one journal entry:

```text
Debit  Accounts Receivable
Credit Unearned Revenue
Amount 916,333.09
```

### Example: `revenue_release`

Output:

- one adjustment doc:
  - `revenue_recognition_schedule`
- one journal entry:

```text
Debit  Unearned Revenue
Credit Service Revenue
Amount <release amount>
```

### Example: `customer_payment`

Output:

- one support doc:
  - `payment_advice`
- one journal entry:

```text
Debit  Cash
Credit Accounts Receivable
Amount <payment amount>
```

### Example: `bundled_contract_allocation`

Output:

- `subscription_order_form`
- `customer_invoice`
- `ssp_rate_card`
- `implementation_acceptance_memo`
- `performance_obligation_schedule`

The invoice line split is intentionally not the accounting allocation. The schedule allocates the contract transaction price using visible SSPs. Implementation revenue is released on acceptance; platform revenue is released ratably.

### Example: `jurisdictional_tax_invoice`

Output:

- `tax_regime_notice`
- `supplier_invoice`
- `tax_exemption_certificate`
- `customer_tax_profile`
- `customer_invoice`

US sales tax on purchases is embedded in inventory cost. India GST uses `Input CGST Receivable` plus `Input SGST Receivable` for same-state purchases and `Input IGST Receivable` for different-state purchases. Valid exemption certificates override default tax on the exempt sale.

### Example: `asset_disposal`, `deferred_tax_depreciation`, and leases

The professional-services level 4 and 5 plans add:

- fixed asset disposal notices and sale proceeds advice
- deferred tax schedules and memos for book/tax depreciation differences
- lease agreements, lease amortization schedules, payment notices, and modification notices

These scenarios drive the `asset_register`, `tax_context`, and `lease_subledger` rather than relying on only one visible invoice.

## Step 8: Amounts Are Scaled

Code:
- [generation/helpers.py](/home/devanshagarwal/projects/finbalance/finbalance/generation/helpers.py)
- [generation/scenario_factories.py](/home/devanshagarwal/projects/finbalance/finbalance/generation/scenario_factories.py)

Amounts are no longer all in one small range.

The generator now scales amounts using:

- industry
- period type
- difficulty
- amount bucket

Examples of buckets:

- `micro`
- `small`
- `operating`
- `inventory`
- `payroll`
- `contract`
- `capital`
- `financing`

This is why:

- receipts can be tiny
- subscription contracts can be large
- yearly financing and manufacturing amounts can be much larger than before

## Step 9: Distractor Documents Are Added

Code:
- [generation/builder.py](/home/devanshagarwal/projects/finbalance/finbalance/generation/builder.py)
- [doc_schemas/](/home/devanshagarwal/projects/finbalance/finbalance/doc_schemas)

After the real business scenarios are built, the builder may add documents that should **not** create new entries.

These use role:

```text
distractor_doc
```

Current distractor types:

- `secondary_copy`
- `vendor_statement`
- `memo`
- `cancellation_note`

What they are for:

- duplicate scans
- overlapping vendor paperwork
- admin notes
- void/reissue notices

Important:

- distractors do not create postings
- they are part of the visible document bundle only
- year records get the most distractors

## Step 10: Opening Balance And Bank Statement Docs Are Added

Code:
- [generation/builder.py](/home/devanshagarwal/projects/finbalance/finbalance/generation/builder.py)

The builder always adds:

- `opening_trial_balance`
- one or more `bank_statement` documents

Bank statements are built from the same bank rows that came from the scenario logic.

If the record uses more than one bank account, the builder now renders one statement per account.

So for a clean record:

- the bank statement is consistent with the entries
- the ledger and visible bank doc come from the same internal truth

## Step 11: Document Seeds Become PDF-Style Documents

Code:
- [rendering/renderer.py](/home/devanshagarwal/projects/finbalance/finbalance/rendering/renderer.py)
- [render.py](/home/devanshagarwal/projects/finbalance/finbalance/render.py)

What goes in:

- one `DocumentSeed`
- its schema
- one layout variant
- one display profile

What comes out:

- a PDF-style file
- OCR text

The renderer now uses:

- issuer block
- recipient block
- reference box
- terms block
- approval/context block
- footer block
- layout variants
- record-specific currency/date formatting

This is where a date may show as:

```text
2025-04-18
```

or:

```text
18/04/2025
```

And where a money amount may show as:

```text
$12,540.00
```

or:

```text
GBP 12,540.00
```

## Step 12: Clean-Packet Validation Runs

Code:
- [validation/doc_validation.py](/home/devanshagarwal/projects/finbalance/finbalance/validation/doc_validation.py)
- [validation/record_validation.py](/home/devanshagarwal/projects/finbalance/finbalance/validation/record_validation.py)

Validation runs on the **clean** record before any negative-control mutation.

Checks include:

- required fields exist
- rendered OCR includes required visible values
- posting references point to real docs
- accounts are allowed for that industry
- same-account debit/credit is rejected
- balance sheet balances
- year records include at least one summary/close doc
- tax totals, tax rates, and exchange-rate computations tie
- ASC 606 allocation totals and release amounts tie to the schedule
- asset disposal NBV and gain/loss computations tie
- deferred tax movement ties to the ending deferred tax liability
- lease payments split into interest/principal and lease modifications adjust liability and ROU asset by the same delta

This is why normal records stay sound.

## Step 13: Ledger Builds The Final Balance Sheet

Code:
- [ledger.py](/home/devanshagarwal/projects/finbalance/finbalance/ledger.py)

For a clean record:

- opening balance + expected entries
  ->
- final balance sheet

This gives:

- final assets
- final liabilities
- final equity
- balanced or not

## Step 14: Negative-Control Records

Code:
- [generation/builder.py](/home/devanshagarwal/projects/finbalance/finbalance/generation/builder.py)
- [inconsistencies.py](/home/devanshagarwal/projects/finbalance/finbalance/inconsistencies.py)

Some records are intentionally made inconsistent.

This happens **after** the clean record has already been generated and validated.

So the flow is:

```text
build a clean sound record
    ->
pick one visible document
    ->
mutate a visible amount
    ->
store inconsistency code
    ->
set expected entries to []
set expected balance sheet to empty
```

Current inconsistency codes:

- `invoice_total_mismatch`
- `bank_closing_mismatch`
- `statement_balance_mismatch`
- `payment_allocation_mismatch`
- `duplicate_reference_conflict`
- `schedule_rollforward_mismatch`
- `inventory_rollforward_mismatch`
- `transfer_mismatch`
- `reclassification_support_mismatch`
- `tax_total_mismatch`
- `tax_rate_mismatch`
- `input_tax_mismatch`
- `jurisdiction_tax_mismatch`
- `tax_exemption_conflict`
- `ssp_allocation_mismatch`
- `performance_obligation_release_mismatch`
- `asset_disposal_mismatch`
- `deferred_tax_rollforward_mismatch`
- `lease_schedule_mismatch`
- `lease_remeasurement_mismatch`
- `exchange_rate_mismatch`
- `fx_settlement_mismatch`
- `remeasurement_mismatch`

Examples:

### `invoice_total_mismatch`

- the visible invoice total is changed
- the listed line items are left as-is
- so the document contradicts itself

### `bank_closing_mismatch`

- the visible bank statement closing balance is changed
- the listed movements are left as-is
- so the closing balance no longer ties

Important:

- the mismatch amount is randomized now
- it is not a fixed signature

## Step 15: What Gets Stored For A Negative-Control Record

In the final dataset record:

- `expected_inconsistency = true`
- `expected_inconsistency_codes = [...]`
- `inconsistency_reasons = [...]`
- `expected_entries = []`
- `expected_balance_sheet = empty`

So the benchmark truth is deterministic.

## Step 16: How The Benchmark Asks Models To Answer

Code:
- [benchmark/prompt.py](/home/devanshagarwal/projects/finbalance/finbalance/benchmark/prompt.py)

The model sees:

- OCR text for all documents
- allowed account names
- allowed inconsistency codes
- strict JSON output shape

The prompt explicitly tells the model:

- distractors may be present
- some support documents only make sense when read together
- one payment can settle several invoices
- some cash movements are inter-bank transfers with no revenue or expense
- some entries are internal reclassifications or corrections
- records may contain ASC 606 bundled contracts where SSP rate cards and performance-obligation schedules drive revenue recognition
- country-specific tax rules may apply; US sales tax purchases are not recoverable input tax, while India GST uses CGST/SGST or IGST based on jurisdiction
- exemption certificates can override default tax treatment
- fixed asset disposals require NBV, accumulated depreciation removal, proceeds, and gain/loss computation
- deferred tax comes only from visible book/tax depreciation differences and tax rates
- lease accounting uses visible lease agreements, payment notices, amortization schedules, and modification notices
- some records may be inconsistent
- if inconsistent:
  - set `has_inconsistency = true`
  - choose from the fixed `inconsistency_codes` list
  - leave `entries = []`
  - leave `balance_sheet` empty
- use only visible rates, SSPs, tax rules, schedules, and support docs
- do not invent assumptions
- do not round except to cents for final monetary amounts

Current inconsistency output shape:

```json
{
  "has_inconsistency": true,
  "inconsistency_codes": ["bank_closing_mismatch"],
  "inconsistency_notes": ["Bank closing balance does not tie to the listed rows."],
  "entries": [],
  "balance_sheet": {
    "assets": {},
    "liabilities": {},
    "equity": {}
  }
}
```

## Step 17: How Inconsistency Is Scored

Code:
- [benchmark/parser.py](/home/devanshagarwal/projects/finbalance/finbalance/benchmark/parser.py)
- [benchmark/scoring.py](/home/devanshagarwal/projects/finbalance/finbalance/benchmark/scoring.py)

For negative-control records, the benchmark compares:

- `has_inconsistency`
- `inconsistency_codes`
- whether the model leaves entries empty
- whether the model leaves the balance sheet empty

Important:

- `inconsistency_codes` are exact-match comparable
- `inconsistency_notes` are only explanatory text
- we do **not** compare free-form sentences as ground truth

## Step 18: How Normal Records Are Scored

Code:
- [benchmark/scoring.py](/home/devanshagarwal/projects/finbalance/finbalance/benchmark/scoring.py)

For normal records, the benchmark now uses four plain exact-match metrics:

- `Final balance sheet matches`
  - the predicted final balance sheet exactly matches the expected final balance sheet
- `Final balance sheet and the journal entries match`
  - both the final balance sheet and the journal entries exactly match
- `Final journal entries match`
  - the predicted journal entries exactly match on:
    - doc refs
    - debit account
    - credit account
    - amount
- `Final journal entries match (not considering doc_refs, only account and amount)`
  - the predicted journal entries exactly match if we ignore doc refs and compare only:
    - debit account
    - credit account
    - amount

This means the benchmark now separates:

- accounting correctness
- document-link correctness

So if a model gets the accounts and amounts right but cites different supporting documents, that will:

- fail `Final journal entries match`
- but may still pass `Final journal entries match (not considering doc_refs, only account and amount)`

The benchmark summary also groups those same metrics by:

- difficulty level
- period type
- industry

## Short Version

The full flow is now:

```text
industry schema
  -> choose period
  -> choose display format
  -> build master data
  -> build opening balance
  -> pick scenarios
  -> maintain contract, asset, lease, jurisdiction, and tax subledgers
  -> create clean document seeds + journal entries + bank rows
  -> add distractor docs
  -> add opening trial balance + bank statement
  -> render PDF-style docs + OCR
  -> validate clean record
  -> ledger builds final balance sheet
  -> if negative-control:
       mutate one visible doc
       store inconsistency code
       replace accounting answer with inconsistency answer
  -> final dataset record
```
