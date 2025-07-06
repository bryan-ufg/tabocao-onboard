import json
from datetime import date

def test_create_truck(client):
    payload = {
        "model": "Volvo FMX",
        "year": 2025,
        "license_plate": "BRA2O25"
    }

    response = client.post("/truck", data=json.dumps(payload), content_type="application/json")
    
    assert response.status_code == 201
    assert b"Truck created successfully" in response.data

def test_get_trucks(client):
    test_create_truck(client)

    response = client.get("/truck")
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)

    assert data[0]