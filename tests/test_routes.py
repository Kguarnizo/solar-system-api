from app.models.planet import Planet

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_returns_seeded_planet(client, one_planet):
    response = client.get(f"/planets/{one_planet.id}")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["id"] == one_planet.id
    assert response_body["name"] == one_planet.name
    assert response_body["description"] == one_planet.description
    assert response_body["num_moons"] == one_planet.num_moons


def test_create_planet_happy_path(client):
    # arrange
    EXPECTED_PLANET = {
        "name": "Mercury",
        "description": "It's the first planet in our solar system",
        "num_moons": 0
    }
    
    response = client.post("/planets", json=EXPECTED_PLANET)
    response_body = response.get_json()

    actual_planet = Planet.query.get(1)
    assert response.status_code == 201
    assert response_body == f"Planet {EXPECTED_PLANET['name']} successfully created"
    assert actual_planet.name == EXPECTED_PLANET["name"]
    assert actual_planet.description == EXPECTED_PLANET["description"]
    assert actual_planet.num_moons == EXPECTED_PLANET["num_moons"]