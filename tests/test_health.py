
from fastapi.testclient import TestClient
from app.main import app

test = TestClient(app)

def test_head():

    response = test.get("/health")

    assert response.status_code == 200
    assert response.json() == {"menssagem": "API rodando com sucesso"}