import os

from dotenv import load_dotenv
from fastapi import FastAPI

from config.config import config_loader
from handlers.afs import afs_chat
from handlers.openai import openai_chat

# Load configuration
cfg = config_loader()

# Load environment variables
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
    response = openai_chat()

    return response

