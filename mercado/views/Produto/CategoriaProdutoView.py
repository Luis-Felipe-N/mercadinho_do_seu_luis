from http.client import ImproperConnectionState
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views.generic.list import ListView
from django.core.exceptions import ObjectDoesNotExist

from mercado.models.Produto import Produto
from mercado.models.Categoria import Categoria

class CategoriaProdutoView(ListView):
    template_name = ''
    model = Produto

    def get(self, request, slug):
        categoria = get_object_or_404(Categoria, slug=slug)

        produtos = categoria.produto_set.all()
        categoria_nome = categoria.nome

        context = {
            "produtos": produtos,
            "categoria_nome": categoria_nome
        }

        return render(request, 'mercado/pages/categoria.html', context)