import os
from dataclasses import dataclass, field
from typing import List


@dataclass
class AFSParams:
    max_new_tokens: int = 100
    temperature: float = 0.5
    top_p: float = 1.0
    top_k: int = 50
    frequency_penalty: int = 1
    stop_sequences: List[str] = field(default_factory=lambda: ["stop"])
    show_probabilities: bool = False
    seed: int = 0


@dataclass
class AfsConfig:
    url: str = "https://api-ams.twcc.ai/api"
    model: str = "ffm-mixtral-8x7b-32k-instruct"
    question: str = "question: What is your name?"
    api_key: str = os.environ.get("AFS_API_KEY")
    params: AFSParams = field(default_factory=AFSParams)
