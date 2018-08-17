from abc import ABC


class Config(ABC):

    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):

    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/content.db"


class TestingConfig(Config):

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/test.db"
