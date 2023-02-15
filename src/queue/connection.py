import aio_pika
from unittest.mock import AsyncMock

async def connect():
    # connection = await aio_pika.connect_robust("amqp://guest:guest@127.0.0.1/",)
    mock = AsyncMock()
    connection = await mock
    return connection
