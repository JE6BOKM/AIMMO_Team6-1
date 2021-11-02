from rest_framework import viewsets
from rest_framework.response import Response

from apps.comments.models import Comment
from apps.comments.permissions import IsCreatorOrReadOnly
from apps.comments.serializers import CommentCUDSerializer, CommentSerializer
from apps.core.serializers import ChooseSerializerClassMixin


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
    permission_classes = (IsCreatorOrReadOnly,)

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
