import factory
from factory.django import DjangoModelFactory
from faker import Faker

from apps.posts.models import Post

__all__ = ["PostFactory"]


fake = Faker()


class PostFactory(DjangoModelFactory):
    author = factory.SubFactory("test.factories.UserFactory")
    title = factory.Faker("sentence", locale="ko_KR")
    content = factory.Faker("text", locale="ko_KR")
    created_at = factory.Faker("date_between", start_date="+0d", end_date="+10d")

    class Meta:
        model = Post
