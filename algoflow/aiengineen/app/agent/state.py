from typing import TypedDict

from app.EventModels.events import KeystrokeEvent
from app.session.state import SessionState


class KeystrokeGraphState(TypedDict):
    event: KeystrokeEvent
    session_state: SessionState