from rest_framework import serializers

from apps.core.serializers import DynamicFieldsSerializerMixin
from apps.users.serializers import UserSerializer

from .models import Post


class PostSerializer(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    author = UserSerializer(fields=["username", "email"])

    class Meta:
        model = Post
        fields = "__all__"


class PostCreateUpdateDestroySerializer(
    DynamicFieldsSerializerMixin, serializers.ModelSerializer
):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ["author", "id", "title", "content", "created_at"]
