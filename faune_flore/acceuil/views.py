import csv,io
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Species 
from .form import ContactForm
from .form import PlanteForm
from .form import ConnexionForm
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Count
from django.db import models
from django.core.paginator import Paginator

def accueil(request):
    species = Species.objects.all().count()
    return render(request, 'acceuil/accueil.html',{'species' : species})

def condition(request):
	return render(request,'acceuil/conditUtil.html')

def confident(request):
	return render(request,'acceuil/confidentiel.html')

def cookies(request):
	return render(request,'acceuil/cookies.html')

def aPropos(request):
	return render(request,'acceuil/aPropos.html')

def connection(request):
	error = False

	if request.method == "POST":
		form = ConnexionForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)
			if user:
				login(request, user)
				return render(request,'acceuil/page_acceuil.html')
			else:
				error=True
		else:
			form=ConnexionForm()
	return render(request,'acceuil/connection.html', locals())

def speciesList(request):
    species_list = Species.objects.all()
    paginator = Paginator(species_list, 50)

    page = request.GET.get('page')
    species = paginator.get_page(page)
    return render(request, 'acceuil/speciesList.html',{'species' : species})


def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		sujet = form.cleaned_data['sujet']
		message = form.cleaned_data['message']
		mail = form.cleaned_data['mail']
		renvoi = form.cleaned_data['renvoi']
		envoi = True
	return render(request,'acceuil/contacter.html',locals())

@login_required
def plante_new(request,pk):
	if request.method == "POST":
		form = PlanteForm(request.POST)
		if form.is_valid():
			species = form.save(commit=False)
			species.save()
			return redirect('species',pk=species.pk)
	else:
		form = PlanteForm()
	return	render(request,'acceuil/ajout.html',{'form': form})


def species(request, pk):
    species = get_object_or_404(Species , pk=pk)
    return render(request, 'acceuil/species.html',{'species': species})

def deconnexion(request):
	logout(request)
	return redirect(reverse(connection))



def upload(request):
    template = "acceuil/upload.html"
    species = Species.objects.all()
    with open('C:\\Users\\rouan\\OneDrive\\Bureau\\Projet\\csv_molecule2.csv') as csvfile:
        spamreader = csv.reader(csvfile,delimiter=';')
        for column in spamreader:
            _, created = Species.objects.update_or_create(
               speciesName = column[9],
                moleculeName = column[3]
            	)
    return render(request, template,{})