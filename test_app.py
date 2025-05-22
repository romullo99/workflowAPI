import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_root(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}

def test_post_data(client):
    response = client.post('/data', json={"name": "Romullo"})
    assert response.status_code == 200
    assert response.get_json() == {"received": {"name": "Romullo"}}

def test_post_invalid_content_type(client):
    response = client.post('/data', data="name=Romullo", headers={"Content-Type": "text/plain"})
    assert response.status_code == 415
    assert "error" in response.get_json()
