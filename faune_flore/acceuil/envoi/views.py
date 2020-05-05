import csv,io
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Sujet
from .form import ContactForm
from .form import SujetForm
from .form import ConnexionForm
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Count

def page_acceuil(request):
	sujet = Sujet.objects.all().count()
	return render(request,'acceuil/page_acceuil.html',{'sujet' : sujet})

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
	sujet = Sujet.objects.all()
	paginate_by = 10
	return render(request,'acceuil/listFaune.html', {'sujet': sujet})

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

@login_required
def sujet_new(request,pk):
	if request.method == "POST":
		form = SujetForm(request.POST)
		if form.is_valid():
			sujet = form.save(commit=False)
			sujet.save()
			return redirect('sujet_detail',pk=sujet.pk)
	else:
		form = SujetForm()
	return	render(request,'acceuil/ajout.html',{'form': form})

def sujet_detail(request, pk):
	sujet = get_object_or_404(Sujet, pk=pk)
	return render(request, 'acceuil/sujet_detail.html', {'sujet': sujet})
# Create your views here.

def deconnexion(request):
	logout(request)
	return redirect(reverse(connection))

def sujet_edit(request,pk):
	sujet = get_object_or_404(Sujet, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			sujet = form.save(commit=False)
			sujet.published_date = timezone.now()
			sujet.save()
			return redirect('sujet_detail', pk=sujet.pk)
	else:
		form = SujetForm(instance=post)
	return render(request, 'acceuil/sujet_detail.html',{'form': form})

def sujet_upload(request):

	template = "acceuil/upload.html"
	sujet = Sujet.objects.all()
	with open('C:\\Users\\rouan\\OneDrive\\Bureau\\Projet\\Full_DNP_YE2.csv') as csvfile:
		spamreader = csv.reader(csvfile,delimiter=';')
		for column in spamreader:
			_, created = Sujet.objects.update_or_create(
        	    nom_commun=column[0]
            	)