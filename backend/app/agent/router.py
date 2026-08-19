STRUGGLE_THRESHOLD = 0.6
COACH_COOLDOWN = 10.0


def route_after_struggle_score(state):

    session = state["session_state"]
    event = state["event"]

    if session.struggle_score < STRUGGLE_THRESHOLD:
        return "update_timestamp"

    if session.last_coach_timestamp is None:
        return "rag_coach"

    elapsed = event.timestamp - session.last_coach_timestamp

    if elapsed >= COACH_COOLDOWN:
        return "rag_coach"

    return "update_timestamp"