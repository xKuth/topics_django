from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    """Faz um logout do usuario."""
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    """Faz o cadastro de um novo usuário."""
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    if request.method != 'POST':
        # Exibe o fromulario de casdastro em branco
        form = UserCreationForm()
    else:
        # Processa o fromulario preenchido
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Faz o login do usuario eo redireciona para a pagina inicial
            authenticate_user = authenticate(username = new_user.username, password = request.POST['password1'])
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)