from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    email = models.EmailField(
        verbose_name="Email do usuário",
        max_length=30,
        unique=True
    )

    is_vendedor = models.BooleanField(
        verbose_name="É um vendedor",
        default=False
    )

    # USERNAME_FIELD = 'email'