from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout,logout_then_login


urlpatterns = [
	url(r'^profile/$', views.ProfileView.as_view(), name = "profile"),
	url(r'^main/$', views.MainView.as_view(), name = "main"),
	url(r'^login/$', login, name = "login"),
]