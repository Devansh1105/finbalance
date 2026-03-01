"""Base interface for all LLM backends."""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class ModelConfig:
    model_id:    str
    temperature: float = 0.0
    seed:        int   = 42
    max_tokens:  int   = 2048
    timeout:     int   = 60


class BaseModel(ABC):
    def __init__(self, config: ModelConfig):
        self.config = config

    @abstractmethod
    def complete(self, prompt: str) -> str:
        """Send a prompt and return the raw text response."""
        ...

    def __repr__(self):
        return f"{self.__class__.__name__}({self.config.model_id})"
