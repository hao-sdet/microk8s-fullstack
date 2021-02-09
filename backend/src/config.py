import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


class BaseConfig:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class Development(BaseConfig):
    DEBUG = True
    TESTING = False


class Production(BaseConfig):
    DEBUG = False
    TESTING = False


app_config = {
    'development': Development,
    'production': Production,
}
