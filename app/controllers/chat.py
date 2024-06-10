import json
import traceback
from dataclasses import dataclass

from classy_fastapi import Routable, websocket as ws
from fastapi import WebSocket

from app.chat_llama.chat import Chat
from app.chat_llama.factory import ModelFactory, ModelType
from app.config.app import AppConfig


@dataclass
class ChatRequest:
    message: str


@dataclass
class ChatResponse:
    message: str


class ChatController(Routable):
    def __init__(self):
        super().__init__()
        # todo: use env to configure. fix env loading during init
        # print(AppConfig.llm_engine)
        # model = ModelFactory().new_model(ModelType[AppConfig.llm_engine])
        # self.chat_model = Chat(model)

        model = ModelFactory().new_model(ModelType.OPENAI)
        self.chat_model = Chat(model)

    @ws('/chat')
    async def ws(self, websocket: WebSocket):

        try:
            print("WS CONNECTION ESTABLISHED...")

            await websocket.accept()
            await websocket.send_json({"message": "What do you want to chat about?"})
            while True:
                data = await websocket.receive_text()

                human = decode_message(data)
                ai = self.chat_model.chat(human.message)

                await websocket.send_json({"message": ai})

        except Exception as e:
            print(e)
            print(traceback.format_exc())
        print("CONNECTION DEAD...")


def decode_message(msg: str) -> ChatRequest:
    json_obj = json.loads(msg)
    instance = ChatRequest(**json_obj)
    return instance


def encode_message(msg: ChatResponse) -> str:
    return json.dumps(dataclasses.asdict(msg))
