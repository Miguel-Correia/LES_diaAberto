import django_filters
from .models import Tarefa

class TarefaFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(field_name="nome", lookup_expr="icontains")
    class Meta:
        model = Tarefa
        fields = ['nome', 'tipoTarefa', 'estado', 'data']
        