from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView
from users.forms.VendedorForm import RegisterVendedorForm
from users.models.Usuario import Usuario


from users.models.Vendedor import Vendedor

class RegisterVendedorView(LoginRequiredMixin ,CreateView):
    template_name = 'users/register-vendedor.html'
    model = Vendedor
    form_class= RegisterVendedorForm
    success_url = 'mercado:home'

    def dispatch(self, request, *args, **kwargs):
        usuario_vendedor = self.request.user.vendedor is not None
        if usuario_vendedor:
            messages.error(self.request, 'Usuário já é vendedor')
            return redirect('mercado:home')
        return super().dispatch(request, *args, **kwargs)
    

    def form_valid(self, form):
        self.request.user.is_vendedor = True
        form.instance.username = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Agora você é um vendedor')
        

    # def get_template(self, form):

    #     context = {
    #         "form": form
    #     }

    #     return render(self.request, self.template_name, context)

    # def get(self, request, *args, **kwargs):
    #     form = RegisterVendedorForm()

    #     return self.get_template(form)

    # def post(self, request, *args, **kwargs):
        
    #     form = RegisterVendedorForm(request.POST)

    #     if form.is_valid():
    #         vendedor = form.save(commit=False)

    #         vendedor.username = request.user

    #         vendedor.username.is_vendedor = True

    #         form.save()

    #         return redirect('mercado:home')

    #     return self.get_template(form)