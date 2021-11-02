from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path, reverse_lazy
from django.views.generic.base import RedirectView

from rest_framework.routers import DefaultRouter

from apps.comments.views import CommentViewSet
from apps.posts.views import PostViewSet

from .users.views import UserCreateViewSet, UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"users", UserCreateViewSet)
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)

api_v1_urls = router.urls

api_v1_urls += [
    path("accounts/", include("dj_rest_auth.urls")),
    path("accounts/", include("dj_rest_auth.registration.urls")),
]


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_v1_urls)),
    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r"^$", RedirectView.as_view(url=reverse_lazy("api-root"), permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
