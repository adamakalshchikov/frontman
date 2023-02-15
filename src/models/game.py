from enum import Enum
from typing import Optional

from aio_pika import Message
from pydantic import BaseModel, conint


class GameType(str, Enum):
    CLASSIC = "CLASSIC"
    CUSTOM = "CUSTOM"


class Game(BaseModel):
    game_type: GameType


class CreateGame(Game):
    def to_message(self) -> Message:
        return Message(str.encode(self.game_type.value))


class LaunchGame(Game):
    pass

class DestroyGame(Game):
    pass

class JoiningParticipant(BaseModel):
    nickname: Optional[str]
    position: conint(ge=1, le=10)


class AssignedParticipant(JoiningParticipant):
    role: str
