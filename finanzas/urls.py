from django.conf.urls import url
from . import views



urlpatterns = [
	url(r'^ingresos/$', views.ListEarning.as_view(), name = "ingresos"),
	url(r'^registro-ingresos/$', views.RegistryEarning.as_view(), name = "registry-earning"),
]