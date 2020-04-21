from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.paginator import Paginator


from diaAbertoConf.models import Transporte, TransporteUniversitarioHorario, HorarioTransporte, Ementa, Prato

from diaAbertoConf.forms import TransporteForm, TransporteUniversitarioHorarioForm, HorarioTransporteForm, EmentaForm, PratoForm, RotaFormSet
# Create your views here.

def index(request):
    #template = loader.get_template('diaAbertoConf/DiaAbertoConfMain.html')
    #return HttpResponse(template.render({}, request))
    return render(request, 'diaAbertoConf/Home.html')

#show all transporteUniversidade_Horarios
def showTransportes(request):
    allTransportesUni_Horario = TransporteUniversitarioHorario.objects.all()

    paginator = Paginator(allTransportesUni_Horario, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj,}
    return render(request, 'diaAbertoConf/ShowTransportes.html', context)

#Transporte CRUD- Create Read Update Delete
#Creates new transporte
def createTransporte(request):
    
    horarios = HorarioTransporte.objects.all()

    if request.method == "GET":
        transporteform = TransporteForm(request.GET or None)
        rotaformset = RotaFormSet(request.GET or None)
    elif request.method == "POST":
        transporteform = TransporteForm(request.POST)
        rotaformset = RotaFormSet(request.POST)
        if transporteform.is_valid() and rotaformset.is_valid():
            transporte = transporteform.save()
            for form in rotaformset:    
                for horario in form.cleaned_data['horarioid']:
                    result = TransporteUniversitarioHorario(
                        horarioid= HorarioTransporte.objects.get(id=horario),
                        transporteid = transporte,
                        origem = form.cleaned_data['origem'],
                        destino = form.cleaned_data['destino'],
                        data = form.cleaned_data['data'],
                    )
                    result.save()
            
            return redirect('diaAbertoConf:allTransportes')
        
    return render(request, 'diaAbertoConf/AdicionarTransporte.html', {
        'transporteform' : transporteform,
        'rotaformset': rotaformset,
        'horarios': horarios,
        })

#deletes a transporteUniversidade_Horario
def deleteTransporte(request, id):
    dados_TransporteUni_Horario = TransporteUniversitarioHorario.objects.get(id = id)
    dados_TransporteUni_Horario.delete()
    return HttpResponseRedirect(reverse('diaAbertoConf:allTransportes'))

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
        return render(request, 'diaAbertoConf/newPratos.html', context)   
        