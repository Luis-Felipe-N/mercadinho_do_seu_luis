from django.shortcuts import redirect, render
from django.views import View
from users.forms.VendedorForm import RegisterVendedorForm


class RegisterVendedorView(View):
    template_name = 'users/register-vendedor.html'

    def get_template(self):
        form = RegisterVendedorForm()

        context = {
            "form": form
        }

        return render(self.request, self.template_name, context)

    def get(self, request, *args, **kwargs):

        return self.get_template()

    def post(self, request, *args, **kwargs):
        
        form = RegisterVendedorForm(request.POST)
        print(dir(request.user))


        if form.is_valid():
            vendedor = form.save(commit=False)

            vendedor.username = request.user

            request.user.is_vendedor = True

            form.save()

            return redirect('mercado:home')

        return self.get_template()