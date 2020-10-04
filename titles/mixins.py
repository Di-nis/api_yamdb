from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .permissions import IsAdmin, IsModerator, IsOwner, IsUser


class ReviewCommentMixin(viewsets.ModelViewSet):
    permission_classes = [IsOwner]
    permission_classes_by_action = {'list': [AllowAny],
                                    'create': [IsUser | IsAdmin | IsModerator],
                                    'retrieve': [AllowAny],
                                    'partial_update': [IsOwner],
                                    'destroy': [IsAdmin | IsModerator]}

    def get_permissions(self):
        try:
            return [permission() for permission
                    in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
