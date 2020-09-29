from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.generics import ListAPIView

from rest_framework import filters, mixins, viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.decorators import api_view, permission_classes


# class UserViewSet(viewsets.ModelViewSet):
# @action(detail=True, methods=['post'])
# class UserViewSet(ListAPIView):


# class UserListCreate(viewsets.ModelViewSet):
# @api_view(['GET', 'POST'])
# @action(methods=['post'], detail=True)
class UserListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['username']
    search_fields = ['username', ]
    # pagination_class = PageNumberPagination
    # pagination_class = LimitOffsetPagination

    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)


class UserRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # lookup_fields = ['username']
    lookup_url_kwarg = 'username'




    # username пользователь для фильтрации, поиск по части username
