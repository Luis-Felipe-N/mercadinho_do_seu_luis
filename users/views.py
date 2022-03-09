from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.views import View
from users.forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

class LoginView(View):
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
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login feito com sucesso')
            return redirect('home')
        else:
            raise ValidationError('Senha ou email inválido', code='invalid')
        


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

        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso')


        return self.get_template()

