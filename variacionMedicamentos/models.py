from django.db import models
from django.forms import ModelForm
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Medicamento(models.Model):
    codigo_medicamento=models.CharField(max_length=7, primary_key=True)
    nombre_medicamento=models.CharField(max_length=50)
    concentraciones=models.ManyToManyField('Concentracion', through='Med_Concentracion')
    def __str__(self):
        return "{0}, {1}".format(self.nombre_medicamento, self.codigo_medicamento)

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
@python_2_unicode_compatible
class Med_Concentracion(models.Model):
    medicamento=models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    concentracion=models.ForeignKey(Concentracion, on_delete=models.CASCADE)
    def __str__(self):
        return "{0}, {1}".format(self.medicamento, self.concentracion)

@python_2_unicode_compatible
class Precio_anios(models.Model):
    medicamento=models.ForeignKey(Med_Concentracion, on_delete=models.CASCADE)
    anio=models.ForeignKey(Anios, on_delete=models.CASCADE)
    precio=models.DecimalField(decimal_places=2, max_digits=10)
    def __str__(self):
        return "{0}, {1}".format(self.medicamento, self.anio, self.precio)

@python_2_unicode_compatible
class SeVende(models.Model):
    medicamento=models.ForeignKey(Med_Concentracion, on_delete=models.CASCADE)
    farmacia=models.ForeignKey(Farmacia, on_delete=models.CASCADE)
    def __str__(self):
        return "{0}, {1}".format(self.medicamento, self.farmacia)

class MedicamentosForm(ModelForm):
    class Meta:
        model = Medicamento
        fields = ['codigo_medicamento', 'nombre_medicamento', 'concentraciones']

class ConcentracionesForm(ModelForm):
    class Meta:
        model = Med_Concentracion
        fields = ['medicamento', 'concentracion']
