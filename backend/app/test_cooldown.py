from app.agent.graph import keystroke_graph
from app.agent.state import KeystrokeGraphState
from app.EventModels.events import KeystrokeEvent, EventType
from app.session.state import SessionState


def create_event(timestamp):
    return KeystrokeEvent(
        session_id="cooldown-test",
        timestamp=timestamp,
        event_type=EventType.BACKSPACE,
        character_count=1,
        code="""
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
""",
        language="python",
    )


# ------------------------------------------
# Initial session
# ------------------------------------------

state: KeystrokeGraphState = {
    "event": create_event(10.0),

    "session_state": SessionState(
        session_id="cooldown-test",
        session_start_timestamp=0.0,
        last_event_timestamp=7.0,
        last_latency=3.0,
        pause_detected=True,
        last_pause_duration=3.0,
        total_keystrokes=2,
        total_backspaces=1,
        backspace_ratio=0.5,
    ),

    "retrieved_context": [],
    "coach_response": "",
}


# ==========================================
# EVENT 1
# ==========================================

print("\n" + "=" * 70)
print("EVENT 1 — FIRST STRUGGLE")
print("=" * 70)

result = keystroke_graph.invoke(state)

print("Struggle score:", result["session_state"].struggle_score)
print(
    "Last coach timestamp:",
    result["session_state"].last_coach_timestamp
)
print(
    "Coach response generated:",
    bool(result.get("coach_response"))
)


# Keep the updated session state
state["session_state"] = result["session_state"]


# ==========================================
# EVENT 2 — 2 seconds later
# ==========================================

state["event"] = create_event(12.0)

print("\n" + "=" * 70)
print("EVENT 2 — 2 SECONDS LATER")
print("=" * 70)

result = keystroke_graph.invoke(state)

print("Struggle score:", result["session_state"].struggle_score)
print(
    "Last coach timestamp:",
    result["session_state"].last_coach_timestamp
)
print(
    "Coach response generated:",
    bool(result.get("coach_response"))
)


state["session_state"] = result["session_state"]


# ==========================================
# EVENT 3 — 11 seconds after first response
# ==========================================

state["event"] = create_event(21.0)

print("\n" + "=" * 70)
print("EVENT 3 — 11 SECONDS AFTER FIRST RESPONSE")
print("=" * 70)

result = keystroke_graph.invoke(state)

print("Struggle score:", result["session_state"].struggle_score)
print(
    "Last coach timestamp:",
    result["session_state"].last_coach_timestamp
)
print(
    "Coach response generated:",
    bool(result.get("coach_response"))
)