from django.views.generic.edit import UpdateView
from django.shortcuts import render
from django.db.models import Q

from mercado.models.Produto import Produto
from mercado.forms.ProdutoForm import ProdutoForm


class EditarProdutoView(UpdateView):
    template_name = template_name = 'mercado/pages/form-produto.html'
    model = Produto
    form_class = ProdutoForm

    def get(self, request, id):
        produto = Produto.objects.get(Q(vendedor__id=self.request.user.vendedor.id) & Q(id=id))
        form = ProdutoForm(instance=produto)

        context = {
            "form": form
        }

        return render(request, self.template_name, context)