import json
from datetime import date
import re

def test_create_driver(client):
    payload = {
        "name": "Senna",
        "birthday": "1960-03-21",
        "cpf": "12345678900",
        "driver_license": "ABC123456"
    }

    response = client.post("/driver", data=json.dumps(payload), content_type="application/json")
    
    assert response.status_code == 201
    assert b"Driver created successfully" in response.data

def test_get_drivers(client):
    test_create_driver(client)

    response = client.get("/driver")
    assert response.status_code == 200

    data = response.get_json()
    assert isinstance(data, list)

    if data:
        first = data[0]
        
        assert "birthday" in first
        date.fromisoformat(first["birthday"])  # formato YYYY-MM-DD
        
        assert "cpf" in first
        assert re.match(r"^\d{11}$", str(first["cpf"]))
