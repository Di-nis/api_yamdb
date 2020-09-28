from django.db import models

# Create your models here.

class Category(models.Model):
    '''Категории (типы) произведений'''
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)


class Genre(models.Model):
    '''Жанры'''
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)


