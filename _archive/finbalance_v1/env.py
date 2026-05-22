"""Project-local environment loading helpers."""

from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv


@lru_cache(maxsize=1)
def load_project_env() -> None:
    """Load the repo-local .env file once if present."""
    repo_root = Path(__file__).resolve().parents[1]
    load_dotenv(repo_root / ".env")
