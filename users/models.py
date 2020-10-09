from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .managers import MyUserManager


class User(AbstractBaseUser):

    class UserRole(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'

    first_name = models.CharField('Имя', null=True, blank=True, max_length=40)
    last_name = models.CharField('Фамилия',
                                 null=True,
                                 blank=True,
                                 max_length=40)
    username = models.CharField(max_length=30,
                                unique=True,
                                null=True,
                                blank=True)
    bio = models.TextField("О себе", null=True, blank=True)
    email = models.EmailField(verbose_name='Адрес электронной почты',
                              unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.USER
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_staff

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
