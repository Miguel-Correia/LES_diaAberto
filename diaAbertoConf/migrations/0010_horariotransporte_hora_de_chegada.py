# Generated by Django 3.0.4 on 2020-04-01 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaAbertoConf', '0009_remove_horariotransporte_hora_de_chegada'),
    ]

    operations = [
        migrations.AddField(
            model_name='horariotransporte',
            name='hora_de_chegada',
            field=models.TimeField(blank=True, db_column='Hora_de_chegada', null=True),
        ),
    ]
