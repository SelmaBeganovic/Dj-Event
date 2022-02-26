from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()
cors = CORS()


def create_app():
    app = Flask(__name__)

    # Create different config for different envs
    app.config.from_object("api.config.DevelopmentConfig")

    from api.commands.events import insert_events_into_database

    app.cli.add_command(insert_events_into_database)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)
    cors.init_app(
        app,
    )

    from api.events.event_routes import events_blueprint
    from api.user.user_routes import user_blueprint
    from api.auth.auth_routes import auth_blueprint
    from api.media.image_routes import media_blueprint

    app.register_blueprint(events_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(media_blueprint)

    return app
