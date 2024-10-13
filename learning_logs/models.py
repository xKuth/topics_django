from django.db import models
from django.contrib.auth.models import User


# Classe dominante para topicos.
class Topic(models.Model):  
    """Um asssunto sobre qual o úsuario esta aprendendo"""
    text = models.CharField(max_length=200) # Definição de tamanho maximo de texto e tipo primitivo.
    date_added = models.DateTimeField(auto_now_add=True) # Data de criação de cada texto.
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # chave estrangeita para registro de usuarios unicos.
    

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text # retorno do texto.
 

 # Subclasse de topicos para entradas.
class Entry(models.Model):
    """Algo especififco aprendido sobre um assunto"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # chave estrangeira do detentor do topico.
    text = models.TextField() # tipo de texto e seu tipo primitivo.
    date_added = models.DateTimeField(auto_now_add=True) # Data da criação de cada anotação.

    class Meta:
        verbose_name_plural = 'entries' # Retorno de nome em plural se ouver mais de uma anotação.

    def __str__(self):
        """Delvolve uma representação em string do modelo"""
        return self.text[:20] + '...' # retorno de no maximo 20 caracters para representação no DB.