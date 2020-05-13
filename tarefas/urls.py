from django.urls import path

from . import views


app_name =  'tarefas'
urlpatterns = [
    path('create', views.createTarefa, name='createTarefa'),
    path('getSessoes/<int:atividadeid>', views.getSessoes, name='getSessoes'),
    path('getInscricoesByDate/<str:date>', views.getInscricoesByDate, name='getInscricoesByDate'),
    path('getSessoes_Inscricao/<int:inscricaoid>/<str:hora>', views.getSessoes_Inscricao, name='getSessoes_Inscricao'),
    path('getLocal_Sessao/<int:sessao_atividadeid>', views.getLocal_Sessao, name='getLocal_Sessao'),
    path('getSessoes_InscricaoNext/<int:inscricaoid>/<str:hora>', views.getSessoes_InscricaoNext, name='getSessoes_InscricaoNext'),
]