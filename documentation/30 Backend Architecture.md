---
type: Architecture
tags: [backend, fastapi, llm, langchain]
---

# 30 Backend Architecture

The backend (`app.py`) is the core intelligence hub.

## 🧠 LLM Interaction Flow

```mermaid
sequenceDiagram
    participant API as FastAPI
    participant LC as LangChain
    participant VS as FAISS Store
    participant LLM as SmolLM2-1.7B

    API->>LC: Process User Query
    LC->>VS: Retrieve Top 5 Chunks
    VS-->>LC: Return Relevant Text
    LC->>LC: Build ChatML Prompt
    LC->>LLM: Generate Answer
    LLM-->>LC: Raw Response
    LC->>API: Formatted Answer
    API->>API: Post-Processing Cleanup
```

## 🛠️ FastAPI Configuration
- **Port:** 8000
- **CORS:** Enabled for Port 3000
- **Inference:** CUDA-aware (float16)

---
[[00 Index|🏠 Back to Home]]
[[70 CI-CD Pipeline]]
[[60 Data Ingestion]]
[[40 Frontend Architecture]]
[[10 Project Overview]]

