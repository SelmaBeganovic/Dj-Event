from distutils.debug import DEBUG
from re import T


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


class TestingConfig(Config):
    DATABASE_URI = "sqlite:///:memory:"
    TESTING = True
