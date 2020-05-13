from django.db import models
from datetime import datetime
# Create your models here.

class Transporte(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    #hora_chegada = models.TimeField(db_column='Hora_de_chegada', blank=True, null=True)  # Field name made lowercase.
    #hora_partida = models.TimeField(db_column='Hora_de_partida', blank=True, null=True)  # Field name made lowercase.
    tipo_transporte = models.CharField(db_column='Tipo_de_transporte', max_length=255, blank=True, null=True)  # Field name made lowercase.
    capacidade = models.IntegerField(db_column='Capacidade', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.tipo_transporte)

    class Meta:
        managed = True
        db_table = 'transporte'

class HorarioTransporte(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hora_de_partida = models.TimeField(db_column='Hora_de_partida', blank=True, null=True)  # Field name made lowercase.
    hora_de_chegada = models.TimeField(db_column='Hora_de_chegada', blank=True, null=True)  # Field name made lowercase.
    #data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.hora_de_partida) + " - " + str(self.hora_de_chegada)

    class Meta:
        managed = True
        db_table = 'horario'

class Rota(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    transporteid = models.ForeignKey(Transporte, on_delete = models.CASCADE, db_column='TransporteID')  # Field name made lowercase.
    horarioid = models.ForeignKey(HorarioTransporte, on_delete = models.CASCADE, db_column='HorarioID', blank=True, null=True)  # Field name made lowercase.
    origem = models.CharField(db_column='Origem', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destino = models.CharField(db_column='Destino', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'transporte_universitario_horario'
        

class Rota_Inscricao(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rotaid = models.ForeignKey(Rota, on_delete= models.CASCADE, db_column='Transporte_Universitario_HorarioID', null=True, blank=True)  # Field name made lowercase.
    inscricaoid = models.ForeignKey("atividades.Inscricao", on_delete= models.CASCADE, db_column='InscricaoID', null=True, blank=True)  # Field name made lowercase.
    num_passageiros = models.IntegerField(db_column='Num_passageiros', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'transporte_universitario_horario_inscricao'



class Ementa(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dia = models.DateField(db_column='Dia', blank=True, null=True)  # Field name made lowercase.
    preco_economico = models.FloatField(db_column='Preco_economico_aluno', blank=True, null=True)  # Field name made lowercase.
    preco_normal = models.FloatField(db_column='Preco_normal_aluno', blank=True, null=True)  # Field name made lowercase.
    #preco_economico_outro = models.FloatField(db_column='Preco_economico_outro', blank=True, null=True)  # Field name made lowercase.
    #preco_outro = models.FloatField(db_column='Preco_outro', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return "Ementa " + str(self.id)

    class Meta:
        #managed = False
        db_table = 'ementa'


class Prato(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ementaid = models.ForeignKey(Ementa, on_delete=models.CASCADE, db_column='EmentaID')  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'prato'