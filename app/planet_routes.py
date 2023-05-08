from app import db
from app.models.planet import Planet
from app.helper import validate_model
from flask import Blueprint, jsonify, abort, make_response, request


planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def create_planets():
    request_body = request.get_json()
    try:
        new_planet = Planet.from_dict(request_body)
        db.session.add(new_planet)
        db.session.commit()

        return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)
    
    except KeyError as error:
        abort(make_response({"error message": f"missing required value: {error}"}, 400))

@planets_bp.route("", methods=["GET"])
def read_all_planets():
    name_query = request.args.get("name")
    description_query = request.args.get("description")
    num_moons_query = request.args.get("num_moons")
    if name_query:
        planets = Planet.query.filter_by(name = name_query)

    if num_moons_query:
        planets = Planet.query.filter_by(num_moons = num_moons_query)

    else:
        planets = Planet.query.all()
    
    planets_response = [planet.to_dict() for planet in planets]
    return jsonify(planets_response)


@planets_bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_model(Planet,planet_id)

    return jsonify(planet.to_dict())
                

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_model(planet_id)

    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.num_moons = request_body["num_moons"]

    db.session.commit()

    return make_response(f"Planet {planet.id} successfully updated")

@planets_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_model(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet {planet.id} successfully deleted")