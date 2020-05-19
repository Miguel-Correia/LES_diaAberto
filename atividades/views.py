from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.forms import modelformset_factory 

from atividades.models import Edificio, Campus, Departamento, Local, Atividade, UnidadeOrganica, Tematica, Utilizador, AtividadeTematica, AtividadeMaterial, Sessao, SessaoAtividade, Material

from atividades.forms import EdificioForm, CampusForm, DepartamentoForm, LocalForm, AtividadeForm, UnidadeOrganicaForm, TematicaForm, AtividadeTematicaFormset, AtividadeMaterialFormset, AtividadeTematicaForm, AtividadeMaterialForm, AtividadeSessaoForm, AtividadeSessaoFormset, SessaoForm

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
            return redirect('atividades:showCreateEdificio', saved=1)
        else:
            form = EdificioForm()
            return render(request, 'atividades/AdicionarEdificio.html')

def showCreateEdificio(request, saved=0):
    allCampus = Campus.objects.all()
    context = {'allCampus' : allCampus, 'saved' : saved}
    return render(request, 'atividades/AdicionarEdificio.html', context)

#show all edificios
def showEdificios(request):
    allEdificios = Edificio.objects.all()
    allCampus = Campus.objects.all()
    paginator = Paginator(allEdificios, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'allCampus' : allCampus, 'allEdificios' : allEdificios, 'page_obj': page_obj,}
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
            return redirect('atividades:showCreateCampus', saved=1)
        else:
            form = CampusForm()
            return render(request, 'atividades/AdicionarCampus.html')

def showCreateCampus(request, saved=0):
    context = {'saved' : saved}
    return render(request, 'atividades/AdicionarCampus.html', context)

#show all campus
def showCampus(request):#, ordena):
    allCampus = Campus.objects.all()
    #if ordena == campus:
    	#dados_campus = Campus.objets.order_by('nome')
    paginator = Paginator(allCampus, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #campus_name = request.GET.get('campus_name')
    #if campus_name != '' and campus_name is not None:
        #allCampus = allCampus.filter(campus__iname=campus_name)
    context = {'allCampus' : allCampus, 'page_obj': page_obj,}
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
    paginator = Paginator(allUnidadeOrganicas, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'allUnidadeOrganicas' : allUnidadeOrganicas, 'page_obj': page_obj,}
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
            return redirect('atividades:showCreateDepartamento', saved=1)
        else:
            form = DepartamentoForm()
            return render(request, 'atividades/AdicionarDepartamento.html')

def showCreateDepartamento(request, saved=0):
    allUnidadeOrganicas = UnidadeOrganica.objects.all()
    context = {'allUnidadeOrganicas' : allUnidadeOrganicas, 'saved' : saved}
    return render(request, 'atividades/AdicionarDepartamento.html', context)

#show all departamntos
def showDepartamentos(request):
    allDepartamentos = Departamento.objects.all()
    paginator = Paginator(allDepartamentos, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'allDepartamentos' : allDepartamentos, 'page_obj': page_obj,}
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
            if form.cleaned_data['indoor'] == False:
                 l = Local(campusid=form.cleaned_data['campusid'],  
                     descricao=form.cleaned_data['descricao'],
                     indoor = form.cleaned_data['indoor'])
                 l.save()
            else:
                l = Local(campusid=form.cleaned_data['campusid'],  
                    descricao=form.cleaned_data['descricao'],
                    indoor = form.cleaned_data['indoor'],
                    edicifioid = Edificio.objects.get(id=request.POST['edicifioid']),
                    andar = form.cleaned_data['andar'],
                    sala = form.cleaned_data['sala'])
                l.save()
            #form.save()
            return redirect('atividades:showCreateLocal', saved=1)
        else:
            form = LocalForm()
            return render(request, 'atividades/AdicionarLocal.html')

def showCreateLocal(request, saved=0):
    allEdificios = Edificio.objects.all()
    allCampus = Campus.objects.all()
    context = {'allCampus' : allCampus, 'allEdificios' : allEdificios, 'saved' : saved}
    return render(request, 'atividades/AdicionarLocal.html', context)

#show all local
def showLocais(request):
    allLocais = Local.objects.all()
    allCampus = Campus.objects.all()
    paginator = Paginator(allLocais, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'allCampus': allCampus, 'allLocais' : allLocais, 'page_obj': page_obj,}
    return render(request, 'atividades/ShowLocais.html', context)

#gets a local with a specific id 
def getLocal(request, id):
    dados_Local = Local.objects.get(id = id)
    #add later
    return 0

#upadates the fields of a spcific local
def updateLocal(request, id):
    dados_Local = Local.objects.get(id = id)
    form = LocalForm(request.POST)
    if form.is_valid():
        if form.cleaned_data['indoor'] == True:
            dados_Local.campusid = form.cleaned_data['campusid']
            dados_Local.indoor = form.cleaned_data['indoor']
            dados_Local.descricao = form.cleaned_data['descricao']
            dados_Local.andar = form.cleaned_data['andar']
            dados_Local.sala = form.cleaned_data['sala']
            dados_Local.edicifioid = Edificio.objects.get(id=request.POST['edicifioid'])
        #form.save()
        else:
            dados_Local.campusid = form.cleaned_data['campusid']
            dados_Local.indoor = form.cleaned_data['indoor']
            dados_Local.descricao = form.cleaned_data['descricao']
            dados_Local.andar = None
            dados_Local.sala = None
            dados_Local.edicifioid = None
        dados_Local.save()
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
        FormsetT = AtividadeTematicaFormset(request.POST, prefix='formTematica')
        FormsetM = AtividadeMaterialFormset(request.POST, prefix='formMaterial')
        # FormsetS = AtividadeSessaoFormSet(request.POST)
        if form.is_valid() and FormsetM.is_valid() and FormsetT.is_valid():
            utilizador = Utilizador.objects.get(id = 1)
            atividade = form.save(commit=False)
            atividade.utilizadorid = utilizador
            atividade.unidadeorganicaid = utilizador.unidade_organicaid
            atividade.validada = -1
            atividade.editavel = True
            atividade.save()
            for form in FormsetM:
                material = form.save(commit=False)
                material.atividadeid = atividade
                material.save()
            for form in FormsetT:
                tematica = form.save(commit=False)
                tematica.atividadeid = atividade
                tematica.save()
            # for form in FormsetS:    
            #     for sessao in form.cleaned_data['sessaoid']:
            #         result = AtividadeSessao(
            #             sessaoid= AtividadeSessap.objects.get(id=sessao),
            #             data = form.cleaned_data['data'],
            #         )
            #         result.save()
            return redirect('atividades:showCreateAtividade', saved=1)
        else:
            form = AtividadeForm()
            return render(request, 'atividades/AdicionarAtividade.html', {'FormsetS' : FormsetS})

def showCreateAtividade(request, saved=0):
    context = {'form' : AtividadeForm(), 'saved' : saved, 
    'AtividadeTematicaFormset' : AtividadeTematicaFormset(queryset=AtividadeTematica.objects.none(), prefix='formTematica'), 
    'AtividadeMaterialFormset' : AtividadeMaterialFormset(queryset=AtividadeMaterial.objects.none(), prefix='formMaterial'),
    # 'AtividadeSessaoFormset' : AtividadeSessaoFormset(queryset=SessaoAtividade.objects.none(), prefix='formSessao')
    }
    return render(request, 'atividades/AdicionarAtividade.html', context)

#show all atividade
def showAtividades(request):
    # allAtividade = Atividade.objects.all()
    # if tipo == departamento:
    # 	dados_atividade = Atividades.objects.filter(departamento = filtro)
    # elif tipo == campus:
    # 	dados_atividade = Atividades.objects.filter(campus = filtro)
    # elif tipo == nome:
    # 	dados_atividade = Atividades.objects.filter(nome = filtro)
    # elif tipo == tipo_atividade:
    # 	dados_atividade = Atividades.objects.filter(tipo_atividade = filtro)
    # elif tipo == validada:
    # 	dados_atividade = Atividades.objects.filter(validada = filtro)
    # elif tipo == unidadeorganica:
    # 	dados_atividade = Atividades.objects.filter(unidadeorgaica = filtro)
    # if ordena == departamento:
    # 	dados_atividade_2 = Atividades.objets.order_by('departamento')
    # elif ordena == campus:
    # 	dados_atividade_2 = Atividades.objets.order_by('campus')
    # elif ordena == nome:
    # 	dados_atividade_2 = Atividades.objets.order_by('nome')
    # elif ordena == duracao:
    # 	dados_atividade_2 = Atividades.objets.order_by('duracao')
    # elif ordena == limite_de_particiantes:
    # 	dados_atividade_2 = Atividades.objets.order_by('limite_de_particiantes')
    allAtividades = Atividade.objects.all()
    paginator = Paginator(allAtividades, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    allTematicaAtividade = AtividadeTematica.objects.all()
    allMaterialAtividade = AtividadeMaterial.objects.all()
    # listTematica = []        
    # for tematica in AtividadeTematica.objects.filter(atividadeid = id):
    #         listTematica.append(tematica.tematicaid.nome)
    # listMaterial = []        
    # for material in AtividadeMaterial.objects.filter(atividadeid = id):
    #         listMaterial.append((material.materialid.nome, material.quantidade))
    context = {'allAtividades' : allAtividades, 'page_obj': page_obj,
    'listTematica' : allTematicaAtividade, 'listMaterial' : allMaterialAtividade}
    return render(request, 'atividades/ShowAtividades.html', context)

def showDetailsAtividade(request, id):
    allDetailsAtividade = Atividade.objects.get(id = id)
    allUnidadeOrganicas = UnidadeOrganica.objects.all()
    allLocais = Local.objects.all()
    listTematica = []        
    for tematica in AtividadeTematica.objects.filter(atividadeid = id):
            listTematica.append(tematica.tematicaid.nome)
    listMaterial = []        
    for material in AtividadeMaterial.objects.filter(atividadeid = id):
            listMaterial.append((material.materialid.nome, material.quantidade))
    context = {'allLocais' : allLocais, 'allUnidadeOrganicas' : allUnidadeOrganicas, 'atividade' : allDetailsAtividade,
    'listTematica' : listTematica, 'listMaterial' : listMaterial}
    return render(request, 'atividades/ShowDetailsAtividade.html', context)

#gets a atividade with a specific id 
def getAtividade(request, id):
    dados_Atividade = Atividade.objects.get(id = id)
    #add later
    return 0

#upadates the fields of a spcific atividade
def updateAtividade(request, id):
    dados_Atividade = Atividade.objects.get(id = id)
    allUnidadeOrganicas = UnidadeOrganica.objects.all()
    allLocais = Local.objects.all()
    #AtividadeTematicaFormset = modelformset_factory(AtividadeTematica, AtividadeTematicaForm, extra=0)

    form = AtividadeForm(request.POST, instance = dados_Atividade)
    #FormsetT = AtividadeTematicaFormset(request.POST)
    # FormsetM = AtividadeMaterialFormset(request.POST, prefix='formMaterial')
    if form.is_valid():
        dados_Atividade.validada = -1
        form.save()
        #FormsetT.save()
        return  HttpResponseRedirect(reverse('atividades:allAtividades'))
    context = {'allLocais' : allLocais, 'allUnidadeOrganicas' : allUnidadeOrganicas, 'atividade' : dados_Atividade, 
    'AtividadeTematicaFormset' : AtividadeTematicaFormset(queryset=AtividadeTematica.objects.filter(atividadeid = id)),
    'AtividadeMaterialFormset' : AtividadeMaterialFormset(queryset=AtividadeMaterial.objects.filter(atividadeid = id))}
    return render(request, 'atividades/EditarAtividade.html', context)

def showUpdateAtividade(request, id):
    AtividadeTematicaFormset = modelformset_factory(AtividadeTematica, AtividadeTematicaForm, extra=0)
    AtividadeMaterialFormset = modelformset_factory(AtividadeMaterial, AtividadeMaterialForm, extra=0)
    dados_Atividade = Atividade.objects.get(id = id)
    allUnidadeOrganicas = UnidadeOrganica.objects.all()
    allLocais = Local.objects.all()
    context = {'allLocais' : allLocais, 'allUnidadeOrganicas' : allUnidadeOrganicas, 'atividade' : dados_Atividade, 
    'AtividadeTematicaFormset' : AtividadeTematicaFormset(queryset=AtividadeTematica.objects.filter(atividadeid = id)),
    'AtividadeMaterialFormset' : AtividadeMaterialFormset(queryset=AtividadeMaterial.objects.filter(atividadeid = id))}
    return render(request, 'atividades/EditarAtividade.html', context)

#deletes a atividade
def deleteAtividade(request, id):
    dados_atividade = Atividade.objects.get(id = id)
    dados_atividade.delete()
    return HttpResponseRedirect(reverse('atividades:allAtividades'))

#request atividade
def requestAtividade(request):
	dados_atividade = atividade.objects.get(id = id)
	dados_atividade.editavel = True
	#add later
	return 0

#valid atividade
def validAtividade(request, id):
    dados_atividade = Atividade.objects.get(id = id)
    #form = AtividadeForm(request.POST, instance = dados_atividade)
    #if form.is_valid():
    #atividade = form.save(commit=False)
    dados_atividade.validada = 1 
    dados_atividade.save()
    return HttpResponseRedirect(reverse('atividades:allAtividades'))
    # dados_atividade = Atividade.objects.get(id = id)
    # dados_atividade.delete()
    # return HttpResponseRedirect(reverse('atividades:allAtividades'))

def recuseAtividade(request, id):
    dados_atividade = Atividade.objects.get(id = id)
    #form = AtividadeForm(request.POST, instance = dados_atividade)
    #if form.is_valid():
    #atividade = form.save(commit=False)
    dados_atividade.validada = 0 
    dados_atividade.save()
    return HttpResponseRedirect(reverse('atividades:allAtividades'))
    # dados_atividade = Atividade.objects.get(id = id)
    # dados_atividade.delete()
    # return HttpResponseRedirect(reverse('atividades:allAtividades'))

#-----------------------------------------------------
# Tematica CRUD- Create Read Update Delete
#----------------------------------------------------------------
#showAll
def showTematicas(request):
    allTematicas = Tematica.objects.all()
    context = {'allTematicas': allTematicas,}
    return render(request, 'atividades/ShowTematicas.html', context)

#show Create
def showCreateTematica(request):
    return render(request, 'atividades/AdicionarTematica.html')

#Add tematica
def addTematica(request):
    if request.method == "POST":
        form = TematicaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('atividades:gestaoAtividades'))
        else:
            form = AtividadeForm()
        return render(request, 'atividades/AdicionarTematica.html')

def showUpdateTematica(request, id):
    dados = Tematica.objects.get(id = id)
    context = {'tematica': dados,}
    return render(request, 'atividades/EditarTematica.html', context)

def updateTematica(request, id):
    dados = Tematica.objects.get(id = id)
    form = TematicaForm(request.POST, instance = dados)
    if form.is_valid():
        form.save()
        return  HttpResponseRedirect(reverse('atividades:allTematicas'))
    return HttpResponseRedirect(reverse('atividades:showUpdateTematica', args=(),
        kwargs={'id': dados.id}))

def deleteTematica(request, id):
    dados = Tematica.objects.get(id = id)
    dados.delete()
    return HttpResponseRedirect(reverse('atividades:allTematicas'))
   
#-----------------------------------------------------------------------------
# Sessao CRUD - Create Read Update Delete
#-------------------------------------------------------------------------

def showSessoes(request):
    allSessoes = Sessao.objects.all()
    return render(request, 'atividades/ShowHorarioSessao.html', {'allSessoes': allSessoes})

def addSessao(request):

    if request.method == "POST":
        form = SessaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atividades:allSessoes')
    
    return render(request, 'atividades/AdicionarHorarioSessao.html')

def updateSessao(request, id):
    dados = Sessao.objects.get(id=id)

    if request.method == "POST":
        form = SessaoForm(request.POST, instance=dados)
        if form.is_valid():
            form.save()
            return redirect('atividades:allSessoes')

    return render(request,'atividades/EditarHorarioSessao.html' , {'sessao':dados})

def deleteSessao(reques, id):
    dados = Sessao.objects.get(id=id)
    dados.delete()
    return redirect('atividades:allSessoes')

    