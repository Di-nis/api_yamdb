from django.shortcuts import render

# Create your views here.
from .models import Category,  Genre
from .serializers import (
    CategorySerializer,
    GenreSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    '''
    Для модели категорий (типов) произведений:
    «Фильмы», «Книги», «Музыка»
    '''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=name')


class GenreViewSet(viewsets.ModelViewSet):
    '''
    Для жанров произведений. Одно произведение 
    может быть привязано к нескольким жанрам.
    '''
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=name',)
    
