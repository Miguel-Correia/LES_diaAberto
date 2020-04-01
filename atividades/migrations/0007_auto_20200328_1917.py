# Generated by Django 3.0.4 on 2020-03-28 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividades', '0006_auto_20200328_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnidadeOrganica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, db_column='Nome', max_length=255, null=True)),
            ],
            options={
                'db_table': 'unidade_organica',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Utilizador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, db_column='Email', max_length=255, null=True)),
                ('nome', models.CharField(blank=True, db_column='Nome', max_length=255, null=True)),
                ('data_de_nascimento', models.DateField(blank=True, db_column='Data_de_nascimento', null=True)),
                ('numero_telemovel', models.IntegerField(blank=True, db_column='Numero_telemovel', null=True)),
                ('cartao_cidadao', models.IntegerField(blank=True, db_column='Cartao_cidadao', null=True)),
                ('deficiencias', models.CharField(blank=True, db_column='Deficiencias', max_length=255, null=True)),
                ('permitir_localizacao', models.IntegerField(blank=True, db_column='Permitir_localizacao', null=True)),
                ('utilizar_dados_pessoais', models.IntegerField(blank=True, db_column='Utilizar_dados_pessoais', null=True)),
                ('tema_do_website', models.IntegerField(blank=True, db_column='Tema_do_website', null=True)),
                ('user_type', models.IntegerField(db_column='User_type')),
                ('daltonico', models.IntegerField(blank=True, db_column='Daltonico', null=True)),
                ('validado', models.IntegerField(db_column='Validado')),
                ('check_in_state', models.IntegerField(db_column='Check_in_state')),
            ],
            options={
                'db_table': 'utilizador',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='atividade',
            options={'managed': False},
        ),
    ]
