from tabnanny import verbose
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(
        verbose_name="Categoria",
        max_length=96
    )

    class Meta:
        verbose_name = "Categoria"
        db_table = "categoria"

    def __str__(self):
        return self.nome