from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planets():
    request_body = request.get_json()
    new_planet = Planet(name = request_body["name"],
        description = request_body["description"],
        num_moons = request_body["num_moons"])
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created, 201")

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    planets_response = []
    planets = Planet.query.all()
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "num_moons": planet.num_moons
            }
        )
    return jsonify(planets_response)

@planets_bp.route("", methods=["PATCH"])
def update_planet():
    request_update = request.get_json()
    update_planet = Planet() #SQLALCHEMY

@planets_bp.route("", methods=["DELETE"])



# class Planet:
#     def __init__(self, id, name, description, num_moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.num_moons = num_moons

#     def to_dict(self):
#         return {
#                 "id": self.id,
#                 "name": self.name,
#                 "description": self.description,
#                 "num_moons": self.num_moons
#             }

# planets = [
#     Planet(1, "Mercury", "It's the first planet in our solar system", 0),
#     Planet(2, "Venus", "It's the second planet in our solar system", 0),
#     Planet(3, "Earth", "It's the third planet in our solar system", 1)
# ]

# @planets_bp.route("", methods=["GET"])
# def handle_planets():
#     planets_response = []
#     for planet in planets:
#         planets_response.append(planet.to_dict())

#     return jsonify(planets_response)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def handle_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return planet.to_dict()
    

# def validate_planet(planet_id):
    # try:
    #     planet_id = int(planet_id)
    # except:
    #     abort(make_response({"error message": f"planet {planet_id} is invalid"}, 400))
    
    # for planet in planets:
    #     if planet.id == planet_id:
    #         return planet
    # abort(make_response({"error message": f"planet {planet_id} not found"}, 404))