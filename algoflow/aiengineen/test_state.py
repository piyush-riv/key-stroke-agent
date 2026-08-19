from app.EventModels.events import EventType, KeystrokeEvent
from app.session.state import SessionState
from app.agent.keystroke_agent import KeystrokeAgent


state = SessionState(
    session_id="session_001"
)

agent = KeystrokeAgent(state)


events = [

    # Student starts typing
    KeystrokeEvent(
        session_id="session_001",
        timestamp=10.0,
        event_type=EventType.KEYPRESS,
        character_count=1
    ),

    KeystrokeEvent(
        session_id="session_001",
        timestamp=10.2,
        event_type=EventType.KEYPRESS,
        character_count=1
    ),

    KeystrokeEvent(
        session_id="session_001",
        timestamp=10.4,
        event_type=EventType.KEYPRESS,
        character_count=1
    ),

    # Student makes corrections
    KeystrokeEvent(
        session_id="session_001",
        timestamp=10.6,
        event_type=EventType.BACKSPACE,
        character_count=1
    ),

    KeystrokeEvent(
        session_id="session_001",
        timestamp=10.8,
        event_type=EventType.BACKSPACE,
        character_count=1
    ),

    # Student pauses for 3 seconds
    KeystrokeEvent(
        session_id="session_001",
        timestamp=13.8,
        event_type=EventType.KEYPRESS,
        character_count=1
    ),
]


for event in events:
    agent.process_event(event)


print(state)