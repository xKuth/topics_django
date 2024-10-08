from django.shortcuts import render
from . models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request): # Rendiriza a pagina principal
    """Pagina principal do learning_log"""
    return render(request, 'learning_logs/index.html')


@login_required 
def topics(request): # renderiza a pagina com todos topicos criados
    """Mostra todos os assuntos"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') # Filtra os topicos do DB ordenados-os.
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id): # renderiza o topico desejado com sua id especifica.
    """Mostra um unico assunto e todas suas entradas. """
    topic = Topic.objects.get(id = topic_id)
    # Garante que o assunto pertence ao usuario atual
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries} 
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request): # Rediriza um formulario para a criação de um novo topico
    """Adiciona um novo assunto."""
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulario em branco´
        form = TopicForm()
    else:
        # dados de Post submetidos; processa od dados
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('topics'))
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id): # Renderiza um formulario para a criação de uma anotação de em um topico.
    """Acresenta uma nova entra para um assunto em particular."""
    topic = Topic.objects.get(id = topic_id)
    if topic.owner != request.user: # Garante que o assunto pertence ao usuario atual
        raise Http404
    if request.method != 'POST':
        # Nenhum dado submetido; cria um formulario em branco
        form = EntryForm()
    else:
        # Dados de Post submetidos; processa os dados
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
    context = {'topic': topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id): # Renderiza um formulario para a edição de uma anotação de um formulario.
    """Edita uma entrada existente."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user: # Garante que o assunto pertence ao usuario atual
        raise Http404
    if request.method != 'POST':
        # Requisição inicial preenche previamnete o formulario com a entrada atual
        form = EntryForm(instance=entry)
    else:
        # Dados de post submetidos; processa os dados
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


def edit_topic(request, topic_id): # Renderiza um formulario para a edição de um topico em um formulario.
    id = Topic.objects.get(id=topic_id)
    topic = Topic.objects.get(text=id)
    if request.method != 'POST': # # Requisição inicial preenche previamnete o formulario com a entrada atual
       form = TopicForm(instance=topic)
    if request.method == 'POST': # Dados de post submetidos; processa os dados
        form = TopicForm(instance=topic, data=request.POST)
        form.is_valid()
        form.save()
        return HttpResponseRedirect(reverse('topics'))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_topic.html', context)




@login_required
def delete_entry(request, entry_id): # Função para deletar uma anotação em um topico.
    if request.method == 'POST': # Se for um metodo POST ele ira apagar a anotação.
        entry = Entry.objects.get(id=entry_id)
        Entry.objects.get(id=entry_id).delete()
        topic = entry.topic_id
        return HttpResponseRedirect(f'/topics/{topic}')
    raise Http404

@login_required
def delete_topic(request, topic_id): # Função para deletar um topico e suas anotações por ser conectado atraves de uma ForeignKey.
    if request.method == 'POST': # Se for um metodo POST ele ira apagar o topico.
        Topic.objects.get(id=topic_id).delete()
        return HttpResponseRedirect('/topics')
    raise Http404

