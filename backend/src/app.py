from flask import Flask
from .config import app_config


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(app_config[env])

    @app.route('/', methods=['GET'])
    def index():
        return 'Welcome to Flask!'

    return app
