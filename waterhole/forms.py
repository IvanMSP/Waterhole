from django import forms
from .models import Comitte

class ComitteRegistrationForm(forms.ModelForm):
    delegate = forms.CharField(label="Delegado:",widget=forms.TextInput(attrs={'placeholder':"Nombre del delegado",}))
    secretary = forms.CharField(label="Secretaria:",widget=forms.TextInput(attrs={'placeholder':"Nombre secretaria",}))
    class Meta:
        model = Comitte
        fields = ('delegate','secretary',)