from rest_framework import serializers
from .models import Category, Genre


class CategorySerializer(serializers.ModelSerializer):
    '''
    Сериализатор для категорий(типов) произведений:
    «Фильмы», «Книги», «Музыка»
    '''
    class Meta:
        fields = '__all__'
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для жанров произведений.
    Одно произведение может быть привязано к нескольким жанрам.
    '''
    class Meta:
        fields = '__all__'
        model = Genre


