from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_cache import Cache


db = SQLAlchemy()
cache = Cache()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    app = Flask(__name__)
    with app.app_context():
        from .v1 import api as api_v1_blueprint
        app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')
        return app
