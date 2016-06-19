from django.forms import modelform_factory, modelformset_factory
from .models import *

MedicamentosForm = modelform_factory(Med_Concentracion, fields=("medicamento",))
