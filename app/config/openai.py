import os
from dataclasses import dataclass


@dataclass
class OpenAIConfig:
    model: str = "gpt-3.5-turbo"
    api_key: str = os.environ.get("OPENAI_API_KEY")
