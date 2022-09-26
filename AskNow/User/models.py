from django.db import models
from django.contrib.auth.models import AbstractUser
from User.managers import CustomUserManager


class User(AbstractUser):
    email = models.EmailField(
        verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(
        verbose_name='created_at', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='updated_at', auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
