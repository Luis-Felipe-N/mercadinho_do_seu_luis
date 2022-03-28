from tabnanny import verbose
from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        blank=False,
        null=False
    )

    descricao = models.TextField(
        verbose_name="Descrição",
    )

    descricao_html = models.TextField(
        verbose_name="Descrição em HTML",
    )

    preco = models.IntegerField(
        verbose_name="Preço",
        blank=False,
        null=False
    )

    vedendor = models.Man