from django.contrib import admin

from .models import *

class Med_ConcenInline(admin.TabularInline):
    model = Medicamento.concentraciones.through


class ConcentracionesAdmin(admin.ModelAdmin):
    inlines = [
        Med_ConcenInline,
    ]
    list_display = ('id', 'valor')


class MedAdmin(admin.ModelAdmin):
    inlines = [
        Med_ConcenInline,
    ]
    model = Medicamento
    list_display = ('codigo_medicamento', 'nombre_medicamento')

class Med_FarInline(admin.TabularInline):
    model = Farmacia.medicamentos.through

class FarmaciaAdmin(admin.ModelAdmin):

    inlines = [
        Med_FarInline,
    ]
    list_display = ('nombre_farmacia', 'descuento')


admin.site.register(Medicamento, MedAdmin)
admin.site.register(Med_Concentracion)
admin.site.register(Concentracion, ConcentracionesAdmin)
admin.site.register(Farmacia, FarmaciaAdmin)
# Register your models here.
