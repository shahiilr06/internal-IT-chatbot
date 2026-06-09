---
type: Guide
tags: [setup, docker, deployment]
---

# 50 Setup & Deployment

## 🐳 Docker (Production)
```bash
docker-compose up --build
```

## 💻 Local (Development)
1. **Backend:** `pip install -r requirements.txt && python app.py`
2. **Frontend:** `cd frontend && npm install && node server.js`

> [!IMPORTANT]
> Always run `python ingest.py` first to initialize the vector database!

---
[[00 Index|🏠 Back to Home]]
