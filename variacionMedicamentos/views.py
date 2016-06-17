from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404, render_to_response, get_list_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import render, get_object_or_404, render_to_response, get_list_or_404

def homepage(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def medicamentos(request):
    medicamentos = Medicamento.objects.all()
    print medicamentos
    return render_to_response( 'medicamentos.html', {'medicamentos': medicamentos})
