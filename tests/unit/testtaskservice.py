from src.config.services.taskservice import TaskService

def test_create_task():
    task = TaskService.create_task("Unit Test Task")
    assert task.title == "Unit Test Task"