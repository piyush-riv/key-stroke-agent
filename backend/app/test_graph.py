from app.agent.graph import keystroke_graph
from app.agent.state import KeystrokeGraphState
from app.EventModels.events import KeystrokeEvent, EventType
from app.session.state import SessionState


# ------------------------------------------
# Simulate a student who is struggling
# ------------------------------------------

event = KeystrokeEvent(
    session_id="test-session",
    timestamp=10.0,
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


session = SessionState(
    session_id="test-session",

    # Simulate previous activity
    session_start_timestamp=0.0,
    last_event_timestamp=7.0,

    # 10 - 7 = 3 seconds → pause
    last_latency=3.0,

    pause_detected=True,
    last_pause_duration=3.0,

    # 1 backspace / 2 keystrokes = 0.5
    total_keystrokes=2,
    total_backspaces=1,

    backspace_ratio=0.5,
)


initial_state: KeystrokeGraphState = {
    "event": event,
    "session_state": session,

    # Initial values for RAG/LLM
    "retrieved_context": [],
    "coach_response": "",
}


print("\n" + "=" * 70)
print("STARTING LANGGRAPH TEST")
print("=" * 70)


result = keystroke_graph.invoke(initial_state)


print("\n" + "=" * 70)
print("GRAPH FINISHED")
print("=" * 70)


print("\nStruggle Score:")
print(result["session_state"].struggle_score)


print("\nRetrieved Context:")
for i, context in enumerate(
    result.get("retrieved_context", []),
    start=1
):
    print(f"\n--- Context {i} ---")
    print(context)


print("\n" + "=" * 70)
print("COACH RESPONSE")
print("=" * 70)

print(result.get("coach_response", "No response generated"))