from mercado.models.Produto import Produto
from django import forms

class ProdutoForm(forms.ModelForm):

    # def __init__(self, *args, **kwargs):
    #     return super().__init__(self, *args, **kwargs)
    
    class Meta:
        model = Produto
        fields = [
            'nome', 'descricao',
            'descricao_html', 'preco',
            'imagem', 'categoria',
            'desconto', 'com_desconto'
        ]