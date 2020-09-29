from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("pk", "username")
    search_fields = ("username",)
    # list_filter = ("pub_date",)
    # empty_value_display = '-пусто-'

admin.site.register(User, UserAdmin)