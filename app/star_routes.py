from flask import Blueprint, jsonify, abort, make_response, request
from app import db

star_bp = Blueprint("stars", __name__, url_prefix="/stars")