from django.shortcuts import render, redirect
from django.http import JsonResponse
from tarefas.models import Tarefa, TarefaSessaoAtividade, ColaboradorTarefa
from tarefas.forms import TarefaForm, TarefaAtividadeForm

from atividades.models import UnidadeOrganica, SessaoAtividade


# Create your views here.

#---------------------------------------------------------
# Tarefas CRUD- Create Read Update Delete
#----------------------------------------------------------

def createTarefa(request):
    if request.method == 'GET':
        formTarefa = TarefaForm()
        #Change later so that id equals the UO of the autheticated Coordenador
        formTarefaAtividade = TarefaAtividadeForm(uoId = UnidadeOrganica.objects.get(id=1))
    elif request.method == 'POST':
        formTarefa = TarefaForm(request.POST)
        formTarefaAtividade = TarefaAtividadeForm(request.POST, uoId = UnidadeOrganica.objects.get(id=1))
        if formTarefa.is_valid() and formTarefaAtividade.is_valid():
            t = formTarefa.save()
            
            tarefa_SessaoAtividade = TarefaSessaoAtividade(
                tarefaid = t, 
                sessao_atividadeid = formTarefaAtividade.cleaned_data['sessaoAtividade'])
            tarefa_SessaoAtividade.save()

            return redirect('tarefas:createTarefa')
    
    context = { 'formTarefa': formTarefa,
                'formTarefaAtividade': formTarefaAtividade}

    return render(request, 'tarefas/AdicionarTarefa.html', context)

#Used in Create Tarefa to dynamically get the Sessoes Atividade of a the selected Atividade
#Returns a Json Response with the data of all the SessaoAtividades that have the atividadeid equal to atividadeid
def getSessoes(request, atividadeid):
    sessoes = [(sessaoAtividade.id, str(sessaoAtividade)) for sessaoAtividade in SessaoAtividade.objects.filter(atividadeid = atividadeid)]
    print(sessoes)
    return JsonResponse(dict(sessoes))