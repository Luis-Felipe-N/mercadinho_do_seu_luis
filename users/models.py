"""
from django.db import models

from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

# Create your models here.
class UserManage( BaseUserManager ):
    def create_user(self, email: str, password: str) -> dict:  

        user = self.model(
            email = self.normalize_email( email )
        )

        user.is_active = True
        user.is_staff = False
        user.is_superuser = False

        user.set_password( password )
        user.save()
        
        return user


class User( AbstractBaseUser ):
    email = models.CharField(
        verbose_name="Usuário",
        max_length=40,
        unique=False
    )

    is_active = models.BooleanField(
        verbose_name="Usuário está ativo",
        default=True
    )

    is_staff = models.BooleanField(
        verbose_name="Usuário é da equipe de desenvolvimento",
        default=False
    )

    is_superuser = models.BooleanField(
        verbose_name="Usuário é um super-usuário",
        default=False
    )

    USERNAME_FIELD = 'email'

    objects = UserManage()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "usuario"

    def __str__(self):
        return self.email
"""