from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

def validate_model(cls,model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"error message": f"{cls.__name__} {model_id} is invalid"}, 400))

    model = cls.query.get(model_id)
    
    if not model:
        abort(make_response({"error message": f"{cls.__name__} {model_id} not found"}, 404))
    
    return model