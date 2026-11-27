from fastapi.testclient import TestClient

from sentinel.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["service"] == "sentinel-api"


def test_agents():
    response = client.get("/v1/agents")
    assert response.status_code == 200
    assert len(response.json()) >= 5


def test_artex_is_inert_by_default():
    response = client.get("/v1/integrations/artex")
    assert response.status_code == 200
    assert response.json()["execution"] == "not_implemented"
