import json
from datetime import date

endpoint = "/user"

def add_user(client):
    payload = {
        "name": "João da Silva",
        "username": "joaosilva",
        "password": "senhaSegura123"
    }

    response = client.post(endpoint, data=json.dumps(payload), content_type="application/json")
    
    return response

def test_create_user(client):
    response = add_user(client)
    assert response.status_code == 201
    assert b"User created successfully" in response.data

def test_get_users(client):
    response = add_user(client)
    assert response.status_code == 201

    response = client.get(endpoint)
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)

    assert data[0]