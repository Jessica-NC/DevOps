"""Testes automatizados da API de tarefas.

Executados localmente com `pytest` e também pelo pipeline de
Integração Contínua (GitHub Actions) a cada push/pull request.
"""
import pytest

from app.app import create_app
from app.models import db


@pytest.fixture
def client():
    app = create_app(
        test_config={
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
            "TESTING": True,
        }
    )
    with app.app_context():
        db.create_all()
    with app.test_client() as client:
        yield client


def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_create_and_list_task(client):
    response = client.post("/tasks", json={"title": "Configurar pipeline de CI"})
    assert response.status_code == 201
    task = response.get_json()
    assert task["title"] == "Configurar pipeline de CI"
    assert task["status"] == "pendente"

    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.get_json()) == 1


def test_create_task_without_title_fails(client):
    response = client.post("/tasks", json={"description": "sem título"})
    assert response.status_code == 400


def test_get_update_and_delete_task(client):
    created = client.post("/tasks", json={"title": "Revisar Pull Request"}).get_json()
    task_id = created["id"]

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200

    response = client.put(f"/tasks/{task_id}", json={"status": "concluida"})
    assert response.status_code == 200
    assert response.get_json()["status"] == "concluida"

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404


def test_get_nonexistent_task_returns_404(client):
    response = client.get("/tasks/999")
    assert response.status_code == 404
