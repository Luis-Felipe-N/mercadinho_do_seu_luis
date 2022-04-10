from django.contrib import messages
from django.views.generic.edit import CreateView
from mercado.forms.ProdutoForm import ProdutoForm
from django.shortcuts import render

class AdicionarProdutoView(CreateView):
    template_name = 'mercado/pages/form-produto.html'
    model = ProdutoForm
    form_class = ProdutoForm
    sucess_url = 'mercado:home'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.vendedor = self.request.POST.user__vendedor
        print(self.request.POST.user__vendedor)
        return super().form_valid(form)

    def get_sucess_url():
        messages.sucess('Produto cadastrado com sucesso')

        return 'mercado:home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo_da_pagina"] = "Adicionar produto"
        return context
    