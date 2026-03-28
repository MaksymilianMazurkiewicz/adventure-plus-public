from flask import Flask
from .models_manager import models_manager

def create_app():
    app = Flask(__name__)
    from .routes import main
    app.register_blueprint(main)

    return app

def cleanup():
    models_manager.cleanup()

