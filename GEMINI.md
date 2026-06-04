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
3.  **Docker Build Check:** Ensures that both `backend.Dockerfile` and `frontend.Dockerfile` can build successfully.

---

## MASTER GUIDE: How to Run the Project

### Option 1: The Docker Way (Recommended)
This is the fastest way to run the entire app with one command.
```bash
docker-compose up --build
```
*   **Backend:** http://localhost:8000
*   **Frontend:** http://localhost:3000

### Option 2: The Developer Way (Local Run)

**1. Data Ingestion (First time only):**
```bash
python ingest.py
```

**2. Start Backend:**
```bash
python app.py
```

**3. Start Frontend:**
```bash
cd frontend
npm install
node server.js
```

### Option 3: Automated Testing
To run the automated test suite locally:
```bash
pytest tests/
```

## Project Structure
- `app.py`: FastAPI Backend (API)
- `ingest.py`: Data Ingestion & FAISS Creation
- `frontend/`: Node.js Frontend (ChatGPT UI)
- `.github/workflows/`: CI/CD Pipeline Configuration
- `tests/`: Automated Python Test Suite
- `rag/`: Source PDFs
- `vectorstore/`: Persistent Vector Database
- `docker-compose.yml`: Master orchestration file
