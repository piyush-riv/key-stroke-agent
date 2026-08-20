# KeyStroke Agent

A real-time AI coding coach that watches how a student types — keystrokes, backspaces, deletes, pauses, pastes — and steps in with a short, Socratic coaching hint when it detects the student is struggling. Built with **LangGraph**, **FastAPI/WebSockets**, a **Retrieval-Augmented Generation (RAG)** knowledge base over FAISS, and a local **Ollama** LLM, with a **Monaco Editor** frontend.

## How It Works

1. The browser editor (Monaco) captures every keypress, backspace, delete, and paste event and streams it to the backend over a WebSocket.
2. Each event is run through a **LangGraph** pipeline that updates a running `SessionState` (keystroke counts, latency between events, pause detection, backspace ratio).
3. A **struggle score** is computed from these signals.
4. If the struggle score crosses a threshold (and the coach isn't on cooldown), the agent:
   - Retrieves relevant DSA concepts from a FAISS vector store (built from local markdown notes on topics like two pointers, binary search, linked lists).
   - Sends the student's code + struggle context + retrieved knowledge to a local LLM (Llama 3.2 via Ollama).
   - Returns one short coaching hint (never a full solution) back to the browser.
5. The frontend updates live metrics (keystrokes, backspace ratio, struggle score, latency, pause) and displays the coach's suggestion when one arrives.

## Architecture

```
Browser (Monaco Editor)
      │  WebSocket (keystroke events)
      ▼
FastAPI WebSocket server (main.py)
      │
      ▼
LangGraph pipeline (graph.py / nodes.py)
  ├─ initialize_session
  ├─ process_event            (tally keystrokes/backspaces/deletes)
  ├─ calculate_latency        (time since last event)
  ├─ detect_pause             (latency > threshold)
  ├─ calculate_backspace_ratio
  ├─ calculate_struggle_score
  ├─ [conditional] route_after_struggle_score (router.py)
  │     ├─ high struggle + cooldown elapsed → RAG + coach path
  │     │     ├─ retrieve_dsa_context  (FAISS retriever)
  │     │     └─ generate_coaching_response (Ollama LLM)
  │     └─ otherwise → skip straight to update_timestamp
  └─ update_timestamp
      │
      ▼
SessionState + coach_response sent back over WebSocket
```

## Project Structure

```
.
├── main.py                 # FastAPI app + WebSocket endpoint
├── index.html               # Frontend shell (Monaco editor + metrics sidebar)
├── app.js                   # WebSocket client, keystroke capture, UI updates
├── style.css                 # Styling
│
├── app/
│   ├── EventModels/
│   │   └── events.py         # KeystrokeEvent + EventType (pydantic)
│   ├── session/
│   │   └── state.py           # SessionState (pydantic) — running per-session metrics
│   ├── agent/
│   │   ├── state.py            # KeystrokeGraphState (TypedDict) — LangGraph state
│   │   ├── nodes.py            # All pipeline node functions
│   │   ├── graph.py            # LangGraph StateGraph wiring
│   │   └── router.py           # Conditional routing / coach cooldown logic
│   ├── llm/
│   │   └── ollama.py            # get_llm() — ChatOllama wrapper (llama3.2)
│   └── rag/
│       ├── loader.py             # Loads markdown knowledge base
│       ├── chunker.py             # Header + recursive text splitting
│       ├── embeddings.py          # HuggingFace sentence-transformer embeddings
│       ├── vector_store.py         # Builds/saves FAISS index
│       └── retriever.py            # Loads FAISS index, returns retriever
│
├── knowledge/                 # DSA knowledge base (markdown)
│   ├── two_pointer.md
│   ├── binary_search.md
│   └── linked_list.md
│
├── test_state.py               # Manual test: SessionState updates
├── test_graph.py                # Manual test: full LangGraph pipeline
├── test_cooldown.py              # Manual test: coach cooldown behavior
├── test_chunker.py                # Manual test: knowledge chunking
├── test_embeddings.py              # Manual test: embedding generation
├── test_faiss.py                    # Manual test: FAISS index + retrieval
├── test_rag.py                       # Manual test: build index + retrieve
├── test_rag_llm.py                    # Manual test: retrieval + LLM response
├── test_ollama.py                      # Manual test: raw LLM call
│
├── requirements.txt
└── .gitignore
```

## Key Concepts

**Struggle Score** (`nodes.py`) — a weighted signal from three sources:
| Signal | Condition | Weight |
|---|---|---|
| Backspace ratio | `> 0.2` | +0.4 |
| Pause detected | `latency > 2.0s` | +0.3 |
| High latency | `latency > 1.0s` | +0.3 |

**Coach Cooldown** (`router.py`) — the coach only fires when struggle score `≥ 0.6` **and** either it has never spoken before or at least `10s` have passed since its last hint (`COACH_COOLDOWN`), so it doesn't spam the student.

**RAG Knowledge Base** — markdown notes on DSA patterns are split by header + recursive character splitting (`chunker.py`), embedded with `all-MiniLM-L6-v2` (`embeddings.py`), and indexed in FAISS (`vector_store.py`). The student's current code is used as the retrieval query (`retrieve_dsa_context` node) so relevant concepts (e.g. "two pointers requires a sorted array") are pulled in before the LLM responds.

## Setup

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com) installed locally, with the `llama3.2:latest` model pulled:
  ```bash
  ollama pull llama3.2:latest
  ```

### Install dependencies
```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Build the FAISS knowledge index
The vector store must be built once from the markdown files in `knowledge/`:
```bash
python test_rag.py
```
This creates the index at `app/rag/data/faiss_index/` (or wherever `VECTOR_DB_PATH` resolves).

### Run the backend
```bash
uvicorn main:app --reload
```
The WebSocket server starts at `ws://127.0.0.1:8000/ws`.

### Open the frontend
Open `index.html` in a browser (or serve it with any static file server). It connects to the WebSocket automatically and loads the Monaco editor.

## Manual Test Scripts

Each `test_*.py` script exercises one part of the system in isolation and prints results to the console — useful while developing without needing the full WebSocket loop running:

| Script | What it tests |
|---|---|
| `test_state.py` | `SessionState` updates from a sequence of keystroke events |
| `test_graph.py` | Full LangGraph pipeline on a single "struggling student" event |
| `test_cooldown.py` | Coach cooldown logic across multiple events over time |
| `test_chunker.py` | Loading + chunking the markdown knowledge base |
| `test_embeddings.py` | Embedding generation for a sample query |
| `test_faiss.py` | Building the FAISS index and running sample retrieval queries |
| `test_rag.py` | Building the index (run this first) and a single retrieval |
| `test_rag_llm.py` | Retrieval + LLM prompt + response end-to-end |
| `test_ollama.py` | Raw call to the local Ollama LLM |

## Notes

- `prompts.py` is currently empty — prompt text lives inline in `nodes.py` (`generate_coaching_response`).
- The coach is instructed to give hints, not full solutions — no complete code, max 80 words, ends with a guiding question.
- `SessionState` and the LangGraph pipeline are currently single-session (`main.py` initializes one `SessionState` per WebSocket connection).