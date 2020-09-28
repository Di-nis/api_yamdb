from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

# from rest_framework import filters, mixins, viewsets
from .models import User
from .serializers import UserSerializer


# class UserViewSet(viewsets.ModelViewSet):
class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly, OwnResourcePermission, )
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = ['username']
    # search_fields = ['=username', ]



    # username пользователь для фильтрации, поиск по части username
