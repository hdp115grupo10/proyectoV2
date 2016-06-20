from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.forms import *
from django.template import loader, RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response, get_list_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import *
from .form import *
from django.db import connection
from django.shortcuts import render, get_object_or_404, render_to_response, get_list_or_404
import csv


def homepage(request):
    return render(request, 'index.html')


def index(request):
    reldata = csv.reader(open('/root/Downloads/SOLO-MEDS.csv'), delimiter=';')
    for row in reldata:
        q = Medicamento(codigo_medicamento=row[0],nombre_medicamento=row[1])
        q.save()
    concen = csv.reader(open('/root/Downloads/CONCETRACIONES.csv'), delimiter=';')
    for row in concen:
        q = Concentracion(id=row[0], valor=row[1])
        q.save()
    medcon = csv.reader(open('/root/Downloads/Datos-Medicamentos.csv'), delimiter=';')
    for row in medcon:
        med = Medicamento.objects.get(codigo_medicamento=row[1])
        con = Concentracion.objects.get(id=row[2])
        p13 = row[3]
        p14 = row[4]
        p15 = row[5]
        f = Med_Concentracion(id=row[0], concentracion_id=con.id, medicamento_id=med.codigo_medicamento, precio13=p13, precio14=p14, precio15=p15)
        f.save()
    return render(request, 'index.html')


def consultaMedicamentos(request):
    with connection.cursor() as cursor:
        cursor.execute("Select codigo_medicamento, nombre_medicamento,valor, precio13, precio14, precio15 From variacionMedicamentos_medicamento Inner Join variacionMedicamentos_med_concentracion On codigo_medicamento = medicamento_id Inner Join variacionMedicamentos_concentracion On concentracion_id = variacionMedicamentos_concentracion.id")
        row = list(cursor)
    return render_to_response('medicamentos.html', {'medicamentos': row})

def consultarFarmacia(request):
    with connection.cursor() as cursor:
        cursor.execute("Select codigo_medicamento, nombre_medicamento, valor, precio15, nombre_farmacia, descuento From variacionMedicamentos_medicamento Inner Join variacionMedicamentos_med_concentracion On codigo_medicamento = medicamento_id Inner Join variacionMedicamentos_concentracion On concentracion_id = variacionMedicamentos_concentracion.id Inner Join variacionMedicamentos_sevende On variacionMedicamentos_sevende.medicamento_id = variacionMedicamentos_med_concentracion.id Inner Join variacionMedicamentos_farmacia On variacionMedicamentos_sevende.farmacia_id = variacionMedicamentos_farmacia.id")
        row = list(cursor)
        print(row)
    return render_to_response('farmacias.html', {'medicamentos': row})


@login_required
def add_medicamento(request):
    MedicamentoFormSet = modelformset_factory(Med_Concentracion, fields=( 'medicamento', 'concentracion', 'precio13', 'precio14', 'precio15'), can_delete=True)
    if request.method == 'POST':
        formset = MedicamentoFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("/meds/farmacias.html")
    else:
        formset = MedicamentoFormSet()
    return render(request, 'add_farmacia.html', {'formset': formset})

@login_required
def add_farmacia(request):
    FarmaciaFormSet = modelformset_factory(SeVende, fields=('medicamento', 'farmacia'), can_delete=True)
    if request.method == 'POST':
        formset = FarmaciaFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("/meds/variacionprecios")
    else:
        formset = FarmaciaFormSet()
    return render(request, 'add_farmacia.html', {'formset': formset})
