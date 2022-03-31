from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
from django.db import models

class Vendedor(AbstractBaseUser, PermissionsMixin):

    username = models.OneToOneField(
        'users.Usuario',
        on_delete=models.CASCADE,
        null=True
    )

    nome_loja = models.TextField(
        verbose_name="Nome da loja"
    )

    nome_completo = models.TextField(
        verbose_name="Nome completo",
    )

    cnpj = models.TextField(
        verbose_name="CNPJ sem formatação",
        blank=False,
        null=False,
        max_length=14
    )

    endereco = models.TextField(
        verbose_name="Endereço",

    )

    telefone = models.TextField(
        verbose_name="Telefone",
        max_length=11
    )



    class Meta:
        verbose_name = "Vendedor"
        db_table = "vendedor"

    def __str__(self):
        return self.nome_completo
