from django.utils.translation import gettext_lazy as _
from django import forms
from django.forms import ModelForm, TextInput, NumberInput, Select, Textarea, modelformset_factory, formset_factory 
from atividades.models import Edificio, Campus, Departamento, Local, Atividade, UnidadeOrganica, Tematica, Material, AtividadeTematica, AtividadeMaterial, SessaoAtividade, Sessao


class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields =    '__all__'

class CampusForm(ModelForm):
    class Meta:
        model = Campus
        fields =    '__all__'

class UnidadeOrganicaForm(ModelForm):
    class Meta:
        model = UnidadeOrganica
        fields =    '__all__'

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields =    '__all__'

class LocalForm(ModelForm):
    class Meta:
        model = Local
        fields =    ['campusid', 'indoor', 'descricao', 'sala', 'andar']

class AtividadeForm(ModelForm):
    class Meta:
        model = Atividade
        fields =    ['nome', 'descricao', 'duracao', 'limite_de_participantes', 'tipo_atividade', 'public_alvo', 'localid']
        choices = (('Laboratorial', 'Laboratorial'),('Prática', 'Prática'), ('Teórica', 'Teórica'),)
        widgets = {
            'nome' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza o nome da atividade',
                'required' : 'required',

            }),

            'descricao' : Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza uma descrição da atividade',
                'required' : 'required',
            }),

            'duracao' : NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza a duração da atividade',
                'min' : 10,
                'required' : 'required',
            }),

            'limite_de_participantes' : NumberInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza um limite de participantes',
                'min' : 0,
                'required' : 'required',
            }),

            'tipo_atividade' : Select(attrs={
                'class' : 'form-control',
                'required' : 'required',
            }, choices = choices),

            'public_alvo' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Introduza o público alvo',
                'required' : 'required',
            }),

            'localid' : Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Indique qual o tipo de local',
                'required' : 'required',
            }),
        }
        labels = {
            'nome' : _('Nome'),
            'descricao' : _('Descrição'),
            'duracao' : _('Duração'),
            'limite_de_participantes' : _('Limite de participantes'),
            'tipo_atividade' : _('Tipo de atividade'),
            'public_alvo' : _('Público alvo'),
            'localid' : _('Local'),
        }

class TematicaForm(ModelForm):
    class Meta:
        model = Tematica
        fields =    '__all__'


# AtividadeTematicaFormset = modelformset_factory(
#     AtividadeTematica,
#     fields=('tematicaid', ),
#     extra = 1,
#     labels = {
#             'tematicaid' : _('Temática'),
#             },
#     widgets={'tematicaid': Select(attrs={
#             'class': 'form-control',
#         },choices = [(tematica.id, tematica.nome) for tematica in Tematica.objects.all()])
#     }
# )

# AtividadeMaterialFormset = modelformset_factory(
#     AtividadeMaterial,
#     fields=('materialid', 'quantidade'),
#     extra = 1,
#     labels = {
#             'materialid' : _('Material'),
#             'quantidade' : _('Quantidade'),
#             },
#     widgets={'materialid': Select(attrs={
#             'class': 'form-control',
#         },choices = [(material.id, material.nome) for material in Material.objects.all()]),
#         'quantidade': NumberInput(attrs={
#             'class': 'form-control',
#             'placeholder' : 'Introduza a quantidade',
#             'min' : 1,
#         }),
#     }
# )

class AtividadeTematicaForm(ModelForm):

    class Meta:
        model = AtividadeTematica
        fields = ['tematicaid']
        widgets = { 
            'tematicaid': Select(
                choices= [(tematica.id, tematica.nome) for tematica in Tematica.objects.all()],
                attrs= {
                    'class' : 'form-control',
                }),
        }
        labels = {
            'tematicaid': ('Temática'),
        } 

AtividadeTematicaFormset = modelformset_factory(AtividadeTematica, AtividadeTematicaForm, extra=1)

class AtividadeMaterialForm(ModelForm):

    class Meta:
        model = AtividadeMaterial
        fields = ['materialid', 'quantidade']
        widgets = { 
            'materialid': Select(
                choices= [(material.id, material.nome) for material in Material.objects.all()],
                attrs= {
                    'class' : 'form-control',
                }),
            'quantidade': NumberInput(attrs={
            'class': 'form-control',
            'placeholder' : 'Introduza a quantidade',
            'min' : 1,
            }),
        }
        labels = {
            'materialid': ('Material'),
            'quantidade' : ('Quantidade'),
        } 

AtividadeMaterialFormset = modelformset_factory(AtividadeMaterial, AtividadeMaterialForm, extra=1)

class AtividadeSessaoForm(forms.Form):
    sessaoid = forms.MultipleChoiceField(
        label = 'Sessão', 
        widget=forms.CheckboxSelectMultiple(),
        choices = [(sessao.id, sessao.hora_de_inicio) for sessao in Sessao.objects.all()]
        )
    data = forms.DateField(
        label = 'Data'
    )

AtividadeSessaoFormset = formset_factory(AtividadeSessaoForm, extra=1)

# class AtividadeSessaoForm(ModelForm):

#     class Meta:
#         model = SessaoAtividade
#         fields = ['sessaoid', 'data']
#         widgets = { 
#             'sessaoid': MultipleChoiceField(
#                 choices= [(sessao.id, sessao.hora_de_inicio) for sessao in Sessao.objects.all()],
#                 attrs= {
#                     'class' : 'form-control',
#                 }),
#             'data': DateField(attrs={
#             'class': 'form-control',
#             'placeholder' : 'Introduza uma data',
#             }),
#         }
#         labels = {
#             'sessaoid': ('Sessão'),
#             'data' : ('Data'),
#         } 

# AtividadeSessaoFormset = modelformset_factory(SessaoAtividade, AtividadeSessaoForm, extra=1)

class SessaoForm(ModelForm):
    class Meta:
        model = Sessao
        fields =    '__all__'
