import requests

BASE = "https://jsonplaceholder.typicode.com"

def test_get_post():
    r = requests.get(f"{BASE}/posts/1", timeout=10)
    assert r.status_code == 200
    assert r.json()["id"] == 1

def test_create_post():
    payload = {"title": "test", "body": "hello", "userId": 1}
    r = requests.post(f"{BASE}/posts", json=payload, timeout=10)
    assert r.status_code == 201
    assert r.json()["title"] == "test"

def test_not_found():
    r = requests.get(f"{BASE}/posts/99999", timeout=10)
    assert r.status_code == 404