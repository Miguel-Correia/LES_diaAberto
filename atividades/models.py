from django.db import models

# Create your models here.


class Edicifio(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    num_edificio = models.IntegerField(db_column='Num_edificio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'edicifio'