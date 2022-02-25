from flask import Blueprint, jsonify, request, make_response

from api import db
from api.user.user_model import User

auth_blueprint = Blueprint("auth", __name__)


@auth_blueprint.route("/login", methods=['GET'])
def login():
    return jsonify({"message": "Login"})


@auth_blueprint.route("/auth/register", methods=['POST'])
def register():
    user_data = request.get_json()

    user = User.query.filter(User.email == user_data.get("email")).first()
    if not user:
        try:
            user = User(username=user_data.get("username"), email=user_data.get("email"),
                        password=user_data.get("password"))
            db.session.add(user)
            db.session.commit()

            response_object = {
                'status': 'success',
                'message': 'Successfully registered.',
                'auth_token': 'token'
            }
            return jsonify(response_object)
        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.'
            }
            return jsonify(response_object)
    else:
        response_object = {
            'status': 'fail',
            'statusCode': 202,
            'message': 'User already exists. Please Log in.'
        }
        return make_response(jsonify(response_object)), 202
