from flask import Flask


def create_app(config_name):
    """Factory pattern:
    http://flask.pocoo.org/docs/1.0/patterns/appfactories/ 
    """
    app = Flask(__name__)
    app.config.from_object(config_name)
    register_extensions(app)

    #@TODO learn more about Blueprint
    from blog.models import User
    return app


def register_extensions(app):
    """Register Flask extenstions."""

    from blog.models import db
    db.init_app(app)    

    from flask_migrate import Migrate
    migrate = Migrate()
    migrate.init_app(app, db)

