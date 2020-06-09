import django_filters
from .models import Tarefa

class TarefaFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(field_name="nome", lookup_expr="icontains")
    data_inicial = django_filters.DateFilter(field_name="data", lookup_expr="gte")
    data_final = django_filters.DateFilter(field_name="data", lookup_expr="lte")
    colaboradores__nome = django_filters.CharFilter(field_name="colaboradores__nome", lookup_expr="icontains")
    colaboradores__email = django_filters.CharFilter(field_name="colaboradores__email", lookup_expr="icontains")


    class Meta:
        model = Tarefa
        fields = ['nome', 'tipoTarefa', 'estado', 'data', 'colaboradores__nome', 'colaboradores__email']
        