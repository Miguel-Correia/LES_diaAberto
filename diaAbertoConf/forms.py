from django import forms
from django.forms import ModelForm, TextInput, NumberInput, CheckboxSelectMultiple, modelformset_factory, formset_factory
from django.utils.translation import gettext_lazy as _
from diaAbertoConf.models import Transporte, TransporteUniversitarioHorario, HorarioTransporte, Prato, Ementa

class TransporteForm(ModelForm):
    class Meta:
        model = Transporte
        fields =    '__all__'

        widgets = {
            'tipo_transporte' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza o tipo de transporte',
                'required' : 'required',

            }),

            'capacidade' : NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza a capacidade',
                'min' : '1',
                'required' : 'required',
            }),
        }
        labels = {
            'tipo_transporte' : _('Tipo de Transporte'),
            'capacidade' : _('Capacidade'),
        }


class RotaForm(forms.Form):
    horarioid = forms.MultipleChoiceField(
        label = 'Horario', 
        widget=forms.CheckboxSelectMultiple(),
        choices = [(horario.id, horario) for horario in HorarioTransporte.objects.all()]
        )
    origem = forms.CharField(
        label = 'Origem',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza uma origem',
                'required' : 'required',
            }
        )
    )
    destino = forms.CharField(
        label = 'Destino',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza um destino',
                'required' : 'required',
            }
        )
    )
    data = forms.DateField(
        label = 'Data'
    )

RotaFormSet = formset_factory(RotaForm, extra = 1)

""" RotaFormSet = modelformset_factory(
    TransporteUniversitarioHorario,
    fields = ('horarioid', 'origem', 'destino', 'data'),
    extra= 1,
    widgets = {
        'horarioid' : CheckboxSelectMultiple(
            choices = [(horario.id, horario) for horario in HorarioTransporte.objects.all()]
        ),
        'origem' : TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Introduza uma origem',
            'required' : 'required',
        }),
        'destino' : TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Introduza um destino',
            'required' : 'required',
        }),
    },
    labels= {
        'horarioid': _('Horario'),
        'origem': _('Origem'),
        'destino': _('Destino'),
        'data': _('Data'),
    }
) """

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