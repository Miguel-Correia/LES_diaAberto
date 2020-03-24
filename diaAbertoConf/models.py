from django.db import models

# Create your models here.


class Transporte(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hora_chegada = models.TimeField(db_column='Hora_de_chegada', blank=True, null=True)  # Field name made lowercase.
    hora_partida = models.TimeField(db_column='Hora_de_partida', blank=True, null=True)  # Field name made lowercase.
    tipo_transporte = models.CharField(db_column='Tipo_de_transporte', max_length=255, blank=True, null=True)  # Field name made lowercase.
    capacidade = models.IntegerField(db_column='Capacidade', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.tipo_transporte

    class Meta:
        managed = False
        db_table = 'transporte'
