# FinBalance — Revision Ledger

Single source of truth for what was measured, what was corrected, what shipped where,
and what remains. Maintained during the ARR May-2026 author-response period
(rebuttal posted July 2026; revision = EMNLP camera-ready if accepted at the Aug 2
commitment, else next-cycle resubmission).

Legend: **[REPLY]** cited in posted reviewer replies · **[RESERVE]** completed, held for
discussion follow-ups · **[REVISION]** goes into the revised paper/artifact ·
**[FROZEN]** must not be touched before the revision.

---

## 1. Experiments run during the response period

All on the 143-record compact split unless noted; harness = submitted code plus two
response-period extensions (`finbalance/benchmark/ocr_noise.py`; native function-calling
loop in `tools.py`), both to be included in the revision artifact.

| # | Experiment | Result | Status |
|---|---|---|---|
| E1 | Payload audit of 6 headline runs | Grok reasoned 710/710 (mean 1,189 tok); GPT-5 mean 3,463; Gemini/Haiku/Qwen 0; DeepSeek endpoint non-reasoning | [REPLY] R2 |
| E2 | deepseek-reasoner vs chat | BS_exact 54.2% vs 8.3%; gap 1.7 vs 42.0pp | [REPLY] R2 |
| E3 | Haiku 4.5 reasoning-low @32k | 38.3% vs 4.2%; gap 8.4 vs 29.1pp | [REPLY] R2 |
| E4 | Grok-4.3 reasoning-none @16k (budget-matched) | 3.3%; gap 27.5pp appears | [REPLY] R2 |
| E5 | GPT-5 minimal @16k | 0%; gap 24.2pp; 22.4% unparseable | [REPLY] R2 |
| E6 | Tool agents text protocol (Gemini 0/572, DeepSeek, Haiku) | 0 invocations everywhere; Haiku 20.0% (protocol effect) | [REPLY] R2 |
| E7 | Tool agents native FC (DeepSeek, GPT-5, Haiku; 8-call budget) | DeepSeek 45.8% (+37.5pp, median 8 calls); GPT-5 52.5%; Haiku 23.3%; strict ≤5.8% all | [REPLY] R2 |
| E8 | OCR corruption sweep, Gemini + DeepSeek, achieved rates 0.94/2.20/4.45% | Monotone recon decline; clean-text shortfall ~3x harshest noise; parse 99-100% | [REPLY] R1 |
| E9 | Repeats x3: DeepSeek, GPT-5, Haiku, Grok, Qwen(Vertex) | BS_exact ranges 0.0-3.3pp | [REPLY] R2 |
| E10 | Fresh-seed 710 regeneration + DeepSeek re-eval | BS_recon 47.3% both; all metrics ~1pp | [REPLY] R2 |
| E11 | Structural audit, 6,710 records, 9 invariants | 100% pass; per-cell CSVs (`results/structural_audit/`) | [REPLY] R3 |
| E12 | Doc_refs decomposition + superset-tolerant scoring | Supersets 42-59% (Gem/GPT-5), 94-96% support-role extras; tolerant strict ≤15.8% | [REPLY] R2 |
| E13 | Gemini native tools (anchor) | DONE: 52.5% BS_exact, 141/143 records used tools (mean 3.4), strict 5.8% | [REPLY] R2 |
| E14 | Gemini repeats x3 (Vertex) | DONE: BS_exact 24.2-25.0% (range 0.8pp) | [REPLY] R2 |
| E15 | deepseek-reasoner @ full 710 (sharded) | DONE: 44.0% BS_exact, gap 4.8pp, false alarms 29.0% | [REPLY] R2 |
| E16 | Gemini 3.1 Pro frontier | 37.5/62.5; strict 6.7%; parse 100% | [RESERVE] |
| E17 | Qwen3-thinking-2507 @32k | DONE: BS_exact 1.7% → 31.7%, gap ~31 → 8.3pp, strict 0.0% — fifth family; promoted into R2 reply (completes reviewer-named list) | [REPLY] R2 |
| E18 | Gemini 3 Flash thinking-high @64k | running (32k budget insufficient: thinking exhausts it) | [RESERVE] |
| E19 | Multimodal rendered-document condition | NOT BUILT — scoped as future work in replies | [REVISION] |

## 2. Corrections to the submitted paper

### Disclosed in the replies (because a reviewer would otherwise find the conflict)
| C1 | Table 8: Grok "no reasoning" → provider-default reasoning ON; add requested-vs-observed columns for all models | R2 opener |
| C2 | Context-stress deltas 16.7/15.8/18.3pp used full-bundle baseline; correct = 5.8-8.3pp vs evidence-only | R1 parenthetical |
| C3 | Doc-ref mismatch metric text: it is incidence per expected entry (52.4% anchor), not share of otherwise-correct entries (61.8%) | R2 sensitivity para |

### Silent revision fixes (normal hygiene; no reviewer asked)
| C4 | §6 difficulty numbers 0.95/0.02 attributed to Figure 6's split; correct: 0.88/0.00 (compact) or label as core-split |
| C5 | Ledger-feedback tool returns full replayed balance sheet + account deltas, not "per-section deltas"; reframe effect as combined announce+replay+revise protocol; "current_assets" example wrong |
| C6 | Ledger-feedback baseline is an independent run, not the treatment's own first pass — label accordingly or rescore |
| C7 | "Specialist" model families → general-purpose only |
| C8 | "Full ablation matrix" → broad unary + targeted suite |
| C9 | Appendix calls compact split "core evaluation split"; some cells 40/45 records — label per condition |
| C10 | BS metric appendix names current/non-current sections that don't exist in scorer |
| C11 | "202 arithmetic errors / 85 account-selection" → "amount mismatches / account mismatches" (matcher categories) |
| C12 | Related-work table implies role tags visible; they are hidden |
| C13 | "Every compact scenario reviewed" → "every industry-period-difficulty cell and every inconsistency code" |
| C14 | BS_recon prose: replayed success can occur without exact entry sets (29/263 Gemini etc.) — qualify |
| C15 | Inconsistency-degradation mechanism ("deltas bias toward reconciling") → mark as conjecture |
| C16 | opening_trial_balance role tag `posting_doc` vs appendix "never generates entries" — document or change role |
| C17 | Record COV_RET_Q5_0039: FY label "Q4 FY 2026-27" should be FY 2025-26 (fiscal_start_month=4) — generator fix |
| C18 | Record COV_WHO_M5_0049: metadata `sales_tax` vs GST documents D015/D016/D019 — generator consistency fix |
| C19 | Abstract "validate the labels" → qualify with 3/23 loose-fit codes (also disclosed in R3 reply) |
| C20 | Human-review scope: reviewers briefed not to recheck arithmetic — state review scope in paper |
| C21 | Related work: add/discuss industry evaluations found post-submission — AccountingBench (Penrose "Can LLMs Do Accounting?": agents close real company books from Ramp/Stripe/Mercury data, judged on statements) and DualEntry's accounting AI benchmark — differentiate on deterministic regenerable labels, citation grounding, inconsistency taxonomy, public generator vs single-company closed data; keep novelty claim scoped exactly as in the rebuttal (pending Codex research verdict) |

## 3. Frozen until revision (and why)

- OpenReview Software/Data zips — platform-frozen during discussion.
- Anonymous mirror, including `human_verification/` "(2)" files and `_archive/` build
  logs containing a local username — mid-review edits create tampering optics; the
  public preprint makes the anonymity point moot under current ARR policy.
- The paper PDF — no uploads during discussion.

## 4. Revision assembly checklist (camera-ready or resubmission)

1. Apply C1-C20. 2. Add response-period experiments as appendix/results updates:
six-family reasoning matrix (E2-E5, E17, E18), dual-protocol tool study (E6, E7, E13),
OCR-corruption appendix (E8), stability checks (E9, E14), fresh-seed replication (E10,
extend to full panel if budget allows), structural audit + script + CSVs (E11), citation
decomposition + dual scoring (E12), frontier row (E16). 3. Prompts appendix; N
annotations; anchor-only scope labels; §7 utility paragraph; "Extending FinBalance"
appendix. 4. Regenerate records for C17/C18;
rerun structural audit; note as erratum. 5. Clean `_archive/` build logs from mirror;
update mirror to revision state. 6. Multimodal condition (E19) if resources allow. 7. Rotate all API keys used during the response period.
8. §7 future-work sentence only (no measurement commitment): ledger-as-verifier for
training (SFT data, verifier-reward RL, efficiency distillation) — deliberately scoped
as intended use; the actual training-utility measurement is the follow-up paper, not a
revision item.

## 5. Repo hygiene

Removed: `rebuttal.md` (pre-session AI draft, superseded), `rebuttal_replies.md` (working
copy; final content preserved in `rebuttal_final_post.md` and `post_ready/`),
`.codex-out/` (worker scratch), and `scripts/rebuttal_runs/07_gemini_free.sh` (AI Studio free-tier path dead —
prepay billing rejected it; superseded by `08_vertex_anchor.sh`). Kept deliberately:
01-06, 08 (document exact run configs behind `results/rebuttal/`), superseded monolithic
result dirs `reasoning_parity/deepseek_reasoner_main710/` and `qwen3_thinking_32k/`
(partial rows merge into shard results; excluded from health watchdog). `.codex-out/`
gitignored. Scratchpad shard files are session-temporary outside the repo.
