from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

# Asignacion de las url de la aplicacion

app_name = 'variacionMedicamentos'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^variacionprecios/$', views.consultaMedicamentos, name='medicamentos'),
    url(r'^add_med/$', views.add_medicamento, name='add_medicamento'),
    url(r'^preciofarmacias/$', views.consultarFarmacia, name='farmacias'),
    url(r'^add_farmacia/$', views.add_farmacia, name='add_farmacia'),
    url(r'^formula/$', views.formula, name='formula'),
]
