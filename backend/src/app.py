from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .models import db, bcrypt
from .config import app_config

from .views.UserView import user_api_blueprint


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(app_config[env])

    # initialize database
    bcrypt.init_app(app)
    db.init_app(app)

    # register api blueprints
    app.register_blueprint(user_api_blueprint, url_prefix='/v1/users')

    @app.route('/', methods=['GET'])
    def index():
        return 'Welcome to Flask!'

    return app
