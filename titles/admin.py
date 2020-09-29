from django.contrib import admin

from .models import Category, Genre


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "slug")
    search_fields = ("name",)
    empty_value_display = "-пусто-"


class GenreAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "slug")
    search_fields = ("name",)
    empty_value_display = "-пусто-"



admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
