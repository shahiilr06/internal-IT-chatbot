# 🤖 Nexira Multi-PDF IT Assistant (ChatGPT Clone)

[![CI/CD Pipeline](https://github.com/your-username/nexira-it-assistant/actions/workflows/main.yml/badge.svg)](https://github.com/your-username/nexira-it-assistant/actions)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Node.js](https://img.shields.io/badge/Frontend-Node.js-339933?logo=node.js)](https://nodejs.org/)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker)](https://www.docker.com/)

A sophisticated **Retrieval-Augmented Generation (RAG)** system designed to serve as an internal IT assistant. This project features a high-performance Python backend and a sleek Node.js frontend that perfectly mimics the **ChatGPT user interface**.

---

## 🌟 Key Features

- **📄 Multi-PDF Support:** Automatically ingests and indexes IT documentation from multiple sources (Google, Aura, Nexira, Vanguard, etc.).
- **🧠 Advanced Reasoning:** Uses **Chain of Thought (CoT)** prompting to ensure accurate, step-by-step technical support.
- **🎨 ChatGPT UI Clone:** A beautiful, responsive frontend built with Tailwind CSS, featuring dark mode, a sidebar, and markdown rendering.
- **🚀 Lightweight & Fast:** Powered by **SmolLM2-1.7B-Instruct**, providing rapid inference with minimal resource usage.
- **🐳 Dockerized Architecture:** Run the entire stack (API + UI) with a single command using Docker Compose.
- **🤖 Factual Lockdown:** Custom-engineered system prompts to prevent AI hallucinations and stick strictly to internal documentation.
- **✅ CI/CD Ready:** Automated testing and build validation via GitHub Actions.

---

## 🛠️ Tech Stack

### Backend (AI & API)
- **FastAPI:** High-performance REST API.
- **LangChain:** RAG orchestration and chain management.
- **Hugging Face:** LLM loading and inference.
- **FAISS:** High-speed vector similarity search.
- **Sentence Transformers:** Deep learning embeddings (`all-MiniLM-L6-v2`).

### Frontend (UI)
- **Node.js & Express:** Production-grade web server.
- **Tailwind CSS:** Modern utility-first styling for the ChatGPT aesthetic.
- **Marked.js:** Perfect rendering of AI-generated Markdown.

---

## 🚦 Getting Started

### Prerequisites
- [Docker](https://www.docker.com/get-started) & [Docker Compose](https://docs.docker.com/compose/install/)
- (Optional for Local) Python 3.11+ & Node.js 20+

### Option 1: The Docker Way (Recommended)
The easiest way to deploy the entire system:
```bash
docker-compose up --build
```
- **Web UI:** [http://localhost:3000](http://localhost:3000)
- **API Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

### Option 2: The Developer Way (Local)

**1. Clone the repository:**
```bash
git clone https://github.com/your-username/internal-it-assistant.git
cd internal-it-assistant
```

**2. Setup Backend:**
```bash
pip install -r requirements.txt
python ingest.py  # Ingest PDFs from /rag folder
python app.py     # Start FastAPI server
```

**3. Setup Frontend:**
```bash
cd frontend
npm install
node server.js    # Start Node server
```

---

## 📁 Project Structure

```text
├── rag/                   # 📂 Place source IT PDFs here
├── vectorstore/           # 🗄️ Persisted FAISS embeddings
├── frontend/              
│   ├── public/            # 🎨 HTML/CSS/JS (ChatGPT UI)
│   └── server.js          # 🌐 Node.js Express server
├── tests/                 # 🧪 Automated test suite
├── .github/workflows/     # ⚙️ CI/CD Pipeline configuration
├── app.py                 # 🧠 FastAPI Backend & RAG Chain
├── ingest.py              # 📥 Data Ingestion Script
├── docker-compose.yml     # 🚢 Multi-container orchestration
├── backend.Dockerfile     # 🐍 Python container config
└── frontend.Dockerfile    # 📦 Node container config
```

---

## 🛡️ CI/CD & Testing
The project includes a robust **GitHub Actions** workflow that:
1. Runs Python unit tests with `pytest`.
2. Validates Node.js environment.
3. Verifies Docker builds for both services.

To run tests locally:
```bash
pytest tests/
```

---

## ⚖️ Development Conventions
- **Model Offloading:** Automatically detects and uses GPU (CUDA) if available, otherwise defaults to CPU.
- **Model Caching:** Docker volumes are used to ensure the 1.7B model isn't re-downloaded on every restart.
- **Safety:** Dangerous deserialization is enabled for FAISS to allow local loading of the knowledge base.

---
Created by Gemini CLI Assistant 🚀
