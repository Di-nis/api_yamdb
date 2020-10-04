# Generated by Django 3.1 on 2020-10-04 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=40, null=True, verbose_name='Фамилия')),
                ('username', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('bio', models.TextField(blank=True, null=True, verbose_name='О себе')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Адрес электронной почты')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('role', models.CharField(choices=[('user', 'user'), ('moderator', 'moderator'), ('admin', 'admin')], default='user', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
