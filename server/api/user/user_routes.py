from flask import Blueprint, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity

from api.user.user_model import User

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/users/profile", methods=["GET"])
def profile():
    return jsonify({"message", "Initial route"})


@user_blueprint.route("/users/me", methods=["GET"])
@jwt_required()
def get_user_data():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)

    return make_response(jsonify(user.serialize())), 200
