from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

def strong_password(password):
    if len(password) < 8:
        raise ValidationError(
            'Sua senha deve haver 8 ou mais caracteres',
            code="invalid"
        )

class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        validators=[strong_password],
        error_messages = {
            'required': 'Senha obrigatória',
            'invalid': 'Sua senha deve haver 8 ou mais caracteres'
        }
    )

    nome_vendedor = forms.CharField(
        required=True
    )

    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name',
            'username', 
            'email',
            'password'
        ]

        # widgets = {
        #     'password':
        # }


    # Propria validação de um campo | clean_nomecampo
    def clean_password(self):
        data = self.cleaned_data.get('password')

        # Logica da validação
        # if 'palavrão' in data:
            # retorna erro
            
            # raise ValidationError(
            #     'Não é válido palavrão',
            #     code="invalid_word"
            # )
            
            # É possivel pegar o error em error_messages
            

        return data