import csv,io
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Plante
from .form import ContactForm
from .form import PlanteForm
from .form import ConnexionForm
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Count
from django.db import models
from django.core.paginator import Paginator

def page_acceuil(request):
	
	plante = Plante.objects.all().count()
	return render(request,'acceuil/page_acceuil.html',{'plante' : plante})

def condition(request):
	return render(request,'acceuil/conditUtil.html')

def confident(request):
	return render(request,'acceuil/confidentiel.html')

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

def listFaune(request):
	paginate_by = 10
	return render(request,'acceuil/listFaune.html')

def listFlore(request):
	plante_list = Plante.objects.all()
	paginator = Paginator(plante_list,10)
	page = request.GET.get('page')
	plante = paginator.get_page(page)
	return render(request,'acceuil/listFlore.html', {'plante' : plante})

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

@login_required
def plante_new(request,pk):
	if request.method == "POST":
		form = PlanteForm(request.POST)
		if form.is_valid():
			plante = form.save(commit=False)
			plante.save()
			return redirect('plante_detail',pk=plante.pk)
	else:
		form = PlanteForm()
	return	render(request,'acceuil/ajout.html',{'form': form})


def plante_detail(request, pk):
	plante = get_object_or_404(Plante, pk=pk)
	return render(request, 'acceuil/plante_detail.html', {'plante' : plante})
# Create your views here.

def deconnexion(request):
	logout(request)
	return redirect(reverse(connection))


def sujet_upload(request):

	template = "acceuil/upload.html"
	plante = Plante.objects.all()
	with open('C:\\Users\\rouan\\OneDrive\\Bureau\\Projet\\csv_molecule2.csv') as csvfile:
		spamreader = csv.reader(csvfile,delimiter=';')
		for column in spamreader:
			_, created = Plante.objects.update_or_create(
        	    InChIKey = column[1],
        	    nom=column[9],
        	    molecule_name = column[3]
            	)