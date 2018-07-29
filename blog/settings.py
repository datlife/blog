"""Server Configuration."""
import os
from datetime import timedelta

class Config(object):
    """Base Configuration."""
    SECRET_KEY = os.environ.get('SERVER_SECRET_KEY', 'yaya')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # current directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    CACHE_TYPE = 'simple'  # Or 'memcached', 'redis', etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    """Production Configuration."""
    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                             default='sqlite:///' + os.path.join(
                                                Config.APP_DIR, 'app.db'))


class DevConfig(Config):
    """Development Configuration."""

    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    # Set the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    CACHE_TYPE = 'simple' # or 'memcached', 'redis'.
    JWT_EXPIRATION_DELTA = timedelta(10**6)