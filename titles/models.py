from django.db import models

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
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        related_name="category_titles", 
        null=True, 
        blank=True
    )

