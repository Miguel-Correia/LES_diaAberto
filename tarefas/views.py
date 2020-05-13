import datetime

from django.shortcuts import render, redirect
from django.http import JsonResponse
from tarefas.models import Tarefa, TarefaSessaoAtividade, ColaboradorTarefa
from tarefas.forms import TarefaForm, TarefaAtividadeForm, TarefaTransporteForm
from django.core.paginator import Paginator


from atividades.models import UnidadeOrganica, SessaoAtividade, Inscricao, SessaoAtividadeInscricao, Utilizador


# Create your views here.

#---------------------------------------------------------
# Tarefas CRUD- Create Read Update Delete
#----------------------------------------------------------

def createTarefa(request):
    if request.method == 'GET':
        formTarefa = TarefaForm()
        #Change later so that id equals the UO of the autheticated Coordenador
        formTarefaAtividade = TarefaAtividadeForm(uoId = UnidadeOrganica.objects.get(id=1))
        formTarefaTransporte = TarefaTransporteForm()
    elif request.method == 'POST':
        formTarefa = TarefaForm(request.POST)
        formTarefaAtividade = TarefaAtividadeForm(request.POST, uoId = UnidadeOrganica.objects.get(id=1))
        formTarefaTransporte = TarefaTransporteForm(request.POST)

        if formTarefa.is_valid() and formTarefaTransporte.is_valid():
            t = formTarefa.save(commit=False)
            t.estado = False
            t.utilizadorid = Utilizador.objects.get(id=1) 
            t.sessao_atividade_inscricaoid_destino = SessaoAtividadeInscricao.objects.get(id = formTarefaTransporte.cleaned_data['sessaoAtividade_destino'])
            t.sessao_atividade_inscricaoid_origem = SessaoAtividadeInscricao.objects.get(id = formTarefaTransporte.cleaned_data['sessaoAtividade_origem'])
            t.origem = formTarefaTransporte.cleaned_data['origem']
            t.destino = formTarefaTransporte.cleaned_data['destino']
            t.horario = formTarefaTransporte.cleaned_data['horario']
            t.data = formTarefaTransporte.cleaned_data['dia']

            t.save()

        elif formTarefa.is_valid() and formTarefaAtividade.is_valid():
            t = formTarefa.save(commit=False)
            t.estado = False
            #Change for logged in user
            t.utilizadorid = Utilizador.objects.get(id=1)
            t.save()
            
            tarefa_SessaoAtividade = TarefaSessaoAtividade(
            tarefaid = t, 
            sessao_atividadeid = SessaoAtividade.objects.get(id = formTarefaAtividade.cleaned_data['sessaoAtividade'])
            )
            tarefa_SessaoAtividade.save()

        return redirect('tarefas:createTarefa')
    
    context = { 'formTarefa': formTarefa,
                'formTarefaAtividade': formTarefaAtividade,
                'formTarefaTransporte': formTarefaTransporte
                }

    return render(request, 'tarefas/AdicionarTarefa.html', context)

#Used in Create Tarefa to dynamically get the Sessoes Atividade of a the selected Atividade
#Returns a Json Response with the data of all the SessaoAtividades that have the atividadeid equal to atividadeid
def getSessoes(request, atividadeid):
    sessoes = [(sessaoAtividade.id, str(sessaoAtividade)) for sessaoAtividade in SessaoAtividade.objects.filter(atividadeid = atividadeid)]
    #print(sessoes)
    return JsonResponse(dict(sessoes))

#Used in Create Tarefa to dynamically get the inscrições from a spcified date
#Return as Json Response with the inscricoes from the given date
def getInscricoesByDate(request, date):
    inscricoes = [(inscricao.id, str(inscricao)) for inscricao in Inscricao.objects.filter(dia = date)]
    return JsonResponse(dict(inscricoes))

#Used to get all the sessaoAtividadeInscricao from a inscricao within a time period
#Returns a Json Response the sessoes that match the inscricaoid and are within the hora
def getSessoes_Inscricao(request, inscricaoid, hora):
    sessoesInsc = []
    for sessaoInsc in SessaoAtividadeInscricao.objects.filter(inscricaoid = inscricaoid):
        hora_inicio = datetime.datetime.combine(sessaoInsc.sessao_atividadeid.data ,sessaoInsc.sessao_atividadeid.sessaoid.hora_de_inicio)
        duracao = sessaoInsc.sessao_atividadeid.atividadeid.duracao
        
        #calculate the hora_fim with the duracao from atividade and hora_inicio from sessao
        hora_fim = hora_inicio + datetime.timedelta(minutes=duracao)

        #convert hora into a datetime obj
        hora_obj = datetime.datetime.strptime(hora, '%H:%M')

        #Only get Sessoes that end within a 20 minute gap of the selected hora
        if hora_fim.time() >= (hora_obj - datetime.timedelta(minutes=20)).time() and hora_fim.time() < (hora_obj + datetime.timedelta(minutes=20)).time():
            sessoesInsc.append((sessaoInsc.id, str(sessaoInsc.sessao_atividadeid.atividadeid.nome) + ", " + str(sessaoInsc.sessao_atividadeid.sessaoid)))
    
    return JsonResponse(dict(sessoesInsc))

def getLocal_Sessao(request, sessao_atividadeid):
    sessaoAtividade = SessaoAtividade.objects.get(id = sessao_atividadeid)
    local = sessaoAtividade.atividadeid.localid.descricao
    print(local)
    return JsonResponse({'local': local})


#Used to get all the sessaoAtividadeInscricao from a inscricao within a time period
#Returns a Json Response the sessoes that match the inscricaoid and are within the hora
def getSessoes_InscricaoNext(request, inscricaoid, hora):
    sessoesInsc = []
    for sessaoInsc in SessaoAtividadeInscricao.objects.filter(inscricaoid = inscricaoid):
        hora_inicio = datetime.datetime.combine(sessaoInsc.sessao_atividadeid.data ,sessaoInsc.sessao_atividadeid.sessaoid.hora_de_inicio)        

        #convert hora into a datetime obj
        hora_obj = datetime.datetime.strptime(hora, '%H:%M')

        #Only get Sessoes that end within a 20 minute gap of the selected hora
        if hora_inicio.time() >= (hora_obj - datetime.timedelta(minutes=20)).time() and hora_inicio.time() < (hora_obj + datetime.timedelta(minutes=20)).time():
            sessoesInsc.append((sessaoInsc.id, str(sessaoInsc.sessao_atividadeid.atividadeid.nome) + ", " + str(sessaoInsc.sessao_atividadeid.sessaoid)))
    
    return JsonResponse(dict(sessoesInsc))

def showTarefas(request):
    allTarefas = Tarefa.objects.all()

    paginator = Paginator(allTarefas, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj,}
    return render(request, 'tarefas/showTarefas.html', context)