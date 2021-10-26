from rest_framework import permissions


class IsAuthor(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # filter out anonymous user
        if is_authenticated := super().has_permission(request, view):
            return obj.author == request.user
        return is_authenticated
