# Multi-PDF Internal IT Assistant

This project is a Retrieval-Augmented Generation (RAG) system designed to serve as an internal IT assistant. It leverages multiple company documentation files to provide accurate and context-aware support through a sleek ChatGPT-clone interface.

## Tech Stack
- **Frontend:** Node.js (Express) + Tailwind CSS (ChatGPT Clone UI).
- **Backend:** FastAPI (Python) - REST API.
- **Orchestration:** LangChain.
- **LLM:** SmolLM2-1.7B-Instruct (Lightweight & Fast).
- **Embeddings:** all-MiniLM-L6-v2.
- **Vector Store:** FAISS.

## CI/CD Pipeline
This project includes a professional **GitHub Actions** CI/CD pipeline defined in `.github/workflows/main.yml`.

### What the Pipeline Does:
1.  **Backend CI:** Sets up Python 3.11, installs dependencies, and runs automated tests using `pytest`.
2.  **Frontend CI:** Sets up Node.js 20, installs dependencies, and validates the frontend build.
3.  **Docker Build Check:** Ensures that the unified `Dockerfile` can build successfully.

---

## MASTER GUIDE: How to Run the Project

### Option 1: The Docker Way (Recommended)
This is the fastest way to run the entire app with one command. It uses a single container that runs both the Python API and Node.js UI.
```bash
docker compose up --build
```
*   **Frontend Chat UI:** http://localhost:3000
*   **Backend API:** http://localhost:8000

### Option 2: The Developer Way (Local Run)

**1. Data Ingestion (First time only):**
```bash
python ingest.py
```

**2. Start Both Services via Script:**
```bash
./start.sh
```
*(This starts both the backend and frontend simultaneously in your local environment)*

### Option 3: Automated Testing
To run the automated test suite locally:
```bash
pytest tests/
```

## Project Structure
- `app.py`: FastAPI Backend (API)
- `ingest.py`: Data Ingestion & FAISS Creation
- `frontend/`: Node.js Frontend (ChatGPT UI)
- `start.sh`: Bash script to execute both frontend and backend
- `.github/workflows/`: CI/CD Pipeline Configuration
- `tests/`: Automated Python Test Suite
- `rag/`: Source PDFs
- `vectorstore/`: Persistent Vector Database
- `docker-compose.yml`: Master orchestration file
- `Dockerfile`: Unified container configuration
