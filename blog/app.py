from flask import Flask
from flask.helpers import get_debug_flag
from blog.exntesions import db, migrate
from blog.models import User, Post
from blog.settings import DevConfig, ProdConfig

def create_app(config_name=DevConfig):
    """Factory pattern:
    http://flask.pocoo.org/docs/1.0/patterns/appfactories/ 
    """
    app = Flask(__name__)
    app.config.from_object(config_name)
    register_extensions(app)
    register_shellcontext(app)
    return app


def register_extensions(app):
    """Register Flask extenstions."""
    with app.app_context():
        db.init_app(app)
    
    migrate.init_app(app, db)


def register_shellcontext(app):
    """Register shell context objects."""
    def shell_context():
        """Shell context objects."""
        return {
            'db': db,
            'User': User,
            'Post': Post,
        }

    app.shell_context_processor(shell_context)