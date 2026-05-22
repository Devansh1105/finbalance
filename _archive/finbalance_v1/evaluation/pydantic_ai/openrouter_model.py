"""PydanticAI/OpenRouter model adapter for the FinBalance runner."""

import os
import random
import time
from dataclasses import asdict

from pydantic_ai import Agent
from pydantic_ai.models.openrouter import OpenRouterModel, OpenRouterModelSettings
from pydantic_ai.providers.openrouter import OpenRouterProvider
from pydantic_ai.usage import RunUsage

from finbalance.env import load_project_env
from finbalance.evaluation.models.base import BaseModel, ModelConfig
from finbalance.evaluation.pydantic_ai.config import OpenRouterAgentConfig


def _is_retryable_openrouter_error(message: str) -> bool:
    text = message.lower()
    if "key limit exceeded" in text:
        return False
    retryable_markers = (
        "status_code: 429",
        "rate limit",
        "connection error",
        "temporarily unavailable",
        "status_code: 500",
        "status_code: 502",
        "status_code: 503",
        "status_code: 504",
        "timed out",
        "timeout",
    )
    return any(marker in text for marker in retryable_markers)


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
                {
                    "effort": runtime_config.openrouter_reasoning_effort,
                    **({"exclude": True} if runtime_config.openrouter_reasoning_effort == "none" else {}),
                }
                if runtime_config.openrouter_reasoning_effort
                else None
            ),
        )
        self._usage = RunUsage()

    def _build_agent(self) -> Agent:
        return Agent(
            self._model,
            model_settings=self._settings,
            system_prompt=self.runtime_config.system_prompt or (),
        )

    def complete(self, prompt: str) -> str:
        last_error: Exception | None = None
        for attempt in range(self.runtime_config.api_retries + 1):
            try:
                result = self._build_agent().run_sync(prompt)
                self._usage += result.usage()
                return str(result.output).strip()
            except Exception as exc:
                last_error = exc
                if attempt >= self.runtime_config.api_retries or not _is_retryable_openrouter_error(str(exc)):
                    raise
                delay = min(
                    self.runtime_config.retry_max_delay_s,
                    self.runtime_config.retry_base_delay_s * (2 ** attempt),
                )
                time.sleep(delay + random.uniform(0.0, 0.5))
        if last_error is not None:
            raise last_error
        raise RuntimeError("OpenRouter completion failed without returning or raising an exception.")

    def export_metadata(self) -> dict:
        metadata = super().export_metadata()
        if self.runtime_config.openrouter_reasoning_effort:
            metadata["openrouter_reasoning_effort"] = self.runtime_config.openrouter_reasoning_effort
        metadata["api_retries"] = self.runtime_config.api_retries
        metadata["retry_base_delay_s"] = self.runtime_config.retry_base_delay_s
        metadata["retry_max_delay_s"] = self.runtime_config.retry_max_delay_s
        return metadata

    def reset_usage(self) -> None:
        self._usage = RunUsage()

    def export_usage(self) -> dict:
        usage = asdict(self._usage)
        usage["total_tokens"] = usage["input_tokens"] + usage["output_tokens"]
        if not usage.get("details"):
            usage.pop("details", None)
        return usage
