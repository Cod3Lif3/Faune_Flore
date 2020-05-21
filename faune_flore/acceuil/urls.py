from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


urlpatterns = [
	path('', views.accueil, name = 'accueil'),
	path('moleculesList/', views.moleculesList, name='moleculesList'),
	path('molecule/<pk>/', views.molecule, name='molecule'),
	path('upload/', views.upload, name = 'upload'),
	
	]
