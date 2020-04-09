from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from atividades.models import Edificio, Campus, Departamento, Local, Atividade, UnidadeOrganica

from atividades.forms import EdificioForm, CampusForm, DepartamentoForm, LocalForm, AtividadeForm, UnidadeOrganicaForm
# Create your views here.

def index(request):
    #template = loader.get_template('atividades/AtividadesMain.html')
    #return HttpResponse(template.render({}, request))
    return render(request, 'atividades/AtividadesMain.html')

def gestaoAtividades(request):
    return render(request, 'atividades/GestaoAtividades.html')

def showatividades(request):
    return render(request, 'atividades/ShowAtividades.html')

def adicionaratividade(request):
    return render(request, 'atividades/AdicionarAtividade.html')

#Creates new edificio
def createEdificio(request):
    if request.method == "POST":
        form = EdificioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('atividades:gestaoAtividades'))
        else:
            form = EdificioForm()
        return render(request, 'atividades/AdicionarEdificio.html')

def showCreateEdificio(request):
    allCampus = Campus.objects.all()
    context = {'allCampus' : allCampus}
    return render(request, 'atividades/AdicionarEdificio.html', context)

#show all edificios
def showEdificios(request):
    allEdificios = Edificio.objects.all()
    allCampus = Campus.objects.all()
    context = {'allCampus' : allCampus, 'allEdificios' : allEdificios,}
    return render(request, 'atividades/ShowEdificios.html', context)

#gets a edificios with a specific id 
def getEdificio(request, id):
    dados_Edificio = Edicifio.objects.get(id = id)
    #add later
    return 0

#upadates the fields of a spcific edificio
def updateEdificio(request, id):
    dados_Edificio = Edificio.objects.get(id = id)
    form = EdificioForm(request.POST, instance = dados_Edificio)
    if form.is_valid():
        form.save()
        return  HttpResponseRedirect(reverse('atividades:allEdificios'))
    return render(request, 'atividades/EditarEdificio.html')

def showUpdateEdificio(request, id):
    dados_Edificio = Edificio.objects.get(id = id)
    allCampus = Campus.objects.all()
    context = {'allCampus' : allCampus, 'edificio' : dados_Edificio}
    return render(request, 'atividades/EditarEdificio.html', context)

#deletes a edificio
def deleteEdificio(request, id):
    dados_edificio = Edificio.objects.get(id = id)
    dados_edificio.delete()
    return HttpResponseRedirect(reverse('atividades:allEdificios'))

#Creates new campus
def createCampus(request):
    if request.method == "POST":
        form = CampusForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('atividades:gestaoAtividades'))
        else:
            form = CampusForm()
        return render(request, 'atividades/AdicionarCampus.html')

def showCreateCampus(request):
    return render(request, 'atividades/AdicionarCampus.html')

#show all campus
def showCampus(request):#, ordena):
    allCampus = Campus.objects.all()
    #if ordena == campus:
    	#dados_campus = Campus.objets.order_by('nome')
    context = {'allCampus' : allCampus,}
    return render(request, 'atividades/ShowCampus.html', context)

#gets a campus with a specific id 
def getCampus(request, id):
    dados_Campus = Campus.objects.get(id = id)
    #add later
    return 0

#upadates the fields of a spcific campus
def updateCampus(request, id):
    dados_Campus = Campus.objects.get(id = id)
    form = CampusForm(request.POST, instance = dados_Campus)
    if form.is_valid():
        form.save()
        return  HttpResponseRedirect(reverse('atividades:allCampus'))
    return render(request, 'atividades/EditarCampus.html')

def showUpdateCampus(request, id):
    dados_Campus = Campus.objects.get(id = id)
    context = {'campus' : dados_Campus}
    return render(request, 'atividades/EditarCampus.html', context)

#deletes a campus
def deleteCampus(request, id):
    dados_campus = Campus.objects.get(id = id)
    dados_campus.delete()
    return HttpResponseRedirect(reverse('atividades:allCampus'))

#Creates new unidade
def createUnidadeOrganica(request):
    if request.method == "POST":
        form = UnidadeOrganicaForm(request.POST)
        if form.is_valid():
            form.save()
            #if 'add_next' in request.POST: 
            return redirect('atividades:showCreateUnidadeOrganica', saved=1)
            #else:
                #return HttpResponseRedirect(reverse('atividades:gestaoAtividades'))
        else:
            form = UnidadeOrganicaForm()
            return render(request, 'atividades/AdicionarUO.html')

def showCreateUnidadeOrganica(request, saved=0):
    #allCampus = Campus.objects.all()
    #context = {'allCampus' : allCampus,}
    context = {'form' : UnidadeOrganicaForm(), 'saved' : saved}
    return render(request, 'atividades/AdicionarUO.html', context)

#show all unidade
def showUnidadeOrganicas(request):
    allUnidadeOrganicas = UnidadeOrganica.objects.all()
    context = {'allUnidadeOrganicas' : allUnidadeOrganicas,}
    return render(request, 'atividades/ShowUO.html', context)

#gets a unidade with a specific id 
def getUnidadeOrganica(request, id):
    dados_UnidadeOrganica = UnidadeOrganica.objects.get(id = id)
    #add later
    return 0

#upadates the fields of a spcific unidade
def updateUnidadeOrganica(request, id):
    dados_UnidadeOrganica = UnidadeOrganica.objects.get(id = id)
    form = UnidadeOrganicaForm(request.POST, instance = dados_UnidadeOrganica)
    if form.is_valid():
        form.save()
        return  HttpResponseRedirect(reverse('atividades:allUnidadeOrganicas'))
    return render(request, 'atividades/EditarUO.html')

def showUpdateUnidadeOrganica(request, id):
    dados_UnidadeOrganica = UnidadeOrganica.objects.get(id = id)
    allCampus = Campus.objects.all()
    context = {'allCampus' : allCampus, 'unidadeorganica' : dados_UnidadeOrganica}
    return render(request, 'atividades/EditarUO.html', context)

#deletes a unidade
def deleteUnidadeOrganica(request, id):
    dados_unidadeorganica = UnidadeOrganica.objects.get(id = id)
    dados_unidadeorganica.delete()
    return HttpResponseRedirect(reverse('atividades:allUnidadeOrganicas'))

#Creates new departamento
def createDepartamento(request):
    if request.method == "POST":
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('atividades:gestaoAtividades'))
        else:
            form = DepartamentoForm()
        return render(request, 'atividades/AdicionarDepartamento.html')

def showCreateDepartamento(request):
    allUnidadeOrganicas = UnidadeOrganica.objects.all()
    context = {'allUnidadeOrganicas' : allUnidadeOrganicas,}
    return render(request, 'atividades/AdicionarDepartamento.html', context)

#show all departamntos
def showDepartamentos(request):
    allDepartamentos = Departamento.objects.all()
    context = {'allDepartamentos' : allDepartamentos,}
    return render(request, 'atividades/ShowDepartamentos.html', context)

#gets a departamento with a specific id 
def getDepartamento(request, id):
    dados_Departamento = Departamento.objects.get(id = id)
    #add later
    return 0

#upadates the fields of a spcific departamento
def updateDepartamento(request, id):
    dados_Departamento = Departamento.objects.get(id = id)
    form = DepartamentoForm(request.POST, instance = dados_Departamento)
    if form.is_valid():
        form.save()
        return  HttpResponseRedirect(reverse('atividades:allDepartamentos'))
    return render(request, 'atividades/EditarDepartamento.html')

def showUpdateDepartamento(request, id):
    dados_Departamento = Departamento.objects.get(id = id)
    allUnidadeOrganicas = UnidadeOrganica.objects.all()
    context = {'allUnidadeOrganicas' : allUnidadeOrganicas, 'departamento' : dados_Departamento}
    return render(request, 'atividades/EditarDepartamento.html', context)

#deletes a departamento
def deleteDepartamento(request, id):
    dados_departamento = Departamento.objects.get(id = id)
    dados_departamento.delete()
    return HttpResponseRedirect(reverse('atividades:allDepartamentos'))

#Creates new local
def createLocal(request):
    if request.method == "POST":
        form = LocalForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('atividades:gestaoAtividades'))
        else:
            form = LocalForm()
        return render(request, 'atividades/AdicionarLocal.html')

def showCreateLocal(request):
    allEdificios = Edificio.objects.all()
    allCampus = Campus.objects.all()
    context = {'allCampus' : allCampus, 'allEdificios' : allEdificios,}
    return render(request, 'atividades/AdicionarLocal.html', context)

#show all local
def showLocais(request):
    allLocais = Local.objects.all()
    allCampus = Campus.objects.all()
    context = {'allCampus': allCampus, 'allLocais' : allLocais,}
    return render(request, 'atividades/ShowLocais.html', context)

#gets a local with a specific id 
def getLocal(request, id):
    dados_Local = Local.objects.get(id = id)
    #add later
    return 0

#upadates the fields of a spcific local
def updateLocal(request, id):
    dados_Local = Local.objects.get(id = id)
    form = LocalForm(request.POST, instance = dados_Local)
    if form.is_valid():
        form.save()
        return  HttpResponseRedirect(reverse('atividades:allLocais'))
    return render(request, 'atividades/EditarLocal.html')

def showUpdateLocal(request, id):
    dados_Local = Local.objects.get(id = id)
    allEdificios = Edificio.objects.all()
    allCampus = Campus.objects.all()
    context = {'allCampus' : allCampus, 'allEdificios' : allEdificios, 'local' : dados_Local,}
    return render(request, 'atividades/EditarLocal.html', context)

#deletes a local
def deleteLocal(request, id):
    dados_local = Local.objects.get(id = id)
    dados_local.delete()
    return HttpResponseRedirect(reverse('atividades:allLocais'))

#Creates new atvidade
def createAtividade(request):
    if request.method == "POST":
        form = AtividadeForm(request.POST)
        if form.is_valid():
            form.save()
            #add later
            return 0
        else:
            form = AtividadeForm()
        #add later
        return 0

#show all atividade
def showAtividade(request, filtro, tipo, ordena):
    allAtividade = Atividade.objects.all()
    if tipo == departamento:
    	dados_atividade = Atividades.objects.filter(departamento = filtro)
    elif tipo == campus:
    	dados_atividade = Atividades.objects.filter(campus = filtro)
    elif tipo == nome:
    	dados_atividade = Atividades.objects.filter(nome = filtro)
    elif tipo == tipo_atividade:
    	dados_atividade = Atividades.objects.filter(tipo_atividade = filtro)
    elif tipo == validada:
    	dados_atividade = Atividades.objects.filter(validada = filtro)
    elif tipo == unidadeorganica:
    	dados_atividade = Atividades.objects.filter(unidadeorgaica = filtro)
    if ordena == departamento:
    	dados_atividade_2 = Atividades.objets.order_by('departamento')
    elif ordena == campus:
    	dados_atividade_2 = Atividades.objets.order_by('campus')
    elif ordena == nome:
    	dados_atividade_2 = Atividades.objets.order_by('nome')
    elif ordena == duracao:
    	dados_atividade_2 = Atividades.objets.order_by('duracao')
    elif ordena == limite_de_particiantes:
    	dados_atividade_2 = Atividades.objets.order_by('limite_de_particiantes')
    #add later
    return 0

#gets a atividade with a specific id 
def getAtividade(request, id):
    dados_Atividade = Atividade.objects.get(id = id)
    #add later
    return 0

#upadates the fields of a spcific atividade
def updateAtividade(request, id):
    dados_Atividade = Atividade.objects.get(id = id)
    form = AtividadeForm(request.POST, instance = dados_Atividade)
    if form.is_valid():
        form.save()
        #add later
        return 0
    #add later
    return 0

#deletes a atividade
def deleteAtividade(request, id):
    dados_atividade = atividade.objects.get(id = id)
    dados_atividade.delete()
    #add later
    return 0

#request atividade
def requestAtividade(request):
	dados_atividade = atividade.objects.get(id = id)
	dados_atividade.editavel = True
	#add later
	return 0

#valid atividade
def validAtividade(request, id):
    dados_atividade = atividade.objects.get(id = id)
    dados_atividade.validada = True 
    #add later
    return 0
