from blog.database import db
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
# To migrate Database easier
migrate = Migrate()