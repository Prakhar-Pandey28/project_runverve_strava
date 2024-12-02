from flask import Flask
from config import Config
import logging

def create_app():
    app = Flask(__name__)
    
    # Configure the app
    app.config.from_object(Config)
    
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    
    # Import and register blueprints
    from .routes import main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app