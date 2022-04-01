from django.views import View
from django.shortcuts import render
from mercado.models.Produto import Produto

class ProdutoView(View):
    template_name = "mercado/pages/produto-detalhe.html"
    
    def get(self, request, id):
        produto = Produto.objects.get(pk=id)

        context = {
            "produto": produto
        }

        return render(request, self.template_name, context)