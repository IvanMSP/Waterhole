from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from django.utils.decorators  import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import Earning
from account.models import User
from .forms import EarningRegistrationForm

# Create your views here.


#Registro Ingresos
class RegistryEarning(View):
	def get(self,request):
		template_name = 'registry-earning.html'
		form_earning = EarningRegistrationForm()
		context = {
			'form_earning':form_earning,
		}
		print(form_earning)
		return render(request,template_name,context)




#Visualizar Ingresos
class ListEarning(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'list-earnings.html'
		earnigns = Earning.objects.all()
		context ={
			"earningactive":"active",
			'earnigns':earnigns,
		}
		print('ingresos',earnigns)
		return render(request,template_name,context)


