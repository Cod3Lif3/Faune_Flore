from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.page_acceuil, name='page_acceuil'),
	path('condition',views.condition, name='condition'),
	]