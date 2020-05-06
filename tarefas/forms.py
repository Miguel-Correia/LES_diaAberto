from django import forms
from django.forms import ModelForm, Textarea, RadioSelect
from django.utils.translation import gettext_lazy as _

from tarefas.models import Tarefa, TarefaSessaoAtividade, ColaboradorTarefa

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
        