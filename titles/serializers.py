from rest_framework import serializers

from titles.models import Category, Comment, Genre, Review, Title


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'slug']
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'slug']
        model = Genre


class TitleCreateSerializer(serializers.ModelSerializer):
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
    genre = GenreSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        fields = '__all__'
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    def validate(self, data):
        super().validate(data)
        if self.context['request'].method != 'POST':
            return data
        user = self.context['request'].user
        title_id = (
            self.context['request'].parser_context['kwargs']['title_id']
        )
        if Review.objects.filter(author=user, title__id=title_id).exists():
            raise serializers.ValidationError(
                "Вы уже оставили отзыв на данное произведение")
        return data

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username',read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
