"""User Model."""
from blog.database import SurrogatePK, db

class User(SurrogatePK, db.Model):
    # limit str to 64 optimizing memory footprint
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)  
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    posts  = db.relationship('Post', backref='author', lazy='dynamic')
    
    def __repr__(self):   # Display class in console, for debugging
        return '<User {}>'.format(self.username)

    def __init__(self, username, email, password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None