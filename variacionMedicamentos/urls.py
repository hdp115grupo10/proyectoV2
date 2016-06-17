from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name='variacionMedicamentos'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^variacionprecios/$', views.medicamentos, name='medicamentos'),
]
