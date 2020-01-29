from django.shortcuts import render

def page_acceuil(request):
	return render(request,'acceuil/page_acceuil.html',{})

# Create your views here.
