from mercado.models.Produto import Produto
from django import forms

class ProdutoForm(forms.ModelForm):


    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'span-3'
            }
        )
    )

    descricao = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'span-3'
            }
        )
    )

    descricao_html = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'span-3'
            }
        )
    )

    com_desconto = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'label-row'
            }
        )
    )

    

    imagem = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'label-imagem',
                'data': 'inputImage'}
        )
    )
    
    class Meta:
        model = Produto
        fields = [
            'nome', 'descricao',
            'descricao_html', 'preco',
            'imagem', 'categoria',
            'desconto', 'com_desconto'
        ]