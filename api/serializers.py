from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
from .models import Category, Genre

class CategorySerializer(serializers.modelSerializer):
    '''
    Сериализатор для категорий(типов) произведений:
    «Фильмы», «Книги», «Музыка»
    '''
    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.modelSerializer):
    '''
    Сериализатор для жанров произведений.
    Одно произведение может быть привязано к нескольким жанрам.
    '''
    class Meta:
        fields = ('name', 'slug')
        model = Genre


