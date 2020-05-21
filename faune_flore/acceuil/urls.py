from django.urls import path
from . import views



urlpatterns = [
	path('', views.accueil, name = 'accueil'),
	path('moleculesList/', views.moleculesList, name='moleculesList'),
	path('molecule/<pk>/', views.molecule, name='molecule'),
	path('upload/', views.upload, name = 'upload'),
	path('register/', views.register, name='register'),
	path('search/', views.search)
	
	]
