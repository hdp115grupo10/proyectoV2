from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader, RequestContext
from django.shortcuts import render, get_object_or_404, render_to_response, get_list_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import *
from .form import *
from django.db import connection
from django.shortcuts import render, get_object_or_404, render_to_response, get_list_or_404


def homepage(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def consultaMedicamentos(request):
    with connection.cursor() as cursor:
        cursor.execute("Select codigo_medicamento, nombre_medicamento, valor, anio, precio\
                       From variacionMedicamentos_medicamento\
                       Inner Join variacionMedicamentos_med_concentracion On codigo_medicamento = medicamento_id\
                       Inner Join variacionMedicamentos_concentracion On concentracion_id = variacionMedicamentos_concentracion.id\
                       Inner Join variacionMedicamentos_precio_anios On variacionMedicamentos_precio_anios.medicamento_id = variacionMedicamentos_med_concentracion.id\
                       Inner Join variacionMedicamentos_anios On variacionMedicamentos_anios.id = variacionMedicamentos_precio_anios.anio_id")
        row = list(cursor)
    return render_to_response('medicamentos.html', {'medicamentos': row})


def add_medicamento(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = MedicamentosForm(request.POST)
        if form.is_valid():
                    form.save(commit=True)
                    return index(request)
        else:
            print form.errors
    else:
        form = MedicamentosForm()
    return render_to_response('add_medicamento.html', {'form': form}, context)
