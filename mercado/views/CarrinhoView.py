from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin



class CarrinhoView(LoginRequiredMixin, ListView):
    template_name = ''
    # model = 