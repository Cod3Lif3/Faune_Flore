from django.shortcuts import render
from .models import Sujet

def page_acceuil(request):
	sujet = Sujet.objects.filter(nom_commun__lte='rouan')
	return render(request,'acceuil/page_acceuil.html',{'sujet' : sujet})


# Create your views here.
