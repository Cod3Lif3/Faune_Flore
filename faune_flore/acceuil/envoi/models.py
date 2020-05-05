from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Sujet(models.Model):
	#id_sujet = models.CharField(max_length=1000)#FA/FL+4L nom famille+3L environnement
	nom_commun = models.CharField(max_length=300)
	published_date = models.DateTimeField(default=timezone.now)

def __str__(self):
	return self.nom_commun

class Alimentation(models.Model):
	id_alimentation = models.CharField(max_length=7, primary_key=True, default='null')
	mode_alimentaire = models.CharField(max_length=20)


def __str__(self):
	return self.mode_alimentaire

class User(models.Model):
	"""docstring for User"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	site_web = models.URLField(blank=True)
	avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
	signature = models.TextField(blank = True)
	inscrit_newsletter = models.BooleanField(default=False)

	def __str__(self):
		return "User de {0}".format(self.user.username)
		

