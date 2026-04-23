"""Minimal OpenRouter client for the document benchmark."""

from __future__ import annotations

from typing import Any

import requests


class OpenRouterClient:
    def __init__(
        self,
        *,
        api_key: str,
        model: str,
        base_url: str = "https://openrouter.ai/api/v1/chat/completions",
        app_name: str = "docs_benchmark",
    ) -> None:
        self.api_key = api_key
        self.model = model
        self.base_url = base_url
        self.app_name = app_name

    def _extract_text(self, payload: dict[str, Any]) -> str:
        choices = payload.get("choices") or []
        if not choices:
            raise ValueError("OpenRouter response did not include any choices")

        message = choices[0].get("message") or {}
        content = message.get("content", "")
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            parts: list[str] = []
            for item in content:
                if isinstance(item, dict) and item.get("type") == "text":
                    parts.append(str(item.get("text", "")))
            return "\n".join(part for part in parts if part).strip()
        raise ValueError("OpenRouter response content had an unsupported shape")

    def complete(
        self,
        prompt: str,
        *,
        temperature: float = 0.0,
        max_tokens: int = 8192,
        timeout: int = 180,
    ) -> tuple[str, dict[str, Any]]:
        response = requests.post(
            self.base_url,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "X-Title": self.app_name,
            },
            json={
                "model": self.model,
                "temperature": temperature,
                "max_tokens": max_tokens,
                "messages": [{"role": "user", "content": prompt}],
            },
            timeout=timeout,
        )
        response.raise_for_status()
        payload = response.json()
        return self._extract_text(payload), payload
