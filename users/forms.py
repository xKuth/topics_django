from django import forms
from django.core.exceptions import ValidationError


class Loginform(forms.Form):
    usuario = forms.CharField(min_length=4, max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}), label='Úsuario')
    Senha = forms.CharField(min_length=4, max_length=64, widget=(forms.PasswordInput(attrs={'class': 'form-control'})))


    def clean_login(self):
        usuario = self.cleaned_data['usuario']
        if not(usuario.isalnum()):
            raise ValidationError('o nome de usário não pode ter caracteres especiais')
        return usuario


class Registerform(forms.Form):
    usuario = forms.CharField(max_length=15, min_length=6, widget=forms.TextInput(attrs={'class':'boxexinput', 'placeholder': 'Nome do usuario:'}), label='Úsuario:')
    senha = forms.CharField(min_length=8, max_length=64, widget=(forms.PasswordInput(attrs={'placeholder': 'Insira uma senha:'})), label='Senha:')
    senha2 = forms.CharField(min_length=8, max_length=64, widget=(forms.PasswordInput(attrs={'placeholder': 'Confirme a senha:'})), label= 'repita a senha:')

