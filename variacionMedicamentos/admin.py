from django.contrib import admin

from .models import *

class Med_ConcenInline(admin.TabularInline):
    model = Medicamento.concentraciones.through


class ConcentracionesAdmin(admin.ModelAdmin):
    inlines = [
        Med_ConcenInline,
    ]


class MedAdmin(admin.ModelAdmin):
    inlines = [
        Med_ConcenInline,
    ]
    exclude = ('concentraciones',)
    model = Medicamento


class Med_Con_AnioInLine(admin.TabularInline):
    model = Anios.medicamentos.through


class Med_ConcentracionAdmin(admin.ModelAdmin):
    inlines = [
        Med_Con_AnioInLine
    ]
class AnioAdmin(admin.ModelAdmin):
    inlines = [
        Med_Con_AnioInLine
    ]



admin.site.register(Medicamento, MedAdmin)
admin.site.register(Med_Concentracion, Med_ConcentracionAdmin)
admin.site.register(Concentracion)
admin.site.register(Farmacia)
admin.site.register(Anios)
# Register your models here.
