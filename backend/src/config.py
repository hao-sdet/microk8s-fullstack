import os


class BaseConfig:
    DEBUG = False


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
