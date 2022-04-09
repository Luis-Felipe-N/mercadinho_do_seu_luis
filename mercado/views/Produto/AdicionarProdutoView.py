from multiprocessing import context
from pyexpat import model
from re import template
from urllib import request
from django.views.generic.edit import CreateView
from mercado.forms.ProdutoForm import ProdutoForm
from django.shortcuts import render

class AdicionarProdutoView(CreateView):
    template_name = 'mercado/pages/form-produto.html'
    model = ProdutoForm
    form = ProdutoForm

    def get(self, request, *args, **kwargs):
        form = ProdutoForm()

        context = {
            "form": form,
            "titulo_da_pagina": "Adicionar produto"
        }

        return render(request, 'mercado/pages/form-produto.html', context)

    def post(self, request, *args, **kwargs):
        form = ProdutoForm(request.POST)

        if form.is_valid():
            form.save(commit=False)