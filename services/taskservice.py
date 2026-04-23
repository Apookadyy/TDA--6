from src.config.core.database import tasks_db
from src.config.models.task import Task

class TaskService:

    @staticmethod
    def create_task(title):
        task = Task(title)
        tasks_db.append(task)
        return task

    @staticmethod
    def get_tasks():
        return tasks_db 
    