"""API REST de gerenciamento de tarefas da CodeFactory Solutions.

Este serviço é o exemplo prático utilizado para demonstrar a
containerização (Docker) e o pipeline de Integração Contínua da
disciplina de DevOps e Integração Contínua (UNINTER).
"""
import os

from flask import Flask, jsonify, request

from app.models import Task, db


def create_app(test_config=None):
    app = Flask(__name__)

    database_url = os.environ.get(
        "DATABASE_URL", "sqlite:///taskmanager.db"
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.get("/health")
    def health():
        """Endpoint usado pelo pipeline de CI e pelo Docker healthcheck."""
        return jsonify(status="ok"), 200

    @app.get("/tasks")
    def list_tasks():
        tasks = Task.query.order_by(Task.id).all()
        return jsonify([task.to_dict() for task in tasks]), 200

    @app.post("/tasks")
    def create_task():
        payload = request.get_json(silent=True) or {}
        title = payload.get("title")
        if not title:
            return jsonify(error="O campo 'title' é obrigatório."), 400

        task = Task(
            title=title,
            description=payload.get("description"),
            status=payload.get("status", "pendente"),
        )
        db.session.add(task)
        db.session.commit()
        return jsonify(task.to_dict()), 201

    @app.get("/tasks/<int:task_id>")
    def get_task(task_id):
        task = db.session.get(Task, task_id)
        if not task:
            return jsonify(error="Tarefa não encontrada."), 404
        return jsonify(task.to_dict()), 200

    @app.put("/tasks/<int:task_id>")
    def update_task(task_id):
        task = db.session.get(Task, task_id)
        if not task:
            return jsonify(error="Tarefa não encontrada."), 404

        payload = request.get_json(silent=True) or {}
        task.title = payload.get("title", task.title)
        task.description = payload.get("description", task.description)
        task.status = payload.get("status", task.status)
        db.session.commit()
        return jsonify(task.to_dict()), 200

    @app.delete("/tasks/<int:task_id>")
    def delete_task(task_id):
        task = db.session.get(Task, task_id)
        if not task:
            return jsonify(error="Tarefa não encontrada."), 404

        db.session.delete(task)
        db.session.commit()
        return "", 204

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
