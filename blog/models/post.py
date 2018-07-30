"""Post Model."""
from datetime import datetime
from slugify import slugify
from blog.database import SurrogatePK, db

class Post(SurrogatePK, db.Model):

    slug = db.Column(db.Text, unique=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.Text)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):   # Display class in console, for debugging
        return '<Post {}>'.format(self.body)

    def __init__(self, author, title, description, body, slug=None, **kwargs):
        db.Model.__init__(self, author=author, title=title, description=description, 
                          body=body, slug=slug or slugify(title), **kwargs)