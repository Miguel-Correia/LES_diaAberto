from django.forms import ModelForm
from diaAbertoConf.models import Transporte

class TransporteForm(ModelForm):
    class Meta:
        model = Transporte
        fields =    '__all__'