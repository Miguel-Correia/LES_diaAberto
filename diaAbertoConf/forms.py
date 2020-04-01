from django.forms import ModelForm
from diaAbertoConf.models import Transporte, TransporteUniversitarioHorario, HorarioTransporte

class TransporteForm(ModelForm):
    class Meta:
        model = Transporte
        fields =    '__all__'

class TransporteUniversitarioHorarioForm(ModelForm):
    class Meta:
        model = TransporteUniversitarioHorario
        fields = '__all__'

class HorarioTransporteForm(ModelForm):
    class Meta:
        model = HorarioTransporte
        fields = '__all__'