from django.shortcuts import redirect, render
from django.views import View
from users.forms.VendedorForm import RegisterVendedorForm


class RegisterVendedorView(View):
    template_name = 'users/register-vendedor.html'

    def get_template(self, form):

        context = {
            "form": form
        }

        return render(self.request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        form = RegisterVendedorForm()

        return self.get_template(form)

    def post(self, request, *args, **kwargs):
        
        form = RegisterVendedorForm(request.POST)

        if form.is_valid():
            vendedor = form.save(commit=False)

            vendedor.username = request.user

            vendedor.username.is_vendedor = True

            form.save()

            return redirect('mercado:home')

        return self.get_template(form)