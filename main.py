import os

from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

LC_API_KEY = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/test")
async def test():
    model = ChatOpenAI(model="gpt-3.5-turbo")
    messages = [
        SystemMessage(content="Translate the following from English into Italian"),
        HumanMessage(content="hi!"),
    ]

    # result = model.invoke(messages)
    #
    # # parse the output
    parser = StrOutputParser()
    # parser.invoke(result)

    chain = model | parser

    return chain.invoke(messages)
