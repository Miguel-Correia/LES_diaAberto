from django.db import models

# Create your models here.

class Tarefa(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sessao_atividade_inscricaoid_destino = models.ForeignKey("atividades.SessaoAtividadeInscricao", related_name='destino', on_delete=models.SET_NULL, db_column='Sessao_Atividade_InscricaoID_Destino', blank=True, null=True)  # Field name made lowercase.
    sessao_atividade_inscricaoid_origem = models.ForeignKey("atividades.SessaoAtividadeInscricao", related_name='origem', on_delete=models.SET_NULL, db_column='Sessao_Atividade_InscricaoID_Origem', blank=True, null=True)  # Field name made lowercase.
    utilizadorid = models.ForeignKey("atividades.Utilizador", models.DO_NOTHING, db_column='UtilizadorID')  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.
    localizacao_do_grupo = models.CharField(db_column='Localizacao_do_grupo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destino = models.CharField(db_column='Destino', max_length=255, blank=True, null=True)  # Field name made lowercase.
    horario = models.TimeField(db_column='Horario', blank=True, null=True)  # Field name made lowercase.
    tipoTarefa = models.CharField(db_column='TarefaTransporte', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tarefa'


class TarefaSessaoAtividade(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tarefaid = models.ForeignKey(Tarefa, on_delete=models.CASCADE, db_column='TarefaID')  # Field name made lowercase.
    sessao_atividadeid = models.ForeignKey("atividades.SessaoAtividade", on_delete=models.CASCADE, db_column='Sessao_AtividadeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tarefa_sessao_atividade'

class ColaboradorTarefa(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    utilizadorid = models.ForeignKey("atividades.Utilizador", on_delete=models.CASCADE, db_column='UtilizadorID')  # Field name made lowercase.
    tarefaid = models.ForeignKey(Tarefa, on_delete=models.CASCADE, db_column='TarefaID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'utilizador_tarefa'
