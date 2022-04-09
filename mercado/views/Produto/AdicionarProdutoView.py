from multiprocessing import context
from urllib import request
from django.views import View
from mercado.forms.ProdutoForm import ProdutoForm
from django.shortcuts import render

class AdicionarProdutoView(View):

    def get(self, request, *args, **kwargs):
        form = ProdutoForm()

        context = {
            "form": form,
            "titulo_da_pagina": "Adicionar produto"
        }

        return render(request, 'mercado/pages/form-produto.html', context)
