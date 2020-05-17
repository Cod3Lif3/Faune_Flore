from django import forms
from .models import Species

class ContactForm(forms.Form):
	sujet = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	mail = forms.EmailField(label="Votre adresse e-mail")
	renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé.",required=False)

class PlanteForm(forms.ModelForm):

	class Meta:
		model = Species
		fields = ('speciesName','moleculeName')
		
class ConnexionForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur", max_length=30)
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)