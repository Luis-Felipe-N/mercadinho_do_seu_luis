from django.contrib.auth.models import User
from django.db import models

class Vendedor(models.Model):
    # usuario = models.OneToOneField(
    #     'User', # Nâo funciona, Por que não é um model
    #     verbose_name="Usuário",
    #     on_delete=models.CASCADE
    # )

    nome_loja = models.TextField(
        verbose_name="Nome da loja"
    )

    nome_completo = models.TextField(
        verbose_name="Nome completo",
    )

    cnpj = models.TextField(
        verbose_name="CNPJ",
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

    def __str__(self):
        return self.nome_completo