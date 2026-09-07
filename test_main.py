from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_dashboard():
    response = client.get("/")
    assert response.status_code == 200

def test_evaluation_compliant():
    response = client.post("/api/qa/evaluate", json={"text": "Hello, how can I help you explore our services today?"})
    assert response.status_code == 200
    data = response.json()["evaluation_result"]
    assert data["compliance_violation"] is False
    assert data["risk_score"] < 0.1

def test_evaluation_violation():
    response = client.post("/api/qa/evaluate", json={"text": "This financial plan offers a 20% guaranteed return with zero risk."})
    assert response.status_code == 200
    data = response.json()["evaluation_result"]
    assert data["compliance_violation"] is True
    assert data["risk_score"] > 0.9