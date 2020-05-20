import datetime

from django.shortcuts import render, redirect
from django.http import JsonResponse
from tarefas.models import Tarefa, ColaboradorTarefa, InscricaoTarefa
from tarefas.forms import TarefaForm, TarefaAtividadeForm, TarefaTransporteForm, TarefaGruposForm, TarefaGruposFormset, ColaboradorTarefaForm
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
        formTarefaAtividade = TarefaAtividadeForm(request.GET or None, uoId = UnidadeOrganica.objects.get(id=1))
        formTarefaTransporte = TarefaTransporteForm(request.GET or None)
        formSetTarefaGrupos = TarefaGruposFormset(request.GET or None)
    elif request.method == 'POST':
        formTarefa = TarefaForm(request.POST)
        formTarefaAtividade = TarefaAtividadeForm(request.POST, uoId = UnidadeOrganica.objects.get(id=1))
        formTarefaTransporte = TarefaTransporteForm(request.POST)
        formSetTarefaGrupos = TarefaGruposFormset(request.POST)


        if formTarefa.is_valid() and formTarefaTransporte.is_valid() and formSetTarefaGrupos.is_valid():
            t = formTarefa.save(commit=False)
            t.estado = False
            #Change for logged in user
            t.utilizadorid = Utilizador.objects.get(id=1) 
            t.sessao_atividadeid_destino = SessaoAtividade.objects.get(id = formTarefaTransporte.cleaned_data['sessaoAtividade_destino'])
            t.sessao_atividadeid_origem = SessaoAtividade.objects.get(id = formTarefaTransporte.cleaned_data['sessaoAtividade_origem'])
            t.origem = formTarefaTransporte.cleaned_data['origem']
            t.destino = formTarefaTransporte.cleaned_data['destino']
            t.horario = formTarefaTransporte.cleaned_data['horario']
            t.data = formTarefaTransporte.cleaned_data['dia']

            t.save()

            for form in formSetTarefaGrupos:
                InscTarefa = InscricaoTarefa(inscricaoid = Inscricao.objects.get(id=form.cleaned_data['inscricao']), tarefaid = t)
                InscTarefa.save()

        elif formTarefa.is_valid() and formTarefaAtividade.is_valid():
            t = formTarefa.save(commit=False)
            t.estado = False
            #Change for logged in user
            t.utilizadorid = Utilizador.objects.get(id=1)
            t.sessao_atividadeid = SessaoAtividade.objects.get(id=formTarefaAtividade.cleaned_data['sessaoAtividade'])
            t.horario = t.sessao_atividadeid.sessaoid.hora_de_inicio
            t.data = t.sessao_atividadeid.data
            t.save()
            
        return redirect('tarefas:showTarefas')
    
    context = { 'formTarefa': formTarefa,
                'formTarefaAtividade': formTarefaAtividade,
                'formTarefaTransporte': formTarefaTransporte,
                'formSetTarefaGrupos': formSetTarefaGrupos,
                }

    return render(request, 'tarefas/AdicionarTarefa.html', context)

#Used in Create Tarefa to dynamically get the Sessoes Atividade of a the selected Atividade
#Returns a Json Response with the data of all the SessaoAtividades that have the atividadeid equal to atividadeid
def getSessoes(request, atividadeid):
    sessoes = [(sessaoAtividade.id, str(sessaoAtividade)) for sessaoAtividade in SessaoAtividade.objects.filter(atividadeid = atividadeid)]
    return JsonResponse(dict(sessoes))

#Used in Create Tarefa to dynamically get the Sessoes Atividade from the selected date
#Returns a Json Response with the SessaoAtividades that have date equal to the arg date
def getSessoesBydate(request, date):
    sessoes = []
    for sessao in SessaoAtividade.objects.filter(data=date):
        #change later to authenticated user
        if sessao.atividadeid.unidadeorganicaid == Utilizador.objects.get(id=1).unidade_organicaid:
            sessoes.append((sessao.id, str(sessao.atividadeid.nome) + ", " + str(sessao.sessaoid.hora_de_inicio)))

    return JsonResponse(dict(sessoes))

#Used in Create Tarefa to dynamically get the Sessoes Atividade from the selected date and that are after the sessao_atual
#Returns a Json Response with the SessaoAtividades that have date equal to the arg date and hora_inicio greather than the hora_fim of the sessao_atual  
def getSessoesNext(request, sessao_atividadeid, date):
    sessoes = []
    sessao_atual = SessaoAtividade.objects.get(id=sessao_atividadeid)

    hora_inicio = datetime.datetime.combine(sessao_atual.data ,sessao_atual.sessaoid.hora_de_inicio)
    duracao = sessao_atual.atividadeid.duracao

    hora_fim = hora_inicio + datetime.timedelta(minutes=duracao)

    for sessao in SessaoAtividade.objects.filter(data=date):
        #change later to authenticated user
        if sessao.atividadeid.unidadeorganicaid == Utilizador.objects.get(id=1).unidade_organicaid:
            #gets all the sessoes within a 30 minute gap since the hora_fim of the sessao_atual
            if sessao.sessaoid.hora_de_inicio >= hora_fim.time() and sessao.sessaoid.hora_de_inicio <= (hora_fim + datetime.timedelta(minutes=30)).time():
                sessoes.append((sessao.id,  str(sessao.atividadeid.nome) + ", " + str(sessao.sessaoid.hora_de_inicio)))

    return JsonResponse(dict(sessoes))

def getHoraFim(request, sessao_atividadeid):
    sessao_atual = SessaoAtividade.objects.get(id=sessao_atividadeid)

    hora_inicio = datetime.datetime.combine(sessao_atual.data ,sessao_atual.sessaoid.hora_de_inicio)
    duracao = sessao_atual.atividadeid.duracao
    hora_fim = hora_inicio + datetime.timedelta(minutes=duracao)

    return JsonResponse({'1': hora_fim.time()})


def getLocal_Sessao(request, sessao_atividadeid):
    sessaoAtividade = SessaoAtividade.objects.get(id = sessao_atividadeid)
    local = sessaoAtividade.atividadeid.localid.descricao
    return JsonResponse({'local': local})

def getGrupos(request, sessao_atividade_origem, sessao_atividade_destino, dia):
    sessao_origem = SessaoAtividade.objects.get(id=sessao_atividade_origem)
    sessao_destino = SessaoAtividade.objects.get(id=sessao_atividade_destino)

    count = 0
    grupos = []

    for grupo in Inscricao.objects.filter(dia = dia):
        for sessaoInsc in SessaoAtividadeInscricao.objects.filter(inscricaoid = grupo):
            if sessaoInsc.sessao_atividadeid.id == sessao_origem.id: 
                count += 1
            elif sessaoInsc.sessao_atividadeid.id == sessao_destino.id:
                count +=1
        if count == 2:
            grupos.append((grupo.id, str(grupo)))

    return JsonResponse(dict(grupos))

def showTarefas(request):
    allTarefas = Tarefa.objects.all()

    paginator = Paginator(allTarefas, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj,}
    return render(request, 'tarefas/showTarefas.html', context)

def atribuirTarefa(request, id):
    tarefa = Tarefa.objects.get(id=id)
    uo_id = tarefa.utilizadorid.unidade_organicaid
    resultColaboradores = []
    
    #change later depending on other group user_type numeration
    colaboradores = Utilizador.objects.filter(unidade_organicaid = uo_id).filter(user_type = 3)

    for colab in colaboradores:
        busy = False
        for colabTarefa in ColaboradorTarefa.objects.filter(utilizadorid = colab):
            if(colabTarefa.tarefaid.horario == tarefa.horario and colabTarefa.tarefaid.data == tarefa.data):
                busy = True
                break
        if not busy:
            resultColaboradores.append(colab)

    tarefaGrupos = None
    if tarefa.tipoTarefa == 'Transporte':
        tarefaGrupos = InscricaoTarefa.objects.filter(tarefaid = tarefa.id)

    if request.method == 'POST':
        form = ColaboradorTarefaForm(request.POST)
        if form.is_valid():
            colabT = form.save(commit=False)
            colabT.tarefaid = tarefa
            colabT.save()

            tarefa.estado = True
            tarefa.save()
            return redirect('tarefas:showTarefas')

    context = {
        'colaboradores': resultColaboradores,
        'dadosTarefa': tarefa,
        'dadosTarefaGrupos': tarefaGrupos,
    }
    return render(request, 'tarefas/AtribuirTarefa.html', context)

def updateTarefa(request, id):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass

def deleteTarefa(request, id):
    tarefa = Tarefa.objects.get(id = id)
    tarefa.delete()
    return redirect('tarefas:showTarefas')

def editTarefa(request, id):
    dados_Tarefa= Tarefa.objects.get(id = id)
    tarefa_Transporte_Form = None
    tarefa_Atividade_Form = None

    if request.method == "GET" :
        if dados_Tarefa.tipoTarefa == 'Transporte':
            tarefa_Transporte_Form = TarefaTransporteForm()
        elif dados_Tarefa.tipoTarefa == 'Atividade':
            tarefa_Atividade_Form = TarefaAtividadeForm(
               initial={'atividade':dados_Tarefa.sessao_atividadeid.atividadeid.id,'sessaoAtividade':dados_Tarefa.sessao_atividadeid.id}, 
               uoId = UnidadeOrganica.objects.get(id=1), 
               sA = dados_Tarefa.sessao_atividadeid.atividadeid.id
            )

        tarefaForm = TarefaForm(instance=dados_Tarefa)
    
    if request.method == "POST":
        tarefaForm = TarefaForm(request.POST, instance=dados_Tarefa)
        if dados_Tarefa.tipoTarefa == 'Transporte':
            pass
        elif dados_Tarefa.tipoTarefa == 'Atividade':
            tarefa_Atividade_Form = TarefaAtividadeForm(request.POST, uoId = UnidadeOrganica.objects.get(id=1))
            if tarefaForm.is_valid() and tarefa_Atividade_Form.is_valid():
                t = tarefaForm.save(commit=False)
                t.tipoTarefa = 'Atividade'
                t.estado = 'False'
                t.sessao_atividadeid = SessaoAtividade.objects.get(id=tarefa_Atividade_Form.cleaned_data['sessaoAtividade'])
                t.horario = t.sessao_atividadeid.sessaoid.hora_de_inicio
                t.data = t.sessao_atividadeid.data
                t.save()

                for colab in ColaboradorTarefa.objects.filter(tarefaid=t.id):
                    colab.delete()

                return redirect('tarefas:showTarefas')

        
    
    context={'formTarefa': tarefaForm, 
             'formTarefaAtividade': tarefa_Atividade_Form,
             'formTarefaTransporte': tarefa_Transporte_Form, 
             'tarefa': dados_Tarefa}   
    return render(request,'tarefas/EditTarefa.html', context)
