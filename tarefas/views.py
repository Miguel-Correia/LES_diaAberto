from django.shortcuts import render, redirect
from tarefas.models import Tarefa, TarefaSessaoAtividade, ColaboradorTarefa
from tarefas.forms import TarefaForm


# Create your views here.

#---------------------------------------------------------
# Tarefas CRUD- Create Read Update Delete
#----------------------------------------------------------

def createTarefa(request):
    if request.method == 'GET':
        formTarefa = TarefaForm()
    elif request.method == 'POST':
        formTarefa = TarefaForm(request.POST)
        if formTarefa.is_valid():
            formTarefa.save()
            return redirect('tarefas:createTarefa')
    
    context = {'formTarefa': formTarefa}

    return render(request, 'tarefas/AdicionarTarefa.html', context)