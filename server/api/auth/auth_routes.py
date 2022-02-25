from flask import Blueprint, jsonify, request, make_response
from flask_jwt_extended import create_access_token

from api import db, bcrypt
from api.user.user_model import User

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/auth/login", methods=["POST"])
def login():
    user_data = request.get_json()
    try:
        user = User.query.filter(User.email == user_data.get("email")).first()

        if user and bcrypt.check_password_hash(
            user.password, user_data.get("password")
        ):
            access_token = create_access_token(identity=user.id)
            return (
                make_response(
                    jsonify(
                        {
                            "status": "success",
                            "message": "Successfully logged in.",
                            "jwt": access_token,
                            "statusCode": 200,
                        }
                    )
                ),
                200,
            )
        else:
            return (
                make_response(
                    jsonify(
                        {
                            "status": "fail",
                            "message": "User does not exist.",
                            "statusCode": 500,
                        }
                    )
                ),
                404,
            )
    except Exception as e:
        print(e)
        return (
            make_response(
                jsonify({"status": "fail", "message": "Try again", "statusCode": 500})
            ),
            500,
        )


@auth_blueprint.route("/auth/register", methods=["POST"])
def register():
    user_data = request.get_json()

    user = User.query.filter(User.email == user_data.get("email")).first()
    if not user:
        try:
            user = User(
                username=user_data.get("username"),
                email=user_data.get("email"),
                password=user_data.get("password"),
            )
            db.session.add(user)
            db.session.commit()

            response_object = {
                "status": "success",
                "message": "Successfully registered.",
                "auth_token": "token",
            }
            return jsonify(response_object)
        except Exception as e:
            response_object = {
                "status": "fail",
                "message": "User already exists. Please Log in.",
            }
            return jsonify(response_object)
    else:
        response_object = {
            "status": "fail",
            "statusCode": 202,
            "message": "User already exists. Please Log in.",
        }
        return make_response(jsonify(response_object)), 202
