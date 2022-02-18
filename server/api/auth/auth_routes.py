from flask import Blueprint, jsonify

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/login", methds=['GET'])
def login():
    return jsonify({"message": "Login"})


@auth_blueprint.route("/register", methds=['GET'])
def register():
    return jsonify({"message": "Register"})