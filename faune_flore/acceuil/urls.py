from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.page_acceuil, name='page_acceuil'),
	path('condition/',views.condition, name='condition'),
	path('confident/', views.confident, name='confident'),
	path('connection/', views.connection, name='connection'),
	path('listFaune/', views.listFaune, name='listFaune'),
	path('listFlore/', views.listFlore, name='listFlore'),
	path('cookies/',views.cookies, name='cookies'),
	path('aPropos/',views.aPropos, name='aPropos'),
	path('contacter/', views.contacter, name='contacter'),

	]