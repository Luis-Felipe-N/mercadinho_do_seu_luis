from django.contrib.auth.models import User
from django import forms

def strong_password(password):
    if len(password) < 8:
        raise forms.ValidationError(
            (
                'Sua senha deve haver mais de 6 caracteres'
            ),
            code="invalid"
        )

class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        validators=[strong_password],
        error_messages = {
            'required': 'Senha obrigatoria',
            'invalid': 'Senha inválida'
        }
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