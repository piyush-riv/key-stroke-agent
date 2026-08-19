from enum import Enum
from pydantic import BaseModel


class EventType(str, Enum):
    KEYPRESS = "keypress"
    BACKSPACE = "backspace"
    DELETE = "delete"
    PASTE = "paste"


class KeystrokeEvent(BaseModel):

    session_id: str

    timestamp: float

    event_type: EventType

    character_count: int

    code: str = ""

    language: str = "python"