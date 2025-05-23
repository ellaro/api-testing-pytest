import pytest
from main import app as flask_app


@pytest.fixture(scope='function')
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client


def test_get_existing_user(client):
    email = "Dsoron@gmail.com"
    response = client.get(f"/users/{email}")
    assert response.status_code == 200
    data = response.get_json()
    assert "email" in data
    assert data["email"] == email


def test_get_non_existing_user(client):
    email = "nonexistentuser@example.com"
    response = client.get(f"/users/{email}")
    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "User not found"
