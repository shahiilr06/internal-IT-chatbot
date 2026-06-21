# Copilot Instructions

## Build, test, and run
- Docker (recommended): `docker compose up --build` (UI on :3000, API on :8000).
- Local (all-in-one): `./start.sh` (builds Tailwind CSS, then runs FastAPI + Node).
- Local (manual):
  - Backend: `pip install -r requirements.txt`, `python ingest.py` (first run), `python app.py`
  - Frontend: `cd frontend && npm install && npm run build:css && node server.js`
- Tests:
  - Full suite: `pytest tests/`
  - Single test: `pytest tests/test_backend.py::test_chat_endpoint_no_data`

## High-level architecture
- `ingest.py` loads PDFs from `rag/`, splits into chunks, embeds with `all-MiniLM-L6-v2`, and saves a FAISS index to `vectorstore/`.
- `app.py` (FastAPI) loads the FAISS index on startup, builds a LangChain retriever + SmolLM2 pipeline, and serves `/chat` that invokes the RAG chain and post-processes the model output.
- `frontend/server.js` is a small Express static server that serves the ChatGPT-style UI from `frontend/public` (Tailwind output at `public/output.css`).
- `start.sh` orchestrates backend + frontend locally; Dockerfile builds the Tailwind CSS during image build; `docker-compose.yml` mounts `rag/`, `vectorstore/`, and the Hugging Face cache volume.

## Key conventions
- The backend expects the FAISS index at `vectorstore/`; if it’s missing, `/chat` returns a 503. Run `python ingest.py` after updating PDFs in `rag/`.
- FAISS loading uses `allow_dangerous_deserialization=True`; keep this if you refactor vectorstore loading.
- Model loading uses `device_map="auto"` with `torch.cuda.is_available()` to pick GPU vs CPU, and sets generation config explicitly in `app.py` (max tokens/length/temperature).
- The system prompt enforces a strict “use context only” policy with a fixed fallback string; preserve this behavior when editing prompts.
- Frontend UI changes require rebuilding Tailwind CSS (`npm run build:css`); `start.sh`/Dockerfile already do this.
