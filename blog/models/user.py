"""User Model."""
import datetime as dt

from blog.database import db, Model, Column, relationship
from blog.extensions import bcrypt


class User(Model):
    id = Column(db.Integer, primary_key=True)
    username = Column(db.String(64), index=True, unique=True, nullable=False)
    email    = Column(db.String(120), index=True, unique=True, nullable=False)
    password = Column(db.String(128))
    posts    = relationship('Post', backref='author', lazy='dynamic')
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __repr__(self):   # Display class in console, for debugging
        return '<User {}>'.format(self.username)

    def __init__(self, username="", email="", password=None, **kwargs):
        """Create User instance."""
        db.Model.__init__(self, username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None
    def __setattr__(self, name, value):
        if name in 'password':
            super(User, self).__setattr__(name, bcrypt.generate_password_hash(value))
        else:
            super(User, self).__setattr__(name, value)

    def set_password(self, new_password):
        self.password = bcrypt.generate_password_hash(new_password)

    def check_password(self, value):
        return bcrypt.check_password_hash(self.password, value)
