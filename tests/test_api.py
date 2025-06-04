from fastapi.testclient import TestClient
from api.app import app

def test_post_recommend():
    client = TestClient(app)
    response = client.post("/recommend", json={
        "heart_rate": 125,
        "height_cm": 175,
        "weight_kg": 70,
        "age": 30,
        "body_fat_pct": 15,
        "objective": "cardio"
    })
    assert response.status_code == 200
    assert "recommendation" in response.json()

def test_create_user():
    client = TestClient(app)
    response = client.post("/user/create", json={
        "name": "Luis",
        "height_cm": 172,
        "weight_kg": 68,
        "age": 28,
        "body_fat_pct": 16,
        "objective": "aerobico"
    })
    assert response.status_code == 200
    assert "user_id" in response.json()
    assert response.json()["name"] == "Luis"