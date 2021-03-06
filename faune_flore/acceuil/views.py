import csv,io
from django.db import models
from .models import Molecule
from .form import NewMolForm
from .form import ContactForm
from .form import RegisterForm
from django.utils import timezone
from django.db.models import Count
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.decorators import login_required


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

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = RegisterForm()

   

    return render(response, "registration/register.html", {"form" : form})

def search(request):
    query = request.GET['query']
    molecules = Molecule.objects.filter(moleculeName__icontains=query)
    paginator = Paginator(molecules, 50)
    return render(request, 'acceuil/moleculesList.html', {'molecules' : molecules})

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        mail = form.cleaned_data['mail']
        renvoi = form.cleaned_data['renvoi']
        envoi = True
        return redirect('/')
    else :
        form = ContactForm()
    return render(request,'acceuil/contacter.html',locals())


def new_molecule(request):
    if request.method == "POST":
        form = NewMolForm(request.POST)
        if form.is_valid():
            molecules = form.save(commit = False)
            molecules.published_date = timezone.now()
            molecules.save()
            return redirect('molecule', pk = molecules.pk)
    else:
        form = NewMolForm()
    return render(request, 'acceuil/ajout.html', {'form' : form})


def edit_molecule(request, pk):
    molecules = get_object_or_404(Molecule, pk=pk)
    if request.method == "POST":
        form = NewMolForm(request.POST, instance=molecules)
        if form.is_valid():
            molecules = form.save(commit = False)
            molecules.published_date = timezone.now()
            molecules.save()  
            return redirect('molecule', pk = molecules.pk)
    else:
        form = NewMolForm(instance=molecules)
    return render(request, 'acceuil/ajout.html', {'form' : form})


def aPropos(request):
    return render(request, 'acceuil/aPropos.html')

