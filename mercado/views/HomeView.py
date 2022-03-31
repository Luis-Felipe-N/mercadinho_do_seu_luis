from django.views import View
from django.shortcuts import render
from mercado.models.Produto import Produto

# Dá para usar o TemplateView, não vou usar porqus estou aprendendo
class HomeView(View):
    template_name = 'pages/home.html'

    def get_template(self, context):

        return render(self.request, 'pages/home.html', context)

    def get(self, request):

        user = request.user

        produtos = Produto.objects.all()

        context = {
            'user': user,
            'produtos': produtos
        }

        return self.get_template(context)
        