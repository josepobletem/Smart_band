from fastapi.testclient import TestClient
from api.app import app

def test_post_recommend():
    """
    Prueba el endpoint '/recommend' enviando datos de usuario.

    Envía un JSON con datos de frecuencia cardíaca, altura, peso, edad,
    porcentaje de grasa corporal y objetivo. Verifica que la respuesta tenga
    código de estado 200 y contenga la clave 'recommendation'.

    Returns
    -------
    None
    """
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
    """
    Prueba el endpoint '/user/create' enviando datos de perfil de usuario.

    Envía un JSON con nombre, altura, peso, edad, porcentaje de grasa corporal
    y objetivo. Verifica que la respuesta tenga código de estado 200, contenga
    la clave 'user_id' y que el nombre retornado sea igual al enviado.

    Returns
    -------
    None
    """
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