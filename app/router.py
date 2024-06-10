from typing import Type

from classy_fastapi import Routable
from fastapi import FastAPI

from app.controllers.chat import ChatController


class Router:
    controllers: list[Type[Routable]] = [
        ChatController
    ]

    def __init__(self, fastapi: FastAPI) -> None:
        self.fastapi = fastapi

    def register_routes(self) -> None:
        for controller in self.controllers:
            instance = controller()
            self.fastapi.include_router(instance.router)
