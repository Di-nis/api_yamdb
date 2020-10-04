from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdministratorOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == 'admin' or request.user.is_staff
        if request.method in SAFE_METHODS:
            return True
        return False


class IsStaffOrOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            obj.author == request.user or
            request.method in permissions.SAFE_METHODS or
            request.user.role == request.user.UserRole.MODERATOR or
            request.user.role == request.user.UserRole.ADMIN
        )
