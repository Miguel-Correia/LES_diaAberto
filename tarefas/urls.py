from django.urls import path

from . import views


app_name =  'tarefas'
urlpatterns = [
    path('create', views.createTarefa, name='createTarefa'),
    path('getSessoes/<int:atividadeid>', views.getSessoes, name='getSessoes'),
]