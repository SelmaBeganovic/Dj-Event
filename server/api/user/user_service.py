from api.user.user_model import User


class UserService:
    @staticmethod
    def get_user_by_id(id: int):
        return User.query.get(id)
