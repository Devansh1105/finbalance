"""Tests for the OCR-noise perturbation and its ablation wiring."""

from finbalance.benchmark.ablations import ABLATION_MATRICES
from finbalance.benchmark.ocr_noise import perturb_ocr_text
from finbalance.benchmark.prompt import OCR_NOISE_RATES, VISIBILITY_VARIANTS

SAMPLE = "INVOICE INV-2024-0031\nInvoice Total: 4,388.89\nTax Amount: 351.11\n"


def test_zero_rate_is_identity():
    assert perturb_ocr_text(SAMPLE, rate=0.0, seed_key="r:d:0") == SAMPLE


def test_noise_is_deterministic_per_seed_key():
    first = perturb_ocr_text(SAMPLE, rate=0.05, seed_key="rec:doc:0.05")
    second = perturb_ocr_text(SAMPLE, rate=0.05, seed_key="rec:doc:0.05")
    assert first == second


def test_noise_varies_with_seed_key():
    variants = {perturb_ocr_text(SAMPLE, rate=0.05, seed_key=f"rec{i}:doc:0.05") for i in range(8)}
    assert len(variants) > 1


def test_noise_actually_corrupts_at_higher_rates():
    noisy = perturb_ocr_text(SAMPLE * 20, rate=0.10, seed_key="rec:doc:0.10")
    assert noisy != SAMPLE * 20


def test_noise_variants_registered():
    for variant in OCR_NOISE_RATES:
        assert variant in VISIBILITY_VARIANTS
    names = [spec.name for spec in ABLATION_MATRICES["ocr_noise"]]
    assert names == ["prompt_baseline", "ocr_noise_2pct", "ocr_noise_5pct", "ocr_noise_10pct"]
