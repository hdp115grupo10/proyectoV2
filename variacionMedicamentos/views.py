from django.http import HttpResponseRedirect
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
from django.shortcuts import render, get_object_or_404, render_to_response
import csv
import os

# Creacion de vistas


# Se Define el Inicio de la pagina
def index(request):
    # Se leen los archivos csv y los guarda en la base
    dr = os.path.abspath('variacionMedicamentos')  # Se obtiene la direccion de la carpeta variacionMedicamentos
    path = os.path.join(dr, "SOLO-MEDS.csv")  # Se une la direccion de la carpeta con el nombre del archivo que queremos
    reldata = csv.reader(open(path), delimiter=';')  # Se lee el csv
    for row in reldata:
        # Por cada fila de lo que se leyo en el csv se crea un objeto Medicamento y lo guarda
        q = Medicamento(codigo_medicamento=row[0],nombre_medicamento=row[1])
        q.save()
    path = os.path.join(dr, "CONCETRACIONES.csv")  # Se une la direccion de la carpeta con el nombre del archivo que queremos
    concen = csv.reader(open(path), delimiter=';')  # Se lee el csv
    for row in concen:
        # Por cada fila de lo que se leyo en el csv se crea un objeto Concentracion y lo guarda
        q = Concentracion(id=row[0], valor=row[1])
        q.save()
    path = os.path.join(dr, "Datos-Medicamentos.csv")  # Se une la direccion de la carpeta con el nombre del archivo que queremos
    medcon = csv.reader(open(path), delimiter=';') # Se lee el csv
    for row in medcon:
        # Por cada fila de lo que se leyo en el csv se crea un objeto Med_Concentracion y lo guarda
        med = Medicamento.objects.get(codigo_medicamento=row[1])
        con = Concentracion.objects.get(id=row[2])
        p13 = row[3]
        p14 = row[4]
        p15 = row[5]
        f = Med_Concentracion(id=row[0], concentracion_id=con.id, medicamento_id=med.codigo_medicamento, precio13=p13, precio14=p14, precio15=p15)
        f.save()
    return render(request, 'index.html') #muestra el index


def consultaMedicamentos(request):   # Definicion de la consulta de medicamentos y sus concentraciones con sus precios por anio
    # Se usa un cursor para conetarse a la base de datos
    with connection.cursor() as cursor:  # se usa el cursor y al final lo cierra
        # Se ejecuta la consulta explicita
        cursor.execute("Select codigo_medicamento, nombre_medicamento,valor, precio13, precio14, precio15 From variacionMedicamentos_medicamento Inner Join variacionMedicamentos_med_concentracion On codigo_medicamento = medicamento_id Inner Join variacionMedicamentos_concentracion On concentracion_id = variacionMedicamentos_concentracion.id")
        row = list(cursor)  #se pasan los resultados a una lista
    return render_to_response('medicamentos.html', {'medicamentos': row})  # se mandan los datos para ser renderizados

def consultarFarmacia(request):  # Definicion de la consulta de farmcias y medicamentos
    # Se usa un cursor para conetarse a la base de datos
    with connection.cursor() as cursor:  # se usa el cursor y al final lo cierra
        # Se ejecuta la consulta explicita
        cursor.execute("Select codigo_medicamento, nombre_medicamento, valor, precio15, nombre_farmacia, descuento From variacionMedicamentos_medicamento Inner Join variacionMedicamentos_med_concentracion On codigo_medicamento = medicamento_id Inner Join variacionMedicamentos_concentracion On concentracion_id = variacionMedicamentos_concentracion.id Inner Join variacionMedicamentos_sevende On variacionMedicamentos_sevende.medicamento_id = variacionMedicamentos_med_concentracion.id Inner Join variacionMedicamentos_farmacia On variacionMedicamentos_sevende.farmacia_id = variacionMedicamentos_farmacia.id")
        row = list(cursor)
    return render_to_response('farmacias.html', {'medicamentos': row})  # se mandan los datos para ser renderizados


@login_required
def add_medicamento(request):  # Se define la vista de agregar medicamento (BETA)
    # se usa el modelformset_factory de Django para generar el formulario y se define el modelo a usar y los campos
    MedicamentoFormSet = modelformset_factory(Med_Concentracion, fields=('medicamento', 'concentracion', 'precio13', 'precio14', 'precio15'), can_delete=True)
    if request.method == 'POST':
        formset = MedicamentoFormSet(request.POST, request.FILES)  # se cargan los datos al formset
        if formset.is_valid():  # Si es valido se guarda y nos redirije a la pagina de los medicamento
            formset.save()
            return HttpResponseRedirect("/meds/variacionprecios")
    else:
        formset = MedicamentoFormSet()
    return render(request, 'add_medicamento.html', {'formset': formset})

@login_required
def add_farmacia(request):  # Se define la vista de agregar farmacia (BETA)
    # se usa el modelformset_factory de Django para generar el formulario y se define el modelo a usar y los campos
    FarmaciaFormSet = modelformset_factory(SeVende, fields=('medicamento', 'farmacia'), can_delete=True)
    if request.method == 'POST':
        formset = FarmaciaFormSet(request.POST, request.FILES) # se cargan los datos al formset
        if formset.is_valid():  # Si es valido se guarda y nos redirije a la pagina de los farmacias
            formset.save()
            return HttpResponseRedirect("/meds/farmacias")
    else:
        formset = FarmaciaFormSet()
    return render(request, 'add_farmacia.html', {'formset': formset})
