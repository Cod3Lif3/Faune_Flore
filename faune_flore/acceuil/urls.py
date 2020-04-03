from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.page_acceuil, name='page_acceuil'),
	path('condition/',views.condition, name='condition'),
	path('confident/', views.confident, name='confident'),
	path('connexion/', views.connection, name='connection'),
	path('listFaune/', views.listFaune, name='listFaune'),
	path('listFlore/', views.listFlore, name='listFlore'),
	path('cookies/',views.cookies, name='cookies'),
	path('aPropos/',views.aPropos, name='aPropos'),
	path('contact/', views.contact, name='contact'),
	path('sujet/new/',views.sujet_new, name='sujet_new'),
	path('post/<pk>/', views.sujet_detail, name='sujet_detail'),
	path('deconnexion/', views.deconnexion, name='deconnexion'),
	path('post/<pk>/edit/', views.sujet_new, name='sujet_edit'),

	]
