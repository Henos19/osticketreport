from flask import Flask
from .views.main import main as main_blueprint

from dotenv import load_dotenv

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.register_blueprint(main_blueprint)

    return app
