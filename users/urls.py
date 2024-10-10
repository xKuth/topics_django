from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login', views.Login , name='login'), # Rota de login
    path('logout', views.logout_view, name='logout'), # rota para saida de úsuario
    path('register', views.register, name='register'), # Rota para registrar úsuario
]


