from django import forms
from django.forms import ModelForm, Textarea, RadioSelect, Select, TextInput
from django.utils.translation import gettext_lazy as _

from tarefas.models import Tarefa, TarefaSessaoAtividade, ColaboradorTarefa
from atividades.models import Atividade, SessaoAtividade

class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ('descricao', 'tipoTarefa')
        #exclude = ['utilizadorid']

        widgets= {
            'descricao': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Introduza a descrição da tarefa',
                'required': 'required',
            }),
            'tipoTarefa': RadioSelect(attrs={
                'class': 'form-check-input',
                'required': 'required',
            },
                choices = (('Atividade', 'Atividade'), ('Transporte', 'Transporte'))
            )
        }

        labels= {
            'descricao': _('Descrição'),
            'tipoTarefa': _('Tipo de Tarefa')
        }

class TarefaAtividadeForm(forms.Form):

    
    atividade = forms.ChoiceField(
        label = 'Atividade',
        widget = Select(attrs= {
            'class' : 'form-control',
            'required' : 'required',
        }),
    )
    sessaoAtividade = forms.ChoiceField(
        label = 'Sessão',
        widget = Select(attrs={
            'class' : 'form-control',
            'required' : 'required',
        })
    )

    def __init__(self, *args, **kwargs):
        self.uoId = kwargs.pop('uoId') 
        super(TarefaAtividadeForm,self).__init__(*args,**kwargs)
        self.fields['atividade'].choices = [(atividade.id, atividade.nome) for atividade in Atividade.objects.filter(unidadeorganicaid = self.uoId).filter(num_colaboradores__gt = 0)]
        firstAtividade = next(iter([atividade.id for atividade in Atividade.objects.filter(unidadeorganicaid = self.uoId).filter(num_colaboradores__gt = 0)]))
        self.fields['sessaoAtividade'].choices = [(sessao.id, str(sessao)) for sessao in SessaoAtividade.objects.filter(atividadeid = firstAtividade)]


class TarefaTransporteForm(forms.Form):


    dia = forms.DateField(
        label = "Dia"
    )
    horario = forms.TimeField(
        label = "Hora"
    )
    inscricao = forms.ChoiceField(
        label = "Grupo",
        widget = Select(attrs={
            'class' : 'form-control',
            'required' : 'required',
        })
    )
    sessaoAtividade_Origem = forms.ChoiceField(
        label = "Atividade atual",
        widget = Select(attrs={
            'class' : 'form-control',
            'required' : 'required',
        })
    )
    sessaoAtividade_Destino = forms.ChoiceField(
        label = "Proxima atividade",
        widget = Select(attrs={
            'class' : 'form-control',
            'required' : 'required',
        })
    )
    origem = forms.CharField(
        label= "Origem",
        widget = TextInput(attrs={
            'class' : 'form-control',
            'required' : 'required',
        })
    )
    destino = forms.CharField(
        label= "Destino",
        widget = TextInput(attrs={
            'class' : 'form-control',
            'required' : 'required',
        })
    )
