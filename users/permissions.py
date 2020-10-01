from rest_framework.permissions import BasePermission


class IsAdministrator(BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role=='admin' or request.user.is_staff
        return False
