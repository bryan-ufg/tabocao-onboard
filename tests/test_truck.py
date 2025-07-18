import json
from datetime import date

endpoint = "/truck"

def add_truck(client):
    payload = {
        "model": "Volvo FMX",
        "year": 2025,
        "license_plate": "BRA2O25"
    }

    response = client.post(endpoint, data=json.dumps(payload), content_type="application/json")

    return response

def test_create_truck(client):
    response = add_truck(client)
    assert response.status_code == 201
    assert b"Truck created successfully" in response.data

def test_get_trucks(client):
    response = add_truck(client)
    assert response.status_code == 201

    response = client.get(endpoint)
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)

    assert data[0]