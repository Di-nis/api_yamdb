from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Avg

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
    rating = models.IntegerField(default=None, null=True, blank=True)
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        related_name="category_titles", 
        null=True, 
        blank=True
    )

    def update_rating(self):
        self.rating = self.review.all().aggregate(Avg('score'))['score__avg']
        self.save()


class Review(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='review')
    score = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    title_id = models.ForeignKey(Title, on_delete=models.CASCADE,
                                 related_name='review')

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comments')
    pub_date = models.DateTimeField(auto_now_add=True)
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE,
                                  related_name='comments')

    def __str__(self):
        return self.text