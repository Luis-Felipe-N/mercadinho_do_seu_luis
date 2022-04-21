from django.views.generic.list import ListView
from django.core.exceptions import ObjectDoesNotExist

from mercado.models.Produto import Produto
from mercado.models.Categoria import Categoria

class CategoriaProdutoView(ListView):
    template_name = 'mercado/pages/produtos.html'
    model = Categoria
    context_object_name = 'produtos'
    
    def get_queryset(self):
        slug = self.kwargs["slug"]
        return super().get_queryset().get(slug=slug).produto_set.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        slug = self.kwargs["slug"]
        categoria = Categoria.objects.get(slug=slug)

        titulo_da_pagina = f'Categoria: {categoria.nome}' 
        context["titulo_da_pagina"] = titulo_da_pagina

        return context
