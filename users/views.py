from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from .forms import Loginform, Registerform
from django.contrib.auth.forms import *

def Login(request):
    error = False
    if request.method != 'POST':
        form = Loginform()
    else:
        form = Loginform(data=request.POST)
        if form.is_valid():
            username = request.POST.get('usuario')
            password = request.POST.get('Senha')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                error = True
    context = {'form': form, 'error': error}
    return render(request, 'users/login.html', context)


def logout_view(request):
    """Faz um logout do usuario."""
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    """Faz o cadastro de um novo usuário."""
    error = False
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    
    if request.method != 'POST':
        # Exibe o fromulario de casdastro em branco
        form = Registerform()
    
    if request.method == 'POST':
        form = Registerform(data=request.POST)
        senha = request.POST.get('password1')
        senha2 = request.POST.get('password2')
        
        if senha != senha2:
            error = True
        
        # Processa o fromulario preenchido
        if form.is_valid():
            new_user = form.save()
            Username = request.POST.get('username')
            # Faz o login do usuario eo redireciona para a pagina inicial
            authenticate_user = authenticate(username=Username, password=senha)

            if authenticate_user:
                new_user.save()
                login(request, authenticate_user)
                return HttpResponseRedirect(reverse('index'))
            else:
                error = True
        
    context = {'form': form, 'error': error}
    return render(request, 'users/register.html', context)