from django import forms
from .models import Molecule
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.Form):
	sujet = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	mail = forms.EmailField(label="Votre adresse e-mail")
	renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.",required=False)

class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["username", "email", "password1","password2"]

class NewMolForm(forms.ModelForm):
	class Meta:
		model = Molecule
		fields = ["InChIKey","moleculeName","moleculeFormula","crcNumber","speciesName","molFileName","accurateMass","casNumber","compoundType","opticalRotation"]
		


	