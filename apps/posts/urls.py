from rest_framework.routers import DefaultRouter

from apps.posts.views import PostViewSet

app_name = "posts"

router = DefaultRouter()
router.register(r"posts", PostViewSet)


urlpatterns = router.urls
