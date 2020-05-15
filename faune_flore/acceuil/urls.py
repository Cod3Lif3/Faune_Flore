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
	path('plante/new/',views.plante_new, name='plante_new'),
	path('deconnexion/', views.deconnexion, name='deconnexion'),
	path('upload-csv/', views.sujet_upload, name='sujet_upload'),
	path('plante/<pk>/', views.plante_detail, name='plante_detail')

	]
