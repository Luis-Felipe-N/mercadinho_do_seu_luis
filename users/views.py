from django.shortcuts import redirect, render
from django.views import View
from users.forms import RegisterForm
from django.contrib import messages

class LoginView(View):
    def get(self, request):
        return (request, 'users/login.html')

    # def post(self, request):
    #     # logar usuário
    #     ...


class RegisterView(View):
    template_name = './users/register.html'

    def get_template(self):
        form = RegisterForm()

        context = {
            'form': form
        }
        
        return render(self.request, self.template_name, context)

    def get(self, request):
        
        return self.get_template()

    def post(self, request):
        form = RegisterForm(request.POST)

        # print(form)

        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso')


        return self.get_template()

