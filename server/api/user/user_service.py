from api import db
from api.user.user_model import User


class UserService:
    @staticmethod
    def get_user_by_id(id: int):
        return User.query.get(id)

    @staticmethod
    def get_user_by_email(email: str) -> User:
        return User.query.filter(User.email == email).first()

    @staticmethod
    def create_user(username: str, email: str, password: str) -> User:
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        return user
