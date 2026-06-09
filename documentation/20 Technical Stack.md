# 20 Technical Stack

This project leverages a carefully selected stack designed for high performance and low resource consumption.

## 🧠 AI & Backend Layer
- **FastAPI (Python 3.11):** Chosen for its asynchronous capabilities and native Pydantic support for request validation.
- **LangChain & LangChain-HuggingFace:** Orchestrates the complex RAG logic and provides easy integration with Hugging Face models.
- **SmolLM2-1.7B-Instruct:** A lightweight model optimized for technical reasoning. It uses **ChatML** formatting for high instruction-following accuracy.
- **FAISS (Facebook AI Similarity Search):** Used for efficient dense vector similarity search. It allows for "dangerous deserialization" to load local knowledge bases safely.
- **Sentence Transformers (`all-MiniLM-L6-v2`):** A 384-dimensional embedding model that balances speed and semantic accuracy.

## 🎨 Frontend UI Layer
- **Node.js 20 & Express:** Serves the static assets and provides a lightweight production server.
- **Tailwind CSS:** Used for the "ChatGPT Clone" aesthetic, featuring dark mode and responsive layouts.
- **Marked.js:** A high-speed Markdown compiler to turn LLM-generated text into clean HTML.
- **FontAwesome:** Provides the iconography for the robot assistant and user avatars.

## ⚙️ Infrastructure & DevOps
- **Docker & Docker Compose:** Encapsulates the Python environment and Node.js server into a unified container.
- **GitHub Actions:** Automates the CI/CD pipeline, including `pytest` for backend logic and Docker build verification.
- **CUDA Support:** The backend automatically detects and utilizes NVIDIA GPUs (if available) for 10x faster inference.

---
[[00 Index|Back to Index]]
