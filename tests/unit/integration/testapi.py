import requests

def test_get_tasks():
    response = requests.get("http://localhost:5000/tasks")
    assert response.status_code == 200