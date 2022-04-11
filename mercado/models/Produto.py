from django.db import models
import locale

from mercado.models.Categoria import Categoria

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        blank=False,
        null=False,
        max_length=96,
        help_text='Ex: Motorola Moto g10',
    )

    descricao = models.TextField(
        verbose_name="Descrição",
        help_text="Ex: Este é o melhor produto do mundo"
    )

    descricao_html = models.TextField(
        verbose_name="Descrição em HTML",
        help_text="Ex: <h1>Este é o melhor produto do mundo</h1>",
        blank=True
    )

    preco = models.FloatField(
        verbose_name="Preço",
        blank=False,
        null=False,

    )

    vendedor = models.ForeignKey(
        'users.Vendedor',
        on_delete=models.CASCADE,
        null=True,
    )

    imagem = models.ImageField(upload_to="mercado/covers/%Y/%m/%d/")

    categoria = models.ForeignKey(
        'Categoria',
        on_delete=models.SET_NULL,
        null=True
    )

    desconto = models.FloatField(
        verbose_name="Porcentagem do desconto",
        blank=True,
        null=True
    )

    com_desconto = models.BooleanField(
        verbose_name="O Produto está com desconto",
        blank=True
    )

    data_criacao = models.DateField(
        verbose_name="Data de criação",
        auto_now=True,
    )

    def get_absolute_url(self):
        return '/produto/%i/' % self.pk
    

    def get_preco_formatado(self, *args, **kwargs):
        locale.setlocale( locale.LC_ALL, '' )
        preco_formatado = locale.currency(self.preco, symbol=False, grouping=True)
        return preco_formatado

    def get_quantidade_desconto(self):
        desconto = self.desconto
        return f'{int(desconto)}%'

    def get_preco_com_desconto(self):
        desconto = self.preco * (self.desconto / 100)

        preco_desconto = self.preco - desconto

        locale.setlocale( locale.LC_ALL, '' )
        preco_formatado = locale.currency(preco_desconto, symbol=False, grouping=True)

        return preco_formatado


    def __str__(self):
        return self.nome