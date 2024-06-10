from __future__ import annotations

from enum import Enum
from typing import Union

from langchain_community.chat_models import ChatOllama
from langchain_core.language_models import (
    LanguageModelInput,
)
from langchain_core.messages import BaseMessage
from langchain_core.runnables import (
    Runnable,
)
from langchain_openai import ChatOpenAI

from app.config.afs import AfsConfig
from app.config.openai import OpenAIConfig
from app.chat_llama.afs import ChatFormosaFoundationModel


class ModelType(Enum):
    # Engine types
    OPENAI = "openai"
    AFS = "afs"
    OLLAMA = "ollama"


class ModelFactory:
    def new_model(self, name: ModelType) -> Union[
        Runnable[LanguageModelInput, str], Runnable[LanguageModelInput, BaseMessage]
    ]:
        if name == ModelType.AFS:
            return ChatFormosaFoundationModel(
                base_url=AfsConfig.url,
                max_new_tokens=350,
                temperature=0.5,
                top_k=50,
                top_p=1.0,
                frequence_penalty=1.0,
                ffm_api_key=AfsConfig.api_key,
                model=AfsConfig.model
            )
        elif name == ModelType.OPENAI:
            return ChatOpenAI(model=OpenAIConfig.model, api_key=OpenAIConfig.api_key)
        elif name == ModelType.OLLAMA:
            return ChatOllama(model="llama3")
