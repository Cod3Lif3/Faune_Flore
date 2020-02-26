from django.shortcuts import render
from .models import Sujet
from .form import ContactForm

def page_acceuil(request):
	sujet = Sujet.objects.filter(nom_commun__lte='rouan')
	return render(request,'acceuil/page_acceuil.html',{'sujet' : sujet})

def condition(request):
	return render(request,'acceuil/conditUtil.html')

def confident(request):
	return render(request,'acceuil/confidentiel.html')

def connection(request):
	return render(request,'acceuil/connection.html')

def listFaune(request):
	return render(request,'acceuil/listFaune.html')

def listFlore(request):
	return render(request,'acceuil/listFlore.html')

def cookies(request):
	return render(request,'acceuil/cookies.html')

def aPropos(request):
	return render(request,'acceuil/aPropos.html')

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		sujet = form.cleaned_data['sujet']
		message = form.cleaned_data['message']
		mail = form.cleaned_data['mail']
		renvoi = form.cleaned_data['renvoi']
		envoi = True
	return render(request,'acceuil/contacter.html',locals())
# Create your views here.
