# -*- coding: utf-8 -*-
"""Defines fixtures available to all tests."""

import pytest
from webtest import TestApp

from blog.app import create_blog_app
from blog.database import db as _db
from blog.config import TestConfig

from .factories import UserFactory

@pytest.yield_fixture(scope='function')
def app():
    """An application for the tests."""
    _app = create_blog_app(TestConfig)
    with _app.app_context():
        _db.create_all()
    ctx = _app.test_request_context()
    ctx.push()
    yield _app
    ctx.pop()


@pytest.fixture(scope='function')
def testapp(app):
    """A Webtest app."""
    return TestApp(app)


@pytest.yield_fixture(scope='function')
def db(app):
    """A database for the tests."""
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    # Explicitly close DB connection
    _db.session.close()
    _db.drop_all()

@pytest.fixture
def user():
    """Create a mock user for all tests."""
    class User():
        def get():
            mock_user = UserFactory(password='icandoit')
