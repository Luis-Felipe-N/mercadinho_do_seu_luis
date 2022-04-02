from pyexpat import model
from re import template
from django.views.generic.list import ListView
from mercado.models.Produto import Produto

class CategoriaProdutoView(ListView):
    template_name = ''
    model = Produto