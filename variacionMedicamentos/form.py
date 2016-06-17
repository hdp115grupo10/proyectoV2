from django import forms
from .models import *
class MedicamentosForm(forms.Form):
	"""docstring for MedicamentosForm"""
	codigo_medicamento=forms.CharField(max_length=7)
	nombre_medicamento=forms.CharField(max_length=50)
	concentraciones=forms.ModelMultipleChoiceField(queryset=Med_Concentracion.objects.all())

class ConcentracionesForm(forms.Form):
	medicamento=forms.ModelChoiceField(queryset=Medicamento.objects.all())
	concentracion=forms.ModelChoiceField(queryset=Concentracion.objects.all())