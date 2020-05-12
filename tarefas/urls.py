from django.urls import path

from . import views


app_name =  'tarefas'
urlpatterns = [
    path('create', views.createTarefa, name='createTarefa'),
    path('getSessoes/<int:atividadeid>', views.getSessoes, name='getSessoes'),
    path('getInscricoesByDate/<str:date>', views.getInscricoesByDate, name='getInscricoesByDate'),
    path('getSessoes_Inscricao/<int:inscricaoid>', views.getSessoes_Inscricao, name='getSessoes_Inscricao'),
]