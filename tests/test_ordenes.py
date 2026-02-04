from app.app import app

def test_crear_orden():
    client = app.test_client()
    response = client.post("/orden", json={
        "cliente": "Juan Perez",
        "descripcion": "Cambio de aceite"
    })
    assert response.status_code == 201

def test_listar_ordenes():
    client = app.test_client()
    response = client.get("/orden")
    assert response.status_code == 200
