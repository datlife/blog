"""Post Model."""
from datetime import datetime
from slugify import slugify
from flask_jwt_extended import current_user

from blog.database import db
from sqlalchemy.orm import relationship

tag_assoc = db.Table("tag_assoc",
                     db.Column("tag",
                               db.Integer,
                               db.ForeignKey("tags.id")),
                     db.Column("post",
                               db.Integer,
                               db.ForeignKey("post.id")))


class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tagname = db.Column(db.String(100))
    def __init__(self, tagname):
        db.Model.__init__(self, tagname=tagname)
    def __repr__(self):
        return '<Tag {}}>'.format(self.tagname)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.Text, unique=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    tag_list = relationship('Tags', secondary=tag_assoc, backref='posts')
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):   # Display class in console, for debugging
        return '<Post {}>'.format(self.body)

    def __init__(self, title="", description="", body="", slug=None, **kwargs):
        db.Model.__init__(self,
                          title=title,
                          description=description,
                          body=body,
                          slug=slug or slugify(title),
                          **kwargs)

    def add_tag(self, tag):
        if tag not in self.tag_list:
            self.tag_list.append(tag)
            return True
        return False

    def remove_tag(self, tag):
        if tag in self.tag_list:
            self.tag_list.remove(tag)
            return True
        return False
