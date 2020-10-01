from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (filters, mixins, permissions, serializers, status,
                            viewsets)
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)

from .filters import TitleFilter
from .models import Category, Genre, Title
from .permissions import IsAdministratorOrReadOnly
from .serializers import (CategorySerializer, GenreSerializer,
                          TitleCreateSerializer, TitleListSerializer)


class CategoriesViewSet(BaseCreateListDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAdministratorOrReadOnly, ]
    search_fields = ['=name', ]
    lookup_field = 'slug'


class GenresViewSet(BaseCreateListDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = [IsAdministratorOrReadOnly, ]
    search_fields = ['=name', ]
    lookup_field = 'slug'
    

class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter
    permission_classes = [IsAdministratorOrReadOnly, ]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TitleCreateSerializer
        return TitleListSerializer
