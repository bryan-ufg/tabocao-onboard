import json
from datetime import date
import re

endpoint = "/driver"

def add_driver(client):
    payload = {
        "name": "Senna",
        "birthday": "1960-03-21",
        "cpf": "12345678900",
        "driver_license": "ABC123456"
    }

    response = client.post(endpoint, data=json.dumps(payload), content_type="application/json")
    
    return response

def test_create_driver(client):
    response = add_driver(client)
    assert response.status_code == 201
    assert b"Driver created successfully" in response.data

def test_get_drivers(client):
    response = add_driver(client)
    assert response.status_code == 201

    response = client.get(endpoint)
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)

    if data:
        first = data[0]
        
        assert "birthday" in first
        date.fromisoformat(first["birthday"])  # formato YYYY-MM-DD
        
        assert "cpf" in first
        assert re.match(r"^\d{11}$", str(first["cpf"]))
