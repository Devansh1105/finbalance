"""Anthropic API model backend (uses the Messages API directly via requests)."""

import os
import requests

from finbalance.evaluation.models.base import BaseModel, ModelConfig

ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"
ANTHROPIC_VERSION = "2023-06-01"


class AnthropicModel(BaseModel):

    def __init__(self, config: ModelConfig, api_key: str | None = None):
        super().__init__(config)
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY", "")
        if not self.api_key:
            raise ValueError("Set ANTHROPIC_API_KEY env var or pass api_key=")

    def complete(self, prompt: str) -> str:
        payload = {
            "model":      self.config.model_id,
            "max_tokens": self.config.max_tokens,
            "messages":   [{"role": "user", "content": prompt}],
        }
        # Anthropic doesn't support 'seed' yet, but temperature=0 gives near-deterministic results
        if self.config.temperature == 0:
            payload["temperature"] = 0

        resp = requests.post(
            ANTHROPIC_API_URL,
            headers={
                "x-api-key":         self.api_key,
                "anthropic-version": ANTHROPIC_VERSION,
                "content-type":      "application/json",
            },
            json=payload,
            timeout=self.config.timeout,
        )
        resp.raise_for_status()
        return resp.json()["content"][0]["text"].strip()
