import os

from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from dotenv import load_dotenv

from db import db
from crypt import bcrypt

from resources import UserBlueprint

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["API_TITLE"] = "Tabocão Onboard REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    migrate = Migrate(app, db) # Habilita o Flask-Migrate

    api = Api(app)
    api.register_blueprint(UserBlueprint)

    bcrypt.init_app(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)