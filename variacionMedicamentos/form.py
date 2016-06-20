from django.forms import modelform_factory, modelformset_factory
from .models import *

#se hace uso del form factory de Django para crear forms para la administracion de  medicamentos y farmacias
MedicamentosForm = modelform_factory(Med_Concentracion, fields=("medicamento",))

FarmaciaForm = modelform_factory(SeVende, fields=("farmacia",))
