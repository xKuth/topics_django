from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.forms import UserCreationForm


class Loginform(forms.Form):
    usuario = forms.CharField(min_length=4, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Úsuario')
    Senha = forms.CharField(min_length=4, max_length=64, widget=(forms.PasswordInput(attrs={'class': 'form-control'})))  
    


    def clean_login(self):
        usuario = self.cleaned_data['usuario']
        if not(usuario.isalnum()):
            raise ValidationError('o nome de usário não pode ter caracteres especiais')
        return usuario


class Registerform(UserCreationForm): 
        username = forms.CharField(label='Nome de usuario', max_length=15, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome de úsuario'}))
        password1 = forms.CharField(min_length=8, max_length=64, widget=(forms.PasswordInput(attrs={'placeholder': 'Insira uma senha:', 'class': 'form-control'})), label='Senha:')
        password2 = forms.CharField(min_length=8, max_length=64, widget=(forms.PasswordInput(attrs={'placeholder': 'Confirme a senha:', 'class': 'form-control'})), label= 'repita a senha:')
        error_messages = {
            'password_mismatch': ('As senhas não estão correspondendo.'),
            'password_is_common': ('A senha esta muito fraca.'),
        }


        class Meta:
            model = User
            fields = ['username', 'password1', 'password2']


        def clean_username(self):
            usuario = self.cleaned_data['username']
            if not usuario.isalnum():
                raise forms.ValidationError('O NOME DE ÚSUARIO NÃO PODE CONTER CARACTERES ESPECIAIS.')
            elif usuario == None:
                raise forms.ValidationError('O campo de Usuario não pode estar vazio.')
            return usuario
        
        