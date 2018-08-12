from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout,logout_then_login


urlpatterns = [
	url(r'^profile/$', views.ProfileView.as_view(), name = "profile"),
	url(r'^main/$', views.MainView.as_view(), name = "main"),
	#URLS the module clients
	url(r'^main-client/$', views.MainClient.as_view(), name = "main-client"),
	url(r'^registry-client/$', views.ClientRegistration.as_view(), name = "registry-client"),
	url(r'^login/$', login, name = "login"),
]