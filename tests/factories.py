# -*- coding: utf-8 -*-
"""Factories to help in tests."""
from factory import PostGenerationMethodCall, Sequence
from factory.alchemy import SQLAlchemyModelFactory

from blog.database import db
from blog.models import User

class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""
    class Meta:
        """Factory configuration."""
        abstract = True
        sqlalchemy_session = db.session

class UserFactory(BaseFactory):
    user = Sequence(lambda n: 'user{0}'.format(n))
    email = Sequence(lambda n: 'user{0}@bar.com'.format(n))
    password = PostGenerationMethodCall('set_password', 'example')

    class Meta:
        """Factory configuration."""
        model = User
