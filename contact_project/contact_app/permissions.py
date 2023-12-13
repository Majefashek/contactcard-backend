from rest_framework.permissions import BasePermission

class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is logged in and authenticated
        return request.user and request.user.is_authenticated