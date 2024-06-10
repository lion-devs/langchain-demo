import os
from dataclasses import dataclass


@dataclass
class AppConfig:
    llm_engine: str = os.environ.get("LLM_ENGINE")
