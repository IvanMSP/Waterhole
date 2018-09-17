from django import forms
from .models import User,ClientProfile,WaterHoleProfile
from django.forms.widgets import ClearableFileInput
from waterhole.models import WaterHole



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