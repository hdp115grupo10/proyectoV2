from django.contrib import admin

from .models import *


class ConcentracionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'valor')


class MedAdmin(admin.ModelAdmin):
    model = Medicamento
    list_display = ('codigo_medicamento', 'nombre_medicamento')

class FarmaciaAdmin(admin.ModelAdmin):
    model = Farmacia
    list_display = ('nombre_farmacia', 'descuento')

class Med_ConAdmin(admin.ModelAdmin):
    model = Med_Concentracion
    list_display = ('medicamento', 'concentracion', 'precio13', 'precio14', 'precio15')

admin.site.register(Medicamento, MedAdmin)
admin.site.register(Med_Concentracion)
admin.site.register(Concentracion, ConcentracionesAdmin)
admin.site.register(Farmacia, FarmaciaAdmin)
# Register your models here.
