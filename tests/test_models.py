import pytest
import datetime as dt
from blog.models import User, Post, Tags

@pytest.mark.usefixtures('db')
class TestPost:
    def test_create_new_post(self):
        post = Post('foo_title', 'foo_description', 'foo_body')
        post.save()
        assert isinstance(post.created, dt.datetime)
        assert bool(post.slug)  

    def test_add_tag(self, user):
        post = Post('foo_title', 'foo_description', 'foo_body')
        post.save()
        t = Tags(tagname='python')
        t1 = Tags(tagname='flask')
        assert post.add_tag(t)
        assert post.add_tag(t1)
        assert len(post.tag_list) == 2

    def test_remove_tag(self, user):
        post = Post('foo_title', 'foo_description', 'foo_body')
        post.save()
        t1 = Tags(tagname='flask')
        assert post.add_tag(t1)
        assert post.remove_tag(t1)
        assert len(post.tag_list) == 0
 
@pytest.mark.usefixtures('db')
class TestUser:
    def test_created_at_defaults_to_datetime(self):
        user = User(username='foo', email='foo@bar.com')
        user.save()
        assert bool(user.created_at)
        assert isinstance(user.created_at, dt.datetime)

    def test_password_is_nullable(self):
        """Test null password."""
        user = User(username='foo', email='foo@bar.com')
        user.save()
        assert user.password is None

    def test_check_password(self):
        """Check password."""
        user = User.create(username='foo', email='foo@bar.com',
                           password='foobarbaz123')
        assert user.check_password('foobarbaz123')
        assert not user.check_password('barfoobaz')