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

    state = SessionState(
        session_id="session_001"
    )

    try:

        while True:

            data = await websocket.receive_json()

            print("Received:", data)

            event = KeystrokeEvent(**data)

            result = keystroke_graph.invoke({
                "event": event,
                "session_state": state,
                "retrieved_context": [],
                "coach_response": ""
            })

            state = result["session_state"]

            await websocket.send_json({
                **result["session_state"].model_dump(),
                "coach_response": result.get("coach_response", "")
            })

    except WebSocketDisconnect:

        print("WebSocket disconnected")

    except Exception as e:

        print("WebSocket error:", e)