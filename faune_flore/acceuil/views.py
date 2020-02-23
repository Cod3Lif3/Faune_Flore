from django.shortcuts import render
from .models import Sujet

def page_acceuil(request):
	sujet = Sujet.objects.filter(nom_commun__lte='rouan')
	return render(request,'acceuil/page_acceuil.html',{'sujet' : sujet})

def condition(request):
	return render(request,'acceuil/conditUtil.html')


# Create your views here.
