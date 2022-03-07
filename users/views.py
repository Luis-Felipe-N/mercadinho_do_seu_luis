from django.shortcuts import redirect, render
from django.views import View
from users.forms import RegisterForm

class LoginView(View):
    def get(self, request):
        return (request, 'users/login.html')

    # def post(self, request):
    #     # logar usuário
    #     ...


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()

        context = {
            'form': form
        }
        
        return render(request, './users/register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)

        # print(form)

        if form.is_valid:
            print('Sim, este form é válido!')

            form.save()

        return render(request, './users/register.html', {
            'form': form
        })

