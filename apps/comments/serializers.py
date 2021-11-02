from rest_framework import serializers

from apps.users.serializers import UserSerializer
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()
    user = UserSerializer(fields=["id", "username", "email"])

    class Meta:
        model = Comment
        fields = ("id", "user", "post", "created_at", "updated_at", "parent", "comment", "reply")
        read_only_fields = ["user"]

    def get_reply(self, instance):
        serializer = self.__class__(instance.reply, many=True)
        serializer.bind("", self)
        return serializer.data


class CommentCUDSerializer(serializers.ModelSerializer):
    user = UserSerializer(fields=["id", "username", "email"])

    class Meta:
        model = Comment
        fields = ["user", "comment", "parent", "post"]
