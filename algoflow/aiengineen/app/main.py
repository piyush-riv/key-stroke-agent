from fastapi import FastAPI, WebSocket, WebSocketDisconnect

from app.EventModels.events import KeystrokeEvent
from app.session.state import SessionState
from app.agent.graph import keystroke_graph

app = FastAPI()


@app.get("/")
async def root():
    return {
        "status": "running",
        "agent": "LangGraph Keystroke Agent"
    }


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    print("WebSocket connection request received")

    await websocket.accept()

    print("WebSocket connection accepted")

    # Create one session state for this WebSocket connection
    state = SessionState(
        session_id="session_001"
    )

    try:

        while True:

            # Receive JSON event from frontend
            data = await websocket.receive_json()

            print("Received:", data)

            # Validate JSON using Pydantic
            event = KeystrokeEvent(**data)

            # Run the complete LangGraph agent
            result = keystroke_graph.invoke({
                "event": event,
                "session_state": state
            })

            # Get updated session state from graph
            state = result["session_state"]

            # Send updated metrics back to frontend
            await websocket.send_json(
                state.model_dump()
            )

    except WebSocketDisconnect:

        print("WebSocket disconnected")

    except Exception as e:

        print("WebSocket error:", e)