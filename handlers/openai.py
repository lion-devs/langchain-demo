from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


def openai_chat():
    """
    Get the answer from LLM model using chatgpt.
    """

    model = ChatOpenAI(model="gpt-3.5-turbo")

    system_template = "Translate the following into {language}:"

    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )

    parser = StrOutputParser()
    chain = prompt_template | model | parser

    return chain.invoke({"language": "italian", "text": "hi"})
