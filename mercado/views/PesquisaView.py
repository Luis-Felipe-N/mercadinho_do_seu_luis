from mercado.models.Produto import Produto
from django.views.generic.list import ListView
from django.db.models import Q

class PesquisaView(ListView):
    template_name = 'mercado/pages/produtos.html'
    model = Produto
    context_object_name = 'produtos'

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('q')
        return super().get_queryset().filter(Q(nome__icontains=termo_pesquisa))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        termo_pesquisa = self.request.GET.get('q')
        print(self.request.GET.get('q'))

        context["titulo_da_pagina"] = f'Pesquisa por: {termo_pesquisa}'
        context["termo_pesquisa"] = termo_pesquisa

        return context