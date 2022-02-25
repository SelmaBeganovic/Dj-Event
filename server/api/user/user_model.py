import datetime

from flask import current_app
from api import db, bcrypt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    registered_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = bcrypt.generate_password_hash(
            password, current_app.config.get("BCRYPT_LOG_ROUNDS")
        ).decode()
        self.registered_on = datetime.datetime.now()

    def serialize(self):
        return {
            "email": self.email,
            "username": self.username,
        }
