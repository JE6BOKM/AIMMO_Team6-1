from django.contrib.sessions.middleware import SessionMiddleware
from django.test import RequestFactory

import pytest
from dj_rest_auth.utils import jwt_encode
from rest_framework.test import APIClient

from apps.users.models import User
from test.factories import UserFactory

pytest_plugins = ["test.schema", "test.factories"]
pytestmark = pytest.mark.django_db


@pytest.fixture
def user() -> User:
    user = UserFactory(name="testuser", eth_address=None, signature=None)
    return user


@pytest.fixture
def client(user):
    access, __ = jwt_encode(user)  # access, refresh
    headers = {"HTTP_AUTHORIZATION": f"Bearer {access}"}
    client = APIClient()
    client.credentials(**headers)
    return client


@pytest.fixture
def no_auth_client():
    client = APIClient()
    return client


@pytest.fixture
def fake_request(rf: RequestFactory, user):
    # build "request" for the test: needed to populate HiddenField(default=serializers.CreateUserDefault())
    request = rf.get("/fake-url/")
    # Django Test Case Error 'WSGIRequest' object has no attribute 'session'
    # https://stackoverflow.com/questions/35659676/django-test-case-error-wsgirequest-object-has-no-attribute-session
    middleware = SessionMiddleware()
    middleware.process_request(request)
    request.session.save()
    request.user = user
    return request
