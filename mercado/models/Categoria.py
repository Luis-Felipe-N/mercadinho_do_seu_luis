from django.db import models

class Categoria(models.Model):
    nome = models.CharField(
        verbose_name="Categoria",
        max_length=96
    )

    def __str__(self):
        return self.nome