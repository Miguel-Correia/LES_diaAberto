from django import forms
from django.forms import ModelForm, Textarea, RadioSelect, Select, TextInput, formset_factory
from django.utils.translation import gettext_lazy as _

from tarefas.models import Tarefa
from atividades.models import Atividade, SessaoAtividade

class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ('descricao', 'tipoTarefa', 'nome')
        #exclude = ['utilizadorid']

        widgets= {
            'nome': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Introduza o nome da tarefa',
                'required': 'required',
            }),
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
            'nome': _('Nome'),
            'descricao': _('Descrição'),
            'tipoTarefa': _('Tipo de Tarefa')
        }

class TarefaAtividadeForm(forms.Form):

    
    atividade = forms.CharField(
        label = 'Atividade',
        widget = Select(attrs= {
            'class' : 'form-control',
            
        },choices = [])
    )
    sessaoAtividade = forms.CharField(
        label = 'Sessão',
        widget = Select(attrs={
            'class' : 'form-control',
        },choices = [])
    )

    def __init__(self, *args, **kwargs):
        self.uoId = kwargs.pop('uoId') 
        super(TarefaAtividadeForm,self).__init__(*args,**kwargs)
        self.fields['atividade'].widget.choices = [(atividade.id, atividade.nome) for atividade in Atividade.objects.filter(unidadeorganicaid = self.uoId).filter(num_colaboradores__gt = 0)]
        firstAtividade = next(iter([atividade.id for atividade in Atividade.objects.filter(unidadeorganicaid = self.uoId).filter(num_colaboradores__gt = 0)]))
        self.fields['sessaoAtividade'].widget.choices = [(sessao.id, str(sessao)) for sessao in SessaoAtividade.objects.filter(atividadeid = firstAtividade)]


class TarefaTransporteForm(forms.Form):

    dia = forms.DateField(
        label = "Dia"
    )
    horario = forms.TimeField(
        label = "Hora"
    )
    sessaoAtividade_origem = forms.CharField(
        label = "Atividade atual",
        widget = Select(attrs={
            'class' : 'form-control',
        })
    )
    sessaoAtividade_destino = forms.CharField(
        label = "Proxima atividade",
        widget = Select(attrs={
            'class' : 'form-control',
        })
    )
    origem = forms.CharField(
        label= "Origem",
    )
    destino = forms.CharField(
        label= "Destino",
    )

class TarefaGruposForm(forms.Form):
    inscricao = forms.CharField(
        label = "Grupo",
        widget = Select(attrs={
            'class' : 'form-control',
        })
    )

TarefaGruposFormset = formset_factory(TarefaGruposForm, extra=1)