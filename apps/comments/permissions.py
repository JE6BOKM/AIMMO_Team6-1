from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAuthenticated


class IsAuth(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # filter out anonymous user
        if is_authenticated := super().has_permission(request, view):
            return obj.author == request.user
        return is_authenticated


class IsCreatorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # only access object craeted user
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS:
                return True
            elif hasattr(obj, "user"):
                return obj.user.id == request.user.id
            return False
        else:
            return False
