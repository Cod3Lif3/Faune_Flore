from django.urls import path
from . import views


urlpatterns = [
	
	path('', views.accueil, name='accueil'),
	path('condition/',views.condition, name='condition'),
	path('confident/', views.confident, name='confident'),
	path('connexion/', views.connection, name='connection'),
	path('deconnexion/', views.deconnexion, name='deconnexion'),
	path('cookies/',views.cookies, name='cookies'),
	path('aPropos/',views.aPropos, name='aPropos'),
	path('contact/', views.contact, name='contact'),
	path('speciesList/',views.speciesList, name='speciesList'),
	path('plante/new/',views.plante_new, name='plante_new'),
	path('upload/', views.upload, name='upload'),
	path('species/<pk>/', views.species, name = 'species'),

	]
