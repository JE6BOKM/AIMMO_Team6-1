from django.db.models import Q

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from apps.core.serializers import ChooseSerializerClassMixin
from apps.posts.permissons import IsAuthor

from .models import Post, UserCount
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
        category = self.request.GET.get("category", None)
        search = self.request.GET.get("search_word", None)
        q = Q

        if category and search:
            q = Q(category__name=category) & Q(title__icontains=search)
        elif category:
            q = Q(category__name=category)
        elif search:
            q = Q(title__icontains=search)
        else:
            return self.queryset
        queryset = self.queryset.filter(q)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        if UserCount.objects.filter(post=obj, user=request.user).exists():
            return super().retrieve(request, *args, **kwargs)

        UserCount.objects.create(post=obj, user=request.user)
        obj.views += 1
        obj.save(update_fields=["views"])
        return super().retrieve(request, *args, **kwargs)
