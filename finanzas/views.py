from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from django.utils.decorators  import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import Earning,OutflowsModel
from account.models import User,WaterHoleProfile
from .forms import EarningRegistrationForm,OutFlowRegistrationForm
import pdb
from decimal import Decimal
from django.db.models import Sum
# Create your views here.


#Registro Ingresos
class RegistryEarning(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'registry-earning.html'
		form_earning = EarningRegistrationForm()
		context = {
			"earningactive":"active",
			'form_earning':form_earning,
		}
		
		return render(request,template_name,context)
	def post(self,request):
		template_name = 'registry-earning.html'
		form_earning = EarningRegistrationForm(request.POST)
		user = request.user
		admin = user.get_adminwaterhole_profile()
	
		if form_earning.is_valid():
			new_earning = form_earning.save(commit = False)
			new_earning.admin_waterhole_earning = admin
			new_earning.save()
			messages.success(self.request,'Ingreso registrado')
			return redirect('finance:ingresos')
		
		else:
			form_earning = EarningRegistrationForm()
			context={
				'form_earning':form_earning,
			}
			return render(request,template_name,context)

#Visualizar Ingresos
class ListEarning(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'list-earnings.html'
		earnigns = Earning.objects.all()
		total = Earning.objects.aggregate(total=Sum('quantity'))['total']
		context ={
			"earningactive":"active",
			'earnigns':earnigns,
			'total':total,
		}
		print('ingresos',earnigns)
		return render(request,template_name,context)

#Visualizar Egresos
class ListOutflow(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'list_outflows.html'
		outflows = OutflowsModel.objects.all()
		total = OutflowsModel.objects.aggregate(total=Sum('quantity'))['total']
		context ={
			"outflow":"active",
			'outflows':outflows,
			'total':total,
		}
		return render(request,template_name,context)

class RegistryOutFlow(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'registry_outflow.html'
		form_outflow = OutFlowRegistrationForm()
		context = {
			"outflow":"active",
			'form_outflow':form_outflow,
		}
		return render(request,template_name,context)
	
	def post(self,request):
		template_name = 'registry_outflow.html'
		form_outflow = OutFlowRegistrationForm(request.POST)
		user = request.user
		admin = user.get_adminwaterhole_profile()
		if form_outflow.is_valid():
			new_outflow= form_outflow.save(commit = False)
			new_outflow.admin_waterhole_outflow = admin
			new_outflow.save()
			messages.success(self.request,'Egreso registrado')
			return redirect('finance:egresos')
		
		else:
			form_outflow = OutFlowRegistrationForm()
			context={
				'form_outflow':form_outflow,
			}
			return render(request,template_name,context)

