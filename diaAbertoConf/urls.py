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
]   