from django.views import View
from django.shortcuts import render
from mercado.models.Produto import Produto

# Dá para usar o TemplateView, não vou usar porqus estou aprendendo
class HomeView(View):
    template_name = 'mercado/pages/home.html'

    def get_template(self, context):
        try:
            print(self.request.user.vendedor)
        except:
            print('não tem vendedor aqui')

        return render(self.request, self.template_name, context)

    def get(self, request):

        user = request.user

        produtos = Produto.objects.all()

        context = {
            'user': user,
            'produtos': produtos
        }

        return self.get_template(context)
        