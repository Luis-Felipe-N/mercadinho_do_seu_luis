from django.views import View
from django.shortcuts import render

class HomeView(View):
    template_name = 'pages/home.html'

    def get_template(self, context):

        

        return render(self.request, self.template_name, context)

    def get(self, request):

        user = request.user

        context = {
            'user': user
        }

        return self.get_template(context)
        

    def post(self, request):

        cep = request.POST.get('search')

        print(cep)
        return self.get_template()
        