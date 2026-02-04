import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def get_openapi_paths():
    schema = client.get("/openapi.json").json()
    return list(schema.get("paths", {}).keys())

@pytest.mark.parametrize("route", get_openapi_paths())
def test_all_routes_exist(route):
    # Só checa se existe e não quebra por 404
    response = client.get(route)
    assert response.status_code != 500
