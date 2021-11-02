from rest_framework.routers import DefaultRouter

from apps.users.views import UserCreateViewSet, UserViewSet

app_name = "users"

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"users", UserCreateViewSet)


urlpatterns = router.urls
