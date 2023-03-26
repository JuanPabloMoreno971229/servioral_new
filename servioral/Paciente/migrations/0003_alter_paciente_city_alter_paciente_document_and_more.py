# Generated by Django 4.0.4 on 2022-05-19 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ciudad', '0002_remove_ciudad_address_alter_ciudad_ciudad'),
        ('Genero', '0002_alter_genero_options_alter_genero_genero'),
        ('Documento', '0002_alter_documento_tipodocu'),
        ('Paciente', '0002_paciente_tto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Ciudad.ciudad', verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Documento.documento', verbose_name='Documento'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Genero.genero', verbose_name='Género'),
        ),
    ]