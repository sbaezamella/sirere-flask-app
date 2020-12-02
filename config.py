import os

basedir = os.path.abspath(os.path.dirname(__file__))


# pylint: disable=too-few-public-methods
class Config():
    DEBUG = False
    TESTING = False
    # SECRET_KEY = os.getenv(
    #     'SECRET_KEY', 'secret-key-goes-here')
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv('MYSQL_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# pylint: disable=too-few-public-methods
class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = 'development'


# pylint: disable=too-few-public-methods
class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False


# pylint: disable=too-few-public-methods
class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}
