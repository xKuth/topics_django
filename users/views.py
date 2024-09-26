from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import Loginform, Registerform


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
    else:
        # Processa o fromulario preenchido
        form = Registerform(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Faz o login do usuario eo redireciona para a pagina inicial
            authenticate_user = authenticate(username = new_user.usuario, password = request.POST['senha'])
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('index'))
            error = True
    context = {'form': form, 'error': error}
    return render(request, 'users/register.html', context)