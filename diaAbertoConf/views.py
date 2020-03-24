from django.shortcuts import render
from diaAbertoConf.models import Transporte

from diaAbertoConf.forms import TransporteForm
# Create your views here.

def index(request):
    pass

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

#upadates the fields of a spcific transporte
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