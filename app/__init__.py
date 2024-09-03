from flask import Flask
from flask_sqlalchemy import SQLAlchemy


database = SQLAlchemy()


def create_webapp(app_key: str, database_uri: str) -> Flask:
    flask_app = Flask(
        import_name=__name__, template_folder="templates", static_folder="assets"
    )

    flask_app.config["SECRET_KEY"] = app_key
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    database.init_app(app=flask_app)

    from app.blueprints import core, authentication

    flask_app.register_blueprint(core, url_prefix="/")
    flask_app.register_blueprint(authentication, url_prefix="/authentication")

    with flask_app.app_context():
        database.create_all()

    return flask_app
