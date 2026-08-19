from app.agent.state import KeystrokeGraphState


STRUGGLE_THRESHOLD = 0.6


def route_after_struggle_score(state: KeystrokeGraphState):

    session = state["session_state"]

    if session.struggle_score >= STRUGGLE_THRESHOLD:
        return "update_timestamp"

    return "update_timestamp"