from django.shortcuts import redirect, render
from django.views import View
from users.forms.UsuarioForm import RegisterUsuarioForm, LoginForm

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView as LoginViewClass

from users.models.Usuario import Usuario

class LoginView(LoginViewClass):
    template_name = './users/login.html'

    def get_template(self, *args, **kwargs):
        form = LoginForm()

        context = {
            'form': form
        }
        
        return render(self.request, self.template_name, context)

    def get(self, request):
        return self.get_template()

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        print(password)

        user = authenticate(request, username=username, password=password)

        # print(username, password, user)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login feito com sucesso')
            return redirect('mercado:home')

        # if form.is_valid():
        #     print('pelo menos vem até aqui')
            
        


class RegisterUsuarioView(View):
    template_name = './users/register.html'

    def get_template(self, form, *args, **kwargs):

        context = {
            'form': form
        }
        
        return render(self.request, self.template_name, context)

    def get(self, request):
        form = RegisterUsuarioForm()
        
        return self.get_template(form)

    def post(self, request):
        form = RegisterUsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso')
            redirect('users:login')


        return self.get_template(form)

