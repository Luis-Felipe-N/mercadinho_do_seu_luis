from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from mercado.models.Carrinho import Carrinho


class CarrinhoView(LoginRequiredMixin, ListView):
    template_name = 'mercado/pages/carrinho.html'
    model = Carrinho
    contect_object_name = 'produtos'

    def get_queryset(self):
        print(Carrinho.objects.all(), super().get_queryset().filter(usuario__id=self.request.user.id))

        return super().get_queryset().filter(usuario__id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["titulo_da_pagina"] = "Carrinho"
        return context