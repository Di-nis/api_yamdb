from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdministrator(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.admin
        # return False
        # if request.user.admin:
        #     return True
        # return False

    # def has_object_permission(self, request, view):
    #     if request.method in SAFE_METHODS:
    #         return True
    #     if request.user.is_authenticated:
    #         return request.user.admin