from flask import Flask
from .views.main import main as main_blueprint
from .views.sheets import sheets as sheets_blueprint
from dotenv import load_dotenv
from app.database import db


def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(sheets_blueprint)

    return app
