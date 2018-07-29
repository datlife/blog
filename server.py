"""Create an application instance."""
from flask.helpers import get_debug_flag
from blog.app import create_app
from blog.settings import DevConfig, ProdConfig

# Create Flask App
app = create_app(DevConfig if get_debug_flag() else ProdConfig)

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'