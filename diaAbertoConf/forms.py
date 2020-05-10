from django import forms
from django.forms import ModelForm, TextInput, NumberInput, CheckboxSelectMultiple, formset_factory, modelformset_factory, Select
from django.utils.translation import gettext_lazy as _
from diaAbertoConf.models import Transporte, Rota, HorarioTransporte, Rota_Inscricao, Prato, Ementa
from atividades.models import Inscricao

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

""" class RotaForm(ModelForm):
    class Meta:
        model = Rota
        fields = '__all__'

        widgets = {
            'horarioid': CheckboxSelectMultiple(choices = [(horario.id, horario) for horario in HorarioTransporte.objects.all()]),
            'origem': TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza uma origem',
                'required' : 'required',
            }),
            'destino': TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza um destino',
                'required' : 'required',
            }),
        }
        labels = {
            'horarioid': _('Horario'),
            'origem': _('Origem'),
            'destino': _('Destino'),
            'data': _('Data'),
        }

RotaFormSet = modelformset_factory(Rota, RotaForm, extra=1)  """


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

RotaFormSet = formset_factory(RotaForm, extra=1)

class HorarioTransporteForm(ModelForm):
    class Meta:
        model = HorarioTransporte
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        hpartida = cleaned_data.get("hora_de_partida")
        hchegada = cleaned_data.get("hora_de_chegada")

        if hpartida >= hchegada:
            raise forms.ValidationError(
                _('Hora de partida deve ser inferior a hora de chegada'),
                code='invalid'
            )

class RotaInscForm(ModelForm):


    class Meta:
        model = Rota_Inscricao
        fields = ['inscricaoid', 'num_passageiros']

        widgets = { 
            'inscricaoid': Select(
                choices= [],
                attrs= {
                    'class' : 'form-control',
                    'required' : 'required',
                }),
            'num_passageiros': NumberInput(
                attrs= {
                    'class' : 'form-control',
                    'required' : 'required',
                    'placeholder': 'Introduza o número de passageiros',
                    'min': '0',
                }),
        }
        labels = {
            'inscricaoid': _('Grupo'),
            'num_passageiros': _('Número de Passageiros'),
        } 

    def __init__(self, *args, choices, **kwargs):
        
        super(RotaInscForm, self).__init__(*args, **kwargs)
        self.fields['inscricaoid'].choices = choices


RotasInscFormset = modelformset_factory(Rota_Inscricao, RotaInscForm, extra=1)


class EmentaForm(ModelForm):
    class Meta:
        model = Ementa
        fields =    '__all__'

class PratoForm(ModelForm):
    class Meta:
        model = Prato
        fields =    '__all__'