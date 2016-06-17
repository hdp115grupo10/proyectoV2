from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Medicamento(models.Model):
    codigo_medicamento=models.CharField(max_length=7, primary_key=True)
    nombre_medicamento=models.CharField(max_length=50)
    concentraciones=models.ManyToManyField('Concentracion', through='Med_Concentracion')
    def __str__(self):
        return self.nombre_medicamento
    def get_precio2013(self):
        return self.precio2013
    def get_precio2014(self):
        return self.precio2014
    def get_precio2013(self):
        return self.precio2014

@python_2_unicode_compatible
class Farmacia(models.Model):
    nombre_farmacia=models.CharField(max_length=30)
    descuento=models.FloatField()
    medicamentos=models.ManyToManyField('Med_Concentracion', through='SeVende')
    def __str__(self):
        return self.nombre_farmacia

@python_2_unicode_compatible
class Anios(models.Model):
    anio=models.CharField(max_length=44)
    medicamentos=models.ManyToManyField('Med_Concentracion', through='Precio_anios')
    def __str__(self):
        return self.anio

@python_2_unicode_compatible
class Concentracion(models.Model):
    valor=models.CharField(max_length=10)
    def __str__(self):
        return self.valor

class Med_Concentracion(models.Model):
    medicamento=models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    concentracion=models.ForeignKey(Concentracion, on_delete=models.CASCADE)

class Precio_anios(models.Model):
    medicamento=models.ForeignKey(Med_Concentracion, on_delete=models.CASCADE)
    anio=models.ForeignKey(Anios, on_delete=models.CASCADE)
    precio=models.DecimalField(decimal_places=2, max_digits=10)

class SeVende(models.Model):
    medicamento=models.ForeignKey(Med_Concentracion, on_delete=models.CASCADE)
    farmacia=models.ForeignKey(Farmacia, on_delete=models.CASCADE)
