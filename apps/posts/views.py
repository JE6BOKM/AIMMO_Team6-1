from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from apps.core.serializers import ChooseSerializerClassMixin
from apps.posts.permissons import IsAuthor

from .models import Post
from .serializers import PostCreateUpdateDestroySerializer, PostSerializer


class PostViewSet(ChooseSerializerClassMixin, viewsets.ModelViewSet):
    """
    Post CRUd
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    serializer_classes = {
        "create": PostCreateUpdateDestroySerializer,
        "update": PostCreateUpdateDestroySerializer,
    }
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_permissions(self):
        if self.action in ["list", "retreive"]:
            self.permission_classes = [AllowAny]
        elif self.action in ["destroy", "update"]:
            self.permission_classes = [IsAuthor]
        return super().get_permissions()

    def get_queryset(self):
        category = self.request.GET['category']
        queryset = self.queryset.filter(category__name=category)
        return queryset