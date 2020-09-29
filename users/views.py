from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from rest_framework import filters, mixins, viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser
# from rest_framework.decorators import action


# class UserViewSet(viewsets.ModelViewSet):
# @action(detail=True, methods=['post'])
# class UserViewSet(ListAPIView):
class UserListCreate(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAdminUser, )
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['username']
    search_fields = ['username', ]



    # username пользователь для фильтрации, поиск по части username
