from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdministratorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role=='admin' or request.user.is_staff
        if request.method in SAFE_METHODS:
            return True
        return False
