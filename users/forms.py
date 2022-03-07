from django.contrib.auth.models import User
from django import forms

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name',
            'username', 
            'email',
            'password'
        ]

        widgets = {
            'password': forms.PasswordInput(attrs={
                'type': 'password'
            })
        }

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