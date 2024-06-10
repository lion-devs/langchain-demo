import os

from dotenv import load_dotenv
from fastapi import FastAPI

from .router import Router as BaseRouter


def bootstrap() -> FastAPI:
    load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"), verbose=True)
    fastapi = FastAPI()

    router = BaseRouter(fastapi)
    router.register_routes()

    return fastapi


app = bootstrap()
#
# @app.get("/test")
# async def test():
#     check_env("OPENAI_API_KEY")
#     model = cfg["openai"]["model"]
#
#     return openai_chat(model)
#
#
# @app.get("/afs")
# async def afs():
#
#     url = cfg["afs"]["url"]
#     model = cfg["afs"]["model"]
#     key = os.getenv("AFS_API_KEY")
#
#     return afs_chat(url, model, key)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True,
    )
