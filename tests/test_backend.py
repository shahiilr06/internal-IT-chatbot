from fastapi.testclient import TestClient
import sys
import os

# Add the parent directory to sys.path to import app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

client = TestClient(app)

def test_read_root():
    # Root route should be healthy
    response = client.get("/")
    assert response.status_code == 200

def test_chat_endpoint_no_data():
    # Testing the chat endpoint without valid payload
    response = client.post("/chat", json={})
    assert response.status_code == 422 # Unprocessable Entity
