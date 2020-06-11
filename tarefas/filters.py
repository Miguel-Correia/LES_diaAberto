import django_filters
from .models import Tarefa
from atividades.models import Utilizador

class TarefaFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(field_name="nome", lookup_expr="icontains")
    data_inicial = django_filters.DateFilter(field_name="data", lookup_expr="gte")
    data_final = django_filters.DateFilter(field_name="data", lookup_expr="lte")
    colaboradores__nome = django_filters.CharFilter(field_name="colaboradores__nome", lookup_expr="icontains")
    colaboradores__email = django_filters.CharFilter(field_name="colaboradores__email", lookup_expr="icontains")


    class Meta:
        model = Tarefa
        fields = ['nome', 'tipoTarefa', 'estado', 'data', 'colaboradores__nome', 'colaboradores__email']

class ColaboradorFilter(django_filters.FilterSet):
    nomeColab = django_filters.CharFilter(field_name="nome", lookup_expr="icontains")
    emailColab = django_filters.CharFilter(field_name="email", lookup_expr="icontains")

    class Meta:
        model = Utilizador
        fields = ['nome', 'email']