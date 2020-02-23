from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Sujet(models.Model):
	#id_sujet = models.ForeignKey('self', on_delete=models.CASCADE)
	nom_commun = models.CharField(max_length=50)
	nom_scientifique = models.CharField(max_length=80)
	nom_espece = models.CharField(max_length=50)
	#id_alimentation = models.ForeignKey('Alimentation',on_delete=models.CASCADE)
	nom_compo = models.CharField(max_length=80)
	description =  models.TextField()
	environnement = models.TextField()
	published_date = models.DateTimeField(blank = True, null = True)


def publish(self):
	self.published_date = timezone.now()
	self.save()


def _str_(self):
	return self.nom_commun