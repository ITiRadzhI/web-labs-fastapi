import os
import tempfile
from pathlib import Path

# Тестовая БД — независимый временный файл; настройка до импорта приложения.
_tmp = tempfile.TemporaryDirectory()
os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///" + str(Path(_tmp.name) / "test.db")

from fastapi.testclient import TestClient  # noqa: E402
from app.main import app  # noqa: E402

def test_crud_and_validation():
    with TestClient(app) as client:
        assert client.get("/api/v1/tasks").json() == []
        create = client.post("/api/v1/tasks", json={"title": "Задача для БД"})
        assert create.status_code == 201
        task_id = create.json()["id"]
        assert client.get(f"/api/v1/tasks/{task_id}").status_code == 200
        assert client.put(f"/api/v1/tasks/{task_id}", json={"title": "Новый текст"}).json()["title"] == "Новый текст"
        assert client.post("/api/v1/tasks", json={"title": ""}).status_code == 422
        assert client.delete(f"/api/v1/tasks/{task_id}").status_code == 204
        assert client.get(f"/api/v1/tasks/{task_id}").status_code == 404

def test_persistence_between_clients():
    with TestClient(app) as client:
        task_id = client.post("/api/v1/tasks", json={"title": "Сохранится"}).json()["id"]
    with TestClient(app) as client:
        assert client.get(f"/api/v1/tasks/{task_id}").json()["title"] == "Сохранится"
