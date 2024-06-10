from __future__ import annotations

from typing import Union

from langchain.chains.conversation.base import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.language_models import (
    LanguageModelInput,
)
from langchain_core.messages import BaseMessage
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    Runnable,
)


class Chat:

    def __init__(self, model: Union[
        Runnable[LanguageModelInput, str], Runnable[LanguageModelInput, BaseMessage]
    ]):
        self.model = model

    def chat(self, message: str):
        template = """
        {history}
        Question: {input}
        """

        prompt = PromptTemplate(input_variables=["history", "input"], template=template)

        # need fix
        memory = ConversationBufferWindowMemory(k=5)
        llm_chain = ConversationChain(prompt=prompt, llm=self.model, memory=memory)

        print(memory)

        result = llm_chain.run(input=message)

        # todo: convert to stream
        return result
