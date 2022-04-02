from dataclasses import field
from django.contrib.auth.models import User
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

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        validators=[strong_password],
        error_messages = {
            'required': 'Senha obrigatória',
            'invalid': 'Sua senha deve haver 8 ou mais caracteres'
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

class LoginForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = Usuario
        fields = [
                'username',
                'password'
        ]
