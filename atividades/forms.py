from django.forms import ModelForm
from atividades.models import Edificio, Campus, Departamento, Local, Atividade, UnidadeOrganica

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields =    '__all__'

class CampusForm(ModelForm):
    class Meta:
        model = Campus
        fields =    '__all__'

class UnidadeOrganicaForm(ModelForm):
    class Meta:
        model = UnidadeOrganica
        fields =    '__all__'

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields =    '__all__'

class LocalForm(ModelForm):
    class Meta:
        model = Local
        fields =    '__all__'

class AtividadeForm(ModelForm):
    class Meta:
        model = Atividade
        fields =    '__all__'
