from unittest.mock import AsyncMock
from fastapi import FastAPI
from models.game import CreateGame

base = dict()


app = FastAPI()
app.on_event("startup")
async def connect():
    # connection = await aio_pika.connect_robust("amqp://guest:guest@127.0.0.1/",)
    mock = AsyncMock()
    connection = await mock
    print("startup")
    base["mq"] = connection


@app.post("/game")
async def create_game(game: CreateGame):
    print(base)
    return "dfadf"