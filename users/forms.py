from django import forms
from django.core.exceptions import ValidationError

class Loginform(forms.Form):
    login = forms.CharField(max_length=30)
    senha = forms.CharField(max_length=30, widget=(forms.PasswordInput))

    def clean_login(self):
        nome= self.cleaned_data['login']
        if not(nome.isalnum()):
            raise ValidationError('o nome de usário não pode ter caracteres especiais')
        return nome
