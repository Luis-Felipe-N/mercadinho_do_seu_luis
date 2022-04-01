from users.models.Vendedor import Vendedor
from django import forms

class RegisterVendedorForm(forms.ModelForm):

    class Meta:
        model = Vendedor
        fields = [
            'nome_loja',
            'nome_completo',
            'cnpj',
            'endereco',
            'telefone'
        ]

        # Adicionar validador de cnpj