from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)

    # Replace with config file
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    from api.events.routes import events_blueprint

    app.register_blueprint(events_blueprint)

    return app
