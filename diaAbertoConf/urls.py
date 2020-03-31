from django.urls import path

from . import views


app_name =  'diaAbertoConf'
urlpatterns = [
    path('', views.index, name='index'),
    path('GestaoTransportes/', views.gestaoTransportes, name='gestaoTransportes'),

    path('GestaoTransporte/Transportes/', views.showTransportes, name='allTransportes'),
    path('GestaoTransporte/Transportes/create', views.showCreateTransporte, name='showCreateTransporte'),
    path('GestaoTransporte/Transportes/add', views.createTransporte, name= 'addTransporte'),
    path('GestaoTransporte/Transportes/delete/<int:id>', views.deleteTransporte, name= 'deleteTransporte'),
    path('GestaoTransporte/Transportes/update/<int:id>', views.showUpdateTransporte, name='showUpdateTransporte'),
    path('GestaoTransporte/Transportes/updates/<int:id>', views.updateTransporte, name= 'updateTransporte'),

    path('GestaoTransporte/HorariosTransporte/', views.showHorarios_Transporte, name='allHorarios'),
    path('GestaoTransporte/HorariosTransporte/create', views.showCreateHorario_Transporte, name='showCreateHorarioTransporte'),
    path('GestaoTransporte/HorariosTransporte/add', views.createHorario_Transporte, name= 'addHorarioTransporte'),
    path('GestaoTransporte/HorariosTransporte/delete/<int:id>', views.deleteHorario_Transporte, name= 'deleteHorarioTransporte'),
    path('GestaoTransporte/HorariosTransporte/update/<int:id>', views.showUpdateHorario_Transporte, name='showUpdateHorarioTransporte'),
    path('GestaoTransporte/HorariosTransporte/updates/<int:id>', views.updateHorario_Transporte, name= 'updateHorarioTransporte'),

    path('GestaoTransporte/RotasTransporte/', views.showTransporteUniversitario_Horarios, name='allRotasTransporte'),
    path('GestaoTransporte/RotasTransporte/create', views.showCreateTransporteUniversitario_Horario, name='showCreateRotaTransporte'),
    path('GestaoTransporte/RotasTransporte/add', views.createTransporteUniversitario_Horario, name='addRotaTransporte'),
    path('GestaoTransporte/RotasTransporte/delete/<int:id>', views.deleteTransporteUniversitario_Horario, name= 'deleteRotaTransporte'),
    path('GestaoTransporte/RotasTransporte/update/<int:id>', views.showUpdateTransporteUniversitario_Horario, name='showUpdateRotaTransporte'),
    path('GestaoTransporte/RotasTransporte/updates/<int:id>', views.updateTransporteUniversitario_Horario, name='updateRotaTransporte'),
    



]   