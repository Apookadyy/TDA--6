from flask import Blueprint, request, jsonify
import src.config.services.taskservice
from src.config.utils.helpers import format_response
from src.config.middleware.logger import log_request

task_api = Blueprint("task_api", __name__)

@task_api.route("/task", methods=["POST"])
def create_task():
    log_request("/task POST")
    title = request.json.get("title")
    task = src.services.taskservice.TaskService.create_task(title)
    return jsonify(format_response(task.__dict__))

@task_api.route("/tasks", methods=["GET"])
def get_tasks():
    log_request("/tasks GET")
    tasks = [t.__dict__ for t in src.services.taskservice.TaskService.get_tasks()]
    return jsonify(format_response(tasks))