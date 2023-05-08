from flask import Blueprint, jsonify, abort, make_response, request
from app.models.star import Star
from app.models.planet import Planet
from app import db
from app.helper import validate_model

star_bp = Blueprint("stars", __name__, url_prefix="/stars")

@star_bp.route("", methods=["POST"])
def create_star():
    request_body = request.get_json()
    try:
        new_star = Star.from_dict(request_body)

        db.session.add(new_star)
        db.session.commit()
        return make_response(jsonify(f"Star {new_star.name} successfully created"), 201)
    except KeyError as error:
        abort(make_response({"error message": f"missing required value {error}"}), 400)

@star_bp.route("", methods=["GET"])
def read_all_stars():
    stars = Star.query.all()
    stars_response = [star.to_dict() for star in stars]

    return jsonify(stars_response)

@star_bp.route("<star_id>/planets", methods=["POST"])
def create_planet(star_id):
    star = validate_model(Star, star_id)
    request_body = request.get_json()
    try:
        new_planet = Planet.from_dict(request_body)
        new_planet.star = star_bp

        db.session.add(new_planet)
        db.session.commit()
    
        return make_response(jsonify(f"Planet {new_planet.name} has the star {star.name} oribit successfully"), 201)
    except KeyError as error:
        abort(make_response({"error message": f"missing required value {error}"}, 400))

@star_bp.route("<star_id>/planets", methods=["GET"])
def read_planets(star_id):
    star = validate_model(Star, star_id)

    planets_response = [planet.to_dict() for planet in star.planets]

    return(jsonify(planets_response))