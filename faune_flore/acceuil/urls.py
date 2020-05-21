from django.urls import path
from . import views


urlpatterns = [
	path('', views.accueil, name = 'accueil'),
	path('moleculesList/', views.moleculesList, name='moleculesList'),
	path('molecule/<pk>/', views.molecule, name='molecule'),
	path('upload/', views.upload, name = 'upload'),
	path('connexion/', views.connexion, name = 'connexion'),
	path('deconnexion/', views.deconnexion, name='deconnexion'),
	path('creation/', views.creation, name='creation')
	]
