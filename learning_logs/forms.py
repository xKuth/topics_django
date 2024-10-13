from django import forms
from .models import Topic, Entry


# Formulario Dominante da classe Topicos
class TopicForm(forms.ModelForm):
    class Meta: # classe Topic de models
        model = Topic 
        fields = ['text']
        labels = {'text': ''}
        widgets =  {'text': forms.Textarea(attrs={'cols': 80})} 


# Subformulario da classe Entry
class EntryForm(forms.ModelForm):
    class Meta: 
        model = Entry # Classe Entry de models
        fields = ['text']
        labels = {'text': ''}
        widgets =  {'text': forms.Textarea(attrs={'cols': 80})}