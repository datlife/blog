from flask import Flask
from blog.extensions import db, migrate, admin, ModelView
from blog.models import User, Post, Tags


def create_blog_app(config_name):
    """Factory pattern: http://flask.pocoo.org/docs/1.0/patterns/appfactories/ 
    """
    app = Flask(__name__)
    app.config.from_object(config_name)
    register_extensions(app)
    register_shellcontext(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    migrate.init_app(app, db)

    # Init a GUI Admin Page for database management
    admin.init_app(app)
    admin.add_view(ModelView(Post, db.session))
    admin.add_view(ModelView(User, db.session))


def register_shellcontext(app):
    """Register shell context objects."""
    def shell_context():
        """Shell context objects."""
        return {
            'db': db,
            'User': User,
            'Post': Post,
            'Tag': Tags
        }
    app.shell_context_processor(shell_context)

