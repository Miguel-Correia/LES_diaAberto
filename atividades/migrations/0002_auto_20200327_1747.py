# Generated by Django 3.0.4 on 2020-03-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, db_column='Nome', max_length=255, null=True)),
                ('localizacao', models.CharField(blank=True, db_column='Localizacao', max_length=255, null=True)),
                ('contacto', models.CharField(blank=True, db_column='Contacto', max_length=255, null=True)),
            ],
            options={
                'db_table': 'campus',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='edicifio',
            options={'managed': True},
        ),
    ]