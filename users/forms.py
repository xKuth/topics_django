from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, forms


class Loginform(forms.Form): # Classe para criar um formulario.
    usuario = forms.CharField(min_length=4, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Úsuario')
    Senha = forms.CharField(min_length=4, max_length=64, widget=(forms.PasswordInput(attrs={'class': 'form-control'})))  
    

    def clean_login(self):# Função para retornar um erro de formulario em português
        usuario = self.cleaned_data['usuario']
        if not(usuario.isalnum()):
            raise ValidationError('o nome de usário não pode ter caracteres especiais')
        return usuario


class Registerform(UserCreationForm): # Classe para criar um formulario para cadastro em português.
        username = forms.CharField(label='Nome de usuario', max_length=15, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome de úsuario'})) # Modificando field de username para português.
        password1 = forms.CharField(min_length=8, max_length=64, widget=(forms.PasswordInput(attrs={'placeholder': 'Insira uma senha:', 'class': 'form-control'})), label='Senha:') # modificando field de 1º senha para português.
        password2 = forms.CharField(min_length=8, max_length=64, widget=(forms.PasswordInput(attrs={'placeholder': 'Confirme a senha:', 'class': 'form-control'})), label= 'repita a senha:') # modificando field de 2º senha para português.
        error_messages = {
            'password_mismatch': ('As senhas não estão correspondendo.') # Retorno de erro de formulario de senhas desiguais.
        }


        class Meta: # Classe de Usercreate para trazer formulario pré prontos.
            model = User
            fields = ['username', 'password1', 'password2']


        def clean_username(self): # Função para retornar erro na pagina em português de formularios.
            usuario = self.cleaned_data['username']
            if not usuario.isalnum():
                raise forms.ValidationError('O NOME DE ÚSUARIO NÃO PODE CONTER CARACTERES ESPECIAIS, ou conter espaços.')
            elif usuario == ' ':
                raise forms.ValidationError('O campo de Usuario não pode estar vazio.')
            return usuario
        
        