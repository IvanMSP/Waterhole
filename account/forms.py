from django import forms
from .models import User,ClientProfile,WaterHoleProfile,ContractModel,AdressModel
from django.forms.widgets import ClearableFileInput
from waterhole.models import WaterHole,ZoneModel



class UserRegistrationForm(forms.ModelForm):
	username = forms.CharField(label = "Nombre de Usuario*", widget = forms.TextInput(attrs = {'placeholder':"Usuario",}))
	email = forms.CharField(label = "Correo*", widget = forms.TextInput(attrs = {'placeholder':"Correo"}))
	first_name = forms.CharField(label="Nombre:*",widget=forms.TextInput(attrs={'placeholder':"Nombre", }))
	last_name = forms.CharField(label="Apellidos:*",widget=forms.TextInput(attrs={'placeholder':"Apellidos", }))
	#password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'placeholder':"Contraseña"}))
	#password2 = forms.CharField(label="Repita contraseña", widget=forms.PasswordInput(attrs={'placeholder':"Repita Contraseña"}))

	

	class Meta:
		model = User
		fields = ('username','email','first_name','last_name')
		help_texts = {'username':None,}

	def clean_password2(self):
		clean = self.cleaned_data
		if clean['password']!= clean['password2']:
			raise forms.ValidationError("Las contraseñas no coinciden")
		return clean['password2']

class UserEditForm(forms.ModelForm):
	username = forms.CharField(label = "Nombre de Usuario", widget = forms.TextInput(attrs = {'placeholder':"Usuario",}))
	email = forms.CharField(label = "Correo", widget = forms.TextInput(attrs = {'placeholder':"Correo"}))
	first_name = forms.CharField(label="Nombre:",widget=forms.TextInput(attrs={'placeholder':"Nombre", }))
	last_name = forms.CharField(label="Apellidos:",widget=forms.TextInput(attrs={'placeholder':"Apellidos", }))

	class Meta:
		model = User
		fields = ('username','email','first_name','last_name')
		help_texts = {
			'username':None,
		}


class MyClearebleFileInput(ClearableFileInput):
	initial_text = 'Actualmente'
	input_text = 'Cambiar foto de perfil'
	clear_checkbox_label = 'Limpiar'


#Formularios para clientes

class ClientRegistrationForm(forms.ModelForm):
	phone_number = forms.CharField(label="Numero celular:",widget=forms.TextInput(attrs={'placeholder':"Celular",}))
	photo_avatar = forms.ImageField(label="Foto del Cliente:", required=False, widget=MyClearebleFileInput)
	class Meta:
		model = ClientProfile
		fields =('phone_number','photo_avatar',)


class ClientRegistration(ClientRegistrationForm):
	waterhole_select = forms.ChoiceField(choices=[],widget=forms.TextInput(attrs={'readonly':'True'}))

	def __init__(self, *args, **kwargs):
		super(ClientRegistration,self).__init__(*args,**kwargs)
		self.fields['waterhole_select'] = forms.ChoiceField(label="Seleccionar Pozo de Agua:",choices=[(waterhole.id, waterhole.name) for waterhole in WaterHole.objects.all()])

	class Meta(ClientRegistrationForm.Meta):
		fields = ClientRegistrationForm.Meta.fields + ('waterhole_select',)

class ClientEditForm(forms.ModelForm):
	phone_number = forms.CharField(label="Numero celular:",widget=forms.TextInput(attrs={'placeholder':"Celular",}))
	photo_avatar = forms.ImageField(label="Foto del Cliente:", required=False, widget=MyClearebleFileInput)

	class Meta:
		model = ClientProfile
		fields = {'phone_number','photo_avatar'}



#Formularios para Administradores
class AdminEditForm(forms.ModelForm):
	photo_avatar = forms.ImageField(label="Foto del Administrador:", required=False, widget=MyClearebleFileInput)
	class Meta:
		model = WaterHoleProfile
		fields = ('phone_number','photo_avatar',)


#Formularios para contrato
class ContractForm(forms.ModelForm):
	ine_ide = forms.BooleanField(label="INE")
	free_copaci = forms.BooleanField(label = "Liberación de Copaci")
	formatt = forms.BooleanField(label = "Formato")
	permission_adress = forms.BooleanField(label = "Permiso para calle")
	cost = forms.DecimalField(label = "Costo:",widget =forms.TextInput(attrs={'placeholder':"0.00"}))
	
	
	class Meta:
		model = ContractModel
		fields = ('ine_ide','free_copaci','formatt','permission_adress','cost','zone_waterhole')
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['zone_waterhole'].queryset = ZoneModel.objects.all()
	
class ContractRegistration(ContractForm):
	zone_waterhole = forms.ChoiceField(choices=[],widget=forms.TextInput(attrs={'readonly':'True'}))

	def __init__(self, *args, **kwargs):
		super(ContractRegistration,self).__init__(*args,**kwargs)
		self.fields['zone_waterhole'] = forms.ChoiceField(label="Seleccionar Zona:",choices=[(zone.id,zone.name) for zone in ZoneModel.objects.all()])

	class Meta(ContractForm.Meta):
		fields = ContractForm.Meta.fields + ('zone_waterhole',)

class AdressForm(forms.ModelForm):
	street = forms.CharField(label="Calle/Avenida:",widget=forms.TextInput(attrs={'placeholder':"nombre de la calle",}))
	interior_number = forms.CharField(label="Número interior:",widget=forms.TextInput(attrs={'placeholder':"número interior de calle",}))
	ext_number = forms.CharField(label="Numero exterior:",widget=forms.TextInput(attrs={'placeholder':"número exterior",}))
	neighborhood = forms.CharField(label="Colonia:",widget=forms.TextInput(attrs={'placeholder':"colonia",}))
	cp = forms.CharField(label="Código Postal:",widget=forms.TextInput(attrs={'placeholder':"código Postal",}))
	delegation = forms.CharField(label="Municipio:",widget=forms.TextInput(attrs={'placeholder':"municipio",}))
	state = forms.CharField(label="Estado:",widget=forms.TextInput(attrs={'placeholder':"estado",}))
	class Meta:
		model = AdressModel
		fields = ('street','interior_number','ext_number','neighborhood','cp','delegation','state',)