import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from test.factories import PostFactory, UserFactory

pytestmark = pytest.mark.django_db


class TestPostViewSet:
    def test_post_list(
        self,
        no_auth_client,
        post_list_schema,
    ):
        post_list_url = reverse("posts:post-list")

        # Test signup success
        resp = no_auth_client.get(post_list_url)
        assert resp.status_code == status.HTTP_200_OK
        assert post_list_schema.is_valid(resp.json())

    def test_create_post(
        self,
        client,
        post_detail_schema,
    ):
        payload = {"title": "Sample title", "content": "hwllo my name is bye"}

        post_create_url = reverse("posts:post-list")

        resp = client.post(post_create_url, data=payload, format="json")
        assert resp.status_code == status.HTTP_201_CREATED
        assert post_detail_schema.is_valid(resp.json())

    def test_delete_post(self, client, user):
        other_user = UserFactory()
        sample_post = PostFactory(author=other_user)

        # Only can author delete own post
        post_delete_url = reverse("posts:post-detail", kwargs={"pk": sample_post.pk})

        resp = client.delete(post_delete_url)
        assert resp.status_code == status.HTTP_403_FORBIDDEN

        post_delete_url = reverse(
            "posts:post-detail", kwargs={"pk": user.posts.first().pk}
        )
        resp = client.delete(post_delete_url)
        assert resp.status_code == status.HTTP_204_NO_CONTENT
