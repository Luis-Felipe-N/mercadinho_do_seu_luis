from multiprocessing import context
from urllib import request
from django.views import View
from mercado.forms.ProdutoForm import ProdutoForm
from django.shortcuts import render

class AdicionarProdutoView(View):

    def get(self, *args, **kwargs):
        form = ProdutoForm()

        context = {
            "form": form
        }

        return render(request, 'mercado/pages/form-produto.html', context)
