from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
	"""docstring for User"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	site_web = models.URLField(blank=True)
	signature = models.TextField(blank = True)
	inscrit_newsletter = models.BooleanField(default=False)
	def __str__(self):
		return "User de {0}".format(self.user.username)

class Plante(models.Model):
	InChIKey = models.CharField(max_length=1000)
	nom = models.CharField(max_length=1000)	
	molecule_name = models.CharField(max_length=1000,primary_key=True)
	published_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.nom

