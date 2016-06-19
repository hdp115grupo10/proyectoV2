from django.contrib import admin

from .models import *

class Med_ConcenInline(admin.TabularInline):
    model = Medicamento.concentraciones.through


class ConcentracionesAdmin(admin.ModelAdmin):
    inlines = [
        Med_ConcenInline,
    ]


class MedAdmin(admin.ModelAdmin):
    exclude = ('concentraciones',)

    inlines = [
        Med_ConcenInline,
    ]
    model = Medicamento


admin.site.register(Medicamento, MedAdmin)
admin.site.register(Med_Concentracion)
admin.site.register(Concentracion, ConcentracionesAdmin)
admin.site.register(Farmacia)
# Register your models here.
