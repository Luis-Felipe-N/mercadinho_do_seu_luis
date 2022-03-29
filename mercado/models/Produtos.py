from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        blank=False,
        null=False,
        max_length=96
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

    vendendor = models.ForeignKey(
        'Vendedor',
        on_delete=models.CASCADE,
    )

    imagem = models.ImageField(upload_to="mercado/covers/%Y/%m/%d/", null=True)

    def __str__(self):
        return self.nome