from django.shortcuts import render, redirect
from django.http import JsonResponse
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
        form = LocalForm(request.POST, request.FILES)
        #image = ImageForm(request.POST, request.FILES)
        print(request.FILES['mapa_sala'])
        if form.is_valid():
            print("aa")
            if form.cleaned_data['indoor'] == False:
                l = Local(campusid=form.cleaned_data['campusid'],  
                    descricao=form.cleaned_data['descricao'],
                    indoor = form.cleaned_data['indoor'],
                    mapa_sala = form.cleaned_data['mapa_sala'])
                l.save()
            else:
                l = Local(campusid=form.cleaned_data['campusid'],  
                    descricao=form.cleaned_data['descricao'],
                    indoor = form.cleaned_data['indoor'],
                    edicifioid = Edificio.objects.get(id=request.POST['edicifioid']),
                    andar = form.cleaned_data['andar'],
                    sala = form.cleaned_data['sala'],
                    mapa_sala = form.cleaned_data['mapa_sala'])
                l.save()
            #form.save()
            #image.save()
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
    form = LocalForm(request.POST, request.FILES)
    if form.is_valid():
        if form.cleaned_data['indoor'] == True:
            dados_Local.campusid = form.cleaned_data['campusid']
            dados_Local.indoor = form.cleaned_data['indoor']
            dados_Local.descricao = form.cleaned_data['descricao']
            dados_Local.andar = form.cleaned_data['andar']
            dados_Local.sala = form.cleaned_data['sala']
            dados_Local.edicifioid = Edificio.objects.get(id=request.POST['edicifioid'])
            if form.cleaned_data['mapa_sala'] != None:
                dados_Local.mapa_sala = form.cleaned_data['mapa_sala']
        #form.save()
        else:
            dados_Local.campusid = form.cleaned_data['campusid']
            dados_Local.indoor = form.cleaned_data['indoor']
            dados_Local.descricao = form.cleaned_data['descricao']
            dados_Local.andar = None
            dados_Local.sala = None
            dados_Local.edicifioid = None
            if form.cleaned_data['mapa_sala'] != None:
                dados_Local.mapa_sala = form.cleaned_data['mapa_sala']
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
        FormsetS = AtividadeSessaoFormset(request.POST, prefix='formSessao')
        if form.is_valid() and FormsetM.is_valid() and FormsetT.is_valid() and FormsetS.is_valid():
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
            for form in FormsetS: 
                sessao = form.save(commit=False) 
                sessao.atividadeid = atividade
                sessao.save()
            #     for sessao in form.cleaned_data['sessaoid']:
            #         result = AtividadeSessao(
            #             sessaoid= AtividadeSessap.objects.get(id=sessao),
            #             data = form.cleaned_data['data'],
            #         )
            #         result.save()
            return redirect('atividades:showCreateAtividade', saved=1)
        else:
            form = AtividadeForm()
            return render(request, 'atividades/AdicionarAtividade.html')

def showCreateAtividade(request, saved=0):
    context = {'form' : AtividadeForm(), 'saved' : saved, 
    'AtividadeTematicaFormset' : AtividadeTematicaFormset(queryset=AtividadeTematica.objects.none(), prefix='formTematica'), 
    'AtividadeMaterialFormset' : AtividadeMaterialFormset(queryset=AtividadeMaterial.objects.none(), prefix='formMaterial'),
    'AtividadeSessaoFormset' : AtividadeSessaoFormset(queryset=SessaoAtividade.objects.none(), prefix='formSessao')
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
    allSessaoAtividade = SessaoAtividade.objects.all()
    # listTematica = []        
    # for tematica in AtividadeTematica.objects.filter(atividadeid = id):
    #         listTematica.append(tematica.tematicaid.nome)
    # listMaterial = []        
    # for material in AtividadeMaterial.objects.filter(atividadeid = id):
    #         listMaterial.append((material.materialid.nome, material.quantidade))
    context = {'allAtividades' : allAtividades, 'page_obj': page_obj,
    'listTematica' : allTematicaAtividade, 'listMaterial' : allMaterialAtividade,
    'listSessao' : allSessaoAtividade}
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
    AtividadeTematicaFormset = modelformset_factory(AtividadeTematica, AtividadeTematicaForm, extra=0)
    AtividadeMaterialFormset = modelformset_factory(AtividadeMaterial, AtividadeMaterialForm, extra=0)
    AtividadeSessaoFormset = modelformset_factory(SessaoAtividade, AtividadeSessaoForm, extra=0)

    if request.method == 'GET':
        tematicaformset = AtividadeTematicaFormset(queryset=AtividadeTematica.objects.filter(atividadeid = id), prefix='formTematica')
        materialformset = AtividadeMaterialFormset(queryset=AtividadeMaterial.objects.filter(atividadeid = id), prefix='formMaterial')
        sessaoformset = AtividadeSessaoFormset(queryset=SessaoAtividade.objects.filter(atividadeid = id), prefix='formSessao')
    elif request.method == 'POST':
        form = AtividadeForm(request.POST, instance = dados_Atividade)
        tematica = AtividadeTematica.objects.filter(atividadeid = id)
        material = AtividadeMaterial.objects.filter(atividadeid = id)
        sessao = SessaoAtividade.objects.filter(atividadeid = id)

        tematicaformset = AtividadeTematicaFormset(request.POST, prefix='formTematica', queryset= tematica)
        materialformset = AtividadeMaterialFormset(request.POST, prefix='formMaterial', queryset= material)
        sessaoformset = AtividadeSessaoFormset(request.POST, prefix='formSessao', queryset= sessao)

        if form.is_valid() and tematicaformset.is_valid() and materialformset.is_valid() and sessaoformset.is_valid():
            dados_Atividade.validada = -1
            dados_Atividade.localid = None
            form.save()
            #Save and add
            if len(tematicaformset) >= len(tematica):
                for form in tematicaformset:
                    f = form.save(commit=False)
                    f.atividadeid = dados_Atividade
                    f.save()
            #Save and delete
            else:
                formset_id_list = [f.cleaned_data['id'].id for f in tematicaformset]
                for t in tematica:
                    if t.id not in formset_id_list:
                        print(str(t.id) + " got deleted")

            materialformset.save()
            sessaoformset.save()
            return  redirect('atividades:allAtividades')

    context = { 'atividade' : dados_Atividade, 
                'AtividadeTematicaFormset' : tematicaformset,
                'AtividadeMaterialFormset' : materialformset,
                'AtividadeSessaoFormset' : sessaoformset,
            }

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

def atribuirLocal(request, id):
    dados_atividade = Atividade.objects.get(id = id)
    allCampus = Campus.objects.all()
    allTematicaAtividade = AtividadeTematica.objects.all()
    allMaterialAtividade = AtividadeMaterial.objects.all()
    allSessaoAtividade = SessaoAtividade.objects.all()
    allEdificios = Edificio.objects.filter(campusid = allCampus[0].id)
    allLocais = Local.objects.filter(edicifioid = allEdificios[0].id)
    if request.method == 'POST':
        dados_atividade.localid = Local.objects.get(id = request.POST.get("localid"))
        dados_atividade.validada = 1
        dados_atividade.save()
        return redirect('atividades:allAtividades')
    context = {'allLocais' : allLocais, 'allEdificios' : allEdificios, 'allCampus' : allCampus, 'atividade' : dados_atividade, 'listTematica' : allTematicaAtividade, 'listMaterial' : allMaterialAtividade, 'listSessao' : allSessaoAtividade}
    return render(request, 'atividades/AtribuirLocal.html', context)

def getEdificio(request, campusid):
    dados_edificio = [(e.id, e.nome_edificio)for e in Edificio.objects.filter(campusid = campusid)]
    return JsonResponse(dict(dados_edificio))

def getLocal(request, edificioid):
    dados_local = [(l.id, "Andar " + str(l.andar) + ", " + "Sala " + str(l.sala))for l in Local.objects.filter(edicifioid = edificioid)]
    return JsonResponse(dict(dados_local))
#-----------------------------------------------------
# Tematica CRUD- Create Read Update Delete
#----------------------------------------------------------------
#showAll
def showTematicas(request):
    allTematicas = Tematica.objects.all()
    context = {'allTematicas': allTematicas,}
    return render(request, 'atividades/ShowTematicas.html', context)

#Add tematica
def addTematica(request):
    form = AtividadeForm()
    if request.method == "POST":
        form = TematicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atividades:allTematicas')
    return render(request, 'atividades/AdicionarTematica.html')

def updateTematica(request, id):
    dados = Tematica.objects.get(id = id)
    if request.method == "POST":
        form = TematicaForm(request.POST, instance = dados)
        if form.is_valid():
            form.save()
            return  redirect('atividades:allTematicas')
    
    context = {'tematica': dados,}
    return render(request, 'atividades/EditarTematica.html', context)

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

def deleteSessao(request, id):
    dados = Sessao.objects.get(id=id)
    dados.delete()
    return redirect('atividades:allSessoes')


    