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

    def __init__(self, username, email, password=None, **kwargs):
        """Create User instance."""
        db.Model.__init__(self, username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        return bcrypt.check_password_hash(self.password, value)
