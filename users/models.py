# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# from django.contrib.auth.models import PermissionsMixin
# from authemail.models import EmailUserManager, EmailAbstractUser


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Неоходимо ввести адрес электронной почты')
        if not username:
            raise ValueError('Неоходимо ввести имя пользователя')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# USER_CHOICES = [
#     ('US', 'user'),
#     ('MO', 'moderator'),
#     ('AD', 'admin')
# ]


# class User(EmailAbstractUser):
# class User(AbstractBaseUser, PermissionsMixin):
class User(AbstractBaseUser):
    first_name = models.CharField('Имя', null=True, blank=True, max_length=40)
    last_name = models.CharField('Фамилия', null=True, blank=True, max_length=40)
    username = models.CharField(max_length=30, unique=True)
    bio = models.TextField("О себе", null=True, blank=True)
    email = models.EmailField(verbose_name='Адрес электронной почты', unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USER = 'US'
    MODERATOR = 'MO'
    ADMIN = 'AD'
    USER_CHOICES = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin')
    ]
    role = models.CharField(
        max_length=2,
        choices=USER_CHOICES,
        default=USER,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


