from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),# Rota para: Pagina inicial.
    path('topics', views.topics, name='topics'),# Rota para: Pagina com todos topicos.
    path('topics/<topic_id>/', views.topic, name='topic'),# Rota para: pagina do topico.
    path('new_topic', views.new_topic, name='new_topic'),# Rota para: Pagina para adicionar um novo topico.
    path('edit_topic/<topic_id>/', views.edit_topic, name='edit_topic'),# Rota para: Pagina de editar o topico.
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),# Rota para: Pagina para editar uma anotação dentro do topico.
    path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'),# Rota para: Pagina para editar anotação dentro do topico.
    path('delete/<entry_id>/', views.delete_entry, name='delete_entry'),# Rota para: Deletar uma anotação de um topico.
    path('delete_topic/<topic_id>/', views.delete_topic, name='delete_topic'),# Rota para: Deletar um topico com todas anotações dentro.
] 