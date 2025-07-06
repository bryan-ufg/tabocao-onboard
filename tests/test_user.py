import json
from datetime import date

def test_create_user(client):
    payload = {
        "name": "João da Silva",
        "username": "joaosilva",
        "password": "senhaSegura123"
    }

    response = client.post("/user", data=json.dumps(payload), content_type="application/json")
    
    assert response.status_code == 201
    assert b"User created successfully" in response.data

def test_get_users(client):
    test_create_user(client)

    response = client.get("/user")
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)

    assert data[0]