# from django.db import models

# from django.contrib.auth.models import (
#     BaseUserManager,
#     AbstractBaseUser,
#     PermissionsMixin,
# )


# class User( AbstractBaseUser, PermissionsMixin ):
#     email = models.CharField(
#         verbose_name="Email",
#         max_length=40,
#         unique=False
#     )

#     username = models.CharField(
#         verbose_name="Usuário",
#         max_length=40,
#         unique=True
#     )

#     first_name = models.CharField(
#         verbose_name="Primeiro nome",
#         max_length=40,
#     )

#     last_name = models.CharField(
#         verbose_name="Último nome",
#         max_length=40,
#     )

#     is_active = models.BooleanField(
#         verbose_name="Usuário está ativo",
#         default=True
#     )

#     is_staff = models.BooleanField(
#         verbose_name="Usuário é da equipe de desenvolvimento",
#         default=False
#     )

#     is_superuser = models.BooleanField(
#         verbose_name="Usuário é um super-usuário",
#         default=False
#     )

#     USERNAME_FIELD = 'username'

#     objects = BaseUserManager()

#     class Meta:
#         verbose_name = "Usuário"
#         verbose_name_plural = "Usuários"
#         db_table = "usuario"

#     def __str__(self):
#         return self.email