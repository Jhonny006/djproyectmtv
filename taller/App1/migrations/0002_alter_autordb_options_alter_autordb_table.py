# Generated by Django 5.0.2 on 2024-07-07 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autordb',
            options={'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterModelTable(
            name='autordb',
            table='Autores',
        ),
    ]
