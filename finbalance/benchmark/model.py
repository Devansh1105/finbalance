"""Minimal OpenRouter client for the document benchmark."""

from __future__ import annotations

import shutil
import subprocess
import time
from typing import Any

import requests

GCLOUD_TOKEN_SENTINEL = "gcloud"
_GCLOUD_TOKEN_TTL_SECONDS = 45 * 60


class _GcloudTokenProvider:
    """Bearer tokens for Vertex AI via `gcloud auth print-access-token`.

    Access tokens expire after ~1 hour; we cache for 45 minutes and refresh
    eagerly so multi-hour benchmark runs never send a stale token.
    """

    def __init__(self) -> None:
        self._token: str | None = None
        self._fetched_at = 0.0

    def token(self, *, force_refresh: bool = False) -> str:
        if (
            not force_refresh
            and self._token
            and time.monotonic() - self._fetched_at < _GCLOUD_TOKEN_TTL_SECONDS
        ):
            return self._token
        gcloud = shutil.which("gcloud") or f"{subprocess.os.path.expanduser('~')}/google-cloud-sdk/bin/gcloud"
        result = subprocess.run(
            [gcloud, "auth", "print-access-token"],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if result.returncode != 0:
            raise RuntimeError(f"gcloud auth print-access-token failed: {result.stderr.strip()[:300]}")
        self._token = result.stdout.strip()
        self._fetched_at = time.monotonic()
        return self._token


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
        self._gcloud_tokens = _GcloudTokenProvider() if api_key == GCLOUD_TOKEN_SENTINEL else None

    def _bearer_token(self, *, force_refresh: bool = False) -> str:
        if self._gcloud_tokens is not None:
            return self._gcloud_tokens.token(force_refresh=force_refresh)
        return self.api_key

    def _extract_text(self, payload: dict[str, Any]) -> str:
        choices = payload.get("choices") or []
        if not choices:
            raise ValueError("OpenRouter response did not include any choices")

        message = choices[0].get("message") or {}
        content = message.get("content", "")
        if content is None and message.get("tool_calls"):
            return ""
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
        tools: list[dict[str, Any]] | None = None,
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
                if tools:
                    request_json["tools"] = tools
                if self.reasoning_effort:
                    if "aiplatform.googleapis.com" in self.base_url:
                        # Vertex's OpenAI-compat layer takes the OpenAI-style field;
                        # "minimal" is the documented thinking-off approximation and
                        # measurably yields 0 reasoning tokens on Gemini 3 Flash.
                        request_json["reasoning_effort"] = self.reasoning_effort
                    else:
                        request_json["reasoning"] = {"effort": self.reasoning_effort}

                response = requests.post(
                    self.base_url,
                    headers={
                        "Authorization": f"Bearer {self._bearer_token()}",
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

            if response.status_code == 401 and self._gcloud_tokens is not None and attempt < self.max_retries:
                self._bearer_token(force_refresh=True)
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
