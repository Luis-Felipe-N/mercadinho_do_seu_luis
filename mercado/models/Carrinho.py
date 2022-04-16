from django.db import models

class Carrinho(models.Model):
    usuario = models.ForeignKey(
        'users.Usuario',
        on_delete=models.CASCADE
    )

    data_criacao = models.DateTimeField(
        auto_created=True,
        verbose_name="Data de criação"
    )

    produto = models.ForeignKey(
        'mercado.Produto',
        on_delete=models.CASCADE
    )

    quantidade = models.IntegerField(
        verbose_name="Quantidade",
        default=1,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.produto.nome