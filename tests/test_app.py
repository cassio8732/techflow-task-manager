"""
Testes automatizados do TechFlow Task Manager.
Executados via Pytest, tanto localmente quanto no pipeline de CI
(GitHub Actions).
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from app import app, tasks


@pytest.fixture
def client():
    """Cria um cliente de teste e garante que a lista de tarefas
    comece vazia antes de cada teste."""
    tasks.clear()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_create_task(client):
    """Deve criar uma tarefa com sucesso quando o título é informado."""
    response = client.post("/tasks", json={"title": "Configurar repositório"})
    assert response.status_code == 201
    assert response.get_json()["title"] == "Configurar repositório"


def test_create_task_without_title(client):
    """Deve retornar erro 400 quando o título não é informado."""
    response = client.post("/tasks", json={})
    assert response.status_code == 400


def test_list_tasks(client):
    """Deve listar as tarefas cadastradas."""
    client.post("/tasks", json={"title": "Tarefa 1"})
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.get_json()) == 1


def test_update_task_status(client):
    """Deve atualizar o status de uma tarefa existente."""
    created = client.post("/tasks", json={"title": "Tarefa X"}).get_json()
    response = client.put(
        f"/tasks/{created['id']}", json={"status": "Concluído"}
    )
    assert response.status_code == 200
    assert response.get_json()["status"] == "Concluído"


def test_delete_task(client):
    """Deve remover uma tarefa existente."""
    created = client.post("/tasks", json={"title": "Tarefa Y"}).get_json()
    response = client.delete(f"/tasks/{created['id']}")
    assert response.status_code == 200
    assert find_deleted(created["id"]) is False


def find_deleted(task_id):
    return any(t["id"] == task_id for t in tasks)
