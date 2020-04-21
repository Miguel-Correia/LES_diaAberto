from django.urls import path

from . import views


app_name =  'diaAbertoConf'
urlpatterns = [
    path('', views.index, name='index'),

    path('Transportes/', views.showTransportes, name='allTransportes'),
    path('Transportes/create', views.createTransporte, name='createTransporte'),
    path('Transportes/delete/<int:id>', views.deleteTransporte, name= 'deleteTransporte'),

    #path('GestaoTransporte/Transportes/update/<int:id>', views.showUpdateTransporte, name='showUpdateTransporte'),
    #path('GestaoTransporte/Transportes/updates/<int:id>', views.updateTransporte, name= 'updateTransporte'),

    path('GestaoTransporte/HorariosTransporte/', views.showHorarios_Transporte, name='allHorarios'),
    path('GestaoTransporte/HorariosTransporte/create', views.showCreateHorario_Transporte, name='showCreateHorarioTransporte'),
    path('GestaoTransporte/HorariosTransporte/add', views.createHorario_Transporte, name= 'addHorarioTransporte'),
    path('GestaoTransporte/HorariosTransporte/delete/<int:id>', views.deleteHorario_Transporte, name= 'deleteHorarioTransporte'),
    path('GestaoTransporte/HorariosTransporte/update/<int:id>', views.showUpdateHorario_Transporte, name='showUpdateHorarioTransporte'),
    path('GestaoTransporte/HorariosTransporte/updates/<int:id>', views.updateHorario_Transporte, name= 'updateHorarioTransporte'),

    path('GestaoEmentas/',views.gestaoEmentas, name='gestaoEmentas'),
    path('GestaoEmentas/delete/<int:id>',views.deleteEmenta, name='deleteEmenta'),
    path('GestaoEmentas/create',views.showNewEmenta, name='showNewEmenta'),
    path('GestaoEmentas/add', views.newEmenta, name='newEmenta'),
    path('GestaoEmentas/create/createPratos/<int:id>',views.showNewPratos, name='showNewPratos'),
    path('GestaoEmentas/create/addPratos/<int:id>', views.newPrato, name='newPratos'),
    

]   