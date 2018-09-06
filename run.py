"""Create a blog app instance."""
from flask.helpers import get_debug_flag
from blog.app import create_blog_app
from blog.config import DevConfig, ProdConfig


app = create_blog_app(DevConfig if get_debug_flag() else ProdConfig)
