from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from django.utils.decorators  import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import pdb

from .forms import (UserRegistrationForm,ClientRegistrationForm,ClientRegistration,
					UserEditForm,AdminEditForm,ClientEditForm,ContractForm,ContractRegistration,AdressForm)
from waterhole.models import WaterHole
from .models import User,ClientProfile,WaterHoleProfile,ContractModel,AdressModel
from waterhole.models import ZoneModel
from finanzas.models import Earning
# Codigó para utilizar weasy print
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
# Codigó para utilizar weasy print

#Vista para los perfiles
class ProfileView(View):
	@method_decorator(login_required)
	def get(self,request):
		profile = None
		form_u = UserEditForm(instance = request.user)
		form_p = None
		template_name = "registration/profile.html"
		user = request.user
		if user.is_admin_waterhole:
			profile = user.get_adminwaterhole_profile()
			form_p = AdminEditForm(instance = profile)
		elif user.is_client:
			profile = user.get_client_profile()
			form_p = ClientEditForm(instance = profile)
			
		else:
			profile = user.get_adminsystem_profile()
			form_p = AdminEditForm(instance = profile)
		context = {
			"profileclass":"active",
			'user':user,
			'profile':profile,
			'form_u': form_u,
			'form_p':form_p,
		}

		return render(request,template_name,context)

	def post(self,request):
		template_name = 'registration/profile.html'
		user = request.user
		form_u = UserEditForm(instance = request.user, data = request.POST)
		profile = None
		form_p = None
		if user.is_admin_waterhole:
			profile = user.get_adminwaterhole_profile()
			form_p = AdminEditForm(instance = profile, data= request.POST,files = request.FILES)
		else:
			profile = user.get_client_profile()
			form_p = ClientEditForm(instance = profile, data = request.POST, files = request.FILES)
		if form_u.is_valid() and form_p.is_valid():
			form_u.save()
			form_p.save()
			messages.success(self.request, 'Perfil Actualizado correctamente!')
			return redirect('account:profile')
		else:
			context = {
				"profileclass":"active",
				'user':user,
				'profile':profile,
				'form_u': form_u,
				'form_p':form_p,
			}
			
		return render(request,template_name,context)


#VIEWS PARA MODULO DE CLIENTS
class ListClient(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'account/list-client.html'
		user = request.user
		great = False
		admin_waterhole = None
		if user.is_admin_waterhole:
			great = True
			admin_waterhole= user.get_adminwaterhole_profile()
		context = {
			'great':great,
			'admin_waterhole':admin_waterhole,
			"mainclient":"active",
		}
		
		return render(request,template_name,context)

class DetailClient(View):
	@method_decorator(login_required)
	def get(self,request,id_client,username_client):
		template_name = 'account/detail-client.html'
		client = get_object_or_404(User, id = id_client, username = username_client)
		client_profile = client.get_client_profile()
		contract = ContractModel.objects.get(user_profile = client_profile)
		adress = AdressModel.objects.get(contract = contract)
		form_client = UserEditForm(instance = client)
		form_client_profile = ClientRegistrationForm(instance = client_profile)
		form_adress = AdressForm(instance = adress)
		context = {
			"mainclient":"active",
			'client':client,
			'client_profile':client_profile,
			'form_client':form_client,
			'form_client_profile':form_client_profile,
			'form_adress':form_adress,
			'contract':contract,
			'adress':adress,
		}
		return render(request,template_name,context)

class RegistryClient(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'account/registry-client.html'
		form = UserRegistrationForm()
		form_client = ClientRegistrationForm()
		form_adress = AdressForm()
		form_contract = ContractForm()
		user = request.user
		admin_waterhole = user.get_adminwaterhole_profile()
		print(admin_waterhole)
		context = {
			"mainclient":"active",
			'form':form,
			'form_client':form_client,
			'form_contract':form_contract,
			'form_adress':form_adress,
		}
		return render(request, template_name, context)

	#Validar username y mandar ntificacion
	def post(self,request):
		template_name = 'account/registry-client.html'
		form = UserRegistrationForm(request.POST)
		form_client = ClientRegistrationForm(request.POST, request.FILES)
		form_adress = AdressForm(request.POST,request.FILES)
		form_contract = ContractForm(data = request.POST)
		user = request.user
		admin_waterhole = user.get_adminwaterhole_profile()
		waterhole = admin_waterhole.waterhole_admin
		
		if form.is_valid() and form_client.is_valid() and form_contract.is_valid() and form_adress.is_valid():
			#Guardamos el usuario del cliente
			
			new_user = form.save(commit=False)
			new_user.is_client=True
			new_user.save()
			

			#guardamos el perfil del cliente 
			new_profile = form_client.save(commit = False)
			new_profile.user_client = new_user
			new_profile.waterhole_client = waterhole
			new_profile.save()
			print(new_profile)

			#Guardamos contrato
			new_contract = form_contract.save(commit = False)
			# #Guardamos la zona
			new_contract.waterhole_admin = waterhole
			new_contract.user_profile = new_profile
			
			#print(zone)
			new_contract.save()
			

			new_adress = form_adress.save(commit=False)
			new_adress.contract = new_contract
			new_adress.save()

			new_earnig = Earning()
			new_earnig.admin_waterhole_earning = admin_waterhole
			new_earnig.subject = new_contract
			new_earnig.quantity = new_contract.cost
			new_earnig.save()
			# new_profile = form_client.save(commit=False)
			# new_client = form_client.cleaned_data
			# waterhole = new_client['waterhole_select']
			# new_profile.user_client = new_user
			# waterhole = get_object_or_404(WaterHole, id = waterhole)

			# print(waterhole)
			# new_profile.waterhole_client = waterhole
			# new_profile.save()

			messages.success(self.request, 'Cliente Registrado satisfactoriamente.')
			

			return redirect('account:detail-client', new_user.id , new_user.username)

		else:
			form = UserRegistrationForm()
			form_client = ClientRegistrationForm()
			form_adress = AdressForm()
			form_contract = ContractForm()
			
			context ={
				"mainclient":"active",
				'form':form,
				'form_client': form_client,
				'form_adress':form_adress,
				'form_contract':form_contract,
			}
			return render(request,template_name,context)


#Se tiene que borrar solo es de prueba ACUERDATE CABRON
class MainView(View):
	def get(self, request):
		template_name = 'registration/profile.html'
		context = {
			"dashboard":"active",
		}
		return render(request,template_name,context)


##PDF SECTION#######################################################
class PdfSection(object):
	def contract_pdf(request, id_client):
		user  = request.user
		admin = user.get_adminwaterhole_profile()
		waterhole = admin.waterhole_admin
		client_profile = get_object_or_404(ClientProfile, id = id_client)
		contract = get_object_or_404(ContractModel, user_profile = client_profile )
		adress = get_object_or_404(AdressModel, contract = contract)
		html = render_to_string('pdfs/contract_pdf.html', {'client_profile':client_profile,'contract':contract,'waterhole':waterhole,'adress':adress,})
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'inline;filename="Contrato_pozo_cozotlan.pdf"'
		weasyprint.HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + '/css/pdf.css')])
		return response
