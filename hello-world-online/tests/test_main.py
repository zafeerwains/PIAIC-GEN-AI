from fastapi import TestClient
from hello_world_online.main import app


def test_root_path():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}


def test_ntu():
    client = TestClient(app=app)
    response = client.get("/ntu")
    assert response.status_code == 200
    assert response.json() == {"ntu": "GEN-AI"}
