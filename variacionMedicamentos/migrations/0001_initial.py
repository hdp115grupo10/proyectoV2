# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 06:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anio', models.CharField(max_length=44)),
            ],
        ),
        migrations.CreateModel(
            name='Concentracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Farmacia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_farmacia', models.CharField(max_length=30)),
                ('descuento', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Med_Concentracion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concentracion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variacionMedicamentos.Concentracion')),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('codigo_medicamento', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('nombre_medicamento', models.CharField(max_length=50)),
                ('concentraciones', models.ManyToManyField(through='variacionMedicamentos.Med_Concentracion', to='variacionMedicamentos.Concentracion')),
            ],
        ),
        migrations.CreateModel(
            name='Precio_anios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('anio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variacionMedicamentos.Anios')),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variacionMedicamentos.Med_Concentracion')),
            ],
        ),
        migrations.CreateModel(
            name='SeVende',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmacia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variacionMedicamentos.Farmacia')),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variacionMedicamentos.Med_Concentracion')),
            ],
        ),
        migrations.AddField(
            model_name='med_concentracion',
            name='medicamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='variacionMedicamentos.Medicamento'),
        ),
        migrations.AddField(
            model_name='farmacia',
            name='medicamentos',
            field=models.ManyToManyField(through='variacionMedicamentos.SeVende', to='variacionMedicamentos.Med_Concentracion'),
        ),
        migrations.AddField(
            model_name='anios',
            name='medicamentos',
            field=models.ManyToManyField(through='variacionMedicamentos.Precio_anios', to='variacionMedicamentos.Med_Concentracion'),
        ),
    ]
