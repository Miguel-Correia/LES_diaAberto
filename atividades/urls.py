from django.urls import path

from . import views


app_name =  'atividades'
urlpatterns = [
    path('', views.index, name='index'),
    path('GestaoAtividades/', views.gestaoAtividades, name='gestaoAtividades'),
    path('ShowAtividades/', views.showatividades, name='showatividades'),
    path('AdicionarAtividade/', views.adicionaratividade, name='adicionaratividade'),

    path('GestaoAtividades/Atividades/', views.showAtividades, name='allAtividades'),
    path('GestaoAtividades/Atividades/<int:id>', views.showDetailsAtividade, name='showDetailsAtividade'),
    path('GestaoAtividades/Atividades/create/<int:saved>', views.showCreateAtividade, name='showCreateAtividade'),
    path('GestaoAtividades/Atividades/add', views.createAtividade, name='addAtividade'),
    path('GestaoAtividades/Atividades/delete/<int:id>', views.deleteAtividade, name='deleteAtividade'),
    path('GestaoAtividades/Atividades/update/<int:id>', views.showUpdateAtividade, name='showUpdateAtividade'),
    path('GestaoAtividades/Atividades/updates/<int:id>', views.updateAtividade, name='updateAtividade'),
    path('GestaoAtividades/Atividades/valid/<int:id>', views.validAtividade, name='validAtividade'),
    path('GestaoAtividades/Atividades/recuse/<int:id>', views.recuseAtividade, name='recuseAtividade'),
    path('GestaoAtividades/Atividades/atribuir/<int:id>', views.atribuirLocal, name='atribuirLocal'),
    path('getEdificio/<int:campusid>', views.getEdificio, name='getEdificio'),
    path('getLocal/<int:edificioid>', views.getLocal, name='getLocal'),
    
    path('GestaoAtividades/Edificios/', views.showEdificios, name='allEdificios'),
    path('GestaoAtividades/Edificios/create/<int:saved>', views.showCreateEdificio, name='showCreateEdificio'),
    path('GestaoAtividades/Edificios/add', views.createEdificio, name='addEdificio'),
    path('GestaoAtividades/Edificios/delete/<int:id>', views.deleteEdificio, name='deleteEdificio'),
    path('GestaoAtividades/Edificios/update/<int:id>', views.showUpdateEdificio, name='showUpdateEdificio'),
    path('GestaoAtividades/Edificios/updates/<int:id>', views.updateEdificio, name='updateEdificio'),

    path('GestaoAtividades/Campus/', views.showCampus, name='allCampus'),
    path('GestaoAtividades/Campus/create/<int:saved>', views.showCreateCampus, name='showCreateCampus'),
    path('GestaoAtividades/Campus/add', views.createCampus, name='addCampus'),
    path('GestaoAtividades/Campus/delete/<int:id>', views.deleteCampus, name='deleteCampus'),
    path('GestaoAtividades/Campus/update/<int:id>', views.showUpdateCampus, name='showUpdateCampus'),
    path('GestaoAtividades/Campus/updates/<int:id>', views.updateCampus, name='updateCampus'),

    path('GestaoAtividades/UnidadeOrganicas/', views.showUnidadeOrganicas, name='allUnidadeOrganicas'),
    path('GestaoAtividades/UnidadeOrganicas/create/<int:saved>', views.showCreateUnidadeOrganica, name='showCreateUnidadeOrganica'),
    path('GestaoAtividades/UnidadeOrganicas/add', views.createUnidadeOrganica, name='addUnidadeOrganica'),
    path('GestaoAtividades/UnidadeOrganicas/delete/<int:id>', views.deleteUnidadeOrganica, name='deleteUnidadeOrganica'),
    path('GestaoAtividades/UnidadeOrganicas/update/<int:id>', views.showUpdateUnidadeOrganica, name='showUpdateUnidadeOrganica'),
    path('GestaoAtividades/UnidadeOrganicas/updates/<int:id>', views.updateUnidadeOrganica, name='updateUnidadeOrganica'),

    path('GestaoAtividades/Departamentos/', views.showDepartamentos, name='allDepartamentos'),
    path('GestaoAtividades/Departamentos/create/<int:saved>', views.showCreateDepartamento, name='showCreateDepartamento'),
    path('GestaoAtividades/Departamentos/add', views.createDepartamento, name='addDepartamento'),
    path('GestaoAtividades/Departamentos/delete/<int:id>', views.deleteDepartamento, name='deleteDepartamento'),
    path('GestaoAtividades/Departamentos/update/<int:id>', views.showUpdateDepartamento, name='showUpdateDepartamento'),
    path('GestaoAtividades/Departamentos/updates/<int:id>', views.updateDepartamento, name='updateDepartamento'),

    path('GestaoAtividades/Locais/', views.showLocais, name='allLocais'),
    path('GestaoAtividades/Locais/create/<int:saved>', views.showCreateLocal, name='showCreateLocal'),
    path('GestaoAtividades/Locais/add', views.createLocal, name='addLocal'),
    path('GestaoAtividades/Locais/delete/<int:id>', views.deleteLocal, name='deleteLocal'),
    path('GestaoAtividades/Locais/update/<int:id>', views.showUpdateLocal, name='showUpdateLocal'),
    path('GestaoAtividades/Locais/updates/<int:id>', views.updateLocal, name='updateLocal'),

    path('GestaoAtividades/Tematicas', views.showTematicas, name='allTematicas'),
    path('GestaoAtividades/Tematicas/create', views.showCreateTematica, name='showCreateTematica'),
    path('GestaoAtividades/Tematicas/add', views.addTematica, name='addTematica'),
    path('GestaoAtividades/Tematicas/delete/<int:id>', views.deleteTematica, name='deleteTematica'),
    path('GestaoAtividades/Tematicas/update/<int:id>', views.showUpdateTematica, name='showUpdateTematica'),
    path('GestaoAtividades/Tematicas/updates/<int:id>', views.updateTematica, name='updateTematica'),

    path('GestaoAtividades/Sessoes', views.showSessoes, name='allSessoes'),
    path('GestaoAtividades/Sessoes/create', views.addSessao, name='addSessao'),
    path('GestaoAtividades/Sessoes/update/<int:id>', views.updateSessao, name='updateSessao'),
    path('GestaoAtividades/Sessoes/delete/<int:id>', views.deleteSessao, name="deleteSessao")
  
]