import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_health(client):
    res = client.get('/health')
    assert res.status_code == 200
    assert res.json['status'] == 'Healthy'

def test_get_favorites(client):
    res = client.get('/api/favorites')
    assert res.status_code == 200
    assert len(res.json) >= 2