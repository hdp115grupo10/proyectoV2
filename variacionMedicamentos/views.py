from django.http import HttpResponse, HttpResponseRedirect

from django.http import Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404, render_to_response, get_list_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import *
def homepage(request):
    return render(request, 'index.html')

@login_required
def index(request):
    return render(request, 'index.html')
def medicamentos(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'medicamentos.html', {'medicamentos':medicamentos})
