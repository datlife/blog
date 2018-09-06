from blog.database import db
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

bcrypt = Bcrypt()    # handling encrypting sensitive data
migrate = Migrate()  # for easier data migration
admin = Admin()      #  manage admin