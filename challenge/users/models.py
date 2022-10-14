from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name='Username', max_length=32, unique=True, blank=False, null=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('username',)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.username)
