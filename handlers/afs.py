from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

from models.afs import ChatFormosaFoundationModel


def afs_chat(url: str, model: str, key: str):
    """
    Get the answer from LLM model using langchain.
    """

    model = ChatFormosaFoundationModel(
        base_url=url,
        max_new_tokens=350,
        temperature=0.5,
        top_k=50,
        top_p=1.0,
        frequence_penalty=1.0,
        ffm_api_key=key,
        model=model
    )

    # system_template = "Translate the following into {language}:"
    #
    # prompt_template = ChatPromptTemplate.from_messages(
    #     [("system", system_template), ("user", "{text}")]
    # )

    messages = [
        HumanMessage(content="人口最多的國家是?"),
        AIMessage(content="人口最多的國家是印度。"),
        HumanMessage(content="主要宗教為?")
    ]

    parser = StrOutputParser()
    chain = model | parser

    return chain.invoke(messages)
