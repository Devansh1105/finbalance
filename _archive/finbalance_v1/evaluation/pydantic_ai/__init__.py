"""PydanticAI-backed evaluation helpers for OpenRouter runs."""

from finbalance.evaluation.pydantic_ai.config import (
    DEFAULT_OPENROUTER_MODELS,
    OpenRouterAgentConfig,
    OpenRouterBatchConfig,
)
from finbalance.evaluation.pydantic_ai.dataset import load_dataset, sample_stratified_subset
from finbalance.evaluation.pydantic_ai.openrouter_model import PydanticAIOpenRouterModel

__all__ = [
    "DEFAULT_OPENROUTER_MODELS",
    "OpenRouterAgentConfig",
    "OpenRouterBatchConfig",
    "PydanticAIOpenRouterModel",
    "load_dataset",
    "sample_stratified_subset",
]
