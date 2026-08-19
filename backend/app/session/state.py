from pydantic import BaseModel


class SessionState(BaseModel):
    session_id: str

    session_start_timestamp: float | None = None
    last_event_timestamp: float | None = None

    last_latency: float | None = None
    last_pause_duration: float | None = None
    pause_detected: bool = False

    total_keystrokes: int = 0
    total_backspaces: int = 0
    total_deletes: int = 0

    total_inserted_characters: int = 0
    total_deleted_characters: int = 0

    backspace_ratio: float = 0.0
    struggle_score: float = 0.0

    last_coach_timestamp: float | None = None