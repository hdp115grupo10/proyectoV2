#importacion de paquetes necesarios
from django.contrib import admin
from .models import *


class ConcentracionesAdmin(admin.ModelAdmin):
    """Se configura los campos que va a mostrar el administrador de Concentraciones"""
    list_display = ('id', 'valor')

class MedAdmin(admin.ModelAdmin):
    """Se configura los campos que va a mostrar el administrador de Medicamentos"""
    model = Medicamento
    list_display = ('codigo_medicamento', 'nombre_medicamento')

class FarmaciaAdmin(admin.ModelAdmin):
    """Se configura los campos que va a mostrar el administrador de Farmacias"""
    model = Farmacia
    list_display = ('nombre_farmacia', 'descuento')

class Med_ConAdmin(admin.ModelAdmin):
    """Se configura los campos que va a mostrar el administrador de La relacion de los medicamentos con las concentraciones"""
    model = Med_Concentracion
    list_display = ('medicamento', 'concentracion', 'precio13', 'precio14', 'precio15')

class SeVendeAdmin(admin.ModelAdmin):
    """Se configura los campos que va a mostrar el administrador de relacion de los medicamentos con sus concentraciones y las farmacias"""
    model = SeVende
    list_display = ('medicamento', 'farmacia')
#Asignacion de opciones de registro al Admin
admin.site.register(Medicamento, MedAdmin)
admin.site.register(Med_Concentracion)
admin.site.register(Concentracion, ConcentracionesAdmin)
admin.site.register(Farmacia, FarmaciaAdmin)
admin.site.register(SeVende, SeVendeAdmin)
# Register your models here.
