import time
import requests

def test_load():
    start = time.time()
    for _ in range(50):
        requests.get("http://localhost:5000/tasks")
    print("Execution Time:", time.time() - start)