import pytest
from fastapi.testclient import TestClient
from main_api import app


@pytest.fixture
def client():
    """
    Get dataset
    """
    api_client = TestClient(app)
    return api_client


def test_get(client):
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello, welcome to our app!"}


def test_get_malformed(client):
    r = client.get("/wrong_url")
    assert r.status_code != 200