import django_filters

from django_filters import DateFilter, CharFilter

from .models import *

class UnidadeOrganicaFilter(django_filters.FilterSet):
	class Meta:
		model = UnidadeOrganica
		fields = '__all__'

class DepartamentoFilter(django_filters.FilterSet):
	class Meta:
		model = Departamento
		fields = '__all__'

class LocalFilter(django_filters.FilterSet):
	class Meta:
		model = Local
		fields = ['edicifioid' ,'campusid']

class CampusFilter(django_filters.FilterSet):
	class Meta:
		model = Campus
		fields = '__all__'

class EdificioFilter(django_filters.FilterSet):
	class Meta:
		model = Edificio
		fields = '__all__'