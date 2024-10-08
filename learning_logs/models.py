from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):  
    """Um asssunto sobre qual o úsuario esta aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text

class Entry(models.Model):
    """Algo especififco aprendido sobre um assunto"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Delvolve uma representação em string do modelo"""
        return self.text[:20] + '...'