from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

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


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    # def validate(self, data):
    #     super().validate(data)
    #     if self.context['request'].method != 'POST':
    #         return data
    #     user = self.context['request'].user
    #     title_id = (
    #         self.context['request'].parser_context['kwargs']['title_id']
    #     )
    #     if Review.objects.filter(author=user, title__id=title_id).exists():
    #         raise serializers.ValidationError(
    #             "Вы уже оставили отзыв на данное произведение")
    #     return data

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date')

        # validators = [ 
        #     UniqueTogetherValidator( 
        #         queryset=Review.objects.all(), 
        #         fields=['author', 'title'] 
        #     )
        # ]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')


class TitleListSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    # rating = serializers.SerializerMethodField()
    # rating = serializers.IntegerField()
    # review = ReviewSerializer(many=True)

    # def get_rating(self, obj):
    #     return sum([review.score for review in obj.reviews.all()]) / obj.reviews.count()

    class Meta:
        # fields = '__all__'
        fields = ('id', 'name', 'year', 'genre', 'category', 'description')
        model = Title
