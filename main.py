import getpass
import os

from dotenv import load_dotenv
from fastapi import FastAPI

from config.config import config_loader
from handlers.afs import afs_chat
from handlers.openai import openai_chat
from tools.check import check_env

# Load configuration
cfg = config_loader()

# Load environment variables from .env
load_dotenv()
check_env("LANGCHAIN_API_KEY")

app = FastAPI(
    title="LangChain Demo",
    description="A simple demo for LangChain",
    version="0.0.1",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/test")
async def test():
    check_env("OPENAI_API_KEY")
    model = cfg["openai"]["model"]

    return openai_chat(model)


@app.get("/afs")
async def afs():
    if not os.environ.get("AFS_API_KEY"):
        os.environ["AFS_API_KEY"] = getpass.getpass()

    url = cfg["afs"]["url"]
    model = cfg["afs"]["model"]
    key = os.getenv("AFS_API_KEY")

    return afs_chat(url, model, key)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True,
    )
