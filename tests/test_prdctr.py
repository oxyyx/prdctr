from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_main():
    """
    We expect the root directory to not return anything.
    """
    response = client.get("/")
    assert response.status_code == 404