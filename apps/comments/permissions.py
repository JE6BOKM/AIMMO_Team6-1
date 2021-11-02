from rest_framework.permissions import IsAuthenticated, BasePermission


class IsAuth(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # filter out anonymous user
        if is_authenticated := super().has_permission(request, view):
            return obj.author == request.user
        return is_authenticated


class IsCreatorOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # filter out anonymous user
        if request.user.is_authenticated:
            if hasattr(obj, "user"):
                return obj.user.id == request.user.id
            return False
        else:
            return False
