from rest_framework import serializers

from titles.models import Category, Genre, Title, Review, Comment


class CategorySerializer(serializers.ModelSerializer):
    '''
    Сериализатор для категорий(типов) произведений:
    «Фильмы», «Книги», «Музыка»
    '''
    class Meta:
        fields = ['name', 'slug']
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    '''
    Сериализатор для жанров произведений.
    Одно произведение может быть привязано к нескольким жанрам.
    '''
    class Meta:
        fields = ['name', 'slug']
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

    class Meta:
        fields = '__all__'
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    title_id = serializers.ReadOnlyField(source='title.pk')
    score = serializers.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
