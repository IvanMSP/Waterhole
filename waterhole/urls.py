from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^comite/$', views.ComitteView.as_view(), name='comitte'),	
]