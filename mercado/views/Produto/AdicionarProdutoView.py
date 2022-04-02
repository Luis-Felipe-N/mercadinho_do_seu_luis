from multiprocessing import context
from django.views import View
from mercado.forms.ProdutoForm import ProdutoForm

class AdicionarProdutoView(View):

    def get(self, *args, **kwargs):
        form = ProdutoForm()

        context = {
            "form": form
        }
        