# Generated by Django 3.0.4 on 2020-03-26 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edicifio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_edificio', models.IntegerField(blank=True, db_column='Num_edificio', null=True)),
            ],
            options={
                'db_table': 'edicifio',
                'managed': False,
            },
        ),
    ]