from blog.database import db
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()    # handling encrypting sensitive data
migrate = Migrate()  # for easier data migration
