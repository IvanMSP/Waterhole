from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from django.utils.decorators  import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegistrationForm,ClientRegistrationForm,ClientRegistration,UserEditForm,AdminEditForm,ClientEditForm
from waterhole.models import WaterHole
from .models import User,ClientProfile,WaterHoleProfile

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
			form_p = AdminBussinessRegistrationForm(instance = profile)
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
			print(context.profileclass)
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
		form_client = UserEditForm(instance = client)
		form_client_profile = ClientRegistration(instance = client_profile)
		context = {
			"mainclient":"active",
			'client':client,
			'client_profile':client_profile,
			'form_client':form_client,
			'form_client_profile':form_client_profile,
		}
		return render(request,template_name,context)

class RegistryClient(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'account/registry-client.html'
		form = UserRegistrationForm()
		form_client =ClientRegistration()
		context = {
			"mainclient":"active",
			'form':form,
			'form_client':form_client,
		}
		return render(request, template_name, context)


	def post(self,request):
		template_name = 'account/registry-client.html'
		form = UserRegistrationForm(request.POST)
		form_client = ClientRegistration(request.POST, request.FILES)
		if form.is_valid() and form_client.is_valid():
			new_user = form.save(commit=False)
			new_user.is_client=True
			new_user.save()

			new_profile = form_client.save(commit=False)
			new_client = form_client.cleaned_data
			waterhole = new_client['waterhole_select']
			new_profile.user_client = new_user
			waterhole = get_object_or_404(WaterHole, id = waterhole)

			print(waterhole)
			new_profile.waterhole_client = waterhole
			new_profile.save()

			messages.success(self.request, 'Cliente Registrado!')
			print(messages)

			return redirect('account:list-client')

		else:
			form = UserRegistrationForm()
			form_client = ClientRegistration()
			context ={
				"mainclient":"active",
				'form':form,
				'form_client': form_client,
			}
			messages.error(self.request,'Error de mensaje')
			print(messages)
			return render(request,template_name,context)


#Se tiene que borrar solo es de prueba ACUERDATE CABRON
class MainView(View):
	def get(self, request):
		template_name = 'registration/profile.html'
		context = {
			"dashboard":"active",
		}
		return render(request,template_name,context)