from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Неоходимо ввести адрес электронной почты')
        # if not username:
        #     raise ValueError('Неоходимо ввести имя пользователя')

        user = self.model(
            email=self.normalize_email(email),
            # username=username,
            **extra_fields,
            )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
