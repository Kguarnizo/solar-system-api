from flask import Blueprint, jsonify, abort, make_response

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

class Planet:
    def __init__(self, id, name, description, num_moons):
        self.id = id
        self.name = name
        self.description = description
        self.num_moons = num_moons

    def to_dict(self):
        return {
                "id": self.id,
                "name": self.name,
                "description": self.description,
                "num_moons": self.num_moons
            }

planets = [
    Planet(1, "Mercury", "It's the first planet in our solar system", 0),
    Planet(2, "Venus", "It's the second planet in our solar system", 0),
    Planet(3, "Earth", "It's the third planet in our solar system", 1)
]

@planets_bp.route("", methods=["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())

    return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = validate_planet(planet_id)

    return planet.to_dict()
    

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        abort(make_response({"error message": f"planet {planet_id} is invalid"}, 400))
    
    for planet in planets:
        if planet.id == planet_id:
            return planet
    abort(make_response({"error message": f"planet {planet_id} not found"}, 404))