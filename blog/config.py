"""Base Config Object for Development/Production."""
import os
from datetime import timedelta


class _BaseConfig():
    """Base Configuration for Blog App."""
    # Your current terminal should have $SERVER_SECRET_KEY$ variable
    SECRET_KEY = os.environ.get('SERVER_SECRET_KEY')

    # Import current directory
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    CACHE_TYPE = 'simple'  # Or 'memcached', 'redis', etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(_BaseConfig):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                             'postgresql://localhost/example')


class DevConfig(_BaseConfig):
    """Development Configuration."""

    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    # Put the db file in project root
    DB_PATH = os.path.join(_BaseConfig.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)

    # Determine if signal the app there is changes in object. (okay in dev mode)
    JWT_EXPIRATION_DELTA = timedelta(10**6)
    CACHE_TYPE = 'simple'  # or 'memcached', 'redis'.


class TestConfig(_BaseConfig):
    """Test configuration."""
    TESTING = True
    DEBUG = True
    # For Test, we use in-memory database
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    BCRYPT_LOG_ROUNDS = 4
