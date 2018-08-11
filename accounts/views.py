from django.shortcuts import render,redirect
from django.views.generic import View
from django.utils.decorators  import method_decorator
from django.contrib.auth.decorators import login_required


class ProfileView(View):
	@method_decorator(login_required)
	def get(self,request):
		profile = None
		#form_u = UserEditForm(instance = request.user)
		form_p = None
		template_name = "registration/profile.html"
		user = request.user
		if user.is_admin_bussiness:
			profile = user.get_adminbussiness_profile()
			form_p = AdminBussinessEditForm(instance = profile)
			

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

class MainView(View):
	def get(self, request):
		template_name = 'registration/profile.html'
		return render(request,template_name)