import django_filters
from .models import Transporte, Rota

class TransporteFilter(django_filters.FilterSet):
    tipo_transporte = django_filters.CharFilter(field_name="tipo_transporte", lookup_expr="icontains")
    origem = django_filters.CharFilter(field_name="rota__origem", lookup_expr="icontains", distinct=True)
    destino = django_filters.CharFilter(field_name="rota__destino", lookup_expr="icontains", distinct=True)
    hora_gte = django_filters.TimeFilter(field_name="rota__horarioid__hora_de_partida", lookup_expr="gte", distinct=True)
    hora_lte = django_filters.TimeFilter(field_name="rota__horarioid__hora_de_chegada", lookup_expr="lte", distinct=True)
    data = django_filters.DateFilter(field_name="rota__data", distinct=True)

    class Meta:
        model = Transporte
        fields = ['tipo_transporte', 'rota__origem', 'rota__destino', 'rota__horarioid__hora_de_partida', 'rota__horarioid__hora_de_chegada', 'rota__data']

class RotaFilter(django_filters.FilterSet):
    origem = django_filters.CharFilter(field_name="origem", lookup_expr="icontains")
    destino = django_filters.CharFilter(field_name="destino", lookup_expr="icontains")
    data = django_filters.DateFilter(field_name="data")
    hora_gte = django_filters.TimeFilter(field_name="horarioid__hora_de_partida", lookup_expr="gte")
    hora_lte = django_filters.TimeFilter(field_name="horarioid__hora_de_chegada", lookup_expr="lte")

    class Meta:
        model = Rota
        fields = ['origem', 'destino', 'data', 'horarioid__hora_de_partida', 'horarioid__hora_de_chegada']