from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from .forms import Loginform, Registerform
from django.contrib.auth.forms import *

def Login(request): # redenrização da pagina login
    error = False
    if request.method != 'POST': # recebe um formulario caso seja um metodo GET.
        form = Loginform()
    else:
        form = Loginform(data=request.POST) # vai salvar o envio de um formulario caso seja metodo POST.
        if form.is_valid():
            username = request.POST.get('usuario')
            password = request.POST.get('Senha')
            user = authenticate(username=username, password=password) # autentica o usuario passados pelo usuario.
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('index')) # Redireciona o usuario para pagina principal.
            else:
                error = True
    context = {'form': form, 'error': error}
    return render(request, 'users/login.html', context) # rendiriza a pagina caso seja metodo GET ou possua errors.


def logout_view(request):
    """Faz um logout do usuario."""
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request): # redenrização da pagina de registrar
    """Faz o cadastro de um novo usuário."""
    error = False
    if request.user.is_authenticated: # retorna a pagina inicial caso estaja logado
        return HttpResponseRedirect(reverse('index'))
    
    if request.method != 'POST':
        # Exibe o fromulario de casdastro em branco
        form = Registerform()
    
    if request.method == 'POST': # caso seja um novo formulario enviado
        form = Registerform(data=request.POST) # recebe o novo formulario enviado
        senha = request.POST.get('password1') # recebe a 1º senha
        senha2 = request.POST.get('password2') # recebe a 2º senha
        
        if senha != senha2: # compara as duas senhas.
            error = True
        
        # Processa o fromulario preenchido
        if form.is_valid() and not error: # verifica se o formulario é valido e não possui error nas senhas.
            new_user = form.save()
            Username = request.POST.get('username')
            # Faz o login do usuario eo redireciona para a pagina inicial
            authenticate_user = authenticate(username=Username, password=senha) # autentica o usuario e a senha criada.

            if authenticate_user: # Se o usuario estiver logado ele salva o novo usuario no DB.
                new_user.save()
                login(request, authenticate_user)
                return HttpResponseRedirect(reverse('index')) # retorna a pagina inicial
            else:
                error = True
        
    context = {'form': form, 'error': error}
    return render(request, 'users/register.html', context) # renderiza a pagina caso seja um metodo GET ou possua errors.