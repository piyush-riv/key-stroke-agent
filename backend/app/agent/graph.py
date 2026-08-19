from langgraph.graph import StateGraph, END

from app.agent.state import KeystrokeGraphState

from app.agent.nodes import (
    initialize_session,
    process_event,
    calculate_latency,
    detect_pause,
    calculate_backspace_ratio,
    calculate_struggle_score,
    retrieve_dsa_context,
    generate_coaching_response,
    update_timestamp
)

from app.agent.router import route_after_struggle_score


workflow = StateGraph(KeystrokeGraphState)


workflow.add_node(
    "initialize_session",
    initialize_session
)

workflow.add_node(
    "process_event",
    process_event
)

workflow.add_node(
    "calculate_latency",
    calculate_latency
)

workflow.add_node(
    "detect_pause",
    detect_pause
)

workflow.add_node(
    "calculate_backspace_ratio",
    calculate_backspace_ratio
)

workflow.add_node(
    "calculate_struggle_score",
    calculate_struggle_score
)

workflow.add_node(
    "retrieve_dsa_context",
    retrieve_dsa_context
)

workflow.add_node(
    "generate_coaching_response",
    generate_coaching_response
)

workflow.add_node(
    "update_timestamp",
    update_timestamp
)


workflow.set_entry_point("initialize_session")


workflow.add_edge(
    "initialize_session",
    "process_event"
)

workflow.add_edge(
    "process_event",
    "calculate_latency"
)

workflow.add_edge(
    "calculate_latency",
    "detect_pause"
)

workflow.add_edge(
    "detect_pause",
    "calculate_backspace_ratio"
)

workflow.add_edge(
    "calculate_backspace_ratio",
    "calculate_struggle_score"
)


workflow.add_conditional_edges(
    "calculate_struggle_score",
    route_after_struggle_score,
    {
        "update_timestamp": "update_timestamp",
        "rag_coach": "retrieve_dsa_context"
    }
)

workflow.add_edge(
    "retrieve_dsa_context",
    "generate_coaching_response"
)

workflow.add_edge(
    "generate_coaching_response",
    "update_timestamp"
)


workflow.add_edge(
    "update_timestamp",
    END
)


keystroke_graph = workflow.compile()