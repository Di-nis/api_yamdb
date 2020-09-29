from rest_framework import serializers
from titles.models import Category, Genre, Title

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


class TitleCreateSerializer(serializers.ModelSerializer):
    '''Сериализатор для добавления произведений'''
    genre = serializers.SlugRelatedField(
        slug_field='slug', 
        many=True, 
        queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug', 
        queryset=Category.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Title


class TitleListSerializer(serializers.ModelSerializer):
    '''Сериализатор для возврата списка произведений'''
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.FloatField()

    class Meta:
        fields = '__all__'
        model = Title
