from rest_framework import filters
from rest_framework import permissions
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin

from .models import Category, Genre, Title
from .serializers import (TitleListSerializer, TitleCreateSerializer, 
                          GenreSerializer, CategorySerializer)
# from .permissions import IsAdminOrAuthor
# from .filters import TitleFilter


class BaseCreateListDestroyViewSet(
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class CategoriesViewSet(BaseCreateListDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    # permission_classes = [IsAdminOrAuthor, ]
    search_fields = ['=name', ]
    lookup_field = 'slug'


class GenresViewSet(BaseCreateListDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    # permission_classes = [IsAdminOrAuthor, ]
    search_fields = ['=name', ]
    lookup_field = 'slug'
    

class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    filter_backends = [DjangoFilterBackend]
    lookup_field = 'id'
    # filterset_class = TitleFilter
    # permission_classes = [IsAdminOrAuthor, ]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return TitleCreateSerializer
        return TitleListSerializer
