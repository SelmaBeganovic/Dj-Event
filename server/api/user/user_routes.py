from flask import Blueprint, jsonify

user_blueprint = Blueprint("user", __name__)


@user_blueprint.route("/profile", methods=['GET'])
def profile():
    return jsonify({"message", "Initial route"})