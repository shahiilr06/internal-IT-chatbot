---
type: Overview
tags: [architecture, flow, rag]
---

# 10 Project Overview

The **Nexira Multi-PDF IT Assistant** is a production-grade **Retrieval-Augmented Generation (RAG)** system.

## 📊 System Flow Diagram

```mermaid
graph TD
    User((User)) -->|Query| UI[Node.js Frontend]
    UI -->|POST /chat| API[FastAPI Backend]
    API -->|Vector Search| VS[(FAISS Vector Store)]
    VS -->|Context Chunks| API
    API -->|Context + Query| LLM[SmolLM2-1.7B]
    LLM -->|Generated Response| API
    API -->|JSON| UI
    UI -->|Markdown Render| User
```

## 🎯 Primary Objectives
- **Zero Hallucination:** Constrained generation using strict system prompts.
- **Accessibility:** Industry-standard ChatGPT user experience.
- **Efficiency:** Deployment on consumer-grade hardware.

---
[[00 Index|🏠 Back to Home]]
