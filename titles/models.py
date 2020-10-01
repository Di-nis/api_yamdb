from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User

class Category(models.Model):
    '''Категории (типы) произведений'''
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    '''Жанры'''
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.TextField(max_length=50)
    year = models.IntegerField("Год выпуска")
    description = models.TextField(max_length=500)
    genre = models.ManyToManyField(Genre)
    # rating = models.IntegerField(verbose_name="Рейтинг",
    #     default=5,
    #     validators=[
    #         MinValueValidator(1),
    #         MaxValueValidator(10)
    #     # min_value=0, max_value=10, 
    #     ]
    # )
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        related_name="category_titles", 
        null=True, 
        blank=True
    )


class Review(models.Model):
    SCORE_CHOICES = zip(range(1, 11), range(1, 11))
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='review'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.IntegerField(choices=SCORE_CHOICES, default=1)
    pub_date = models.DateTimeField(
        'Дата публикации отзыва',
        auto_now_add=True,
    )


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comment'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comment'
    )
    pub_date = models.DateTimeField(
        'Дата публикации комментария',
        auto_now_add=True
    )