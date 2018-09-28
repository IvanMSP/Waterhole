from django import forms
from .models import Earning
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

	# def __init__(self,current_user,*args,**kwargs):
	# 	super(EarningRegistrationForm,self).__init__(*args,**kwargs)
	# 	self.fields['admin_waterhole_earning'].queryset = self.fields['admin_waterhole_earning'].queryset.filter(user_admin_waterhole_id = current_user.id)

# class EarningRegistration(EarningRegistrationForm):
# 	admin_select = forms.ChoiceField(choices=[],widget=forms.TextInput(attrs={'readonly':'True'}))

# 	def __init__(self, *args, **kwargs):
# 		super(EarningRegistration,self).__init__(*args,**kwargs)
# 		self.fields['admin_select'] = forms.ChoiceField(label="Administrador:",choices=[(admin.id,admin.username) for admin in User.objects.all()])

# 	class Meta(EarningRegistrationForm.Meta):
# 		fields = EarningRegistrationForm.Meta.fields + ('admin_select',)

