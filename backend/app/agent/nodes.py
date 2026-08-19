from app.EventModels.events import EventType
from app.agent.state import KeystrokeGraphState
from app.rag.retriever import get_retriever
from app.llm.ollama import get_llm


# ==========================================
# Thresholds
# ==========================================

PAUSE_THRESHOLD = 2.0
LATENCY_THRESHOLD = 1.0
BACKSPACE_RATIO_THRESHOLD = 0.2


# ==========================================
# Node 1: Initialize session
# ==========================================

def initialize_session(state: KeystrokeGraphState):

    session = state["session_state"]
    event = state["event"]

    if session.session_start_timestamp is None:
        session.session_start_timestamp = event.timestamp

    return {
        "session_state": session
    }


# ==========================================
# Node 2: Process event
# ==========================================

def process_event(state: KeystrokeGraphState):

    session = state["session_state"]
    event = state["event"]

    if event.event_type == EventType.KEYPRESS:

        session.total_keystrokes += 1
        session.total_inserted_characters += event.character_count

    elif event.event_type == EventType.BACKSPACE:

        session.total_backspaces += 1
        session.total_deleted_characters += event.character_count

    elif event.event_type == EventType.DELETE:

        session.total_deletes += 1
        session.total_deleted_characters += event.character_count

    elif event.event_type == EventType.PASTE:

        session.total_inserted_characters += event.character_count

    return {
        "session_state": session
    }


# ==========================================
# Node 3: Calculate latency
# ==========================================

def calculate_latency(state: KeystrokeGraphState):

    session = state["session_state"]
    event = state["event"]

    if session.last_event_timestamp is not None:

        latency = (
            event.timestamp
            - session.last_event_timestamp
        )

        session.last_latency = latency

    return {
        "session_state": session
    }


# ==========================================
# Node 4: Detect pause
# ==========================================

def detect_pause(state: KeystrokeGraphState):

    session = state["session_state"]

    if (
        session.last_latency is not None
        and session.last_latency > PAUSE_THRESHOLD
    ):

        session.pause_detected = True
        session.last_pause_duration = session.last_latency

    else:

        session.pause_detected = False
        session.last_pause_duration = None

    return {
        "session_state": session
    }


# ==========================================
# Node 5: Calculate backspace ratio
# ==========================================

def calculate_backspace_ratio(state: KeystrokeGraphState):

    session = state["session_state"]

    if session.total_keystrokes > 0:

        session.backspace_ratio = (
            session.total_backspaces
            / session.total_keystrokes
        )

    return {
        "session_state": session
    }


# ==========================================
# Node 6: Calculate struggle score
# ==========================================

def calculate_struggle_score(state: KeystrokeGraphState):

    session = state["session_state"]

    score = 0.0

    if session.backspace_ratio > BACKSPACE_RATIO_THRESHOLD:
        score += 0.4

    if session.pause_detected:
        score += 0.3

    if (
        session.last_latency is not None
        and session.last_latency > LATENCY_THRESHOLD
    ):
        score += 0.3

    session.struggle_score = min(score, 1.0)

    return {
        "session_state": session
    }


# ==========================================
# Node 7: Update timestamp
# ==========================================

def update_timestamp(state: KeystrokeGraphState):

    session = state["session_state"]
    event = state["event"]

    session.last_event_timestamp = event.timestamp

    return {
        "session_state": session
    }

# ==========================================
# Node 8: Retrieve DSA context
# ==========================================

def retrieve_dsa_context(state: KeystrokeGraphState):

    event = state["event"]
    session = state["session_state"]

    # Use the student's current code as the main retrieval query.
    code = event.code

    query = f"""
    Programming language: {event.language}

    Student's current code:
    {code}

    Find relevant DSA concepts, algorithms, patterns,
    common mistakes, and better approaches for this code.
    """

    retriever = get_retriever()

    results = retriever.invoke(query)

    context = [
        document.page_content
        for document in results
    ]

    return {
        "retrieved_context": context
    }

# ==========================================
# Node 9: Generate coaching response
# ==========================================

def generate_coaching_response(state: KeystrokeGraphState):

    event = state["event"]
    session = state["session_state"]

    context = "\n\n".join(
        state.get("retrieved_context", [])
    )

    prompt = f"""
    You are a real-time DSA coding coach inside a code editor.

    STUDENT CODE:
    {event.code}

    LANGUAGE:
    {event.language}

    STRUGGLE SCORE:
    {session.struggle_score}

    RETRIEVED KNOWLEDGE:
    {context}

    Your job is to give the student ONE short, useful coaching hint.

    STRICT OUTPUT RULES:
    - Maximum 80 words.
    - Do NOT use headings.
    - Do NOT repeat the retrieved knowledge.
    - Do NOT explain the entire algorithm.
    - Do NOT provide the complete solution.
    - Do NOT use markdown tables.
    - Do NOT start with phrases like "Based on the student's code".
    - Do NOT say "The student".
    - Speak directly to the student using "you".
    - Give only one main idea.
    - End with one short question that makes the student think.
    - Never assume an array is sorted unless the code or problem explicitly establishes it.
    - If an approach has an important prerequisite, mention it briefly.

    If the current approach is inefficient, point out the possible direction
    without writing the complete replacement code.

    Return ONLY the coaching message.
    """

    llm = get_llm()

    response = llm.invoke(prompt)

    session.last_coach_timestamp = event.timestamp

    return {
        "coach_response": response.content,
        "session_state": session
    }