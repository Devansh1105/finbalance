"""Minimal OpenRouter client for the document benchmark."""

from __future__ import annotations

import time
from typing import Any

import requests


class OpenRouterRequestError(RuntimeError):
    """HTTP failure returned by OpenRouter with a compact response body."""

    def __init__(self, status_code: int, body: str) -> None:
        self.status_code = int(status_code)
        self.body = body[:1000]
        super().__init__(f"OpenRouter request failed with status {self.status_code}: {self.body}")


class OpenRouterClient:
    def __init__(
        self,
        *,
        api_key: str,
        model: str,
        base_url: str = "https://openrouter.ai/api/v1/chat/completions",
        app_name: str = "finbalance",
        max_retries: int = 3,
        retry_backoff_seconds: float = 5.0,
        reasoning_effort: str | None = None,
    ) -> None:
        self.api_key = api_key
        self.model = model
        self.base_url = base_url
        self.app_name = app_name
        self.max_retries = int(max_retries)
        self.retry_backoff_seconds = float(retry_backoff_seconds)
        self.reasoning_effort = reasoning_effort

    def _extract_text(self, payload: dict[str, Any]) -> str:
        choices = payload.get("choices") or []
        if not choices:
            raise ValueError("OpenRouter response did not include any choices")

        message = choices[0].get("message") or {}
        content = message.get("content", "")
        if isinstance(content, str):
            return content
        if isinstance(content, dict):
            for key in ("text", "content", "output_text"):
                value = content.get(key)
                if isinstance(value, str):
                    return value
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
        return self.complete_messages(
            [{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
            timeout=timeout,
        )

    def complete_messages(
        self,
        messages: list[dict[str, str]],
        *,
        temperature: float = 0.0,
        max_tokens: int = 8192,
        timeout: int = 180,
    ) -> tuple[str, dict[str, Any]]:
        attempt = 0
        while True:
            try:
                request_json: dict[str, Any] = {
                    "model": self.model,
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                    "messages": messages,
                }
                if self.reasoning_effort:
                    request_json["reasoning"] = {"effort": self.reasoning_effort}

                response = requests.post(
                    self.base_url,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                        "X-Title": self.app_name,
                    },
                    json=request_json,
                    timeout=timeout,
                )
            except (requests.ConnectionError, requests.Timeout):
                if attempt >= self.max_retries:
                    raise
                self._sleep_before_retry(attempt)
                attempt += 1
                continue

            if response.status_code in {429, 500, 502, 503, 504} and attempt < self.max_retries:
                self._sleep_before_retry(attempt, response=response)
                attempt += 1
                continue

            if not response.ok:
                raise OpenRouterRequestError(response.status_code, response.text)

            payload = response.json()
            return self._extract_text(payload), payload

    def _sleep_before_retry(self, attempt: int, *, response: requests.Response | None = None) -> None:
        retry_after = response.headers.get("Retry-After") if response is not None else None
        if retry_after:
            try:
                delay = float(retry_after)
            except ValueError:
                delay = self.retry_backoff_seconds * (2**attempt)
        else:
            delay = self.retry_backoff_seconds * (2**attempt)
        time.sleep(delay)
