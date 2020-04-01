from django.forms import ModelForm
from diaAbertoConf.models import Transporte, TransporteUniversitarioHorario, HorarioTransporte, Prato, Ementa

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

class EmentaForm(ModelForm):
    class Meta:
        model = Ementa
        fields =    '__all__'

class PratoForm(ModelForm):
    class Meta:
        model = Prato
        fields =    '__all__'