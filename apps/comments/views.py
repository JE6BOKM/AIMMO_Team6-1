from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.comments.permissions import IsAuth, IsCreatorOnly
from apps.core.serializers import ChooseSerializerClassMixin

from .models import Comment
from .serializers import CommentCUDSerializer, CommentSerializer


class CommentViewSet(ChooseSerializerClassMixin, viewsets.ModelViewSet):
    """
    Comment CRUD
    """

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    serializer_classes = {
        "create": CommentCUDSerializer,
        "update": CommentCUDSerializer,
    }
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_permissions(self):
        if self.action in ["list", "retreive"]:
            self.permission_classes = [AllowAny]
        elif self.action in ["create"]:
            self.permission_classes = [IsAuth]
        elif self.action in ["destroy", "update"]:
            self.permission_classes = [IsCreatorOnly]
        return super().get_permissions()

    def get_queryset(self):
        qs = super().get_queryset()

        post_id = self.request.query_params.get("post_id", "")
        if post_id:
            qs = qs.filter(post=post_id)
        return qs

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(parent=None).all()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
