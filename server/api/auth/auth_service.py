from flask_jwt_extended import create_access_token


class AuthService:
    @staticmethod
    def generate_token(user_id: int):
        return create_access_token(identity=user_id)
