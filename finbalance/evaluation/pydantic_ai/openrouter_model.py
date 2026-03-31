"""PydanticAI/OpenRouter model adapter for the FinBalance runner."""

import os

from pydantic_ai import Agent
from pydantic_ai.models.openrouter import OpenRouterModel, OpenRouterModelSettings
from pydantic_ai.providers.openrouter import OpenRouterProvider

from finbalance.env import load_project_env
from finbalance.evaluation.models.base import BaseModel, ModelConfig
from finbalance.evaluation.pydantic_ai.config import OpenRouterAgentConfig


class PydanticAIOpenRouterModel(BaseModel):
    """BaseModel-compatible wrapper around PydanticAI's OpenRouter integration."""

    def __init__(self, runtime_config: OpenRouterAgentConfig):
        super().__init__(
            ModelConfig(
                model_id=runtime_config.model_id,
                temperature=runtime_config.temperature,
                seed=runtime_config.seed,
                max_tokens=runtime_config.max_tokens,
                timeout=runtime_config.timeout,
            )
        )
        self.runtime_config = runtime_config
        load_project_env()
        self.api_key = runtime_config.api_key or os.environ.get("OPENROUTER_API_KEY", "")
        if not self.api_key:
            raise ValueError("Set OPENROUTER_API_KEY or pass api_key in OpenRouterAgentConfig.")

        self._provider = OpenRouterProvider(
            api_key=self.api_key,
            app_url=runtime_config.app_url,
            app_title=runtime_config.app_title,
        )
        self._model = OpenRouterModel(
            runtime_config.model_id,
            provider=self._provider,
        )
        self._settings = OpenRouterModelSettings(
            temperature=runtime_config.temperature,
            seed=runtime_config.seed,
            max_tokens=runtime_config.max_tokens,
            timeout=runtime_config.timeout,
            openrouter_reasoning=(
                {"effort": runtime_config.openrouter_reasoning_effort}
                if runtime_config.openrouter_reasoning_effort
                else None
            ),
        )

    def _build_agent(self) -> Agent:
        return Agent(self._model, model_settings=self._settings)

    def complete(self, prompt: str) -> str:
        result = self._build_agent().run_sync(prompt)
        return str(result.output).strip()

    def export_metadata(self) -> dict:
        metadata = super().export_metadata()
        if self.runtime_config.openrouter_reasoning_effort:
            metadata["openrouter_reasoning_effort"] = self.runtime_config.openrouter_reasoning_effort
        return metadata
