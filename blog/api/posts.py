from marshmallow import fields
from flask import Blueprint, jsonify
from flask_apispec import marshal_with, use_kwargs

from blog.models import Post, Tags
from blog.exceptions import InvalidUsage

# Define blueprint for Posts API
blueprint = Blueprint('posts', __name__)

@blueprint.route('/api/posts', method=('GET'))
@use_kwargs(
    {'tag': fields.Str(),
     'limit': fields.Int(), 
     'offset': fields.Int()})
def get_articles(tag=None, limit=5, offset=0):
    res = Post.query
    if tag is not None:
        res = res.filter(Post.tagList.any(Tags.tagname == tag))
    return res.offset(offset).limit(limit).all()

@blueprint.route('/api/posts/<slug>', methods=('GET',))
def get_article(slug):
    post = Post.query.filter_by(slug=slug).first()
    if post is None:
        raise InvalidUsage.article_not_found()
    return post