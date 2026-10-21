from fastapi.testclient import TestClient
from app.main import app
from app.services import tasks

client = TestClient(app)

def setup_function():
    tasks._tasks.clear()
    tasks._next_id = 1

def test_crud():
    assert client.get("/api/v1/tasks").json() == []
    result = client.post("/api/v1/tasks", json={"title": "Первая задача", "description": "Описание"})
    assert result.status_code == 201
    assert result.json()["id"] == 1
    assert client.get("/api/v1/tasks/1").status_code == 200
    assert len(client.get("/api/v1/tasks").json()) == 1
    result = client.put("/api/v1/tasks/1", json={"title": "Изменено"})
    assert result.status_code == 200 and result.json()["title"] == "Изменено"
    assert client.delete("/api/v1/tasks/1").status_code == 204
    assert client.get("/api/v1/tasks/1").status_code == 404

def test_errors():
    assert client.post("/api/v1/tasks", json={"title": ""}).status_code == 422
    assert client.put("/api/v1/tasks/999", json={"title": "abc"}).status_code == 404
    assert client.delete("/api/v1/tasks/999").status_code == 404
