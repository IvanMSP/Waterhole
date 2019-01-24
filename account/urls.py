from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout,logout_then_login


urlpatterns = [
	url(r'^profile/$', views.ProfileView.as_view(), name = "profile"),
	#url(r'^main/$', views.MainView.as_view(), name = "main"),
	#URLS the module clients
	url(r'^list-client/$', views.ListClient.as_view(), name = "list-client"),
	url(r'^registry-client/$', views.RegistryClient.as_view(), name = "registry-client"),
	url(r'^detail-client/(?P<id_client>\d+)/(?P<username_client>[-\w]+)/$', views.DetailClient.as_view(), name = "detail-client"),
	#Urls login and logout
	url(r'^login/$', login, name = "login"),
	url(r'^logout-then-login/$', logout_then_login, name='logout-then-login'),

	#Pdf Urls
	url(r'^pdf-contract/pdf/(?P<id_client>\w+)/$', views.PdfSection.contract_pdf, name='pdf_contract'),
	url(r'^pdf-ticket/(?P<id_ticket>\d+)/(?P<id_client>\d+)/$', views.PdfSection.ticket_id_pdf, name='pdf_ticket_id'),
	
	#Url tickets
	url(r'^generate-ticket/(?P<id_client>\d+)/$', views.GenerateTicket.as_view(), name='generate_ticket'),

	#Url graphs
	url(r'^reports-graph/$', views.GraphView.as_view(), name='report'),
	
]