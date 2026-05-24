"""Two zero-cost analyses on existing per-record results.

A. Per-concept BS_recon and BS_exact by concept flag, per model baseline.
B. Cross-model entry/BS-path comparison to understand why GPT-5-low and Grok-4.3
   lack the aggregation gap.
"""
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path('/home/devanshagarwal/projects/finbalance')

MODEL_BASELINES = {
    'gemini-3-flash':    'results/gemini3flash_promoted_coverage_full_fixed/prompt_baseline/per_record_results.jsonl',
    'gpt-5-low':         'results/gpt5_sweep_baseline_low/prompt_baseline/per_record_results.jsonl',
    'claude-haiku-4.5':  'results/claude_haiku45_sweep_baseline/prompt_baseline/per_record_results.jsonl',
    'grok-4.3':          'results/grok43_sweep_baseline/prompt_baseline/per_record_results.jsonl',
    'deepseek-v3.2':     'results/deepseek_v32_sweep/prompt_baseline/per_record_results.jsonl',
    'qwen-3-235b':       'results/qwen3_235b_sweep_baseline/prompt_baseline/per_record_results.jsonl',
}

CONCEPTS = ['has_asc606', 'has_asset_disposal', 'has_deferred_tax', 'has_lease',
            'has_tax_exemption', 'has_fx', 'has_multi_invoice_payment',
            'has_interbank_transfer', 'has_reclassification', 'has_rollforward']

def load_records(path):
    records = []
    with open(ROOT / path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return records

def standard_only(records):
    """Standard records only (BS metrics are not meaningful for inconsistency packets)."""
    return [r for r in records if not r.get('record_features', {}).get('expected_inconsistency')]

def metric_mean(records, key):
    vals = [r.get('metrics', {}).get(key) for r in records]
    vals = [v for v in vals if v is not None and isinstance(v, (int, float, bool))]
    if not vals:
        return None, 0
    return sum(vals) / len(vals), len(vals)

# --- Analysis A: per-concept --------------------------------------------------
print('=' * 78)
print('A. Per-concept BS_recon and BS_exact (standard records only)')
print('=' * 78)
per_model_data = {}
for model, path in MODEL_BASELINES.items():
    p = ROOT / path
    if not p.exists():
        print(f'  MISSING: {model} -> {path}')
        continue
    records = standard_only(load_records(path))
    per_model_data[model] = records
    print(f'\n{model} (n={len(records)} standard records)')
    bs_recon, _ = metric_mean(records, 'predicted_entries_reconstruct_correct_final_balance_sheet')
    bs_exact, _ = metric_mean(records, 'final_balance_sheet_matches')
    print(f'  overall            BS_recon={bs_recon:.3f}  BS_exact={bs_exact:.3f}  gap={bs_recon-bs_exact:+.3f}')
    for concept in CONCEPTS:
        sub = [r for r in records if r.get('record_features', {}).get(concept)]
        if len(sub) < 4:
            continue
        recon, n = metric_mean(sub, 'predicted_entries_reconstruct_correct_final_balance_sheet')
        exact, _ = metric_mean(sub, 'final_balance_sheet_matches')
        print(f'  {concept:18s} BS_recon={recon:.3f}  BS_exact={exact:.3f}  gap={recon-exact:+.3f}  n={n}')

# --- Analysis B: why GPT-5-low and Grok-4.3 have no gap -----------------------
print()
print('=' * 78)
print('B. Cross-model entry quality and BS path comparison (standard records)')
print('=' * 78)
print(f'{"model":<18s}  {"BS_exact":>9s}  {"BS_recon":>9s}  {"gap":>7s}  {"JE_lenient":>11s}  {"JE_strict":>10s}  {"doc_refs_err":>13s}  {"miss":>6s}  {"extra":>6s}  {"avg_ent_diff":>13s}')
for model, records in per_model_data.items():
    bs_exact, _ = metric_mean(records, 'final_balance_sheet_matches')
    bs_recon, _ = metric_mean(records, 'predicted_entries_reconstruct_correct_final_balance_sheet')
    je_lenient, _ = metric_mean(records, 'final_journal_entries_match_no_doc_refs')
    je_strict, _ = metric_mean(records, 'final_journal_entries_match')
    doc_refs_wrong, _ = metric_mean(records, 'entries_accounting_correct_but_doc_refs_wrong')
    # Avg counts
    miss_vals = [r.get('metrics', {}).get('missing_entry_count', 0) for r in records]
    extra_vals = [r.get('metrics', {}).get('extra_entry_count', 0) for r in records]
    miss = sum(miss_vals) / max(len(miss_vals), 1)
    extra = sum(extra_vals) / max(len(extra_vals), 1)
    # Avg expected vs predicted entry count
    diffs = [r.get('metrics', {}).get('predicted_entry_count', 0) - r.get('metrics', {}).get('expected_entry_count', 0) for r in records]
    avg_diff = sum(diffs) / max(len(diffs), 1)
    print(f'{model:<18s}  {bs_exact:>9.3f}  {bs_recon:>9.3f}  {bs_recon-bs_exact:>+7.3f}  {je_lenient:>11.3f}  {je_strict:>10.3f}  {doc_refs_wrong:>13.3f}  {miss:>6.2f}  {extra:>6.2f}  {avg_diff:>+13.2f}')

# --- Analysis B2: did GPT-5/Grok skip entries entirely to dodge the gap? ------
print()
print('=' * 78)
print('B2. Did GPT-5/Grok submit fewer entries (e.g., skipping hard ones)?')
print('=' * 78)
print(f'{"model":<18s}  {"pred_entry_ct":>14s}  {"exp_entry_ct":>13s}  {"ratio":>7s}')
for model, records in per_model_data.items():
    pred = [r.get('metrics', {}).get('predicted_entry_count', 0) for r in records]
    exp = [r.get('metrics', {}).get('expected_entry_count', 0) for r in records]
    if not pred: continue
    avg_pred = sum(pred) / len(pred)
    avg_exp = sum(exp) / len(exp)
    ratio = avg_pred / avg_exp if avg_exp else 0
    print(f'{model:<18s}  {avg_pred:>14.2f}  {avg_exp:>13.2f}  {ratio:>7.2f}')

# --- Analysis B3: where do GPT-5/Grok BS_exact come from? Is BS_recon also low?
print()
print('=' * 78)
print('B3. The two regimes:')
print('   "Gap-having models": baseline BS_recon high, BS_exact low')
print('   "No-gap models":    BS_recon and BS_exact both ~equal (low? high?)')
print('=' * 78)
