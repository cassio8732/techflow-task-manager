"""
TechFlow Task Manager
Sistema simples de gerenciamento de tarefas (CRUD) usando Flask.

Este módulo implementa uma API REST básica para criar, listar,
atualizar e deletar tarefas, simulando o sistema solicitado pela
startup de logística fictícia (TechFlow Solutions).
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# "Banco de dados" em memória (lista de dicionários).
# Simples de propósito, já que o foco do trabalho é o processo ágil
# e não a persistência de dados.
tasks = []
next_id = 1


def find_task(task_id):
    """Busca uma tarefa pelo id. Retorna None se não encontrar."""
    return next((t for t in tasks if t["id"] == task_id), None)


@app.route("/tasks", methods=["GET"])
def list_tasks():
    """Lista todas as tarefas cadastradas."""
    return jsonify(tasks), 200


@app.route("/tasks", methods=["POST"])
def create_task():
    """Cria uma nova tarefa. Requer o campo 'title'."""
    global next_id
    data = request.get_json(silent=True) or {}
    title = data.get("title")

    if not title:
        return jsonify({"error": "O campo 'title' é obrigatório"}), 400

    task = {
        "id": next_id,
        "title": title,
        "status": data.get("status", "A Fazer"),
        # campo adicionado na mudança de escopo (ver README.md)
        "priority": data.get("priority", "media"),
    }
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    """Atualiza o status/título/prioridade de uma tarefa existente."""
    task = find_task(task_id)
    if not task:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    data = request.get_json(silent=True) or {}
    task["title"] = data.get("title", task["title"])
    task["status"] = data.get("status", task["status"])
    task["priority"] = data.get("priority", task["priority"])
    return jsonify(task), 200


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """Remove uma tarefa pelo id."""
    task = find_task(task_id)
    if not task:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    tasks.remove(task)
    return jsonify({"message": "Tarefa removida com sucesso"}), 200


if __name__ == "__main__":
    app.run(debug=True)
