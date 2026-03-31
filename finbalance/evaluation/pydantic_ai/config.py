"""Pydantic config models for the PydanticAI evaluation path."""

from pathlib import Path

from pydantic import BaseModel as PydanticModel
from pydantic import ConfigDict, Field

from finbalance.evaluation.models.base import DEFAULT_MAX_TOKENS

DEFAULT_OPENROUTER_MODELS = (
    "qwen/qwen3.5-flash-02-23",
    "deepseek/deepseek-v3.2",
    "openai/gpt-oss-120b",
    "google/gemini-3-flash-preview",
    "qwen/qwen3.6-plus-preview:free",
)


class OpenRouterAgentConfig(PydanticModel):
    """Runtime settings for one OpenRouter-backed PydanticAI model."""

    model_config = ConfigDict(extra="forbid")

    model_id: str
    temperature: float = 0.0
    seed: int = 42
    max_tokens: int = DEFAULT_MAX_TOKENS
    timeout: int = 120
    api_key: str | None = None
    app_url: str | None = None
    app_title: str = "FinBalance"
    openrouter_reasoning_effort: str | None = None
    system_prompt: str | None = None
    api_retries: int = 6
    retry_base_delay_s: float = 2.0
    retry_max_delay_s: float = 30.0


class OpenRouterBatchConfig(PydanticModel):
    """Batch-run settings for the dedicated PydanticAI harness."""

    model_config = ConfigDict(extra="forbid")

    dataset_path: Path = Path("data/large500.jsonl")
    output_dir: Path = Path("results/pydantic_ai")
    subset_size: int = 500
    subset_seed: int = 42
    write_subset_path: Path | None = None
    model_ids: tuple[str, ...] = Field(default=DEFAULT_OPENROUTER_MODELS)
    strategies: tuple[str, ...] = ("zero_shot",)
    parallel_runs: int = 1
    workers: int = 1
    resume: bool = False
    retry_failed_only: bool = False
    seed: int = 42
    temperature: float = 0.0
    max_tokens: int = DEFAULT_MAX_TOKENS
    timeout: int = 120
    api_key: str | None = None
    app_url: str | None = None
    app_title: str = "FinBalance"
    cot_openrouter_reasoning_effort: str = "high"
    api_retries: int = 6
    retry_base_delay_s: float = 2.0
    retry_max_delay_s: float = 30.0
