from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_all():
    resp = client.get("/exercises")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)

def test_filter_muscle():
    resp = client.get("/exercises?muscle=Core")
    assert all(ex["muscle"] == "Core" for ex in resp.json())
