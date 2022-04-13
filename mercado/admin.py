from django.contrib import admin

from mercado.models import *

admin.site.register(Produto)
admin.site.register(Categoria)

@admin.register(Carrinho)
class CarrinhoAdmin(admin.ModelAdmin):
    pass