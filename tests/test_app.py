import json
import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_api_prompt(client):
    response = client.post(
        "/api/prompt",
        data=json.dumps({"prompt": "Hello, world!"}),
        content_type="application/json"
    )
    assert response.status_code == 200
    data = response.get_json()
    assert "sanitized_prompt" in data
