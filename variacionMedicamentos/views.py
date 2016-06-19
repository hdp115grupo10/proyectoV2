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


def homepage(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def consultaMedicamentos(request):
    with connection.cursor() as cursor:
        cursor.execute("Select codigo_medicamento, nombre_medicamento,valor, precio13, precio14, precio15 From variacionMedicamentos_medicamento Inner Join variacionMedicamentos_med_concentracion On codigo_medicamento = medicamento_id Inner Join variacionMedicamentos_concentracion On concentracion_id = variacionMedicamentos_concentracion.id")
        row = list(cursor)
    return render_to_response('medicamentos.html', {'medicamentos': row})


def add_medicamento(request):
    MedicamentoFormSet = modelformset_factory(Med_Concentracion, fields=('concentracion', 'precio13', 'precio14', 'precio15'))
    if request.method == 'POST':
        formset = MedicamentoFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("/meds/variacionprecios")
    else:
        formset = MedicamentoFormSet()
    return render(request, 'add_medicamento.html', {'formset': formset})
