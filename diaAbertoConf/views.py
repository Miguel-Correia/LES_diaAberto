from django.shortcuts import render
from diaAbertoConf.models import Transporte, TransporteUniversitarioHorario, HorarioTransporte

from diaAbertoConf.forms import TransporteForm, TransporteUniversitarioHorarioForm, HorarioTransporteForm
# Create your views here.

def index(request):
    pass

#Transporte CRUD- Create Read Update Delete
#Creates new transporte
def createTransporte(request):
    if request.method == "POST":
        form = TransporteForm(request.POST)
        if form.is_valid():
            form.save()
            #add later
            return 0
        else:
            form = TransporteForm()
        #add later
        return 0

#show all transportes
def showTransportes(request):
    allTransportes = Transporte.objects.all()
    #add later
    return 0

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
        #add later
        return 0
    #add later
    return 0

#deletes a transporte
def deleteTransporte(request, id):
    dados_transporte = Transporte.objects.get(id = id)
    dados_transporte.delete()
    #add later
    return 0

#TransporteUniversitario_Horario CRUD- Create Read Update Delete
#Creates new TransporteUniversitario_Horario, associates Horario to transporte 
# and defines its Origen and Destino
def createTransporteUniversitario_Horario(request):
    if request.method == "POST":
        form = TransporteUniversitarioHorarioForm(request.POST)
        if form.is_valid():
            form.save()
            #add later
            return 0
        else:
            form = TransporteForm()
        #add later
        return 0

#show all transporteUniversidade_Horarios
def showTransporteUniversidade_Horarios(request):
    allTransportesUni_Horario = TransporteUniversitarioHorario.objects.all()
    #add later
    return 0

#gets a transporteUniversidade_Horario with a specific id 
def getTransporteUniversidade_Horario(request, id):
    dados_TransporteUni_Horario = TransporteUniversitarioHorario.objects.get(id = id)
    #add later
    return 0

#upadates the fields of a spcific transporteUniversidade_Horario
def updateTransporteUniversidade_Horario(request, id):
    dados_TransporteUni_Horario = TransporteUniversitarioHorario.objects.get(id = id)
    form = TransporteUniversitarioHorarioForm(request.POST, instance = dados_TransporteUni_Horario)
    if form.is_valid():
        form.save()
        #add later
        return 0
    #add later
    return 0

#deletes a transporteUniversidade_Horario
def deleteTransporte(request, id):
    dados_TransporteUni_Horario = TransporteUniversitarioHorario.objects.get(id = id)
    dados_TransporteUni_Horario.delete()
    #add later
    return 0

#Horario Transporte CRUD- Create Read Update Delete
#Creates new Horario Transporte
def createHorario_Transporte(request):
    if request.method == "POST":
        form = HorarioTransporteForm(request.POST)
        if form.is_valid():
            form.save()
            #add later
            return 0
        else:
            form = HorarioTransporteForm()
        #add later
        return 0

#show all Hprarios Transporte
def showHorarios_Transporte(request):
    allHorarios_Transporte = HorarioTransporte.objects.all()
    #add later
    return 0

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
        #add later
        return 0
    #add later
    return 0

#deletes a Horario_Transporte
def deleteHorario_Transporte(request, id):
    dados_Horario_Transporte = Horario_Transporte.objects.get(id = id)
    dados_Horario_Transporte.delete()
    #add later
    return 0