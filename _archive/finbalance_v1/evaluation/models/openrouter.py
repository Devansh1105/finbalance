"""OpenRouter API model backend."""

import os
import requests

from finbalance.env import load_project_env
from finbalance.evaluation.models.base import BaseModel, ModelConfig


class OpenRouterModel(BaseModel):
    API_URL = "https://openrouter.ai/api/v1/chat/completions"

    def __init__(self, config: ModelConfig, api_key: str | None = None):
        super().__init__(config)
        load_project_env()
        self.api_key = api_key or os.environ.get("OPENROUTER_API_KEY", "")
        if not self.api_key:
            raise ValueError("Set OPENROUTER_API_KEY env var or pass api_key=")

    def complete(self, prompt: str) -> str:
        payload = {
            "model":       self.config.model_id,
            "messages":    [{"role": "user", "content": prompt}],
            "temperature": self.config.temperature,
            "seed":        self.config.seed,
            "max_tokens":  self.config.max_tokens,
        }
        resp = requests.post(
            self.API_URL,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type":  "application/json",
            },
            json=payload,
            timeout=self.config.timeout,
        )
        resp.raise_for_status()
        content = resp.json()["choices"][0]["message"]["content"]
        if content is None:
            raise ValueError("OpenRouter returned null content (possible content filter or empty completion)")
        return content.strip()
