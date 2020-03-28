from django.db import models

# Create your models here.


class Transporte(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    #hora_chegada = models.TimeField(db_column='Hora_de_chegada', blank=True, null=True)  # Field name made lowercase.
    #hora_partida = models.TimeField(db_column='Hora_de_partida', blank=True, null=True)  # Field name made lowercase.
    tipo_transporte = models.CharField(db_column='Tipo_de_transporte', max_length=255, blank=True, null=True)  # Field name made lowercase.
    capacidade = models.IntegerField(db_column='Capacidade', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return "Transporte nº " + str(self.id)

    class Meta:
        #managed = True
        db_table = 'transporte'

class HorarioTransporte(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hora_de_partida = models.TimeField(db_column='Hora_de_partida', blank=True, null=True)  # Field name made lowercase.
    Hora_de_chegada = models.TimeField(db_column='Hora_de_chegada', blank=True, null=True)  # Field name made lowercase.
    #data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = True
        db_table = 'horario'

class TransporteUniversitarioHorario(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    horarioid = models.ForeignKey(HorarioTransporte, on_delete = models.CASCADE, db_column='HorarioID')  # Field name made lowercase.
    transporteid = models.ForeignKey(Transporte, on_delete = models.CASCADE, db_column='TransporteID')  # Field name made lowercase.
    origem = models.CharField(db_column='Origem', max_length=255, blank=True, null=True)  # Field name made lowercase.
    destino = models.CharField(db_column='Destino', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data = models.DateField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = True
        db_table = 'transporte_universitario_horario'


class Ementa(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dia = models.DateField(db_column='Dia', blank=True, null=True)  # Field name made lowercase.
    preco_economico_aluno = models.FloatField(db_column='Preco_economico_aluno', blank=True, null=True)  # Field name made lowercase.
    preco_normal_aluno = models.FloatField(db_column='Preco_normal_aluno', blank=True, null=True)  # Field name made lowercase.
    preco_economico_outro = models.FloatField(db_column='Preco_economico_outro', blank=True, null=True)  # Field name made lowercase.
    preco_outro = models.FloatField(db_column='Preco_outro', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ementa'
