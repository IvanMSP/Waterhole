from django import forms
from .models import Earning,OutflowsModel
from account.models import User
from account.models import WaterHoleProfile
import datetime


class EarningRegistrationForm(forms.ModelForm):
	subject = forms.CharField(label = "Concepto:",widget=forms.TextInput(attrs={'placeholder':"concepto",}))
	quantity = forms.DecimalField(label = "Costo:",widget=forms.TextInput(attrs={'placeholder':"costo",}))
	#admin_waterhole_earning = forms.ChoiceField(choices=[],widget=forms.TextInput(attrs={'readonly':'True',}))
	

	class Meta:
		model = Earning
		fields = ('subject','quantity')

class OutFlowRegistrationForm(forms.ModelForm):
	subject = forms.CharField(label = 'Concepto',widget = forms.TextInput(attrs = {'placeholder':"Concepto",}))
	quantity = forms.CharField(label = 'Cantidad',widget = forms.TextInput(attrs = {'placeholder':"Cantidad",}))

	class Meta:
		model = OutflowsModel
		fields = ('subject','quantity')

