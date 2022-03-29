from django.contrib import admin
from mercado.models.Produtos import Produto

from mercado.models.Vendedor import Vendedor

admin.site.register(Vendedor)
admin.site.register(Produto)