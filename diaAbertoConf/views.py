from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from diaAbertoConf.models import Transporte, TransporteUniversitarioHorario, HorarioTransporte, Ementa, Prato

from diaAbertoConf.forms import TransporteForm, TransporteUniversitarioHorarioForm, HorarioTransporteForm, EmentaForm, PratoForm
# Create your views here.

def index(request):
    #template = loader.get_template('diaAbertoConf/DiaAbertoConfMain.html')
    #return HttpResponse(template.render({}, request))
    return render(request, 'diaAbertoConf/DiaAbertoConfMain.html')

def gestaoTransportes(request):
    #template = loader.get_template('diaAbertoConf/GestaoTransportes.html')
    #return HttpResponse(template.render({}, request)) 
    return render(request, 'diaAbertoConf/GestaoTransportes.html')
 

#Transporte CRUD- Create Read Update Delete
#Creates new transporte
def createTransporte(request):
    if request.method == "POST":
        form = TransporteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('diaAbertoConf:gestaoTransportes'))
        else:
            form = TransporteForm()
        return render(request, 'diaAbertoConf/AdicionarTransporte.html')

def showCreateTransporte(request):
    return render(request, 'diaAbertoConf/AdicionarTransporte.html')

#show all transportes
def showTransportes(request):
    allTransportes = Transporte.objects.all()
    context = {'allTransportes' : allTransportes,}
    #template = loader.get_template('diaAbertoConf/ShowTransportes.html')
    return render(request, 'diaAbertoConf/ShowTransportes.html', context)

#gets a transporte with a specific id 
def getTransporte(request, id):
    dados_Transporte = Transporte.objects.get(id = id)
    #add later
    return 0

#updates the fields of a spcific transporte
def updateTransporte(request, id):
    dados_Transporte = Transporte.objects.get(id = id)
    form = TransporteForm(request.POST, instance = dados_Transporte)
    if form.is_valid():
        form.save()
        return  HttpResponseRedirect(reverse('diaAbertoConf:allTransportes'))
    return render(request, 'diaAbertoConf/EditarTransporte.html')

def showUpdateTransporte(request, id):
    dados_Transporte = Transporte.objects.get(id = id)
    context = {'transporte' : dados_Transporte,}
    return render(request, 'diaAbertoConf/EditarTransporte.html', context)


#deletes a transporte
def deleteTransporte(request, id):
    dados_transporte = Transporte.objects.get(id = id)
    dados_transporte.delete()
    return HttpResponseRedirect(reverse('diaAbertoConf:allTransportes'))

#TransporteUniversitario_Horario CRUD- Create Read Update Delete
#Creates new TransporteUniversitario_Horario, associates Horario to transporte 
# and defines its Origen and Destino
def createTransporteUniversitario_Horario(request):
    if request.method == "POST":
        form = TransporteUniversitarioHorarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('diaAbertoConf:gestaoTransportes'))
        else:
            form = TransporteForm()
        #add later
        return HttpResponseRedirect(reverse('diaAbertoConf:showCreateRotaTransporte'))

def showCreateTransporteUniversitario_Horario(request):
    dadosTransportes = Transporte.objects.all()
    dadosHorarios = HorarioTransporte.objects.all()
    context = { 'allTransportes': dadosTransportes,
                'allHorarios': dadosHorarios,}
    return render(request, 'diaAbertoConf/AdicionarTransporteUniversitario_Horario.html', context)

#show all transporteUniversidade_Horarios
def showTransporteUniversitario_Horarios(request):
    allTransportesUni_Horario = TransporteUniversitarioHorario.objects.all()
    for transporteUni_Horario in allTransportesUni_Horario:
        transporteUni_Horario.transporte = 'aaa'
        transporteUni_Horario.horario = 'aaa'

    context = {'allRotas': allTransportesUni_Horario,}
    return render(request, 'diaAbertoConf/showTransporteUniversitario_Horario.html', context)

#gets a transporteUniversidade_Horario with a specific id 
def getTransporteUniversidade_Horario(request, id):
    dados_TransporteUni_Horario = TransporteUniversitarioHorario.objects.get(id = id)
    #add later
    return 0

#upadates the fields of a spcific transporteUniversidade_Horario
def updateTransporteUniversitario_Horario(request, id):
    dados_TransporteUni_Horario = TransporteUniversitarioHorario.objects.get(id = id)
    form = TransporteUniversitarioHorarioForm(request.POST, instance = dados_TransporteUni_Horario)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('diaAbertoConf:allRotasTransporte'))
    return HttpResponseRedirect(reverse('diaAbertoConf:showUpdateTransporteUniversitario_Horario', args=(),
        kwargs={'id': dados_TransporteUni_Horario.id}))

def showUpdateTransporteUniversitario_Horario(request, id):
    dados_TransporteUni_Horario = TransporteUniversitarioHorario.objects.get(id = id)
    dadosTransportes = Transporte.objects.all()
    dadosHorarios = HorarioTransporte.objects.all()
    context = {'rota' : dados_TransporteUni_Horario,
                'allTransportes': dadosTransportes,
                'allHorarios': dadosHorarios,}
    return render(request, 'diaAbertoConf/EditarTransporteUniversitario_Horario.html', context)

#deletes a transporteUniversidade_Horario
def deleteTransporteUniversitario_Horario(request, id):
    dados_TransporteUni_Horario = TransporteUniversitarioHorario.objects.get(id = id)
    dados_TransporteUni_Horario.delete()
    return HttpResponseRedirect(reverse('diaAbertoConf:allRotasTransporte'))

#Horario Transporte CRUD- Create Read Update Delete
#Creates new Horario Transporte
def createHorario_Transporte(request):
    if request.method == "POST":
        form = HorarioTransporteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('diaAbertoConf:gestaoTransportes'))
        else:
            form = HorarioTransporteForm()
        return render(request, 'diaAbertoConf/AdicionarHorarioTransporte.html')

def showCreateHorario_Transporte(request):
    return render(request, 'diaAbertoConf/AdicionarHorarioTransporte.html')

#show all Hprarios Transporte
def showHorarios_Transporte(request):
    allHorarios_Transporte = HorarioTransporte.objects.all()
    context = {'allHorarios_Transporte': allHorarios_Transporte,}
    return render(request, 'diaAbertoConf/ShowHorarioTransportes.html', context)

#gets a Horario_Transporte with a specific id 
def getHorario_Transporte(request, id):
    dados_Horario_Transporte = HorarioTransporte.objects.get(id = id)
    #add later
    return 0

#updates the fields of a spcific Horario_Transporte
def updateHorario_Transporte(request, id):
    dados_Horario_Transporte = HorarioTransporte.objects.get(id = id)
    form = HorarioTransporteForm(request.POST, instance = dados_Horario_Transporte)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('diaAbertoConf:allHorarios'))
    return HttpResponseRedirect(reverse('diaAbertoConf:showUpdateHorarioTransporte', args=(),
        kwargs={'id': dados_Horario_Transporte.id}))

def showUpdateHorario_Transporte(request, id):
    dados_Horario_Transporte = HorarioTransporte.objects.get(id = id)
    context = {'horario' : dados_Horario_Transporte,}
    return render(request, 'diaAbertoConf/EditarHorarioTransporte.html', context)

#deletes a Horario_Transporte
def deleteHorario_Transporte(request, id):
    dados_Horario_Transporte = HorarioTransporte.objects.get(id = id)
    dados_Horario_Transporte.delete()
    return HttpResponseRedirect(reverse('diaAbertoConf:allHorarios'))


def gestaoEmentas(request):
    allEmentas = Ementa.objects.all()
    context = {'allEmentas' : allEmentas,}
    return render(request, 'diaAbertoConf/GestaoEmentas.html', context)

def deleteEmenta(request, id):
    dados_Ementa = Ementa.objects.get(id = id)
    dados_Ementa.delete()
    return HttpResponseRedirect(reverse('diaAbertoConf:gestaoEmentas'))

def newEmenta(request):
    if request.method == "POST":
        form = EmentaForm(request.POST)
        if form.is_valid():
            ementaData=form.save()
            #add later
            return HttpResponseRedirect(reverse('diaAbertoConf:showNewPratos',args=(),kwargs={'id': ementaData.id}))
        else:
            form = EmentaForm()
        #add later
        return render(request, 'diaAbertoConf/AdicionarEmenta.html')

def showNewEmenta(request):
     return render(request, 'diaAbertoConf/AdicionarEmenta.html')

def showNewPratos(request, id):
    dados_Ementa = Ementa.objects.get(id = id)
    context={ 'ementaData': dados_Ementa,}
    return render(request, 'diaAbertoConf/newPratos.html',context)

def newPrato(request,id):
    dados_Ementa = Ementa.objects.get(id = id)
    context={ 'ementaData': dados_Ementa,}
    if request.method == "POST":
        form = PratoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('diaAbertoConf:showNewPratos',args=(),kwargs={'id': id}))
        else:
            form = PratoForm()
        return render(request,'diaAbertoConf/newPratos.html',context)   