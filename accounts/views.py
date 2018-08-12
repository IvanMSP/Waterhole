from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from django.utils.decorators  import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm,ClientRegistrationForm,ClientRegistration
from waterhole.models import WaterHole
from .models import ClientProfile


class ProfileView(View):
	@method_decorator(login_required)
	def get(self,request):
		profile = None
		#form_u = UserEditForm(instance = request.user)
		form_p = None
		template_name = "registration/profile.html"
		user = request.user
		if user.is_admin_waterhole:
			profile = user.get_adminwaterhole_profile()
			#form_p = AdminBussinessEditForm(instance = profile)
			

		elif user.is_client:
			profile = user.get_client_profile()
			form_p = ClientEditForm(instance = profile)
			
		else:
			profile = user.get_adminsystem_profile()
			form_p = AdminBussinessRegistrationForm(instance = profile)
		context = {
			'user':user,
			'profile':profile,
			'form_u': form_u,
			'form_p':form_p,
		}
		return render(request,template_name,context)


#VIEWS PARA MODULO DE CLIENTS
class MainClient(View):
	def get(self,request):
		template_name = 'account/main-client.html'
		context = {
			"mainclient":"active",
		}
		print(context)
		return render(request,template_name,context)

class ClientRegistration(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'account/registry-client.html'
		form = UserRegistrationForm()
		form_client =ClientRegistration()
		print(form_client)
		context = {
			"mainclient":"active",
			'form':form,
			'form_client':form_client,
		}
		return render(request, template_name, context)


	# def post(self,request):
	# 	template_name = 'account/registry-client.html'
	# 	form = UserRegistrationForm(request.POST)
	# 	form_client = ClientRegistration(request.POST, request.FILES)
	# 	if form.is_valid() and form_client.is_valid():
	# 		new_user = form.save(commit=False)
	# 		new_user.is_client=True
	# 		new_user.save()

	# 		new_profile = form_client.save(commit=False)
	# 		client = form_client.cleaned_data
	# 		waterhole = client['waterhole_select']
	# 		new_profile.user_client = new_user
	# 		waterhole = get_object_or_404(WaterHole, id = waterhole)
	# 		new_profile.save()
	# 		new_profile.waterhole_client.add(waterhole)
	# 		new_profile.save()
	# 		return redirect('account:main')
	# 	else:
	# 		form = UserRegistrationForm()
	# 		form_client = ClientRegistrationForm()
	# 		context ={
	# 			'form':form,
	# 			'form_client': form_client,
	# 		}
	# 		return render(request,template_name,context)


#Se tiene que borrar solo es de prueba ACUERDATE CABRON
class MainView(View):
	def get(self, request):
		template_name = 'registration/profile.html'
		context = {
			"dashboard":"active",
		}
		return render(request,template_name,context)