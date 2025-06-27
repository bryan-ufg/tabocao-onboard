import os

from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from dotenv import load_dotenv
from apscheduler.schedulers.background import BackgroundScheduler

from db import db
from crypt import bcrypt
from jwt_auth import jwt
from sync import fetch_and_sync_placeholder

from resources import UserBlueprint
from resources import DriverBlueprint
from resources import TruckBlueprint
from resources import TripBlueprint
from resources import ASOBlueprint
from resources import TruckMaintenanceBlueprint
from resources import MockDataBlueprint
from resources import APIPlaceholderBlueprint

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
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    db.init_app(app)

    migrate = Migrate(app, db) # Habilita o Flask-Migrate

    api = Api(app)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(DriverBlueprint)
    api.register_blueprint(TruckBlueprint)
    api.register_blueprint(TripBlueprint)
    api.register_blueprint(ASOBlueprint)
    api.register_blueprint(TruckMaintenanceBlueprint)
    api.register_blueprint(MockDataBlueprint)
    api.register_blueprint(APIPlaceholderBlueprint)

    bcrypt.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        scheduler = BackgroundScheduler()
        scheduler.add_job(fetch_and_sync_placeholder, 'interval', hours=1, id='fetch_and_sync_placeholder_job', args=[app], replace_existing=True)
        scheduler.start()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)