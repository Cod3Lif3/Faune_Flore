import csv,io
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Molecule
from .form import ContactForm
from .form import PlanteForm
from .form import ConnexionForm
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Count
from django.db import models
from django.contrib.auth.models import User
from django.core.paginator import Paginator

def accueil(request):
    molecules = Molecule.objects.all().count()
    return render(request, 'acceuil/accueil.html', {'molecules' : molecules})

def moleculesList(request):
    molecule_list = Molecule.objects.all()
    paginator = Paginator(molecule_list, 50)

    page = request.GET.get('page')
    molecules = paginator.get_page(page)
    return render(request, 'acceuil/moleculesList.html', {'molecules' : molecules})

def molecule(request, pk):
    molecules = get_object_or_404(Molecule, pk = pk)
    return render(request, 'acceuil/molecule.html', {'molecules' : molecules})

def connexion(request):
    error = False
    
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username = username, password=password)
            if user :
                login(request, user)
                return render(request, 'acceuil/accueil.html')
            else :
                error = True
        else :
            form=ConnexionForm()
    return render(request, 'acceuil/connection.html',locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

def upload(request):
    template = "acceuil/upload.html"
    molecule = Molecule.objects.all()
    with open('C:\\Users\\rouan\\OneDrive\\Bureau\\Projet\\csv_molecule2.csv') as csvfile:
        spamreader = csv.reader(csvfile,delimiter=';')
        for column in spamreader:
            _, created = Molecule.objects.update_or_create(
        	InChIKey = column[1],
                moleculeName = column[3],
                moleculeFormula =column[4],
                crcNumber = column[2],
                molFileName = column[0],
                accurateMass = column[6],
                casNumber = column[7],
                compoundType = column[8],
                opticalRotation = column[10],
                speciesName = column[9]
            	)
    return render(request, template,{})