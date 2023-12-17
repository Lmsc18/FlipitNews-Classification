import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    # Create a TestClient for making test requests to the FastAPI app
    return TestClient(app)

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

