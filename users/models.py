from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .managers import MyUserManager


class User(AbstractBaseUser):
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
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    class UserRole(models.TextChoices):
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'
    # user = 'user'
    # moderator = 'moderator'
    # admin = 'admin'
    # USER_CHOICES = (
    #     (user, 'user'),
    #     (moderator, 'moderator'),
    #     (admin, 'admin')
    # )
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.USER
        # choices=USER_CHOICES,
        # default=user,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


    @property
    def administrator(self):
        if request.user.is_authenticated:
            return request.user.role == 'admin' or request.user.is_staff
        return False

    # @property
    # def is_moderator(self):
    #     return self.is_admin



    # class UserRole:
    #     USER = 'user'
    #     ADMIN = 'admin'
    #     MODERATOR = 'moderator'
    #     choices = [
    #         (USER, 'user'),
    #         (ADMIN, 'admin'),
    #         (MODERATOR, 'moderator'),
    #     ]
