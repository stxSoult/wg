from rest_framework import permissions


class OwnProfilePermission(permissions.BasePermission):
    """
    Object-level permission to only allow updating his own profile
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_superuser:
            return True

        try:
            return obj.user == request.user
        except AttributeError:
            return obj == request.user
        # obj here is a UserProfile instance
