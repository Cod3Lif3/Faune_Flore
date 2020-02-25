from django.shortcuts import render
from .models import Sujet

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

def contacter(request):
	return render(request,'acceuil/contacter.html')
# Create your views here.
