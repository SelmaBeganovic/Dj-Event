from distutils.debug import DEBUG
from re import T

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    TESTING = False
    BCRYPT_LOG_ROUNDS = 13


class ProductionConfig(Config):
    DATABASE_URI = "mysql://user@localhost/foo"


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///../app.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 5
    JWT_SECRET_KEY = "top_secrec_key"
    SECRET_KEY = os.environ.get("SECRET_KEY")
    UPLOAD_FOLDER = os.path.join(basedir, "static/uploads")
    SERVER_NAME = "localhost:5000"


class TestingConfig(Config):
    DATABASE_URI = "sqlite:///:memory:"
    TESTING = True
