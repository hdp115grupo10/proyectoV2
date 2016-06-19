from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'variacionMedicamentos'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^variacionprecios/$', views.consultaMedicamentos, name='medicamentos'),
    url(r'^add_med/$', views.add_medicamento, name='add_medicamento'),
    url(r'^preciofarmacias/$', views.consultarFarmacia, name='farmacias'),
]
