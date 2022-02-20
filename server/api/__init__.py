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

    from api.commands.events import insert_events_into_database

    app.cli.add_command(insert_events_into_database)

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)

    from api.events.routes import events_blueprint
    from api.user.user_routes import user_blueprint
    from api.auth.auth_routes import auth_blueprint

    app.register_blueprint(events_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(auth_blueprint)

    return app
