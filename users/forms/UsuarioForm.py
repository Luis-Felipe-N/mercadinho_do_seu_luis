from django import forms
from django.core.exceptions import ValidationError

from users.models.Usuario import Usuario

def strong_password(password):
    if len(password) < 8:
        raise ValidationError(
            'Sua senha deve haver 8 ou mais caracteres',
            code="invalid"
        )

class RegisterUsuarioForm(forms.ModelForm):

    # password = forms.PasswordInput(
    #     required=True,
    #     widget=forms.PasswordInput(),
    #     validators=[strong_password],
    #     error_messages = {
    #         'required': 'Senha obrigatória',
    #         'invalid': 'Sua senha deve haver 8 ou mais caracteres',
    #         'noconfirm': 'As senhas não coincidem'
    #     }
    # )

    confirmar_senha = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        label="Confirmar Senha",
        error_messages = {
            'required': 'Senha obrigatória',
            'noconfirm': 'As senhas não coincidem'
        }
    )

    class Meta:
        model = Usuario
        fields = [
            'first_name', 
            'last_name',
            'username', 
            'email',
            'password'
        ]

    def clean(self):
        cleaned_data = super().clean()

        senha_primaria = cleaned_data.get("password")
        senha_secondaria = cleaned_data.get("confirmar_senha")

        if senha_primaria != senha_secondaria   :

            self.add_error('password', 'As senhas não coincidem')

            raise ValidationError(
                'As senhas não coincidem',
                code='noconfirm'
            )

        return super().clean()

class LoginForm(forms.ModelForm):



    class Meta:
        model = Usuario
        fields = [
                'username',
                'password'
        ]
